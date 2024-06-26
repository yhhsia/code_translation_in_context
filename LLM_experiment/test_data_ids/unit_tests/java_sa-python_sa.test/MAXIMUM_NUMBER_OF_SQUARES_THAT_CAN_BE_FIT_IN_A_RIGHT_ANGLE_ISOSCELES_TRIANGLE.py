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
def f_gold ( b , m ) :
    return ( b / m - 1 ) * ( b / m ) / 2


def f_filled ( b , m ): return (int)(b / m ** 2 / 2) #
#INDENTif(b%(m*m)==0):returnint(b/(m**2))*int(b/(m**2))*int(b/(m**2))+f_filled(b%(m*m),m)#D

if __name__ == '__main__':
    param = [
    (40,74,),
    (38,35,),
    (47,71,),
    (52,29,),
    (21,9,),
    (50,33,),
    (8,82,),
    (56,80,),
    (93,5,),
    (21,90,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))