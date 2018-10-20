def ReverseInput(inp):
    temp = ''
    for i in range(-len(inp),0):
        temp += inp[i+1]
    print(temp)

ReverseInput("Hello")

