import numpy as np
import csv

ax_val= np.zeros((5,7), np.float32)
with open('/media/shantam/D6E430F0E430D509/youbot_k_identification/20_11/20_11.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=' ')
	count=0
 	for row in csv_reader:
		ax_val[count] = [float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])]
 		count+=1
print ax_val.shape  	

a=[0,0,0,0]
A=[0,0,0,0]
d=[0,0,0,0]

x = np.zeros((4,3), np.float32)
y = np.zeros((4,3), np.float32)

def findperp(N_1, N_2, X_0, X_3):	
	c3 = np.matmul(np.transpose(N_1), N_2)
	#print "c3", c3
	C=np.array([[c3, -1.], [1., -c3]])
	#print C.shape
	#print np.linalg.inv(C).shape
	#print np.array([[N_1[0], N_2[0]], [N_1[1], N_2[1]]]).shape
	CF= np.matmul(np.matmul( -np.linalg.inv(C), np.transpose(np.array([[N_1[0], N_2[0]], [N_1[1], N_2[1]], [N_1[2], N_2[2]]]))), (X_3-X_0))
	#print CF.shape, X_3.shape
	X_2= CF[0]*N_2+X_3;
	X_1= CF[1]*N_1+X_0;
	return X_1, X_2

for i in range(0,4):
	#print 'counting' + str(i)
	#print ax_val[i][3:6]
	#print y[i]
	x[i], y[i] = findperp( np.transpose(ax_val[i][3:6]), np.transpose(ax_val[i+1][3:6]), np.transpose(ax_val[i][0:3]), np.transpose(ax_val[i+1][0:3]))

for i in range(0,4):
	print sum(x[i,:] - y[i,:])
	a[i] = np.sqrt(sum(np.power(x[i,:] - y[i,:], 2)))
	#a(i)=sqrt(power(sum((x[:,i]-y[:,i]),2),1))
	# A(i)=(acos((ax_val(i,4:6))*(ax_val(i+1,4:6))'))*180/pi;
	# if i>1
	#     d(i)=sqrt(sum((x(:,i)-y(:,(i-1))).^2,1));
	# else
	#     d(i)=sqrt(sum((x(:,i)).^2,1));
	# end
	# end
print a