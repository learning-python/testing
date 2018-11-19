import calc, buy_stuff
import unittest

settings = {
  'money': 10,
  'apples': 0,
  'price': 2
}

my_pocket = buy_stuff.Pocket(settings)

class TestCalc(unittest.TestCase):
  def test_three(self):
    my_pocket.buy_apples(3)
    self.assertEqual(my_pocket.apples, 3)
    self.assertEqual(my_pocket.money, 4)

  def test_three_more(self):
    self.assertRaises(Exception, my_pocket.buy_apples, 3)

if __name__ == '__main__':
    unittest.main()