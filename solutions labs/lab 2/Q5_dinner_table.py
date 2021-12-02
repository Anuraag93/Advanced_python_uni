# Question 5
# A program to read (a) number of diner of a group and
# the table size of tables in a hotel (assume all are
# of the same size). The program calculate the number
# of tables to book for the group.


"""
Suppose the table size = 4.
Let n be the number of diners.

If n = 8 => 2 tables
If n = 7 => 2 tables
If n = 9 => 3 tables

    
"""



tableSize = int(input("Enter the table size: "))
nbOfDiners = int(input("Enter the number of diners: "))

nbOfTables = nbOfDiners / tableSize
print("Number of tables to book:", nbOfTables)
