import numpy as np
import rosbag, time
import csv, rospy
from std_msgs.msg import Int16
#file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/ccw.txt", "w")
#writer = csv.writer(file)

	
pub = rospy.Publisher('l_wheel', Int16, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz

bag=rosbag.Bag("/media/shantam/D6E430F0E430D509/exp_22_2/navigation_repeat/just_ticks.bag")

for topic, msg, t in bag.read_messages(topics='/rwheel'):
	
#		msg.data = np.int16(msg.data)
#		outbag.write(topic, msg, t)
	print type((msg.data))
	pub.publish()
	time.sleep(0.1)