import pygame
from pygame.locals import *
import os
import random

W=150
H=200


black=[0, 0, 0]
grey = [190,190,190]
  
#loading shapes from the files.. 
os.chdir("/Users/moramaldonado/Desktop/Priming NonMaximality/Creating images/Shapes")
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

objects['C2_black'] = pygame.image.load('square-black.png')
objects['C2_blue'] = pygame.image.load('square-blue.png')
objects['C2_yellow'] = pygame.image.load('square-yellow.png')

objects['C1_black'] = pygame.image.load('circle-black.png')
objects['C1_blue'] = pygame.image.load('circle-blue.png')
objects['C1_yellow'] = pygame.image.load('circle-yellow.png')



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

    os.chdir("/Users/moramaldonado/Desktop/Priming NonMaximality/Images")

    for key in shapes:
        m = shapes[key]
        m = pygame.transform.scale(m, (10, 10))
        #randomly choose sides for X1 and X2
        X1 = random.choice([C1,C2])
        if X1==C2:
            X2 = C1
        else:
            X2 = C2

        #randomly choose sides for X1 and X2
        Y1 = random.choice([E1,E2])
            
        if Y1==E2:
            Y2 = E1
            Z1 = E2 + 15
            Y1 = Z1 + 10
            Z2 = E1 - 10

        else:
            Y2 = E2
            Z2 = Y2 + 15
            Z1 = Y1 - 10 

        #type B
            

        for key1 in objects:
            n = pygame.transform.scale(objects[key1], (20, 20))

            if key1 == 'C1_black' or key1 == 'C1_blue' or key1 == 'C1_yellow':
                D = 'D1'
            else:
                D = 'D2'

            p1 = [X1-5, Y1+25-5]
            p2 = [X1-5, Y1-25-5]
            p3 = [X1+25-5, Y1-5]
            p4 = [X1-25-5, Y1-5]

            p5 = [X1+18-5, Y1+15-5]
            p6 = [X1-18-5, Y1+15-5]
            p7 = [X1+18-5, Y1-15-5]
            p8 = [X1-18-5, Y1-15-5]

            b1 = [X2-5, Y1+25-5]
            b2 = [X2-5, Y1-25-5]
            b3 = [X2+25-5, Y1-5]
            b4 = [X2-25-5, Y1-5]

            b5 = [X2+18-5, Y1+15-5]
            b6 = [X2-18-5, Y1+15-5]
            b7 = [X2+18-5, Y1-15-5]
            b8 = [X2-18-5, Y1-15-5]

            

            # 4 dots
            window.fill([255,255,255])
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)

            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p3)
            window.blit(m, p4)


            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_6-_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()

            window.fill([255,255,255])
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)

            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p3)
            window.blit(m, p4)


            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_8-_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()

            # 6 dots
            window.fill([255,255,255])

            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)

            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p5)
            window.blit(m, p6)
            window.blit(m, p7)
            window.blit(m, p8)
            

            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_6_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()


            # 8 dots
            window.fill([255,255,255])

            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)


            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p3)
            window.blit(m, p4)
            
            window.blit(m, p5)
            window.blit(m, p6)
            window.blit(m, p7)
            window.blit(m, p8)
            

            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_8_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()




            # 6 dots
            window.fill([255,255,255])
            
            pygame.draw.line(window, black, (X2,Y1), (X2,Y1+25-2), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2-25-2,Y1), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2+25-2,Y1), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2,Y1-25-2), 1)

            
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)

            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p5)
            window.blit(m, p6)
            window.blit(m, p7)
            window.blit(m, p8)
                        
            window.blit(m, b1)
            window.blit(m, b2)
            window.blit(m, b3)
            window.blit(m, b4)
            

            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_6+_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()


            # 8 dots
            window.fill([255,255,255])

            pygame.draw.line(window, black, (X1,Y1), (X1,Y1+25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1,Y1-25-2), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1+15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-18+3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+18-3,Y1-15), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1-25-2,Y1), 1)
            pygame.draw.line(window, black, (X1,Y1), (X1+25-2,Y1), 1)

            pygame.draw.line(window, black, (X2,Y1), (X2,Y1+25-2), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2-25-2,Y1), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2+25-2,Y1), 1)
            pygame.draw.line(window, black, (X2,Y1), (X2,Y1-25-2), 1)


            window.blit(m, p1)
            window.blit(m, p2)
            window.blit(m, p3)
            window.blit(m, p4)
            
            window.blit(m, p5)
            window.blit(m, p6)
            window.blit(m, p7)
            window.blit(m, p8)
            
            window.blit(m, b1)
            window.blit(m, b2)
            window.blit(m, b3)
            window.blit(m, b4)
            
            window.blit(n, [X1-10,Z1])
            window.blit(n, [X2-10,Z1])
           
            window.blit(n, [C3-10,Z2])

            imgname = 'B_8+_'+str(key)+'_'+D+'_'+str(key1)+'.png'
                        
            pygame.image.save(window, imgname)
            pygame.display.flip()






