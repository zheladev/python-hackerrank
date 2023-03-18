#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def cipher(k):
    lc_int_diff = 32
    uc_a_int_value = 65
    letters = 26

    def _do_cipher(s):
        s = ord(s)
        if s < 65 or s > 90 and s < 97 or s > 122:
            return chr(s)
        mod = uc_a_int_value + lc_int_diff * int(s >= 97)
        sp = (s - mod + k) % letters
        return chr(sp + mod)
    return _do_cipher


def caesarCipher(s, k):
    sprime = list(map(cipher(k), list(s)))
    print(sprime)
    # Write your code here
    return "".join(sprime)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
