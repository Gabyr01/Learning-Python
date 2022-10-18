from tkinter import *

root = Tk()

#entry widget
entry = Entry(root, bg="pink")
#borderwidth = 5
entry.pack()
entry.insert(0,"enter your name: ")
#gets entry value
# entry.get()
def myClick():
    hello = "hello " + entry.get()
    myLabel1 = Label(root, text = hello)
    myLabel1.pack()


MyButton = Button(root, text="enter", command=myClick)
MyButton.pack()


root.mainloop()