import AdditionalFunctions as AF
import statistics as st

example_list_odd = [20,34,156,12,45]
example_list_even = [56,32,14,67,43,24]

#Mediany
print(AF.median(example_list_even))
print(AF.median(example_list_odd))

#Odchylenie standardowe
print(AF.stand_deviation(example_list_even))
print(AF.stand_deviation(example_list_odd))

#Srednia
print(AF.avg(example_list_even))
print(AF.avg(example_list_odd))
