
def points(CONDITION,OBJECT):
#points() > only for type A images, creates the positions for each shape (dots or crosses) depending on the condition and the collective predicate
    if  CONDITION == 'False':
        if OBJECT == 'triangle':
            P = [[10,30],
                 [30,30],
                 [20,10]]
        else:
            P = [[10,30],
            [30,30],
            [10,10],
            [30,10]]

    if  CONDITION == 'Target':
        if OBJECT == 'triangle':
            P = [[12,72],[24,72],[36,72],[48,72],[60,72],[72,72],
            [16,62],[68,62],
            [20,52],[64,52],
            [24,43],[60,42],
            [28,32],[56,32],
            [32,22],[52,22],
            [36,12],[48,12],
            [42,4]]

        else:
            P = []
            N = [12,24,36,48,60,72]
            for n in range(len(N)):
                P.append([N[n],12])
                P.append([N[n],72])
                P.append([12,N[n]])
                P.append([72,N[n]])

    if  CONDITION == 'True':
        if OBJECT == 'triangle':
            P = [[10,50],[30,50],
            [50,50],[20,30],[40,30],
            [30,10]]

        else:
            P = []
            X = [10,30,50]
            Y = [10,30,50]
            for x in range(len(X)):
                for y in range(len(Y)):
                    if not (X[x]==30 and Y[y]==30):
                        P.append([X[x],Y[y]])

    return P



def parametters_shapes(CONDITION, TYPE):
# parametters_shapes()>> depending on the condition and the type of image, determinates the size of the figure,
#the ratio of the shapes and the letters, the width of the lines and the positions

    if  CONDITION == 'False':
        if TYPE == 'B':
            #parametters of "False"
            W = 50
            H = 50
            radio = 3
            letter_size = 14
            width_shape = 2

            # P corresponds to the list of points for the shapes; L corresponds to the two-points arrays for the connections
            P = [[W/2-15,H/2],
            [W/2+15,H/2],
            [W/2,H/2-15],
            [W/2,H/2+15]]

            L = [[[W/2-10,H/2],[W/2-5,H/2]],
            [[W/2+10,H/2],[W/2+5,H/2]],
            [[W/2,H/2-12],[W/2,H/2-5]],
            [[W/2,H/2+13],[W/2,H/2+4]]]

        if TYPE == 'A':
            W = 40
            H = 40
            radio = 4
            letter_size = 14
            width_shape = 2
            L = 0
            P = 0


    if CONDITION == 'True':
        W = 60
        H = 60
        radio = 3
        letter_size = 18
        width_shape = 2

        P = [[W/2-10,H/2+20],
        [W/2+10,H/2+20],
        [W/2-10,H/2-20],
        [W/2+10,H/2-20],
        [W/2-20,H/2],
        [W/2+20,H/2]]

        L = [[[W/2-10,H/2+20],[W/2-5,H/2+5]],
        [[W/2+10,H/2+20],[W/2+5,H/2+5]],
        [[W/2-10,H/2-20],[W/2-7,H/2-5]],
        [[W/2+10,H/2-20],[W/2+5,H/2-5]],
        [[W/2-20,H/2],[W/2-7,H/2]],
        [[W/2+20,H/2],[W/2+5,H/2]]]

    if CONDITION == 'Target':
        if TYPE == 'A':
            W = 84
            H = 84
        else:
            W = 70
            H = 70


        radio = 2
        letter_size = 20
        width_shape = 1


        P = [[W/2-15,H/2+21],
        [W/2+15,H/2+21],
        [W/2-8,H/2+24],
        [W/2+8,H/2+24],
        [W/2-26,H/2+7],
        [W/2+26,H/2+7],
        [W/2-15,H/2-21],
        [W/2+15,H/2-21],
        [W/2-8,H/2-24],
        [W/2+8,H/2-24],
        [W/2-26,H/2-7],
        [W/2+26,H/2-7],
        [W/2-27,H/2],
        [W/2+27,H/2],
        [W/2-22,H/2-15],
        [W/2+22,H/2-15],
        [W/2-22,H/2+15],
        [W/2+22,H/2+15],
        [W/2,H/2-26],
        [W/2,H/2+26]]


        L = [[[W/2-15,H/2+21],[W/2-6,H/2+6]],
        [[W/2+15,H/2+21],[W/2+5,H/2+6]],
        [[W/2-8,H/2+24],[W/2-6,H/2+6]],
        [[W/2+8,H/2+24],[W/2+5,H/2+6]],
        [[W/2-26,H/2+7],[W/2-6,H/2]],
        [[W/2+26,H/2+7],[W/2+5,H/2]],
        [[W/2-15,H/2-21],[W/2-2,H/2-6]],
        [[W/2+15,H/2-21],[W/2+2,H/2-6]],
        [[W/2-8,H/2-24],[W/2-2,H/2-6]],
        [[W/2+8,H/2-24],[W/2+2,H/2-6]],
        [[W/2-26,H/2-7], [W/2-6,H/2]],
        [[W/2+26,H/2-7],[W/2+5,H/2]],
        [[W/2-27,H/2],[W/2-6,H/2]],
        [[W/2+27,H/2],[W/2+5,H/2]]]
        ##                     [W/2-22,H/2-15],
        ##                     [W/2+22,H/2-15],
        ##
        ##                     [W/2-22,H/2+15],
        ##                     [W/2+22,H/2+15],
        ##
        ##                     [W/2,H/2-26],
        ##                     [W/2,H/2+26]
        ##                     ]

    return W,H,radio,letter_size, P, L, width_shape

