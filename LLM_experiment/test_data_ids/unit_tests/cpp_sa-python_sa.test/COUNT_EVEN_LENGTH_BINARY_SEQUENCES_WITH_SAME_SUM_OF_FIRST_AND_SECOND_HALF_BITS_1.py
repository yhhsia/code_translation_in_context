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
    nCr = 1
    res = 1
    for r in range ( 1 , n + 1 ) :
        nCr = ( nCr * ( n + 1 - r ) ) / r ;
        res += nCr * nCr ;
    return res ;


def f_filled(n): nCr, res = 1, 1for r in range(1, n+1): nCr = nCr * (n + 1 - r) // r res += nCr * nCrreturn resNEWLINE#EndofPythoncode.

if __name__ == '__main__':
    param = [
    (52,),
    (75,),
    (25,),
    (80,),
    (18,),
    (17,),
    (33,),
    (8,),
    (99,),
    (8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))