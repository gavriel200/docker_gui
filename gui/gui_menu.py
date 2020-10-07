from tkinter import *

class Make_menubutton():
    # ------------------------------------------------   creating the menu-buttons ------------------------------------------------ #
    def __init__(self, master, menu_master, old_frame):
        self.old_frame = old_frame
        self.master = master
        self.menu_master = menu_master

    
    def menu_button_images(self, con_but, sea_but, home_but):
        self.con_but = con_but
        self.sea_but = sea_but
        self.home_but = home_but
        self.button = Button(self.menu_master, text = "images", bg="#0e1733", fg="white", 
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=37, pady=39, command=lambda:self.images_page())
        self.button.place(x=0,y=0)

    def menu_button_containers(self, img_but, sea_but, home_but):
        self.img_but = img_but
        self.sea_but = sea_but
        self.home_but = home_but
        self.button = Button(self.menu_master, text = "containers", bg="#0e1733", fg="white", 
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=27, pady=39, command=lambda:self.containers_page())
        self.button.place(x=125,y=0)

    def menu_button_sea(self, img_but, con_but, home_but):
        self.img_but = img_but
        self.con_but = con_but
        self.home_but = home_but
        self.button = Button(self.menu_master, text = "sea", bg="#0e1733", fg="white", 
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=50, pady=39, command=lambda:self.sea_page())
        self.button.place(x=250,y=0)

    def menu_button_home(self, img_but, con_but, sea_but):
        self.img_but = img_but
        self.con_but = con_but
        self.sea_but = sea_but
        self.button = Button(self.menu_master, text = "home", bg="#0e1733", fg="white", 
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=42, pady=39, command=lambda:self.home_page())
        self.button.place(x=375,y=0)

    # ------------------------------------------------   functions for buttons ------------------------------------------------ #


    # -------- button press related functions -------- #
    def onpage(self, but):
        #function to change the color on the page that we are on more lighter color
        #just need to put in the button obj you want to change color
        self.but = but
        self.but["bg"] = "#102052"
        self.but["activebackground"] = "#102052"

    def notonpage(self, but):
        #function to change the color back to the normal color
        #just need to put in the button obj you want to change color
        self.but = but
        self.but["bg"] = "#0e1733"
        self.but["activebackground"] = "#0e1733"


    # -------- frame related functions -------- #
    def remove_old_frame(self):
            self.old_frame.destroy()

    @staticmethod
    def add_main_frame(master):
        global main_frame
        main_frame = Frame(master, width=500, height=550, bg="#102052")
        main_frame.pack()
    
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
        l = Label(main_frame, text = "images")
        l.place(x=200,y=200)

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
        l = Label(main_frame, text = "containers")
        l.place(x=200,y=200)


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
        l = Label(main_frame, text = "sea")
        l.place(x=200,y=200)

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
        l = Label(main_frame, text = "home")
        l.place(x=200,y=200)