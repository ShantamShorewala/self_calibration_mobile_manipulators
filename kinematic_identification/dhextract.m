clear;
% ax_val=load('C:\Users\USER\Desktop\Mydata_lt.csv');
% ax_val=load('C:\Users\USER\Desktop\My_data_8mm.csv');
% ax_val=load('C:\Users\USER\Desktop\My_data_8mm_it_ninit.csv');
% ax_val=load('C:\Users\user\Desktop\My_data_8mm_it_ninit_rcim.csv');
% ax_val=load('C:\Users\user\Desktop\rcim_aruco_cpm_perp6.csv');
% ax_val=load('C:\Users\user\Desktop\rcim_calib_cpm_perp.csv');
% ax_val=load('C:\Users\user\Desktop\rcim_uncalib_cpm_plan.csv');
% ax_val=load('E:\Riby Files 2\phd publications\RCIM\uncalib_235.csv');
% ax_val=load('C:\Users\USER\Desktop\My_data_cp_d0_1.csv');
% ax_val=load('My_data.csv');
% ax_val=load('C:\Users\useZ!qr\Desktop\aruco_map1.csv');

ax_val=load('/media/shantam/D6E430F0E430D509/youbot_k_identification/data/center.csv');
disp(ax_val)
nol=4;

a=[0,0,0,0,0]
A=[0,0,0,0,0]
d=[0,0,0,0,0]

% for i=1:nol
% %     if i~=2
% %         cross((ax_val(i,4:6))',(ax_val(i+1,4:6))')
% %         disp(findperp((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))'))
% % [x(:,i), y(:,i)] 
%            [x(1:3,i), y(1:3,i)] = findperp((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))');
% %     else
% %           [x(1:3,i), y(1:3,i)] = findperp((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))');
% %         [X_1, Y_1]=findperp((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))',y(:,i-1));
% %     end
% % sum((x-y).^2)
% %    2.0140e+04(:,



for i=1:nol
    if (i==1)
    cross((ax_val(i,4:6))',(ax_val(i+1,4:6))')
        [x(1:3,i), y(1:3,i)]=findperp((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))');
    else
        [x(1:3,i), y(1:3,i)]=(findperp_pl((ax_val(i,4:6))',(ax_val(i+1,4:6))',(ax_val(i,1:3))',(ax_val(i+1,1:3))',y(:,i-1)))
    end

disp("well then");
% disp(X);
% disp(acos((ax_val(i,4:6))*(ax_val(i+1,4:6))')*180/pi);
a(i)=sqrt(sum((x(:,i)-y(:,i)).^2,1));
A(i)=(acos((ax_val(i,4:6))*(ax_val(i+1,4:6))'))*180/pi;
if i>1
    d(i)=sqrt(sum((x(:,i)-y(:,(i-1))).^2,1));
else
    d(i)=sqrt(sum((x(:,i)).^2,1));
end
end
disp("a");
disp(a);
disp("A");
disp(A);
disp("d");
disp(d);


% %   141.9142
% [x(2) y(2)]=findperp([0.9992539   0.034533  -0.017298]',[-0.9276808   0.373364  -0.002735]',[23.0899288 1169.8971680 390.7329650]',[449.0340733 1389.6136334 -324.2216308]');
% a(2)=sqrt(sum((x(2)-y(2)).^2))
% % ans =
% %   697.2435
% [x(3) y(3)]=findperp([-0.0157597  -0.995207  -0.096508]',[-0.9276808   0.373364  -0.002735]',[11.7441323 411.2334465 -720.4734747]',[449.0340733 1389.6136334 -324.2216308]');
% a(3)=sqrt(sum((x(3)-y(3)).^2))
% %   282.2318
% [x(4) y(4)]=findperp([-0.0157597  -0.995207  -0.096508]',[-0.8886894  -0.327579   0.320817]',[11.7441323 411.2334465 -720.4734747]',[-47.8826622 508.0919030 -401.5162519]');
% a(4)=sqrt(sum((x(4)-y(4)).^2))
% %   263.6356
% [x(5) y(5)]=findperp([-0.0157597  -0.995207  -0.096508]',[-0.0654753   0.747513  -0.661012]',[11.7441323 411.2334465 -720.4734747]',[42.8032421 346.1181833 -329.6384624]');
% a(5)=sqrt(sum((x(5)-y(5)).^2))
% %     9.7162

