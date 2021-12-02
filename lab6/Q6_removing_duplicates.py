def removeDuplicates(receivedList):
    newlist = receivedList
    # for l in receivedList:
    #     if l not in newlist:
    #         newlist.append(l)
    return list(set(newlist))

# main 
list1 = [2, 4, 1, 3, 5, 2, 3] 
print("‘list1:’", list1) 
# call the function 
list2 = removeDuplicates(list1) 
print("‘list2:’", list2) 
print("‘list1:’", list1) 
# list2 has no duplicates print("list2:", list2) 
# # list1 remains the same print("list1:", list1)