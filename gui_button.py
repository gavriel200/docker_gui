from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilename

from docker_command import Docker_images
from gui_label import Make_label
from gui_popup import Make_popup


class Make_button():
# ---------------- create __init__ button ---------------------------------------- #
    def __init__(self, master, text, width, height, color, font_size, font_color):
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.color = color
        self.font_size = font_size
        self.font_color = font_color

# ---------------- create image upload button ------------------------------------ #
    def images_upload(self, reload):
        # needs a loading effect while the image is uploaded
        self.reload = reload
        self.button = Button(self.master, text = self.text, width = self.width, height = self.height, bg = self.color, 
        fg = self.font_color, font=("Courier", self.font_size), cursor="hand2", borderwidth=0, command=lambda:self.image_upload_browse(self.reload))

# ---------------- function for image upload button ------------------------------ #
    def image_upload_browse(self, reload):
        # needs a loading effect while the image is uploaded
        self.reload = reload
        # -------- open file exp -------- #
        filename = askopenfilename(initialdir = "~", title = "Select a .tar File", filetypes = (("docker image tar files", "*.tar*"), ("all files", "*.*")))
        if len(filename)==0:
            pass
        else:
            com = Docker_images.load_image(filename)
            print(com)
            if com[0]==1:
                error_popup = Make_popup("ERROR")
                error_popup.error(com[1]) 
            else:
                self.reload()

# ---------------- placing the button -------------------------------------------- #
    def place(self, x, y):
        self.x = x
        self.y = y
        self.button.place(x = self.x, y = self.y)

    def grid(self, col ,row):
        self.col = col
        self.row = row
        self.button.grid(column = self.col, row = self.row) 

class Make_image_button():
# ---------------- create __init__ image button ---------------------------------- #
    def __init__(self, master, dir_to_image):
        self.master = master
        self.dir_to_image = dir_to_image
        self.image = PhotoImage(file=self.dir_to_image)
        self.button = Button(self.master, image = self.image, cursor="hand2", borderwidth=0)

# ---------------- image page buttons -------------------------------------------- #
    # ---------------- run ------------------------- #
    def run_image(self, rep_tag, reload_image_page):
        self.reload_image_page =reload_image_page
        self.rep_tag = rep_tag
        self.button.configure(command=self.run_image_function)

    def run_image_function(self):
        self.pop_up = Make_popup("RUN IMAGE")
        self.pop_up.run_image_popup(self.rep_tag, self.reload_image_page)

    # ---------------- edit ------------------ #
    def edit_image(self, rep_tag, reload_image_page):
        self.reload_image_page =reload_image_page
        self.rep_tag = rep_tag
        self.button.configure(command=self.edit_image_function)

    def edit_image_function(self):
        self.pop_up = Make_popup("EDIT IMAGE NAME")
        self.pop_up.edit_image_popup(self.rep_tag, self.reload_image_page)

    # ---------------- save ------------------------ #
    def save_image(self, rep_tag, reload_image_page):
        self.reload_image_page =reload_image_page
        self.rep_tag = rep_tag
        self.button.configure(command=self.save_image_function)

    def save_image_function(self):
        self.pop_up = Make_popup("SAVE IMAGE TO FILE")
        self.pop_up.save_image_popup(self.rep_tag, self.reload_image_page)

    # ---------------- remove ---------------------- #
    def rm_image(self, rep_tag, reload_image_page):
        self.reload_image_page =reload_image_page
        self.rep_tag = rep_tag
        self.button.configure(command=self.rm_image_function)

    def rm_image_function(self):
        self.pop_up = Make_popup("REMOVE IMAGE")
        self.pop_up.rm_image_popup(self.rep_tag, self.reload_image_page)

# ---------------- placing the image button -------------------------------------- #
    def place(self, x, y):
        self.x = x
        self.y = y
        self.button.place(x = self.x, y = self.y)

    def grid(self, col ,row):
        self.col = col
        self.row = row
        self.button.grid(column = self.col, row = self.row) 
