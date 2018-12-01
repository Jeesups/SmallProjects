import numpy as np
import matplotlib.pyplot as plt

a = input("Prosze podac wartosc A: ")
b = input("Prosze podac wartosc B: ")


def calculatePos(x):
    return int(a)*x + int(b)

plt.title("Wykres f(x) = a*x +b")

X = np.linspace(-10,10,endpoint=True)
temp_X = []

for i in range(0,len(X)):
    temp_X.append(int(a) * X[i] + int(b)) 
    

plt.plot(X,temp_X)
plt.show()