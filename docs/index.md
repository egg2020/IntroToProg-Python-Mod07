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

![alt text](.docs/Capture.PNG "tooltip text")  

I wanted to show this just as an example of when things go wrong.  I added an extra letter into my code so that an error would show up.  But now, I am going to have the program call a custom error class, that is a little more detailed.  Below is an example of a custom class, and how it looks when it's called.

![alt text](https://github.com/egg2020/IntroToProg-Python-Mod07/blob/main/docs/Capture1.PNG "tooltip text")  

And here is how it is called in the code:

![alt text](https://github.com/egg2020/IntroToProg-Python-Mod07/blob/main/docs/Capture2.PNG "tooltip text")

I am using this particular error handling code, only in one location where the user has the ability to enter more numbers than my code can handle, and this code let's the user know that the input was invalid.  

## Summary 
In summary, pickling enables us to store formatted data into a file, with the added bonus of obscuring the data.  Error Handling allows us to put in custom error codes, where we feel they may be needed.  


