from typedproperty import typedproperty

class Stock:
    '''An instance of a stock holding consisting of name, shares, and price.'''
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        '''Return cost as shares * price.'''
        return self.price * self.shares

    def sell(self, amnt):
        '''Sell a number of shares.'''
        self.shares -= amnt

    def __repr__(self):
        # self.name!r == repr(self.name)
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
