# Q7

from q6_catalog import Catalog

catalog = Catalog()
def main():
    
    catalog.loadData()

    menu = \
    """
    === Catalog Menu ===
    1. Add a product
    2. Change a product's Price
    3. Remove a product
    4. Display products
    Q. Quit
    """
    
    while True:
 
        print(menu)
        option = input("Enter an option (1-5, Q): ")
        option = option.strip().upper()

        if option == "1":
            doAddProduct()

        elif option == "2":
            doChangeProductPrice()

        elif option == "3":
            doRemoveProduct()

        elif option == "4":
            print(catalog)
            
        elif option == "Q":
            break

        else:
            print("Invalid option")

    catalog.saveData()

def doAddProduct():
    id = input("Enter the product's id: ").strip()
    name = input("Enter the product's name: ").strip()
    price = float(input("Enter the price: "))
    catalog.addProduct(id, name, price)

def doChangeProductPrice():
    id = input("Enter the product's id: ").strip()
    price = float(input("Enter the new price: "))
    catalog.changeProductPrice(id, price)

def doRemoveProduct():
    id = input("Enter the product's id: ").strip()
    catalog.removeProduct(id)
 

main()
