# Q11

# A

def readInt(low, high):
    keepReading = True
    while keepReading:
        userInput = input( "Enter integer between {} and {}: "
                   .format(low, high))
        n = int(userInput)
        
        if low <= n <= high:
            keepReading = False  # to terminate the loop
    return n

# B

name = input("Enter the name:  ")
mark = readInt(0, 100)
print("name:", name, "mark:", mark)


"""
Enter the name:  Bob
Enter integer between 0 and 100: -10
Enter integer between 0 and 100: 110
Enter integer between 0 and 100: 80
name: Bob mark: 80
"""
