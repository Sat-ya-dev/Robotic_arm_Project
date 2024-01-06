# simulating the positions and storing it in gif
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter

writer=PillowWriter(fps=10)
fig=plt.figure()
a1=[142.0, 140.0, 137.0, 135.0, 133.0, 131.0, 130.0, 128.0, 127.0, 125.0, 125.0, 125.0, 125.0, 126.0, 126.0, 128.0, 129.0, 131.0, 133.0, 129.0, 125.0, 120.0, 116.0, 112.0, 108.0, 105.0, 101.0, 97.0, 99.0, 102.0, 104.0, 107.0, 110.0, 114.0, 117.0, 121.0, 125.0]
a2=[83.0, 83.0, 83.0, 82.0, 81.0, 80.0, 79.0, 77.0, 75.0, 73.0, 78.0, 83.0, 87.0, 91.0, 94.0, 98.0, 101.0, 103.0, 106.0, 108.0, 110.0, 111.0, 113.0, 114.0, 114.0, 115.0, 115.0, 114.0, 117.0, 119.0, 120.0, 122.0, 123.0, 124.0, 125.0, 125.0, 126.0]

temp1=[]
temp2=[]
with writer.saving(fig,'graph.gif',100): #The gif with file name graph will be created in the present directory
    for i in range(len(a1)):
        temp1.append(0.0928*np.cos(np.radians(a1[i]))+(0.0843*np.cos(np.radians(a2[i]+a1[i]))))
        temp2.append(0.0928*np.sin(np.radians(a1[i]))+(0.0843*np.sin(np.radians(a2[i]+a1[i]))))
        plt.plot(temp1,temp2,'b')
        writer.grab_frame()

    temp1=[]
    temp2=[]