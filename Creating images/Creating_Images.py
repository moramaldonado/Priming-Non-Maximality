import pygame
from pygame.locals import *
import os
import random

W=150
H=200


black=[0, 0, 0]
grey = [190,190,190]
  
#loading shapes from the files.. 
os.chdir("/Users/moramaldonado/Dropbox/2015-PhD/Priming NonMaximality/Creating images/Shapes")
#shapes_S={}
#shapes_S['dot']

shapes = {}
objects = {}
shapes['dots_red']= pygame.image.load('dot-red.png') 
shapes['dots_green']= pygame.image.load('dot-green.png')
shapes['dots_black']= pygame.image.load('dot-black.png')
shapes['crosses_red']= pygame.image.load('cross-red.png') 
shapes['crosses_black']= pygame.image.load('cross-black.png')
shapes['crosses_green']= pygame.image.load('cross-green.png')

objects['A_black'] = pygame.image.load('A-black.png')
objects['S_blue'] = pygame.image.load('S-blue.png')
objects['B_red'] = pygame.image.load('B-red.png')


coll_predicate=['triangle','circle']
dist_predicate = ['D1','D2']


m = pygame.transform.scale(shapes['dots_red'], (10, 10))

#some coordenates

x= (m.get_width())/2
y= (m.get_height())/2


#divide the screen in 4 points at the same distance
C1 = 37 - x
C2 = 112 - x
C3 = 75 - x

E1 = 75 - y 
E2 = 125 - y



try:
           
    pygame.init()
    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    os.chdir("/Users/moramaldonado/Dropbox/2015-PhD/Priming NonMaximality/Images")



# target x target


    
    m1 = shapes['dots_red']
    m1 = pygame.transform.scale(m1, (10, 10))

    m2 = shapes['crosses_green']
    m2 = pygame.transform.scale(m2, (10, 10))

    X1= 37
    X2= 112

    Y1= 50
    Y2= 150
    
    n = objects['A_black']
    n = pygame.transform.scale(n, (20, 20))
    X = 10
    Y = 10
    radio = 20

    window.fill([255,255,255])

    pygame.draw.line(window, [0,0,0], (5,100) , (145,100) , 3)
    window.blit(n, [X1-X,Y1-X])
    
    p1 = [X1-x+radio/2, Y1-y+radio]
    p2 = [X1-x-radio/2, Y1-y+radio]
    
    p3 = [X1-x+radio, Y1-y-radio/3]
    p4 = [X1-x-radio, Y1-y-radio/3]
    
    p5 = [X1-x, Y1-y-radio]


    window.blit(m1, p4)
    window.blit(m1, p1)
    window.blit(m1, p2)
    window.blit(m1, p3)
    window.blit(m1, p5)

    window.blit(n, [X2-X,Y2-X])

    
    p1 = [X2-x+radio, Y2-y+radio/2]
    p2 = [X2-x-radio, Y2-y+radio/2]
    
    p6 = [X2-x, Y2-y+radio]
    
    p3 = [X2-x+radio, Y2-y-radio/2]
    p4 = [X2-x-radio, Y2-y-radio/2]
    
    p5 = [X2-x, Y2-y-radio]
   
    
    window.blit(m2, p4)
    window.blit(m2, p1)
    window.blit(m2, p2)
    window.blit(m2, p3)
    window.blit(m2, p5)
    window.blit(m2, p6)




    
    n = pygame.transform.scale(n, (30, 30))
    X = 15
    Y = 15
    radio = 35
    



    window.blit(n, [X2-X,Y1-Y])
    
    p1 = [X2-x, Y1+radio-y]
    p2 = [X2-x, Y1-radio-y]
    p3 = [X2+radio-x-5, Y1-y]
    p4 = [X2-radio-x+5, Y1-y]


    p5 = [X2-x+radio/2+5, Y1+radio/2-y]
    p6 = [X2-x+radio/2+5, Y1-radio/2-y]
    
    p7 = [X2-radio/2-x-5, Y1-y+radio/2]
    p8 = [X2-radio/2-x-5, Y1-y-radio/2]

    p9 = [X2-x-8, Y1-y-radio/2-10]
    p10 = [X2+8-x, Y1-y-radio/2-10]

    p11 = [X2-x-8, Y1-y+radio/2+10]
    p12 = [X2+8-x, Y1-y+radio/2+10]

    window.blit(m1, p4)

    window.blit(m1, p3)

    window.blit(m1, p5)
    window.blit(m1, p6)
    window.blit(m1, p7)
    window.blit(m1, p8)
    
    window.blit(m1, p9)
    window.blit(m1, p10)
    
    window.blit(m1, p11)
    window.blit(m1, p12)






    
    
    
    p1 = [X1-x, Y2+radio-y]
    p2 = [X1-x, Y2-radio-y]
    p3 = [X1+radio-x-5, Y2-y]
    p4 = [X1-radio-x+5, Y2-y]
    p5 = [X1-x+radio/2+5, Y2+radio/2-y]
    p6 = [X1-x+radio/2+5, Y2-radio/2-y]
    
    p7 = [X1-radio/2-x-5, Y2-y+radio/2]
    p8 = [X1-radio/2-x-5, Y2-y-radio/2]

    p9 = [X1-x-8, Y2-y-radio/2-10]
    p10 = [X1+8-x, Y2-y-radio/2-10]

    p11 = [X1-x-8, Y2-y+radio/2+10]
    p12 = [X1+8-x, Y2-y+radio/2+10]


    
    pygame.draw.line(window, black, (X1,Y2), (X1-radio-x+5, Y2) , 2)
    window.blit(m2, p4)
    
    pygame.draw.line(window, black, (X1,Y2), (X1+radio-x-5, Y2), 2)
    window.blit(m2, p3)

    pygame.draw.line(window, black, (X1,Y2), (X1+radio/2+5, Y2+radio/2), 2)
    window.blit(m2, p5)
    
    pygame.draw.line(window, black, (X1,Y2), (X1-x+radio/2+5, Y2-radio/2), 2)
    window.blit(m2, p6)

    window.blit(m2, p7)
    window.blit(m2, p8)
    
    window.blit(m2, p9)
    window.blit(m2, p10)
    
    window.blit(m2, p11)
    window.blit(m2, p12)

    window.blit(n, [X1-X,Y2-Y])

    
    imgname = 'trial.png'
                        
    pygame.image.save(window, imgname)
    pygame.display.flip()

 


finally:
    pygame.quit()

    




    
# true x false

# false x true






