# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:55:34 2015

@author: moramaldonado
"""

import os
import random
from functions import *


def baseline_sentences(group, SHAPE, COLOR1, COLOR2, CONDITION, SET_COLOR1, SET_COLOR2):

    if group  =='A':

        if CONDITION == 'Env-F':
            COLOR_FALSE=looking_false_color(COLOR1,SET_COLOR1)
            sentence1 = 'The ' +SHAPE+' are '+COLOR_FALSE+'.'

            COLOR_FALSE=looking_false_color(COLOR1,SET_COLOR1)
            sentence2 = 'The ' +SHAPE+' are '+COLOR_FALSE+'.'

        else:
            sentence1 = 'The ' +SHAPE+' are '+COLOR1+'.'
            sentence2 = 'The ' +SHAPE+' are '+COLOR1+'.'            
        
    else:

        if CONDITION == 'Env-F':
            COLOR_FALSE = looking_false_color(COLOR2,SET_COLOR2)
            sentence1 = 'The circles are '+COLOR_FALSE+'.'

            COLOR_FALSE = looking_false_color(COLOR2,SET_COLOR2)
            sentence2 = 'The squares are '+COLOR_FALSE+'.'

        else:
            
            sentence1 = 'The circles are '+COLOR2+'.'
            sentence2 = 'The squares are '+COLOR2+'.'


    return sentence1, sentence2