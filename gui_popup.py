from tkinter import *
from tkinter import filedialog

from docker_command import Docker_images
from gui_label import Make_label

# -------------------------------------------------------------------------------- #
# ----------------

class Make_popup():
# ---------------- create __init__ popup ----------------------------------------- #
    def __init__(self, popup_name):
        self.popup_name = popup_name
        self.popup = Toplevel()
        self.popup.grab_set()
        self.popup.resizable(False, False)
        self.popup.title(self.popup_name)
        self.popup.configure(bg = '#0e1733')

# ---------------- error popups -------------------------------------------------- #
    def error(self, text):
        self.text = text
        error_massage = Make_label(self.popup, self.text, 18, "red", "#0e1733")
        error_massage.pack()

# ---------------- images page popup --------------------------------------------- #
    # ---------------- run ------------------------- #
    def run_image_popup(self, rep_tag, reload_page):
        self.rep_tag = rep_tag
        # -------- reload main gui ------ #
        self.reload_page = reload_page
        
        self.bash = False
        self.popup.geometry("350x350")

        self.port = []
        self.vol = []
        self.name = []
        
        self.main_frame = Frame(self.popup, width=350, height=300, bg="#0e1733")
        self.main_frame.pack()
        
        # -------- main page build ------ #
        def update_page():
        # ---------------- frame remove old add new ---- #
            # -------- removing old frame ----#
            try:
                self.main_frame.destroy()
            except:
                pass
            # -------- add new frame -------- #
            self.main_frame = Frame(self.popup, width=350, height=350, bg="#0e1733")
            self.main_frame.pack()

            # -------- add frame for color -- #
            self.frame_for_the_color = Frame(self.main_frame,  width=330, height=80, bg="#344658")
            self.frame_for_the_color.place(x = 10, y = 160)

            # -------- add frame vols ports - #
            self.port_vol_frame = Frame(self.main_frame,  width=330, height=80, bg="#344658")
            self.port_vol_frame.place(x = 10, y = 160)

            # -------- docker image name ---- #
            self.docker_run_label = Make_label(self.main_frame, "docker run " + self.rep_tag, 11, "white", "#0e1733")
            self.docker_run_label.place(15, 20)

            # -------- host and conainer ---- #
            self.host_label = Make_label(self.main_frame, "host", 15, "white", "#0e1733")
            self.host_label.place(30,93)
            self.cont_label = Make_label(self.main_frame, "container", 13, "white", "#0e1733")
            self.cont_label.place(126,93)

        # ---------------- ports ----------------------- #
            # -------- entry ports ---------- #
            self.port_host = Entry(self.main_frame, width = 10)
            self.port_host.place(x = 10, y = 60)
            self.port_cont = Entry(self.main_frame, width = 10)
            self.port_cont.place(x = 130, y = 60)
            self.port_host_cont = Make_label(self.main_frame, ":", 18, "White", "#0e1733")
            self.port_host_cont.place(105, 60)

            # -------- add port but --------- #
            self.port_add = Button(self.main_frame, text="add port", bg="#344658", font=("Courier",9), fg = "white", padx=21, 
            command = lambda : port_add_function(self.port_host.get(), self.port_cont.get()), cursor="hand2")
            self.port_add.place(x = 235, y = 60)

        # ---------------- volumes --------------------- #
            # -------- entry vols ----------- #
            self.vol_host = Entry(self.main_frame, width = 10)
            self.vol_host.place(x = 10, y = 120)
            self.vol_cont = Entry(self.main_frame, width = 10)
            self.vol_cont.place(x = 130, y = 120)
            self.vol_host_cont = Make_label(self.main_frame, ":", 18, "White", "#0e1733")
            self.vol_host_cont.place(105, 120)

            # -------- add volumes but ------ #
            self.vol_add = Button(self.main_frame, text="add vol", bg="#344658", font=("Courier",9), fg = "white", padx=25, 
            command = lambda : vol_add_function(self.vol_host.get(), self.vol_cont.get()), cursor="hand2")
            self.vol_add.place(x = 235, y = 120)
            
        # ---------------- added ports and vols -------- #
            # -------- vols and ports label - #
            self.ports_list = Make_label(self.port_vol_frame, "ports: ", 12, "white", "#344658")
            self.ports_list.grid(0,0)
            self.space = Make_label(self.port_vol_frame, "", 12, "white", "#344658")
            self.space.grid(0,1)
            self.vols_list = Make_label(self.port_vol_frame, "vols: ", 12, "white", "#344658")
            self.vols_list.grid(0,2)

            # -------- ports and vols list -- #
            col = 1
            for items in self.port:
                self.port_from_list = Remove_vols_and_ports(self.port_vol_frame, items, self.port, update_page)
                self.port_from_list.grid(col, 0)
                col=col+1
            col = 1
            for items in self.vol:
                self.vol_from_list = Remove_vols_and_ports(self.port_vol_frame, items, self.vol, update_page)
                self.vol_from_list.grid(col, 2)
                col=col+1

        # ---------------- name ------------------------ #
            # -------- entry name ----------- #
            self.name_label = Make_label(self.main_frame, "name:", 16, "white", "#0e1733")
            self.name_label.place(10, 257)
            self.name_entry = Entry(self.main_frame, width=20)
            self.name_entry.place(x = 80, y = 255)

            # -------- add chosen name ------ #
            try:
                self.name_entry.insert(0,self.name[0].split(" ")[1])
            except:
                pass

            # -------- add name but --------- #
            self.name_add_button = Button(self.main_frame, text="ADD", bg="#344658", font=("Courier",14), fg = "white", cursor="hand2", 
            command=lambda:name_add_function(self.name_entry.get()))
            self.name_add_button.place(x = 250, y = 250)

        # ---------------- bash ------------------------ #
            # -------- change bash color ---- #
            if self.bash == False:
                self.bash_button = Button(self.main_frame, text="bash", bg="#344658", font=("Courier",18), fg = "white", command = bash_button_function, cursor="hand2")
                self.bash_button.place(x = 10, y = 300)
            else:
                self.bash_button = Button(self.main_frame, text="bash", bg="#0e1733", font=("Courier",18), fg = "white", command = bash_button_function, cursor="hand2") 
                self.bash_button.place(x = 10, y = 300)
                self.running_in_bash = Make_label(self.main_frame, "running bash", 16, "white", "#0e1733")
                self.running_in_bash.place(100, 310)
            
        # ---------------- run ------------------------- #
            self.run_button = Button(self.main_frame, text="RUN", bg="#344658", font=("Courier",18), fg = "white", command=run_button_function, cursor="hand2")
            self.run_button.place(x = 270, y = 300)

        # -------- add ports and vols --- #
        def port_add_function(host_entry, cont_entry):
            try:
                # -------- check if int -------- #
                int(host_entry)
                int(cont_entry)
                new_port = f"-p {host_entry}:{cont_entry}"
                # -------- check if exists ------ #
                if new_port in self.port:
                    self.port_host.delete(0, END)
                    self.port_cont.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! make sure that you write both the\nhost and the container port\nand that you dont have two of the same ports")
                    self.popup.grab_set()
                # -------- check if spaces ------ #
                elif " " in host_entry or " " in cont_entry:
                    self.port_host.delete(0, END)
                    self.port_cont.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! cant have spaces in ports")
                    self.popup.grab_set()
                else:
                    self.port.append(new_port)
                    self.port_host.delete(0, END)
                    self.port_cont.delete(0, END)
                    update_page()
            except:
                self.port_host.delete(0, END)
                self.port_cont.delete(0, END)
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! make sure the port is an integer\nand also make sure that you write both the\nhost and the container port")
                self.popup.grab_set()

        def vol_add_function(host_entry, cont_entry):
            try:
                new_vol = f"-v {host_entry}:{cont_entry}"
                # -------- check if exists ------ #
                if new_vol in self.vol:
                    self.vol_host.delete(0, END)
                    self.vol_cont.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! make sure that you dont have two of the same volume")
                    self.popup.grab_set()
                else:
                    self.vol.append(new_vol)
                    self.vol_host.delete(0, END)
                    self.vol_cont.delete(0, END)
                    update_page()
            except:
                self.vol_host.delete(0, END)
                self.vol_cont.delete(0, END)
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR!")
                self.popup.grab_set()                

        # -------- bash on off ---------- #
        def bash_button_function():
            # -------- true/false bash ------ #
            if self.bash == False:
                self.bash = True
            else:
                self.bash = False
            update_page()
        
        # -------- add image name ------- #
        def name_add_function(name_entry):
            # -------- check if spaces ------ #
            if " " in name_entry:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! you cant have spaces in the container name use _")
                self.popup.grab_set()
            # -------- check if too long ---- #
            elif len(name_entry) > 13:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! you should not make names so long")
                self.popup.grab_set()
            # add a check if name alredy exists
            else:
                if len(self.name) == 0:
                    self.name.append(f"--name {name_entry}")
                    update_page()
                else:
                    self.name.pop()
                    self.name.append(f"--name {name_entry}")
                    update_page()

        # -------- run command ---------- #
        def run_button_function():
            # -------- check name ----------- #
            if len(self.name)==0:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! you should name your container so you could find it later")
                self.popup.grab_set()
            else:
                name = self.name[0].split(" ")[1]
                print(f"running {self.rep_tag} with ports {self.port}, volumes {self.vol}, name {name} and {self.bash} bash")
                run = Docker_images()
                run.run_image(self.rep_tag, self.port, self.vol, self.name, self.bash)
                self.reload_page()
                self.popup.destroy()

        # -------- start the page ------- #
        update_page()

    # ---------------- edit ------------------------ #
    def edit_image_popup(self, rep_tag, reload_page):
        self.rep_tag = rep_tag
        self.reload_page = reload_page

        self.popup.geometry("340x250")

        # -------- old image name ------- #
        self.old_label = Make_label(self.popup, "OLD", 18, "white", "#0e1733")
        self.old_label.place(20, 20)

        self.old_frame = Frame(self.popup, bg="#344658", width=300, height=40)
        self.old_frame.place( x = 20, y = 50)

        if len(self.rep_tag)>15:
            self.rep_tag_label = Make_label(self.old_frame, self.rep_tag, 10, "white", "#344658")
            self.rep_tag_label.place(60, 15)
        else:
            self.rep_tag_label = Make_label(self.old_frame, self.rep_tag, 15, "white", "#344658")
            self.rep_tag_label.place(70, 10)

        # -------- new image name ------- #
        self.new_label = Make_label(self.popup, "NEW", 18, "white", "#0e1733")
        self.new_label.place(20, 105)

        self.new_rep = Entry(self.popup,  width = 15)
        self.new_rep.place(x = 20, y = 135)
        
        self.new_tag = Entry(self.popup,  width = 15)
        self.new_tag.place(x = 193, y = 135)

        self.seperate_new = Make_label(self.popup, ":", 19, "white", "#0e1733")
        self.seperate_new.place(160, 135)

        # -------- edit button ---------- #
        self.edit_button = Button(self.popup, text="EDIT", bg="#344658", font=("Courier",26), fg = "white", width=13, height=1, 
        command=lambda:edit_button_function(self.new_rep.get(),self.new_tag.get()), cursor="hand2")
        self.edit_button.place(x = 20, y = 180)

        # -------- edit command ---------- #
        def edit_button_function(new_rep, new_tag):
            # -------- check if rep name ---- #
            if len(new_rep) == 0:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! make sure you write a reposotry name")
                self.popup.grab_set()
            # -------- check rep len -------- #
            if len(new_rep) > 13:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! you should not make names so long")
                self.popup.grab_set()
            # -------- check rep spaces ----- #
            elif " " in new_rep:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! should not have spaces in rep name")
                self.popup.grab_set()
            else:
                # -------- check tag spaces ----- #
                if " " in new_tag:
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! should not have spaces in tag name")
                    self.popup.grab_set()
                # -------- check tag len -------- #
                elif len(new_tag) >13:
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! you should not make tags so long")
                    self.popup.grab_set()
                elif len(new_tag) == 0:
                    # -------- edit rep:latest ------ #
                    new_rep_tag = new_rep
                    edit = Docker_images().change_image_tag(self.rep_tag, new_rep_tag)
                    if edit[0] == 1:
                        self.error_popup = Make_popup("ERROR")
                        self.error_popup.error(edit[1])
                        self.popup.grab_set()
                    else:
                        print(f"changed {self.rep_tag} to {new_rep_tag}:latest")
                        self.reload_page()
                        self.popup.destroy()
                else:
                    # -------- edit rep:tag --------- #
                    new_rep_tag = new_rep+":"+new_tag
                    edit = Docker_images().change_image_tag(self.rep_tag, new_rep_tag)
                    if edit[0] == 1:
                        self.error_popup = Make_popup("ERROR")
                        self.error_popup.error(edit[1])
                        self.popup.grab_set()
                    else:
                        print(f"changed {self.rep_tag} to {new_rep_tag}")
                        self.reload_page()
                        self.popup.destroy()

    # ---------------- save ------------------------ #
    def save_image_popup(self, rep_tag, reload_page):
        self.rep_tag = rep_tag
        self.reload_page = reload_page

        self.popup.geometry("360x220")

        self.rep_tag_label = Make_label(self.popup, self.rep_tag, 14, "white", "#0e1733")
        self.rep_tag_label.place(20, 17)

        # -------- choose dir ----------- #
        self.choose_dir_button = Button(self.popup, text="choose dir", bg="#344658", font=("Courier",15), 
        fg = "white", width=25, height=0, cursor="hand2",command=lambda:choose_dir_button_function())
        self.choose_dir_button.place(x = 20, y = 50)

        self.chosen_dir = Entry(self.popup, width = 15, state=DISABLED, disabledforeground="black")
        self.chosen_dir.place(x = 20, y = 100)

        self.slesh_label = Make_label(self.popup, "/", 18, "white", "#0e1733")
        self.slesh_label.place(150 ,102)

        # -------- file name ------------ #
        self.file_name = Entry(self.popup, width = 15)
        self.file_name.place(x = 170, y = 100)

        self.tar_label = Make_label(self.popup, ".tar", 14, "white", "#0e1733")
        self.tar_label.place(300 ,103)

        # -------- save button ----------- #
        self.save_button = Button(self.popup, text="SAVE", bg="#344658", font=("Courier",24), 
        fg = "white", width=5, height=1, cursor="hand2", command=lambda:save_button_function())
        self.save_button.place(x = 220,y = 155)

        # -------- choose dir function -- #
        def choose_dir_button_function():
            self.dir = filedialog.askdirectory(initialdir = "~", title = "Select a Folder")
            self.chosen_dir.config(state=NORMAL)
            self.chosen_dir.delete(0,END)
            self.chosen_dir.insert(0,self.dir)
            self.chosen_dir.config(state=DISABLED)

        # -------- save command --------- #
        def save_button_function():
            # -------- check dir exists ----- #
            if len(self.chosen_dir.get()) == 0:
                error_popup = Make_popup("ERROR")
                error_popup.error("ERROR! your file should have a directory")
                self.popup.grab_set()
            else:
                # -------- check name exists ---- #
                self.file = self.file_name.get()
                if len(self.file) == 0:
                    self.file_name.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! your file should have a name...")
                    self.popup.grab_set()
                # -------- check no / ----------- #
                elif "/" in self.file: # verry importand in windows should add more symbols / \ : ? * " < > |
                    self.file_name.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! you cant have / in your file name!!")
                    self.popup.grab_set()
                # -------- check spaces --------- #
                elif " " in self.file:
                    self.file_name.delete(0, END)
                    error_popup = Make_popup("ERROR")
                    error_popup.error("ERROR! you should not use spaces in a file name use _ !")
                    self.popup.grab_set()
                else:
                    self.save_file = self.dir + "/" + self.file + ".tar"
                    save = Docker_images().save_image(self.rep_tag, self.save_file)
                    if save[0] == 1:
                        self.error_popup = Make_popup("ERROR")
                        self.error_popup.error(save[1])
                        self.popup.grab_set()
                    else:
                        print(f"saved image {self.rep_tag} to {self.save_file}")
                        self.reload_page()
                        self.popup.destroy()

    # ---------------- remove ---------------------- #
    def rm_image_popup(self, rep_tag, reload_page):
        self.rep_tag = rep_tag
        self.reload_page = reload_page

        self.popup.geometry("300x100")

        # -------- rep name ------------- #
        self.label = Make_label(self.popup, f"are you sure you want to remove\n{rep_tag}?", 10, "white", "#0e1733")
        self.label.place(25,10)

        # -------- cancel button -------- #
        self.cancel_button = Button(self.popup, text="cancel", bg="#344658", font=("Courier",15), fg = "white", width=5, height=0, command=self.popup.destroy,  cursor="hand2")
        self.cancel_button.place(x = 10,y = 55)

        # -------- remove button -------- #
        self.rm_button =  Button(self.popup, text="REMOVE", bg="#344658", font=("Courier",15), fg = "white", width=5, height=0, command=lambda:rm_button_function(),  cursor="hand2")
        self.rm_button.place(x = 200,y = 55)

        # -------- remove command ------- #
        def rm_button_function():
            rm = Docker_images().rm_image(self.rep_tag)
            if rm[0] == 1:
                self.error_popup = Make_popup("ERROR")
                self.error_popup.error(rm[1])
                self.popup.grab_set()
            else:
                print(f"removed image {self.rep_tag}")
                self.reload_page()
                self.popup.destroy()

