# Python Project

# Title : Python GUI
# Date : 2020-07-13
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="Disable(Today)", variable=chkvar)

chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Disable(A week)", variable=chkvar2)
chkbox2.pack()


def btncmd():
    # 0 : Checked, 1 : Not Checked
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
