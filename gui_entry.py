from tkinter import *

class Make_entry():
    def __init__(self, master, width):
        self.master = master
        self.width = width
    
        self.entry = Entry(self.master, width = self.width)

    def get_entry(self):
        self.entry.get()

        # ------------------------ placing the entry widget ------------------------ #
    def place(self, x, y):
        self.x = x
        self.y = y
        self.entry.place(x = self.x, y = self.y)

    # ------------------- putting the entry widget on a grid ------------------- #
    def grid(self, col, row):
        self.col = col
        self.row = row
        self.entry.grid(column=self.col, row=self.row)

    # ----------------------------- just pack it ------------------------------- #
    def pack(self):
        self.entry.pack()