#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n): 
    recipant = 5
    liked = []
    for i in range(n):
        n = recipant//2
        l = n * 3
        liked.append(n)
        recipant = l
    return sum(liked)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



