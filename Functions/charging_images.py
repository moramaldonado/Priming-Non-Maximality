def charging_images(TRIAL_INFO):
    import random

    if TRIAL_INFO['CONDITION']=='Env-F' or TRIAL_INFO['CONDITION']=='Filler-Env-F' :
        code  =  'False'
    else:

        if TRIAL_INFO['CONDITION']=='Env-T' or TRIAL_INFO['CONDITION']=='Filler-Env-T' :
            code  =  'True'

        else:
            code =  'Target'

    if TRIAL_INFO['IMAGE_TYPE'] == 'A' or TRIAL_INFO['IMAGE_TYPE'] == 'C':
        if TRIAL_INFO['PREDICATE_TYPE'] == 'Collective' or TRIAL_INFO['PREDICATE_TYPE'] == 'Baseline':
            TRIAL_INFO['KEY_PRED_1'] = random.choice(['below','above'])
            TRIAL_INFO['KEY_PRED_2'] = random.choice(['below','above'])

        TRIAL_INFO['IMAGE_1'] =  code+'_A_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_1']+'_'+'triangle'+'_'+TRIAL_INFO['KEY_PRED_1']+'_.png'
        TRIAL_INFO['IMAGE_2'] =  code+'_A_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_2']+'_'+'square'+'_'+TRIAL_INFO['KEY_PRED_2']+'_.png'

    elif TRIAL_INFO['IMAGE_TYPE'] == 'B':

            TRIAL_INFO['IMAGE_1'] = code+'_B_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_1']+'_.png'
            TRIAL_INFO['IMAGE_2'] = code+'_B_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_2']+'_.png'

    else:
            TRIAL_INFO['IMAGE_1'] = code+'_D_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_1']+'_.png'
            TRIAL_INFO['IMAGE_2'] = code+'_D_'+TRIAL_INFO['SHAPE']+'_'+TRIAL_INFO['Color_2']+'_.png'

    if not TRIAL_INFO['CONDITION'].startswith('Filler'):

        if TRIAL_INFO['PREDICATE_TYPE'] == 'Baseline':
            TRIAL_INFO['TRUTH_VALUE_1'] = 'True'
            TRIAL_INFO['TRUTH_VALUE_2'] = 'False'
        else:
            TRIAL_INFO['TRUTH_VALUE_1'] = code
            TRIAL_INFO['TRUTH_VALUE_2'] = code


    return TRIAL_INFO
