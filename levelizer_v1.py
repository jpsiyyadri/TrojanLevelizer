import time
import xlrd
import xlwt
import sys

start = time.time()
file_name = "c432countertrojan.xlsx"
def get_sheet(file_source_name):
    book = xlrd.open_workbook(file_source_name)
    sheet_0 = book.sheet_by_index(0)
    return sheet_0

sheet_0 = get_sheet(file_name)
sheet_nets_0 = get_sheet("c432netsreport.xlsx")
sheet_combinationaltroj_nets_0 = get_sheet("c432sequentialtrojannetsreport.xlsx")
sheet_power_0 = get_sheet("c432gcpowerreport.xlsx")
sheet_combinationaltroj_power_0 = get_sheet("c432sequentialtrojanpowerreport.xlsx")

def get_list(sheet_, col_):
    rows = sheet_.nrows
    list_ = []
    for row_index in range(5, rows): # this condition checks are there any non visited rows?
        row_dict = {}
        for i in range(0, len(col_)-1):
            row_dict[col_[i]] = sheet_.cell_value(rowx=row_index, colx=i)
        if(row_dict[col_[0]]!=''):
            list_.append(row_dict)
    return list_

# compare these two file and print non existed nets and count param change for existed net
def find_non_existed(list_1, list_2):
    dict_ = {}
    non_existed_list = []
    defective = False
    for row_1 in list_1:
        non_existed = True
        for row_2 in list_2:
            if(row_1['net'] == row_2['net']):
                non_existed = False
                param_change = 0
                for  k,v in row_1.items():
                    if(row_2[k]!=v):
                        param_change += 1
                dict_[row_1['net']] = param_change
                break
        if(non_existed):
            defective = True
            non_existed_list.append(row_1['net'])
            # print("non existed {0}".format(row_1['net']))
    return dict_, non_existed_list
set_param_change_list = []
set_non_existed_list = []
def unique(list1): 
    # intilize a null list 
    unique_list = [] 
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
    return unique_list

def get_attribute_dict(normal_list, trojan_list):
    # print("normal list {0}".format(normal_list))
    # print("trojan list {0}".format(trojan_list))
    dict_, non_existed_list_1 = find_non_existed(normal_list, trojan_list)
    dict_1, non_existed_list_2 = find_non_existed(trojan_list, normal_list)
    set_non_existed_list.append(unique(non_existed_list_1 + non_existed_list_2))
    list_change_nets = []
    for k,v in dict_.items():
        if(v>0):
            # print("param change net {0}".format(k))
            list_change_nets.append(k)
    for k,v in dict_1.items():
        if(v>0):
            # print("param change net {0}".format(k))
            list_change_nets.append(k)
    # print("param change list {0}".format(set(list_change_nets)))
    set_param_change_list.append(list_change_nets)
    return dict_

list_nets = get_list(
                        sheet_nets_0, [
                                        'net', 'fanout', 'fanin',
                                        'load', 'resistance', 'pins', 'attributes'
                                    ]
                    )

list_trojan_nets = get_list(
                                sheet_combinationaltroj_nets_0, [
                                                                    'net', 'fanout', 'fanin',
                                                                    'load', 'resistance', 'pins',
                                                                    'attributes'
                                                                ]
                            )

list_power = get_list(
                        sheet_power_0, [
                                        'net', 'net load', 'prob',
                                        'rate', 'power'
                                    ]
                    )

list_trojan_power = get_list(
                                sheet_combinationaltroj_power_0, [
                                                        'net', 'net load', 'prob',
                                                        'rate', 'power'
                                                    ]
                            )

the_attributes_of_net = get_attribute_dict(list_nets, list_trojan_nets)
the_attributes_of_power = get_attribute_dict(list_power, list_trojan_power)

set_param_change_list = [value for value in set_param_change_list[0] if value in set_param_change_list[1]]

present_in_param_change = set(set_param_change_list)
present_in_existed = set(set_non_existed_list[0]+set_non_existed_list[1])
if(len(present_in_existed)>0 | len(present_in_param_change)>0):
    print("------ defective circuit -----------")
if(len(present_in_existed)>0):
    print("param change nets {0}".format(present_in_existed))
if(len(present_in_param_change)>0):
    print("non existed nets {0}".format(present_in_param_change))

all_n_values = {}
all_n_counts = {}

