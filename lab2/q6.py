computers = int(input("number of computers: "))
cable_length = float(input("cable length: ")) 
roll_length = float (input("roll length in metres: "))
total_cable_length = computers * cable_length

rolls = int(total_cable_length / (roll_length*100))
if(total_cable_length % roll_length != 0): rolls += 1
print("Number of rolls needed:", rolls)
