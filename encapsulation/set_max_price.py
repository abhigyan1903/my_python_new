#making a class with a private variable and trying tryibng various waysd to access it
class shop_sell:
    def __init__(self):
        self.__maxprice=20000
    def sell(self):
        print("The price is:",self.__maxprice)
    def set_max_price(self,max_price):
        self.__maxprice=max_price
        
stock=shop_sell()
stock.sell()
stock.set_max_price(300000)
stock.sell()
stock.__maxprice=1200000
stock.sell()