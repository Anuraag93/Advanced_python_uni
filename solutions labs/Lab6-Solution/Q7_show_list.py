# Q7

# A

def show1(stringList):
    for s in stringList:
        print(s)


L = dir(__builtins__)
#show1(L)



# B

def show2(stringList):
    for s in stringList:
        if s[0].islower():
            print(s)

show2(dir(__builtins__))

