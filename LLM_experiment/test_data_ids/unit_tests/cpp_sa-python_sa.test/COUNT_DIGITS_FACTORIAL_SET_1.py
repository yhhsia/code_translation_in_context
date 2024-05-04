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

def f_gold ( n ) :
    if ( n < 0 ) :
        return 0 ;
    if ( n <= 1 ) :
        return 1 ;
    digits = 0 ;
    for i in range ( 2 , n + 1 ) :
        digits += math.log10 ( i ) ;
    return math.floor ( digits ) + 1 ;


def f_filled(n):#NEWLINEifn<0:#INDENTreturn0#DEDENTifn<=1:return1#DEDENTdigits=0#NEWLINEforiinrange(2,n+1):digits+=log10(i)#DEDENTreturnint(digits)+1#NEWLINE#Note:Pythondoesnothavealog1

if __name__ == '__main__':
    param = [
    (66,),
    (7,),
    (55,),
    (37,),
    (76,),
    (16,),
    (17,),
    (95,),
    (71,),
    (90,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))