# Software credits: Jonathan Uhler

"""
RT-triangle-generator.py

Right Triangle side-length generator to use with the KerasPredictor
"""

import random # Random function used to generate random numbers
import math # Used for square root


# =================================================================================================
# GLOBAL VARIABLES
#
numTraining = 10000
numInference = 1000
maxSideTrain = 100
maxSideInf = 100
dataArray = []
#
# end: GLOBAL VARIABLES


# =================================================================================================
# def right
#
# Creates a right triangle
#
# Arguments--
#
# a:        the side length for one of the sides
#
# b:        the side length for the second side
#
# Returns--
#
# c:        the hypotenuse
#
def right(a, b):
    cSqr = a ** 2 + b ** 2
    c = math.sqrt(cSqr)

    return c
# end: def right


# =================================================================================================
# def notRight
#
# Creates a non-right triangle
#
# Arguments--
#
# a:        the side length for one of the sides
#
# b:        the side length for the second side
#
# delta:    the margin-of-error value to make the triangle not right
#
# Returns--
#
# c:        the hypotenuse tweaked with the delta value to make the triangle non-right
#
def notRight(a, b, delta):
    c = right(a, b)
    plus_minus = random.random()

    if (plus_minus >= 0.5):
        return c + delta
    else:
        return c - delta
# end: def notRight


# =================================================================================================
# def writeData
#
# A function to write data to a file
#
# Arguments--
#
# data:     the data to be written
#
# Returns--
#
# None
#
def writeData(data, path):
    f = open(path, "a")
    f.write(data)
    f.close()
# end: def writeData


def createData(filePath, amt, maxSide):

    dataArray = []

    for i in range(int(amt / 2)):
        # Get two random values for the a and b sides
        a = (random.random() * maxSide)
        b = (random.random() * maxSide)

        # add the a, b, c, and the triangle status to an array of data
        dataArray.append(str(a) + "," + str(b) + "," + str(right(a, b)) + ",1\n")
        dataArray.append(str(a) + "," + str(b) + "," + str(notRight(a, b, (random.random() * 10))) + ",0\n")

    # randomize the array
    random.shuffle(dataArray)

    # print each line of the array to a data file
    for i in range(len(dataArray)):
        writeData(dataArray[i], filePath)


createData("triangle-sides.csv", numTraining, maxSideTrain)
createData("triangle-inference.csv", numInference, maxSideInf)