# ---------------- containers page popup ----------------------------------------- #
    # ---------------- save ------------------------ #
    def save_container_popup(self, cont_id, reload_page):
        self.cont_id = cont_id
        self.reload_page = reload_page  

        self.popup.geometry("360x180")

    # ---------------- remove ---------------------- #
    def rm_container_popup(self, cont_id, reload_page, cont_name):
        self.cont_id = cont_id
        self.reload_page = reload_page
        self.cont_name = cont_name

        self.popup.geometry("300x100")

# ---------------- sea page popup ------------------------------------------------ #

class Remove_vols_and_ports():
# ---------------- create vols and ports objects --------------------------------- #
    # this class is used in the run image popup, because we cant import the button class and we want to save the button object and its content
    #so we created a class here that stores those contents
    def __init__(self, master, text, list_p_v, update_fun):
        self.master = master
        self.text = text
        self.list_p_v = list_p_v
        self.update_fun = update_fun
        if len(self.list_p_v) > 1:
            self.button = Button(self.master, text=self.text, bg = "#344658", fg = "white", font=("Courier",7), command=self.remove_p_v, bd=0, cursor="hand2")
        elif len(self.list_p_v) > 2:
            self.button = Button(self.master, text=self.text, bg = "#344658", fg = "white", font=("Courier",6), command=self.remove_p_v, bd=0, cursor="hand2")
        else:
            self.button = Button(self.master, text=self.text, bg = "#344658", fg = "white", font=("Courier",8), command=self.remove_p_v, bd=0, cursor="hand2")
                
    def remove_p_v(self):
        self.list_p_v.remove(self.text)
        self.update_fun()

    def grid(self, col, row):
        self.col = col
        self.row = row
        self.button.grid(column=self.col, row=self.row)
