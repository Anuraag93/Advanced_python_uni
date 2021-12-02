s="123,56.78"
s1=""
for i in s:
    if i==",":
        s1=s1+"."
    elif i==".":
        s1=s1+","
    else:
        s1=s1+i
        
print (s1)