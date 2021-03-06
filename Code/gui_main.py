from tkinter import *

from gui_menu import Make_menubutton


class MainApplication():
# ---------------- creating the main app ----------------------------------------- #
    def __init__(self):
        self.app = Tk()
        self.app.geometry('500x550')
        self.app.resizable(False, False)
        self.app.title("Shark")
        self.app.configure(bg = '#0e1733')
        # self.app.iconbitmap("/shark.ico") # for windows

        # ---------------- create frames --------------- #
        self.top_frame = Frame(self.app, width=500, height=100, bg="#0e1733") # not visible used to place the menu button on the top
        self.top_frame.place(x=0,y=0)

        self.startup_frame = Frame(self.app, width=500, height=450, bg="#0e1733") # visible when opened
        self.startup_frame.place(x=0,y=100)

        # ---------------- create menu buttons --------- #
        self.menu_images = Make_menubutton(self.top_frame, self.app, self.startup_frame)
        self.menu_images.menu_button_images()
        self.menu_containers = Make_menubutton(self.top_frame, self.app, self.startup_frame)
        self.menu_containers.menu_button_containers()
        self.menu_home = Make_menubutton(self.top_frame, self.app, self.startup_frame)
        self.menu_home.menu_button_home()
        self.menu_home.invoke()

        # ---------------- mainloop -------------------- #
        self.app.mainloop()

if __name__ == "__main__":
    root = MainApplication()
