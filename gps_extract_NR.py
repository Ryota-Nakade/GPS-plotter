## python2
# This progmram converts bag file to txt (python2)
# To run this program, enter below command in terminal.
# $ python gps_extract_NR.py

import rosbag
import os
from tqdm import tqdm
import glob

# To use GUI
import Tkinter as tk
import tkFileDialog as fd

# Not to show tkinter-window
root = tk.Tk()
root.withdraw()

def export(bagPath, topicName, txtPath):	
	txt = open(txtPath,'w')
	for topic, msg, t in tqdm(rosbag.Bag(bagPath).read_messages()):
		if topic == topicName:
			txt.write(str(msg))
	txt.close()
	print('Done!!')

if __name__ == '__main__':
	print("Choose bagfile")
	bagPath = fd.askopenfilename(
	    title = "Choose a ROSBAG file",
	    filetypes=[("BAG", ".bag")]
    	)
	print("Input export-txt-file")
	txtPath = fd.asksaveasfilename(
	    initialfile = "txtfile",
	    defaultextension = ".txt",
	    title = "Input export GPS-txt file",
	    filetypes=[("TEXT", ".txt"),("ALL","*")]
    	)

	names = glob.glob(bagPath)
	print(names)
	
	topicName = '/fix'

	for j in range(len(names)):
		bagName = names[j]
		export(bagName, topicName, txtPath)

