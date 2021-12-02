# Q9

# A

def getBalance(amount, rate, months):
    """
    'rate': monthly interest rate as decimal number
    """
    balance = amount * (1 + rate) ** months
    return balance

# B

amount = 1000
rate1 = 0.02
rate2 = 0.05
rate3 = 0.1

print("Initial amount:", amount, "\n")
#print("rates to compare:", rate1, rate2, rate3)

print("{:5s} {:>10s} {:>10s} {:>10s}\n".format(
    "month", "2%", "5%", "10%"))

for month in range(1, 12 + 1):
    print("{:5d} {:10.2f} {:10.2f} {:10.2f}".format(
          month,
          getBalance(amount, rate1, month),
          getBalance(amount, rate2, month),
          getBalance(amount, rate3, month)))
