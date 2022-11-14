def solution(A):
    # write your code in Python 3.6
    max_value_a = max(A)
    B = list(range(min(A), max_value_a + 1))
    list(map(lambda x: B.remove(x) if x in B else None, A))
    if B:
        max_value_b = max(B)
        if max_value_b <= 0:
            return 1
        else:
            return max_value_b
    else:
        return max_value_a + 1



def solution2(A):
    # write your code in Python 3.6
    A = set(A)
    max_value_a = max(A)
    B = set(range(min(A), max_value_a + 1))
    C = set(set(A) ^ B)
    if C:
        max_value_C = max(C)
        if max_value_C <= 0:
            return 1
        else:
            return max_value_C
    else:
        return max_value_a + 1


def solution3(A):
    # write your code in Python 3.6
    max_value_a = max(set(A))
    if max_value_a <= 0:
        return 1
    B = set(range(min(A), max_value_a + 1))
    C = set(set(A) ^ B)
    if C:
        max_value_C = max(C)
        return max_value_C
    else:
        return max_value_a + 1

def solution4(A):
    # write your code in Python 3.6
    max_value_a = max(set(A))
    if max_value_a <= 0:
        return 1
    C = set(set(A) ^ set(range(min(A), max_value_a + 1)))
    return max(C) if C else max_value_a + 1


def solution5(A):
    # write your code in Python 3.6

    max_value_a = max(set(A))
    if max_value_a <= 0:
        return 1
    B = set(set(A) ^ set(range(min(A), max_value_a + 1)))
    try:
        return next(filter(lambda x: max(x), B), None) if B else max_value_a + 1
    except TypeError:
        return max(B)

def solution6(A):
    # write your code in Python 3.6
    A = set(A)
    max_value_a = max(A)
    if max_value_a <= 0:
        return 1
    B = set(A ^ set(range(1, max_value_a + 1)))
    try:
        return B.pop()
    except:
        return max_value_a + 1
    return next(filter(lambda x: max(x), B), None)


def solution7(A):
    # write your code in Python 3.6
    if not A:
        return 1
    A = set(A)
    max_value_a = max(A)
    if max_value_a <= 0:
        return 1
    B = set(A ^ set(range(1, max_value_a + 1)))
    try:
        return B.pop()
    except:
        return max_value_a + 1
    return next(filter(lambda x: max(x), B), None)

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1
    A = set(A)
    max_value_a = max(A)
    if max_value_a <= 0:
        return 1
    B = set(A ^ set(range(1, max_value_a + 1)))
    try:
        return next(filter(lambda x: max(x), B), None) if B else max_value_a + 1
    except TypeError:
        return B.pop()

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1
    A.sort(reverse=True)
    A = set(A)
    max_value_a = max(A)
    if max_value_a <= 0:
        return 1
    B = set(A ^ set(range(max_value_a + 1, 0, -1)))
    try:
        return next(filter(lambda x: max(x), B), None) if B else max_value_a + 1
    except TypeError:
        return B.pop()

assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([-1, -3]) == 1

'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
