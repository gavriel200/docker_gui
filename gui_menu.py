import webbrowser
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
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=55, pady=39, command=lambda:self.images_page(), font=("Courier", 16))
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
        activeforeground="#bfbfbf", activebackground="#0e1733", borderwidth=0, padx=40, pady=40, command=lambda:self.containers_page(), font=("Courier", 14))
        self.button.place(x=187,y=0)

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
        f1 = Frame(main_frame, width=440, height=400, bg = "#00080f")
        f1.place(x = 30, y = 130)
        l1 = Make_label(f1, "hello and welcome to SHARK", 17, "white", "#00080f")
        l1.place(35,20)
        l2 = Make_label(f1, "so what is shark?", 12, "white", "#00080f")
        l2.place(30,55)
        l3 = Make_label(f1, "shark is a docker gui designed to help", 13, "white", "#00080f")
        l3.place(30,75)
        l4 = Make_label(f1, "with basic functions that the docker", 13, "white", "#00080f")
        l4.place(30,95)
        l5 = Make_label(f1, "user uses often.", 13, "white", "#00080f")
        l5.place(30,115)
        l6 = Make_label(f1, "this platfor was build in python so its not ideal", 9, "white", "#00080f")
        l6.place(30,150)
        l7 = Make_label(f1, "for a gui.", 9, "white", "#00080f")
        l7.place(30,165)
        l8 = Make_label(f1, "you should watch when you name your images", 9, "white", "#00080f")
        l8.place(30,180)
        l9 = Make_label(f1, "or your containers, some times if the name is", 9, "white", "#00080f")
        l9.place(30,195)
        l10 = Make_label(f1, "too long it will move the buttons and you wont", 9, "white", "#00080f")
        l10.place(30,210)
        l11 = Make_label(f1, "be able to use shark proparly.", 9, "white", "#00080f")
        l11.place(30,225)
        l12 = Make_label(f1, "same goes for when you add ports and vols in image run.", 9, "white", "#00080f")
        l12.place(30,240)
        l13 = Make_label(f1, "i'd be happy for your support (:", 13, "white", "#00080f")
        l13.place(30,320)
        

        def callback(url):
            webbrowser.open_new(url)

        link1 = Label(f1, text="github link", fg="#707ec7", cursor="hand2", bg="#00080f", font=("Courier",13), borderwidth=0)
        link1.place(x=30, y=350)
        link1.bind("<Button-1>", lambda e: callback("https://github.com/gavriel200/docker_gui"))
    
    def invoke(self):
        # -------- press button --------- #
        self.button.invoke()

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
