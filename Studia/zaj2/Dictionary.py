import json   #Tym bede zapisywal dane do pliku i odczytywal je z pliku
"""
TODO: 
Zmodyfikować trzeba metody wczytujące i zapisujące do pliku, niech
wpierw program zapisuje do zmiennej listy słownik, po czym niech
go wysle gdy uzytkownik to potwierdzi.

"""

class Dictionary():

    def __init__(self):
        self.dictionary = {}
        self.inputKey = ""
        self.inputValue = ""
        self.inputChoice = ""
        self.exit = False
        self.file = ""


        self.startingMessage()
        
        while not self.exit:
            self.checkInput()

    def readFile(self):
        with open('dict.json') as data_file:
            self.file = json.load(data_file)
    
    def writeFile(self,source):
        #Dodac Try catch aby stworzyl plik TXT gdy go nie ma,
        #Inaczej dziala w modzie append (a)
        try:
            json.dump([source],open("dict.json",'a')) 
        except IOError:
            file = open("dict.txt",w)
            file.close()

    def modifyDict(self,key,value):
        self.dictionary[key] = value
    
    def addToDict(self,key,value):
        self.dictionary[str(key)] = str(value)
        print("Pozycja o kluczu {} i wartosci {} zostala dodana".format(key,value))

    def getInputChoiceFromUser(self):
        self.inputChoice = input("Wybor: ")

    def getInputValueFromUser(self):
        self.inputValue = input("Wartosc: ")
    def getInputKeyFromUser(self):
        self.inputKey = input("Klucz: ")

    def searchByKey(self,key):
        return self.file[key]
    def deleteByKey(self,key):
        del self.file[key]

    def startingMessage(self):
        
        self.optionMenu()

    def optionMenu(self):
        print("Witam w słowniku")
        print("Co chcesz zrobic?")
        print("1.Dodać nowa pozycje")
        print("2.Wyswietlic WSZYSTKIE pozycje w slowniku")
        print("3.Wyswietlic POSZCZEGOLNE pozycje w slowniku")
        print("4.Usunac pozycje ze slownika")
        print("5.Zakonczyc")
        self.getInputChoiceFromUser()

    def checkInput(self):
        if(self.inputChoice == '1'):
            print("\n Prosze podac wartosci do dodania")
            self.getInputKeyFromUser()
            self.getInputValueFromUser()
            self.addToDict(self.inputKey,self.inputValue)
            self.writeFile(self.dictionary)
            
            self.optionMenu()
       
        elif(self.inputChoice == '2'):
            print("Wyswietlam wszystkie klucze wraz z ich wartosciami")
            self.readFile()
            for key in self.file:
               print("{}".format(key))
            
            self.optionMenu()
            
        elif(self.inputChoice == '3'):
            print("Prosze podac klucz do wyszukania")
            key = self.getInputKeyFromUser()
            print(self.searchByKey(key))

            self.optionMenu()
            

        elif(self.inputChoice == '4'):
            print("Prosze podac klucz do usuniecia")
            key = self.getInputKeyFromUser()
            self.deleteByKey(key)

            self.optionMenu()

        elif(self.inputChoice == '5'):
            self.exit = True
            print("Do zobaczenia!")
        
        else:
            print("ZLY NUMER OPCJI")
            self.checkInput()

dicts = Dictionary()