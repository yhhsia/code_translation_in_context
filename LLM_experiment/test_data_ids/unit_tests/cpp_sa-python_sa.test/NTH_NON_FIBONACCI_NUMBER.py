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
    prevPrev = 1
    prev = 2
    curr = 3
    while n > 0 :
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n


def f_filled ( n ): prevPrev, prev, curr = 1, 2, 3while n > 0: prevPrev, prev, curr = prev, curr, prevPrev + prevn += curr - prevreturn prev + nNEWLINE#EndofPythoncode.DEDENT(twice)togobacktotheoriginalindentationlevel.DEDENTDEDENT

if __name__ == '__main__':
    param = [
    (76,),
    (91,),
    (62,),
    (65,),
    (83,),
    (57,),
    (76,),
    (6,),
    (2,),
    (86,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))