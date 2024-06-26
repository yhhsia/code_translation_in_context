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
    if ( n == 0 ) :
        return "0" ;
    bin = "" ;
    while ( n > 0 ) :
        if ( n & 1 == 0 ) :
            bin = '0' + bin ;
        else :
            bin = '1' + bin ;
        n = n >> 1 ;
    return bin ;


def f_filled(n): return "0" if n==0 else "".join(str(int(n%2)) for n in (bin(int(n))[2:][::-1])) + "\n"

if __name__ == '__main__':
    param = [
    (35,),
    (17,),
    (8,),
    (99,),
    (57,),
    (39,),
    (99,),
    (14,),
    (22,),
    (7,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))