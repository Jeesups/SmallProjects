import math

class SquareEquasion():
    def __init__(self,*args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.delta = 0

        self.calculate_Delta()


    def calculate_Delta(self):
        self.delta = (self.b**2) - (4*self.a*self.c)
        
        if(self.delta < 0):
            print("Brak pierwiastkow funkcji")
        elif(self.delta == 0):
            answer = -self.b/(2*self.a)
            print("Pierwiastek wynosi {}".format(answer))
        elif(self.delta > 0):
            x1 = ((-self.b - math.sqrt(self.delta))/2*self.a)
            x2 = ((-self.b + math.sqrt(self.delta))/2*self.a)
            print("""Pierwiastek x1 wynosi: {} \nPierwiastek x2 wynosi: {}""".format(x1,x2))




if __name__ == '__main__':
    squareequasion = SquareEquasion(1,2,-3)