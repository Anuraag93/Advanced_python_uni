lst = [1,2,3,4,5,6,7,8]
def move_even_front(a):
    even = []
    odd = []
    for element in a:
        if element % 2 == 0:
           even.append(element)
        else:
            odd.append(element)

    return even+odd

print(move_even_front(lst))