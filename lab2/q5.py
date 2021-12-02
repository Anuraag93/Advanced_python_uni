table_size = int(input("Enter the table size: "))
diners = int(input("Enter the number of diners: " ))

tables = int(diners/table_size)

if(diners % table_size != 0): tables += 1

print("Number of tables to book:  ", tables) 