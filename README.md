# SHARK a docker gui

## What is Shark

Shark is a gui created for easy docker work, if its hard for you to work from the terminal all the time
fear no more shark can do some of the most important docker functions just with a click of a button.
This was made using a someking of self made api that sends commands to the docker and you controll it
through the Shark docker gui
  
## shark for ubuntu
 
![Alt text](https://github.com/gavriel200/docker_gui/blob/master/images/ubuntu_shark.png)

For the ubuntu user who wants easy work with docker here is the solusion, but before you start you'll need some things.
First you will need python. this project has been tested only on python 3.8.5 yet.
If you dont have python installed simply use the terminal to download it
```bash
$ sudo apt install python3
```
Then you will need docker of course.
Easy way to download it is using the [docker installation guid](https://docs.docker.com/engine/install/ubuntu/).
After you have docker you will have to enabel your user to do docker commands without sudo.
you can do that with few simple commands:
Create the docker group.
```bash
$ sudo groupadd docker
```
Add your user to the docker group.
```bash
$ sudo usermod -aG docker $USER
```
Log out and log back in so that your group membership is re-evaluated.

You can also run the following command to activate the changes to groups.
```bash
$ sudo service docker restart
```
Thats it you are all set and done.
now all you need to do is run the gui_main.py the main aplication.
```bash
$ python gui_main.py
```
## issues
* you can't check the voulume dir when you run an image, cant know if its a legit image
