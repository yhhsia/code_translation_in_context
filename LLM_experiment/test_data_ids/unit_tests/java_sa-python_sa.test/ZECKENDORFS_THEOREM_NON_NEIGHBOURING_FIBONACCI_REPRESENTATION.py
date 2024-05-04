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
    f1 , f2 , f3 = 0 , 1 , 1
    while ( f3 <= n ) :
        f1 = f2 ;
        f2 = f3 ;
        f3 = f1 + f2 ;
    return f2 ;


def f_filled ( n ): fib1, fib2, fib3 = 0, 1, 1 while fib3 <= n: fib1, fib2, fib3 = fib2, fib3, fib1+fib2 return fib2

if __name__ == '__main__':
    param = [
    (54,),
    (71,),
    (64,),
    (71,),
    (96,),
    (43,),
    (70,),
    (94,),
    (95,),
    (69,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))