inputs = sheet_0.cell_value(rowx=1, colx=0).split(',')
primary_inputs = {}
for elem in inputs:
    primary_inputs[elem] = 0
all_n_values = primary_inputs

outputs = sheet_0.cell_value(rowx=1, colx=1).split(',')
primary_outputs = {}
for elem in outputs:
    primary_outputs[elem] = -1

for k,v in primary_outputs.items():
    if(k not in all_n_values.keys()):
        all_n_values[k] = v

def count_n(intermed_n):
    if(intermed_n in all_n_counts.keys()):
        all_n_counts[intermed_n] += 1
    else:
        all_n_counts[intermed_n] = 1

# takes list of N's and return the calculated value
def formulae(gate_inputs):
    gate_inputs_values = [all_n_values[elem] for elem in gate_inputs]
    return (max(gate_inputs_values) + 1)

# takes list of N's if we have every N value in all_n_values then it returns True
def all_exists(gate_inputs):
    for elem in gate_inputs:
        count_n(elem)
        if(elem not in all_n_values.keys()):
            all_n_values[elem] = 0
    return True

rows = sheet_0.nrows # all rows in excel except first 3 rows as they are occupied for inputs and outputs 202
last_column = sheet_0.ncols -1
middle_outputs = {}
non_visited_index = [i for i in range(3, rows)] # initially we have all indexes needs to be visited [3,4,5,..,201]
                                                # finally non_visited_index becomes [] 

while(len(non_visited_index) > 0): # this condition checks are there any non visited rows?
    # non visited rows are there
    visited_index = []
    for row_index in non_visited_index: # visit non visited row indexes
        # for each row at last column we have operands N1,N5 it stores in gate_inputs
        gate_inputs = sheet_0.cell_value(rowx=row_index, colx=last_column).split(',')
        intermed_n = sheet_0.cell_value(rowx=row_index, colx=2).split(",")
        # print(row_index)
        if(all_exists(gate_inputs)):
            calc_val = formulae(gate_inputs)
            for x in intermed_n:
                middle_outputs[x] = calc_val
                all_n_values[x] = calc_val
            visited_index.append(row_index)
    for v_index in visited_index:
        non_visited_index.remove(v_index)
            
for p_o in primary_outputs:
    count_n(p_o)

pi_level = 0
po_level = max(all_n_values.values())
final_output = {}
for n_val,net_val in all_n_values.items():
    final_output[n_val] = {'pi':net_val - pi_level, 'po':po_level - net_val}
excel_output = []

book = xlwt.Workbook()
i = 0
sheet1 = book.add_sheet('Sheet 1')

sheet1.write(i, 0, 'nets')
sheet1.write(i, 1, 'level')
sheet1.write(i, 2, 'connectivity')
sheet1.write(i, 3, 'pi')
sheet1.write(i, 4, 'po')
sheet1.write(i, 5, 'score')
sheet1.write(i, 6, 'strategy pay off 1')
sheet1.write(i, 7, 'strategy pay off 2')
sheet1.write(i, 8, 'strategy pay off 3')
sheet1.write(i,9,'lowest allowable fine')

i += 1
max_score = 0
min_score = sys.maxsize
for key, value in all_n_counts.items():
    # print(key, value)
    sheet1.write(i, 0, key)
    sheet1.write(i, 1, all_n_values[key])
    sheet1.write(i, 2, value)
    sheet1.write(i, 3, final_output[key]['pi'])
    sheet1.write(i, 4, final_output[key]['po'])
    score = value + all_n_values[key]+final_output[key]['pi']+final_output[key]['po']
    if(key in the_attributes_of_net.keys()):
        score += the_attributes_of_net[key]
    if(key in the_attributes_of_power.keys()):
        score += the_attributes_of_power[key]
    # to-do:  add the_attribute_net['net'] + the_attribute_power['net load']
    # print('{0} {1} {2}'.format(score, min_score, max_score))
    if(score < min_score):
        min_score = score
    if(score > max_score):
        max_score = score
    sheet1.write(i, 5, score)
    i += 1
div_n = 3
mid_score = (max_score - min_score) // div_n
x = min_score+mid_score
y = x + mid_score
z = y + mid_score
sheet1.write(1, 6, x)
sheet1.write(1, 7, y)
sheet1.write(1, 8, z)
sheet1.write(1,9,min_score)
book.save(file_name.split('.')[0]+"_score.xls") # maybe can only write .xls format
end = time.time()
print(end - start)
