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







##
##
##
##    for key in shapes:
##        m = shapes[key]
##        m = pygame.transform.scale(m, (10, 10))
##        #randomly choose sides for X1 and X2
##        X1 = random.choice([C1,C2])
##        if X1==C2:
##            X2 = C1
##        else:
##            X2 = C2
##
##        #randomly choose sides for X1 and X2
##        Y1 = random.choice([E1,E2])
##            
##        if Y1==E2:
##            Y2 = E1
##            Z1 = E2 + 15
##            Y1 = Z1 + 10
##            Z2 = E1 - 10
##
##        else:
##            Y2 = E2
##            Z2 = Y2 + 15
##            Z1 = Y1 - 10 
##
##        #type B
##            
##
##        for key1 in objects:
##            n = pygame.transform.scale(objects[key1], (20, 20))
##
##            if key1 == 'C1_black' or key1 == 'C1_blue' or key1 == 'C1_yellow':
##                D = 'D1'
##            else:
##                D = 'D2'
##
##            p1 = [X1-5, Y1+25-5]
##            p2 = [X1-5, Y1-25-5]
##            p3 = [X1+25-5, Y1-5]
##            p4 = [X1-25-5, Y1-5]
##
##            p5 = [X1+18-5, Y1+15-5]
##            p6 = [X1-18-5, Y1+15-5]
##            p7 = [X1+18-5, Y1-15-5]
##            p8 = [X1-18-5, Y1-15-5]
##
##            b1 = [X2-5, Y1+25-5]
##            b2 = [X2-5, Y1-25-5]
##            b3 = [X2+25-5, Y1-5]
##            b4 = [X2-25-5, Y1-5]
##
##            b5 = [X2+18-5, Y1+15-5]
##            b6 = [X2-18-5, Y1+15-5]
##            b7 = [X2+18-5, Y1-15-5]
##            b8 = [X2-18-5, Y1-15-5]
##
##            
##
##            # 4 dots
##            window.fill([255,255,255])
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)
##
##            window.blit(m, p1)
##            window.blit(m, p2)
##            window.blit(m, p3)
##            window.blit(m, p4)
##
##
##            window.blit(n, [X1-10,Z1])
##            window.blit(n, [X2-10,Z1])
##           
##            window.blit(n, [C3-10,Z2])
##
##            imgname = 'B_6-_'+str(key)+'_'+D+'_'+str(key1)+'.png'
##                        
##            pygame.image.save(window, imgname)
##            pygame.display.flip()
##
##            window.fill([255,255,255])
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)
##
##            window.blit(m, p1)
##            window.blit(m, p2)
##            window.blit(m, p3)
##            window.blit(m, p4)
##
##
##            window.blit(n, [X1-10,Z1])
##            window.blit(n, [X2-10,Z1])
##           
##            window.blit(n, [C3-10,Z2])
##
##            imgname = 'B_8-_'+str(key)+'_'+D+'_'+str(key1)+'.png'
##                        
##            pygame.image.save(window, imgname)
##            pygame.display.flip()
##
##            # 6 dots
##            window.fill([255,255,255])
##
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)
##
##            window.blit(m, p1)
##            window.blit(m, p2)
##            window.blit(m, p5)
##            window.blit(m, p6)
##            window.blit(m, p7)
##            window.blit(m, p8)
##            
##
##            window.blit(n, [X1-10,Z1])
##            window.blit(n, [X2-10,Z1])
##           
##            window.blit(n, [C3-10,Z2])
##
##            imgname = 'B_6_'+str(key)+'_'+D+'_'+str(key1)+'.png'
##                        
##            pygame.image.save(window, imgname)
##            pygame.display.flip()
##
##
##            # 8 dots
##            window.fill([255,255,255])
##
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
##            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)
##
##
##            window.blit(m, p1)
##            window.blit(m, p2)
##            window.blit(m, p3)
##            window.blit(m, p4)
##            
##            window.blit(m, p5)
##            window.blit(m, p6)
##            window.blit(m, p7)
##            window.blit(m, p8)
##            
##
##            window.blit(n, [X1-10,Z1])
##            window.blit(n, [X2-10,Z1])
##           
##            window.blit(n, [C3-10,Z2])



