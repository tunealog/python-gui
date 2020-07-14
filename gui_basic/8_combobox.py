# Python Project

# Title : Python GUI
# Date : 2020-07-14
# Creator : tunealog

import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

values = [str(i) + "days" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Days")


readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="Select", command=btncmd)
btn.pack()
root.mainloop()
