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
    for i in range ( 0 , len ( str ) ) :
        if ( str [ i ].istitle ( ) ) :
            return str [ i ]
    return 0


def f_filled(str):=sum(i for i,c in enumerate(str) if c.isupper())[0],int(ord('A')) if f_filled<int('A') else ord(f_filled)NEWLINE#Note:PythondoesnothaveadirectequivalenttotheC++chardatatype.TheabovePythoncodeusesastringandconvertsthef_filledcharactertoanintegerifitisuppercase.IftheoriginalC++codeuses

if __name__ == '__main__':
    param = [
    ('pH',),
    ('96544000',),
    ('000010000',),
    ('ujqpx',),
    ('20684847994',),
    ('111',),
    ('rclkv',),
    ('45173693434',),
    ('11111011001101',),
    ('f',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))