from bs4 import BeautifulSoup
import pandas as pd
import os

# elementos a serem buscados dentro do "process"
outerElements = ['association', 'startEvent', 'intermediateCatchEvent', 'intermediateThrowEvent', 'endEvent',
                 'exclusiveGateway',
                 'parallelGateway', 'complexGateway', 'eventBasedGateway', 'inclusiveGateway', 'task', 'sendTask',
                 'receiveTask', 'userTask', 'manualTask', 'businessRuleTask', 'serviceTask', 'scriptTask',
                 'callActivity', 'subProcess', 'transaction', 'adHocSubProcess', 'dataObjectReference',
                 'dataStoreReference', 'boundaryEvent',
                 'textAnnotation', 'collaboration', 'laneSet', 'sequenceFlow', 'group']
eventDefinitions = ['messageEventDefinition', 'timerEventDefinition', 'conditionalEventDefinition',
                    'signalEventDefinition', 'linkEventDefinition', 'escalationEventDefinition',
                    'compensateEventDefinition', 'errorEventDefinition', 'terminateEventDefinition',
                    'cancelEventDefinition']
# lista de elementos a serem buscados dentro do "colaboration"
collabElements = ['participant', 'messageFlow', 'association', 'textAnnotation', 'group']
# definitions
intermediateCatchEventDefinitions = eventDefinitions[0:5]
startEventDefinitions = eventDefinitions[0:4]
intermediateThrowEventDefinitions = [eventDefinitions[i] for i in [0, 3, 4, 5, 6]]
endEventDefinitions = [eventDefinitions[i] for i in [0, 3, 5, 6, 7, 8]]
boundaryEventDefinitions = [eventDefinitions[i] for i in [0, 1, 2, 3, 5, 6, 7, 9]] + [eventDefinitions[i] +
                                                                                      'NonInterrupting' for i in
                                                                                      [0, 1, 2, 3, 5, 6, 7, 9]]
taskDefinitions = ['multiInstanceLoopCharacteristics', 'standardLoopCharacteristics']
multiInstanceTypes = ['multiInstanceLoopSequential', 'multiInstanceLoopParallel']

colunas = ['Collaboration_id', 'file', 'Process_id', 'Element_type', 'Element_id', 'Element_name', 'Element_definition',
           'Definition_id', 'is_sub', 'In', 'Out', 'text', 'ProcessRef', 'attachedToRef', 'cancelActivity',
           'LoopCharacteristics', 'isSequential', 'categoryValueRef', 'Group']


# função de coleta de elementos acionada pela função buscador
def elements(df, Element, aux, k, filename, co_id, h=None, sub=None, category=None):
    # passos padrão
    df = df.append({'is_sub': sub, 'Process_id': h, 'Element_type': k, 'file': filename,
                    'Collaboration_id': co_id}, ignore_index=True)
    x = Element.attrs
    df.at[aux, 'Element_id'] = x.get('id')
    df.at[aux, 'Element_name'] = x.get('name')
    df.at[aux, 'attachedToRef'] = x.get('attachedToRef')
    df.at[aux, 'cancelActivity'] = x.get('cancelActivity')
    df.at[aux, 'In'] = x.get('sourceRef')
    df.at[aux, 'Out'] = x.get('targetRef')
    df.at[aux, 'ProcessRef'] = x.get('processRef')

    # passos a mais que devem ser dados em alguns casos

    if k.endswith('Event'):
        for inner in (startEventDefinitions or boundaryEventDefinitions):
            result = Element.find(inner)
            if result:
                df.at[aux, 'Element_definition'] = inner
                df.at[aux, 'Definition_id'] = result.attrs.get('id')
    elif k.endswith('task') or k.endswith(
            'Task') or k == 'callActivity' or k == 'subProcess' or k == 'adHocSubProcess' or k == 'transaction':
        for inner in taskDefinitions:
            result = Element.find(inner)
            if result:
                df.at[aux, 'LoopCharacteristics'] = inner
                df.at[aux, 'isSequential'] = result.attrs.get('isSequential')
    elif k == 'textAnnotation':
        result = Element.find('text')
        if result:
            df.at[aux, 'text'] = result.contents[0]
    elif k == 'group':
        df.at[aux, 'categoryValueRef'] = Element.attrs.get('categoryValueRef')
        result = category.find_all('categoryValue')
        if result:
            for grp in result:
                if grp.attrs.get('id') == Element.attrs.get('categoryValueRef'):
                    df.at[aux, 'Group'] = grp.attrs.get('value')
    return df


# função que varre o interior do processo buscando elementos
def buscador(df_saida, tag, filename, co_id, sub=False, categ=None):
    # define se estamos tratando de um Process ou de um Collaboration
    if tag.get('id').startswith('Collaboration'):
        lista = collabElements
        h = None
        sub = None
    else:
        h = tag.get('id')
        lista = outerElements

    # cria lista com todos os elementos que podem aparecer no interior da tag e cada uma de suas apariçoes
    rawcatch = {x: [] for x in lista}
    for outerElement in lista:
        rawcatch[outerElement] += tag.find_all(outerElement, recursive=False)
    # k = Element_type e v = lista com todas as aparições desse elemento
    for k, v in rawcatch.items():
        df = pd.DataFrame(columns=colunas)
        if k == 'laneSet':  # todas as lanes de uma pool ficam dentro do laneSet
            for laneSet in v:
                found = laneSet.find_all('lane', recursive=False)
                aux = 0
                for x in found:
                    df = elements(df, x, aux, 'lane', filename, co_id, h=h, sub=sub)
                    aux += 1
                df_saida = df_saida.append(df, ignore_index=True)

        elif k == 'subProcess' or k == 'adHocSubProcess' or k == 'transaction':
            aux = 0
            # para cada subprocesso apos o registro é feita uma nova chamada da funçao buscador
            for subProcess in v:
                df = elements(df, subProcess, aux, k, filename, co_id, h, sub)
                aux += 1
                df_saida = df_saida.append(df, ignore_index=True)
                df_sub = pd.DataFrame(columns=colunas)
                df_sub = buscador(df_sub, subProcess, filename, co_id, sub=True)
                df_saida = df_saida.append(df_sub, ignore_index=True)
        # os demais elementos nao precisam de "tratamento especial"
        else:
            aux = 0
            for element in v:
                df = elements(df, element, aux, k, filename, co_id, h, sub, category=categ)
                aux += 1
            df_saida = df_saida.append(df, ignore_index=True)

    return df_saida


def extractor(pathways, output_location):
    df_out = pd.DataFrame(columns=colunas)  # Cria o dataframe
    for pathway in pathways:  # para cada arquivo:
        with open(pathway, 'r', encoding='utf8') as file:
            content = "".join(file.readlines())
            soup = BeautifulSoup(content, 'xml')  # 'xml' setting needed to interpret .bpmn files
            category = soup.find('category')
            processes = soup.find_all('process')  # File should have 1,however some modelers add empty processes
            collaborations = soup.find('collaboration')
            for processo in processes:  # o mesmo arquivo pode conter varios processos (Pools)
                df_out = buscador(df_out, processo, pathway, collaborations.get('id'))

            df_out = buscador(df_out, collaborations, pathway, collaborations.get('id'),
                              categ=category)  # cada arquivo possui somente um collaborations

        df_out = df_out.set_index('file')
        df_out.to_csv(output_location)  # Final result of execution
        break
