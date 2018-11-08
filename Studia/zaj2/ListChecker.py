
class ListChecker:
    '''
    Program ma wykonac szereg zadan zwiazanych z listami,
    wpierw uzytkownik musi wprowadzic n liczb do listy, oznacza to
    ze trzeba zrobic warunek konczacy zapis do listy.
    '''

    def __init__(self):
        self.num_list = []
        self.inp = ""
        self.isWorking = True

        self.createList()

    def addToList(self,value):
        self.num_list.append(value)
    
    def createList(self):
        print("Witaj w programie wypisujacym dane z listy")
        print("Dane zostaja wpisane do listy po czym nastepuje iteracja po nich")
        print("Wpisanie \"q\" spowoduje zakonczenie dodawania do listy")
        while self.isWorking:
            try:
                self.inp = str(input("Prosze podac wartosc: "))
                if(self.inp == "q"):
                    self.printVal()
                    self.isWorking = False
                else:
                    self.addToList(int(self.inp))
            except ValueError:
                print("To nie jest liczba!")

    
    def printVal(self):
        print("W tej chwili lista posiada {} elementow".format(len(self.num_list)))
        print("-----------------------------")
        self.printValAndIndex()
        print("-----------------------------")
        self.printReversed()
        print("-----------------------------")
        self.printSorted()
    def printValAndIndex(self):
        for i in range(0,len(self.num_list)):
            print("{} . {}".format(i,self.num_list[i]))

    def printReversed(self):
        for i in reversed(self.num_list):
            print("{} ".format(i))
    def printSorted(self):
        temp_list = self.num_list.copy()
        temp_list.sort()
        for i in temp_list:
            print(i)
    def delFromList(self):#Skonczyc usuwanie z listu o podanym indeksie
        try:
            self.inp = input("Prosze podac index do usuniecia")
            del self.num_list[int(self.inp)]
        except TypeError:
            print("Nieobslugiwany typ indeksu!")
  
        



lc = ListChecker()