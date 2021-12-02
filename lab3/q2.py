x= int(input("Enter 1st integer "))
y= int(input("Enter 2nd integer "))
z= int(input("Enter 3rd integer "))
max = 0
if x>y and x>z:
    max = x 
elif y>z:
    max = y 
else: 
    max = z
print(max)