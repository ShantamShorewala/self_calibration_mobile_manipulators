import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

file = open("/media/shantam/D6E430F0E430D509/robomuse_kid/21_01/images/cw/cw_aruco.txt", "r")
csv_reader = csv.reader(file, delimiter=' ')

array=[]
for row in csv_reader:
	array.append([float(row[1]), float(row[2]), float(row[3])])

print len(array)

fig = plt.figure()
ax = plt.axes()

for i in array:
	print i
	ax.scatter(i[0], i[1], marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

plt.show()