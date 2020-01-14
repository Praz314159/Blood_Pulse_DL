from keras.datasets import boston_housing 

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
mean = train_data.mean(axis = 0) 
print("TRAIN DATA SHAPE: ", train_data.shape, "|MEAN SHAPE: ", mean.shape) 
train_data -= mean
