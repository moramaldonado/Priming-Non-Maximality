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
    black,grey,white,colors,shapes,objects,letters,condition, path_in, path_out = variables_experiment()
    shapes_by_shapes(path_in,condition,colors,objects,shapes)
    letter_with_connections(path_in,condition,colors,letters,shapes)
    random_letters(path_in,colors,letters)
    images_A(colors, shapes,condition,objects,path_in, path_out)
    images_B(colors, shapes,letters,condition,path_in, path_out)
    
finally:
    pygame.quit()
