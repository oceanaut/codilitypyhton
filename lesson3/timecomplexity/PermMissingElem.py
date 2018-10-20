#!/bin/python3

"""
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
Detected time complexity:
O(N) or O(N * log(N))
"""
def solution(A):
    N = len(A) + 1
    missing = ((N + 1) * N) / 2
    for x in A:
        missing -= x
    return int(missing)
if __name__ == '__main__':
    print(solution([2, 3, 1, 5]))