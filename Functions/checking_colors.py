def checking_colors(TRIAL_INFO,colors):
    import random
    TRIAL_INFO['Color_1'] = random.choice(colors.keys())
    TRIAL_INFO['Color_2'] = random.choice(colors.keys())

    TRIAL_INFO['False_Color_2'] = random.choice(colors.keys())
    while TRIAL_INFO['Color_2'] == TRIAL_INFO['False_Color_2']:
        TRIAL_INFO['False_Color_2'] = random.choice(colors.keys())

    TRIAL_INFO['False_Color_1'] = random.choice(colors.keys())
    while TRIAL_INFO['Color_1'] == TRIAL_INFO['False_Color_1']:
        TRIAL_INFO['False_Color_1'] = random.choice(colors.keys())

    return TRIAL_INFO