def shapes_by_shapes(path,condition,colors,objects,shapes):
    import pygame
    import os

    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    for s in range(len(shapes)):
        for key in colors:
            for o in range(len(objects)):
                for c in range(len(condition)):

                    #busco los parametros para esa condicion
                    W,H,radio,letter_size, P, L, width_shape = parametters_shapes(condition[c],'A')
                    P = points(condition[c],objects[o])

                    # creo mi pagina en blanco
                    window = pygame.display.set_mode([W, H])
                    window.fill(white)

                    for p in range(len(P)):

                        if shapes[s] == 'crosses':
                            pygame.draw.line(window, colors[key], [P[p][0]-radio,P[p][1]-radio], [P[p][0]+radio,P[p][1]+radio],width_shape)
                            pygame.draw.line(window, colors[key], [P[p][0]-radio,P[p][1]+radio], [P[p][0]+radio,P[p][1]-radio],width_shape)

                        if shapes[s] == 'dots':
                            pygame.draw.circle(window, colors[key], P[p], radio)

                # guardo la imagen en mi path querido
                    os.chdir(path)
                    imgname = condition[c]+'_A_'+shapes[s]+'_'+str(key)+'_'+objects[o]+'.png'
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

    pass

def letter_with_connections(path,condition,colors,letters,shapes):
    #letter_with_connctions() >> for color,condition and shape, creates a figure with a letter connected to number of shapes
    import pygame
    import os

    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    for s in range(len(shapes)):
        for key in colors:
            for l in range(len(letters)):
                for c in range(len(condition)):

                    #busco los parametros para esa condicion
                    W,H,radio,letter_size, P, L, width_shape = parametters_shapes(condition[c],'B')

                    #parametros de letras!
                    font = pygame.font.SysFont('Tahoma', letter_size)
                    text = font.render(letters[l], True, colors[key])
                    text_x, text_y = font.size(letters[l])

                    # creo mi papel en blanco
                    window = pygame.display.set_mode([W, H])
                    window.fill(white)

                    #A DIBUJAR!

                    #(1) I draw the connections
                    for i in range(len(L)):
                        pygame.draw.line(window, grey, L[i][0], L[i][1],1)

                    #(2) I draw the letter
                    window.blit(text, ((W-text_x)/2,(H-text_y)/2))

                    #(3) I draw the shapes
                    for p in range(len(P)):

                        if shapes[s] == 'dots':
                            pygame.draw.circle(window, black, P[p], radio)

                        if shapes[s] == 'crosses':
                            pygame.draw.line(window, black, [P[p][0]-radio,P[p][1]-radio], [P[p][0]+radio,P[p][1]+radio],width_shape)
                            pygame.draw.line(window, black, [P[p][0]-radio,P[p][1]+radio], [P[p][0]+radio,P[p][1]-radio],width_shape)

                # guardo la imagen en mi path querido
                    os.chdir(path)
                    imgname = condition[c]+'_B_'+shapes[s]+'_'+str(key)+'_'+letters[l]+'.png'
                    pygame.image.save(window, imgname)
                    pygame.display.flip()

    pass


