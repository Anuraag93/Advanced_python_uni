# Question 6


nrOfComputers = 35          # number of computers (int)
cableLength = 30            # cable length in cms (float)
rollLengthInMetres = 5      # roll length in metres (float)

rollLength = rollLengthInMetres * 100
nrOfComputersPerRoll = rollLength / cableLength
nrOfRolls = (nrOfComputers / nrOfComputersPerRoll)
print("Number of rolls needed:", nrOfRolls)


"""
In the above program, replace
    nrOfComputers = 35          
    cableLength = 30            
    rollLengthInMetres = 5

by
    nrOfComputers = int(input("Enter number of computers: "))
    cableLength = float(input("Enter the cable length: "))
    rollLength = float(input("Enter the roll length: "))
"""

