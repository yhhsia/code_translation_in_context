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
def f_gold ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1


def f_filled ( s ): sum = 0 ; for n in range ( 1 , 50001 ): sum += n * n ; if sum == s : return n ; NEWLINE return - 1 #INDENTforninrange(1,50001):#DEDENTsum+=n*n#NEWLINE#DEDENTifsum==s:#DEDENT#NEWLINEreturnn#D

if __name__ == '__main__':
    param = [
    (1,),
    (5,),
    (14,),
    (140,),
    (204,),
    (3,),
    (506,),
    (42,),
    (4,),
    (87,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))