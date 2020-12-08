# Software credits: Jonathan Uhler, Neo Liu, Xander Yee

"""
KerasPredictor.py

A simple neural network that predicts results based on patterns found in training data.
"""

# Import required libraries and APIs
from numpy import loadtxt # NumPy is a number/data processor
from keras.optimizers import SGD
from keras.models import Sequential # Keras is the AI/ML API. A Keras model is the entire network
from keras.layers import Dense # A layer is each set of nodes that make up the network


# =================================================================================================
# GLOBAL VARIABLES
# 
# Change here for easy access:
#
# Load in the data file using NumPy
dataCSV = 'banknote-authentication.csv'
dataSeperator = ','
# The number of input dimensions (the width of the input layer)
# inputDims = 4 # NOTE: this number should be 1 less than the total number of data points per row
outputDims = 10
#
# end: GLOBAL VARIABLES


# Read in and split the data elements by a seperator, both the input file and the delimiter are
# defined above.
dataset = loadtxt(dataCSV, delimiter = dataSeperator)

# Get the width for the input layer
inputDims = len(dataset[0]) - 1

# Split the data into two sets
# For n is the length of a row of data -- X dataset = 0:(n - 1), Y dataset = n
X = dataset[:,0:inputDims] # The X set houses a 2D array of all the data-data
Y = dataset[:,inputDims] # The Y set houses an array of all the "answers"


# Define the Keras model as being a sequential model
# A sequential model has a stack of layers where each layer has exactly 1 input tensor and 1 output tensor
model = Sequential()


# Build the layers of the networks
# =================================================================================================
# NETWORK SPECIFICATIONS:
#
# Input layer: inputDims nodes
# Hidden layer 1: (5 * inputDims) nodes, ReLU activation
# Hidden layer 2: (2 * inputDims) nodes, ReLU activation
# Output layer: outputDims node, softmax activation
#
model.add(Dense((inputDims * 5), input_dim = inputDims, activation = 'relu')) # "input_dim = ..." creates the input layer and
                                                                              # the rest of the line created the output layer
model.add(Dense((inputDims * 2), activation = 'relu')) # Hidden layer 2
model.add(Dense(outputDims, activation = 'softmax')) # Output layer
# end: Network


# Compiling the model
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


# Fit the model to the dataset (run the model for training)
model.fit(X, Y, epochs = 300, batch_size = 10)


# Let the model evaluate itself
_, accuracy = model.evaluate(X, Y)
print('Accuracy: %.2f' % (accuracy * 100))


# =================================================================================================
# def closest
#
# A function that returns the value from a list that is closest to an input value
#
# Arguments--
#
# lst:      the list of numbers to compare to the next arguments
#
# K:        the final number, this is what the list numbers are compared against
#
# Returns--
#
# result:   which of the numbers in the list was the closest
#
def closest(lst, K): 

    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
# end: def closest


# =================================================================================================
# def cleanUp
#
# A function that cleans up the elements of an array and makes them floating-point numbers
#
# Arguments--
#
# lst:      the list to clean up
#
# Returns--
#
# cleanedList: the cleaned list
#
def cleanUp(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].replace("[","")
        lst[i] = lst[i].replace("]","")

        lst[i] = float(lst[i])

    cleanedList = lst
    return cleanedList
# end: def cleanUp


prediction = model.predict(X)

# Go through all of the predictions for each of the X data examples
for i in range(len(prediction)):

    # Declare the expected result
    answer = Y[i]

    # For each prediction, there will be multiple results, so put them into a string
    predictionString = str(prediction[i])

    # Split that string up by spaces
    predictions = predictionString.split(" ")
    bestPred = 0

    # Call the cleanUp function to remove any extra characters from the list and make all
    # elements floats.
    cleanUp(predictions)

    # Find the closest prediction
    bestPred = closest(predictions, answer)

    # Print each of the test casses from the testing dataset
    print("Test case: " + str(i + 1))
    # Print the best prediction, the useful (or rounded) prediction, and the expected result
    print("Prediction (Actual): " + str(float(bestPred)) + " | Prediction (Useful): " + str(round(float(bestPred), 0)) + " | Expected: " + str(answer) + "\n")