w=-1
while w != -100:
    if w < 0:
        print("the entry is invalid")
        w = int(input("Enter the weight "))
    else:
        p = w/0.45359237
        print("weight in pounds is ",p)
        break