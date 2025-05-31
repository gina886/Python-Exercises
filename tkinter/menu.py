from tkinter import *
from tkinter import messagebox

def do_nothing():
    print("nothing done")

# create the main window
root = Tk()  # Correct usage: Tk() is the constructor
root.title("Colored Menu Bar")  # Set the window title
root.geometry("400x300")  # Set the window size

# define colors
MENU_BG = "#333333"      # Menu bar background color (dark gray)
MENU_FG = "white"        # Menu bar text color (white)
SUB_BG = "#555555"       # Submenu background color (lighter gray)
SUB_FG = "white"         # Submenu text color (white)
HOVER_BG = "#0078d7"     # Hover background color (blue)
HOVER_FG = "white"       # Hover text color (white)

# create a menu bar
menu_bar = Menu(root,
                bg=MENU_BG,
                fg=MENU_FG,
                activebackground=HOVER_BG,
                activeforeground=HOVER_FG)
root.config(menu=menu_bar)  # Attach the menu bar to the main window

# create a file submenu
file_menu = Menu(menu_bar,
                 tearoff=0,
                 bg=SUB_BG,
                 fg=SUB_FG,
                 activebackground=HOVER_BG,
                 activeforeground=HOVER_FG)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=do_nothing)
file_menu.add_command(label="New", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an edit submenu
edit_menu = Menu(menu_bar,
                 tearoff=0,
                 bg=SUB_BG,
                 fg=SUB_FG,
                 activebackground=HOVER_BG,
                 activeforeground=HOVER_FG)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=do_nothing)

# Confirmation dialog when closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()


