# Pickles and Errors
**Patrick Regan**, *8.21.2023*  
*Module07-Python*  

Pickling data is when you serializing and de-serializing data, where a files data is converted into different formats, for more effiecient storage and easier data transfer.  An upside to formatting, is data ambiguity, meaning the data in the storage file has been obscured.  This may be helpful if you do not want your end user to view the data from a file, in a way where they can see exactly what is happening in the code.  There are a few ways to pickle data, and I will be covering both pickle.dump and pickle.load.  Later in this tutorial, I will talk about Error Handling.  Let's get to it!  

## Pickling
First things first, let's create a file and an object that represents it:

```
lstData = []
lstTemp = []
filename = ("dostuff.txt)  # create file name  
lstData = str(input("add some data"))  # get input from user
objFile = open(filename, "wb")  # create object for the file and open using write binary
pickle.dump(strData, objFile)  # dump that stuff!
objFile.close()  # close file
```

Here we prompt the user for data to put in the file objFile, and dump it to the corresponding file.  That's really all there is to it.  But we have to use pickle.load to be able to read and retrieve the correct formatting.  Let's look at that next:

```
objFile = open(filename, "rb")  # open our object with read binary
lstTemp = pickle.load(objFile)  # load the information into a new list
print("Your data has been returned as: ", lstTemp)  # display what is in that list.
objFile.close()
```  

As you can see, it's all pretty simple.  Now lets take a look at Error Handling.  

## Error Handling  
When something goes wrong in the code, python uses built in Error classes to explain to the programmer what has happened.  This usually results in a program crash.  We can create our own error handling classes, and call them whenever we think there is potential for errors to occur.  What is more, is that the program doesn't neccessarily need to crash.  Below is an example of when python's built error code kicks in:
