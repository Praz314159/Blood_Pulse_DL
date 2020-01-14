from keras import models 
from keras import layers 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_excel(open('Features_fulldata.xlsx', 'rb')) 
data.astype('float64').dtypes #homogenizing data type 
pure_data = data.to_numpy() #converting to numpy array

output_1 = pure_data[:,74]  
output_2 = pure_data[:,75]
output_3 = pure_data[:,76]
output_4 = pure_data[:,77] 

#first, we want to load our data and split it into (training data, training labels) and 
#(test data, test labels) --> these are randomly selected 

pure_data = pure_data[:,:74]

train_data, test_data, train_targets, test_targets = train_test_split(pure_data, output_1, test_size =0.2)

'''
train_data = np.asarray(train_data)
train_targets = np.asarray(train_targets)
test_data = np.asarray(test_data)
test_targets = np.asarray(test_targets)
pure_data = np.asarray(pure_data)
'''

print("TRAINING DATA SHAPE: ", train_data.shape, "|TESTING DATA SHAPE: ", test_data.shape)
print("TRAINING TARGETS SHAPE: ", train_targets.shape, "|TESTING TARGETS SHAPE: ", test_targets.shape)

#Assuming we already have the training data, we normalize it. 

mean = train_data.mean(axis = 0)
#print("MEAN SHAPE: ", mean.shape, "|TRAIN DATA SHAPE: ", train_data.shape, "|TEST SHAPE: ", test_data.shape) 
#print("TRAIN DATA: ", train_data)
train_data -= mean
std = train_data.std(axis = 0) 
train_data /= std 

test_data -= mean
test_data /= std 

#building model 

def build_model(): 
    model = models.Sequential()
    model.add(layers.Dense(74, activation = 'relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(50, activation = 'relu')) #hidden layer
    model.add(layers.Dense(1)) 
    model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['mae'])

    return model 

#Preparing validation data --> k-fold validation 
k = 4
num_val_samples = len(train_data) // k
num_epochs = 100 
#all_scores = [] 
all_mae_histories = []

for i in range(k): 
    print("processing fold #", i) 
    val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
    val_targets = train_targets[i*num_val_samples: (i+1)*num_val_samples]

    partial_train_data = np.concatenate([train_data[:i*num_val_samples], \
            train_data[(i+1)*num_val_samples:]], axis = 0) 
    partial_train_targets = np.concatenate([train_targets[:i*num_val_samples],\
            train_targets[(i+1)*num_val_samples:]], axis = 0)

    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets, epochs = num_epochs, batch_size = 1, \
            verbose = 0)
    #val_mse, val_mae = model.evaluate(val_data, val_targets, verbose = 0) 
    #all_scores.append(val_mae)
    #print("HISTORY KEYS: ", history.history.keys())
    mae_history = history.history['mae'] 
    all_mae_histories.append(mae_history) 


average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]

plt.plot(range(1, len(average_mae_history) + 1), average_mae_history) 
plt.xlabel('Epochs') 
plt.ylabel('Validation MAE') 
plt.show() 
