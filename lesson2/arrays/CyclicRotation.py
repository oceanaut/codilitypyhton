#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

#!/bin/python3
import unittest
import random

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def solution(A,K):

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

if __name__ == '__main__':
    #the function should return [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6],3))
    #the function should return [0, 0, 0]
    print(solution([0, 0, 0],1))
    #the function should return [1, 2, 3, 4]
    print(solution([1, 2, 3, 4],4))