# (Price, isPet, quantity)
p1 = [
    (550, True, 1),
    (10.50, False, 4)
]
sales = [
    (1000, True, 1),    # 1000
    (50, False, 4),     # 200
    (100, False, 2)     # 200
]
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

def pet_shop(tuple_list):
    total_cost = 0
    discount = 0
    cost_after = 0
    pet_count = 0
    item_count = 0
    for t in tuple_list:
        print(t)
        cost = t[0] * t[2]
        dis = 0
        # calculate discount if not pet
        if t[1]:
            pet_count += t[2]
        else:
            # calculate 20% of the items cost and deduct from total cost
            item_count += t[2]
            dis = cost * 0.2
        discount += dis
        total_cost += cost
    if pet_count < 1 or item_count < 5:
        discount = 0

    cost_after += total_cost-discount

    print("cost before discount", total_cost)
    print("discount amount", discount)
    print("the cost after discount", cost_after)


# pet_shop(p1)
pet_shop(sales)
