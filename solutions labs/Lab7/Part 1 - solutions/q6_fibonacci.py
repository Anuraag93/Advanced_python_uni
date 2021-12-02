# Q8

# In this question, we consider the Fibonacci problem,
# but we do it from the object-oriented viewpoint.
# We define a class which represents a colony of rabbits.
# The population growth of this colony follows the
# terms of the Fibonacci sequence

class Colony:

    def __init__(self):
        self.month = 1
        self.newborn = 1
        self.oneMonth = 0
        self.mature = 0

    def __repr__(self):
        return "Colony<month: " + str(self.month) +          \
               ", newborn: " + str(self.newborn) +      \
               ", oneMonth: " + str(self.oneMonth) +    \
               ", mature: " + str(self.mature) + ">"


    def next(self):
        pre_newborn = self.newborn
        pre_oneMonth = self.oneMonth
        pre_mature = self.mature
        
        self.month += 1
        self.newborn = pre_oneMonth + pre_mature
        self.oneMonth = pre_newborn
        self.mature = pre_oneMonth + pre_mature

    def pop(self):
        return self.newborn + self.oneMonth + self.mature
        

# Basic tests
"""
Create a colony
Display it
Apply method 'next' to it a few times and inspect to see
how the state changes
"""

# Display Fibonacci sequences
"""
Print population of the first month (stay on the line)
Repeat 14 times:
    Apply method 'next'
    Print the population (stay on the line)

OR: slight variation below
"""

c = Colony()
print(c.pop(), end=" ")

for _ in range(14):   # repeat 14 times
    c.next()
    print(c.pop(), end=" ")
