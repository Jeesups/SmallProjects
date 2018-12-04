

class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.askForValues()
        self.checkValues()
    def askForValues(self):
        print("Witaj w programie w ktorym dowiesz sie czy z danych bokow da sie utworzyc trojkat")
        print("Podaj kolejno 3 wartosci by sprawdzic czy udaloby sie utworzyc z nich trojkat")
        self.a = int(input("Prosze podac wielkosc pierwszego boku: "))
        self.b = int(input("Prosze podac wielkosc drugiego boku: "))
        self.c = int(input("Prosze podac dlugosc podstawy: "))

    def checkValues(self):
        if((self.b - self.c) < self.a and self.a < (self.b + self.c) ):
            print("Boki spelniaja nierownosci")
            print("Jest mozliwe utworzenie trojkatu")
        else:
            print("Nie da sie utworzyc jakiegokolwiek trojkatu")
        if (self.c**2 == self.a**2 + self.b**2):
            print("Da sie utworzyc takze trojkat prostokatny")
        else:
            print("Nie da sie utworzyc trojkatu prostokatnego")
    

tr= Triangle()