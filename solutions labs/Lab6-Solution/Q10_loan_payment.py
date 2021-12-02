# Q10

def getPayment(loanAmount, rate, months):

    payment = amount * rate / (1 - (1 - rate)**months)
    return payment


amount = 5000
rate = 0.05

# If pay in 1 year,
# How much to pay per month if pay in 1 year
# Total payment?

months = 12
payment = getPayment(amount, rate, months)
total = payment * months
print(payment, total, "\n")

# If pay in 2 years,
# How much to pay per month if pay in 1 year
# Total payment?

months = 2 * 12
payment = getPayment(amount, rate, months)
total = payment * months
print(payment, total, "\n")

# If pay in 3 years,
# How much to pay per month if pay in 1 year
# Total payment?

months = 3 * 12
payment = getPayment(amount, rate, months)
total = payment * months
print(payment, total, "\n")
