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
def f_gold ( a , b , mod ) :
    res = 0 ;
    a = a % mod ;
    while ( b ) :
        if ( b & 1 ) :
            res = ( res + a ) % mod ;
        a = ( 2 * a ) % mod ;
        b >>= 1 ;
    return res ;


def f_filled(a, b, mod): INDENT res = 0 NEWLINE a %= mod NEWLINE while b: NEWLINE if b & 1: res = (res + a) % mod NEWLINE a = (2 * a) % mod NEWLINE b >>= 1 NEWLINE DEDENT return res NEWLINE NEWLINE

if __name__ == '__main__':
    param = [
    (60,24,58,),
    (46,43,29,),
    (4,50,71,),
    (67,1,66,),
    (93,35,73,),
    (89,97,8,),
    (8,78,55,),
    (53,73,22,),
    (96,92,83,),
    (38,64,83,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))