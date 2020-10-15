# SHARK a docker gui

## What is Shark
  
  Shark is a gui created for easy docker work, if its hard for you to work from the terminal all the time
  fear no more shark can do some of the most important docker functions just with a click of a button.
  
## shark for ubuntu
 
![Alt text](https://www.linkpicture.com/q/ubuntu_shark.png)

For the ubuntu user who wants easy work with docker here is the solusion, but before you start you need some things
first you will need docker of course.

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
