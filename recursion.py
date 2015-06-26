import unittest

def factorial(k):
    if (k <= 1):
        return 1
    else:
        return k * (factorial(k - 1))

def bunny_ears(bunnies):
    if (bunnies == 0):
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)

print (bunny_ears(0))
print (bunny_ears(1))
print (bunny_ears(2))

class RecursionTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(4), 24)

    def test_bunny_ears(self):
        self.assertEqual(bunny_ears(0), 0)
        self.assertEqual(bunny_ears(1), 2)
        self.assertEqual(bunny_ears(2), 4)

if __name__ == '__main__':
    unittest.main()
