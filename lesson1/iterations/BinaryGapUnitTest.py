#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

#!/bin/python3
import unittest

MAXINT = 2147483647

def solution(n):
    maxgap = 0
    gap = 0
    firstbit=True

    if not isinstance(n,int):
        raise TypeError("input must be integer")
    if n < 1:
        raise ValueError("input must be positive")
    if n > MAXINT:
        raise ValueError("positive integer must be less than 2,147,483,647")
    binary_string = str(bin(n))[2:]
    for bit in binary_string:
        if bit == '0':
            gap += 1
        else:
            if(firstbit):
                maxgap = max(maxgap,gap)
                gap = 0
    return maxgap


class TestBinaryGap(unittest.TestCase):
    #Candidate Report results verification
    def test_example1(self):
        self.assertEqual(solution(1041),5)
    def test_example2(self):
        self.assertEqual(solution(15),0)
    def test_example3(self):
        self.assertEqual(solution(32),0)
    def test_extremes(self):
        self.assertEqual(solution(1),0)
        self.assertEqual(solution(5),1)
        self.assertEqual(solution(328),2)
    def test_trailing_zeros(self):
        self.assertEqual(solution(6), 0)
        #self.assertEqual(0, solution(6))
        self.assertEqual(solution(328), 2)
    def test_power_of_2(self):
        #self.assertEqual(solution(6), 0)
        #self.assertEqual(0, solution(6))
        self.assertEqual(solution(5), 1)
        self.assertEqual(solution(2**4), 0)
        self.assertEqual(solution(2**10), 0)
    def test_simple1(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(11), 1)
    def test_simple2(self):
        self.assertEqual(solution(19), 2)
        self.assertEqual(solution(42), 1)
    def test_simple3(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(5), 1)
    def test_medium1(self):
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(20), 1)
    def test_medium2(self):
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(9), 2)
    def test_medium3(self):
        self.assertEqual(solution(66561), 9)
    def test_large1(self):
        self.assertEqual(solution(6291457), 20)
    def test_large2(self):
        self.assertEqual(solution(74901729), 4)
    def test_large3(self):
        self.assertEqual(solution(805306373), 25)
    def test_large4(self):
        self.assertEqual(solution(1376796946), 5)
    def test_large5(self):
        self.assertEqual(solution(1073741825), 29)
    def test_large6(self):
        self.assertEqual(solution(1610612737), 28)
    #custom unit tests
    def test_non_int(self):
        self.assertRaises(TypeError, solution, 1.0)
    def test_zero(self):
        self.assertRaises(ValueError, solution, 0)
    def test_zero(self):
        self.assertRaises(ValueError, solution, -2)
    def test_maxint_plus_one(self):
        self.assertRaises(ValueError, solution, 2147483648)


if __name__ == '__main__':
    unittest.main()