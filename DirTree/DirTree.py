import os

class DirTree():
    def __init__(self,directory):
        self.dir = directory
        
        self.drawTree()
    def drawTree(self,extension = ''):
        extension = extension.lower()
        for dirpath, dirnames, files in os.walk(self.dir):
            for name in files:
                if extension and name.lower().endswith(extension):
                    print(os.path.join(dirpath,name))
                elif not extension:
                    print(os.path.join(dirpath,name))


if __name__ == '__main__':
    dirtree = DirTree('C:\Development')
    