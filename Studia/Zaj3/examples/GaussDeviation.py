import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
mi,sigma = 100,15
x = mi + sigma * np.random.randn(10000)
sigma ** 2
n,bins,patches = plt.hist(x,50,density = True,facecolor='green',alpha = 0.75)

bincenters = 0.5 *(bins[1:]+bins[:-1])
y = mlab.normpdf(bincenters,mi,sigma)
l = plt.plot(bincenters,y,'r--',linewidth = 1)