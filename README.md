# Python AI-ML

A dive into basic machine learning in Python 3. Project made for comp sci final exam.


# Dependencies
Python 3 or higher - https://www.python.org/downloads/   |   pip (used to install packages and APIs) - https://pip.pypa.io/en/stable/installing/   |   Keras (neural network API) - https://pypi.org/project/Keras/   |   NumPy (data handler) - https://numpy.org/install/   |   MatPlotLib (for displaying data using a GUI) - https://matplotlib.org/3.3.3/users/installing.html


# Installation
Install Keras, NumPy, and MatPlotLib. Clone or download the KerasPredictor.py file as well as the training data .csv file.


# RT-triangle-generator.py Usage
To generate new testing data, open and clear the "triangle-sides.csv" and "triangle-inference.csv" files and then run "python3 RT-triangle-generator-py" in command-line; this will generate new data to be used. To change the amount of data that is generated, change the "numTriangles" variable at the top of the file (the total number of new datapoints will be this times 2). Note: you can also change the maximum side length for the A and B legs with the "maxSideLength" variable, but in order for the network to understand patterns and learn, do not increase this above 100.


# KerasPredictor.py Usage
Using the change directory command in command-line, move to the directory with the file. To run the network, run "python3 KerasPredictor.py" in command-line. You should see the status for all of the epochs begin printing. If you have debug enabled, all the test-case predictions will print after the epochs are done (after this, you will also be able to see the inference accuracy). If you have the visualizer graph enabled, the graph should launch as a seperate python app after the data has been printed.


# KerasInferencer.py Usage
The inferencer loads a saved model and uses the inference dataset to test it without having to train it first. To create a saved model, run the KerasPredictor.py with "save" set to true. A new model should be saved. To load and test the model, set the "loadModel" to be the path to the model in question, then run the KerasInferencer.py and the model will be inferenced. Unless the inference dataset is very large, I suggest setting debug to 1 (print incorrect cases) or 2 (print all cases) so you can see the inferences.


# PredictorCongif.json
In order to change the properties of the predictor (e.g. the input file, whether the visualizer is enabled, etc.) open the PredictorConfig.json file and change the elements. The elements are: train file location, data seperator, output width, visualizer toggle, debug toggle, inference file location, number of epochs, save toggle, train only toggle, and saved model location.
