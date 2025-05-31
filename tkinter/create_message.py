from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()
root.withdraw() 

messagebox.showinfo("This is a message")

answer = messagebox.askquestion("Question")

if answer == "yes":
    print("Your answer is yes")
else:
    print("Your answer is no")

root.mainloop()
