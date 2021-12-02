# Q6

# In this question, we complete the defintion of class Catalog.
# We do so by adding 2 methods: to save and load data.
# This program can and will be used as a module in
# the menu-driven program for Question7

from q1_product import Product

class Catalog:

    def __init__(self):
        self.productList = []

    def __repr__(self):
        outstring = "catalog:\n"
        for p in self.productList:
            outstring +=  str(p) + "\n"
        return outstring

    def search(self, id):
        for p in self.productList:
            if p.id == id:
                return p
        return None

    def addProduct(self, id, name, price):
        product = self.search(id)

        pre = product == None
        if not pre:
            return
        product = Product(id, name, price)
        self.productList.append(product)

    def changeProductPrice(self, id, price):
        product = self.search(id)
        pre = product != None
        if not pre:
            return
        product.setPrice(price)
        
    def removeProduct(self, id):
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
        pass


    def saveData(self):
        """
        Open the outfile catalog.txt for writing
        for each product in the product list:
            write id, name, price -- separated by semi-colons
        Close the file
        """

        outfile = open("catalog.txt", "w")
        for p in self.productList:
            outfile.write(str(p.id) + ";" + 
                str(p.name) + ";" + str(p.price) + "\n")
        outfile.close()

    def loadData(self):
        """
        Open the file for reading
        Let the attribute productList be an empty list
        Repeat this for each line of the file:
            read a line of the file
            split the line into tokens
            extract id, name and price
            create the product with those values
            append to the product list
        Close the file
        """
        infile = open("catalog.txt")
        self.productList = []
        while True:
            line = infile.readline().strip()
            if line == "":
                break
            tokens = line.split(";")
            id = tokens[0].strip()
            name = tokens[1].strip()
            price = float(tokens[2].strip())
            product = Product(id, name, price)
            self.productList.append(product)
        infile.close()

        

