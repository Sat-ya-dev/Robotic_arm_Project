import numpy as np
import matplotlib.pyplot as plt
import math

#length of link1 and link2 arm
l1 = 9.28
l2 = 8.04

x = []
y = []
#plotting the area the 2-link arm can cover
for i in range(0,180):
    for j in range(0,180):
        t1 = np.radians(i)
        t2 = np.radians(j)
        x.append(l1*np.cos(t1)+l2*np.cos(t1+t2)) # x coordinate equation
        y.append(l1*np.sin(t1)+l2*np.sin(t1+t2)) # y coordinate equation

plt.scatter(x,y,color='b')
# plt.show()

# X,Y coordinates for letter M
X=[-13, -13, -13, -13, -13, -13, -13, -13, -13, -13,-12.722, -12.444, -12.167, -11.889, -11.611, -11.333, -11.056, -10.778,-10.5, -10.222, -9.944, -9.667, -9.389, -9.111, -8.833, -8.556, -8.278,-8, -8, -8, -8, -8, -8,-8,-8,-8,-8]
Y=[0.0, 0.556, 1.111, 1.667, 2.222, 2.778, 3.333, 3.889, 4.444, 5.0,4.444, 3.889, 3.333, 2.778, 2.222, 1.667, 1.111, 0.556,0.0, 0.556, 1.111, 1.667, 2.222, 2.778, 3.333, 3.889, 4.444, 5.0,4.444,3.889,3.333,2.778,2.222,1.667,1.111,0.556,0]

# print(len(X))
# plt.scatter(X,Y,color='r')

theta1 = [] # angle made by link1
theta2 = [] # angle made by link2 wrt link1
# calculating theta1 and theta2 values for x-y pairs
for i in range(len(X)):
    x = X[i]
    y = Y[i]
    a = np.arccos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
    theta2.append(a)
    c=l2*np.sin(a)/(l1+l2*np.cos(a))
    b=np.arctan(y/x) - np.arctan(c) + np.pi
    theta1.append(b)

# new theta1 , theta2 in degrees values after rounding off to nearest integers
nt1=[]
nt2=[]
for i in range(len(X)):
    nt1.append(np.round(np.degrees(theta1[i])))
    nt2.append(np.round(np.degrees(theta2[i])))
    # nt1.append(np.degrees(theta1[i]))
    # nt2.append(np.degrees(theta2[i]))

#New x y coordinates with the new theta1 and theta2 values
x_n = []
y_n = []
for i in range(len(X)):
    a=np.radians(nt1[i])
    b=np.radians(nt2[i])
    x_n.append(l1*np.cos(a)+l2*np.cos(a+b))
    y_n.append(l1*np.sin(a)+l2*np.sin(a+b))

plt.scatter(x_n,y_n,color='r')
plt.show()
# print(nt1)
# print(nt2)