# Q5

# Inthis question, we define class Catalog.
# This is a class that manages a COLLECTION of products.
# The products are instances of class Product defined
# in question 1 (Notice how we import the Product class)

# attribute: list of products
# __init__
# __repr__

# search

# add
# change price
# remove

# search by name

from q1_product import Product

class Catalog:

    def __init__(self):
        """
        This class has attribute to hold a list of products.
        Let us call it 'productList'.
        Initially the list is empty.
        """
        self.productList = []
        

    def __repr__(self):
        """
        This method returns a string that contains details
        of all products in the list.
        Try to display each product on a separate line.
        """
        # return "Catalog<" + str(self.productList) + ">"
        outstring = "Catalog:\n"
        for p in self.productList:
            outstring += str(p) + "\n"
        return outstring
        

    def search(self, id):
        """
        This method searches the list of products for the
        product that matches the specified id exactly.
        If the product is found, it returns the product
        (i.e. the Product object)
        Otherwise, it returns None (an object of NoneType)
        """
        
        for p in self.productList:
            if p.id == id:
                return p

        return None
    

    def addProduct(self, id, name, price):

        """
        This method must search for a product with the
        given id. If a product is found, it means we have
        a duplicate id, and the method should return
        without adding a product (alternatively, we can raise
        an exception, but we are not going down that path).

        The there is no duplicate id, create the product
        and append it to the list.
        """
        product = self.search(id)
        
        pre = product == None   # The pre condition specifies
                                # what we want to be true for
                                # this function to proceed.,
                                # namely the product with the
                                # given id does not exist
        
        if not pre:             # if the pre condition is not
            return              # satisfied,we will not go on.
                                # A simple response is to eturn.
                                # A better response is to raise
                                # an exception 
        
        product = Product(id, name, price)  # If we reach this
        self.productList.append(product)    # statement, then the
                                            # precondition is
                                            # satisfied. So we create
                                            # a product and add it
                                            # to the list.
                
    def changeProductPrice(self, id, price):

        """
        Search for the product first.
        If not found, return straight away.
        Otherwise, change the price of the found product.
        """
        product = self.search(id)
        pre = product != None
        if not pre:
            return

        product.setPrice(price)
        
    def removeProduct(self, id):
        """
        Search for the product first.
        If not found, return straight away.
        Otherwise, remove the found product.
        """
        product = self.search(id)
        
        pre = product != None
        
        if not pre:
            return
        
        self.productList.remove(product)
        

    def searchByName(self, key):
        """
        Return the list of products whose names
        contains 'key' as a substring.
        """
        
        outlist = []
        
        for p in self.productList:
            if key in p.name:
                outlist.append(p)
        return outlist

# == Tests ==
##"""
##Create a Catalog object
##Add a few products(and display the catalog for inspection)
##Add a product with duplicate id
##"""
##
cat = Catalog()
cat.addProduct("p1", "table", 10)
cat.addProduct("p2", "chair", 20)
cat.addProduct("p3", "desk", 30)
##
##"""
##Change the price of a few poducts
##Change the price of a non-existent product
##"""

cat.changeProductPrice("p1", 20)
print(cat)

##
##"""
##Remove a product
##Remove a non-existent product
##"""
cat.removeProduct("p2")
print(cat)

##
##"""
##Make a few search by name with different keywords (search words)
##including one that returns an empty list
##"""
##cat.searchByName("ab")
##cat.searchByName("a")




