import matplotlib.pyplot as plt
import numpy as np


class App:
    def __init__(self):
        self.x = np.linspace(0.0, 2.0,100)
               
        self.createPlot()
        self.modifyLabels()

        plt.title("Different Styles")
        plt.legend()
        plt.show()

    def modifyLabels(self):
        plt.xlabel("x label")
        plt.ylabel("y label")
    def createPlot(self):
        plt.plot(self.x,self.x, label='One', ls=":")
        plt.plot(self.x,self.x/2, label="Two",ls="--")
        plt.plot(self.x,self.x**2, label="Three",ls="-.")

a = App()