# Q4

# In function 'chat', what kind of variable is 'myName'?

def chat(msg):
    print(myName, "writes:")   # line 2
    print(msg)
    print()

# call
myName = "Bob"
message = \
    """
    Hello, Everyone!
    Keep in touch.
    """

chat(message)

# Answer: 'myName' is a global variable.
# It is defined outside the function
