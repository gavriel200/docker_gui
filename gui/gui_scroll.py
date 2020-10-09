
from tkinter import *

class Make_scrollbar():

    def __init__(self, master, width, height, canvas_color, frame_color):

        self.master = master
        self.width = width
        self.height = height
        self.canvas_color = canvas_color
        self.frame_color = frame_color

        self.canvas = Canvas(self.master, borderwidth=0, background=self.canvas_color, width = self.width, height=self.height)
        self.frame = Frame(self.canvas, background=self.frame_color)
        self.vsb = Scrollbar(self.master, orient="vertical", cursor="hand2", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="bottom", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            t="this is the second column for row %s" %row
            Label(self.frame, text=t, bg="#102052", font=("Courier",10), fg="white").grid(row=row, column=0)

    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
