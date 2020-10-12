from tkinter import *
from gui_label import Make_label

class Make_popup():
    def __init__(self, popup_name):
        """the popup size should look like this 500x500 and also as a string"""
        self.popup_name = popup_name
        # self.popup_size = popup_size

        self.popup = Toplevel()
        self.popup.grab_set()
        # self.popup.geometry(self.popup_size) add later for each popup
        self.popup.resizable(False, False)
        self.popup.title(self.popup_name)
        self.popup.configure(bg = '#0d1a3f')

    def error(self, text):
        self.text = text
        error_massage = Make_label(self.popup, self.text, 10, "red", "#0d1a3f")
        error_massage.pack()

    def loading(self):
        print("aa")
        self.popup.geometry("200x50")
        loading = Make_label(self.popup, "loading", 20, "white", "#0d1a3f")
        loading.place(40, 10)

    def exit_popup(self):
        self.popup.destroy()

    
