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
    N = 10
    count = 1
    for i in range ( 1 , n + 1 ) :
        count = int ( count * ( N + i - 1 ) )
        count = int ( count / i )
    return count


def f_filled ( n ): N, count = 10, 1 :for i in range ( 1, n + 1 ): count *= ( N + i - 1 ) ; N += 1 ; count /= ireturn count
Here's the Python code equivalent to the given C++ code.Note that the C++ code seems to have a mistake in the calculation of N, as it should be

if __name__ == '__main__':
    param = [
    (40,),
    (11,),
    (94,),
    (73,),
    (6,),
    (73,),
    (58,),
    (40,),
    (64,),
    (66,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))