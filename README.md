# Enfuse for Gimp

## Description

This plugin allows you to create a HDR image without leaving Gimp.

Just create one layer for each exposure, call the plugin and a new layer will be added to your current image with the blend result.

## Requirements

* [Gimp 2.8](https://www.gimp.org/)
* [Enfuse 4.2](http://enblend.sourceforge.net/)
* Windows PC

## Instalation

1. Download [Enfuse 4.2](http://enblend.sourceforge.net/) and save it to a folder
2. Copy the file enfuse.py to the Gimp plugin folder
3. Set the path of the Enfuse executable on the top of the script **enfusePath = "C:\\enfuse\\bin\\enfuse.exe"**. Don't forget the double slash to separate the folders.

## Using the plugin

1. Start Gimp
2. Open all the exposures as different layers of a single image
3. Run the Enfuse plugin which is located in Filters → Combine → Enfuse
4. Pick a temporary file folder. 
   This is used for saving the intermediate working files. 
   These will be deleted at the end of the process.
5. Click OK. The process will begin and at the end the resulting image will be shown as a new layer.


## Acknowledgements

This plugin was the original idea of Fernando Batista, a great friend and photographer and he's helping me testing and providing feedback and new ideas.

This is my first Gimp plugin and Python script so these resources got me through it.
Thanks!

* [Jackson Bates](https://gist.github.com/JacksonBates)
* [Gimp Book](http://gimpbook.com/)
* [ShellOut](http://gimpchat.com/viewtopic.php?f=9&t=970&p=12542#p12541)
