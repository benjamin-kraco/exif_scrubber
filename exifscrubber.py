import PIL.Image
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfile
import PySimpleGUI as gui


root = tkinter.Tk()
root.withdraw()


#testing read of exif data below
#_____________________________________
#fileName = askopenfilename()
#img = PIL.Image.open(fileName)
#exif_data = img.getexif()

#print(exif_data)





fileNames = askopenfilenames()
imgList = list(fileNames)

layout = [[gui.Text('Scrubbing!')],
		[gui.ProgressBar(len(imgList), orientation='h', size=(30,30), key='progressbar')],
		[gui.Button('Cancel')]]


window = gui.Window('Scrubbing Selected Images',layout)
progress_bar = window['progressbar']


for i in range (0, len(imgList)):
	img2 = PIL.Image.open(fileNames[i])
	# space for logging exif data
	img2.save(fileNames[i])

	event, values = window.read(timeout=10)
	if event == 'Cancel' or event == gui.WIN_CLOSED:
		break

	progress_bar.UpdateBar(i)
	i = i+1

window.close()