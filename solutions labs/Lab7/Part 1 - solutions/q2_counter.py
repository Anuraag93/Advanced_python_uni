# Q2

# Define class Counter (to model a sheep counter)
#   attribute: count
#   methods:   __init__
#              __repr__
#              click
#              clear

class Counter:

    MAX_COUNT = 10  # This is a class-own attribute
                    # Access this clas-own attribute
                    # as Counter.MAX_COUNT (see method
                    #'click' below
    
    def __init__(self):
        self.count = 0
        
    def __repr__(self):
        return "Counter<" + \
               ", count: " + str(self.count) + ">"

    def click(self):
        self.count += 1
        if self.count > Counter.MAX_COUNT:
            self.count = 0
            
    def clear(self):
        self.count = 0
        
# Basic tests
# make up tests to do the following:
"""
Test constructor
Display object
Display attributes
Test set methods
"""

# Test that 'count' wraps around from MAX_COUNT to 0
# Set MAX_COUNT to 10 for easy testing

c = Counter()
for _ in range(15):
    c.click()
    print(c)


