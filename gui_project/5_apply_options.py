# Python Project

# Title : Image Edit Program
# Date : 2020-07-18
# Creator : tunealog

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *  # __all__
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Tune a GUI")

# Add File


def add_file():
    files = filedialog.askopenfiles(title="Select Images",
                                    filetypes=(("PNG File", "*.png"),
                                               ("All File", "*.*")),
                                    # Raw Srtring
                                    initialdir=r"/Users/macbookair/Desktop/python/")
    for file in files:
        list_file.insert(END, file.name)

# Delete File


def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# Save Path


def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# Merge Image


def merge_image():

    try:
        # Image Width
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1
        else:
            img_width = int(img_width)

        # Image Space
        img_space = cmb_space.get()
        if img_space == "Narrow":
            img_space = 30
        elif img_space == "Normal":
            img_space = 60
        elif img_space == "Wide":
            img_space = 90
        else:
            img_space = 0

        # Image Format
        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]

        # Image Size Process
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(
                img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        # MAX Width, Total Height
        max_width, total_height = max(widths), sum(heights)

        # Create SketchBook
        if img_space > 0:
            total_height += (img_space * (len(images)-1))

        result_img = Image.new(
            "RGB", (max_width, total_height), (255, 255, 255))

        # y Position Information
        y_offset = 0

        for idx, img in enumerate(images):

            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        # Format Option Process
        file_name = "photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Alert", "Edit Complete")

    except Exception as err:
        msgbox.showerror("Error", err)

# Start


def start():

    # File Check
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add Images")
        return
    # Save Path Check
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select the save path")

    merge_image()


# File Frame (Add File, Delete File)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=10,
                      text="Add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10,
                      text="Delete File", command=del_file)
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

btn_dest_path = Button(path_frame, text="Open",
                       width=10, command=browse_dest_path)
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
opt_space = ["None", "Narrow", "Normal", "Wide"]
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

btn_start = Button(frame_run, padx=5, pady=5,
                   text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
