import numpy as np
import rosbag, time
import csv

file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/ccw/cw.txt", "w")
writer = csv.writer(file)

for i in range(1,16):
	
	bag=rosbag.Bag("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/calib_21_"+str(i)+".bag")

	ticks_r=0
	for topic, msg, t in bag.read_messages(topics='/rwheel'):
		#print msg
		if len(str(msg))==7:	
			if int(str(msg)[6]) is not 0:
		#		print str(msg)[6]
				ticks_r+=int(str(msg)[6])

		elif len(str(msg))==8:	
			if int(str(msg)[7]) is not 0:
		#		print str(msg)[7]
				ticks_r+=int(str(msg)[7])

	ticks_l=0
	for topic, msg, t in bag.read_messages(topics='/lwheel'):
		#print msg
		if len(str(msg))==7:	
			if int(str(msg)[6]) is not 0:
		#		print str(msg)[6]
				ticks_l+=int(str(msg)[6])

		elif len(str(msg))==8:	
			if int(str(msg)[7]) is not 0:
		#		print str(msg)[7]
				ticks_l+=int(str(msg)[7])

	rot_r = (float(ticks_r) / 600.0)*360.0
	rot_l = (float(ticks_l) / 600.0)*360.0

	writer.writerow([i, rot_r, rot_l])
