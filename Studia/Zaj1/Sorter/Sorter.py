import random
#I needs to do it in reverse way than this 6.10.2018
class Sorter():
    def __init__(self,lists):
        self.List = lists
        self.printList()
        self.sort()
        print("_---------------------------_")
        self.printList()

    def sort(self):
        for passnum in range(len(self.List)-1,0,-1):
            for i in range(passnum):        
                if(self.List[i] > self.List[i+1]):
                    temp = self.List[i]
                    self.List[i] = self.List[i+1]
                    self.List[i+1] = temp
        
    def printList(self):
        for element in reversed(self.List):
            print(element)


def generateRandomList():
    l = [1]
    for i in range(50):
        l.append(random.randrange(100))
    return l
    
list = generateRandomList()
app = Sorter(list)
