# Python Project

# Title : Python GUI
# Date : 2020-07-15
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "days")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
