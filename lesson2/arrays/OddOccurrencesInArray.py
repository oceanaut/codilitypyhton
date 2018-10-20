#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

#!/bin/python3


def solution(A):
    ret=0
    for i in A:
        ret ^= i
    return ret

if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))

