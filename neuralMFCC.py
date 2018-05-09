# Imports

# Import numpy for arrays
import numpy as np
from math import isnan
# Keras Imports
from keras.models import Sequential            
from keras.layers import Dense, Activation, BatchNormalization, Dropout    # Layers
from keras import optimizers                # Optimization Algorithm

# Metrics Function
from sklearn.metrics import recall_score, precision_recall_fscore_support

####################################################################################################
# The following lines define the random seeds
# Using the same seeds allows the results to be reproducible at each run

import os
import random as rn
import tensorflow as tf
from keras import backend as K

os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
rn.seed(12345)
session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
tf.set_random_seed(1234)
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.set_session(sess)

####################################################################################################

# Library to be used to plot the training history
import matplotlib.pyplot as plt

# CSV File Parsers
def parse_data(file_name):
    # Input: File Path
    # Outputs: Data Array

    with open(file_name, 'r') as f:        # Open File
        data = []
        for line in f:
            line = line.rstrip('\n')    # Remove new line characters
            line = line.split(',') # Split line by ',' obtaining a list of strings as a result

            sample = []
            for value in line:
                fv = float(value)
                if isnan(fv):
                    for i in range(0,13):
                        sample.append(0)
                else:
                    sample.append(fv)
                   
            data.append(sample)            # Add to Data array

    return np.array(data)                # Return data as Numpy Array



def parse_labels(file_name):

    with open(file_name, 'r') as f:            # Open File
        labels = [int(line.rstrip('\n')) for line in f]    # For each line in the file, 
                                                            # remove new line characters and cast the remaning string as an int
    return np.array(labels)

