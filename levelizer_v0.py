import time
import xlrd
import xlwt
import sys

start = time.time()
file_name = "s27combotroj.xlsx"
book = xlrd.open_workbook(file_name)
sheet_0 = book.sheet_by_index(0)

# load nets.xlsx and load combinationaltroj_nets.xlsx
file_name_nets = "s27nets.xlsx"
book_nets = xlrd.open_workbook(file_name_nets)
sheet_nets_0 = book_nets.sheet_by_index(0)

file_name_combinationaltroj_nets = "s27combinationaltrojan_nets.xlsx"
book_combinationaltroj_nets = xlrd.open_workbook(file_name_combinationaltroj_nets)
sheet_combinationaltroj_nets_0 = book_combinationaltroj_nets.sheet_by_index(0)
# compare these two file and print non existed nets and count param change for existed net
sheet_rows = book_combinationaltroj_nets.rows()
sheet_columns = book_combinationaltroj_nets.columns()
# variables: the_attributes_of_net -> stores param change count

# load power.xlsx and load combinationaltroj_power.xlsx
file_name_power = "s27power.xlsx"
book_nets = xlrd.open_workbook(file_name_power)
sheet_nets_0 = book_nets.sheet_by_index(0)

file_name_combinationaltroj_power = "s27combinationaltrojan_power.xlsx"
book_combinationaltroj_power = xlrd.open_workbook(file_name_combinationaltroj_power)
sheet_combinationaltroj_power_0 = book_combinationaltroj_power.sheet_by_index(0)
# compare these two files and print non existed new and count param chhange for existed new
# variables: the_attributes_of_power -> stores param change count



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
        intermed_n = sheet_0.cell_value(rowx=row_index, colx=2)
        # print(row_index)
        if(all_exists(gate_inputs)):
            calc_val = formulae(gate_inputs)
            middle_outputs[intermed_n] = calc_val
            all_n_values[intermed_n] = calc_val
            visited_index.append(row_index)
    for v_index in visited_index:
        non_visited_index.remove(v_index)
            
for p_o in primary_outputs:
    count_n(p_o)

# for k in all_n_values.keys():
#     if(k not in all_n_counts.keys()):
#         print(k+' not there in all_n_counts')
# for k in all_n_counts.keys():
#     if(k not in all_n_values.keys()):
#         print(k+' not there in all_n_values')

# for k,v in all_n_values.items():
#     if(k in primary_outputs.keys()):
#         primary_outputs[k] = v
# print('po {0} '.format(primary_outputs.keys()))
# print('anv {0} '.format(all_n_values.keys()))
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