
import os
import random
from baseline_sentences import *
from filler_sentences import *
from group_ordering import *
from functions import *

##############################################
                
SET_COLOR1 = ['black','green','red']
SET_COLOR2 = ['black','blue','yellow']

study=['1','2','3','4','5','6']
group=[['A','B'],['B','A']]

shapes = ['dots','crosses']
numerals = {'5-7':['five','seven',6],'7-9':['seven','nine',8]}
predicates={'C': {'A':['form a circle','form a triangle'],'B':['surround a circle','surround a square']},
            'D':{'A':['are above the line','are below the line'],'B':['are connected to the circle', 'are connected to the square']},
            'Bas':{'A':['',''],'B':['','']}}
conditions={'Env-T':{'1':'C','2':'D','3':'Bas','4':'Bas','5':'C','6':'C'}, 'Env-F':{'1':'C','2':'D','3':'Bas','4':'Bas','5':'C','6':'C'},
            'Target1':{'1':'C','2':'D','3':'C','4':'D','5':'C','6':'D'}, 'Target2':{'1':'C','2':'D','3':'C','4':'D','5':'D','6':'D'}}
mypath = "/Users/moramaldonado/Desktop/Priming NonMaximality/"


#############################################

#creating folders for each study
for m in range(len(study)):
    x = mypath+'Study'+study[m]+'/'
    if not os.path.isdir(x):
       os.makedirs(x)
    os.chdir(x)

