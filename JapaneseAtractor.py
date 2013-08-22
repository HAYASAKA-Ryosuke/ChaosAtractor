#coding:utf-8
import scipy.integrate
import matplotlib.pyplot as plt
import math
import numpy

#F_x=lambda x,y:y-0.97*x+(5/(1+x**2))-5
#F_x=lambda a,x,y:y+a*x-(5/(1+x**2))+6+0.2*math.exp(-y**2)
#F_x=lambda a,x,y: y+a*x+(1/(1+x**2))
#F_y=lambda a,b,x,y:-b*x
#F_y=lambda x:x
F_x=lambda x,y:y
F_y=lambda x,y,ck,cB,t:-ck*y-x**3+cB*math.cos(t)

def Func(val,t,ck,cB):
    return [F_x(val[0],val[1]),F_y(val[0],val[1],ck,cB,t)]

xx=2.1
yy=0
a=-1.94
b=0.99
ck=0.05
cB=7.0
t=numpy.arange(0,8000,2*math.pi)
ansx=[]
ansy=[]
ans=scipy.integrate.odeint(Func,[xx,yy],t,args=(ck,cB,))
#for i in range(0,50,1):
#    x,y=Func([x,y],i,a,b)
#    ansx.append(x)
#    ansy.append(y)
plt.plot(ans.T[0],ans.T[1],'.')
plt.show()
