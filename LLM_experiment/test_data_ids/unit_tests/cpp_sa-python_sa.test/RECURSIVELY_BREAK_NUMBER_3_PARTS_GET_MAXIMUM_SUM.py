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
    if ( n == 0 or n == 1 ) :
        return n
    return max ( ( f_gold ( n // 2 ) + f_gold ( n // 3 ) + f_gold ( n // 4 ) ) , n )


def f_filled( n ): return n if n in ( 0, 1 ) else max( ( f_filled( n // 2 ) + f_filled( n // 3 ) + f_filled( n // 4 ) ), n )NEWLINE#Testcaseprint(f_filled(10))DEDENT

if __name__ == '__main__':
    param = [
    (39,),
    (79,),
    (7,),
    (76,),
    (48,),
    (18,),
    (58,),
    (17,),
    (36,),
    (5,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))