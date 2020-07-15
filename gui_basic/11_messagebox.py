# Python Project

# Title : Python GUI
# Date : 2020-07-15
# Creator : tunealog

import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")


def info():
    msgbox.showinfo("Alert", "Info Message")


def warn():
    msgbox.showwarning("Warning", "Warning Message")


def error():
    msgbox.showerror("Error", "Error Message")


def okcancel():
    msgbox.askokcancel("OK / Cancel", "OK / Cancel Message")


def retrycancel():
    response = msgbox.askretrycancel(
        "Retry / Cancel", "Retry / Cancel Message")
    if response == 1:
        print("Retry")
    elif response == 0:
        print("Cancel")


def yesno():
    msgbox.askyesno("Yes / No", "Yes / No Message")


def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Yes / No / Cancel")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")


Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()
Button(root, command=okcancel, text="OK Cancel").pack()
Button(root, command=retrycancel, text="Retry Cancel").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()

root.mainloop()
