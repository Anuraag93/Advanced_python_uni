def takeInput(num):
   return int(input("Enter {} integer ".format(num))) 
x,y,z =0,0,0
while True:
    if x<=0:
        x = takeInput("First")
        if x<=0: continue
    if y<=0:
        y = takeInput("Second")
        if y<=0: continue
    if z<=0:
        z = takeInput("Third")
        if z<=0: continue
    break

print(x,y,z)
# x= int(input("Enter 1st integer "))
# y= int(input("Enter 2nd integer "))
# z= int(input("Enter 3rd integer "))
# x,y,z = 10, 20, 15
# x,y,z = 10, 20, 5
# x,y,z = 10, 20, 10


maxSide = 0
maxSide = x if x >=y else y

if z > maxSide: 
    maxSide = z 

sum = x +y +z - maxSide

if maxSide < sum:
    print("This is a triangle")
else:
    print("this is not a triangle")
