"""
0 is Mondy, 1 is Tuesday, ect.
"""

# A

def printCalendar(nbOfDays, firstDay):
    """
    nbOfDays: number of days in the mont, e.g. 30
    firstDay: day of week of the first day, e.g 2 (Wednesday)
    """
                  
    print(" Mon Tue Wed Thu Fri Sat Sun")
    skip = "    " * (firstDay)
    print(skip, end = "")
    
    pos = first

    for day in range(1, nbOfDays + 1):
        print(format(day, "4d"), sep = "", end = "")
        pos = pos + 1
        if pos % 7 == 0:
            print()

# B

days = 31
first = 2 # Wed
printCalendar(days, first)

"""
 Mon Tue Wed Thu Fri Sat Sun
           1   2   3   4   5
   6   7   8   9  10  11  12
  13  14  15  16  17  18  19
  20  21  22  23  24  25  26
  27  28  29  30  31
"""
  
