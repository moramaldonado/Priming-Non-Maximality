
import os, random, pickle, pygame

import sys

sys.path.insert(0, '/Users/moramaldonado/Dropbox/2015-PhD/Priming-Non-Maximality/Functions')

from variables import *
from experimental_trials import *
from fillers import *
from to_ibex import *
from checking_colors import *
from charging_images import *
from validation import *

##############################################
#import all the variables
black,grey,white,colors,shapes,objects,letters,truth_value, conditions, path_in, path_out, mypath, study, group, predicates = variables()

#############################################
#creating folders for each study
for m in range(len(study)):
    x = mypath+'Pilot-Study'+study[m]+'/'
    if not os.path.isdir(x):
       os.makedirs(x)
    os.chdir(x)


#creating txt files for each group inside one particular study
    for g in range(len(group)):
        file_name = group[g][0]+group[g][-1]
        stru = open(file_name+'.txt', 'w')

        ibex_file = group[g][0]+group[g][-1]+'_IBEX.txt'
        out = open(ibex_file, 'w')
        trials = []

        index = 0
        #for each condition (Env-T, Env-F, Target1, Target2)
        for key in conditions:
            #for both types of shapes
            for s in range(len(shapes)):
                    #two repetitions
                    for i in range(0,2):
                        for i in range(0,2):
                            TRIAL_INFO = {}
                            TRIAL_INFO['PREDICATE_TYPE'] = conditions[key][study[m]]

                            TRIAL_INFO['CONDITION'] = key
                            if TRIAL_INFO['CONDITION']=='Target2':
                                TRIAL_INFO['IMAGE_TYPE'] = group[g][-1]
                            else:
                                TRIAL_INFO['IMAGE_TYPE'] = group[g][0]

                            TRIAL_INFO['SHAPE'] = shapes[s]
                            TRIAL_INFO['GROUP'] = group[g]
                            TRIAL_INFO['STUDY'] = study[m]
                            
                            TRIAL_INFO = checking_colors(TRIAL_INFO,colors)

                            TRIAL_INFO = experimental_trials(TRIAL_INFO,predicates)

                            TRIAL_INFO = charging_images(TRIAL_INFO)

                            trials.append(TRIAL_INFO)

                            
                            data_line_bis_1, data_line_bis_2, = to_ibex2(TRIAL_INFO, "Sentence", "SubHtmlFlash")

                            print >> out, data_line_bis_1,','
                            print >> out, data_line_bis_2,','

                            print >> stru, TRIAL_INFO['CONDITION'], ',',TRIAL_INFO['S1'], ',',TRIAL_INFO['IMAGE_1'], ',',TRIAL_INFO['TRUTH_VALUE_1'],',',TRIAL_INFO['N1']
                            print >> stru, TRIAL_INFO['CONDITION'], ',',TRIAL_INFO['S2'], ',',TRIAL_INFO['IMAGE_2'], ',',TRIAL_INFO['TRUTH_VALUE_2'],',',TRIAL_INFO['N2']
                        
                        FILLER_INFO = fillers(TRIAL_INFO)
                        FILLER_INFO = charging_images(FILLER_INFO)
                        trials.append(FILLER_INFO)

                        #data for Ibex
                        
                        data_line_bis_3, data_line_bis_4, = to_ibex2(FILLER_INFO, "Sentence", "SubHtmlFlash")

                        print >> out, data_line_bis_3,','
                        print >> out, data_line_bis_4,','

                        print >> stru, FILLER_INFO['CONDITION'], ',', FILLER_INFO['S1'], ',',FILLER_INFO['IMAGE_1'], ',',FILLER_INFO['TRUTH_VALUE_1'], ',',FILLER_INFO['N1']
                        print >> stru, FILLER_INFO['CONDITION'], ',',FILLER_INFO['S2'], ',',FILLER_INFO['IMAGE_1'], ',',FILLER_INFO['TRUTH_VALUE_2'], ',',FILLER_INFO['N2']

                        
            index= index + 1



        with open(file_name+'.pickle', 'wb') as handle:
          pickle.dump(trials, handle)

        validation(trials)

        out.close()
        stru.close()
