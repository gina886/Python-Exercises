
from tkinter import*

root=Tk()
topframe = Frame(root)
topframe.pack()
bottomframe = Frame (root)
bottomframe.pack(side =BOTTOM)

b1 = Button(topframe, text = "open", fg="red")
b2 =Button(topframe,text="close",fg="blue")
b3 = Button (topframe,text ="exit",fg ="green")

b1.pack(side =LEFT) 
b2.pack(side= LEFT)
b3.pack(side = RIGHT)

root.mainloop()