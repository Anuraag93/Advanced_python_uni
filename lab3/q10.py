hours = 20
rate = 15.45
totalSales = 4600.90

hours = 10.0
rate = 20.00
totalSales = 3000.00

bonus = 0
if totalSales > hours * 100:
    bonus = (totalSales - hours * 100) * 0.1
pay = hours * rate  + bonus
print("excess = ", (totalSales - 20 * 100))
print("bonus = ", bonus)
print("pay = ", pay)

