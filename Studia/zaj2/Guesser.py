import random

class Guesser:
    def __init__(self):
        self.score = 0
        self.temp_one = 0
        self.temp_word = ''

        self.words = ("python","gdansk","dlaczego","gdynia","wsb")
        print("""
            Witaj w grze 'Wymieszane litery'!
            Uporządkuj litery, aby odtworzyć prawidłowe słowo.
            (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
        """)
        self.correct_word = ""
        self.mixed = ""
        self.answer = ""
        self.mixWords()
        self.getAnswer()
        self.checkAnswer()

    def giveHint(self,char):
        'Method to gave hints if player asks for it'
        print("Jest tam znak: %s" % (char))

    def mixWords(self):
        'Method to get one word, and mix it'
        word = random.choice(self.words)
        self.correct_word = word

        while word:
            position = random.randrange(len(word))
            self.mixed += word[position]
            word = word[:position] + word[(position + 1):]

    def getAnswer(self):
        print("Zgadnij, jakie to słowo: %s" % (self.mixed))
        self.answer = input("\n Twoja odpowiedź: ")

    def checkAnswer(self):

        while self.answer != self.correct_word and self.answer != "":
            print("Niestety to nie to słowo.")
            print("Czy chcesz skorzystać z podpowiedzi?")
            choice = input("T/N")
            if (choice.upper() == "t".upper()):
                #TODO!!!!!!!
                #Zrobić tak, aby po sprawdzeniu słowa, by dodawał literkę do zbioru i pokazywał cały zbiór.
                self.score -= 1
                self.temp_word += self.correct_word[self.temp_one]
                self.giveHint(self.temp_word)
                self.temp_one += 1
            self.answer = input("Twoja odpowiedź: ")
        if(self.score == 0):
            self.score += 100
        if(self.answer == self.correct_word):
            print("Zgada się! Zgadłeś!\n")
            print("Zakończyłeś grę mając %s punktów" %(self.score))

game = Guesser()