# Q1
# Reads three numbers, prints the maximum

##n1 = int(input("Enter the first number: "))
##n2 = int(input("Enter the second number: "))
##n3 = int(input("Enter the third number: "))

n1, n2, n3 = 10, 20, 30
n1, n2, n3 = 10, 30, 20
n1, n2, n3 = 30, 10, 20
n1, n2, n3 = "hello", "good bye", "hi"

if n1 >= n2:
    max = n1
else:
    max = n2

if n3 > max:
    max = n3
    
print(n1, n2, n3, sep="/")
print("max:", max)

