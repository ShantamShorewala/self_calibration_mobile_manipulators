import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import time
import cv2.aruco as aruco

#help(cv2.aruco)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

img = cv2.imread("test_1_8mm.bmp")
img = cv2.resize(img, (500,500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
print (ids)
frame_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)

while True:

	cv2.imshow("img",frame_markers)
	cv2.waitKey(1)