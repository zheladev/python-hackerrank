#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    time = s[:-2]
    is_post_meridiem = s[-2:] == "PM"
    hour = int(time[:2])
    if hour == 12:
        hour = hour * int(is_post_meridiem)
    else:
        hour = hour + 12 * int(is_post_meridiem)

    return f"{str(hour).zfill(2)}{time[2:]}"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
