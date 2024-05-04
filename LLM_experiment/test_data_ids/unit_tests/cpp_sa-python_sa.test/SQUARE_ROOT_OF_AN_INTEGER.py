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
def f_gold ( x ) :
    if ( x == 0 or x == 1 ) :
        return x
    i = 1 ; result = 1
    while ( result <= x ) :
        i += 1
        result = i * i
    return i - 1


def f_filled ( x : int ) :#INDENTifxin{0,1}:returnxi:int=1result:int=1whileresult<=x:i+=1result=i*i#DEDENTreturni-1#NEWLINE#LastDEDENTshouldbehere```PleasenotethatPythondoesnothaveanequivalent

if __name__ == '__main__':
    param = [
    (89,),
    (11,),
    (14,),
    (92,),
    (76,),
    (63,),
    (51,),
    (16,),
    (83,),
    (66,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))