 import numpy as np
import csv

# #file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/images/cw/cw_aruco.txt", "r")
# file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/ccw.txt", "r")
# csv_reader = csv.reader(file, delimiter=' ')

# #write_file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw_vision.txt", "w")
# file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/ccw.txt", "w")
# writer = csv.writer(write_file)

# count=0
# quaternions=[]

# angles = []
# for row in csv_reader:
# 	quaternions.append([float(row[4]), float(row[5]), float(row[6]), float(row[7])])

# for i in range(0, len(quaternions)-1):
# 	q1 = quaternions[i]
# 	q2 = quaternions[i+1]

# 	q2_conj = np.multiply(q2, [1.,-1.,-1.,-1.])
# 	z = np.matmul(q1, q2_conj)
# 	theta = 2*np.arccos(z)
# 	angles.append(theta)
# 	#writer.writerow([2*theta])

# file_bag = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw.txt", "r")
# bag_reader = csv.reader(file_bag, delimiter=',')

# rotations = []
# for row in bag_reader:
# 	rotations.append([float(row[1]), float(row[2])])

# angles = np.transpose(np.asarray([angles]))
# rotations = np.asarray(rotations)

# print np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(rotations), rotations)), np.transpose(rotations)), angles)

# print angles.shape, rotations.shape


#file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/images/cw/cw_aruco.txt", "r")
file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/rot.txt", "r")
csv_reader = csv.reader(file, delimiter=',')

#write_file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw_vision.txt", "w")
file_2 = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/images/ccw.txt", "r")
reader_2 = csv.reader(file_2, delimiter=',')

count = 0
angles = []
rotations = []
for row, row_2 in zip(csv_reader, reader_2):
	angles.append(float(row_2[1]))
	count+=1
	rotations.append([float(row[1]), -float(row[2])])
	angles.append(float(row_2[1]))
	rotations.append([float(row[2]), -float(row[1])])

	print ((63.5/439.4)*(float(row[2]) + float(row[1]))), row_2[1], row

angles = np.asarray(angles)
rotations = np.asarray(rotations)

#for i in range(0,count):
	#print angles[i], np.sum(rotations[i])*63.5/439.4

# count=0
# quaternions=[]

# angles = []
# for row in csv_reader:
# 	quaternions.append([float(row[4]), float(row[5]), float(row[6]), float(row[7])])

# for i in range(0, len(quaternions)-1):
# 	q1 = quaternions[i]
# 	q2 = quaternions[i+1]

# 	q2_conj = np.multiply(q2, [1.,-1.,-1.,-1.])
# 	z = np.matmul(q1, q2_conj)
# 	theta = 2*np.arccos(z)
# 	angles.append(theta)
# 	#writer.writerow([2*theta])

# file_bag = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/bags/cw/cw.txt", "r")
# bag_reader = csv.reader(file_bag, delimiter=',')

# rotations = []
# for row in bag_reader:
# 	rotations.append([float(row[1]), float(row[2])])

# angles = np.transpose(np.asarray([angles]))
# rotations = np.asarray(rotations)

[alpha_r, alpha_l] = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(rotations), rotations)), np.transpose(rotations)), angles)

# print angles.shape, rotations.shape
alpha_r += 0.01
alpha_l -= 0.015
print alpha_r, alpha_l

coeff = -alpha_r/(2*alpha_l)
print coeff

print alpha_r*439.5
# file.close()
# file_2.close()

# print "final"
file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/bags/cw.txt", "r")
csv_reader = csv.reader(file, delimiter=',')

file_2 = open("/media/shantam/D6E430F0E430D509/robomuse_kid/22_02/images/cw.txt", "r")
reader_2 = csv.reader(file_2, delimiter=',')

count=0
rotations=[]
disp=[]

for row, row_2 in zip(csv_reader, reader_2):
	print row_2[1], row
	count+=1
	if count is not (1 or 4):
		disp.append(float(row_2[1]))
		#print (63.5/2)*(float(row[2]) + float(row[1])), row_2[1]
		rotations.append( 0.75*(coeff*float(row[2])*2 + float(row[1])) )
		print coeff*float(row[2])*2 + float(row[1])
disp = np.transpose(np.asarray([disp]))
rotations = np.transpose(np.asarray([rotations]))
# print rotations
# print disp.shape, rotations.shape

rl = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(rotations), rotations)), np.transpose(rotations)), disp)

a = (-(alpha_r)*rl/(alpha_l))
b =  -rl/alpha_l

print rl, a, b