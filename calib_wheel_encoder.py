import numpy as np
import rosbag, time
import csv

#file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/ccw.txt", "w")
#writer = csv.writer(file)

for i in range(1,2):
	
	bag=rosbag.Bag("/media/shantam/D6E430F0E430D509/exp_22_2/optitrack_calib/part_"+str(i)+"_new.bag")

	ticks_r=0
	# for topic, msg, t in bag.read_messages(topics='/left_ticks'):
	# 	#print float(str(msg)[6:])
	# 	time.sleep(0.1)
	# 	if len(str(msg))==7:	
	# 		if int(str(msg)[6]) is not 0:
	# 	#		print str(msg)[6]
	# 			ticks_r+=int(str(msg)[6])

	# 	elif len(str(msg))==8:	
	# 		if int(str(msg)[7]) is not 0:
	# 	#		print str(msg)[7]
	# 			ticks_r+=int(str(msg)[7])

	ticks_l=0
	for topic, msg, t in bag.read_messages(topics='/right_ticks'):
		print float(str(msg)[6:])
		time.sleep(0.1)
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

	#writer.writerow([i, rot_r, rot_l])
