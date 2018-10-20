#!/bin/python3

"""
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
Detected time complexity:
O(1)
"""

def solution(X, Y, D):
    if not isinstance(X,int):
        raise TypeError("input must be integer")
    if X > 1000000000:
        raise ValueError("positive integer must be less than or equal to 1,000,000,000")
    quotadien, remainder = divmod(Y-X, D)
    return quotadien if remainder == 0 else quotadien + 1

if __name__ == '__main__':
    print(solution(10,85,30))