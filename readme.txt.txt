~~HELLO!~~

This is a simple program for scrubbing EXIF data (metadata) from your JPEG images before posting or distribution.

Some phone & other web-connected cameras log data about a photo, whether it be camera type, camera settings, or even geolocation data.

This application is a way to quickly scrub that metadata in bulk. Run the .exe file, and when the option to choose your files appears, select as many as you'd like. 
Then, the program wipes the metadata by saving the image in place using the python PIL library. Your images are not stored anywhere besides your local machine and this shouldn't alter any sizing
or other edits. 

THIS IS IRREVERSIBLE. IF YOU WANT TO MAINTAIN YOUR METADATA, DO NOT RUN THIS ON PHOTOS THAT HAVEN'T BEEN BACKED UP.

The modules used in this project:

tkinter (bundled with python)
Pillow/PIL
progressbar

.exe built from PyInstaller

