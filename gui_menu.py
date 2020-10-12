from tkinter import *

from docker_command import Docker_images
from gui_button import Make_button
from gui_label import Make_label
from gui_scroll import Make_scrollbar


class Make_menubutton():
    # ------------------------------------------------   creating the menu-buttons ------------------------------------------------ #
    def __init__(self, master, menu_master, old_frame):
        self.old_frame = old_frame
        self.master = master
        self.menu_master = menu_master
        self.image = PhotoImage(file="./shark2.png")
    
    def menu_button_images(self):
        self.button = Button(self.menu_master, text = "images", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=22, pady=39, command=lambda:self.images_page(), font=("Courier", 16))
        self.button.place(x=0,y=0)

    def menu_button_containers(self):
        self.button = Button(self.menu_master, text = "containers", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=6, pady=40, command=lambda:self.containers_page(), font=("Courier", 14))
        self.button.place(x=125,y=0)

    def menu_button_sea(self):
        self.button = Button(self.menu_master, text = "sea", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=34, pady=34, command=lambda:self.sea_page(), font=("Courier", 23))
        self.button.place(x=250,y=0)

    def menu_button_home(self):
        self.button = Button(self.menu_master, image=self.image, borderwidth=0, cursor="hand2", command=lambda:self.home_page())
        self.button.place(x=375,y=0)

    # ------------------------------------------------   functions for buttons ------------------------------------------------ #

    # -------- frame related functions -------- #
    def remove_old_frame(self):
            self.old_frame.destroy()

    @staticmethod
    def add_main_frame(master):
        global main_frame
        global scrollbar_frame
        main_frame = Frame(master, width=500, height=550, bg="#0d1a3f")
        main_frame.pack()

        #this is an invisble label to pulldown the main frame
        Label(main_frame, height=10, bg="#0d1a3f", borderwidth=0).grid(row=0,column=0)

        scrollbar_frame = Frame(main_frame, width=500, height=550, bg="#0d1a3f")
        scrollbar_frame.grid(row=3,column=0)
    
    @staticmethod
    def remove_main_frame(frame):
            frame.destroy()

    # ------------------------------------------------   main functions for the menu buttons   ------------------------------------------------ #
    
    # ---------------- images_page ----------------- #
    def images_page(self):
        try:
            self.remove_old_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.master)
        self.scrollbar = Make_scrollbar(scrollbar_frame, 485, 375, "#0e1733", "#0e1733")
        self.scrollbar.image_page_scrollbar()
        # needs a loading effect while the image is uploaded
        self.button_upload = Make_button(main_frame, "upload", 0, 0, "#344658", 18, "white")
        self.button_upload.images_upload(self.images_page)
        self.button_upload.place(380, 120)

    # --------------- containers_page --------------- #
    def containers_page(self):
        try:
            self.remove_old_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.master)
        l1 = Make_label(main_frame, "containers", 16, "#ffffff", "#203165")
        l1.place(200,200)

    # ------------------- sea_page ------------------ #
    def sea_page(self):
        try:
            self.remove_old_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.master)
        l1 = Make_label(scrollbar_frame, "sea", 16, "#ffffff", "#203165")
        l1.place(200,200)

    # ------------------ home_page ------------------- #
    def home_page(self):
        try:
            self.remove_old_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.master)
        l1 = Make_label(scrollbar_frame, "home", 16, "#ffffff", "#203165")
        l1.place(200,200)
