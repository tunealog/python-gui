# Python Project

# Title : Python GUI
# Date : 2020-07-16
# Creator : tunealog

import os
from tkinter import *

root = Tk()
root.title("None Title - Memo")
root.geometry("640x480")


def file_open():
    if os.path.isfile("mynote.txt"):
        mynote_file = open("mynote.txt", "r", encoding="utf8")
        txt.delete("1.0", END)
        txt.insert(END, mynote_file.read())
        mynote_file.close()


def file_save():
    mynote_file = open("mynote.txt", "w", encoding="utf8")
    mynote_file.write(txt.get("1.0", END))
    mynote_file.close()


menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="File Open", command=file_open)
menu_file.add_command(label="File Save", command=file_save)
menu_file.add_command(label="Exit", command=root.quit)

menu_edit = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit", menu=menu_edit)
menu.add_cascade(label="View", menu=menu_view)
menu.add_cascade(label="Help", menu=menu_help)
root.config(menu=menu)

frame = Frame(root)
frame.pack(fill="both", expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt = Text(frame, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)
root.mainloop()
