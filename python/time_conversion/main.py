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
    print(s)
    time, period = s[:8], s[8:]
    print(time, period)
    hh, mm, ss = map(int, time.split(':'))
    if period == 'PM' and hh != 12:
        hh +=12
    if period == 'AM' and hh == 12:
        hh = 0
    return f'{hh:02d}:{mm:02d}:{ss:02d}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
