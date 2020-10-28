# SHARK a docker gui

## What is Shark

Shark is an alternative gui to Docker Desktop for the linux Ubuntu users.
This gui aplication was build in python using the Tkinter library, instrad of using the 
terminal for every docker command, Shark helps you with some of the most used docker commands
for images and containers control.
For example:
* run images
* upload images from .tag files
* remove containers
* open containers in bash
and more.

![Alt text](https://github.com/gavriel200/docker_gui/blob/master/Code/images/ubuntu_shark.png)

# Code

the source code for the Shark aplication is located in the code folder.

## requirements

### Python
If you dont have python installed on your Ubuntu machine simply use the terminal to download it using:

```bash
$ sudo apt install python3
```

You will also need the Tkinter library for python:

```bash
$ sudo apt-get install python-tk
```

> Watch out!
> Before you use the apt or apt-get install commands you should do the 
> ```bash
    $ sudo apt update
    ```
> ```bash
    $ sudo apt-get update
    ```
``` 
Watch out!
    Before you use the apt or apt-get install commands you should do the 
    ```bash
        $ sudo apt update
    ```
    ```bash
        $ sudo apt-get update
    ```
```
## docker

Then of course you will need docker.
Easy way to download it is using the [docker installation guid](https://docs.docker.com/engine/install/ubuntu/).

After you docker you will need to enabel your user to use docker commands without "sudo".
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

## run

now all you need to do is run the gui_main.py the main aplication from the Code folder.

```bash
$ python gui_main.py
```

if you have python 2 also installed there is a chance youll have to specify you python version

```bash
$ python3 gui_main.py
```

## issues
* When you have a long image/container name the buttons will be moved right and you wont be able to click them.
* Same goes for when you run an image and you add to many vols or ports.

# Executable file

## runing the executable file

the executable is very easy to use all you need to have are the images folder at the same
directory as the executable file, and you are all set up.

I recomand to copy the executable file and the images folder to your own doc or working directory,
and then create a shortcut to the executable file.