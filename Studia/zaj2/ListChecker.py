
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
        print("-----------------------------")
        print("Lista przed usunieciem elementu o wskazanym ID")
        self.printValAndIndex()
        self.delFromList()
        print("Lista po usunieciu elementu o wskazanym ID")
        self.printValAndIndex()
        print("-----------------------------")
        self.countEntries()
        print("-----------------------------")
        self.getFromTo()
        print("-----------------------------")

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
    def delFromList(self):
        try:
            self.inp = input("Prosze podac index do usuniecia: ")
            del self.num_list[int(self.inp)]
        except TypeError:
            print("Nieobslugiwany typ indeksu!")
        except IndexError:
            print("ID poza zasiegiem!")
            self.inp = input("Prosze podac index do usuniecia: ")
            del self.num_list[int(self.inp)]
    def countEntries(self):#Funkcja ma zapytac sie o element i sprawdza ilosc wystapien i pierwszy index obiektu.
        self.inp = input("Prosze podac nazwe elementu aby go wyszukac: ")
        counter = 0
        
        for i in self.num_list:
            #Dodac tutaj iteracje przez liste i zliczanie elementow.
            if(self.inp == str(i)):
                counter = counter + 1
        
        print("Ilosc wystapien wartosci {} = {}".format(self.inp,counter))
        print("Pierwszy index wartosci {} to {}".format(self.inp,self.firstOfKind(self.num_list,self.inp)))
    def firstOfKind(self,arr,inp):
        for i in arr:
            if(inp == str(i)):
                return arr.index(i)

    #Funkcja ma wybrac elementy z podanego zakresu przez uzytkownika
    #Trzeba zrobic wyjatki zlej wartosci czy indexu poza zasiegiem.
    def getFromTo(self):
        try:
            begin = input("Prosze podac od ktorego indexu mam wczytac.")
            end = input("Prosze podac do ktorego indexu mam wczytac.")
            for i in range(int(begin),int(end)+1):
                print(self.num_list[i])
        except ValueError:
            print("Zla wartosc jako zakres!")
        except IndexError:
            print("Index poza zakresem!")
lc = ListChecker()