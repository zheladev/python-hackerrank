# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    n = str(sum((int(num) for num in n))*k)
    while (len(n) > 1):
        n = str(sum((int(num) for num in n)))
    return n


# def superDigit(n, k):
#     # Write your code here
#     acc = 0
#     n = int(n)
#     while (n > 0):
#         acc += n % 10
#         n //= 10
#     n = acc*k
#     while (n >= 10):
#         acc = 0
#         while (n > 0):
#             acc += n % 10
#             n //= 10
#         n = acc
#     return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
