def solution(A):
    # write your code in Python 3.6
    m = len(A)
    return int((m * (m  + 1 ))//2 - sum(A) == 0)