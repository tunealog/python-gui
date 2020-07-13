# Python Project

# Title : Python GUI
# Date : 2020-07-13
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="./img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="Seeya!")

    global photo2
    photo2 = PhotoImage(file="./img2.png")
    label2.config(image=photo2)


btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()
