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
    if ( n == 0 or n == 9 ) :
        return True
    if ( n < 9 ) :
        return False
    return f_gold ( ( int ) ( n >> 3 ) - ( int ) ( n & 7 ) )


def f_filled ( n ): return bool(n in {0, 9} or (n > 3 and not f_filled(n >> 3 - n & 7)))
#Note:Pythondoesnothaveabooleantype,butitautomaticallyconvertsvaluestoboolwhenneeded.Inthiscase,weusethebuilt-inboolconstructortocreateabooleanvaluefromaPythonobject.

if __name__ == '__main__':
    param = [
    (96,),
    (85,),
    (54,),
    (14,),
    (47,),
    (11,),
    (49,),
    (99,),
    (28,),
    (82,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))