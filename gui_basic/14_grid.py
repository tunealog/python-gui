# Python Project

# Title : Python GUI
# Date : 2020-07-15
# Creator : tunealog

from tkinter import *

root = Tk()
root.title("Tune a GUI")
root.geometry("640x480")

# btn1 = Button(root, text="Button1")
# btn2 = Button(root, text="Button2")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

btn_f16 = Button(root, text="F16", width=4, height=3)
btn_f17 = Button(root, text="F17", width=4, height=3)
btn_f18 = Button(root, text="F18", width=4, height=3)
btn_f19 = Button(root, text="F19", width=4, height=3)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)


btn_clear = Button(root, text="clear", width=4, height=3)
btn_equal = Button(root, text="=", width=4, height=3)
btn_div = Button(root, text="/", width=4, height=3)
btn_mul = Button(root, text="*", width=4, height=3)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_7 = Button(root, text="7", width=4, height=3)
btn_8 = Button(root, text="8", width=4, height=3)
btn_9 = Button(root, text="9", width=4, height=3)
btn_sub = Button(root, text="-", width=4, height=3)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_4 = Button(root, text="4", width=4, height=3)
btn_5 = Button(root, text="5", width=4, height=3)
btn_6 = Button(root, text="6", width=4, height=3)
btn_add = Button(root, text="+", width=4, height=3)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_1 = Button(root, text="1", width=4, height=3)
btn_2 = Button(root, text="2", width=4, height=3)
btn_3 = Button(root, text="3", width=4, height=3)
btn_enter = Button(root, text="enter", width=4, height=3)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

btn_0 = Button(root, text="0", width=4, height=3)
btn_point = Button(root, text=".", width=4, height=3)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()
