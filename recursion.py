import unittest
from math import pow

def factorial(k):
    if k <= 1:
        return 1
    else:
        return k * (factorial(k - 1))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + (fibonacci(n - 2)))

def bunny_ears(bunnies):
    if bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)

def bunny_ears_2(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies % 2 == 1:
        return 2 + bunny_ears_2(bunnies - 1)
    else:
        return 3 + bunny_ears_2(bunnies - 1)

def triangle(rows):
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows - 1)

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(int(n / 10))

def sum_down_by_2(n):
    if n < 1:
        return 0
    else:
        return n + sum_down_by_2(n - 2)

def count_7(n):
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + count_7(int(n / 10))
    else:
        return count_7(int(n / 10))

def count_8(n):
    if n == 0:
        return 0
    elif n >= 88 and n % 100 == 88:
        return 2 + count_8(int(n / 10))
    elif n % 10 == 8:
        return 1 + count_8(int(n / 10))
    else:
        return count_8(int(n / 10))

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))

def geometric_sum(k):
    if k < 0:
        return 0
    else:
        return 1 / (pow(2, k)) + geometric_sum(k - 1)

def expt(n, k):
    if k <= 0:
        return 1
    else:
        return n * expt(n, k - 1)

def count_x(str):
    if len(str) == 0:
        return 0
    elif str[0] == 'x':
        return 1 + count_x(str[1:])
    else:
        return count_x(str[1:])

def count_hi(str):
    if len(str) < 2:
        return 0
    elif str[0:2] == 'hi':
        return 1 + count_hi(str[2:])
    else:
        return count_hi(str[1:])

def change_xy(str):
    if len(str) == 0:
        return str
    elif str[0] == 'x':
        return 'y' + change_xy(str[1:])
    else:
        return str[0] + change_xy(str[1:])

def change_pi(str):
    if len(str) < 2:
        return str
    elif str[0:2] == 'pi':
        return '3.14' + change_pi(str[2:])
    else:
        return str[0] + change_pi(str[1:])

def no_x(str):
    if len(str) == 0:
        return ''
    elif str[0] == 'x':
        return no_x(str[1:])
    else:
        return str[0] + no_x(str[1:])

def all_star(str):
    if len(str) <= 1:
        return str
    else:
        return str[0] + '*' + all_star(str[1:])

def pair_star(str):
    if len(str) < 2:
        return str
    elif str[0] == str[1]:
        return str[0] + '*' + pair_star(str[1:])
    else:
        return str[0] + pair_star[str[1:]]

def reverse_string(text):
    if len(text) <= 1:
        return text
    else:
        return reverse_string(text[1:] + text[0])

def end_x(str):
    if len(str):
        return str
    elif str[0] == 'x':
        return end_x(str[1:] + 'x')
    else:
        return str[0] + end_x(str[1:])

def count_pairs(str):
    if len(str) < 3:
        return 0
    elif str[0] == str[2]:
        return 1 + count_pairs(str[1:])
    else:
        return count_pairs(str[1:])

def count_abc(str):
    if len(str) < 3:
        return 0
    elif str[0:3] == 'abc' or str[0:3] == 'aba':
        return 1 + count_abc(str[1:])
    else:
        return count_abc(str[1:])

def count_11(str):
    if len(str) < 2:
        return 0
    elif str[0:2] == '11':
        return 1 + count_11(str[2:])
    else:
        return count_11(str[1:])

def string_clean(str):
    if len(str) < 2:
        return str
    elif str[0] == str[1]:
        return string_clean(str[1:])
    else:
        return str[0] + string_clean(str[1:])

def string_count(str, sub):
    if len(str) < len(sub):
        return 0
    elif str[0:len(sub)] == sub:
        return 1 + string_count(str[len(sub)], sub)
    else:
        return string_count(str[1:], sub)

def string_copies(str, sub, n):
    if len(str) < len(sub):
        return n <= 0
    elif str[0:len(sub)] == sub:
        return string_copies(str[1:], sub, n - 1)
    else:
        return string_copies(str[1:], sub, n)

def string_dist(str, sub):
    if str.index(sub) == -1:
        return 0
    elif str[0:len(sub)] == sub and str[len(str) - len(sub)] == sub:
        return len(str)
    elif not(str[0:len(sub)] == sub):
        return string_dist(str[1:], sub)
    else:
        return string_dist(str[0:len(str) - 1], sub)

def lcm(j, k):
    return (j * k) / gcd(j, k)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def loan_length(p, i, mp):
    return __loan_length_helper__(p, i / 12, mp, 0)

def __loan_length_helper__(p , i, mp, months):
    if p <= 0:
        return months
    else:
        return __loan_length_helper__((p - mp) + (p * i), i, mp, months + 1)

def primes(x, i):
    if i == 1:
        return True
    elif x % i == 0:
        return False
    else:
        return primes(x, i - 1)

def tower_of_hanoi(n, start, auxillary, end):
    if n == 1:
        print ('Current Disk ', n, ': ', start, ' -> ', end)
    else:
        tower_of_hanoi(n - 1, start, end, auxillary)
        print ('Current Disk ', n, ': ', start, ' -> ', end)
        tower_of_hanoi(n - 1, auxillary, start, end)

class RecursionTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(4), 24)

    def test_bunny_ears(self):
        self.assertEqual(bunny_ears(0), 0)
        self.assertEqual(bunny_ears(1), 2)
        self.assertEqual(bunny_ears(2), 4)

    def test_bunny_ears_2(self):
        self.assertEqual(bunny_ears_2(0), 0)
        self.assertEqual(bunny_ears_2(1), 2)
        self.assertEqual(bunny_ears_2(2), 5)

    def test_triangle(self):
        self.assertEqual(triangle(0), 0)
        self.assertEqual(triangle(1), 1)
        self.assertEqual(triangle(2), 3)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(126), 9)
        self.assertEqual(sum_digits(49), 13)
        self.assertEqual(sum_digits(12), 3)

    def test_count_7(self):
        self.assertEqual(count_7(8643), 0)
        self.assertEqual(count_7(717), 2)

    def test_count_8(self):
        self.assertEqual(count_8(8), 1)
        self.assertEqual(count_8(818), 2)
        self.assertEqual(count_8(8188), 4)

    def test_sum_down_by_2(self):
        self.assertEqual(sum_down_by_2(0), 0)
        self.assertEqual(sum_down_by_2(2), 2)
        self.assertEqual(sum_down_by_2(6), 12)

    def test_harmonic_sum(self):
        self.assertEqual(harmonic_sum(1), 1)
        self.assertEqual(harmonic_sum(2), 1.5)
        self.assertAlmostEqual(harmonic_sum(3), 1.833, 3)
        self.assertAlmostEqual(harmonic_sum(4), 2.083, 3)

    def test_geometric_sum(self):
        self.assertAlmostEqual(geometric_sum(0), 1, 1)
        self.assertAlmostEqual(geometric_sum(1), 1.5, 1)

    def test_count_x(self):
        self.assertEqual(count_x('hi'), 0)
        self.assertEqual(count_x('hixx'), 2)
        self.assertEqual(count_x('xxhixx'), 4)

    def test_count_hi(self):
        self.assertEqual(count_hi('hi'), 1)
        self.assertEqual(count_hi('xxhixx'), 1)
        self.assertEqual(count_hi('xhixhix'), 2)

    def test_change_xy(self):
        self.assertEqual(change_xy('codex'), 'codey')
        self.assertEqual(change_xy('xxhixx'), 'yyhiyy')
        self.assertEqual(change_xy('xhixhix'), 'yhiyhiy')


if __name__ == '__main__':
    unittest.main()
