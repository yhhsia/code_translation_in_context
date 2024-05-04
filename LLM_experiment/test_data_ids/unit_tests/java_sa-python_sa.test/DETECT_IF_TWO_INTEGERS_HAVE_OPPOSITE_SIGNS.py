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
def f_gold ( x , y ) :
    return ( ( x ^ y ) < 0 ) ;


def f_filled(x, y): return (x ^ y) < 0
#Or,ifyoupreferamorePythonicsyntax:defopposite_signs(x,y):returnx*y<0
#Or,ifyouwanttokeeptheoriginalC++logic:deff_filled(x,y):return(xify<0else-x)*(yif

if __name__ == '__main__':
    param = [
    (59,-99,),
    (-20,-21,),
    (-100,79,),
    (54,-49,),
    (-16,16,),
    (-23,-68,),
    (93,37,),
    (24,-61,),
    (-8,69,),
    (29,10,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))