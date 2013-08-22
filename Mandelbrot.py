#coding:utf-8
import matplotlib.pyplot as plt
import math

F_x=lambda a,b,x,y:x**2-y**2+a
F_y=lambda a,b,x,y:2*x*y+b

def Func(val,t,a,b):
    return [F_x(a,b,val[0],val[1]),F_y(a,b,val[0],val[1])]

x=0
y=0
a=-1.74972763
b=-0.00003417
ansx=[]
ansy=[]
for i in range(-1500,500):
    for j in range(-10000,10000):
        x=i*0.5
        y=j*0.005
        if(x**2+y**2<=4):
            x,y=Func([x,y],i,a,b)
            ansx.append(x)
            ansy.append(y)
plt.plot(ansx,ansy,'*')
plt.show()
