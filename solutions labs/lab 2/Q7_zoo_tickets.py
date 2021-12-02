# Question 5
# Write a program to read numbe of adults, number of
# children. The program calculates an display tickets
# of each kind and the total cost
# adult ticket price = 10
# child ticket price = 5
# family tikect price = 25


# Note 
# +	Addition	x + y	
# -:	Subtraction	x - y	
# *:	Multiplication	x * y	
# /:	Division	x / y	
# %:	Modulus	x % y	
# **:	Exponentiation	x ** y	
# //:	Floor division	x // y




nrOfAdults = int(input("Enter number of adults: "))
nrOfChildren = int(input("Enter number of children: "))

minnrOfAdults=nrOfAdults // 2
minnrOfChildren= nrOfChildren // 2
# nrOfFamilyTickets should be either equal to minnrOfAdults or minnrOfChildren
nrOfFamilyTickets = minnrOfChildren
nrOfAdultTickets = nrOfAdults - 2 * nrOfFamilyTickets
nrOfChildTickets = nrOfChildren - 2 * nrOfFamilyTickets
totalCost = nrOfFamilyTickets * 26 + \
 nrOfAdultTickets * 10 + \
 nrOfChildTickets * 5

print("Number of family tickets:", nrOfFamilyTickets)
print("Number of adult tickets:", nrOfAdultTickets)
print("Number of child ticket:", nrOfChildTickets)
print("Total cost: $" , totalCost)