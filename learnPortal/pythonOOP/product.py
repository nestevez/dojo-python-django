class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price += self.price*tax
        return self

    def return_item(self,reason):
        if reason is "defective":
            self.status = "defective"
            self.price = 0
        elif reason is "in box, like new":
            self.status = "for sale"
        elif reason is "in box, opened":
            self.status = "used"
            self.price *= 0.8
        return self

    def display_info(self):
        print "Price: {}, Item Name: {}, Weight: {}, Brand: {}, Cost: {}, Status: {}".format(self.price, self.name, self.weight, self.brand, self.cost, self.status)
        return self


blouse = Product(25, "Green blouse", "5oz", "Some Brand", 15)

blouse.add_tax(0.10).sell().return_item("defective").display_info()
