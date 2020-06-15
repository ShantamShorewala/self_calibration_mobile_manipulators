#! /usr/bin/python
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time

# Instantiate CvBridge
bridge = CvBridge()

cnt = 1

def image_callback(msg):
    print("Received an image!")
    global cnt
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        cv2.imwrite("sim/checkerboard/exp_3/imgs/"+str(cnt)+".png", cv2_img)
        time.sleep(1)
        cnt+=1

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    # image_topic = "/pylon_camera_node/image_raw"
    image_topic = "/camera/image"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
