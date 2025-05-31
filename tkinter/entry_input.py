from tkinter import *
root = Tk()
#create an label and an entry
l1=Label(root, text="please enter your name: ")
l2=Label(root, text="place enter your password:")

entry1 = Entry(root)
entry2= Entry(root, show="*")# hide the input

l1.grid(row=0, sticky=E) #first row
l2.grid(row=1, sticky=E) #second row

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()