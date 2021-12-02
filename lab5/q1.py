# A 1

l = list(range(2, 101))
# print(l)
    
#A 2
l1 = [0] *100
# print(l1)

#b 
# append -> add new item at the end of the list 
# insert is add item at the given index

# c 
'''
removes: takes in element to remove, 
pop: takes in index to remove 
both raise exception
'''
# d
even = []
lst = [1,2,5,6,8]
for i in lst:
    if i%2 == 0:
        even.append(i)
    
# print(even)
# e

lst = [1,2,5,6,8]
for i in range(len(lst)):
    lst[i]=lst[i]*2
# print(lst)

#f

a = [4, 3,  -1, -2, 1, 2]
print(a)
a.sort(key = abs)
print(a)
