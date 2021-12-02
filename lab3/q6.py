# x= int(input("Enter 1st integer "))
# y= int(input("Enter 2nd integer "))
# z= int(input("Enter 3rd integer "))
x,y,z = 10, 20, 15
x,y,z = 10, 20, 5
x,y,z = 10, 20, 10


# if x+y > z and x+z >y and y+z > x :
#     print("This is a triangle")
# else:
#     print("this is not a triangle")

maxSide = 0
maxSide = x if x >=y else y

if z > maxSide: 
    maxSide = z 

sum = x +y +z - maxSide

if maxSide < sum:
    print("This is a triangle")
else:
    print("this is not a triangle")
