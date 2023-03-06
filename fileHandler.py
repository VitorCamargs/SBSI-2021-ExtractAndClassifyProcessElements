import pandas as pd


def img_file(df, aux):
    tipo = df.at[aux, 'Element_type']
    if tipo.endswith('Event'):
        if tipo == 'boundaryEvent':
            if type(df.at[aux, 'cancelActivity']) == str:
                tipo = 'nonInterruptingEvent'
            else:
                tipo = 'IntermediateCatchEvent'
        if type(df.at[aux, 'Element_definition']) == str:
            return 'imagens\\' + tipo + '-' + df.at[aux, 'Element_definition'] + '.png', ''

        else:
            return 'imagens\\' + tipo + '.png', ''

    elif tipo.endswith('task') or tipo.endswith('Task') or tipo in ['callActivity', 'subProcess', 'adHocSubProcess',
                                                                    'transaction']:
        if type(df.at[aux, 'LoopCharacteristics']) == str:
            if df.at[aux, 'LoopCharacteristics'] == 'standardLoopCharacteristics':
                return 'imagens\\' + tipo + '.png', 'imagens\\Loop.png'
            else:
                if df.at[aux, 'isSequential']:
                    return 'imagens\\' + tipo + '.png', 'imagens\\sequential.png'
                else:
                    return 'imagens\\' + tipo + '.png', 'imagens\\parallel.png'
        else:
            return 'imagens\\' + tipo + '.png', ''
    else:
        return 'imagens\\' + tipo + '.png', ''


errors_list = ['Orthography', 'Language', 'Others']
categories = ['Process Participants', 'System, tools, and technologies', 'Processed documents and information']
classifications = ['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree']

colunas = ['Collaboration_id', 'Element_type', 'Element_id', 'Name', 'Element_definition',
           'is_sub', 'cancelActivity', 'LoopCharacteristics', 'isSequential',
           'Who_Classified', '% g translate']
colunas.extend(categories)
colunas.extend(errors_list)


def openfile(filename):
    try:
        dataframe = pd.read_csv(filename)

        if dataframe[dataframe["Classified"] == False].shape[0] == 0:
            return 'File already fully classified'
    except KeyError:
        return 'File missing column "Classify" check if it is a valid input'

    try:
        dataframe[categories[0]]
    except KeyError:
        for key in categories:
            dataframe[key] = pd.Series(float)
        for key in ['Who_Classified', 'timestamp']:
            dataframe[key] = pd.Series(str())
        for key in errors_list:
            dataframe[key] = pd.Series(bool)

    return dataframe
