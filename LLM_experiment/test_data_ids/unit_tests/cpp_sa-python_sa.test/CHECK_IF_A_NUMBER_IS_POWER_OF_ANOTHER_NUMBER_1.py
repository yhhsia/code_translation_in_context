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
import math

def f_gold ( x , y ) :
    res1 = math.log ( y ) / math.log ( x ) ;
    res2 = math.log ( y ) / math.log ( x ) ;
    return 1 if ( res1 == res2 ) else 0 ;


def f_filled ( x , y ): return ( pow ( x , y ) == x ** y ) NEWLINEif \( __name__ == "__main__" \): INDENT x = 2 y = 3 print ( f_filled ( x , y ) ) DEDENT NEWLINE

if __name__ == '__main__':
    param = [
    (57,1,),
    (3,9,),
    (10,101,),
    (10,10000,),
    (6,46656,),
    (2,2048,),
    (2,40,),
    (20,79,),
    (96,98,),
    (25,5,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))