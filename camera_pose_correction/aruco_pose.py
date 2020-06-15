import sys, argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import time
import cv2.aruco as aruco
import csv

def min_dist(x, y):

	x = np.squeeze(x)
	y = np.squeeze(y)
	return np.power(np.power(x[0]-y[0],2) + np.power(x[1]-y[1],2) + np.power(x[2]-y[2],2),0.5)

def compute_distances(dict_ids):

	ordered_ids = [131, 136, 129, 133, 135, 118, 124, 134, 120, 123, 117, 137, 121, 119, 128, 113, 138, 132]
	distances = []
	for i in range(0, len(ordered_ids)-1):
		print ()
		val = (min_dist(dict_ids[ordered_ids[i]], dict_ids[ordered_ids[i+1]]))
		print (ordered_ids[i], ordered_ids[i+1], val)
		distances.append(val)
	return distances

def pose_estimation(img, mtx, dist, size):
	'''
		Detects the aruco markers and estimates pose for each.
		Returns a list of marker positions.
	'''	
	dict_ids = {}
	aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
	parameters =  aruco.DetectorParameters_create()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
	img = aruco.drawDetectedMarkers(img.copy(), corners, ids)
	for corner, id_ in zip(corners, ids):
		rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corner, size, mtx, dist)
		img = aruco.drawAxis(img, mtx, dist, rvec, tvec, 0.005)
		dict_ids[id_[0]] = tvec

	return img, dict_ids

def read_image(filename):

	img = cv2.imread(filename)

	if img is not None:
		print ("Image found.")
		img = cv2.resize(img, (500,500))
	else:
		print ("Image not found, enter a valid path.")
		exit(1)

	return img

def load_camera_matrix(filename):
	'''
		Args: Filename of the csv file that contains the camera matrix and distortion coefficients.
			  The first three rows should correspond to each row of the camera matrix (3x3) and the
			  fourth row should contain the distortion coefficients.
	'''
	file = open(filename)
	reader = csv.reader(file, delimiter=' ')

	mtx = np.zeros((3,3))
	dist = np.zeros((1,5))
	row_cnt=0
	for row in reader:
		print row
		if row_cnt<3:
			mtx[row_cnt] = list(map(np.float32, row)) #[float(row[0]),float(row[1]),float(row[2])]
		else:
			dist = list(map(np.float32, row))
		row_cnt+=1
	
	return mtx, np.asarray(dist)

if __name__=="__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--i', metavar='img_path', type=str,
				   help='Provide the path to the image', default = '')
	parser.add_argument('--mtx', metavar='camera_matrix', type=str,
				   help='Provide the path to the camera intrinsics (3x3) and distortion coeffs', default = '')
	parser.add_argument('--out', metavar='o', type=str,
				   help='filename for the output image', default = None)
	parser.add_argument('--m', metavar='marker_size', type=float,
				   help='aruco marker size (in m)', default = 0.01)
	args = parser.parse_args()

	img = read_image(args.i)
	mtx, dist = load_camera_matrix(args.mtx)
	img, dict_ids= pose_estimation(img,mtx,dist,args.m)
	distances = compute_distances(dict_ids)
	
	#print (distances)
	
	for i in range(0,100000):		
		cv2.imshow('img', img)
		cv2.waitKey(1)
