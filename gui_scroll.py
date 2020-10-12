from tkinter import *
from docker_command import Docker_images
from gui_label import Make_label
from gui_button import Make_button

class Make_scrollbar():
    # ------------------------------------------------   creating the Scrollbar ------------------------------------------------ #
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

    # Reset the scroll region to encompass the inner frame
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))    

    # -----------------------------------------   adding diffrenrt widgets for each page ---------------------------------------- #

    # ---------------- images page ----------------- #
    def image_page_scrollbar(self):
        self.run_image = PhotoImage(file="./run_button.png")
        self.edit_image = PhotoImage(file="./edit_button.png")
        self.save_image = PhotoImage(file="./save_button.png")
        self.rm_image = PhotoImage(file="./rm_button.png")

        self.rep = Make_label(self.frame, "    rep   ", 10, "white", "#0e1733")
        self.rep.grid(0,0)
        self.tag = Make_label(self.frame, "|   tag  |", 10, "white", "#0e1733")
        self.tag.grid(1,0)
        self.image_id = Make_label(self.frame, "  id     ", 10, "white", "#0e1733")
        self.image_id.grid(2,0)
        self.created = Make_label(self.frame, "|created ", 10, "white", "#0e1733")
        self.created.grid(3,0)
        self.size = Make_label(self.frame, "| size ", 10, "white", "#0e1733")
        self.size.grid(4,0)

        images = Docker_images.list_images()

        row = 1
        for rows in images:
            if len(rows[0]) > 10:
                Label(self.frame, text=rows[0], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=0)
            else:
                Label(self.frame, text=rows[0], bg="#0e1733", font=("Courier",9), fg="white").grid(row=row, column=0)
            if len(rows[1]) > 10:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=1)
            else:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",9), fg="white").grid(row=row, column=1)
            Label(self.frame, text=rows[2], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=2)
            Label(self.frame, text=(str(rows[3])+" "+str(rows[4])+" "+str(rows[5])), bg="#0e1733", font=("Courier",7), fg="white").grid(row=row, column=3)
            Label(self.frame, text=rows[6], bg="#0e1733", font=("Courier",10), fg="white").grid(row=row, column=4)
            Button(self.frame, image = self.run_image, cursor="hand2", borderwidth=0).grid(row=row, column=5)
            Button(self.frame, image = self.edit_image, cursor="hand2", borderwidth=0).grid(row=row, column=6)
            Button(self.frame, image = self.save_image, cursor="hand2", borderwidth=0).grid(row=row, column=7)
            Button(self.frame, image = self.rm_image, cursor="hand2", borderwidth=0).grid(row=row, column=8)
            row = row + 1
    
    # --------------- containers page --------------- #

    # --------------- sea page --------------- #
