#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
  """
  Approach: mark a element as element arr[a] += k and b+1 value as arr[b+1] -= k, then when we will do a commulative sum from from a to be we will get values k 
  from b onwards we will add -k in this way after all the queries we will set different values of k at different indexes with some values positive and some negative
  and adding all will give net result of k after all the queries and then find max from commulative sum of array will give the result.
  """
    # Write your code here
    n +=1
    arr = [0]*n
    for a,b,k in queries:
        arr[a-1] += k
        arr[b] -= k
    
    arrSum = 0
    maxSum = 0
    for i in range(len(arr)):
        arrSum += arr[i]
        maxSum = max(arrSum, maxSum)
    
    return maxSum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
