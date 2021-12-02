

# first test case
sales = [
    (1000, True, 1),    # 1000
    (50, False, 4),     # 200
    (100, False, 2)     # 200
    ]


# Other test cases

# sales = [
#     (1000, True, 1),    # 1000
#     (100, False, 2),    # 200
#     (100, False, 2)     # 200
#     ]

# sales = [
#     (1000, False, 1),   # 1000
#     (50, False, 4),     # 200
#     (100, False, 2)     # 200
#     ]


itemSales = 0
petSales = 0
itemCount = 0
petCount = 0

for sale in sales:

    # note the use of assignmnt statement
    price, isPet, quantity = sale

    subtotal = price * quantity
    
    if isPet:
        petSales += subtotal
        petCount += quantity
    else:
        itemSales += subtotal
        itemCount += quantity

totalSales = itemSales + petSales

if petCount > 0 and itemCount >= 5:
    discount = itemSales * 0.20
else:
    discount = 0

amountToPay = totalSales - discount

print("total sales amount:", totalSales)
print("discount amount: ", discount)
print("amount to pay:", amountToPay)



