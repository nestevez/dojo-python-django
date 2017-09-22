class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print "Price: {}, Max Speed: {}, Miles: {}".format(self.price,self.max_speed,self.miles)
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        if self.miles >= 5:
            self.miles -= 5
        else:
            self.miles = 0
        return self



redbike = Bike(200, "25mph")
bluebike = Bike(50, "15mph")
greenbike = Bike(750, "30mph")

redbike.ride().ride().ride().reverse().display_info()
bluebike.ride().ride().reverse().reverse().display_info()
greenbike.reverse().reverse().reverse().display_info()
