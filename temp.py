class stock:
    m=90
    def __init__(self,name):
        self.name=name
        print('stockname :', self.name)
    def openingprice(self,price):
        self.price=price
        m=77
        return price,m
class quantity(stock):
    def __init__(self,name,price,quantity3):
        super().__init__(
            name, price

        )

        self.quantity3=int(quantity3)

    def totalprice(self):

        print(self.quantity3*self.price)
        return self.quantity3*self.price
j=quantity("ama","333",5)
print(j.totalprice())