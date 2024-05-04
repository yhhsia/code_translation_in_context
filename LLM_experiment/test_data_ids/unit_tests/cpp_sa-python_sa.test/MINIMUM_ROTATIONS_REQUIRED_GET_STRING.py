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
def f_gold ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : n ]
        if ( str == substring ) :
            return i
    return n


def f_filled(str): return len(str) if str in (str+str)[1:] else next((i for i in range(1,len(str)+1) if str==str[i:]),None)[]

if __name__ == '__main__':
    param = [
    ('vdevdNdQSopPtj',),
    ('5',),
    ('100010101011',),
    ('tlDOvJHAyMllu',),
    ('06',),
    ('101',),
    ('DYgtU',),
    ('4',),
    ('00',),
    ('Dt',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))