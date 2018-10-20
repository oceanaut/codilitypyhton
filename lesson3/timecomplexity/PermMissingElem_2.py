#!/bin/python3

#https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
#Detected time complexity:
#O(N) or O(N * log(N))


def solution(A):
    return sum(range(1, len(A)+2)) - sum(A)
if __name__ == '__main__':
    print(solution([2, 3, 1, 5]))