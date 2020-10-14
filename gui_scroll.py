from tkinter import *

from docker_command import Docker_images
from gui_button import Make_button
from gui_button import Make_image_button
from gui_label import Make_label
from gui_popup import Make_popup


class Make_scrollbar():
# ---------------- create __init__ a scrollbar ----------------------------------- #
    def __init__(self, master, width, height, canvas_color, frame_color):
        # -------- create init ---------- # 
        self.master = master
        self.width = width
        self.height = height
        self.canvas_color = canvas_color
        self.frame_color = frame_color

        # -------- create the scrollbar - # 
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

# ---------------- populate scrollbar -------------------------------------------- #
    # ---------------- images ----------------------- #
    def image_page_scrollbar(self, reload_image_page):
        # -------- reload page fun ------ #
        self.reload_image_page = reload_image_page
        # -------- menu bar ~ ----------- #
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

        # -------- get list of images --- #
        images = Docker_images.list_images()

        row = 1
        for rows in images:
            # -------- adding the images ---- #
            if len(rows[0]) > 10:
                Label(self.frame, text=rows[0], bg="#0e1733", font=("Courier",7), fg="white").grid(row=row, column=0)
            else:
                Label(self.frame, text=rows[0], bg="#0e1733", font=("Courier",9), fg="white").grid(row=row, column=0)
            if len(rows[1]) > 10:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",7), fg="white").grid(row=row, column=1)
            else:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",9), fg="white").grid(row=row, column=1)
            Label(self.frame, text=rows[2], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=2)
            Label(self.frame, text=(str(rows[3])+" "+str(rows[4])+" "+str(rows[5])), bg="#0e1733", font=("Courier",7), fg="white").grid(row=row, column=3)
            Label(self.frame, text=rows[6], bg="#0e1733", font=("Courier",10), fg="white").grid(row=row, column=4)

            # -------- adding the buttons --- #
            self.run = Make_image_button(self.frame, "./run_button.png")
            self.run.run_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.run.grid(5, row)
            self.edit = Make_image_button(self.frame, "./edit_button.png")
            self.edit.edit_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.edit.grid(6, row)
            self.save = Make_image_button(self.frame, "./save_button.png")
            self.save.save_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.save.grid(7, row)
            self.rm = Make_image_button(self.frame, "./rm_button.png")
            self.rm.rm_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.rm.grid(8, row)
            row = row + 1

    # ---------------- containers ------------------- #

    # ---------------- sea -------------------------- #
