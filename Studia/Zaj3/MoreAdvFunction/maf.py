import numpy as np
import matplotlib.pyplot as plt

a = input("Prosze podac A: ")

X = np.linspace(-10,0,endpoint = True)
X1 = np.linspace(0,10, endpoint = True)
temp_X1 = []
temp_X2 = []
plt.title("Wykres f(x)")

for i in range(0,len(X)):
    if(X[i] <= 0):
        temp_X1.append(X[i]/(-3)+int(a))
    #if(X1[i] >= 0):
    #    temp_X2.append(X[i]*X[i]/3)
for i in range(0,len(X1)):
    if(X1[i] >= 0):
        temp_X2.append(X[i]*X[i]/3)
#Przerobic program, pewnie uciac ilosc tablic do jednej i tam zrobic poprawki
plt.plot(X,temp_X1)
plt.plot(X,temp_X2)

plt.show()