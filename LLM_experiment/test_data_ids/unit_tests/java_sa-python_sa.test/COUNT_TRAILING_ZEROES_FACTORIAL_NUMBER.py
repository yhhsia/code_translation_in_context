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
    count = 0
    i = 5
    while ( n / i >= 1 ) :
        count += int ( n / i )
        i *= 5
    return int ( count )


def f_filled(n): return sum(int(n / 5) for _ in range(n > 0 and n % 5 == 0, 0, 5)) #
#INDENTdefmain():print(f_filled(10))print(f_filled(25))print(f_filled(3

if __name__ == '__main__':
    param = [
    (9,),
    (43,),
    (50,),
    (32,),
    (37,),
    (51,),
    (33,),
    (49,),
    (1,),
    (75,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))