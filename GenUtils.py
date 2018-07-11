#!/usr/bin/env python
"""Provides commonly used (during coding).

The file defines a bunch of functions that can be used on the command line.
In later version of python these may already be a part of python package in some form
I will continue to add functions that I find useful during python development work

# python ./GenUtils.py version
# python ./GenUtils.py dirCount ./
# python ./GenUtils.py saveToFile ./testfile.txt dataToSave
# python ./GenUtils.py readFile ./testfile.txt
# python ./GenUtils.py filesize ./testfile.txt
# python ./GenUtils.py touch ./testfile.txt
"""
import sys
import time
import os
import json
import urllib
import shutil
import datetime
#from PIL import Image
from subprocess import call

__author__ = "Vagish"
__copyright__ = "Copyright 2018, The Pug Project"
__credits__ = ["WWW, Python Developers, Google, stackoverflow"]
__license__ = "MIT"
__version__ = "3.5.6"
__maintainer__ = "Vagish"
__email__ = "vagish@gmail.com"
__status__ = "Development"

#----------------------------------------------
# Common logging function, modify as needed
#----------------------------------------------
def logLocal(msg):
    #We are adding this since already encoded string throws exception
    try:
        msgT = msg.encode('utf-8')
    except:
        msgT = msg
        
    mString  = time.ctime() + ": " + msgT
    
    #Optionally: Write to a log file
    #with open("./logfile.txt", "a") as myfile:
    #    myfile.write("\r\n" + mString)
    print (mString)

#----------------------------------------------    
# This is a general utils class for functions
#----------------------------------------------
class GenUtils:

    @staticmethod
    def version():
        return __version__ 
    
    #---------------------------------------------------
    #Save a base64 string to an image file
    #---------------------------------------------------
    @staticmethod
    def saveImageStrToPath(image_string, image_path = ""):
        if image_string == "":
            return ""
        
        if image_path == "":
            epoch_time = int(time.time())
            timestr = str(epoch_time)
            image_path = "./labelme-" + timestr + ".jpg"
            
        fh = open(image_path, "wb")
        fh.write(image_string.decode('base64'))
        fh.close()
        
        return image_path
    
    #---------------------------------------------------
    #Get number of items in a directory, source unknown
    #---------------------------------------------------
    @staticmethod
    def dirCount(DIR):
        return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    
    
    #---------------------------------------------------
    #Save some data to a file
    #---------------------------------------------------
    @staticmethod
    def saveToFile(fileName, dataToSave):
        file = open(fileName,"w") 
        file.write(dataToSave) 
        file.close() 
        return fileName
    
    #---------------------------------------------------
    #Read some data from a file
    #---------------------------------------------------
    @staticmethod
    def readFile(fileName):
        data = ""
        with open(fileName, 'r') as myfile:
            data = myfile.read()
            myfile.close() 
        return data
    
	#----------------------------------------------
    # Method to simulate Linux touch command
    #----------------------------------------------
    @staticmethod
    def touch(fname, times=None):
        open(fname, 'a').close()
        with open(fname, 'a'):
            os.utime(fname, times)
        
    #----------------------------------------------
    # Subtract a month from time, source of code unknown
    #----------------------------------------------    
    @staticmethod
    def subtract_one_month(t):
        """Return a `datetime.date` or `datetime.datetime` (as given) that is
        one month later.
        
        Note that the resultant day of the month might change if the following
        month has fewer days:
        
            >>> subtract_one_month(datetime.date(2010, 3, 31))
            datetime.date(2010, 2, 28)
        """
        one_day = datetime.timedelta(days=1)
        one_month_earlier = t - one_day
        while one_month_earlier.month == t.month or one_month_earlier.day > t.day:
            one_month_earlier -= one_day
        return one_month_earlier

#----------------------------------------------
#Run Utility function if called from command-line  
#----------------------------------------------      
if __name__ == '__main__':

    # Try to read the main paramenter
    task = ""
    try:
        task = sys.argv[1]
    except:
        task = ""
    
    if task == "version":
        logLocal("Version: " + GenUtils.version())
        
    elif task == "dirCount":
        dirPath = sys.argv[2]
        logLocal("dirCount: " + str(GenUtils.dirCount(dirPath))) 
        
    elif task == "saveToFile":
        filePath = sys.argv[2]
        fileData = sys.argv[3]
        logLocal("Save To: " + GenUtils.saveToFile(filePath, fileData)) 
        
    elif task == "readFile":
        filePath = sys.argv[2]
        logLocal("Data Read: " + GenUtils.readFile(filePath))
        
    elif task == "touch":
        filePath = sys.argv[2]
        GenUtils.touch(filePath)
        logLocal("File Touched: " + filePath)   

    elif task == "filesize":
        filePath = sys.argv[2]
        filesize = 0
        if os.path.isfile(filePath) == True:
            filesize = os.path.getsize(filePath)
        logLocal("filesize: " + str(filesize))
    
    else:
        logLocal("Looks like nothing was done, check parameters.")
        
        
