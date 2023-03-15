#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def map_arr(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n > 0:
        return 1


def plusMinus(arr: list):
    arr = [map_arr(n) for n in arr]
    sample_size = len(arr)
    ratios = Counter(arr)
    for i in [1, -1, 0]:  # output order
        print("{:.6f}".format(ratios[i]/sample_size))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
