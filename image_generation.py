import pygame
from pygame.locals import *
import os
import random
import sys
sys.path.insert(0, '/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/Functions')

from variables import *
from creative_functions import *
from functions import *

try:
    pygame.init()
    black,grey,white,colors,shapes,objects,letters,truth_value, conditions, path_in, path_out, mypath, study, group, predicates = variables()
    #shapes_by_shapes(path_in,truth_value,colors,objects,shapes)
    #images_A(colors, shapes,truth_value,objects,path_in, path_out)
    images_B(colors, shapes,letters,truth_value,path_in, path_out)
    
finally:
    pygame.quit()
