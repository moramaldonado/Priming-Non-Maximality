def validation(trials):
    valida = {'True': 0, 'False': 0, 'Filler':0, 'Env-F': 0,  'Env-T': 0,  'Target1': 0, 'Target2': 0, 'Total':0, 'Baseline':0, 'Collective':0, 'Distributive':0, 'A':0, 'B':0, 'C':0, 'D':0}


    for i in range(len(trials)):
        
        if trials[i]['CONDITION'].startswith('Filler'):
            valida['Filler'] = valida['Filler']+2

        for key in valida:
            if trials[i]['CONDITION'] == key:
                valida[key] = valida[key]+2

            if trials[i]['TRUTH_VALUE_1'] == key:
                valida[key] = valida[key]+1

            if trials[i]['TRUTH_VALUE_2'] == key:
                valida[key] = valida[key]+1

            if trials[i]['PREDICATE_TYPE'] == key:
                valida[key] = valida[key]+2

            if trials[i]['IMAGE_TYPE'] == key:
                valida[key] = int(valida[key])+2

                
    valida['Total'] = (i+1)*2

    print '\n'
    print 'study: ' +str(trials[0]['STUDY'])
    print 'group: ' +str(trials[0]['GROUP'])
    
    print valida
