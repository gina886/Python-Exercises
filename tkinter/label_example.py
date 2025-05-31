from tkinter import *

root=Tk() #creater a main window
#create a label 
label1 = Label(root, text="hello,label")
label1.pack() # pack the lanbel into the window

label2 = Label(root,bg="pink")
label2.pack(fill=X) #x = horizontal fill

label3 =Label(root, bg="white")
label3.pack(side=LEFT, fill=Y) #Y= vertical fi
root.mainloop() #start the main loop　