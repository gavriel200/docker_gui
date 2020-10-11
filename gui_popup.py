from tkinter import *

class Make_popup():
    def __init__(self, popup_name, popup_size):
        """the popup size should look like this 500x500 and also as a string"""
        self.popup_name = popup_name
        self.popup_size = popup_size

        self.app = Toplevel()
        self.app.grab_set()
        self.app.geometry(self.popup_size)
        self.app.resizable(False, False)
        self.app.title(self.popup_name)
        self.app.configure(bg = '#0d1a3f')

    
