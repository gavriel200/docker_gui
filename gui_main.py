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
        self.frame_menu = Frame(self.app, width=500, height=100, bg="#0e1733") # not visible
        self.frame_menu.place(x=0,y=0)

        self.frame_start = Frame(self.app, width=500, height=450, bg="red") # visible when opened
        self.frame_start.place(x=0,y=100)

        # ---------------- create menu buttons --------- #
        self.menu_images = Make_menubutton(self.frame_menu, self.app, self.frame_start)
        self.menu_images.menu_button_images()
        self.menu_containers = Make_menubutton(self.frame_menu, self.app, self.frame_start)
        self.menu_containers.menu_button_containers()
        self.menu_sea = Make_menubutton(self.frame_menu, self.app, self.frame_start)
        self.menu_sea.menu_button_sea()
        self.menu_home = Make_menubutton(self.frame_menu, self.app, self.frame_start)
        self.menu_home.menu_button_home()

        # ---------------- mainloop -------------------- #
        self.app.mainloop()

if __name__ == "__main__":
    root = MainApplication()
