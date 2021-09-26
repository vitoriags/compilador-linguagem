def manipularArquivo(arquivo, tipo):
    abrirarquivo = (open(arquivo, tipo))
    lerarquivo = abrirarquivo.read()
    abrirarquivo.close()
    return lerarquivo


def gerarLista(arquivo, tipo):
    lista = manipularArquivo(arquivo, tipo)
    listaseparada = lista.split(" ")
    # print (listaseparada, '\n')
    return listaseparada


def validate_string(string, machine):

    if string in machine[ALPHABET]:
        return True
    elif string in machine[ALPHABET][2][0]:
        return True
    return False


(
    ALPHABET,
    TRANSITION_FUNCTION,
    START_STATE,
    FINAL_STATES
) = range(4)


def process_string(machine, strings, listavar):
    state = machine[START_STATE]
    for char in strings:
        print(char)
        if not validate_string(char, machine):
            return None  # Processamento do automato.

        try:
            state = machine[TRANSITION_FUNCTION][state][char]
        except:
            return None
        print(state)

    return state in machine[FINAL_STATES]


def vaivenafita(inp, listavar):
    alphabet = ['vaivenafita', '(', listavar[0], ')', ';']
    trans_func = {'q0': {'vaivenafita': 'sc1'},
                  'sc1': {'(': 'sc2'},
                  'sc2': {listavar[0]: 'sc3'},
                  'sc3': {')': 'sc4'},
                  'sc4': {';': 'q0'}}

    start_state = 'q0'
    final_states = {'q0'}
    machine = (alphabet, trans_func, start_state, final_states)

    result = process_string(machine, inp, listavar)
    if result is not None:
        print(f'Machine: {machine}')
    else:
        print('Fora de ordem')
