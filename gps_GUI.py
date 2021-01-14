#google map plot(python3)

# This program plots gps-data on Google-map. 
# To run this program, enter below command in terminal.
# $ python3 gps_GUI.py

import numpy as np
import gmplot

# To use GUI
import tkinter
from tkinter import filedialog

# Create root window
root = tkinter.Tk()
# Not to show tkinter-window
root.withdraw()

# take position from Log -------------
data = []

gps_file = tkinter.filedialog.askopenfilename(
	title = "Choose a txt file",
	filetypes = [("TEXT",".txt"),("ALL","*")]
	)

with open(gps_file,"rb") as my_file:
    for line in my_file:
        data.append(line)
        
la = []
lo = []
for line in data:
    if (str(line[:8])=="b'latitude'") and (np.bitwise_not(np.isnan(float(line[10:])))):
        la.append(float(line[10:]))
    elif (str(line[:9])=="b'longitude'") and (np.bitwise_not(np.isnan(float(line[11:])))):
        lo.append(float(line[11:]))
        
la = np.array(la)
lo = np.array(lo)

### plot -------------
gmap = gmplot.GoogleMapPlotter(43.075830, 141.341446, 18)
gmap.scatter( la, lo, '#FF5733', size = 0.1, marker = None )

htmlPath = filedialog.asksaveasfilename(
	    initialfile = "htmlfile",
	    defaultextension = ".html",
	    title = "Input export GPS-html file",
	    filetypes=[("HTML", ".html"),("ALL","*")]
	)
gmap.draw(htmlPath)


