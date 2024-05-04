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
def f_gold ( N ) :
    dp = [ 0 for i in range ( N ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 2
    i = 1
    while dp [ i ] <= N :
        i = i + 1
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ]
    return ( i - 1 )


def f_filled(N):=sum(dp[:N+1])//2 if [1,1]+[1,1,1,...,(N-1),1] else sum(dp[:N])//2 if [1,1,1,...,(N-1)]dp = [1, 1] + [0] * (N - 2)return len(dp) if sum(dp) > N

if __name__ == '__main__':
    param = [
    (73,),
    (28,),
    (33,),
    (23,),
    (84,),
    (31,),
    (48,),
    (46,),
    (45,),
    (90,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))