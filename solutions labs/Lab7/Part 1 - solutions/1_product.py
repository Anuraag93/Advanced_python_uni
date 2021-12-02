# Q1
# Define class product

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def setPrice(self, price):
        self.price = price

    def __repr__(self):
        return "Product<" +                     \
                "id " + str(self.id) +          \
                ", name: " + str(self.name) +   \
                ", price:" + str(self.price) + ">"

# == test ==

p = Product("P1", "table", 40)   # create object

print("p:", p)      # display object

print(p.id)         # access and displat attributes
print(p.name)
print(p.price)

newPrice = p.price * 1.10   # test set methods
p.setPrice(newPrice)
print("p:", p)


