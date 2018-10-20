#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

#!/bin/python3

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


if __name__ == '__main__':
    #For example, given N = 1041 the function should return 5
    print(solution(1041))
    #The number 15 has binary representation 1111 and has no binary gaps
    print(solution(15))
    #Given N = 32 the function should return 0
    print(solution(32))
    #number 9 has binary representation 1001 and contains a binary gap of length 2
    print(solution(9))