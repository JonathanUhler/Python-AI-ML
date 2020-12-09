# Python AI-ML

A dive into basic machine learning in Python 3. Project made for comp sci final exam.


# Dependencies
Python 3 or higher - https://www.python.org/downloads/   |   pip (used to install packages and APIs) - https://pip.pypa.io/en/stable/installing/   |   Keras (neural network API) - https://pypi.org/project/Keras/   |   NumPy (data handler) - https://numpy.org/install/   |   MatPlotLib (for displaying data using a GUI) - https://matplotlib.org/3.3.3/users/installing.html


# Installation
Install Keras, NumPy, and MatPlotLib. Clone or download the KerasPredictor.py file as well as the training data .csv file.


# Usage/Running
Using the change directory command in command-line, move to the directory with the file. To generate new testing data, open and clear the "triangle-sides.csv" file and then run "python3 RT-triangle-generator-py" in command-line. To run the network, run "python3 KerasPredictor.py" in command-line. You should see the status for all 300 epochs begin printing. If you have debug enabled, all the test-case predictions will print after the epochs are done.


# PredictorCongif.json
In order to change the properties of the predictor (e.g. the input file, whether the visualizer is enabled, etc.) open the PredictorConfig.json file and change the elements. The elements are: input file, data seperation character, output layer width, visualizer enabler, and debug message enable.
