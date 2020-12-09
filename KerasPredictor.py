# Software credits: Jonathan Uhler, Neo Liu, Xander Yee

"""
KerasPredictor.py

A simple neural network that predicts results based on patterns found in training data.
"""

# Import required libraries and APIs
from numpy import loadtxt # NumPy is a number/data processor
from keras.models import Sequential # Keras is the AI/ML API. A Keras model is the entire network
from keras.layers.core import Dense # A layer is each set of nodes that make up the network
import matplotlib.pyplot as plt # MatPlotLib is the library used to visualize the data
import json # JSON library is used to read config data from a config file


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
    cleanedList = lst.tolist()

    return cleanedList
# end: def cleanUp


# =================================================================================================
# GLOBAL VARIABLES
# To change these config values, go to "PredictorConfig.json"
#
with open('PredictorConfig.json') as PredictorConfigData:
    data = json.load(PredictorConfigData)
#
data = data['configData']
#
dataCSV = data[0] # --> The input with with data for training and testing
dataSeperator = data[1] # --> The character that seperates data elements in the input file
outputDims = data[2] # --> The width of the output layer
visualizer = data[3] # --> The toggle for whether or not a graph is displayed when the NN finishes
debug = data[4] # --> The toggle for the debug messages
#       data[5] --> used later as the location of the inference data file
#       data[6] --> used later as the number of epochs
saveModel = data[7] # --> The toggle for whether or not the trained model will be saved
#
print("dataCSV: " + str(dataCSV) + "\ndataSeperator: " + str(dataSeperator) + "\noutputDims: " + str(outputDims) + "\nvisualizer: " + str(visualizer) + "\ndebug: " + str(debug) + "\nsaveModel: " + str(saveModel) + "\n")
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
model.add(Dense((inputDims * 4), input_dim = inputDims, activation = 'relu')) # "input_dim = ..." creates the input layer and
                                                                              # the rest of the line created the output layer
model.add(Dense((inputDims * 3), activation = 'relu')) # Hidden layer 2
model.add(Dense(outputDims, activation = 'softmax')) # Output layer
# end: Network


# Compiling the model
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


# Fit the model to the dataset (run the model for training)
if (visualizer):
    history = model.fit(X, Y, validation_split = 0.33, epochs = data[6], batch_size = 10, verbose = 1)
else:
    model.fit(X, Y, epochs = data[6], batch_size = 10)

# Save the model if wanted
if (saveModel):
    model.save("SavedModel")

# Show the accuracy at the end of the epochs
_, accuracy = model.evaluate(X, Y) # --> _, accuracy: discard the accuracy for X data and keep for Y data
print('Accuracy: %.2f' % (accuracy * 100))


# =================================================================================================
# def highest
#
# A function that returns the value from a list that is closest to an input value
#
# Arguments--
#
# lst:      the list of numbers to pick the largest from
#
# Returns--
#
# highestValue:   which of the numbers in the list was the largest
#
def highest(lst):

    highestValue = 0
    found = 0
    
    for i in range(len(lst)):
        if (lst[i] > highestValue):
            highestValue = lst[i]
            found = i

    return (highestValue, found)
# end: def highest


# Read in the new inference/testing file data
inference = loadtxt(data[5], delimiter = dataSeperator)

# Define the new datasets for the inference data
infX = inference[:,0:inputDims]
infY = inference[:,inputDims]
numTimesWrong = 0 # Number of times the NN was incorrect

infXList = cleanUp(infX)
prediction = model.predict(infXList)

# Go through all of the predictions for each of the X data examples
for i in range(len(prediction)):

    # Declare the expected result
    answer = infY[i]
    highestPossibleAnswer = 0

    # Clean up the prediction
    predictions = cleanUp(prediction[i])
    bestPred = 0

    # Find the best prediction
    bestPred, bestNode = highest(predictions)

    # Account for datasets that might have answers larger than 1 and find the largest answer in the dataset
    for j in range(len(infY)):

        if (infY[j] >= highestPossibleAnswer):
            highestPossibleAnswer = infY[j]

    # Adjust the output value to change from 0-1 to 0-the max answer value
    bestPred *= highestPossibleAnswer

    # Print each of the test casses from the testing dataset
    if (debug):
        print("Test case: " + str(i + 1))
        print("Node brightness: " + str(predictions))
        # Print the best prediction, the useful (or rounded) prediction, and the expected result
        print("Prediction (Accuarcy): " + str(float(bestPred)) + " | Prediction (Node): " + str(bestNode) + " | Expected: " + str(answer) + "\n")

        if (not bestNode == answer):
            numTimesWrong += 1 # If wrong, add to this value

print("Number of times correct: " + str(len(prediction) - numTimesWrong) + "/" + str(len(prediction))) # Print the number of times correct


# =================================================================================================
# def showChart
#
# A function to load a chart that visualizes the data from the network
#
# Arguments--
#
# plot1:        the metric from history to plot
#
# plot2:        the second metric from history to plot
#
# title:        the title of the graph
#
# ylabel:       the title of the y-axis
#
# xlabel:       the title of the x-axis
#
# legend1:      the name of the first plotted datapoint
#
# legend2:      the name of the second plotted datapoint
#
# legendLoc:    the location of the legend on the screen
#
# Arguments--
#
# None
#
def showChart(plot1, plot2, title, ylabel, xlabel, legend1, legend2, legendLoc):
    
    # Assemble the chart
    plt.plot(history.history[plot1])
    plt.plot(history.history[plot2])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend([legend1, legend2], loc = legendLoc)

    # Show the chart
    plt.show()
# end: def showChart


# Call the show chart function
if (visualizer):
    showChart('accuracy', 'val_accuracy', 'model accuracy', 'accuracy', 'epoch', 'train', 'test', 'upper left')
    showChart('loss', 'val_loss', 'model loss', 'loss', 'epoch', 'train', 'test', 'upper left')
