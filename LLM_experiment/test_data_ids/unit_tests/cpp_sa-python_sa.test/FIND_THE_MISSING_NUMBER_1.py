import numpy as np 
import math
from math import *
import collections
from collections import *
import heapq
import itertools
import random
import sys

# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , n ) :
    i , total = 0 , 1
    for i in range ( 2 , n + 2 ) :
        total += i
        total -= a [ i - 2 ]
    return total


def f_filled(a, n): total = 1 INDENT for i in range(2, n+1): total += i - a[i-2] DEDENT return total NEWLINE

if __name__ == '__main__':
    param = [
    ([13, 27, 46, 59, 62, 82, 92],6,),
    ([22, 86, -64, -20, -56, -16, 86, 42, 72, -90, 10, 42, 56, 8, 50, 24, -34, 0, -78, 64, 18, 20, -84, -22, 90, -20, 86, 26, -54, 0, 90, -48, 4, 88, 18, -64, -22, -74, 48, -36, -86, -24, 88, -64, 68, 62, 92],38,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,),
    ([55, 89, 56, 85, 26, 4, 91, 91, 3, 77, 63, 59, 76, 90, 1, 94, 44, 70, 8, 54, 3, 91, 29, 95, 28, 75, 20],22,),
    ([-94, -84, -80, -78, -66, -62, -54, -52, -26, -8, -8, -6, 4, 4, 8, 14, 26, 58, 60, 62, 62, 76, 78, 86, 92],18,),
    ([1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],25,),
    ([1, 2, 7, 7, 9, 14, 23, 29, 31, 31, 35, 35, 38, 41, 44, 49, 49, 50, 51, 54, 55, 56, 57, 63, 67, 69, 73, 79, 79, 80, 86, 88, 93],24,),
    ([78, -48, 16, 22, -16, 34, 56, -20, -62, -82, -74, -40, 20, -24, -46, 64, 66, -76, 58, -84, 96, 76, 86, -32, 46],12,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([73, 76, 25, 59, 40, 85, 90, 38, 13, 97, 93, 99, 45, 7],12,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))