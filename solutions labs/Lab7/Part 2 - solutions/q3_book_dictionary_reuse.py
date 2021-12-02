# Q2

# Start with this class
# which has the normal style of coding

class Book:

    def __init__(self, title, nrPages):
        self.title = title
        self.nrPages = nrPages

    def __repr__(self):
        return "Book<: " + \
                "title:" + str(self.title) + \
                ", nrPages: " + str(self.nrPages) + ">"

"""
Test:
>>> b = Book("The Arts of Programming", 150)
>>> b
Book<: title:The Arts of Programming, nrPages: 150>
"""

# Here is a new version
# Note the differences

##class Book:
##
##    def __init__(self, title, nrPages):
##        self.title = title
##        self.nrPages = nrPages
##
##    def getDetails(self):
##        return "title: " + str(self.title) + \
##               ", nrPages: " + str(self.nrPages)
##
##    def __repr__(self):
##        return self.__class__.__name__ + \
##               "<" + self.getDetails() + ">"
"""
Test:
>>> b = Book("The Arts of Programming", 150)
>>> b.getDetails()
'title: The Arts of Programming, nrPages: 150'
>>> b
Book<title: The Arts of Programming, nrPages: 150>
"""


# define class Dictionary

class Dictionary(Book):

   def __init__(self, title, nrPages, nrEntries):
       super().__init__(title, nrPages)
       self.nrEntries = nrEntries

   def getDetails(self):
       return \
           super().getDetails() + \
           ", nrEntries: " + str(self.nrEntries)

   # Inherit __repr__ from superclass
        
"""
Test:
>>> d = Dictionary("Essential English Dictionary", 200, 30000)
>>> d.getDetails()
'title: Essential English Dictionary, nrPages: 200, nrEntries: 30000'
>>> d
Dictionary<title: Essential English Dictionary, nrPages: 200, nrEntries: 30000>
"""