#Type A

        for c in range(len(coll_predicate)):
            for d in range(len(dist_predicate)):

                if dist_predicate[d] == 'D1':
                    Y1= E1
                    Y2 = E2
                else:
                    Y1 = E2
                    Y2 = E1-25

                if coll_predicate[c] == 'triangle':

                    
                    p1 = [X1,Y1-25]
                    p2 = [X1+12,Y1]
                    
                    p3 = [X1+25,Y1+25]
                    p4 = [X1,Y1+25]
                    
                    p5 = [X1-25,Y1+25]
                    p6 = [X1-12, Y1]


                    p7 = [X1+9, Y1-6]
                    p8 = [X1-9, Y1-6]

                    p9 = [X1+18, Y1+12]
                    p10 = [X1-18, Y1+12]


                    b1 = [X2,Y1-25]
                    b2 = [X2+12,Y1]
                  
                    b3 = [X2+25,Y1+25]
                    b4 = [X2,Y1+25]
                    
                    b5 = [X2-25,Y1+25]
                    b6 = [X2-12, Y1]


                    b7 = [X2+9, Y1-6]
                    b8 = [X2-9, Y1-6]

                    b9 = [X2+18, Y1+12]
                    b10 = [X2-18, Y1+12]

 
                    # 3 dots
                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p3)

                    window.blit(m, p5)

                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)

                    


                    imgname = 'A_8-_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()


                    # 3 dots
                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p3)

                    window.blit(m, p5)

                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)

                    


                    imgname = 'A_6-_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

                    
                    # 6 dots
                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p2)
                    window.blit(m, p3)

                    window.blit(m, p5)
                    window.blit(m, p4)
                    window.blit(m, p6)

                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_6_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()


                    #8 dots


                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p3)
                    window.blit(m, p4)
                    window.blit(m, p5)

                    window.blit(m, p7)
                    window.blit(m, p8)
                    window.blit(m, p9)
                    window.blit(m, p10)


                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_8_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()


                    #8+ dots


                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p3)
                    window.blit(m, p4)
                    window.blit(m, p5)

                    window.blit(m, p7)
                    window.blit(m, p8)
                    window.blit(m, p9)
                    window.blit(m, p10)

                    window.blit(m, b1)
                    window.blit(m, b2)
                    window.blit(m, b3)
                    window.blit(m, b4)
                    window.blit(m, b6)
                    window.blit(m, b5)

                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_8+_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()
                    


                    #6+ dots


                    window.fill([255,255,255])


                    pygame.draw.line(window, [190,190,190], (X1+x,Y1+y-25), (X1-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1-25+x,Y1+25+y),(X1+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X1+25+x,Y1+25+y), (X1+x,Y1+y-25), 1)

                    pygame.draw.line(window, [190,190,190], (X2+x,Y1+y-25), (X2-25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2-25+x,Y1+25+y),(X2+25+x,Y1+25+y), 1)
                    pygame.draw.line(window, [190,190,190], (X2+25+x,Y1+25+y), (X2+x,Y1+y-25), 1)

                    window.blit(m, p1)
                    window.blit(m, p3)
                    window.blit(m, p4)
                    window.blit(m, p5)

                    window.blit(m, p2)
                    window.blit(m, p6)


                    window.blit(m, b1)
                    window.blit(m, b2)
                    window.blit(m, b3)
                    window.blit(m, b4)
                    window.blit(m, b6)
                    window.blit(m, b5)

                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_6+_'+str(key)+'_'+dist_predicate[d]+'_'+'C2'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()




                    ###############

                if coll_predicate[c] == 'circle':
                    
                    radio=25

                    p1 = [X1,Y1-25]
                    p2 = [X1+25,Y1]
                    
                    p3 = [X1-25,Y1]
                    p4 = [X1,Y1+25]
                    
                    p5 = [X1+19,Y1+14]
                    p6 = [X1-19,Y1+14]

                    p7 = [X1+19, Y1-14]
                    p8 = [X1-19, Y1-14]

                    b1 = [X2,Y1-25]
                    b2 = [X2+25,Y1]
                    
                    b3 = [X2-25,Y1]
                    b4 = [X2,Y1+25]
                    
                    b5 = [X2+19,Y1+14]
                    b6 = [X2-19,Y1+14]

                    b7 = [X2+19, Y1-14]
                    b8 = [X2-19, Y1-14]

                    #4 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p3)
                    window.blit(m, p4)
                    window.blit(m, p2)

                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_6-_'+str(key)+'_'+dist_predicate[d]+'_'+'C1'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()


                    #4 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p3)
                    window.blit(m, p4)
                    window.blit(m, p2)

                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_8-_'+str(key)+'_'+dist_predicate[d]+'_'+'C1'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()






                    #6 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p7)
                    window.blit(m, p4)
                    window.blit(m, p8)
                    window.blit(m, p5)
                    window.blit(m, p6)

                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_6_'+str(key)+'_'+dist_predicate[d]+'_'+'C1_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

                    #8 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p7)
                    window.blit(m, p4)
                    window.blit(m, p8)
                    window.blit(m, p5)
                    window.blit(m, p6)
                    window.blit(m, p2)
                    window.blit(m, p3)
                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_8_'+str(key)+'_'+dist_predicate[d]+'_'+'C1'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

                    #6+4 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p7)
                    window.blit(m, p4)
                    window.blit(m, p8)
                    window.blit(m, p5)
                    window.blit(m, p6)


                    window.blit(m, b1)
                    window.blit(m, b4)
                    window.blit(m, b2)
                    window.blit(m, b3)
                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_6+_'+str(key)+'_'+dist_predicate[d]+'_'+'C1'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

                    
                    
                    #8+4 dots

                    window.fill([255,255,255])


                    pygame.draw.circle(window, grey, (X1+x,Y1+y), radio, 1)
                    pygame.draw.circle(window, grey, (X2+x,Y1+y), radio, 1)

                    window.blit(m, p1)
                    window.blit(m, p7)
                    window.blit(m, p4)
                    window.blit(m, p8)
                    window.blit(m, p5)
                    window.blit(m, p6)
                    window.blit(m, p2)
                    window.blit(m, p3)

                    window.blit(m, b1)
                    window.blit(m, b4)
                    window.blit(m, b2)
                    window.blit(m, b3)
                    
                    pygame.draw.line(window, [0,0,0], (5,Y2+20) , (145,Y2+20) , 3)


                    imgname = 'A_8+_'+str(key)+'_'+dist_predicate[d]+'_'+'C1'+'_.png'
                    
                    pygame.image.save(window, imgname)
                    pygame.display.flip()


finally:
    pygame.quit()

