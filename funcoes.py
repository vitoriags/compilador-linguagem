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


def sepa(entrada):

    alphabet = ['reservada', 'tipo', 'símbolo', 'variável', 'número']

    trans_func = {'q0': {'reservada': 'c0'},
                  'c0': {'símbolo': 'c1'},
                  'c1': {'tipo': 'c2', 'variável': 'c3', 'número': 'c3'},
                  'c2': {'variável': 'c3'},
                  'c3': {'símbolo': 'c4'},
                  'c4': {'número': 'c6', 'símbolo': 'c5', 'variável': 'c7'},
                  'c5': {'número': 'c6', 'variável': 'c7'},
                  'c6': {'símbolo': 'c8'},
                  'c7': {'símbolo': 'c8'},
                  'c8': {'símbolo': 'c9'},
                  'c9': {'símbolo': 'q0'}}

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


def obaguieesse(entrada):

    alphabet = ['reservada', 'tipo', 'símbolo', 'variável', 'número', 'texto']

    trans_func = {'q0': {'reservada': 'p0'},
                  'p0': {'símbolo': 'p1'},
                  'p1': {'símbolo': 'p2', 'variável': 'p4', 'símbolo': 'p6'},
                  'p2': {'texto': 'p3'},
                  'p3': {'símbolo': 'c4'},
                  'p4': {'símbolo': 'p5'},
                  'p5': {'símbolo': 'q0'},
                  'p6': {'símbolo': 'p7'},
                  'p7': {'texto': 'p8', 'símbolo': 'p9'},
                  'p8': {'símbolo': 'p9', 'símbolo': 'p12'},
                  'p9': {'variável': 'p10'},
                  'p10': {'símbolo': 'p11'},
                  'p11': {'texto': 'p8', 'símbolo': 'p9', 'símbolo': 'p12'},
                  'p12': {'símbolo': 'p5'}}

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
