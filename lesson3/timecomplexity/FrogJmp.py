#!/bin/python3

"""
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
Detected time complexity:
O(1)
"""
import math
def solution(X, Y, D):
    if not isinstance(X,int):
        raise TypeError("input must be integer")
    if X > 1000000000:
        raise ValueError("positive integer must be less than or equal to 1,000,000,000")
    return int(math.ceil( float(Y-X)/D ))

if __name__ == '__main__':
    print(solution(10,85,30))