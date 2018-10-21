import statistics #Jezeli chcemy zrobic to szybciej
import math

def median(val):
    result = 0
    #Gdy parzysta ilosc elementow
    if(len(val)%2 == 0):
        result = val[math.floor(len(val)/2)-1]+val[math.ceil(len(val)/2)]/2

    #Gdy nieparzysta ilosc elementow
    if (len(val)%2 != 0):
        result = val[int(len(val) / 2)]

    return result

def avg(val):
    result = 0
    temp = 0
    for i in val:
        temp += i
    result = temp / 2
    return result

def stand_deviation(val):
    result = 0
    temp = 0 
    temp_list = val
    me = mean(val)
    
    for i in range(len(val)):
        temp_list[i] = (temp_list[i] - me) ** 2
        temp += temp_list[i]

    result = math.sqrt(temp/(len(val)-1))
    return result

#Support function
def mean(val):
    result = 0
    temp = 0
    for i in val:
        temp += i
    result = temp / len(val)
    return result

