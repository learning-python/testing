import calc
import unittest

# This class can be named anything.
class TestCalc(unittest.TestCase):

    def hello(self): # why does this test not run?
        print("running hello")
        ans = "hello"
        expected = "hello"
        self.assertEqual(ans, expected)
 
    def test_add(self):
        print("running test_add")
        ans = calc.add(3, 4)
        expected = 7
        self.assertEqual(ans, expected)
 
    def test_subtract(self):
        print("running test_subtract")
        ans = calc.subtract(3, 4)
        expected = -1
        self.assertEqual(ans, expected)
 
    def test_multiply(self):
        print("running test_multiply")
        ans = calc.multiply(3, 4)
        expected = 12
        self.assertEqual(ans, expected)

    def test_divide(self):
        print("running test_divide")
        ans = calc.divide(3, 4)
        expected = 0.75
        self.assertEqual(ans, expected)
 
 
if __name__ == '__main__':
    unittest.main()