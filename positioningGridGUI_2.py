from tkinter import *

root = Tk() #frame to manage all components of tkinter application


#creating label widget
#w = Label ( master, option, ... )
#master − This represents the parent window.
#options can be used as key-value pairs separated by commas

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Gaby")

#option 2 - grid system 
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop()