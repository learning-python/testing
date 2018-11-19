import calc
class Pocket:

    def __init__(self, settings):
        self.money = settings['money']
        self.apples = settings['apples']
        self.price = settings['price']

    def buy_apples(self, num_apples):
        needed = calc.multiply(self.price, num_apples)
        would_be_left = calc.subtract(self.money, needed)

        if would_be_left >= 0:
            self.money -= self.price * num_apples
            self.apples += num_apples
        else:
            raise Exception("Not enough money to buy " + str(num_apples) + " apples")