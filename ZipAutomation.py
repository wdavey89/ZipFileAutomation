import sys, os, time, datetime, zipfile, send2trash, ctypes, csv

def main():
    ctypes.windll.kernel32.SetConsoleTitleW('ZipAutomation.py')
    print('--- ZipFile Automation ---')
    file = 'directories.csv' # Use the directories.csv file to get list of directories
    readFile(file)
    endProgram()        

def readFile(file):
    try: # Open CSV file and read line by line and call startzip() on each iteration
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                directory = row[0] # Read each line of the csv file and assign value to directory.
                try:
                    os.chdir(directory)                    
                    startZip(directory)
                    print('----- Directory Complete {} -----\n\n'.format(directory))                    
                except FileNotFoundError:
                    print('Directory does not exist')                    
            
    except FileNotFoundError:
        print('File does not exist')
    


def startZip(directory):
    # Create two lists to check months and years against date modified of each file in the directory specified
    # Create an archive directory inside the specified directory, and create a zip folder for each month and year that contains files that match
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years = [2015, 2016, 2017, 2018]
    print('----- Checking directory {} -----'.format(directory))
    if len(os.listdir(directory)) != 0:
        print('{} files have been found in this directory to be zipped. '.format(len(os.listdir(directory))))
        archivePath = os.path.join(directory, 'Archive')
        if not os.path.exists(archivePath):
            os.makedirs(archivePath)
        for items in os.listdir('.'):
            dt = datetime.date.fromtimestamp(os.path.getmtime(items))
            if os.path.isfile(items):
                if dt.year in years and dt.month in months:
                    files = [items]                    
                    zipLocation = os.path.join(archivePath, str(dt.month) + str(dt.year) + '.zip')
                    newZip = zipfile.ZipFile(zipLocation, 'a', allowZip64=True) # Allow Zip64 meaning zip files can be larger tha 4Gb
                    for found in files:                                    
                        newZip = zipfile.ZipFile(zipLocation, 'a', zipfile.ZIP_DEFLATED)
                        newZip.write(found)                    
                        print(found)
                        os.unlink(found) # Delete files once they've been zipped
    else:
        print('Directory {} is empty, moving to next directory '.format(directory))


def endProgram():
    try:
        input('All directories complete, press any key to exit. ')
    except SyntaxError:
        pass
    

if __name__ == '__main__':
    main()