## Model Initialization Functions
def build_model(input_shape, learning_rate=0.01):

    # This function receives as inputs
    # input_shape: shape of the training data
    # learning_rate (default 0.01)

    # Keras models are commonly initialized as Sequential
    # This serves as a placeholder for the layers in the model
    model = Sequential()                                
        
    # Fully Connected or Dense Layer receives as input the number of hidden units
    model.add(Dense(20, input_shape=(input_shape[1],))) 
    model.add(BatchNormalization()) 
    
    # The first layer in the model it needs to receive the input shape
    # For feature vectors the input shape can be defined as (number_of_features,)
    # The empty slot after number_of_features denotes that the size of the batch will be defined later    
    model.add(Activation('relu'))    # Second Activation Layer

    model.add(Dropout(0.5))

    model.add(Dense(10))            # Second Dense Layer
    model.add(BatchNormalization()) 

    model.add(Activation('relu'))    # Second Activation Layer
    
    # Output Layer
    # This layer will have as many outputs/units as there are classes in the model
    model.add(Dropout(0.5))

    model.add(Dense(1))
    
    # Output Activation Layer: Usually a Sigmoid like function, because it is bounded between 0 and 1
    model.add(Activation('sigmoid'))
    
    # Optimizer and Parameters
    rmsprop = optimizers.RMSprop(learning_rate, rho=0.9, epsilon=None, decay=0)
    
    # The Optimization algorithms need parameters:
    # - learning rate (lr)
    # - weight decay  (wd)
    # Each individual optimization algorithm has its own set of unique parameters(besides the lr and wd), these can be changed
    # but their default values will work well for most applications
    
    # To complete the model, we need to compile it, indicate the optimizer, 
    # the loss function and a set of metrics we may want to get
    
    model.compile(optimizer=rmsprop, 
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
                  
    return model

# Function to train the model
def train_model(train, dev, learning_rate=0.01, n_epochs=100, batch_size=500):
    
    ###
    # Inputs:
    # -train: (train_data, train_labels)
    # -dev: (dev_data, dev_labels)
    # -learning_rate: (default 0.01)
    # -n_epochs: Number of epochs (default 100)
    # -batch_size: Number of samples per training batch (default 500)
    #
    # Outputs: Trained Model, Training History
    ###
    
    # Load Data
    data = train[0]
    labels = train[1]
    
    dev_data = dev[0]
    dev_labels = dev[1]
    
    ## Train Model
    model = build_model(data.shape, learning_rate)
    
    # To train the model we use model.fit()
    # This method receives as input:
    # - training data and labels
    # - validation data and labels(optional)
    # - number of epochs
    # - batch size
    # It outputs the "history", which contains the evolution of the loss function and metrics after each epoch
    
    history = model.fit(data, labels, 
                        validation_data=(dev_data, dev_labels),
                        epochs=n_epochs, 
                        batch_size=batch_size)
                            
    return model, history

# Function to test the model
def test_model(data, labels, trained_model):
    
    ### 
    # Inputs:
    # -data: Test Data
    # -labels: Labels
    # -trained_model: Model previously trained
    #
    # Outputs: Predicted Labels Loss, (Precision, Recall, F1 Score, Support), Predicted Labels
    ###
    
    # To obtain the loss over the test data we can use the method model.evaluate(test_data, test_labels)
    loss = trained_model.evaluate(data, labels)
    
    # To obtain predictions over the test data we can use model.predict(test_data)
    predicted_labels = trained_model.predict(data)
    
    # The predicted labels will be values between 0 and 1, as a result of the output activation function
    # If we want to compute metrics on the labels we need to round them to 0 and 1
    rounded_labels = np.clip(np.abs(np.round(predicted_labels)), 0, 1)
    
    # This function outputs a set of metrics to evaluate classification results
    # It gets as inputs the labels, the predicted(now rounded) labels, the set of possible labels [0,1]
    # It can compute the metrics for each class individually, or average them, using average='macro'
    # The output of the function includes(in order): Precision, Recall, F1 Score and Support (number of 0s/1s in the original labels)
    f1 = precision_recall_fscore_support(labels, rounded_labels, labels=[0,1], average='macro')
    
    return loss, f1, predicted_labels

## Plots MSE evolution for the Training and Development Data Sets
def display_train_history(history):
    
    # Displays the training history
    # Inputs: history
    
    fig = plt.figure(0)                                            # Select Figure 0
    fig.canvas.set_window_title('BCE')                            # Set window title: Binary Crossentropy
    t, = plt.plot(history.history['loss'], label='Train')        # Plot Train Data loss evolution
    d, = plt.plot(history.history['val_loss'], label='Devel')    # Plot Validation Data loss evolution
    plt.legend(handles=[t, d])                                    # Set legend

    fig = plt.figure(1)                                            # Select Figure 1    
    fig.canvas.set_window_title('ACC')                            # Set window title: Accuracy
    t, = plt.plot(history.history['acc'], label='Train')        # Plot Training Data Accuracy
    d, = plt.plot(history.history['val_acc'], label='Devel')    # Plot Validation Data Accuracy
    plt.legend(handles=[t, d])                                    # Set legend
    
    plt.show()    # Display Plot

def main():
    
    # Set file tuples
    train_files = ('MFCC/train_converted.csv', 'labels_train.txt')
    dev_files = ('MFCC/dev_converted.csv', 'labels_dev.txt')
    
    ## Load Data using Parsers
    
    # Training Data
        
    train_data = parse_data(train_files[0])

    train_labels = parse_labels(train_files[1])
    
    # Development Data
    dev_data = parse_data(dev_files[0])
    dev_labels = parse_labels(dev_files[1])
    
    # Set Training Parameters
    learning_rate =  0.0205
    epochs = 50
    batch_size = 1000
    
    # Train Model
    model, history = train_model((train_data, train_labels), (dev_data, dev_labels), learning_rate, epochs, batch_size)
    
    # Display Training History
    display_train_history(history)
    
    # Get metrics for the development set
    loss, f1, predicted_labels = test_model(dev_data, dev_labels, model)
    
    print("Loss:", loss)
    print("UAR:", f1[1])
    
    return
    
if __name__ == "__main__":
    main()