def random_letters(path,colors,letters):
    import pygame
    import os
    import random

    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    for key in colors:
        for l in range(len(letters)):
            W = 60
            H = 60

            #parametros de letras!
            font = pygame.font.SysFont('Tahoma', 16)
            text = font.render(letters[l], True, colors[key])
            text_x, text_y = font.size(letters[l])

            # creo mi papel en blanco
            window = pygame.display.set_mode([W, H])
            window.fill(white)
            window.blit(text, ((W-text_x)/2,(H-text_y)/2))

            # guardo la imagen en mi path querido
            os.chdir(path)
            imgname = 'Fill'+'_B_'+str(key)+'_'+letters[l]+'.png'
            pygame.image.save(window, imgname)
            pygame.display.flip()

    pass


def parametters(TYPE):
    W = 180
    H = 220
    positions = {}

    if TYPE == 'A':
        positions['above']= [[W/4,H/4],[W-W/4,H/3],[W/2,H/3]]
        positions['below']= [[W/4,H-H/4],[W-W/4,H-H/3],[W/2,H-H/3]]
    else:
        positions['B'] = [[W/4,H/4],[W-W/4,H/4],[W/2,H-H/4]]

    return W,H,positions

def images_A(colors, shapes,condition,objects,path_in, path_out):
    import pygame
    import random
    import os
    from functions import *

    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    W,H,positions = parametters('A')

    for s in range(len(shapes)):
        for c in range(len(condition)):
            for o in range(len(objects)):
                for key in colors:
                    for key1 in positions:


                        window = pygame.display.set_mode([W, H])
                        window.fill([255,255,255])
                        pygame.draw.line(window, black, (W-10,H/2),(10,H/2) , 2)

                        if condition[c] == 'Target':
                            image1 = 'Target'+'_A_'+shapes[s]+'_'+str(key)+'_'+objects[o]+'.png'
                            image2 = 'True'+'_A_'+shapes[s]+'_'+str(key)+'_'+objects[o]+'.png'
                            display_img(path_in, image1, window, positions[key1][0])
                            display_img(path_in, image2, window, positions[key1][1])

                        else:
                            image = condition[c]+'_A_'+shapes[s]+'_'+str(key)+'_'+objects[o]+'.png'
                            display_img(path_in, image, window, positions[key1][2])

                        os.chdir(path_out)
                        imgname = condition[c]+'_A_'+shapes[s]+'_'+str(key)+'_'+objects[o]+'_'+str(key1)+'_.png'
                        pygame.image.save(window, imgname)
                        pygame.display.flip()


def images_B (colors, shapes,letters,condition,path_in, path_out):
    import pygame
    import random
    import os
    from functions import *

    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    W,H,positions = parametters('B')

    for s in range(len(shapes)):
        for c in range(len(condition)):
            for key in colors:
                window = pygame.display.set_mode([W, H])
                window.fill([255,255,255])
                random.shuffle(positions['B'])
                random.shuffle(letters)

                if condition[c] == 'Target':
                    image1 = 'Target'+'_B_'+shapes[s]+'_'+str(key)+'_'+letters[0]+'.png'
                    image2 = 'True'+'_B_'+shapes[s]+'_'+str(key)+'_'+letters[1]+'.png'
                    fill = 'Fill'+'_B_'+str(key)+'_'+letters[2]+'.png'
                    display_img(path_in, image1, window, positions['B'][0])
                    display_img(path_in, image2, window, positions['B'][1])
                    display_img(path_in, fill, window, positions['B'][2])

                else:
                    image = condition[c]+'_B_'+shapes[s]+'_'+str(key)+'_'+letters[1]+'.png'
                    fill1 ='Fill'+'_B_'+str(key)+'_'+letters[0]+'.png'
                    fill2 ='Fill'+'_B_'+str(key)+'_'+letters[1]+'.png'
                    display_img(path_in, image, window, positions['B'][2])
                    display_img(path_in, fill2, window, positions['B'][1])
                    display_img(path_in, fill1, window, positions['B'][0])

                os.chdir(path_out)
                imgname = condition[c]+'_B_'+shapes[s]+'_'+str(key)+'_.png'
                pygame.image.save(window, imgname)
                pygame.display.flip()
