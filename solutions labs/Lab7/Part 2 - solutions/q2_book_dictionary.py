# Q2

# Start with this class

class Book:

    def __init__(self, title, nrPages):
        self.title = title
        self.nrPages = nrPages

    def __repr__(self):
        return "Book<: " + \
                "title:" + str(self.title) + \
                ", nrPages: " + str(self.nrPages) + ">"

"""
Try some basic tests, e.g.
>>> b = Book("The Arts of Programming", 150)
>>> b
Book<: title:The Arts of Programming, nrPages: 150>
"""

# Define class Dictionary
# which has additional attribute 'nrEntries'

#define class Dictionary

class Dictionary(Book):

   def __init__(self, title, nrPages, nrEntries):
       super().__init__(title, nrPages)
       self.nrEntries = nrEntries

   def getDetails(self):
       return \
           super().getDetails() + \
           ", nrEntries: " + str(self.nrEntries)
"""
Declare Dictionary is a subclass of Book.
In the constructor, call constructor of the superclass.
__repr__ is coded as usual.

Tests:
>>> d = Dictionary("Essential English Dictionary", 200, 30000)
>>> d.getDetails()
'title: Essential English Dictionary, nrPages: 200, nrEntries: 30000'
>>> d
Dictionary<title: Essential English Dictionary, nrPages: 200, nrEntries: 30000>
"""
