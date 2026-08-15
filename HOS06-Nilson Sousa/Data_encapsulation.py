# Computer class that demonstrates data encapsulation using name mangling
# to create private attributes that cannot be easily accessed from outside
class Computer:

    # __init__ is the constructor that initializes a Computer object
    # It sets the private attribute __maxprice to a default value of 900
    # The double underscore prefix makes this attribute "private" through name mangling
    def __init__(self):
        # __maxprice uses double underscore (name mangling) to simulate a private attribute
        # This prevents direct access from outside the class and protects the data
        # Python will internally rename it to _Computer__maxprice
        self.__maxprice = 900

    # sell() displays the current maximum price of the computer
    # This is a public method that allows controlled access to the private __maxprice attribute
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # setMaxPrice() is a setter function that allows controlled modification of the private __maxprice attribute
    # This is the proper way to change the price, protecting the data encapsulation
    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
