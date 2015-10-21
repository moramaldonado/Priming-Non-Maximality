import pygame
from pygame.locals import *
import os
import random


#loading shapes from the files..
os.chdir("/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/Creating images")

#colors
black=[0, 0, 0]
grey = [190,190,190]

colors =  {}
colors['red']= [255,0,0]
colors['green'] = [0,153,0]
colors['blue'] = [0,0,153]
colors['yellow'] = [204,204,0]


try:

    pygame.init()

    #4 items
    W=40
    H=40
    radio = 4
    X = [10,30]
    Y = [10,30]

    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    for key in colors:

        window.fill([255,255,255])
        for x in range(len(X)):
            for y in range(len(Y)):
                pygame.draw.line(window, colors[key], [X[x]-radio,Y[y]-radio], [X[x]+radio,Y[y]+radio],2)
                pygame.draw.line(window, colors[key], [X[x]-radio,Y[y]+radio], [X[x]+radio,Y[y]-radio],2)


        imgname = 'cross_4_'+str(key)+'.png'

        pygame.image.save(window, imgname)
        pygame.display.flip()


    #20 items
    W = 70
    H = 70

    radio = 2

    N = [10,20,30,40,50,60]

    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    for key in colors:
        window.fill([255,255,255])

        for n in range(len(N)):
            pygame.draw.circle(window, colors[key], [N[n],10], radio)
            pygame.draw.circle(window, colors[key], [N[n],60], radio)
            pygame.draw.circle(window, colors[key], [10,N[n]], radio)
            pygame.draw.circle(window, colors[key], [60,N[n]], radio)

        imgname = 'square_20_'+str(key)+'.png'

        pygame.image.save(window, imgname)
        pygame.display.flip()




    #8 items
    W = 60
    H = 60

    radio = 3

    X = [10,30,50]
    Y = [10,30,50]

    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    for key in colors:
        window.fill([255,255,255])

        for x in range(len(X)):
            for y in range(len(Y)):
                if not (X[x]==30 and Y[y]==30):
                    pygame.draw.circle(window, colors[key], [X[x],Y[y]], radio)

        imgname = 'square_8_'+str(key)+'.png'

        pygame.image.save(window, imgname)
        pygame.display.flip()


    #8 items
    W = 60
    H = 60

    radio = 3

    X = [10,30,50]
    Y = [10,30,50]

    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    for key in colors:
        window.fill([255,255,255])

        for x in range(len(X)):
            for y in range(len(Y)):
                if not (X[x]==30 and Y[y]==30):

                    pygame.draw.line(window, colors[key], [X[x]-radio,Y[y]-radio], [X[x]+radio,Y[y]+radio],2)
                    pygame.draw.line(window, colors[key], [X[x]-radio,Y[y]+radio], [X[x]+radio,Y[y]-radio],2)



        imgname = 'crosses_8'+str(key)+'.png'

        pygame.image.save(window, imgname)
        pygame.display.flip()




    #4 items
    W=40
    H=40
    radio = 4
    x1 = 10
    x2 = 30
    y1 = 10
    y2 = 30
    window = pygame.display.set_mode([W, H], DOUBLEBUF)

    for key in colors:

        window.fill([255,255,255])

        pygame.draw.circle(window, colors[key], [x1,y1], radio)
        pygame.draw.circle(window, colors[key], [x1,y2], radio)
        pygame.draw.circle(window, colors[key], [x2,y2], radio)
        pygame.draw.circle(window, colors[key], [x2,y1], radio)

        imgname = 'square_4_'+str(key)+'.png'

        pygame.image.save(window, imgname)
        pygame.display.flip()


finally:
    pygame.quit()
