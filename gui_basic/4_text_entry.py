# Python Project

# Title : Python GUI
# Date : 2020-07-13
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Text")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Entry")


def btncmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
