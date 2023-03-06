import pandas as pd
from googletrans import Translator

translator = Translator()
toClassify = []

colunas = ['Collaboration_id', 'Element_type', 'Element_id', 'Name', 'Element_definition',
           'is_sub', 'cancelActivity', 'LoopCharacteristics', 'isSequential', "% g translate"]


def english_check(text):
    verificador = translator.detect(text)
    if 'en' in verificador.lang:
        if type(verificador.confidence) == list:
            porcentagem = verificador.confidence[verificador.lang.index('en')]
        else:
            porcentagem = verificador.confidence
        return porcentagem
    else:
        return 0


def pre_classify(file_in, file_out, selected, tradutor):
    dataframe_in = pd.read_csv(file_in)

    # remover elementos sem texto
    dataframe_in = dataframe_in[
        dataframe_in['Element_name'].notna() + dataframe_in['Group'].notna() + dataframe_in['text'].notna()]

    dataframe_in = dataframe_in.reset_index(drop=True)

    # remover selecionados
    for x in selected:
        dataframe_in = dataframe_in[dataframe_in['Element_type'] != x]

    # agregar textos na mesma coluna  Name
    dataframe_in.loc[dataframe_in['Element_type'] == 'group', 'Name'] = dataframe_in['Group']
    dataframe_in.loc[dataframe_in['Element_type'] == 'textAnnotation', 'Name'] = dataframe_in['text']
    dataframe_in.loc[dataframe_in['Name'].isna(), 'Name'] = dataframe_in['Element_name']
    if tradutor:
        dataframe_in['% g translate'] = dataframe_in["Name"].apply(english_check)
        dataframe_non_english = dataframe_in[dataframe_in['% g translate'] == 0]
        dataframe_non_english.to_csv('Non_english.csv', index=False)
        dataframe_in = dataframe_in[dataframe_in['% g translate'] != 1]

    dataframe_out = pd.DataFrame(columns=colunas, data=dataframe_in)
    dataframe_out = dataframe_out.sample(frac=1, random_state=2022).reset_index(drop=True)

    dataframe_out['Classified'] = False
    dataframe_out.to_csv(file_out, index=False)

    return dataframe_out
