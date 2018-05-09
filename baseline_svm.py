# Imports
import numpy as np
from sklearn import svm,metrics

# CSV File Parsers
def parse_data(file_name):

    # Input: File Path
    # Outputs: Data Array

    with open(file_name, 'r') as f:        # Open File
        data = []
        for line in f:
            line = line.rstrip('\n')    # Remove new line characters
            line = line.split(',')        # Split line by ',' obtaining a list of strings as a result

            sample = [float(value) for value in line] # For each string in the list cast as a float
            
            data.append(sample)            # Add to Data array
        
    return np.array(data)                # Return data as Numpy Array


def parse_labels(file_name):

    with open(file_name, 'r') as f:            # Open File
        labels = [int(line.rstrip('\n')) for line in f]    # For each line in the file, 
                                                            # remove new line characters and cast the remaning string as an int
    return np.array(labels)


# Function to train the model
def train_model(data,labels,C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, max_iter=-1, decision_function_shape='ovr', random_state=None):
    
    model = svm.SVC(C=C, 
                    kernel=kernel,
                    degree=degree,
                    gamma=gamma,
                    coef0=coef0, 
                    shrinking=shrinking,
                    probability=probability,
                    tol=tol, 
                    cache_size=cache_size,
                    class_weight=class_weight,
                    max_iter=max_iter, 
                    decision_function_shape=decision_function_shape, 
                    random_state=random_state)

    model.fit(data,labels)  
                            
    return model

# Function to test the model
def test_model(data, labels, trained_model):
    predicted_labels = trained_model.predict(data)
    rounded_labels = np.clip(np.abs(np.round(predicted_labels)), 0, 1)
    f1 = metrics.precision_recall_fscore_support(labels,rounded_labels, labels=[0,1], average='macro')

    return f1, predicted_labels


def main():
    
    # Set file tuples
    train_files = ('features_MFCC_train.csv', 'labels_train.txt')
    dev_files = ('features_MFCC_dev.csv', 'labels_dev.txt')
    
    ## Load Data using Parsers
    
    # Training Data
    train_data = parse_data(train_files[0])
    train_labels = parse_labels(train_files[1])
    
    # Development Data
    dev_data = parse_data(dev_files[0])
    dev_labels = parse_labels(dev_files[1])
        
    # Train Model
    model = train_model(train_data, train_labels,
                        C=1.0, 
                        kernel='rbf', 
                        degree=3, 
                        gamma='auto', 
                        coef0=0.0, 
                        shrinking=True, 
                        probability=False, 
                        tol=0.001, 
                        cache_size=200, 
                        class_weight=None, 
                        max_iter=-1, 
                        decision_function_shape='ovr', 
                        random_state=None)
    
    # Get metrics for the development set
    f1, predicted_labels = test_model(dev_data, dev_labels, model)
    
    print("UAR:", f1[1])
    
    return
    
if __name__ == "__main__":
    main()
