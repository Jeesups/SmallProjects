#Open file, make copy of text, delete words in file using list, save file.
class StringRemover():
    def __init__(self, filename):
        self.blacklisted_words = ["According","black","white"]
        self.filename = filename
        self.openFile()

    def checkForWords(self,words):
        '''
        sprobowac odwrocic, wpierw niech czyta linie tekstu, potem niech sprawdza
        zakazane slowa, linie powinny zostac podzielone na oddzielne listy aby latwiej mozna bylo je porownac.
        '''
        for word in words:
            for i in self.blacklisted_words:
                #It doesnt seem to find later any word equal to blacklisted word
                word.split()
                print(word)
                if word.upper() == i.upper():
                    print(word)
                    word = ''
                   
                else:
                    continue

    def openFile(self):
        file_object = open(self.filename,'r')
        with file_object as file:
            line = file.readlines()
            self.checkForWords(line)


sremover = StringRemover("Script.txt")


