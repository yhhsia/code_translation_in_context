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
    count = 0
    if ( n and ( not ( n & ( n - 1 ) ) ) ) :
        while ( n > 1 ) :
            n >>= 1
            count += 1
        if ( count % 2 == 0 ) :
            return True
        else :
            return False


def f_filled ( n ):count = 0x = n & ( n - 1 )if n > 0 and x == 0:indentwhile n > 1:n >>= 1count += 1DEDENTreturn ( count % 2 == 0 )
#ENDOFFUNCTION#LastDEDENTgoeshere```Note:

if __name__ == '__main__':
    param = [
    (1,),
    (4,),
    (64,),
    (-64,),
    (128,),
    (1024,),
    (45,),
    (33,),
    (66,),
    (74,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))