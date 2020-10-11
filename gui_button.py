from tkinter import *
from tkinter.filedialog import askopenfilename

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
        
        self.button = Button(self.master, text = self.text, width = self.width, height = self.height, bg = self.color, 
        fg = self.font_color, font=("Courier", self.font_size), cursor="hand2", borderwidth=0)

    def images_upload(self):
        self.button.config(command=self.image_upload_browse)

    # ------------------------------------------------   button functions ------------------------------------------------ #
    
    def image_upload_browse(self):
        filename = askopenfilename(initialdir = "~", title = "Select a .tar File", filetypes = (("docker image tar files", "*.tar*"), ("all files", "*.*")))
        if len(filename)==0:
            pass
        else:
            print(filename)

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
