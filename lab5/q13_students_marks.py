# Q13

data = {
    "Alex": 70, 
    "Adam": 80,
    "Andy": 90,
    "Ash": 100,
    "Bruce": 90,
    "Brendan": 80,
    "Baker": 70,
    "Bryan": 100,
    "Anton": 90,
    "Allen": 80,
    "Albert":70,
    "Ben":70,
    "Brian": 80,
    "Bowen": 90,
    "Benson": 100,
    }

# A: display the data (students and their marks)
print("A:")
for k in data:
    print(k, data[k])


# B: add a student
print("B:")
data["William"] = 80
print(data) # Note that william has been added

# C: remove a student
print("C")
data.pop("William")
print(data) # Note that william has been removed

# D: change mark of a student
print("D")
data["Benson"] = 98
print(data) # Note that Benson mark has been changed

# E: get a list of tuples (student, mark)
print("E")
pairs = list(data.items())
print(pairs)

# F: sort by mark in decreasing order,
#    in groups of equal marks, sort by name


print("F")
dataList = list(data.items())
dataList.sort(key = )
dataList.sort(key = , reverse = True)
for e in dataList:
    print(e)




