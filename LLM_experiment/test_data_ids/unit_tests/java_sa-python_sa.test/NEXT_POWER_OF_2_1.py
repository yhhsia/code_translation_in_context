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
    p = 1
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( p < n ) :
        p <<= 1
    return p ;


def f_filled ( n ): return (1 << ( n.bit_length() or 1 ) ) if (n and (n & (n-1)) == 0) else (1 << (n.bit_length() or 1)).__int__() if n > 0 else 0
INDENTwhile ( n > p ):p <<= 1
return pDEDENT

if __name__ == '__main__':
    param = [
    (8,),
    (79,),
    (31,),
    (63,),
    (18,),
    (2,),
    (6,),
    (85,),
    (29,),
    (8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))