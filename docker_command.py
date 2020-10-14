import subprocess
import re
import os

class Docker_images:
    # ------------------------------------------------   functions for docker images ------------------------------------------------ #
    @staticmethod    
    def just_images():
        """ prints the command docker images as it comes"""

        sub = subprocess.run(["docker","images"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout
    
    @staticmethod
    def list_images():
        """ prints a list of lists of words for each line in the images command // name // tag // id // (when was created) // size //."""

        sub = subprocess.run(["docker","images"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            list_of_images = []
            for items in sub.stdout.split("\n"):
                list_of_images.append(re.sub(' +', ' ',items).split(' '))
            list_of_images.pop(0)
            list_of_images.pop(-1)
            return list_of_images
    
    @staticmethod 
    def load_image(dir_to_image):
        """ load image from dir should be .zip/.tar file"""

        sub = subprocess.run(["docker","load", "-i", dir_to_image], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout
    
    @staticmethod
    def rm_image(image_rep_tag):
        """ remove image from docker by docker id"""

        sub = subprocess.run(["docker","image", "rm", "-f", image_rep_tag], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout

    @staticmethod
    def run_image(image_rep_tag, port, vol, name, bash):
        """ runing an image with the ability to add ports and volumes, if running in bash == True the a terminal will be opened
        takes in the ports and volumes as a list of string e.g. ["-p 80:80","-p 60:130"]"""

        command = ["docker", "run", image_rep_tag]
        for vols in vol:
            command.insert(2, vols)
        for ports in port:
            command.insert(2, ports)
        for names in name:
            command.insert(2, names)
        if bash == True:
            command.insert(2, '-it')
            command.extend(['bash'])
            cmd_command = ""
            for items in command:
                cmd_command = cmd_command + items + " "
            # os.system("start cmd /c " + cmd_command) # for 
            os.system(f"gnome-terminal -e 'bash -c \"{cmd_command}; sleep 1000000\" '")
            return 0, 0
        else:
            subprocess_command = []
            for items in command:
                splited = items.split()
                for item in splited:
                    subprocess_command.append(item)
            print(subprocess_command)
            sub = subprocess.run(subprocess_command, capture_output=True, text=True)
            if sub.returncode == 1:
                return sub.returncode, sub.stderr
            else:
                return sub.returncode, sub.stdout

    @staticmethod
    def save_image(image_rep_tag, dir_and_tar_name):
        """ save image into .tar file"""

        sub = subprocess.run(["docker","save", "-o", dir_and_tar_name, image_rep_tag], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout
    
    @staticmethod
    def change_image_tag(image_rep_tag, new_image_rep_tag):
        """ change the rep and tags of an image this also removes the old image with the old rep and tags"""

        sub = subprocess.run(["docker","image", "tag", image_rep_tag, new_image_rep_tag], capture_output=True, text=True)
        sub = subprocess.run(["docker","image", "rm", "-f", image_rep_tag], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout
    
class Docker_container:
    # ------------------------------------------------   functions for docker containers ------------------------------------------------ #
    @staticmethod
    def just_containers():
        """ prints the command "docker container ls --all" as it comes"""

        sub = subprocess.run(["docker","container", "ls", "--all"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout
    
    @staticmethod
    def list_containers():
        """ prints a list of lists of words for each line in the containers id // base image // ports // (when was created) // name //."""

        sub = subprocess.run(["docker","container", "ls", "--all"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            list_of_containers = []
            for items in sub.stdout.split("\n"):
                list_of_containers.append(re.sub(' +', ' ',items).split(' '))
            list_of_containers.pop(0)
            list_of_containers.pop(-1)
            return list_of_containers

    @staticmethod
    def running_containers():
        """prints list of ids of the running contianers"""

        sub = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:  
            list_of_running_containers = []
            list_of_ids = []
            for items in sub.stdout.split("\n"):
                list_of_running_containers.append(re.sub(' +', ' ',items).split(' '))
            list_of_running_containers.pop(0)
            list_of_running_containers.pop(-1)
            for containers in list_of_running_containers:
                list_of_ids.append(containers[0])
            
            return list_of_ids

    @staticmethod
    def save_container(container_id, new_image_rep_tag):
        """ saves a container into a new image"""

        sub = subprocess.run(["docker", "commit", container_id, new_image_rep_tag], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:
            return sub.returncode, sub.stdout

    @staticmethod
    def start_or_stop_containers(container_id):
        """ this ether stops a runing contianer or it starts one that is down """
        # the way it works is by using the command "docker ps", this command shows 
        # all the running containers then we create a list of the containers ids that run and 
        # if the container we want to start/stop is in the list we stop it if not we start it
        
        sub = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:  
            list_of_running_containers = []
            list_of_ids = []
            for items in sub.stdout.split("\n"):
                list_of_running_containers.append(re.sub(' +', ' ',items).split(' '))
            list_of_running_containers.pop(0)
            list_of_running_containers.pop(-1)
            for containers in list_of_running_containers:
                list_of_ids.append(containers[0])

            if container_id in list_of_ids:
                sub = subprocess.run(["docker", "stop", container_id], capture_output=True, text=True)
                if sub.returncode == 1:
                    return sub.returncode, sub.stderr
                else:
                    return sub.returncode, sub.stdout

            else:
                sub = subprocess.run(["docker", "start", container_id], capture_output=True, text=True)
                if sub.returncode == 1:
                    return sub.returncode, sub.stderr
                else:
                    return sub.returncode, sub.stdout
    
    @staticmethod
    def start_container_in_bash(container_id):
        """ starts a container in bash opens cmd only a running container can be executed into bash"""

        sub = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:  
            list_of_running_containers = []
            list_of_ids = []
            for items in sub.stdout.split("\n"):
                list_of_running_containers.append(re.sub(' +', ' ',items).split(' '))
            list_of_running_containers.pop(0)
            list_of_running_containers.pop(-1)
            for containers in list_of_running_containers:
                list_of_ids.append(containers[0])

            if container_id in list_of_ids:
                cmd_command = "docker exec -it " + container_id + " bash"
                print(cmd_command)
                os.system("start cmd /c " + cmd_command)
                return "opening bash"
            else:
                return "container " + container_id + " is not running"
        

    @staticmethod
    def remove_container(container_id):
        """ removes a container by the container id this will also remove a running container"""
        sub = subprocess.run(["docker", "rm", "-f", container_id], capture_output=True, text=True)
        if sub.returncode == 1:
            return sub.returncode, sub.stderr
        else:  
            return sub.returncode, sub.stdout

# a = Docker_images()
# a.run_image("ubuntu", ["-p 80:130"], "", False)