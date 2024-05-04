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
def f_gold ( num ) :
    if num < 0 :
        return f_gold ( - num )
    if ( num == 0 or num == 7 ) :
        return True
    if ( num < 10 ) :
        return False
    return f_gold ( num / 10 - 2 * ( num - num / 10 * 10 ) )


def f_filled(num): INDENT if num < 0: num = -numif num in {0, 7}: return 1if num < 10: return 0return f_filled(num // 10 - 2 * (num % 10))DEDENT NEWLINE#Note:Pythondoesnotsupportmultiplereturnstatementsinasinglefunctionlike

if __name__ == '__main__':
    param = [
    (0,),
    (-21,),
    (7,),
    (63,),
    (84,),
    (73,),
    (81,),
    (-10,),
    (47,),
    (23,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))