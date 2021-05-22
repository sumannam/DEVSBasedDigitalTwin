# -*- coding: utf-8 -*- 
import simpy.r
import time
import numpy as np
import matplotlib.pyplot as plt

path_list = [[0,0], [1,1], [2,4], [3,9], [4,16]]
x_points = []
y_points = []

#x_values과 y_values에 2차원 리스트의 값을 각각 넣기 위해 X, Y 값 분리
for i in range(len(path_list)):
    for j in range(len(path_list[i])):
        if j == 0:
            x_points.append(path_list[i][j])
        else:
            y_points.append(path_list[i][j])

x_values = np.array(x_points)
y_values = np.array(y_points)

plt.plot(x_values, y_values) # 그래프에 line(Path)를 그립니다

# 그래프에 점을 통해 이동 경로 표시
for i in range(len(path_list)):
    point = path_list[i]
    x = point[0]
    y = point[1]
    plt.scatter(x, y)
    plt.pause(1)

# 그래프를 화면 표시
plt.show() 
