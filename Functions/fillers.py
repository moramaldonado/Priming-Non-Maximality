def fillers(TRIAL_INFO):
    import random
    FILLER_INFO = {}
    FILLER_INFO['PREDICATE_TYPE'] = 'Baseline'
    FILLER_INFO['SHAPE'] = TRIAL_INFO['SHAPE']
    FILLER_INFO['GROUP'] = TRIAL_INFO['GROUP']
    FILLER_INFO['STUDY'] = TRIAL_INFO['STUDY']ju
    FILLER_INFO['CONDITION'] = 'Filler-'+TRIAL_INFO['CONDITION']
    FILLER_INFO['Color_1'] = TRIAL_INFO['Color_1']
    FILLER_INFO['Color_2'] = TRIAL_INFO['Color_2']
    FILLER_INFO['False_Color_1'] = TRIAL_INFO['False_Color_1']
    FILLER_INFO['False_Color_2'] = TRIAL_INFO['False_Color_2']
    FILLER_INFO['N1'] = 'X-X'
    FILLER_INFO['N2'] = 'X-X'
    FILLER_INFO['PREDICATE_2'] = 'X'
    FILLER_INFO['PREDICATE_1'] = 'X'

    FILLER_INFO['IMAGE_TYPE'] = random.choice(TRIAL_INFO['GROUP'])

    if FILLER_INFO['IMAGE_TYPE']=='B':
        pred = 'letters'

    else:
        pred = TRIAL_INFO['SHAPE']

    if FILLER_INFO['IMAGE_TYPE'] != 'D':

        if TRIAL_INFO['CONDITION'] == 'Env-T':
            FILLER_INFO['TRUTH_VALUE_1'] = 'False'
            FILLER_INFO['S1'] = 'Some '+ pred+' are '+ TRIAL_INFO['False_Color_1']+'.'
            FILLER_INFO['TRUTH_VALUE_2'] = 'False'
            FILLER_INFO['S2'] = 'Some '+ pred+' are '+ TRIAL_INFO['False_Color_2']+'.'

        else:

            if TRIAL_INFO['CONDITION'] == 'Env-F':
                FILLER_INFO['TRUTH_VALUE_1'] = 'True'
                FILLER_INFO['S1'] = 'Some '+ pred+' are '+ TRIAL_INFO['Color_1']+'.'
                FILLER_INFO['TRUTH_VALUE_2'] = 'True'
                FILLER_INFO['S2'] = 'Some '+ pred+' are '+ TRIAL_INFO['Color_2']+'.'

            else:
                FILLER_INFO['TRUTH_VALUE_1'] = random.choice(['False','True'])

                if FILLER_INFO['TRUTH_VALUE_1'] == 'False':
                    color = TRIAL_INFO['False_Color_1']
                else:
                    color = TRIAL_INFO['Color_1']

                FILLER_INFO['S1'] = 'All '+pred+' are '+ color+'.'

                FILLER_INFO['TRUTH_VALUE_2'] = random.choice(['False','True'])

                if FILLER_INFO['TRUTH_VALUE_2'] == 'False':
                    color = TRIAL_INFO['False_Color_2']
                else:
                    color = TRIAL_INFO['Color_2']
                FILLER_INFO['S2'] = 'All '+pred +' are '+ color+'.'
    else:

        if TRIAL_INFO['CONDITION'] == 'Env-T':
            FILLER_INFO['TRUTH_VALUE_1'] = 'False'
            FILLER_INFO['S1'] = 'All '+ pred+' are '+ TRIAL_INFO['False_Color_1']+'.'
            FILLER_INFO['TRUTH_VALUE_2'] = 'False'
            FILLER_INFO['S2'] = 'All '+ pred+' are '+ TRIAL_INFO['False_Color_2']+'.'

        else:

            if TRIAL_INFO['CONDITION'] == 'Env-F':
                FILLER_INFO['TRUTH_VALUE_1'] = 'True'
                FILLER_INFO['S1'] = 'All '+ pred+' are '+ TRIAL_INFO['Color_1']+'.'
                FILLER_INFO['TRUTH_VALUE_2'] = 'True'
                FILLER_INFO['S2'] = 'All '+ pred+' are '+ TRIAL_INFO['Color_2']+'.'

            else:
                FILLER_INFO['TRUTH_VALUE_1'] = random.choice(['False','True'])

                if FILLER_INFO['TRUTH_VALUE_1'] == 'False':
                    color = TRIAL_INFO['False_Color_1']
                else:
                    color = TRIAL_INFO['Color_1']

                FILLER_INFO['S1'] = 'Some '+pred+' are '+ color+'.'

                FILLER_INFO['TRUTH_VALUE_2'] = random.choice(['False','True'])

                if FILLER_INFO['TRUTH_VALUE_2'] == 'False':
                    color = TRIAL_INFO['False_Color_2']
                else:
                    color = TRIAL_INFO['Color_2']
                FILLER_INFO['S2'] = 'Some '+pred +' are '+ color+'.'


    return FILLER_INFO
