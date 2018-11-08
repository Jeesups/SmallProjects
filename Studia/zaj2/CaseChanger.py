
class CaseChanger:
    def __init__(self):
        self.word = "aAbBcCdD"
        self.printWord()
        self.checkCases(self.word)
        self.printWord()
    def checkCases(self,word):
        tempstring = ""
        for i in range(0,len(word)):
            if(word[i].isupper()==True):
                tempstring += word[i].lower()
            if(word[i].islower()==True):
                tempstring += word[i].upper()
        self.word = tempstring
            

    def printWord(self):
        print("------------------")
        for i in self.word:
            print(i)

app = CaseChanger()