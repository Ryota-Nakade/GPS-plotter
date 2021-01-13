import rosbag
import os
from tqdm import tqdm
import glob

## python2
#bag file to txt (python2)

def export(bagPath, topicName):
	txt = open('gps20210112170346.txt','w')
	for topic, msg, t in tqdm(rosbag.Bag(bagPath).read_messages()):
		if topic == topicName:
			txt.write(str(msg))
	txt.close()
	print('Done!!')

if __name__ == '__main__':
	bagPath = '2021-01-12-17-03-46.bag'
	names = glob.glob(bagPath)
	print(names)
	
	topicName = '/fix'

	for j in range(len(names)):
		bagName = names[j]
		export(bagName, topicName)