#creating txt files for each group inside one particular study
    for g in range(len(group)):
        file_name = group[g][0]+group[g][1]+'.txt'
        out = open(file_name, 'w')
        print >>out,'Code'+','+'Sentence'+','+'Picture'

        #for each condition (Env-T, Env-F, Target1, Target2)
        for key in conditions: 

            #for both types of shapes
            for s in range(len(shapes)):

                #for both numeral combinations
               for key2 in numerals:


                    #two repetitions
                    for i in range(0,2):
                        
                        CONDITION = key
                        SHAPE = shapes[s]
                        NUMERALS =  numerals[key2]
                        GROUP = group[g]
                        PREDICATE_TYPE = conditions[key][study[m]]
                        N_SHAPES =  numerals[key2][2]

                        # Number of shapes according to condition
                        if CONDITION=='Target1' or CONDITION=='Target2':
                            N_SHAPES =  str(numerals[key2][2])+'+'
                        if CONDITION=='EnvF':
                            N_SHAPES =  str(numerals[key2][2])+'-'

                        if CONDITION == 'Target2':

                            COLOR1, COLOR2, PREDICATE_C1, PREDICATE_C2, PREDICATE_D1, PREDICATE_D2 = group_ordering(GROUP[1],PREDICATE_TYPE, SHAPE,SET_COLOR1, SET_COLOR2)
                            PREDICATE_1 = predicates[conditions[key][study[m]]][group[g][1]][0]
                            PREDICATE_2 = predicates[conditions[key][study[m]]][group[g][1]][1]

                            #sentence with one possible predicate 
                            sentence1 =  'Between '+numerals[key2][0]+' and '+numerals[key2][1]+' '+shapes[s]+' '+PREDICATE_1+'.'
                            picture1 =  GROUP[1]+'_'+N_SHAPES+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D1+'_'+PREDICATE_C1+'_'+COLOR2+'.png'
                            code1 = GROUP[0]+GROUP[1]+'_'+'Target'+'_'+CONDITION+'_'+PREDICATE_TYPE+'_'+key2+'_'+SHAPE+'_'+PREDICATE_1

                            #sentence with a second possible predicate 
                            sentence2= 'Between '+numerals[key2][0]+' and '+numerals[key2][1]+' '+shapes[s]+' '+PREDICATE_2+'.'
                            picture2= GROUP[1]+'_'+N_SHAPES+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D2+'_'+PREDICATE_C2+'_'+COLOR2+'.png'
                            code2= GROUP[0]+GROUP[1]+'_'+'Target'+'_'+CONDITION+'_'+PREDICATE_TYPE+'_'+key2+'_'+SHAPE+'_'+PREDICATE_2 
                            

                            filler1, filler2, f1, f2, COLOR1, COLOR2= filler_creation(GROUP[1], SHAPE, CONDITION, SET_COLOR1, SET_COLOR2)
                            picturefiller1 =  GROUP[1]+'_'+N_SHAPES+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D1+'_'+PREDICATE_C1+'_'+COLOR2+'.png'
                            picturefiller2= GROUP[1]+'_'+N_SHAPES+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D2+'_'+PREDICATE_C2+'_'+COLOR2+'.png'                            
                            code1_filler= GROUP[0]+GROUP[1]+'_'+f1+'_'+CONDITION+'_'+'Bas'+'_'+key2+'_'+SHAPE+'_'+PREDICATE_1 
                            code2_filler= GROUP[0]+GROUP[1]+'_'+f2+'_'+CONDITION+'_'+'Bas'+'_'+key2+'_'+SHAPE+'_'+PREDICATE_2
                            
                            
      
                        else:

                            PREDICATE_1 = predicates[conditions[key][study[m]]][group[g][0]][0]
                            PREDICATE_2 = predicates[conditions[key][study[m]]][group[g][0]][1]
                            
                            COLOR1, COLOR2, PREDICATE_C1, PREDICATE_C2, PREDICATE_D1, PREDICATE_D2 = group_ordering(GROUP[0],PREDICATE_TYPE, SHAPE,SET_COLOR1, SET_COLOR2)

                          
                            if PREDICATE_TYPE == 'Bas':
                                sentence1, sentence2 = baseline_sentences(GROUP[0], SHAPE, COLOR1, COLOR2, CONDITION,SET_COLOR1, SET_COLOR2)
                            else:
                                sentence1 = 'Between '+numerals[key2][0]+' and '+numerals[key2][1]+' '+shapes[s]+' '+PREDICATE_1+'.'
                                sentence2= 'Between '+numerals[key2][0]+' and '+numerals[key2][1]+' '+shapes[s]+' '+PREDICATE_2+'.'

                           #sentence with one possible predicate
                           
                            picture1 =  GROUP[0]+'_'+str(N_SHAPES)+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D1+'_'+PREDICATE_C1+'_'+COLOR2+'.png'
                            code1 = '\''+ GROUP[0]+GROUP[1]+'_'+'Target'+'_'+CONDITION+'_'+PREDICATE_TYPE+'_'+key2+'_'+SHAPE+'_'+PREDICATE_1+'\''


                            #sentence with a second possible predicate 

                            picture2= GROUP[0]+'_'+str(N_SHAPES)+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D2+'_'+PREDICATE_C2+'_'+COLOR2+'.png'
                            code2= '\''+GROUP[0]+GROUP[1]+'_'+'Target'+'_'+CONDITION+'_'+PREDICATE_TYPE+'_'+key2+'_'+SHAPE+'_'+PREDICATE_2+'\''



                            filler1, filler2, f1, f2, COLOR1, COLOR2 = filler_creation(GROUP[0], SHAPE, CONDITION, SET_COLOR1, SET_COLOR2)

                            picturefiller1 = GROUP[0]+'_'+str(N_SHAPES)+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D1+'_'+PREDICATE_C1+'_'+COLOR2+'.png'
                            picturefiller2 = GROUP[0]+'_'+str(N_SHAPES)+'_'+SHAPE+'_'+COLOR1+'_'+PREDICATE_D2+'_'+PREDICATE_C2+'_'+COLOR2+'.png'    

                            code1_filler= '\''+GROUP[0]+GROUP[1]+'_'+f1+'_'+CONDITION+'_'+'Bas'+'_'+key2+'_'+SHAPE+'_'+PREDICATE_1+'\''
                            code2_filler= '\''+GROUP[0]+GROUP[1]+'_'+f2+'_'+CONDITION+'_'+'Bas'+'_'+key2+'_'+SHAPE+'_'+PREDICATE_2+'\''



                        print >>out, '['+code1+','+ '\"SubHtmlFlash\"'+','+'{html:"<center> <img src=\'https://dl.dropboxusercontent.com/u/13340774/Images/'+ picture1+'\''+'border=\'2\'></center>\"'+','+'q:\"'+ sentence1 +'\"'+',hasCorrect:1}],'
                       
                        print >>out, '['+code2+','+ '\"SubHtmlFlash\"'+','+'{html:"<center> <img src=\'https://dl.dropboxusercontent.com/u/13340774/Images/'+ picture2+'\''+'border=\'2\'></center>\"'+','+'q:\"'+ sentence2 +'\"'+',hasCorrect:1}],'
                        
                        print >>out, '['+code1_filler+','+ '\"SubHtmlFlash\"'+','+'{html:"<center> <img src=\'https://dl.dropboxusercontent.com/u/13340774/Images/'+ picturefiller1+'\''+'border=\'2\'></center>\"'+','+'q:\"'+ filler1 +'\"'+',hasCorrect:1}],'
                       
                        print >>out, '['+code2_filler+','+ '\"SubHtmlFlash\"'+','+'{html:"<center> <img src=\'https://dl.dropboxusercontent.com/u/13340774/Images/'+ picturefiller2+'\''+'border=\'2\'></center>\"'+','+'q:\"'+ filler2 +'\"'+',hasCorrect:1}],'

        out.close()







    
