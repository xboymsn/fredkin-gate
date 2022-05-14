#!/usr/bin/env python
# coding: utf-8

# In[128]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from copy import deepcopy


# In[129]:

#نسخه ی دوم(فرعی) تمرین که با اضافه شدن s به عنوان خروجی برای نمایش صفحه مناسب تر شده است
#نمایش کامل نشده و ایراد دارد
x = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
o = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,1,0],[1,0,1],[1,1,1]]
e = 1
teta1 = 1.8
teta2 = 1.6
eta = 0.1
w = [[1,1.4,-3],[2,0.2,3.1],[0,0,0]]
z=w
#wt = [[1,4],[2,5],[3,6]]


# In[134]:

def plate(p,wm):
    print(y)
    point  = p
    w =deepcopy(wm)
    #w.pop(-1)
    print(f"im here in plate:  w{w}")
    print(w)
    point2 = np.array([5, 5, 5])

    d = -point.dot(w)

    xx, yy = np.meshgrid(range(10), range(10))

    z1 = (-w[0][1] * xx - w[0][2] * yy - teta1) * 1. /w[0][0]
    z2 = (-w[1][1] * xx - w[1][2] * yy - teta2) * 1. /w[1][0]

    plt3d = plt.figure().gca(projection='3d')
    plt3d.plot_surface(xx, yy, z1, alpha=0.2)

    plt.show()

while e>0 :
    e=0
    for i in range(8):
        y=[None,None]
        wt = np.transpose(w)
        y =np.matmul(x[i],wt)
        #y = x[i]*wt
        if y[0] >= teta1:
            y[0] = 1
        else:
            y[0] = 0
        if y[1] >= teta2:
            y[1] = 1
        else:
            y[1] = 0
        if y[0]!=o[i][0]:
            teta1=teta1 -eta*((o[i][0])-y[0])
            w[0] = w[0] + (eta*(o[i][0]-y[0])*np.array(x[i]))
            e = e + abs(o[i][0]-y[0])
        if y[1]!=o[i][1]:
            teta2=teta2 -eta*(o[i][1]-y[1])
            w[1] = w[1] + (eta*(o[i][1]-y[1])*np.array(x[i]))
            e = e + abs(o[i][1]-y[1])
            pass

    print(f'teta1:{teta1}')
    print(f'teta2:{teta2}')
    print(f'w:{w}')
    print(f'y:{y}')
    print(f'e:{e}')
    plate(y,w)
    #plt3d = plt.figure().gca(projection='3d')
    #plt.plot(w[0][0],w[0][1],w[0][2],w[1][0],w[1][1],w[1][2])
    #xx, yy = np.meshgrid(range(10), range(10))
    #plt3d.plot_surface(xx,yy,zz,alpha=0.2)
    #ax= plt.gca()
    #ax.hold(True)
    #ax.scatter(0,10,-10)
    #plt.show()


# In[133]:



# In[ ]:




