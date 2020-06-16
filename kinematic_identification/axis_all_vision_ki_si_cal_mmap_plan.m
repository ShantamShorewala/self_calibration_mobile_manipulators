% load the data given by KUKA LBR 
% load circ_test.mat
% nwar=1000*cpmxyzr2;
%  nwar=1000*cpmxyz;
%  nwar=1000*cpmxyz_rct;
load('/media/shantam/D6E430F0E430D509/youbot_k_identification/23_12/poses/new_3')
nwar=1000*new_4(:,2:4)
%  nwar=cpmxyzr;
%  nwar=pdat;
%  nwar=pdat(1:40,:);
% nwar=cpmxyzr;
% nwar=1000*cpmxyz;
% nwar=cpmxyz_r1;
% nwar=pdat;
% p_p_ax=15;
p_p_ax=size(nwar,1);
% p_p_ax=10;
% create a matrix of the data of joint 6
for i=0:1:0
%cpm stretched perpendicular
    %joint 1 : 2:10
    %joint 2 : 11:20
    %joint 3 : 21:30
%joint 4 : 31:39 range=((i)*10+2):((i+1)*10);
    %joint 5 : 42:50
    %joint 6 : 51:57
%  range=((i)*20+1):((i+1)*20);
range=((i)*p_p_ax+1):((i+1)*p_p_ax);
% range=1:60;

C = {'k','b','r','g','y','k'};
x=nwar((range),1);
y=nwar((range),2);
z=nwar((range),3);
% plotting original set of data to get a feel of spread
% figure(1)
% plot3(x,y,z)
                

% creating a matrix of set of datas as [x y z]
dat=[x  y  z];
%plotting the data
figure(2)
plot3(dat(:,1),dat(:,2),dat(:,3),'o')
% see the xy view which will give intution that it is not in a plane
%mean or centroid of the data set
mean_dat=mean(dat);
%subtracting mean from each element
dat_minus_mean = bsxfun(@minus,dat,mean(dat));
K=dat_minus_mean;
% singular value decomposition
%placing zero as svd(a,0) gives only non sero singular value matrix 
[U,S,V] = svd(K,0);
%The matrix V  contains orthonormal bases for the column space of                                 K
%  data and for its orthogonal complement. 

S
V
% the first two columns of V  comprise the orthonormal basis [V(:,1), V(:,2)]
%% the last column gives normal to the plane V(:,3)
n=V(:,3)
%% Projecting the points on the plane 
R=V'*K';
TT=V*K'; %// checking inner product%
%Thus, the first two rows of R  are taken as x and y-coordinates of points in an 
 % xy -plane spanned by [V(:,1), V(:,2)]
U1=R(1,:)';
U2=R(2,:)';
% here we put the data in col. after multiplying by factor 2 (also in example)--??
A=[2*U1 2*U2 ones(size(range,2),1)];
%a vector b as sum of squares of x and y
b=[U1.^2+U2.^2];
% solution for the above matrix Ax=b with least square
c=pinv(A)*b;
%% Radius of the circle
r=sqrt(c(3)+(c(1)^2)+(c(2)^2));
%Center of the circle in 2D plane with projected points
v=[c(1) c(2) 1];
% Transfering back to the 3D plane by adding Centroid
center=(c(1)*V(:,1)+c(2)*V(:,2)+mean_dat');
center_coordinate=[center(1) center(2) center(3)]
hold on
plot3(center(1),center(2),center(3),'*r')
% plotting of normal from center
% grid on
hold on
quiver3(center(1),center(2),center(3),n(1),n(2),n(3),100,'g')

hold on
plotCircle3D_color(center_coordinate,n',r,(i+1))
text(center(1),center(2),center(3),['Center',num2str(i+1)],'FontSize',5)
% axis equal
%      axis ([-700 700 -1000 1000 -10 1500])
hold on
 plot3(0,0,0,'r*','MarkerSize',25)
% % 
data1=[center_coordinate n' r]; %Sample 2-dimensional data
% xlswrite('C:\Users\user\Desktop\My_data.xls',data1)
% fid = fopen('C:\Users\user\Desktop\cmeri_aruco_refn_resid_axwise.csv', 'a');
% opened = fopen('/media/shantam/D6E430F0E430D509/youbot_k_identification/data/center.csv', 'a');
% fprintf(fid,'%6.7f %12.7f %20.7f %30.7f %35.7f %40.7f\r\n', data1)
% fprintf(opened,'%1.7f %10.7f %10.7f %10.7f %10f %10f %10f\r\n', data1);
% fwrite(fid,num2str(data1))
fclose(opened);
clear fid;
% success = xlsappend('myworkbook.xls',data1)
figure(3+i)
plot3(dat(:,1),dat(:,2),dat(:,3),'color',C{(i+1)},'marker','o')
title(['Points of Joint ',num2str((i+1))])
grid on
end


