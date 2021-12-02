# Q1 - Review

# A
# How to declare that class B is a subclass of class A?

"""
By enclosing B in a pair of parentheses.

Follow-up question:
Try to give a very short (but complete) example
to demonstrate the point.
Do this for the questions below as well.
"""

# B
# How to call a method in the superclass?

"""
By using the super function.
"""



# C

# Class A has attribute x and a constructor to initialize x.
# B is a subclass of A. It has extra attribute y, and a
# constructor to initialize x and y.
#
# Write definitions of classes A and B.

"""
Very often, we use function super in the constructor
of a subclass to call the constructor in the super class.
"""

    

# D
# What is polymorphism?

"""
Polymorphism is the ability of a function call to different
version of a method, depending on the type of the object
involved.
"""



# D
# Meaning of   type(x) is C?
# Meaning of   isinstance(x, C)?

"""
type(x, C) is True IF
    x is an instance of C

isinstance(x, C) is True IF
    x is an instance of C OR
    x is an instance of a subclass of C
"""


