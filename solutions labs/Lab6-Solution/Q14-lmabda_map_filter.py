##Lambda

# write a  lambda function to calculate the cube of a given number
f = lambda x: x*x*x 
r=f(5)
print (r)

# write a  lambda function to calculate the power of a given number
f2=lambda x: x **2
r1=f2(5)
print (r1)


##Map
# write a map() function to calculate the square root for list of elements, e.g l=[4,6,9,12,15,25]
def fun_Square(x):
    return x*x
l=[4,6,9,12,15,25]
s_l= map(fun_Square, l)

# Can we use Lambda with Map to calculate the square root? 
s_l = map(lambda x: x*x, l)


#Filter

# Write a filter function to remove 'a' letter from the given list. l=['a','b','c','d','a','e','f,'a']

def Romove_a(l):
    if(l =='a'):
        return False		
    else:
        return True
l=['a','b','c','d','a','e','f,'a']
N_l = filter(Romove_a, l)