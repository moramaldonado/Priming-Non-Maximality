def experimental_trials(TRIAL_INFO, PREDICATES):
    import random

    #numerals
    TRIAL_INFO['N1']  = '4-8'
    TRIAL_INFO['N2']  = '5-9'

    #for baselines
    if TRIAL_INFO['PREDICATE_TYPE'] == 'Baseline':
        TRIAL_INFO['PREDICATE_1']  = 'are'
        TRIAL_INFO['PREDICATE_2']  = 'are'
        if TRIAL_INFO['IMAGE_TYPE'] == 'B': # image B
            if TRIAL_INFO['CONDITION']=='Target1' or TRIAL_INFO['CONDITION']=='Target2':
                TRIAL_INFO['S1']  = 'The letters are ' +TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'The letters are ' +TRIAL_INFO['False_Color_2']+'.'
            else:
                TRIAL_INFO['S1']  = 'Some letters are ' +TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'Some letters are ' +TRIAL_INFO['False_Color_2']+'.'

        elif TRIAL_INFO['IMAGE_TYPE'] == 'D': # image D

            if TRIAL_INFO['CONDITION']=='Target1' or TRIAL_INFO['CONDITION']=='Target2':
                TRIAL_INFO['S1']  = 'Some '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'Some '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['False_Color_2']+'.'
            else:
                TRIAL_INFO['S1']  = 'The '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'The '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['False_Color_2']+'.'

        else:
            if TRIAL_INFO['CONDITION']=='Target1' or TRIAL_INFO['CONDITION']=='Target2':
                TRIAL_INFO['S1']  = 'The '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'The '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['False_Color_2']+'.'
            else:
                TRIAL_INFO['S1']  = 'Some '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['Color_1']+'.'
                TRIAL_INFO['S2']  = 'Some '+TRIAL_INFO['SHAPE']+' are '+TRIAL_INFO['False_Color_2']+'.'

    #for collective and distributive predicates
    else:

        if (TRIAL_INFO['PREDICATE_TYPE']  == 'Distributive' and (TRIAL_INFO['IMAGE_TYPE']  == 'A' or TRIAL_INFO['IMAGE_TYPE']  == 'C')):
            TRIAL_INFO['KEY_PRED_1'] = random.choice(['below','above'])
            TRIAL_INFO['PREDICATE_1']  = 'are ' +TRIAL_INFO['KEY_PRED_1']+' the line'
            TRIAL_INFO['KEY_PRED_2'] = random.choice(['below','above'])
            TRIAL_INFO['PREDICATE_2']  = 'are ' +TRIAL_INFO['KEY_PRED_2']+' the line'
            TRIAL_INFO['S1']  = 'Between 4 and 8 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_1']+'.'
            TRIAL_INFO['S2']  = 'Between 5 and 9 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_2']+'.'
            TRIAL_INFO['N1']  = '4-8'
            TRIAL_INFO['N2']  = '5-9'

        elif TRIAL_INFO['IMAGE_TYPE'] =='B' or TRIAL_INFO['IMAGE_TYPE'] =='D': #change this for all B
            TRIAL_INFO['PREDICATE_1']  = PREDICATES[TRIAL_INFO['PREDICATE_TYPE']][TRIAL_INFO['IMAGE_TYPE']][TRIAL_INFO['N1']]
            TRIAL_INFO['PREDICATE_2']  = PREDICATES[TRIAL_INFO['PREDICATE_TYPE']][TRIAL_INFO['IMAGE_TYPE']][TRIAL_INFO['N2']]
            TRIAL_INFO['S1']  = 'Between 6 and 10 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_1']+'.'
            TRIAL_INFO['N1']  = '6-10'
            TRIAL_INFO['S2']  = 'Between 5 and 9 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_2']+'.'
            TRIAL_INFO['N2']  = '5-9'

        else:
            TRIAL_INFO['PREDICATE_1']  = PREDICATES[TRIAL_INFO['PREDICATE_TYPE']][TRIAL_INFO['IMAGE_TYPE']][TRIAL_INFO['N1']]
            TRIAL_INFO['PREDICATE_2']  = PREDICATES[TRIAL_INFO['PREDICATE_TYPE']][TRIAL_INFO['IMAGE_TYPE']][TRIAL_INFO['N2']]
            TRIAL_INFO['S1']  = 'Between 4 and 8 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_1']+'.'
            TRIAL_INFO['S2']  = 'Between 5 and 9 '+TRIAL_INFO['SHAPE']+' '+TRIAL_INFO['PREDICATE_2']+'.'
            TRIAL_INFO['N1']  = '4-8'
            TRIAL_INFO['N2']  = '5-9'


    return TRIAL_INFO
