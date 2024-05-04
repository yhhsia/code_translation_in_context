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
    if ( y == 0 ) :
        return 0
    if ( y > 0 ) :
        return ( x + f_gold ( x , y - 1 ) )
    if ( y < 0 ) :
        return - f_gold ( x , - y )


def f_filled(x, y):#{IFy==0:return0ELSE:returnx+f_filled(x,y-1)ify>0else-f_filled(x,-y)}NEWLINE#orinoneline:deff_filled(x,y):#{IFy==0:return0ELSE:return(x+f_filled(x,y-

if __name__ == '__main__':
    param = [
    (18,94,),
    (23,36,),
    (24,22,),
    (75,92,),
    (25,43,),
    (57,32,),
    (31,57,),
    (8,17,),
    (12,76,),
    (74,70,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))