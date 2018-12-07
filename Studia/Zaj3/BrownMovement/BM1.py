import numpy as np
import random
import matplotlib.pyplot as plt

class BrownMovement():
    def __init__(self):
        self.input = 0
        self.x,self.y = 0, 0
        self.lx = [0]
        self.ly = [0]
        self.s = 0
        self.getMovementAmount()
        self.calcAngle()
        self.calcVector()
        self.drawGraph()


    def calcAngle(self):
        for i in range(0,self.input):
            rad = float(random.randint(0,360))* np.pi / 180
            self.x = self.x + np.cos(rad)   #Wyliczenie losowego x
            self.y = self.y + np.sin(rad)   #wyliczenie losowego y
            self.lx.append(self.x)
            self.ly.append(self.y)

    def getMovementAmount(self):
        self.input = int(input("Prosze podac ilosc ruchow: "))

    def calcVector(self):
        self.s = np.fabs(np.sqrt(self.x**2 + self.y**2))
        print("Wektor przesuniecia {}".format(self.s))

    def drawGraph(self):
        plt.plot((0, self.lx[-1]),(0,self.ly[-1]),color="blue")
        plt.plot(self.lx,self.ly, "o:",color="green",linewidth = 2,alpha = 0.5)
        plt.legend(["Dane x,y\nPrzemieszczenie: " +str(self.s)],loc="upper left")
        plt.xlabel("lx")
        plt.ylabel("ly")
        plt.title("Brown Movement")
        plt.grid(True)
        plt.show()


if(__name__ =="__main__"):
    bm = BrownMovement()