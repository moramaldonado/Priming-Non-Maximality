def display_img(path_in, image, screen, positions):
    #display_img() >> charges one image from a particular path and puts it in a white window.
    import pygame
    import os

    os.chdir(path_in)
    img = pygame.image.load(image)
    img_size_x, img_size_y = img.get_size()

    img_pos_x = positions[0] - img_size_x/2
    img_pos_y = positions[1]- img_size_y/2

    screen.blit(img,(img_pos_x,img_pos_y))
