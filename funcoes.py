(ALPHABET, TRANSITION_FUNCTION, START_STATE, FINAL_STATES) = range(4)


def manipulararquivo(arquivo, tipo):
    abrirarquivo = (open(arquivo, tipo))
    lerarquivo = abrirarquivo.read()
    abrirarquivo.close()
    return lerarquivo


def gerarlista(arquivo, tipo):
    lista = manipulararquivo(arquivo, tipo)
    listaseparada = lista.split(" ")
    return listaseparada


def validate_string(machine, strings):
    for string in strings:
        if string in machine[ALPHABET]:
            return True
        else:
            return False


def process_string(machine, strings):
    if not validate_string(machine, strings):
        return None

    state = machine[START_STATE]
    for string in strings:
        try:
            state = machine[TRANSITION_FUNCTION][state][string]
        except:
            return None

    return state in machine[FINAL_STATES]


def sepa(entrada, reservadas, simbolos, numericos, tipos, listavariaveis):
    alphabet = reservadas + simbolos + numericos + tipos + listavariaveis
    print(f'alfabeto: {alphabet}')

    trans_func = {'q0': {'sepa': 'c0'},
                  'c0': {'(': 'c1'},
                  'c1': {tipos[0]: 'c2', listavariaveis[0]: 'c3'},
                  'c2': {listavariaveis[0]: 'c3'},
                  'c3': {simbolos[1]: 'c4'},
                  'c4': {listavariaveis[0]: 'c5', numericos[0]: 'c6'},
                  'c5': {')': 'c7'},
                  'c6': {')': 'c7'},
                  'c7': {'{': 'c8'},
                  'c8': {'}': 'q0'}}

    #print(f'trans_func: {trans_func}')

    start_state = 'q0'
    final_states = (['q0'])
    machine = (alphabet, trans_func, start_state, final_states)
    strings = entrada

    result = process_string(machine, strings)

    if result is not None:
        for string in strings:
            print(f'{result}: {string}')
    else:
        print("\nERROR")
