# https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-five&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def get_bracket_index(b):
    if b == "{":
        return 0
    if b == "[":
        return 1
    if b == "(":
        return 2
    if b == "}":
        return 3
    if b == "]":
        return 4
    if b == ")":
        return 5
    return -1


def isBalanced(s):
    bracket_types = 3
    bracket_list = []
    for bracket in s:
        b_idx = get_bracket_index(bracket)
        if b_idx < 3:
            bracket_list.append(b_idx)
        elif len(bracket_list) == 0 or b_idx % bracket_types != bracket_list[-1]:
            return "NO"
        else:
            bracket_list = bracket_list[:-1]
    return "YES" if len(bracket_list) == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
