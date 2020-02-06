import numpy as np
import csv

file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/images/cw/cw_aruco.txt", "r")
csv_reader = csv.reader(file, delimiter=' ')

write_file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw_vision.txt", "w")
writer = csv.writer(write_file)

count=0
quaternions=[]

angles = []
for row in csv_reader:
	quaternions.append([float(row[4]), float(row[5]), float(row[6]), float(row[7])])

for i in range(0, len(quaternions)-1):
	q1 = quaternions[i]
	q2 = quaternions[i+1]

	q2_conj = np.multiply(q2, [1.,-1.,-1.,-1.])
	z = np.matmul(q1, q2_conj)
	theta = 2*np.arccos(z)
	angles.append(theta)
	#writer.writerow([2*theta])

file_bag = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw.txt", "r")
bag_reader = csv.reader(file_bag, delimiter=',')

rotations = []
for row in bag_reader:
	rotations.append([float(row[1]), float(row[2])])

angles = np.transpose(np.asarray([angles]))
rotations = np.asarray(rotations)

print np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(rotations), rotations)), np.transpose(rotations)), angles)

print angles.shape, rotations.shape