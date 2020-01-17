import glob 
import numpy as np 

'''
Preliminary steps: 
    1) First, we downloaded all the files
    2) Then, we renamed them all with the .csv extension: ren *_ *_.csv
'''

#getting all filenames 
files = [f for f in glob.glob("**/*.csv", recursive = True)] 

final_data = np.zeros(shape = (1, 76))

#loading data from each file; getting second col; replacing last four vals with
#correct vals; transposing col; appending as new row

#initializing first 9 rows. We're doing this now because it looks like 
#there's a weird file ordering in the directory 
cycle_1 = np.loadtxt("P1_C1_.csv", delimiter = ",") 
cycle_1_col = cycle_1[:,1]
cycle_1_row = cycle_1_col.transpose() 
final_data[1] = cycle_1_row 

rows_till_nine = ["P1_C2_.csv","P1_C3_.csv","P1_C4_.csv","P1_C5_.csv","P1_C6_.csv","P1_C7_.csv","P1_C8_.csv","P1_C9_.csv"]

#building first nine rows
for name in first_rows: 
    data = np.loadtxt(name, delimiter = ",")
    col = dat[:,1]
    new_row = col.transpose()
    np.append(final_data,[[new_row]], axis = 0) 

#building rows 10 - 42, which seems to be organized in folder in order 
for f in files:
    if (f not in rows_till_nine) and (f != "P1_C1_.csv"):
        data = np.loadtxt(f, delimiter = ",")
        col = dat[:,1]
        new_row = col.transpose()
        np.append(final_data,[[new_row]], axis = 0) 

#now we have a 
    

