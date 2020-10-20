from tkinter import *

from docker_command import Docker_images
from docker_command import Docker_container
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
        self.img_rep_label = Make_label(self.frame, "    rep   ", 10, "white", "#0e1733")
        self.img_rep_label.grid(0,0)
        self.img_tag_label = Make_label(self.frame, "|   tag  |", 10, "white", "#0e1733")
        self.img_tag_label.grid(1,0)
        self.img_image_id_label = Make_label(self.frame, "  id     ", 10, "white", "#0e1733")
        self.img_image_id_label.grid(2,0)
        self.img_created_label = Make_label(self.frame, "|created ", 10, "white", "#0e1733")
        self.img_created_label.grid(3,0)
        self.img_size_label = Make_label(self.frame, "| size ", 10, "white", "#0e1733")
        self.img_size_label.grid(4,0)

        # -------- get images list ------ #
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
            self.img_run_button = Make_image_button(self.frame, "./images/run_button.png")
            self.img_run_button.run_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.img_run_button.grid(5, row)
            self.img_edit_button = Make_image_button(self.frame, "./images/edit_button.png")
            self.img_edit_button.edit_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.img_edit_button.grid(6, row)
            self.img_save_button = Make_image_button(self.frame, "./images/save_button.png")
            self.img_save_button.save_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.img_save_button.grid(7, row)
            self.img_rm_button = Make_image_button(self.frame, "./images/rm_button.png")
            self.img_rm_button.rm_image(rows[0]+":"+rows[1], self.reload_image_page)
            self.img_rm_button.grid(8, row)
            row = row + 1

    # ---------------- containers ------------------- #
    def containers_page_scrollbar(self, reload_container_page):
        # -------- reload page fun ------ #
        self.reload_container_page = reload_container_page
        # -------- menu bar ~ ----------- #
        self.cont_name_label = Make_label(self.frame, "    name   ", 10, "white", "#0e1733")
        self.cont_name_label.grid(0,0)
        self.cont_cont_id_label = Make_label(self.frame, "| container id", 10, "white", "#0e1733")
        self.cont_cont_id_label.grid(1,0)
        self.cont_image_label = Make_label(self.frame, "|     image     |", 10, "white", "#0e1733")
        self.cont_image_label.grid(2,0)
        # -------- get containers list ---#
        containers = Docker_container.list_containers()
        running_containers = Docker_container.running_containers() #lists ids of running contianers
        
        row = 1
        for rows in containers:
            # -------- adding the containers - #
            if len(rows[-1]) > 20:
                Label(self.frame, text=rows[-1], bg="#0e1733", font=("Courier",6), fg="white").grid(row=row, column=0)
            else:
                Label(self.frame, text=rows[-1], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=0)
            Label(self.frame, text=rows[0], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=1)
            if len(rows[1]) > 21:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",6), fg="white").grid(row=row, column=2)
            else:
                Label(self.frame, text=rows[1], bg="#0e1733", font=("Courier",8), fg="white").grid(row=row, column=2)
            
            # -------- adding the buttons --- #
            if rows[0] in running_containers:
                self.cont_start_stop_button = Make_image_button(self.frame, "./images/stop_button_cont.png")
                self.cont_start_stop_button.start_stop_container(rows[0], self.reload_container_page)
                self.cont_start_stop_button.grid(3, row)
                self.cont_bash_button = Make_image_button(self.frame, "./images/bash_button_on_cont.png")
                self.cont_bash_button.bash_on_container(rows[0], self.reload_container_page)
                self.cont_bash_button.grid(4, row)
            else:
                self.cont_start_stop_button = Make_image_button(self.frame, "./images/start_button_cont.png")
                self.cont_start_stop_button.start_stop_container(rows[0], self.reload_container_page)
                self.cont_start_stop_button.grid(3, row)
                self.cont_bash_button = Make_image_button(self.frame, "./images/bash_button_off_cont.png")
                self.cont_bash_button.bash_off_container(rows[0], self.reload_container_page)
                self.cont_bash_button.grid(4, row)
            self.cont_save_button = Make_image_button(self.frame, "./images/save_button.png")
            self.cont_save_button.save_container(rows[0], self.reload_container_page)
            self.cont_save_button.grid(5, row)
            self.cont_rm_button = Make_image_button(self.frame, "./images/rm_button.png")
            self.cont_rm_button.rm_container(rows[0], self.reload_container_page, rows[-1])
            self.cont_rm_button.grid(6, row)
            row = row + 1

    # ---------------- sea -------------------------- #
