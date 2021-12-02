# Q6

def removeDuplicates(receivedList):

    newList = []
    for item in receivedList:
        if item not in newList:
            newList.append(item)
    return newList

# main

list1 = [2, 4, 1, 3, 5, 2, 3]
print("list1:", list1)

# call the function
list2 = removeDuplicates(list1)

# list2 has no duplicates
print("list2:", list2)

# list1 remains the same
print("list1:", list1)

"""
list2: [2, 4, 1, 3, 5]
list1: [2, 4, 1, 3, 5, 2, 3]
"""
