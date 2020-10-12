from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilename

from docker_command import Docker_images
from gui_label import Make_label
from gui_popup import Make_popup


class Make_button():
    # ------------------------------------------------   creating button ------------------------------------------------ #
    def __init__(self, master, text, width, height, color, font_size, font_color):
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.color = color
        self.font_size = font_size
        self.font_color = font_color
        
        # self.button = Button(self.master, text = self.text, width = self.width, height = self.height, bg = self.color, 
        # fg = self.font_color, font=("Courier", self.font_size), cursor="hand2", borderwidth=0)

    # -------------------------------------------   images page -------------------------------------------- #

    # ------------------------ creating upload button ------------------------- #
    def images_upload(self, reload):
        # needs a loading effect while the image is uploaded
        self.reload = reload
        self.button = Button(self.master, text = self.text, width = self.width, height = self.height, bg = self.color, 
        fg = self.font_color, font=("Courier", self.font_size), cursor="hand2", borderwidth=0, command=lambda:self.image_upload_browse(self.reload))
    
    # ------------------------------------------------   button functions ------------------------------------------------ #
    
    def image_upload_browse(self, reload):
        # needs a loading effect while the image is uploaded
        self.reload = reload
        filename = askopenfilename(initialdir = "~", title = "Select a .tar File", filetypes = (("docker image tar files", "*.tar*"), ("all files", "*.*")))
        if len(filename)==0:
            pass
        else:
            com = Docker_images.load_image(filename)
            print(com)
            if com[0]==1:
                self.error_popup(com[1])
            else:
                self.reload()

    def error_popup(self, text):
        self.text = text
        self.app = Make_popup("Error")
        self.app.error(self.text)

    # ------------------------------------------------   button possioning ----------------------------------------------- #

    # ------------------------ placing the button widget ------------------------ #
    def place(self, x, y):
        self.x = x
        self.y = y
        self.button.place(x = self.x, y = self.y)

    # ------------------- putting the button widget on a grid ------------------- #
    def grid(self, col ,row):
        self.col = col
        self.row = row
        self.button.grid(column = self.col, row = self.row) 
