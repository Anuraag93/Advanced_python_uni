# Q11

# Reads 'prescribed or not', 'used before or not', and
# number of students
# Calculates and prints 'how mny books to order'

"""
prescribed + new: 90% will buy
prescribed + not new: 65%
not prescribed + new: 40%
not precribed + not new: 20%
"""

prescribed = True
new = True
nbOfStudents = 100

if prescribed:
    if new:
        rate = 0.90
    else:
        rate = 0.65
else:
    if new:
        rate = 0.40
    else:
        rate = 0.20

order = nbOfStudents * rate
print(order, "copies")

"""
Here is how we can get the inputs from the use:

userInput = input("prescribed? (y,n): ")
prescribed = userInput == "y"
"""
        



