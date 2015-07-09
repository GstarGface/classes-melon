"""This file should have our melon-type classes in it."""
class Melons(object):
    base_price = 5.0 #make sure this is a float! 


class WatermelonOrder(Melons):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    

    # def __init__(self, base_price=6.0):
    #     self.get_base_price = base_price


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3: 
            total = self.base_price * float(qty) * 0.75
        else:
            total = qty * self.base_price 

        print total # ultimately, we'd like to add a $ here...


class CantaloupeOrder(Melons):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 5: 
            total = self.base_price * float(qty) * 0.5
        else:
            total = float(qty) * self.base_price 

        print total # ultimately, we'd like to add a $ here...



class CasabaOrder(Melons):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall' 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = (self.base_price + 1) * float(qty) * 1.5
        

        print total # ultimately, we'd like to add a $ here...

   

class SharlynOrder(Melons):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = self.base_price * float(qty) * 1.5
        

        print total # ultimately, we'd like to add a $ here...


class SantaClausOrder(Melons):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = self.base_price * float(qty) * 1.5
        

        print total # ultimately, we'd like to add a $ here...


class ChristmasOrder(Melons):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = self.base_price * float(qty) 
        

        print total # ultimately, we'd like to add a $ here...

class HorneMelonOrder(Melons):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = self.base_price * float(qty) * 1.5
        

        print total # ultimately, we'd like to add a $ here...

class XiguaOrder(Melons):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = self.base_price * float(qty) * 1.5 * 2.0
        

        print total # ultimately, we'd like to add a $ here...

# order2 = XiguaOrder()
# order2.get_price(1)

class OgenOrder(Melons):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

    
        total = (self.base_price + 1) * float(qty)
        

        print total # ultimately, we'd like to add a $ here...
