def solution(A):
    # write your code in Python 3.6
    length_A = len(A)
    if len(set(A)) != length_A:
        return 0
    n = length_A
    if  ((n * (n  + 1 )) // 2) - sum(A) != 0:
        return 0
    return 1