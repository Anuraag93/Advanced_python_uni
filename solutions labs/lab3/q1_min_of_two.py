"""
Q1
Reads three numbers, prints the minimum 
"""

"""
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
"""

n1, n2 = 10, 20

##n1, n2 = 20, 10
##n1, n2 = 10, 10
##n1, n2 = "hello", "good bye"

if n1 <= n2:
    minn = n1
else:
    minn = n2
    
print("min:", minn)

