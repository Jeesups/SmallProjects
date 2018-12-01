import numpy as np 
import matplotlib.pyplot as plt

A = np.arange(20)
X,Y = np.meshgrid(A,A)
Z = X + Y
plt.imshow(Z,cmap='hot',interpolation='none')
plt.colorbar()
plt.show()