import numpy as np
import matplotlib.pyplot as plt


class QuadraticEquation():
    def __init__(self):
        self.X = np.arange(-10,10)
        self.temp_X = []
        self.a = 1
        self.b = -3
        self.c = 1

        self.calc()
        self.drawGraph()

    def calc(self):
        for i in range(0,len(self.X)):
            val = self.a * self.X[i]**2 + self.b*self.X[i] + self.c
            self.temp_X.append(val)

    def drawGraph(self):
        plt.plot(self.X,self.temp_X)
        plt.show()


qe = QuadraticEquation()