# Q8







def adjust(amount):
    """
    This functions takes an 'amount' of 0, 1, 2, up to 9,
    and returns 0 or 5 or 10
    """
    if amount==0 or amount==1 or amount==2:
        return 0
    elif amount==5 or amount==3 or  amount==4 or amount==6 or amount==7:
        return 5
    else:
        if amount==8 or amount==9:
            return 10
    
    

# tests
#for n in range(0, 10):
 #   print(n, adjust(n))
    
# B

def roundOff(amountInDollars):
    
    """
    Convert the ammount in dollars into amount in cents.
    Get the last digits.
    Convert the last digit to 0 or 5 or 10
    Calculate the rounded-off amount in cents
    Calculate the rounded-off amount in dollars
    """
    
    n = str(amountInDollars)
    amountInDollars=float(amountInDollars)
    last_digits= int(n[len(n)-1])
    NewamountInDollars=0
    #print ("last_digits", last_digits)
    last=adjust(last_digits)
    if last==0 or last==1 or last==2:
        NewamountInDollars=n[:len(n)-1]+"0"        
    elif last==3 or last==4 or last==5 or last==6 or last==7:
        NewamountInDollars=n[:len(n)-1]+"5"
    
    else:       
        last2=int (n[len(n)-2:])
        last2=round(last2/10)*10 # Round Number to Nearest 10 using round()
        NewamountInDollars=n[:len(n)-2]+str(last2)
        

    return NewamountInDollars
    

# we can use a list like this for test cases
cases = [123.40, 123.41, 123.42, 123.43, 123.44, 123.45,  123.46, 123.47, 123.48, 123.49, 123.50]

for each in cases:
    kk="{:.2f}".format(each)
    print (each, " ", roundOff(kk))


"""
Format your output to look like this:

123.41 123.40
123.42 123.40
123.43 123.45
123.44 123.45
123.45 123.45
123.46 123.45
123.47 123.45
123.48 123.50
123.49 123.50
123.50 123.50
"""
