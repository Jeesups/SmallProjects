from pylab import *
def f(x,y):
    return exp(-x**2-y**2/4)+\
    exp(-(x+2)**2-y**2/2)+\
    exp(-(x-2)**2-2*y**2)

n=256
z = 3.5
x = linspace(-z,z,n)
y = linspace(-z,z,n)
X,Y = meshgrid(x,y)
contourf(X,Y,f(X,Y),8)
C = contour(X,Y,f(X,Y),8,colors='b',linewidth =1)
clabel(C,inline=1,fontsize = 10)
savefig("kontur.png")
show()