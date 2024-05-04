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
def f_gold ( string ) :
    l = 0
    h = len ( string ) - 1
    while h > l :
        l += 1
        h -= 1
        if string [ l - 1 ] != string [ h + 1 ] :
            return False
    return True


def f_filled ( s ): return all ( s [ i ] == s [- i - 1] for i in range ( len ( s ) // 2 ) ) NEWLINEif **name** == '**main**': print ( f_filled ( "racecar" ) ) DEDENT#orforPython3.xprint(f_filled("racecar"))

if __name__ == '__main__':
    param = [
    ('aadaa',),
    ('2674377254',),
    ('11',),
    ('0011000',),
    ('26382426486138',),
    ('111010111010',),
    ('abccba',),
    ('5191',),
    ('1110101101',),
    ('abcdecbe',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))