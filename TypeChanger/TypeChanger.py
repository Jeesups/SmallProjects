import os

class TypeChanger():
    def __init__(self,directory):
        self.dir = directory
        self.changeType()
    def changeType(self):
        for filename in os.listdir(self.dir):
            infilename = os.path.join(self.dir,filename)
            if not os.path.isfile(infilename):
                continue
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.jpg','.png')
            output = os.rename(infilename,newname)
            
if __name__ == '__main__':
    typechanger = TypeChanger('.')
