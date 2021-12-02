# a. How do you define a string (string literal) that has one or more single quotes?
#e.g. Walk. Don't run.

s="Walk. Don\'t run."
print (s)


# b How do you define a string that has one or more single quotes and one or more double quotes?
# e.g. The sign says, "Don’t walk!”

s="The sign says, \"Don’t walk!”"
print (s)

#c. How do you define a string that contains two or more lines of text?
# e.g. Walk.
# Keep walking.
# Stop!

s=""" Walk.
Keep walking.
Stop!"""
print (s)


# d. Why does this expression "number " + 9 give a run-time error? How to fix it?
# can not combine string with number 
# we can chnage it into "number " + "9"

#e. How do you test if a string s contains a substring sub?

string ='CSE5APGsub'
if 'sub' in string:
    print('The string contains sub.')

# f. What string function allows you to count how many times a substring sub appears in a string s?

string ='CSE5subAPGsub'
count=string.count("sub")
print (count)

# g. Given a string called name. How to test if the name starts with two underscores?
name="_hello"
if name[0]=="_":
    print ("The string starts with _")


# h. Given a non-empty string. How do you test that it contains only letters?
s=""
if len(s)==0:
    print ("Empy string")
 
 
 # i. Given a string. How to remove all the leading and trailing whitespace characters?
 s=" CSE5APG "
s1=s.strip()
print (s1)


# j. Given a string s. How do you get a string the same as s but with all the lower-case letters converted to upper case?
 s="CSE5APG"
s1=s.lower()
print (s1)



# Question 2 – The First, the Last and the Middle

# Write a program that asks for a string, and then
# • Display the first character
# • Display the last character
#• If the string has an odd number of characters, display the middle character. 
# Otherwise, display the two middle ones (e.g. for beauty, display au).

s="CSE5APG"
l=len(s)
print ("len of s", l)
print (s[0])
print (s[l-1]) 
# print (s[-1])

if l%2!=0:
    mid=int((l)/2)
    print (s[mid])
else:
    mid=int((l)/2)
    print (s[mid-1])
    print (s[mid])
    
# Question 3 – Negative Indexes

#Python allows negative indexes. Given a negative index -n, the equivalent positive index is len(s)-n. For example, the positive index corresponding to -3 is len(s)-3.
#Assume that a string contains two characters or more. Use a negative index to display
#• The last character of s
#• The second last character of s
#• The substring of s, which excludes the first and the last character.

s="Welcome to CSE5APG"
print (s[-1])
print (s[-2])

print (s[1:-1])

#Question 4 – Displaying Phone Number
#Write a program that asks the user for a string of a 10-digit phone number and prints it out in a readable format, as shown in the example below.
#Input: 0394791234
#Output: (03)9479-1234

#s="0394791234"
s=input("enter phone number: ")
s1="("+s[0:2]+")"+s[2:]
print (s1)

#Question 5 – Masking the Characters
#Write a program that asks for a string s of length 4 or more. The program then displays a string that has the first two characters of s and the last character, with each of the characters in between replaced by a star *.
#Sample:
#Input: Strings
#Output: St****s

s="Strings"
l=len(s)-3
s1=""
s1=s[0:2]+"*"*l+s[-1]
print (s1)

#Question 6 – Swapping Dots and Commas
#Write a program that asks for a string s. The program then displays the string s but with all the dots replaced by commas and vice versa.
#Sample: Input: 123,56.78 output: 123.56,78

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































