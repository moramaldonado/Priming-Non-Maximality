def variables():
    black=[0, 0, 0]
    grey = [190,190,190]
    white = [255,255,255]

    colors =  {}
    colors['red']= [255,0,0]
    colors['green'] = [0,153,0]
    colors['blue'] = [0,0,255]
    #colors['orange'] = [255,153,0]

    shapes = ['dots','crosses']
    objects = ['square','triangle']
    letters = ['A','E','S','H']
    truth_value = ['True','False','Target']

    study=['1','2']
    group=[['A','B'],['B','A'],['C','D'],['D','C']]

    conditions = {'Env-T':{'1':'Collective','2':'Distributive'},
    'Env-F':{'1':'Collective','2':'Distributive'},
    'Target1':{'1':'Baseline','2':'Baseline'},
    'Target2':{'1':'Collective','2':'Distributive'}}

    predicates = {'Collective': {'A': {'4-8': 'form a triangle', '5-9':'form a square'}, 'B':{'4-8': 'surround their letter', '5-9':'surround their letter'},
    'C': {'4-8': 'are arranged as a triangle', '5-9':'are arranged as a square'}, 'D': {'4-8': 'form a circle around the letter', '5-9':'form a circle around the letter'}},
    'Distributive': {'A': {'4-8': ['are above the line','are below the line'],'5-9':['are above the line','are below the line']}, 'B': {'4-8': 'are connected to their letter', '5-9':'are connected to their letter'}, 'C': {'4-8': ['are above the line','are below the line'],'5-9':['are above the line','are below the line']},
    'D': {'4-8': 'are connected to the letter', '5-9':'are connected to the letter'}},'Baseline': {'A': {'are'},'B': {'are'}}}

    mypath = "/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/"
    path_in = mypath + "New_Shapes"
    path_out = mypath + "Images_copy"

    return black,grey,white,colors,shapes,objects,letters,truth_value, conditions, path_in, path_out, mypath, study, group, predicates
