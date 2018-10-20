import random

class WordGuesser():
    def __init__(self):
        #TODO   dorobic petle ktora bedzie dzialac do momentu zakonczenia przez uzytkownika.
        self.gameStart = True
        self.chances = 6
        self.temp_word = ""
        self.correct_word = ""
        self.counted_words = 0
        self.words = ("python", "gdansk", "dlaczego", "gdynia", "wsb")
        self.answer = ""

        # Blok szykujący grę
        self.beginGame()
        self.randomizeWord()
        self.countWord()

        #Glowne metody gry
        print("Komputer wylosował slowo, jest ono dlugosci: {} liter".format(self.counted_words))
        print("Prosze podać proponowaną literę.")
        self.getAnswer()
        self.askQuestion()


    def countWord(self):
        self.counted_words = len(self.correct_word)

    def randomizeWord(self):
        self.correct_word = self.words[random.randint(0, len(self.words) - 1)]

    def beginGame(self):
        print("""
            Witaj w grze zgadnij słowo!
            Zasady gry są prostę
            Komputer losuje jedno słowo z listy
            Po czym daje szansę na znalezienie pojedynczych liter w słowie
            Po wykorzystaniu wszystkich szans musisz podać wylosowane słowo.
            UWAGA! Komputer może odpowiadać jedynie TAK/NIE na szukane litery.
            Dodatkowo pierwszą darmową podpowiedzią jest ilość liter!
            Gracz ma jedynie 5 szans na odgadnięcie litery
            POWODZENIA!
        """)

    def getAnswer(self):
        self.answer = input("")

    def askQuestion(self):
        if(self.answer in self.correct_word and self.chances > 0):
            print("TAK")
            self.temp_word += self.answer
            self.chances -= 1
            print(self.temp_word)
        else:
            print("NIE")
    def checkAnswer(self):
        if(self.answer == self.correct_word):
            print("Gratulacje, to jest to słowo!")
        else:
            print("Przykro mi, proszę spróbować ponownie")
            self.getAnswer()

word = WordGuesser()