# ------------------------------------------------- #
# Title: assignment07
# Description: Combined topics of pickling and error handling
# ChangeLog: (Who, When, What)
# <Patrick Regan>,<8-20-23>,Created Script
# ------------------------------------------------- #

import os
import pickle

class file_exists(Exception):
    """*** This file already exists"""
    def __str__(self):
        return '>>> Error 1, cannot create duplicate file.'
class choice_error(Exception):
    """*** Please enter a valid choice"""
    def __str__(self):
        return '>>> Error 2, selection must only contain a number from list.'

class pickle_error(Exception):
    """*** Data must first be dumped before you can load pickled data"""
    def __str__(self):
        return '>>> Error 3, file contains no data formatted with pickle dump.'


filename = None
objFile = None
strData = None
choice = None
strTemp = None

while True:
    filename = str(input("Enter the name of a new file to store data:\n"))  # ask user for new file name
    filename = (filename + ".pkl")  # add extension to file
    try:
        if os.path.isfile(filename):  # check to see if file exists
            raise file_exists()  # if it does exist, run this error code
        else:
            break
    except Exception as e:  # this runs more detailed information on the error that is called on line 37
        print(e)  # print info on error
        print(e.__doc__)  # print info on error

objFile = open(filename, "w")  # open the new file in a variable
objFile.write("")  # write something to the file so that it is actually created
objFile.close()

print("\nThank you.\n",  end='')  # message

while True:
    print("\nPlease choose from the following options, and select choice by number")  # choose selection
    print("**************************")
    print("1. add data to list and pickle\n2. pickle.load data\n3. exit")
    print("**************************")
    choice = str(input(">>> ")).strip()  # choice is stripped of spaces
    if choice == "1":
        strData = str(input("add some data"))  # add some data from user
        objFile = open(filename, "wb")  # open with binary write
        pickle.dump(strData, objFile) # dump the information into the file with pickle.dump
        objFile.close()
        print("data successfully pickled")
    elif choice == "2":
        try:
            if os.stat(filename).st_size == 0:  # if file has no information in it, raise the error below
                raise pickle_error()
            else:
                objFile = open(filename, "rb")  # if data exists, read data with binary read
                strTemp = pickle.load(objFile)  # store to temp variable
                print("Your data has been returned as: ", strTemp)  # display file contents to user
                objFile.close()
        except Exception as e:  # code that explains the error called in pickle_error()
            print(e)
            print(e.__doc__)

    elif choice == "3":  # quit program
        quit()
    else:  # if any other number besides the options in the menu, raise choice_error
        try:
            if choice != "1" or "2" or "3":
                raise choice_error()
            else:
                continue
        except Exception as e:  # details on choice_error
            print(e)
            print(e.__doc__)
