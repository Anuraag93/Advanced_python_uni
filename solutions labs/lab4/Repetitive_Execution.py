# a. Use for-loop to print Pascal's triangle as follows.
height=5 # height = int(input('Enter height of triangle: '))
row = 0
for row in range (height):
    count = 0
    for count in range(height - row):  
        print(end=' ')
    count = 0
    for count in range (2*row + 1):
        print(row,end='')
    print()




# b.Use for-loop to print table that includes 6 rows and 6 columns where the dignal should be "X".

for i in range(6):
    for j in range (6):
        if i== j:
            print('{0:^3}'.format("X"), end="")
        else:
            print('{0:^3}'.format(i+1), end="")
    print ()




# c. Use for-loop to print lower triangle (dignal) of 5x5 as a '*' pattern as follows:
for i in range(6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()


#d. The code below prints the numbers from 1 to 56. Rewrite the code using a while-loop.
 #   for i in range(1,56): 
 #       print(i)
 
# i=0
# while i <56:
#     print (i)
    
# e. Write a program that uses a while-loop to read a string from user and then print the characters of the string one-by-one on separate lines.
while True:
    s=input("enter string or 0 to stop: ")
    if s=="0":
        break
    i=0
    while i < len (s):
        print (s[i], end="\n")
        i=i+1


#f. Write a program that asks the user for a weight and converts it from kilograms to pounds (pound= kilograms /0.45359237). 
#If the user key in a weight below 0, the program should tell the user that their entry is invalid and then ask the user to enter a new weight. 
#The program should terminate if the user enter -100. [Hint: Use a while loop only, not an if statement].

while True:
    k=float (input("enter kilograms or -100 to stop: "))
    if k==-100:
        break       
    while k > 0:
        pound= k/0.45359237
        print (pound)
        break
    else:
        print ("invalid input -- enter new value")



