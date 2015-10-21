# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:58:46 2015

@author: moramaldonado
"""

import random



def group_ordering(group,PREDICATE_TYPE, SHAPE, SET_COLOR1, SET_COLOR2):
    PREDICATE_D1 = 'D1'
    PREDICATE_D2 = 'D2'
    PREDICATE_C1 = 'C1'
    PREDICATE_C2 = 'C2'
   
    COLOR1 = random.choice(SET_COLOR1)
    COLOR2 = random.choice(SET_COLOR2)
  

    if group=='A':
        COLOR2 = ''
        if PREDICATE_TYPE == 'C':
                PREDICATE_D1 = random.choice(['D1','D2'])
                PREDICATE_D2 = random.choice(['D1','D2'])

        if PREDICATE_TYPE == 'D':
                PREDICATE_C1 = random.choice(['C1','C2'])
                PREDICATE_C2 = random.choice(['C1','C2'])



    return COLOR1, COLOR2, PREDICATE_C1, PREDICATE_C2, PREDICATE_D1, PREDICATE_D2
