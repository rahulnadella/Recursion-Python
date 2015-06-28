"""
 Copyright (c) 2015, Rahul Nadella
 All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other
 materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from math import pow
import unittest
import logging

# Set the Logger level to Info and log any messages to recursion.log
logging.basicConfig(filename='recursion.log', level=logging.INFO)

"""
In mathematics, the factorial of a non-negative integer n, denoted by n!,
is the product of all positive integers less than or equal to n. For
example, The value of 0! is 1, according to the convention for an empty
product.
"""


def factorial(k):
  if k <= 1:
    return 1
  else:
    return k * (factorial(k - 1))

"""
Solves the Fibonacci Sequence using recursion.
"""


def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

"""
We have a number of bunnies and each bunny has two big floppy ears. We
want to compute the total number of ears across all the bunnies
recursively (without loops or multiplication).

<pre>
Example:
bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
</pre>
"""


def bunny_ears(bunnies):
  if bunnies == 0:
    return 0
  else:
    return 2 + bunny_ears(bunnies - 1)

"""
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
(1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
have 3 ears, because they each have a raised foot. Recursively return the
number of "ears" in the bunny line 1, 2, ... n (without loops or
multiplication).

<pre>
Example:
bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
</pre>
"""


def bunny_ears_2(bunnies):
  if bunnies == 0:
    return 0
  elif bunnies % 2 == 1:
    return 2 + bunny_ears_2(bunnies - 1)
  else:
    return 3 + bunny_ears_2(bunnies - 1)

"""
We have triangle made of blocks. The topmost row has 1 block, the next
row down has 2 blocks, the next row has 3 blocks, and so on. Compute
recursively (no loops or multiplication) the total number of blocks in
such a triangle with the given number of rows.

<pre>
Example:
triangle(0) → 0
triangle(1) → 1
triangle(2) → 3
</pre>
"""


def triangle(rows):
  if rows == 0:
    return 0
  else:
    return rows + triangle(rows - 1)

"""
Given a non-negative int n, return the sum of its digits recursively (no
loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is
6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

<pre>
Example:
sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
</pre>
"""


def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))

"""
Recursive method returns the sum of the positive integers of
n+(n-2)+(n-4)... (until n-x =< 0)
"""


def sum_down_by_2(n):
  if n < 1:
    return 0
  else:
    return n + sum_down_by_2(n - 2)

"""
Given a non-negative int n, return the count of the occurrences of 7 as a
digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10
yields the rightmost digit (126 % 10 is 6), while divide (/) by 10
removes the rightmost digit (126 / 10 is 12).

<pre>
Example:
count7(717) → 2
count7(7) → 1
count7(123) → 0
</pre>
"""


def count_7(n):
  if n == 0:
    return 0
  elif n % 10 == 7:
    return 1 + count_7(int(n / 10))
  else:
    return count_7(int(n / 10))

"""
Given a non-negative int n, compute recursively (no loops) the count of
the occurrences of 8 as a digit, except that an 8 with another 8
immediately to its left counts double, so 8818 yields 4. Note that mod
(%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by
10 removes the rightmost digit (126 / 10 is 12).

<pre>
Example:
count8(8) → 1
count8(818) → 2
count8(8818) → 4
</pre>
"""


def count_8(n):
  if n == 0:
    return 0
  elif n >= 88 and n % 100 == 88:
    return 2 + count_8(int(n / 10))
  elif n % 10 == 8:
    return 1 + count_8(int(n / 10))
  else:
    return count_8(int(n / 10))

"""
Recursive method returns the harmonic sum of n-1
"""


def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))

"""
Recursive method returns the geometric sum
"""


def geometric_sum(k):
  if k < 0:
    return 0
  else:
    return 1 / (pow(2, k)) + geometric_sum(k - 1)

"""
Recursive method returns the multiplacative sum of j*k (uses multhelper
and then addresses the negative case)
"""


def mult(j, k):
  if k < 0:
    return -__mult_helper__(j, -k)
  else:
    return __mult_helper__(j, k)

"""
Recursive method returns the multiplacative sum of j*k when integers j, k
are positive

This function is private please use the mult function
"""


def __mult_helper__(j, k):
  if j == 0 or k == 0:
    return 0
  else:
    return (j + mult(j, k - 1))

"""
Recursive method returns the value of n to the k
"""


def expt(n, k):
  if k <= 0:
    return 1
  else:
    return n * expt(n, k - 1)

"""
Given a string, compute recursively (no loops) the number of lowercase
'x' chars in the string.

<pre>
Example:
countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
</pre>
"""


def count_x(str):
  if len(str) == 0:
    return 0
  elif str[0] == 'x':
    return 1 + count_x(str[1:])
  else:
    return count_x(str[1:])

"""
Given a string, compute recursively (no loops) the number of times
lowercase "hi" appears in the string.

<pre>
Example:
countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
</pre>
"""


def count_hi(str):
  if len(str) < 2:
    return 0
  elif str[0:2] == 'hi':
    return 1 + count_hi(str[2:])
  else:
    return count_hi(str[1:])

"""
Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars.

<pre>
Example:
changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
</pre>
"""


def change_xy(str):
  if len(str) == 0:
    return str
  elif str[0] == 'x':
    return 'y' + change_xy(str[1:])
  else:
    return str[0] + change_xy(str[1:])

"""
Given a string, compute recursively (no loops) a new string where all
appearances of "pi" have been replaced by "3.14".

<pre>
Example:
changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
</pre>
"""


def change_pi(str):
  if len(str) < 2:
    return str
  elif str[0:2] == 'pi':
    return '3.14' + change_pi(str[2:])
  else:
    return str[0] + change_pi(str[1:])

"""
Given a string, compute recursively a new string where all the 'x' chars
have been removed.

<pre>
Example:
noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
"""


def no_x(str):
  if len(str) == 0:
    return ''
  elif str[0] == 'x':
    return no_x(str[1:])
  else:
    return str[0] + no_x(str[1:])

"""
Given a string, compute recursively a new string where all the adjacent
chars are now separated by a "*".

<pre>
Example:
allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
</pre>
"""


def all_star(str):
  if len(str) <= 1:
    return str
  else:
    return str[0] + '*' + all_star(str[1:])

"""
Given a string, compute recursively a new string where identical chars
that are adjacent in the original string are separated from each other by
a "*".

<pre>
Example:
pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
</pre>
"""


def pair_star(str):
  if len(str) < 2:
    return str
  elif str[0] == str[1]:
    return str[0] + '*' + pair_star(str[1:])
  else:
    return str[0] + pair_star(str[1:])

"""
The reverseString method returns a String in reverse order (HELLO ->
OLLEH)
"""


def reverse_string(text):
  if len(text) <= 1:
    return text
  else:
    return reverse_string(text[1:]) + text[0]

"""
Given a string, compute recursively a new string where all the lowercase
'x' chars have been moved to the end of the string.

<pre>
Example:
endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
</pre>
"""


def end_x(str):
  if len(str) == 0:
    return str
  elif str[0] == 'x':
    return end_x(str[1:]) + 'x'
  else:
    return str[0] + end_x(str[1:])

"""
We'll say that a "pair" in a string is two instances of a char separated
by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA"
contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number
of pairs in the given string.

<pre>
Example:
countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
</pre>
"""


def count_pairs(str):
  if len(str) < 3:
    return 0
  elif str[0] == str[2]:
    return 1 + count_pairs(str[1:])
  else:
    return count_pairs(str[1:])

"""
Count recursively the total number of "abc" and "aba" substrings that
appear in the given string.

<pre>
Example:
countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
</pre>
"""


def count_abc(str):
  if len(str) < 3:
    return 0
  elif str[0:3] == 'abc' or str[0:3] == 'aba':
    return 1 + count_abc(str[1:])
  else:
    return count_abc(str[1:])

"""
Given a string, compute recursively (no loops) the number of "11"
substrings in the string. The "11" substrings should not overlap.

<pre>
Example:
count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
</pre>
"""


def count_11(str):
  if len(str) < 2:
    return 0
  elif str[0:2] == '11':
    return 1 + count_11(str[2:])
  else:
    return count_11(str[1:])

"""
Given a string, return recursively a "cleaned" string where adjacent
chars that are the same have been reduced to a single char. So "yyzzza"
yields "yza".

<pre>
Example:
stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
</pre>
"""


def string_clean(str):
  if len(str) < 2:
    return str
  elif str[0] == str[1]:
    return string_clean(str[1:])
  else:
    return str[0] + string_clean(str[1:])

"""
Given a string and a non-empty substring sub, compute recursively the
number of times that sub appears in the string, without the sub strings
overlapping.

<pre>
Example:
strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
</pre>
"""


def string_count(str, sub):
  if len(str) < len(sub):
    return 0
  elif str[0:len(sub)] == sub:
    return 1 + string_count(str[len(sub):], sub)
  else:
    return string_count(str[1:], sub)

"""
Given a string and a non-empty substring sub, compute recursively if at
least n copies of sub appear in the string somewhere, possibly with
overlapping. N will be non-negative.

<pre>
Example:
strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
</pre>
"""


def string_copies(str, sub, n):
  if len(str) < len(sub):
    return n <= 0
  elif str[0:len(sub)] == sub:
    return string_copies(str[1:], sub, n - 1)
  else:
    return string_copies(str[1:], sub, n)

"""
Given a string and a non-empty substring sub, compute recursively the
largest substring which starts and ends with sub and return its length.

<pre>
Example:
strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
</pre>
"""


def string_dist(str, sub):
  if str.index(sub) == -1:
    return 0
  elif str[0:len(sub)] == sub and str[len(str) - len(sub):] == sub:
    return len(str)
  elif not(str[0:len(sub)] == sub):
    return string_dist(str[1:], sub)
  else:
    return string_dist(str[0:len(str) - 1], sub)

"""
Recursive method returns the least common multiple of integers j and k
"""


def lcm(j, k):
  return (j * k) / gcd(j, k)

"""
Recursive method returns the greatest common denominator of integers a
and b
"""


def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

"""
Finds months needed to pay off loan payment with an interest rate over a
year
"""


def loan_length(p, i, mp):
  return __loan_length_helper__(p, i / 12, mp, 0)

"""
Finds the months needed to pay off loan payment

This function is private please use the loan_length function
"""


def __loan_length_helper__(p, i, mp, months):
  if p <= 0:
    return months
  else:
    return __loan_length_helper__((p - mp) + (p * i), i, mp, months + 1)

"""
Determines if a number is prime or not.
"""


def primes(x, i):
  if i == 1:
    return True
  elif x % i == 0:
    return False
  else:
    return primes(x, i - 1)

"""
Given an array of ints, compute recursively if the array contains a 6.
We'll use the convention of considering only the part of the array that
begins at the given index. In this way, a recursive call can pass index+1
to move down the array. The initial call will pass in index as 0.

<pre>
Example:
array6({1, 6, 4}, 0) → true
array6({1, 4}, 0) → false
array6({6}, 0) → true
</pre>
"""


def array6(nums, index):
  if len(nums) == 0:
    return False
  elif index == len(nums) - 1:
    return nums[index] == 6
  elif nums[index] == 6:
    return True
  else:
    return array6(nums, index + 1)

"""
Given an array of ints, compute recursively the number of times that the
value 11 appears in the array. We'll use the convention of considering
only the part of the array that begins at the given index. In this way, a
recursive call can pass index+1 to move down the array. The initial call
will pass in index as 0.

<pre>
Example
array11({1, 2, 11}, 0) → 1
array11({11, 11}, 0) → 2
array11({1, 2, 3, 4},0) → 0
</pre>
"""


def array11(nums, index):
  if index == len(nums):
    return 0
  elif nums[index] == 11:
    return 1 + array11(nums, index + 1)
  else:
    return array11(nums, index + 1)

"""
Given an array of ints, compute recursively if the array contains
somewhere a value followed in the array by that value times 10. We'll use
the convention of considering only the part of the array that begins at
the given index. In this way, a recursive call can pass index+1 to move
down the array. The initial call will pass in index as 0.

<pre>
Example:
array220({1, 2, 20}, 0) → true
array220({3, 30}, 0) → true
array220({3},0) → false
</pre>
"""


def array220(nums, index):
  if len(nums) < 2 or index == len(nums) - 1:
    return False
  elif nums[index + 1] == nums[index] * 10:
    return True
  else:
    return array220(nums, index + 1)

"""
The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower,[1]
and sometimes pluralized) is a mathematical game or puzzle. It consists
of three rods, and a number of disks of different sizes which can slide
onto any rod. The puzzle starts with the disks in a neat stack in
ascending order of size on one rod, the smallest at the top, thus making
a conical shape.

The objective of the puzzle is to move the entire stack to another rod,
obeying the following simple rules:

Only one disk can be moved at a time. Each move consists of taking the
upper disk from one of the stacks and placing it on top of another stack
i.e. a disk can only be moved if it is the uppermost disk on a stack. No
disk may be placed on top of a smaller disk.
"""


def tower_of_hanoi(n, start, auxillary, end):
  if n == 1:
    logging.info("Current Dist '{0}' : '{1}' -> '{2}'".format(n, start, end))
  else:
    tower_of_hanoi(n - 1, start, end, auxillary)
    logging.info("Current Dist '{0}' : '{1}' -> '{2}'".format(n, start, end))
    tower_of_hanoi(n - 1, auxillary, start, end)

"""
The RecursionTest is used to test the several common functions using recursion
"""


class RecursionTest(unittest.TestCase):

  """
  Test to determine whether the factorial method returns the correct sum
  """

  def test_factorial(self):
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(4), 24)

  """
    Test to determine whether the bunnyEars method returns the correct sum
    """

  def test_bunny_ears(self):
    self.assertEqual(bunny_ears(0), 0)
    self.assertEqual(bunny_ears(1), 2)
    self.assertEqual(bunny_ears(2), 4)

  """
    Test to determine whether the bunnyEars2 method returns the correct sum
    """

  def test_bunny_ears_2(self):
    self.assertEqual(bunny_ears_2(0), 0)
    self.assertEqual(bunny_ears_2(1), 2)
    self.assertEqual(bunny_ears_2(2), 5)

  """
    Test to determine whether the triangle method returns the correct blocks
    """

  def test_triangle(self):
    self.assertEqual(triangle(0), 0)
    self.assertEqual(triangle(1), 1)
    self.assertEqual(triangle(2), 3)

  """
    Test to determine whether the sumDigits method returns the calculated
    value
    """

  def test_sum_digits(self):
    self.assertEqual(sum_digits(126), 9)
    self.assertEqual(sum_digits(49), 13)
    self.assertEqual(sum_digits(12), 3)

  """
    Test to determine whether the count7 method returns the number of 7's in
    the integer value.
    """

  def test_count_7(self):
    self.assertEqual(count_7(8643), 0)
    self.assertEqual(count_7(717), 2)

  """
    Test to determine whether the count8 method returns the corresponding
    number of 8's in integer value
    """

  def test_count_8(self):
    self.assertEqual(count_8(8), 1)
    self.assertEqual(count_8(818), 2)
    self.assertEqual(count_8(8188), 4)

  """
    Test to determine whether the sumDownBy2 recursive method returns the sum
    of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
    """

  def test_sum_down_by_2(self):
    self.assertEqual(sum_down_by_2(0), 0)
    self.assertEqual(sum_down_by_2(2), 2)
    self.assertEqual(sum_down_by_2(6), 12)

  """
    Test to determine whether the harmonicSum recursive method returns the
    sum of the positive integers of 1 + 1/2 + 1/(n-1) .... + 1/n
    """

  def test_harmonic_sum(self):
    self.assertEqual(harmonic_sum(1), 1)
    self.assertEqual(harmonic_sum(2), 1.5)
    self.assertAlmostEqual(harmonic_sum(3), 1.833, 3)
    self.assertAlmostEqual(harmonic_sum(4), 2.083, 3)

  """
    Test to determine whether the geometricSum recursive method returns the
    sum of the positive integers of 1 + 1/2 + 1/(n-1) .... + 1/n
    """

  def test_geometric_sum(self):
    self.assertAlmostEqual(geometric_sum(0), 1, 1)
    self.assertAlmostEqual(geometric_sum(1), 1.5, 1)

  """
    Test to determine whether the mult recursive method returns j*k
    """

  def test_mult(self):
    self.assertEqual(mult(2, 3), 6)
    self.assertEqual(mult(-2, 5), -10)

  """
    Test to determine whether the recursive method returns the value of n to
    k
    """

  def test_expt(self):
    self.assertEqual(expt(2, 3), 8)
    self.assertEqual(expt(3, 1), 3)

  """
    Test to determine whether the countX method returns the integer value of
    X's contained in the String object.
    """

  def test_count_x(self):
    self.assertEqual(count_x('hi'), 0)
    self.assertEqual(count_x('hixx'), 2)
    self.assertEqual(count_x('xxhixx'), 4)

  """
    Test to determine whether the countHi method returns the integer value of
    Hi's contained in the String object
    """

  def test_count_hi(self):
    self.assertEqual(count_hi('hi'), 1)
    self.assertEqual(count_hi('xxhixx'), 1)
    self.assertEqual(count_hi('xhixhix'), 2)

  """
    Test to determine whether the changeXY method returns the String object
    with any X characters changed to Y characters
    """

  def test_change_xy(self):
    self.assertEqual(change_xy('codex'), 'codey')
    self.assertEqual(change_xy('xxhixx'), 'yyhiyy')
    self.assertEqual(change_xy('xhixhix'), 'yhiyhiy')

  """
    Test to determine whether the changePi method returns the String object
    with any Pi characters changed to 3.14
    """

  def test_change_pi(self):
    self.assertEqual(change_pi('xpix'), 'x3.14x')
    self.assertEqual(change_pi('pipi'), '3.143.14')
    self.assertEqual(change_pi('pip'), '3.14p')

  """
    Test to determine whether the noX method returns the String object
    without an X's characters in it
    """

  def test_no_x(self):
    self.assertEqual(no_x('xaxb'), 'ab')
    self.assertEqual(no_x('abc'), 'abc')
    self.assertEqual(no_x('xx'), '')

  """
    Test to determine whether the allStar method returns the String object
    containing * character in it.
    """

  def test_all_star(self):
    self.assertEqual(all_star('hello'), 'h*e*l*l*o')
    self.assertEqual(all_star('abc'), 'a*b*c')
    self.assertEqual(all_star('ab'), 'a*b')

  """
    Test to determine whether the pairStar method returns the String object
    containing * character for identical pairs of characters within the
    String.
    """

  def test_pair_star(self):
    self.assertEqual(pair_star('hello'), 'hel*lo')
    self.assertEqual(pair_star('xxyy'), 'x*xy*y')
    self.assertEqual(pair_star('aaaa'), 'a*a*a*a')

  """
    Test to determine whether the endX method returns a String object with
    any X character moved to the end of the String.
    """

  def test_end_x(self):
    self.assertEqual(end_x('xxre'), 'rexx')
    self.assertEqual(end_x('xxhixx'), 'hixxxx')
    self.assertEqual(end_x('xhixhix'), 'hihixxx')

  """
    Test to determine whether the countPairs method returns the Integer value
    with corresponding pairs within a String object
    """

  def test_count_pairs(self):
    self.assertEqual(count_pairs('axa'), 1)
    self.assertEqual(count_pairs('axax'), 2)
    self.assertEqual(count_pairs('axbx'), 1)

  """
    Test to determine whether the countABC method returns the Integer value
    of the number of ABC character within the String
    """

  def test_count_abc(self):
    self.assertEqual(count_abc('abc'), 1)
    self.assertEqual(count_abc('abcxxabc'), 2)
    self.assertEqual(count_abc('abaxxaba'), 2)

  """
    Test to determine whether the count11 method returns the Integer value of
    the number of 11 characters within the String
    """

  def test_count_11(self):
    self.assertEqual(count_11('11abc11'), 2)
    self.assertEqual(count_11('abc11x11x11'), 3)
    self.assertEqual(count_11('111'), 1)

  """
    Test to determine whether the stringClean method returns the String
    object of a String without any adjacent characters within it
    """

  def test_string_clean(self):
    self.assertEqual(string_clean('yyzzza'), 'yza')
    self.assertEqual(string_clean('abbbcdd'), 'abcd')
    self.assertEqual(string_clean('Hello'), 'Helo')

  """
    Test to determine whether the strCount method returns the Integer value
    of String containing a specific sequence of characters within it
    """

  def test_string_count(self):
    self.assertEqual(string_count('catcowcat', 'cat'), 2)
    self.assertEqual(string_count('catcowcat', 'cow'), 1)
    self.assertEqual(string_count('catcowcat', 'dog'), 0)

  """
    Test to determine whether the strCopies method returns the Boolean value
    """

  def test_string_copies(self):
    self.assertEqual(string_copies('catcowcat', 'cat', 2), True)
    self.assertEqual(string_copies('catcowcat', 'cow', 2), False)
    self.assertEqual(string_copies('catcowcat', 'cow', 1), True)

  """
    Test to determine whether the strDist method returns the Integer value
    """

  def test_string_dist(self):
    self.assertEqual(string_dist('catcowcat', 'cat'), 9)
    self.assertEqual(string_dist('catcowcat', 'cow'), 3)
    self.assertEqual(string_dist('cccatcowcatxx', 'cat'), 9)

  """
    Test to determine whether the recursive method returns the least common
    multiple of j and k
    """

  def test_lcm(self):
    self.assertAlmostEqual(lcm(5, 3), 15, 1)
    self.assertAlmostEqual(lcm(6, 8), 24, 1)

  """
    Test to determine whether loan length calc works
    """

  def test_loan_length(self):
    self.assertEqual(loan_length(0, 0, 0), 0)
    self.assertEqual(loan_length(1000, 0.1, 250), 5)

  """
    Test to determine whether reverseString works
    """

  def test_reverse_string(self):
    self.assertEqual(reverse_string('Hello'), 'olleH')

  """
    Test to print out all prime numbers of 100
    """

  def test_primes(self):
    for i in range(2, 100):
      if primes(i, i - 1):
        print (+i, ' is prime')

  """
    Test to determine if the array6 function outputs the correct Boolean value
    """

  def test_array6(self):
    self.assertTrue(array6([1, 6, 4], 0))
    self.assertFalse(array6([1, 4], 0))
    self.assertTrue(array6([6], 0))

  """
    Test to determine if the array11 function computes the correct number of times
    11 is in the array
    """

  def test_array11(self):
    self.assertEqual(array11([1, 2, 11], 0), 1)
    self.assertEqual(array11([11, 11], 0), 2)
    self.assertEqual(array11([1, 2, 3, 4], 0), 0)

  """
    Test to determine if the array220 function computes the correct Boolean value
    """

  def test_array220(self):
    self.assertTrue(array220([1, 2, 20], 0))
    self.assertTrue(array220([3, 30], 0))
    self.assertFalse(array220([3], 0))

  """
    Test to solve the Tower of Hanoi game
    """

  def test_tower_of_hanoi(self):
    tower_of_hanoi(1, 'A', 'B', 'C')
    tower_of_hanoi(2, 'A', 'B', 'C')
    tower_of_hanoi(3, 'A', 'B', 'C')
    tower_of_hanoi(4, 'A', 'B', 'C')
    tower_of_hanoi(5, 'A', 'B', 'C')

if __name__ == '__main__':
  unittest.main()
