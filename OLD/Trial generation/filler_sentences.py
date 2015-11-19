# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:56:25 2015

@author: moramaldonado
"""

import random
from functions import *


def filler_creation(group, SHAPE, CONDITION, SET_COLOR1, SET_COLOR2):

#I choose the colors for the fillers and the filler pictures
    COLOR1 = random.choice(SET_COLOR1)
    COLOR2 = random.choice(SET_COLOR2)
    
# differences between groups regarding the filler properties
    if group=='A':
        COLOR2 = ''
        PREDICATE_FILLER_1 = SHAPE
        PREDICATE_FILLER_2 = SHAPE
        COLOR = COLOR1
        COLOR_FALSE = looking_false_color(COLOR1,SET_COLOR1)

    else:
        PREDICATE_FILLER_1 = 'circles'
        PREDICATE_FILLER_2 = 'squares'
        COLOR = COLOR2
        COLOR_FALSE = looking_false_color(COLOR2,SET_COLOR2)
       
    if CONDITION =='Env-F':
        
        filler1 = 'There are ' + COLOR + ' '+PREDICATE_FILLER_1+'.'
        f1 = 'FillerT'
        filler2 = 'There are ' + COLOR + ' '+PREDICATE_FILLER_2+'.'
        f2 = 'FillerT'        

    if CONDITION =='Env-T':
        
        filler1 = 'There are ' + COLOR_FALSE + ' '+PREDICATE_FILLER_1+'.'
        f1 = 'FillerF'
        filler2 = 'There are ' + COLOR_FALSE + ' '+PREDICATE_FILLER_2+'.'
        f2 = 'FillerF'        
    
    if CONDITION =='Target1':
        filler1 = 'There are ' + COLOR + ' '+PREDICATE_FILLER_1+'.'
        f1 = 'FillerT'
        filler2 = 'There are ' + COLOR_FALSE + ' '+PREDICATE_FILLER_2+'.'
        f2 = 'FillerF'   
        
    if CONDITION =='Target2':
        filler1 = 'There are ' + COLOR + ' '+PREDICATE_FILLER_1+'.'
        f1 = 'FillerT'
        filler2 = 'There are ' + COLOR_FALSE + ' '+PREDICATE_FILLER_2+'.'
        f2 = 'FillerF'

    return filler1, filler2, f1, f2, COLOR1, COLOR2

