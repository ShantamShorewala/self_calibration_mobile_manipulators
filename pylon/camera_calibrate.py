#teknic
# [[ 1.82986215e+03  2.54988421e+01  6.13436190e+02 -3.00324487e+02]
#  [ 4.09558595e+01  1.84596707e+03  1.62833872e+02 -1.07696746e+02]
#  [ 2.51491467e-02  9.40787591e-02  9.95247059e-01  1.11363826e+03]]

#ps
# [[ 1.21021456e+03  8.81297445e+01  5.81043177e+02 -3.10576516e+02]
#  [ 4.76718129e+01  1.21951156e+03  5.92206231e+01 -1.21995232e+02]
#  [ 5.40813779e-02  2.01605261e-01  9.77972660e-01  2.41569121e+03]]

#iiitB
# [[ 1.57967799e+03  4.08657105e+01  4.90765224e+02 -2.60555727e+02]
#  [ 3.43873774e+01  1.54492724e+03  2.24632141e+02 -8.06877215e-01]
#  [ 1.11230545e-01  7.50346635e-02  9.90957903e-01  1.24154660e+03]]


import cv2, numpy as np, os 

#file = cv2.VideoCapture("/media/shantam/D6E430F0E430D509/elcita_video_share_Sept2019/videos_checkerBoard/10_107/cam_t1_10_107-000.mp4")

import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = (np.mgrid[0:8,0:6].T.reshape(-1,2))*3#41.6

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# img_dir = "/home/shantam/Documents/Programs/calib_images/selected/"
# img_dir = "/home/shantam/catkin_ws/src/pylon_camera/config/calibrate_03_12/"
img_dir = "/home/shantam/catkin_ws/src/pylon_camera/config/sim/checkerboard/exp_2/subset"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

counter=0
for file in files:
	counter+=1
	print file
	#if counter<2000:
	frame = cv2.imread(file)

	# cv2.imshow('original', frame)
	# cv2.waitKey(1)

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print gray.shape[::-1]
	
	# Find the chess board corners
	ret, corners = cv2.findChessboardCorners(gray, (8,6),None)

	# If found, add object points, image points (after refining them)
	if ret == True:
		objpoints.append(objp)

		corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
		imgpoints.append(corners2)

		#print "doing it"
		# Draw and display the corners
		img = cv2.drawChessboardCorners(frame, (8,6), corners2,ret)
		cv2.imshow('img',frame)
		cv2.waitKey(1)

# gray=np.zeros((2,2))
print "starting calibration"
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1] , None ,None)
print "mtx", mtx, "\n"
print "dist", dist, "\n"

rotation_mat = np.zeros(shape=(3, 3))
R = cv2.Rodrigues(rvecs[0], rotation_mat)[0]
P = np.column_stack((np.matmul(mtx,R), tvecs[0]))
print P

# tot_error = 0
# for i in xrange(len(objpoints)):
#     imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
#     error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
#     tot_error += error

# print "total error: ", mean_error/len(objpoints)
	#cv2.destroyAllWindows()