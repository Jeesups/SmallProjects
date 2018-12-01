from pylab import *
from mpl_toolkits.mplot3d\
import Axes3D

fig = figure()
axe=Axes3D(fig)
n = 40
z = 10
x = linspace(-z,z,n)
y = linspace(-z,z,n)
X,Y = meshgrid(x,y)
R = sqrt(X**2 + Y ** 2)
Z = sin(R)/R
axe.plot_surface(X,Y,Z,rstride = 1, cstride = 1,cmap="hot")
savefig("3d.png")
show()