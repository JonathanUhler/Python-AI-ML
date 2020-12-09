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
