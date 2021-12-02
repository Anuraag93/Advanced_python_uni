# Q10

# Reads name, hours worked, pay rate, total sales
# bonus at 10% of (total sales - hours * 100) if +ve

# (Let us omit name. It is irrelevant to the aim of
# question)

hours = 20.0
rate = 15.45
sales = 4600.90

hours = 10.0
rate = 20.00
sales = 3000.00

if sales > hours * 100:
    bonus = 0.10 * (sales - hours * 100)
else:
    bonus = 0

pay = hours * rate + bonus

print("pay", pay)
