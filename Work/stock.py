class Stock:
    '''An instance of a stock holding consisting of name, shares, and price.'''
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        '''Return cost as shares * price.'''
        return self.price * self.shares

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        self._shares = value

    def sell(self, amnt):
        '''Sell a number of shares.'''
        self.shares -= amnt

    def __repr__(self):
        # self.name!r == repr(self.name)
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
