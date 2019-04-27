# ZipFileAutomation
This program reads in directories from a CSV file, and creates a zip file for each months' worth of files contained in that directory, based on the date modified time of each file. Months and Years are specified within the program so this can be tailored for your environment. Once files are zipped into their respective zip folders, files are deleted from the original directory.
The program will then loop round until all directories from the CSV file have been read and checked for files that have a date modified month and year that exists in the two lists.
