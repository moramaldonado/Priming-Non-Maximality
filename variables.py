def variables_experiment():
    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    colors =  {}
    colors['red']= [255,0,0]
    colors['green'] = [0,153,0]
    colors['blue'] = [0,0,153]
    colors['orange'] = [255,153,0]

    shapes = ['dots','crosses']
    objects = ['square','triangle']
    letters = ['A','E','S','H']
    condition = ['True','False','Target']
    path_in ="/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/Shapes"
    path_out = "/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/Images"

    return black,grey,white,colors,shapes,objects,letters,condition, path_in, path_out
