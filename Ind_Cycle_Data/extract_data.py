import glob 
import numpy as np 
import xlrd 
import pandas as pd
import xlsxwriter 
'''
Preliminary steps: 
    1) First, we downloaded all the files
    2) Then, we renamed them all with the .csv extension: ren *_ *_.csv
'''
#getting all filenames 
files = [f for f in glob.glob("**/*.csv", recursive = True)] 

final_data = np.zeros(shape = (1, 77))

#loading data from each file; getting second col; replacing last four vals with
#correct vals; transposing col; appending as new row

#initializing first 9 rows. We're doing this now because it looks like 
#there's a weird file ordering in the directory 
cycle_1 = np.loadtxt("P1_C1_.csv", delimiter = ",") 
cycle_1_col = cycle_1[:,1]
cycle_1_row = cycle_1_col.transpose() 
final_data[0] = cycle_1_row 

rows_till_nine = ["P1_C2_.csv","P1_C3_.csv","P1_C4_.csv","P1_C5_.csv","P1_C6_.csv","P1_C7_.csv","P1_C8_.csv","P1_C9_.csv"]

#building first nine rows
for name in rows_till_nine: 
    data = np.loadtxt(name, delimiter = ",")
    col = data[:,1]
    new_row = col.transpose()
    final_data = np.vstack([final_data, new_row])
    #np.append(final_data,[[new_row]], axis = 0) 

#building rows 10 - 42, which seems to be organized in folder in order 
for f in files:
    if (f not in rows_till_nine) and (f != "P1_C1_.csv"):
        data = np.loadtxt(f, delimiter = ",")
        col = data[:,1]
        new_row = col.transpose()
        final_data = np.vstack([final_data, new_row])
        #np.append(final_data,[[new_row]], axis = 0) 

#now we have to get SBP, DBP, MAP, and PP from Pressure_PWV.xlsx
#rearrange them in order of MAP, SBP, DBP, PP, and replace the 
#last 4 cols with these vals 

outputs = pd.read_excel(open('Pressure_PWV.xlsx', 'rb'))
outputs = outputs[['SBP','DBP','MAP','PP']]
pure_outputs = outputs.to_numpy()

SBP = pure_outputs[:,0]
DBP = pure_outputs[:,1]
MAP = pure_outputs[:,2]
PP = pure_outputs[:,3] 

final_data[:,73] = MAP
final_data[:,74] = SBP
final_data[:,75] = DBP
final_data[:,76] = PP


print(final_data)
#now we should have all the correct values in their correct places 
#we convert the numpy array to an xlsx file so that we can copy and
#paste into fullData

#final_data_frame = pd.DataFrame(final_data) 
#final_data_frame.to_excel("induced_BP.xlsx", index = False)

np.savetxt("Induced_BP.csv", final_data, delimiter = ',')

