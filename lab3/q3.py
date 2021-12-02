# x= int(input("Enter 1st integer "))
# y= int(input("Enter 2nd integer "))
# z= int(input("Enter 3rd integer "))
x,y,z = 2,9,2

print(x,y,z)
if x>y :
    x,y = y,x
if x>z: 
    x,z = z,x
if y>z:
    y,z = z,y
    
print(x,y,z)