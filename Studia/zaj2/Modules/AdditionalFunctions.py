import statistics #Jezeli chcemy zrobic to szybciej
import math

def median(list):
    result = 0
    #Gdy parzysta ilosc elementow
    if(len(list)%2 == 0):
        result = list[math.floor(len(list/2))]+list[math.ceil(len(list)/2)]

    #Gdy nieparzysta ilosc elementow
    if (len(list)%2 != 0):
        result = list[len(list / 2)]

    return result

def avg():
    pass

def stand_deviation():
    pass

print(__file__)