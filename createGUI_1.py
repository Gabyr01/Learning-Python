
#creating a very simple GUI with TKinter
#first video from playlist "pythons GUI's with TKinter"

from tkinter import * #import from tkinter

root = Tk()

#create a label widget
myLabel = Label(root, text="Hello world!")
#first option - pack
myLabel.pack()


root.mainloop() # runs the tkinter event loop 


