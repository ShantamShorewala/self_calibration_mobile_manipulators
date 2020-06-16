function plotCircle3D_color(center,normal,radius,i)
C = {'k','b','r','g','y','k'};
theta=0:0.01:2*pi;
v=null(normal);
points=repmat(center',1,size(theta,2))+radius*(v(:,1)*cos(theta)+v(:,2)*sin(theta));
plot3(points(1,:),points(2,:),points(3,:),'color',C{i});

end