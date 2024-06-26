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
def f_gold ( n ) :
    sm = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            sm = sm + i * j
    return sm


def f_filled(n): sum = 0; for i in range(1, n+1): for j in range(i, n+1): sum += i*j; INDENT NEWLINE return sum; DEDENT DEDENT

if __name__ == '__main__':
    param = [
    (21,),
    (32,),
    (16,),
    (38,),
    (9,),
    (3,),
    (5,),
    (46,),
    (45,),
    (87,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))