# Python Project

# Title : Python GUI
# Date : 2020-07-13
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "Berry")
listbox.insert(2, "Banana")
listbox.insert(END, "Melon")
listbox.insert(END, "Orange")
listbox.pack()


def btncmd():

    # Object Delete
    listbox.delete(0)  # 0 or END

    # Object Count
    print("ListBox has", listbox.size(), "objects")

    # Object Check (Start idx, End idx)
    print("1 ~ 3 object : ", listbox.get(0, 2))

    # Selected Object Check
    print("Selected Object : ", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
