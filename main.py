import calc, buy_stuff

settings = {
  'money': 10,
  'apples': 0,
  'price': 2
}

my_pocket = buy_stuff.Pocket(settings)

my_pocket.buy_apples(3)