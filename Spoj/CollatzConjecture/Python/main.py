
class Application:
    def __init__(self):
        self.values = []
        self.counter = 0 
        self.input = 0
        self.adding = True
    def getValues(self):
        self.counter = input()
        while self.adding:
            self.input = input()
            if(str(self.input).upper() == 'koniec'.upper()):
                self.adding = False

    def calculate(self):
        pass