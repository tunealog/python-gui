# Python Project

# Title : Python GUI
# Date : 2020-07-14
# Creator : tunealog

import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()


# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="Stop", command=btncmd)
# btn.pack()
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())


btn2 = Button(root, text="Start", command=btncmd2)
btn2.pack()

root.mainloop()
