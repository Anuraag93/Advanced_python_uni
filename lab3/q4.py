# x= int(input("Enter 1st integer "))
# y= int(input("Enter 2nd integer "))
# z= int(input("Enter 3rd integer "))

x,y,z = 3,4,5
x,y,z = 3,4,4
x,y,z = 3,2,1




if y>x and z>y:
    print("strictly increasing")
elif x>y and y>z:
    print("strictly decreasing")
else: 
    print("neither")
        