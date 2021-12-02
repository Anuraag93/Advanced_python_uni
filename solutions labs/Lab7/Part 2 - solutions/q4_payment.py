# Q4

# Define class Payment
"""
Define as usual
"""

# Define class CashPayment
"""
Try to exploit code reuse
"""

# Define class CreditCardPayment
"""
Try to exploit code reuse
"""

# == Tests ===
from misc.q4_ans import Payment, CashPayment, CreditCardPayment

"""
>>> p = Payment(100)
>>> p
>>> p.printDetails()

>>> cp = CashPayment(100)
>>> cp
>>> cp.printDetails()

>>> ccp = CreditCardPayment(100, "ABC123")
>>> ccp
>>> ccp.printDetails()
"""

##p = Payment(100)
##cp = CashPayment(100)
##ccp = CreditCardPayment(100, "ABC123")

p1 = CashPayment(100)
p2 = CreditCardPayment(200, "AB123")
p3 = CashPayment(200)
p4 = CreditCardPayment(100, "CD456")
payments = [p1, p2, p3, p4]

for p in payments:
    print(p)

    
