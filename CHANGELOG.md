# Changelog Description

How this file is used: When changing other files in this reposity, MAKE SURE to update the changelog with a version, date, and a list of new changes (this does not have to be extremely detailed)

Version conventions (IMPORTANT): The version conventions used for this file are "MAJOR.Minor.patch"
	-A major version  will be incompatible with older versions of the software
	-A minor version  may be incompatible with certain parts of older software
	-A patch should not be incompatible at all with older versions; patches are usually documentation changes
	

# Changelog

	version		 date			changes
	-------		-------		----------------------------------------------------
	1.0.0		12/8/20		Changes in this version:
								-First acceptably working version of KerasPredictor.py
								
	1.1.0		12/8/20		Changes in this version:
								-Added the debug boolean option to the config file
								-Added a right and non-right triangle side generator file
								-Moved old testing datasets to a "deprecated datasets" folder
									-Created a new dataset (given side lengths, determine if a triangle is right)
									
	1.2.0		12/9/20		Changes in this version:
								-Added a debug option and the number of epochs to the config file
								-Changed "import keras.layers" to "import keras.layers.core"
								-Rebuilt the cleanUp(lst) function
								-Add an inferencing dataset

	1.3.0		12/9/20		Changes in this version:
								-"Fixed" an issue with the network seemingly not learning and just outputing 50% accuracy
									-IMPORTANT: This was not really a bug, the issue causing this was the large triangle max side in the triangle genertor. Decreating this number (or dramatically increasing the data to millions of points) allowed to network to find patterns easier
									
	1.4.0		12/9/20		Changes in this version:
								-Added an option to save the model

	1.4.1		12/9/20		Changes in this version:
								-Added seperate variables in the dataset generator for number of right triangles and number of non-right triangles
								-Added a display of the percent after showing debug data
								
	1.4.2		12/10/20	Changes in this version:
								-Reorganized PredictorConfig.json to include labels explaining the use of the config data elements
								-Added more customization to the RT-triangle-generator.py file
