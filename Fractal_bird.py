#coding:utf-8
import matplotlib.pyplot as plt
import math

F_x=lambda a,b,x,y:y+a*x-(5/(1+x**2))+6+0.2*math.exp(-y**2)
F_y=lambda a,b,x,y:-b*x

def Func(val,t,a,b):
    return [F_x(a,b,val[0],val[1]),F_y(a,b,val[0],val[1])]

x=1
y=0
a=-1.6
b=0.99
ansx=[]
ansy=[]
for i in range(0,900):
    x,y=Func([x,y],i,a,b)
    ansx.append(x)
    ansy.append(y)
plt.plot(ansx,ansy,'*')
plt.show()
