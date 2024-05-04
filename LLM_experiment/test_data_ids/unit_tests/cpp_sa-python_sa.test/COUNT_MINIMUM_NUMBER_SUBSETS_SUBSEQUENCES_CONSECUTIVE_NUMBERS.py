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
def f_gold(arr, n):
    x = sorted(arr)
    count = 1
    for i in range(0, n - 1):
        if (x[i] + 1 != x[i + 1]):
            count = count + 1
    return count


def f_filled(arr, n):= { import math arr.sort() INDENT count = 1 for i in range(n-1): if arr[i] + 1 != arr[i+1]: count += 1 DEDENT return count} NEWLINE#Note:Pythondoesnothavebuilt-insupportforsortingarrayslikeC++,#soIimportedthemathmoduletouse

if __name__ == '__main__':
    param = [
        ([3, 7, 7, 11, 14, 14, 14, 16, 17, 17, 21, 22, 24, 27, 27, 27, 31, 33, 35, 36, 36, 37, 38, 43,
          45, 49, 52, 54, 57, 59, 59, 60, 67, 73, 74, 74, 74, 75, 75, 79, 83, 87, 90, 93, 97], 42,),
        ([-28, 72, 60, 62, 40, 64, 50, -36, -24, 40, -6, 78, -80, -82, 2, -30,
          70, 94, -2, -30, 92, 12, -46, 32, -96, -2, 36, -40, -42, 66, 98], 24,),
        ([1, 1], 1,),
        ([96, 89, 24, 28, 70, 78, 78, 35, 98, 65, 18, 81, 35, 91, 33, 88, 69, 52, 66, 17, 73, 79, 30, 33,
          78, 60, 42, 8, 36, 6, 47, 87, 8, 98, 9, 77, 78, 24, 86, 91, 13, 79, 50, 85, 3, 7, 61, 94, 86], 26,),
        ([-92, -92, -90, -84, -78, -66, -60, -60, -46, -42, -38, -32, -24, -20, -18, -16, -14, -10, 0, 4, 6,
          12, 24, 32, 34, 44, 48, 50, 50, 64, 66, 68, 80, 84, 86, 86, 88, 90, 90, 90, 92, 94, 96, 98, 98], 42,),
        ([0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
          1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], 27,),
        ([8, 12, 13, 14, 16, 20, 20, 21, 23, 23, 24, 27, 29, 29, 29, 29, 35, 35, 38, 39, 40, 46, 50, 52,
          60, 62, 62, 65, 65, 65, 70, 71, 72, 73, 75, 76, 80, 81, 82, 83, 85, 91, 95, 97, 98, 98], 29,),
        ([-84, 92, 70, -46, 26, -94, -82, -26, -90, -62, 52, 62, -58, 44, -14, -6, 58, 2, 10, 76, -34, 42, -
          26, 80, 26, 32, -82, 38, 2, 72, 68, 44, 24, 84, -32, 54, -96, -8, 36, 80, -82, 32, 98, -68], 25,),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 21,),
        ([64, 10, 6, 3, 67, 95, 72, 96, 72, 30, 99, 21, 46, 23, 48, 38, 48, 50, 53, 91, 59, 58, 27, 95,
          63, 20, 27, 22, 58, 3, 11, 75, 77, 64, 46, 1, 67, 79, 6, 46, 57, 79, 49, 83, 21, 36, 44], 46,)
    ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
