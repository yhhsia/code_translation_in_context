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
    res = 0
    x = 0
    while ( x * x < n ) :
        y = 0
        while ( x * x + y * y < n ) :
            res = res + 1
            y = y + 1
        x = x + 1
    return res


def f_filled ( n ): res = 0 ; for x in range ( 0 , int ( math.sqrt ( n ) ) + 1 ): for y in range ( 0 , int ( math.sqrt ( n ) ) + 1 ): res += 1 ; return res
#Importmathmoduleforsqrtcalculationimportmath#Functiondefinitiondeff_filled(n):INDENTres=

if __name__ == '__main__':
    param = [
    (61,),
    (45,),
    (53,),
    (4,),
    (82,),
    (86,),
    (37,),
    (48,),
    (81,),
    (50,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))