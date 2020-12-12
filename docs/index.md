Rick Vandercar  
11/08/20  
IT FDN 110A Intro to Programming (Python)  
Assignment07  
https://github.com/rvandercar/IntroToProg-Python-Mod7  
https://rvandercar.github.io/IntroToProg-Python-Mod7/  

# Files, exceptions, & GitHub

## Introduction  

For this module we covered the basics of dealing with text files and binary files. We also went into how to handle exceptions in an elegant way. Beyond that, we went deeper into using GitHub and creating a web page using the Markdown language.

I explored a few pages to learn more about pickling and how it can be used for serializing and de-serializing a Python object structure.

I found the following pages to be helpful with information about pickling.  

https://www.geeksforgeeks.org/understanding-python-pickling-example/ (external)  
sample:  

![Geeks for Geek sample](https://github.com/rvandercar/IntroToProg-Python-Mod7/raw/main/docs/pics/geeksforgeeks_sample.png "Geeks for Geeks") 
 

https://www.datacamp.com/community/tutorials/pickle-python-tutorial (external)  
sample:  

![Data camps sample](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/data_camps_sample.png "Data Camp")

https://yasoob.me/2013/08/02/what-is-pickle-in-python/ (external)  
sample:  

![Yasoob sample](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/yasoob_sample.png "Yasoob Sample")  
 
I found the following pages very helpful with learning about python exception handling.  

https://docs.python.org/3/tutorial/errors.html (external)  
sample:  
 
![Python.org sample](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/python_org_sample.png "Python.org sample")

https://www.datacamp.com/community/tutorials/exception-handling-python (external)  
sample:  

![Data camp samples](https://github.com/rvandercar/IntroToProg-Python-Mod7/main/docs/pics/data_camp_error_sample.png "Data Camp Samples2")

https://overiq.com/python-101/exception-handling-in-python/ (external)  
sample:  

![Overiq sample](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/over_iq_sample.png "Overiq Sample")

I enjoyed learning about the exception handling as I think it’s important to use this to make your program nicer to use.  


## Applying my knowledge

I really struggled with this script. I tried to make a nice elegant script with lots of useful functions, but also showing pickling and error exceptions. I found that the script I was writing was just too messy to clean up. I have kept it and will going back to it after this course, so that I can make it work. I got pretty close, but I have spent way too much time on it so I went for a functional script that would show you the basics. 

I created a simple program that will take some user input on what musical keyboards they want, and at what price they are selling for. When the file is saved or read from it is doing it via the pickle function. 

There is exception error handling on the price for the keyboard and to verify that there is a file that exists when you try to show the current keyboard list. If you put in text for the price of the keyboard, it will ask you one more time for a proper input. If you don’t provide it, it dumps you out of the program. If you put in correct data the second time, then things continue on as normal. 

A file is not necessary to start the program, but if you try to save to the file without adding anything to the list, you will get an error and be returned to the menu.

Initial menu in PyCharm

![Inital menu in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/init_py.png "Initial menu in PyCharm")

Showing missing file exception in PyCharm  

![File exception in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/file_py.png "File exception in PyCharm")

Adding to list in PyCharm  

![Adding to list in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/list_py.png "Adding to list in PyCharm")

Showing error trapping of text for price in PyCharm  

![Error trapping of price in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/price_py.png "Price error trapping in PyCharm")

Showing recovery after error exception in PyCharm  

![Error recovery in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/revocer_py.png "Error recovery in PyCharm")
 
Showing file being saved (using pickle) in PyCharm  

![Pickling in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/save_py.png "Pickling in PyCharm")

Showing reading of pickled file in PyCharm  

![Reading pickled file in PyCharm](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/read_py.png "Reading pickled file in PyCharm")

Initial menu in terminal  

![Initial page in Terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/init_term.png "Initial page in terminal")

Showing missing file exception in terminal  

![Missing file in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/file_term.png "Missing page in terminal")

Adding to list in terminal  

![Adding to list in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/list_term.png "Adding to list in terminal")

Showing error trapping of text for price in terminal  

![Error trapping of price in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/price_term.png "Price error trapping in terminal") 

Showing recovery after error exception in terminal  

![Error recovery in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/revocer_term.png "Error recovery in terminal")

Showing file being saved (using pickle) in terminal  

![Pickling in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/save_term.png "Pickling in terminal")

Showing reading of pickled file in terminal  

![Reading pickled file in terminal](https://github.com/rvandercar/IntroToProg-Python-Mod7/blob/main/docs/pics/read_term.png "Reading pickled file in terminal")


## Summary  
I love the concept of graceful error handling and appreciated some of the intricacies of it in the exercise. As a QA person, I find a lot of faults in my programs. They will do the basics of what they are supposed to do, but I can easily break them. This error handling will hopefully make my programs more robust and bullet proof in the future.

Pickling my data in the future will help my programs to read and write to the files quicker which will certainly help when dealing with very large amounts of data. It will also help me to be able to be more selective with the data I pull from the file, rather than having to read in an entire text file.

My apologies for turning this in so late. I have been in the process of going to hefty interview sessions with two companies. They have both turned me down, so now I hopefully have the time to catch up in class.

