adults = int(input("Number of adults: "))
children = int(input("Number of children: "))

a = int (adults/2)
b = int (children/2)

tickets_family = a if a<b else b

tickets_adult = adults - (tickets_family*2)
tickets_child = children - (tickets_family*2)

cost = tickets_adult * 10 + tickets_child * 5 + tickets_family * 26

print("Number of family tickets: ",tickets_family)
print("Number of adult tickets: ",tickets_adult)
print("Number of child tickets: ",tickets_child)
print("Total cost: $",cost)
