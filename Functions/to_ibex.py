
def to_ibex(TRIAL_INFO, CONTROLLER_1, CONTROLLER_2):
    coma = ','
    guion = '_'
    divisor1 = '\''
    divisor2 = '\"'
    image_path = "https://dl.dropboxusercontent.com/u/13340774/Images/"

    CODE1 = divisor1+TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_1']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+guion+TRIAL_INFO['N1']+guion+TRIAL_INFO['PREDICATE_1']+divisor1
    IMAGE = "html:" + divisor2 + "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_1'] + divisor1 + "border=\'2\'>"+"</center> " + divisor2
    CONTRO1= "{html: \"<center>"+TRIAL_INFO['S1']+'</center>\"},'
    SENTENCE2= "q:"+ '\"'+ TRIAL_INFO['S1']+ '\"'
    CONTROL2 = "{" + IMAGE + coma + SENTENCE2 + '}'
    data_line_1 = '[' + CODE1 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTRO1 + divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    CODE2 = divisor1 + TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_2']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+guion+TRIAL_INFO['N2']+guion+TRIAL_INFO['PREDICATE_2']+divisor1
    IMAGE = "html:" + divisor2 + "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_2'] + divisor1 + "border=\'2\'>"+ "</center>" + divisor2
    CONTRO1= "{html: \"<center>"+TRIAL_INFO['S2']+'</center>\"},'
    SENTENCE2= "q:"+ '\"'+ TRIAL_INFO['S2']+ '\"'
    CONTROL2 = "{" + IMAGE + coma + SENTENCE2+ '}'
    data_line_2 = '[' + CODE2 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTRO1 +  divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    return data_line_1, data_line_2


def to_ibex2(TRIAL_INFO, CONTROLLER_1, CONTROLLER_2):
    coma = ','
    guion = '_'
    divisor1 = '\''
    divisor2 = '\"'
    image_path = "http://cogexpe.scicog.fr/PSIM/Non-Max/"


    CODE1 = divisor1+TRIAL_INFO['STUDY']+guion+TRIAL_INFO['GROUP'][0]+TRIAL_INFO['GROUP'][1]+guion+TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_1']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+guion+TRIAL_INFO['N1']+guion+TRIAL_INFO['PREDICATE_1']+divisor1
    IMAGE =  "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_1'] + divisor1 + "border=\'2\'>"+"</center> " + divisor2
    CONTROL1= "{html: \"<center>"+TRIAL_INFO['S1']+'</center>' + "<br> <center> <img src=" + divisor1 + 'https://dl.dropboxusercontent.com/u/13340774/Images/white.png' + divisor1 + " border=\'2\'>"+"</center>" + divisor2 + "},"
    SENTENCE1= "html:" + divisor2 + "<center>"+TRIAL_INFO['S1']+'</center> <br>'
    SENTENCE2= "q:"+ divisor1 + TRIAL_INFO['S1'] + divisor1
    CONTROL2 = "{" + SENTENCE1 + IMAGE + coma + SENTENCE2 + '}'
    data_line_1 = '[' + CODE1 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTROL1 + divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    CODE2 = divisor1 + TRIAL_INFO['STUDY']+guion+TRIAL_INFO['GROUP'][0]+TRIAL_INFO['GROUP'][1]+guion+TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_2']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+guion+TRIAL_INFO['N2']+guion+TRIAL_INFO['PREDICATE_2']+divisor1
    IMAGE =  "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_2'] + divisor1 + "border=\'2\'>"+"</center> " + divisor2
    CONTROL1= "{html: \"<center>"+TRIAL_INFO['S2']+'</center>' + "<br> <center> <img src=" + divisor1 + 'http://cogexpe.scicog.fr/PSIM/Non-Max/white.png' + divisor1 + " border=\'2\'>"+"</center>" + divisor2 + "},"
    SENTENCE1= "html:" + divisor2 + "<center>"+TRIAL_INFO['S2']+'</center> <br>'
    SENTENCE2= "q:"+ divisor1 + TRIAL_INFO['S2'] + divisor1
    CONTROL2 = "{" + SENTENCE1 + IMAGE + coma + SENTENCE2+ '}'
    data_line_2 = '[' + CODE2 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTROL1 + divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    return data_line_1, data_line_2


def to_ibex_validation(TRIAL_INFO, CONTROLLER_1, CONTROLLER_2):
    coma = ','
    guion = '_'
    divisor1 = '\''
    divisor2 = '\"'
    image_path = "https://dl.dropboxusercontent.com/u/13340774/Images/"


    CODE1 = divisor1+TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_1']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+divisor1
    IMAGE =  "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_1'] + divisor1 + "border=\'2\'>"+"</center> " + divisor2
    CONTROL1= "{html: \"<center>"+TRIAL_INFO['S1']+'</center>' + "<br> <center> <img src=" + divisor1 + 'https://dl.dropboxusercontent.com/u/13340774/Images/white.png' + divisor1 + " border=\'2\'>"+"</center>" + divisor2 + "},"
    SENTENCE1= "html:" + divisor2 + "<center>"+TRIAL_INFO['S1']+'</center> <br>'
    SENTENCE2= "q:"+  CODE1
    CONTROL2 = "{" + SENTENCE1 + IMAGE + coma + SENTENCE2 + '}'
    data_line_1 = '[' + CODE1 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTROL1 + divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    CODE2 = divisor1+TRIAL_INFO['CONDITION']+guion+TRIAL_INFO['TRUTH_VALUE_2']+guion+TRIAL_INFO['IMAGE_TYPE']+guion+TRIAL_INFO['PREDICATE_TYPE']+divisor1
    IMAGE =  "<center> <img src=" + divisor1 + image_path + TRIAL_INFO['IMAGE_2'] + divisor1 + "border=\'2\'>"+"</center> " + divisor2
    CONTROL1= "{html: \"<center>"+TRIAL_INFO['S2']+'</center>' + "<br> <center> <img src=" + divisor1 + 'https://dl.dropboxusercontent.com/u/13340774/Images/white.png' + divisor1 + " border=\'2\'>"+"</center>" + divisor2 + "},"
    SENTENCE1= "html:" + divisor2 + "<center>"+TRIAL_INFO['S2']+'</center> <br>'
    SENTENCE2= "q:"+ CODE2
    CONTROL2 = "{" + SENTENCE1 + IMAGE + coma + SENTENCE2+ '}'
    data_line_2 = '[' + CODE2 + coma + divisor2 + CONTROLLER_1 + divisor2 + coma + CONTROL1 + divisor2 + CONTROLLER_2 + divisor2 + coma + CONTROL2 + ']'

    return data_line_1, data_line_2
