# shark for ubuntu
 
![Alt text](https://github.com/gavriel200/docker_gui/blob/master/Ubuntu/images/ubuntu_shark.png)

The first shark version was build on ubuntu so it supports only ubuntu. (there wiil be a windows version later).
This palication was made using python's Tkinter not the ideal way to create an aplication but it works.
It has been tested only on python 3.8 yet but more test shall come with time.

## requirements

# Python
If you dont have python installed on your machine simply use the terminal to download it

```bash
$ sudo apt install python3
```
# docker

Then of course you will need docker.
Easy way to download it is using the [docker installation guid](https://docs.docker.com/engine/install/ubuntu/).

After you have docker you will need to enabel your user to use docker commands without "sudo".
You can do that with few simple commands:

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

# run

now all you need to do is run the gui_main.py the main aplication.

```bash
$ python gui_main.py
```

if you have python 2 also installed there is a chance youll have to specify you python version

```bash
$ python3 gui_main.py
```
you should also make sure you run the gui_main.py from the Ubuntu folder

## issues
* When you have a long image/container name the buttons will be moved right and you wont be able to click them.
* When you run an image and you add more the 4 vols or ports you wont be able to see all the vols/ports added
* No windows version