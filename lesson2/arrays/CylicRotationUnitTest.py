#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

#!/bin/python3
import unittest
import random

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def solution(A,K):
    N=len(A)
    if not isinstance(K,int):
        raise TypeError("input must be integer")
    if K < 0:
        raise ValueError("input must be positive")
    if K > 100:
        raise ValueError("positive integer must be less than or equal to 100")
    if not len(A):
        return A
    shiftCount = (len(A) + K) % len(A)
    if shiftCount > 0:
        head = A[len(A)-shiftCount:]
        tail = A[:-shiftCount]
        return head + tail
    else:return A

class TestCyclicRotation(unittest.TestCase):
    # Candidate report
    def test_example(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 1), [6, 3, 8, 9, 7])
    def test_example2(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
    def test_test_example3(self):
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
    def test_extreme_empty(self):
        self.assertEqual(solution([], 100), [])
    def test_small_random_all_rotations(self):
        N = 15
        #K = random.randint(0, 15)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print(N, K)
        #print(N, K, A)
        #print(solution(A, K))
    def test_medium_random(self):
        N = 100
        #K = random.randint(0, 15)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print(N, K)
        #print(N, K, A)
        #print(solution(A, K))
    def test_medium_random(self):
        N = 100
        #K = random.randint(*INT_RANGE)
        K=100
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print(N, K)
        #print(N, K, A)
        #print(solution(A, K))

    # custom unit tests
    def test_non_int(self):
        self.assertRaises(TypeError, solution,[6, 3, 8, 9, 7],1.1)
    def test_positiveK(self):
        self.assertRaises(ValueError,solution,[6, 3, 8, 9, 8], -9)
    def test_maxK_plus_one(self):
        self.assertRaises(ValueError,solution,[6, 3, 8, 9, 7],101)
    def test_zero(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])
    def test_full(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])
    def test_extremes(self):
        self.assertEqual(solution([], 100), [])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
    def test_random(self):
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        #A = [random.randint(*ARRAY_RANGE) for i in xrange(0, N)]
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        #print(N, K, A)
        #print(solution(A, K))

if __name__ == '__main__':
    unittest.main()