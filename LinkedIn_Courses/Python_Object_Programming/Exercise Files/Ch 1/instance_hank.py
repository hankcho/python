# using instance methods and attributes

# a basic class
class Book:
    # the "init" function is called when the instance is created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price 
        self.__secret = "this is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def setdiscount(self, amount):
        self._discount = amount 
    
    # we're not committed to creating attributes just within in the init function
    # we can create them in a separate function within the object
    # naming the attribute with an underscore is to let others know that this should not be accessed from outside the class' logic


# TODO: create some book instances
b1 = Book("Brave New World", "Leo Tolstoy", 1223, 39.95)
b2 = Book("War on Peace", "JD Salinger", 234, 29.95)


# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())


# TODO: properties with double underscores are hidden by the interpretter
print(b2._Book__secret)