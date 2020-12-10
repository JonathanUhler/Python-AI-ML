# Software credits: Jonathan Uhler, Neo Liu, Xander Yee

"""
KerasInferencer.py

A program that inferences saved models
"""

# Import required libraries and APIs
from numpy import loadtxt # NumPy is a number/data processor
from tensorflow import keras
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


# =================================================================================================
# def printDebug
#
# A function to handle printing debug messages
#
# Arguments--
#
# testCase:         the test case number being printed
#
# nodeBrightness:   each of the probabilities for the output nodes
#
# msg:              the message to be printed
#
# Returns--
#
# None
#
def printDebug(testCase, nodeBrightness, msg):
    print("Test case: " + str(testCase))
    print("Node brightness: " + str(nodeBrightness))
    # Print the best prediction, the useful (or rounded) prediction, and the expected result
    print(msg)
# end: printDebug


# =================================================================================================
# GLOBAL VARIABLES
# To change these config values, go to "PredictorConfig.json"
#
with open('PredictorConfig.json') as PredictorConfigData:
    data = json.load(PredictorConfigData)
#
data = [data['trainFile'], data['dataSeperator'], data['outputWidth'], data['visualizer'], data['debug'], data['inferFile'], data['numEpochs'], data['save'], data['trainOnly'], data['loadModel']]
#
dataCSV = data[0] # --> The input with with data for training and testing
dataSeperator = data[1] # --> The character that seperates data elements in the input file
outputDims = data[2] # --> The width of the output layer
visualizer = data[3] # --> The toggle for whether or not a graph is displayed when the NN finishes
debug = data[4] # --> On a scale of 0-2. 0) no debug, 1) only wrong cases, 2) all cases
#       data[5] --> used later as the location of the inference data file
#       data[6] --> used later as the number of epochs
saveModel = data[7] # --> The toggle for whether or not the trained model will be saved
trainOnly = data[8] # --> The toggle for whether or not the network will only train or train and inference
loadModel = data[9] # --> The path to a saved model
#
print("dataCSV: " + str(dataCSV) + "\ndataSeperator: " + str(dataSeperator) + "\noutputDims: " + str(outputDims) + "\nvisualizer: " + str(visualizer) + "\ndebug: " + str(debug) + "\nsaveModel: " + str(saveModel) + "\n")
#
#
# Read in and split the data elements by a seperator, both the input file and the delimiter are
# defined above.
dataset = loadtxt(dataCSV, delimiter = dataSeperator)
# Get the width for the input layer
inputDims = len(dataset[0]) - 1
#
# end: GLOBAL VARIABLES


# Define the Keras model as being a sequential model
# A sequential model has a stack of layers where each layer has exactly 1 input tensor and 1 output tensor
model = keras.models.load_model(loadModel)


def inference():
    # Read in the new inference/testing file data
    inference = loadtxt(data[5], delimiter = dataSeperator)

    # Define the new datasets for the inference data
    infX = inference[:,0:inputDims]
    infY = inference[:,inputDims]
    numTimesCorrect = 0 # Number of times the NN was incorrect

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
        if (debug == 2):
            printDebug(i + 1, predictions, "Prediction (Accuarcy): " + str(float(bestPred)) + " | Prediction (Node): " + str(bestNode) + " | Expected: " + str(answer) + "\n")

        elif (debug == 1 and not (bestNode == answer)):
                printDebug(i + 1, predictions, "Prediction (Accuarcy): " + str(float(bestPred)) + " | Prediction (Node): " + str(bestNode) + " | Expected: " + str(answer) + "\n")


        if (bestNode == answer):
            numTimesCorrect += 1 # If wrong, add to this value

    print("Number of times correct: " + str(numTimesCorrect) + "/" + str(len(prediction)) + " | Accuracy: " + str((numTimesCorrect / len(prediction)) * 100) + "%") # Print the number of times correct
# end: def inference


if (not trainOnly):
    # Inference the data
    inference()
