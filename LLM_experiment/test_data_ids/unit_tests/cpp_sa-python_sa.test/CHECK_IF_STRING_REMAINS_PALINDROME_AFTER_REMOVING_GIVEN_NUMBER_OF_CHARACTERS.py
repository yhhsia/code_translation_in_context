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
def f_gold ( str , n ) :
    l = len ( str )
    if ( l >= n ) :
        return True
    return False


def f_filled\_Possible ( str , n ):return len ( str ) >= nNEWLINE#orinoneline:deff_filled\_Possible(str,n):returnlen(str)>=niflen(str)elseFalse

if __name__ == '__main__':
    param = [
    ('ZCoQhuM',2,),
    ('7437725',53,),
    ('11',30,),
    ('buGlvR',1,),
    ('9',92,),
    ('101101010110',3,),
    ('YguiM',18,),
    ('8198',90,),
    ('11101',71,),
    ('hUInqJXNdbfP',4,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))