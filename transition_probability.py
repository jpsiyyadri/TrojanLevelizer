import xlrd
import numpy as np
import random
import xlsxwriter
#readng the input file
book = xlrd.open_workbook("C432.xlsx")

#opening the workbook
#workbook=xlsxwriter.workbook('/home/desktop/fullscoap/storing_workbook.xlsx')
#data1=workbook.add_worksheet('data')


#settng the pointer to first cell
first_sheet = book.sheet_by_index(0)

no_of_inputs = 36
no_of_outputs = 7
no_of_rows=162
no_of_gates=160

primary_inputs = []
primary_outputs = []
input1=[]
input2=[]
input3=[]
input4=[]
input5=[]
input6=[]
input7=[]
input8=[]
input9=[]
input10=[]
output=[]
gates=[]
non_primary=[]
net=[]
transition_prob=[]

def tp0_not(tp0_inp1,tp1_inp1):
      tp0_output=tp1_inp1
      return(tp0_output)
def tp1_not(tp0_inp1,tp1_inp1):
      tp1_output=tp0_inp1
      return(tp1_output)

def tp0_buff(tp0_inp1,tp1_inp1):
      tp0_output=tp0_inp1
      return(tp0_output)
def tp1_buff(tp0_inp1,tp1_inp1):
      tp1_output=tp1_inp1
      return(tp1_output)

#MAIN FUNCTN FOR 2_INPUT for transition probability
def tp_2(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2):
      for i in range(0,len_gates,1):
            if (gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2
                  return(tp0_output)
            elif gates[i]=="and":
                  tp0_output=1-(tp1_inp1*tp1_inp2)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2)+(tp1_inp1*tp1_inp2)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2)+(tp1_inp1*tp1_inp2))
                  return(tp0_output)

#MAIN FUNCTN FOR 3_INPUT for transition probability
def tp_3(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3)+(tp1_inp1*tp1_inp2*tp1_inp3))
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp1_output=1-((tp0_inp1*tp0_inp2*tp0_inp3)+(tp1_inp1*tp1_inp2*tp1_inp3))
                  return(tp0_output)

#MAIN FUNCTN FOR 4_INPUT for transition probability
def tp_4(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4))
                  return(tp0_output)

def tp_5(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5))
                  return(tp0_output)
def tp_6(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5,tp0_inp6,tp1_inp6):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6))
                  return(tp0_output)

def tp_7(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5,tp0_inp6,tp1_inp6,tp0_inp7,tp1_inp7):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7))
                  return(tp0_output)

def tp_8(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5,tp0_inp6,tp1_inp6,tp0_inp7,tp1_inp7,tp0_inp8,tp1_inp8):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8))
                  return(tp0_output)

def tp_9(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5,tp0_inp6,tp1_inp6,tp0_inp7,tp1_inp7,tp0_inp8,tp1_inp8,tp0_inp9,tp1_inp9):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp89)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9))
                  return(tp0_output)

def tp_10(tp0_inp1,tp1_inp1,tp0_inp2,tp1_inp2,tp0_inp3,tp1_inp3,tp0_inp4,tp1_inp4,tp0_inp5,tp1_inp5,tp0_inp6,tp1_inp6,tp0_inp7,tp1_inp7,tp0_inp8,tp1_inp8,tp0_inp9,tp1_inp9,tp0_inp10,tp1_inp10):
      for i in range(0,len_gates,1):
            if(gates[i]=="nand"):
                  tp0_output=tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9*tp1_inp10
                  return(tp0_output)
            elif(gates[i]=="and"):
                  tp0_output=1-(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9*tp1_inp10)
                  return(tp0_output)
            elif(gates[i]=="or"):
                  tp0_output=tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9*tp0_inp10
                  return(tp0_output)
            elif(gates[i]=="nor"):
                  tp0_output=1-(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9*tp0_inp10)
                  return(tp0_output)
            elif(gates[i]=="xor"):
                  tp0_output=(tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9*tp0_inp10)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9*tp1_inp10)
                  return(tp0_output)
            elif(gates[i]=="xnor"):
                  tp0_output=1-((tp0_inp1*tp0_inp2*tp0_inp3*tp0_inp4*tp0_inp5*tp0_inp6*tp0_inp7*tp0_inp8*tp0_inp9*tp0_inp10)+(tp1_inp1*tp1_inp2*tp1_inp3*tp1_inp4*tp1_inp5*tp1_inp6*tp1_inp7*tp1_inp8*tp1_inp9*tp1_inp10))
                  return(tp0_output)


