#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumSum(arr):
    # Write your code here
    if arr:
        new_arr = []
        for i in range(len(arr)):
            list(map(lambda j: new_arr.append(sum(arr[i:j])), range(len(arr) + 1)))
            # for j in range(len(arr)+1):
            #     new_arr.append(sum(arr[i:j]))
        if new_arr:
            max_value = max(new_arr)
            if max_value <= 0:
                return 0
            else:
                return max_value
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maximumSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
4
-1
-2
1
3

4
'''

'''
def foo(value):
    while True:
        value = (yield value)

bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))
'''

