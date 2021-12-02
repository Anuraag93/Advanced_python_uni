# Q10 - OPTIONAL

# In this question, we define a version of class Product
# that prevents misuses.

# To do that, we start with the previous class definition.
# Then we
# (1) Change attributes into privates one
# (2) Add assert statement one by one

# Note on testing:
# As soon as we add a new feature, we should test it straight
# away.
# For example, after making the attributes private,
# we should test to verify that we can no longer access the
# attributes directly.
# As soon as we add an assertion, test it to verify that
# the class rejects invalid requests.

class Product:

    def __init__(self, id, name, price):

        assert type(id) is str and len(id) > 0,      \
               "id is not valid: " + str(id)

        assert type(name) is str and len(name) > 0,      \
               "name is not valid: " + str(id)

        assert (type(price) is float or \
               type(price) is int) and  \
                price > 0,  \
               "price is invalid: " + str(price)
                   
        """
        Initialize attributes. Make them private
        """
        self.__id = id
        self.__name = name
        self.__price = price
        

    def __repr__(self):
        """
        Return string containg products' details
        """
        return "Product<" +                     \
                "id: " + str(self.__id) +          \
                ", name: " + str(self.__name) +   \
                ", price:" + str(self.__price) + ">"
        
    
    def setPrice(self, price):

        """
        assert the type and value for 'price'
        Set attribute 'price'
        """
        self.__price = price
        

    def getId(self):
        return self.__id
    
    def getName(self):
        pass

    def getPrice(self):
        pass


# == tests ==

"""
Test the valid use of the constructor

Test the invalid use. Use try/except
Try different error of type and error of value
"""

"""
Test valid use of setPrice
Test invalid use. Alos, use try/except
Try error of type and error of value
"""

"""
Test that we cannot access attributes directly.
We have to do this through get methods.
"""