#readng the primary nets from file
for i in range(2,2*no_of_inputs,1):
      inp=first_sheet._cell_values[0][i]
      primary_inputs.append(inp)

for i in range(2,2*no_of_outputs,1):
    inp = first_sheet._cell_values[1][i]
    primary_outputs.append(inp)

print("primary-inputs")
print(primary_inputs)
print("primary-outputs")
print(primary_outputs)

#readng the non primary nets
for i in range(2,no_of_rows,1):
      oup=first_sheet._cell_values[i][3]
      output.append(oup)

for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][4]
      input1.append(inp)


for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][5]
      input2.append(inp)

for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][6]
      input3.append(inp)

for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][7]
      input4.append(inp)

for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][8]
      input5.append(inp)
      
for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][9]
      input6.append(inp)
      
for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][10]
      input7.append(inp)
      
for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][11]
      input8.append(inp)
      
for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][12]
      input9.append(inp)
      
for i in range(2,no_of_rows,1):
      inp=first_sheet._cell_values[i][13]
      input10.append(inp)
	  
for i in range(2,no_of_rows,1):
      gat=first_sheet._cell_values[i][2]
      gates.append(gat)

len_gates=len(gates);
len_input1=len(input1)
len_input2=len(input2)
len_input3=len(input3)
len_input4=len(input4)
len_input5=len(input5)
len_input6=len(input6)
len_input7=len(input7)
len_input8=len(input8)
len_input9=len(input9)
len_input10=len(input10)
len_output=len(output)
len_primaryinputs=len(primary_inputs)
len_primaryoutputs=len(primary_outputs)

#isolatng non_prmary net
for i in input1:
      if( (i not in primary_inputs )and (i not in primary_outputs) and (i not in non_primary)):
          non_primary.append(i)

for i in input2:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)

for i in input3:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)

for i in input4:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)

for i in input5:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)
          
for i in input6:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)
          
for i in input7:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)
          
for i in input8:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)
          
for i in input9:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)
          
for i in input10:
      if( (i not in primary_inputs )and (i not in primary_outputs)and (i not in non_primary)):
          non_primary.append(i)

for i in output:
      if( (i not in primary_inputs )and (i not in primary_outputs) and (i not in non_primary)):
          non_primary.append(i)
print("non_prmary_nets")
print(non_primary)


for i in primary_inputs:
      net.append(i)
for i in non_primary:
      net.append(i)
for i in primary_outputs:
      net.append(i)
print("net")
print(net)

len_net=len(net)
print("length_net")
print(len_net)

#declaration of tp0 and tp1 lists
tp0=[0]*len_primaryinputs
print("tp0")
print(tp0)
tp1=[0]*len_primaryinputs
print("tp1")
print(tp1)
#initializing tp0 and tp1 lists
for i in range(0,len_primaryinputs,1):
      if(net[i] in primary_inputs):
            tp0[i]=0.5
            tp1[i]=0.5
      
print("net")
print(net)
print("tp0")
print(tp0)
print("tp1")
print(tp1)

#computing of the transition probability

