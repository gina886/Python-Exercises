from tkinter import *
root= Tk()

def leftclick(event):
    print("Left click")

def middleclick(event):
    print("Middle click")

def rightclick(event):
    print("Right click")


frame = Frame(root, width=200, height=200, bg="pink")
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack(expand=True, fill=BOTH)

root.mainloop()


