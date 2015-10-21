# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:01:48 2015

@author: moramaldonado
"""

import random

def looking_false_color(COLOR, SET_COLORS):
    COLOR_FALSE = random.choice(SET_COLORS)
    while COLOR == COLOR_FALSE:
        COLOR_FALSE = random.choice(SET_COLORS)
    return COLOR_FALSE