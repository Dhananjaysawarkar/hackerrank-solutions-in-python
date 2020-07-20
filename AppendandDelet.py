#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if len(s)<len(t):
        return "No"
    elif (len(s)+len(t) < k):
        return "Yes"

    commonlength = 0
    for i in range(0,min(len(s),len(t)),1):
        if s[i]==t[i]:
            commonlength += 1
        else:
            break
    a = len(s)-(commonlength)
    b = len(t)-(commonlength)
    if (a+b)<= k:
        return "Yes"
    return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
