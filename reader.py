from tkinter import filedialog as fd
import tkinter as tk
from tkinter import ttk
import os
import customtkinter as ctk
from customtkinter import CTk
from PIL import Image, ImageTk
import re


width = 1500
height = 2000


def next_page(file_list, index):
    global cur_index
    img_path = os.path.join(base_dir, file_list[index + 1])
    image = Image.open(img_path)
    image_ctk = ctk.CTkImage(light_image=image, size=(width, height))
    label.configure(image=image_ctk)
    cur_index += 1
    print(index)


def prev_page(file_list, index):
    global cur_index
    img_path = os.path.join(base_dir, file_list[index - 1])
    image = Image.open(img_path)
    image_ctk = ctk.CTkImage(light_image=image, size=(width, height))
    label.configure(image=image_ctk)
    cur_index -= 1
    print(index)


def list_dir(file):
    b_dir = '/'.join([part for part in file.rsplit('/', 1)][:1])
    file_name = os.path.basename(file)
    dir_list = os.listdir(b_dir)
    sorted_filenames = sorted(dir_list, key=lambda x: int(x.split('.')[0]))
    return sorted_filenames, b_dir, file_name


app = ctk.CTk()
app.title("Manga App")
ctk.set_appearance_mode("dark")
app._state_before_windows_set_titlebar_color = 'zoomed'

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Pick an Image
filename = fd.askopenfilename(initialdir="C:\D\BILDER\Iwas\Bilder\Comics\Selenium", title="Select Image")

# Create sorted list of files in directory
f_list, base_dir, name = list_dir(filename)
cur_index = f_list.index(name)

first_image = Image.open(filename)
first_image_ctk = ctk.CTkImage(light_image=first_image, size=(width, height))

my_frame = ctk.CTkScrollableFrame(master=app, width=width, height=height, corner_radius=0, fg_color="transparent")
my_frame.grid(row=0, column=0, sticky="n")

label = ctk.CTkLabel(my_frame, text="", image=first_image_ctk)
label.grid(row=0, column=0, padx=20)

next_button = ctk.CTkButton(app, text="", command=lambda: next_page(f_list, cur_index))
next_button.grid(row=0, column=0, sticky="e")

prev_button = ctk.CTkButton(app, text="<<<", command=lambda: prev_page(f_list, cur_index))
prev_button.grid(row=0, column=0, sticky="w")

app.mainloop()