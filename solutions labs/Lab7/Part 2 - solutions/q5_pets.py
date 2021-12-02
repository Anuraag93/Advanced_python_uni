# Q5
#A
# Define class Pet
class Pet:

    def __init__(self, id, name, owner):
        pass

    def getDetails(self):
        return ""

    def __repr__(self):
        return ""

"""
p = Pet("p1", "Little Lamb", "Mary")
"""


# B, C

class Dog(Pet):

    def __init__(self, id, name, owner, size):
        pass

    def getDetails(self):
        return ""

"""
d = Dog("d1", "Snoopy", "Charlie", "medium")
"""

class Cat(Pet):

    def __init__(self, id, name, owner, hairType):
        pass

    def getDetails(self):
        return ""

"""
c = Cat("c1", "Garfield", " Jon", "LH")
"""

class DangerousDog(Dog):

    def __init__(self, id, name, owner, size, incidents = 0):
        pass

    def getDetails(self):
        return ""

"""
dd = DangerousDog("d2", "Buck", "John", "large", 4)
"""

# D, E, F
# (polymorphism and type check)

p1 = Dog("p1", "Buddy", "Bob", "small")
p2 = Cat("p2", "Lucy", "Alice", "SH")
p3 = DangerousDog("p3", "Buster", "Eve", "large", 4)
p4 = Dog("p4", "Oscar", "John", "medium")
p5 = DangerousDog("p5", "Butch", "Paul", "large", 2)

pets = [p1, p2, p3, p4, p5]

print("\nD")
for p in pets:
    print(p)

print("\nE")
for p in pets:
    pass

print("\nF")
count = 0
for p in pets:
    pass
print("count: ", count)

    


