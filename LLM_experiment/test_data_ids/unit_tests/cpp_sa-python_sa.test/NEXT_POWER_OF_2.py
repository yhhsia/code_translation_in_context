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
    count = 0 ;
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( n != 0 ) :
        n >>= 1
        count += 1
    return 1 << count ;


def f_filled(n): return 1 << int(bin(n.bit_length())[2:].count('1')) if n else 0 #NEWLINEINDENTdefmain():a=10;print(f_filled(a))#Prints:16#DEDENT#NEWLINE```

if __name__ == '__main__':
    param = [
    (74,),
    (70,),
    (85,),
    (78,),
    (71,),
    (32,),
    (97,),
    (90,),
    (64,),
    (48,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))