from tkinter import *
 
root = Tk ()

def button_click(event):
    print("button clicked")

button1= Button(root, text= "one", fg="red")
button1.bind("<Button-1>", button_click)
button1.pack(side= LEFT)  # keeping the 3 buttons in the same line

button2= Button(root, text= "two", fg="green")
button2.bind("<Button-1>", button_click)
button2.pack(side =LEFT)# keeping the 3 buttons in the same line

button3= Button(root, text= "three", fg="blue")
button3.bind("<Button-1>", button_click) 
button3.pack(side=LEFT)# keeping the 3 buttons in the same line

root.mainloop()


