from tkinter import *
from tkinter import messagebox

def do_nothing():
    print("nothing done")

# create the main window
root = Tk()
root.title("Colored Menu Bar")
root.geometry("400x300")

# define colors
MENU_BG = "#333333"      # Menu bar background color (dark gray)
MENU_FG = "white"        # Menu bar text color (white)
SUB_BG = "#555555"       # Submenu background color (lighter gray)
SUB_FG = "white"         # Submenu text color (white)
HOVER_BG = "#0078d7"     # Hover background color (blue)
HOVER_FG = "white"       # Hover text color (white)

# ===== Menu Bar =====
menu_bar = Menu(root,
                bg=MENU_BG,
                fg=MENU_FG,
                activebackground=HOVER_BG,
                activeforeground=HOVER_FG)
root.config(menu=menu_bar)

# File submenu
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

# Edit submenu
edit_menu = Menu(menu_bar,
                 tearoff=0,
                 bg=SUB_BG,
                 fg=SUB_FG,
                 activebackground=HOVER_BG,
                 activeforeground=HOVER_FG)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=do_nothing)

# ===== Toolbar =====
toolbar = Frame(root, bg="blue")
insert_button = Button(toolbar, text="Insert Image", command=do_nothing, bg="white", fg="black")
insert_button.pack(side=LEFT, padx=2, pady=2)

print_button = Button(toolbar, text="Print", command=do_nothing, bg="white", fg="black")
print_button.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ===== Window Close Confirmation =====
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main event loop
root.mainloop()