for i in range(0,len_gates,1):
    if(gates[i]=="not" and input2[i]=="" and input3[i]=="" and input4[i]=="" and input5[i]=="" and input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp=j
            elif(input2[i]==net[j]):
                index_inp=j
            elif(input3[i]==net[j]):
                index_inp=j
            elif(input4[i]==net[j]):
                index_inp=j
            elif(input5[i]==net[j]):
                index_inp=j
            elif(input6[i]==net[j]):
                index_inp=j
            elif(input7[i]==net[j]):
                index_inp=j
            elif(input8[i]==net[j]):
                index_inp=j
            elif(input9[i]==net[j]):
                index_inp=j
            elif(input10[i]==net[j]):
                index_inp=j
            elif(output[i]==net[j]):
                index_output=j
        tp0[index_output]=tp0_not(tp0[index_inp],tp1[index_inp])
        tp1[index_output]=tp1_not(tp0[index_inp],tp1[index_inp])
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]
        
    elif(gates[i]=="buff" and input2[i]=="" and input3[i]=="" and input4[i]=="" and input5[i]=="" and input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp=j
            elif(input2[i]==net[j]):
                index_inp=j
            elif(input3[i]==net[j]):
                index_inp=j
            elif(input4[i]==net[j]):
                index_inp=j
            elif(input5[i]==net[j]):
                index_inp=j
            elif(input6[i]==net[j]):
                index_inp=j
            elif(input7[i]==net[j]):
                index_inp=j
            elif(input8[i]==net[j]):
                index_inp=j
            elif(input9[i]==net[j]):
                index_inp=j
            elif(input10[i]==net[j]):
                index_inp=j
            elif(output[i]==net[j]):
                index_output=j
        tp0[index_output]=tp0_buff(tp0[index_inp],tp1[index_inp])
        tp1[index_output]=tp1_buff(tp0[index_inp],tp1[index_inp])
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]
        

    elif(input3[i]=="" and input4[i]=="" and input5[i]=="" and input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==""):
                index_inp3=""
            if(input4[i]==""):
                index_inp4=""
            if(input5[i]==""):
                index_inp5=""
            if(input6[i]==""):
                index_inp6=""
            if (input7[i]==""):
                index_inp7=""
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_2(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]
    elif(input4[i]=="" and input5[i]=="" and input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==""):
                index_inp4=""
            if(input5[i]==""):
                index_inp5=""
            if(input6[i]==""):
                index_inp6=""
            if (input7[i]==""):
                index_inp7=""
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_3(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]
    elif(input5[i]=="" and input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
               index_inp3=j
            if(input4[i]==net[j]):
               index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==""):
                index_inp6=""
            if (input7[i]==""):
                index_inp7=""
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_4(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    elif(input6[i]=="" and input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
               index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==""):
                index_inp6=""
            if (input7[i]==""):
                index_inp7=""
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_5(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    elif(input7[i]=="" and input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
                index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==net[j]):
                index_inp6=j
            if (input7[i]==""):
                index_inp7=""
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_6(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5],tp0[index_inp6],tp1[index_inp6])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    elif(input8[i]=="" and input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
                index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==net[j]):
                index_inp6=j
            if (input7[i]==net[j]):
                index_inp7=j
            if (input8[i]==""):
                index_inp8=""
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_7(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5],tp0[index_inp6],tp1[index_inp6],tp0[index_inp7],tp1[index_inp7])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    elif(input9[i]=="" and input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
               index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==net[j]):
                index_inp6=j
            if (input7[i]==net[j]):
                index_inp7=j
            if (input8[i]==net[j]):
                index_inp8=j
            if (input9[i]==""):
                index_inp9=""
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_8(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5],tp0[index_inp6],tp1[index_inp6],tp0[index_inp7],tp1[index_inp7],tp0[index_inp8],tp1[index_inp8])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    elif(input10[i]==""):
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
                index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==net[j]):
                index_inp6=j
            if (input7[i]==net[j]):
                index_inp7=j
            if (input8[i]==net[j]):
                index_inp8=j
            if (input9[i]==net[j]):
                index_inp9=j
            if (input10[i]==""):
                index_inp10=""
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_9(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5],tp0[index_inp6],tp1[index_inp6],tp0[index_inp7],tp1[index_inp7],tp0[index_inp8],tp1[index_inp8],tp0[index_inp9],tp1[index_inp9])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]

    else:
        for j in range(0,len_net,1):
            if(input1[i]==net[j]):
                index_inp1=j
            if(input2[i]==net[j]):
                index_inp2=j
            if(input3[i]==net[j]):
                index_inp3=j
            if(input4[i]==net[j]):
                index_inp4=j
            if(input5[i]==net[j]):
                index_inp5=j
            if(input6[i]==net[j]):
                index_inp6=j
            if (input7[i]==net[j]):
                index_inp7=j
            if (input8[i]==net[j]):
                index_inp8=j
            if (input9[i]==net[j]):
                index_inp9=j
            if (input10[i]==net[j]):
                index_inp10=j
            if(output[i]==net[j]):
                index_output=j
#calling the function for 2 input for controllability
        tp0[index_output]=tp_10(tp0[index_inp1],tp1[index_inp1],tp0[index_inp2],tp1[index_inp2],tp0[index_inp3],tp1[index_inp3],tp0[index_inp4],tp1[index_inp4],tp0[index_inp5],tp1[index_inp5],tp0[index_inp6],tp1[index_inp6],tp0[index_inp7],tp1[index_inp7],tp0[index_inp8],tp1[index_inp8],tp0[index_inp9],tp1[index_inp9],tp0[index_inp10],tp1[index_inp10])
        tp1[index_output]=1-tp0[index_output]
        transition_prob[index_output]=tp0[index_output]*tp1[index_output]
print("tpo")
print(tp0)
print("tp1")
print(tp1)
print("tp1")
print("tp")
print(tp)
