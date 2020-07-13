# Python Project

# Title : Python GUI
# Date : 2020-07-13
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button22222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button4444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")
btn5.pack()

photo = PhotoImage(file="./img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("Click!")


btn7 = Button(root, text="Active Button", command=btncmd)
btn7.pack()
root.mainloop()
