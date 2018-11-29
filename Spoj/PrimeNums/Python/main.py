

print("Program showing which number from n set is prime number")
print("If number is prime, it prints Yes next to it, otherwise it prints No")

print("------------------------------")
try:
    n_amount = int(input("Please, write size of set"))
    i = 0
    while (i <= n_amount):
        if(i%2 == 0):
            print("{} - NO".format(i))
        if(i%2 != 0):
            print("{} - YES".format(i))
        i = i + 1
except TypeError:
    print("Wrong size format!")