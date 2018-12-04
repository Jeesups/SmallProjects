

class CaesarCipher():
    def __init__(self):
        self.offset = 3
        self.line = ""
        
        self.getLine()
        self.printAll()
    def code(self,text):
        ciphered = ""
        for i in range(len(text)):
            if(ord(text[i])> 122 - self.offset):
                ciphered += chr(ord(text[i]) + self.offset - 26)
            else:
                ciphered += chr(ord(text[i]) + self.offset)
        return ciphered

    def getLine(self):
        self.line = input("Prosze podac slowo do zaszyfrowania: ")

    def printAll(self):
        print("Slowo przed szyfrowaniem")
        print(self.line)
        print("Slowo po szyfrowaniu \n{}".format(self.code(self.line)))


cs = CaesarCipher()