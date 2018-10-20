import random

def Count(start,end,step):
    temp = start
    for i in range(start,end):
        print(temp)
        if(temp >= end):
            break
            print("OOB")
        else:
            temp += step



Count(20,60,10)
