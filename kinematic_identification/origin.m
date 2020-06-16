vals = load('/media/shantam/D6E430F0E430D509/youbot_k_identification/23_12/poses/plane')
points = 1000*vals(:,2:4)

normal = fitNormal(points, false)
% normal = [0.015 1.000 0.007]

% -193.9716886 285.0898082 376.6208542
c_1 = [-193.9716886 136.445 376.6208542]
% c_1 = [-556.2291082 84.2683106 786.8063705]
% 136.4459983
[Well well] = dist2plane(c_1, normal)