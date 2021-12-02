'''
required + new = 90%
required + used = 65%
not required + new = 40%
not required + used = 20%
'''

numOfStudents = 100
required = False
new = True

if required:
    if new:
        percentage  = 0.90
    else:
        percentage = 0.65
else:
    if new:
        percentage  = 0.40
    else:
        percentage = 0.20

booksToBeOrdered = percentage * numOfStudents

print(booksToBeOrdered)
