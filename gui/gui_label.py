from tkinter import *

class Make_label():
    def __init__(self, master, text, font_size, font_color, bg_color):
        self.master = master
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color
        self.label = Label(self.master, text=self.text, font=("Courier",self.font_size), fg=self.font_color, bg=self.bg_color, borderwidth=0)

    def place(self, x, y):
        self.x = x
        self.y = y
        self.label.place(x = self.x, y = self.y)