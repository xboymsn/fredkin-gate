import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
x = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
o = [[0,0],[0,1],[1,0],[1,1],[0,0],[1,0],[0,1],[1,1]]
e = 1
teta1 = 0.2
teta2 = -1.3
eta = 0.1
w = [[1,2,3],[3,2,1]]
z=w
#wt = [[1,4],[2,5],[3,6]]
fig = plt.figure()
ax = plt.axes(projection='3d')
xt = np.transpose(x)
ax.scatter(xt[0],xt[1],xt[2])
plt.show()
epoch = 1
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
    print("..............")
    print(f"epoch:{epoch}")
    print(f'teta1:{teta1}')
    print(f'teta2:{teta2}')
    print(f'w:{w}')
    print(f'y:{y}')
    print(f'e:{e}')
    epoch+=1

"""متن فایل را در ژوپیتر نوت بوک  کپی کرده و اجرا کنید"""