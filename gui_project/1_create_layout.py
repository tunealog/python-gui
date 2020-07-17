# Python Project

# Title : Image Edit Program
# Date : 2020-07-17
# Creator : tunealog

import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Tune a GUI")

# File Frame (Add File, Delete File)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="Add File")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="Delete File")
btn_del_file.pack(side="right")

# List Frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Save Path Frame
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Open", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option Frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. Width Option
# Image Width Label
lbl_width = Label(frame_option, text="Width", width=6)
lbl_width.pack(side="left", padx=5, pady=5)

# Image Width Combo
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=6)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. Space Option
# Space Option Label
lbl_space = Label(frame_option, text="Space", width=6)
lbl_space.pack(side="left", padx=5, pady=5)

# Space Option Combo
opt_space = ["None", "Narrow", "Nomal", "Wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=6)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. File Format Option
# File Format Option Label
lbl_format = Label(frame_option, text="Format", width=6)
lbl_format.pack(side="left", padx=5, pady=5)

# File Format Option Combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=6)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Run Frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Quit",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
