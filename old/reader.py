from tkinter import filedialog as fd
import os
import customtkinter as ctk
from PIL import Image


# NOT CONTINUED
# TESTING TKINTER

width = 1800
height = 2700


def right_arrow_pressed(event):
    next_page(f_list, cur_index)


def left_arrow_pressed(event):
    prev_page(f_list, cur_index)


def next_page(file_list, index):
    global cur_index
    img_path = os.path.join(base_dir, file_list[index + 1])
    image = Image.open(img_path)
    image_ctk = ctk.CTkImage(light_image=image, size=(width, height))
    label.configure(image=image_ctk)
    cur_index += 1


def prev_page(file_list, index):
    global cur_index
    img_path = os.path.join(base_dir, file_list[index - 1])
    image = Image.open(img_path)
    image_ctk = ctk.CTkImage(light_image=image, size=(width, height))
    label.configure(image=image_ctk)
    cur_index -= 1


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
app.bind('<KeyRelease-Right>', right_arrow_pressed)
app.bind('<KeyPress-Left>', left_arrow_pressed)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


# Pick an Image
filename = fd.askopenfilename(initialdir="C:\D\BILDER\Iwas\Bilder\Comics\Selenium", title="Select Image")

# Create sorted list of files in directory
f_list, base_dir, name = list_dir(filename)
cur_index = f_list.index(name)

first_image = Image.open(filename)
first_image_ctk = ctk.CTkImage(light_image=first_image, size=(width, height))

my_frame = ctk.CTkScrollableFrame(master=app, width=2560, height=3000, corner_radius=0, fg_color="transparent")
my_frame.grid(row=0, column=0, padx=20, sticky="nsew")

label = ctk.CTkLabel(my_frame, text="", image=first_image_ctk)
label.grid(row=0, column=0, padx=350, sticky="e")

next_button = ctk.CTkButton(app, text=">>>", command=lambda: next_page(f_list, cur_index))
next_button.grid(row=0, column=0, padx=50, sticky="e")

prev_button = ctk.CTkButton(app, text="<<<", command=lambda: prev_page(f_list, cur_index))
prev_button.grid(row=0, column=0, padx=50, sticky="w")

app.mainloop()