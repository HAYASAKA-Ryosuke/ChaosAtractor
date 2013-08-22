#coding:utf-8
import matplotlib.pyplot as plt
import math

F_x=lambda a,b,x,y:y-a*x+b/(1+x**2)
F_y=lambda a,b,x,y:-x

def Func(val,t,a,b):
    return [F_x(a,b,val[0],val[1]),F_y(a,b,val[0],val[1])]

x=0
y=0
a=0.893
b=2.525
ansx=[]
ansy=[]
for i in range(0,80000):
    x,y=Func([x,y],i,a,b)
    ansx.append(x+y)
    ansy.append(x-y)
plt.plot(ansx,ansy,'*')
plt.show()
