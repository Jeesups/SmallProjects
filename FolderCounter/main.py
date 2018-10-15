import os

class Application():
    def __init__(self):
        self.dirList = os.listdir("C:\Development")
        self.testThis()
        self.countDirectories()

    def countDirectories(self):
        number_of_files = len(self.dirList)
        print(number_of_files)

if __name__ =="__main__":
    app = Application()
