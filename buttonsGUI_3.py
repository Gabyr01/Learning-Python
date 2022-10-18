from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="click me", command=myClick) 
#don't call function with parenthesis --> myClick
myButton.pack()
#state = DISABLED

root.mainloop()