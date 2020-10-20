from tkinter import *

from docker_command import Docker_images
from gui_button import Make_button
from gui_label import Make_label
from gui_scroll import Make_scrollbar


class Make_menubutton():
# ---------------- create __init__ menu button ----------------------------------- #
    def __init__(self, top_frame, app_frame, startup_frame):
        self.top_frame = top_frame
        self.app_frame = app_frame
        self.startup_frame = startup_frame

# ---------------- menu buttons -------------------------------------------------- #
    # ---------------- images ----------------------- #
    def menu_button_images(self):
        self.button = Button(self.app_frame, text = "images", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=22, pady=39, command=lambda:self.images_page(), font=("Courier", 16))
        self.button.place(x=0,y=0)

    def images_page(self):
        # -------- reload page ---------- #
        try:
            self.remove_startup_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.top_frame)
        # -------- add scrollbar -------- #
        self.scrollbar_images = Make_scrollbar(scrollbar_frame, 485, 375, "#0e1733", "#0e1733")
        self.scrollbar_images.image_page_scrollbar(self.images_page)
        # -------- upload button -------- #
        self.upload_button = Make_button(main_frame, "upload", 0, 0, "#344658", 18, "white")
        self.upload_button.images_upload(self.images_page)
        self.upload_button.place(380, 120)

    # ---------------- containers ------------------- #
    def menu_button_containers(self):
        self.button = Button(self.app_frame, text = "containers", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=6, pady=40, command=lambda:self.containers_page(), font=("Courier", 14))
        self.button.place(x=125,y=0)

    def containers_page(self):
        # -------- reload page ---------- #
        try:
            self.remove_startup_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.top_frame)
        # -------- add scrollbar -------- #
        self.scrollbar_images = Make_scrollbar(scrollbar_frame, 485, 375, "#0e1733", "#0e1733")
        self.scrollbar_images.containers_page_scrollbar(self.containers_page)

    # ---------------- sea -------------------------- #
    def menu_button_sea(self):
        self.button = Button(self.app_frame, text = "sea", bg="#0e1733", fg="white", cursor="hand2",
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=34, pady=34, command=lambda:self.sea_page(), font=("Courier", 23))
        self.button.place(x=250,y=0)

    def sea_page(self):
        # -------- reload page ---------- #
        try:
            self.remove_startup_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.top_frame)
        l1 = Make_label(main_frame, "sea", 16, "#ffffff", "#203165")
        l1.place(200,200)

    # ---------------- home ------------------------- #
    def menu_button_home(self):
        self.image = PhotoImage(file="./images/shark2.png")
        self.button = Button(self.app_frame, image=self.image, borderwidth=0, cursor="hand2", command=lambda:self.home_page())
        self.button.place(x=375,y=0)

    def home_page(self):
        # -------- reload page ---------- #
        try:
            self.remove_startup_frame()
        except:
            pass
        try:
            self.remove_main_frame(main_frame)
        except:
            pass
        self.add_main_frame(self.top_frame)
        l1 = Make_label(main_frame, "home", 16, "#ffffff", "#203165")
        l1.place(200,200)

# ---------------- other functions ----------------------------------------------- #
    # ---------------- frame related --------------- #
    def remove_startup_frame(self):
            self.startup_frame.destroy()

    @staticmethod
    def add_main_frame(top_frame):
        global main_frame
        global scrollbar_frame
        main_frame = Frame(top_frame, width=500, height=550, bg="#0e1733")
        main_frame.pack()

        #this is an invisble label to pulldown the main frame
        Label(main_frame, height=10, bg="#0e1733", borderwidth=0).grid(row=0,column=0)

        scrollbar_frame = Frame(main_frame, width=500, height=550, bg="#0e1733")
        scrollbar_frame.grid(row=3,column=0)
    
    @staticmethod
    def remove_main_frame(frame):
            frame.destroy()
