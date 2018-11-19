class Pocket:

    def __init__(self, settings):
        self.money = settings['money']
        self.apples = settings['apples']
        self.price = settings['price']

    def buy_apples(self, num_apples):
        if self.money - self.price * num_apples >= 0:
            self.money -= self.price * num_apples
            self.apples += num_apples
            print("Apples: " + str(self.apples))
            print("Money left:" + str(self.money))
        else:
            raise Exception("Not enough money to buy " + str(num_apples) + " apples")