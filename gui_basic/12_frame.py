# Python Project

# Title : Python GUI
# Date : 2020-07-15
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

Label(root, text="Choose the menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

# Burger Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
Button(frame_burger, text="Burger").pack()
Button(frame_burger, text="Cheese Burger").pack()
Button(frame_burger, text="Chicken Burger").pack()

# Drink Frame
frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Cider").pack()

root.mainloop()
