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


def validate_string(machine, string):
    if string in machine[ALPHABET]:
        return True
    else:
        return False


def process_string(machine, strings):
    state = machine[START_STATE]

    for string in strings:
        if not validate_string(machine, string):
            return None
        try:
            state = machine[TRANSITION_FUNCTION][state][string]
        except:
            return None

    return state in machine[FINAL_STATES]

def sepa(entrada):

    alphabet = ['sepa', 'tipo', 'variável', 'número', '(', ')', '{', '}', '<', '>', '*', '+', '-', '=']

    trans_func = {'q0': {'sepa': 'c0'},
                  'c0': {'(': 'c1'},
                  'c1': {'tipo': 'c2', 'variável': 'c3', 'número': 'c3'},
                  'c2': {'variável': 'c3'},
                  'c3': {'<': 'c4', '>': 'c4', '=': 'c4'},
                  'c4': {'número': 'c6', '=': 'c5', 'variável': 'c7'},
                  'c5': {'número': 'c6', 'variável': 'c7'},
                  'c6': {')': 'c8'},
                  'c7': {')': 'c8'},
                  'c8': {'{': 'c9'},
                  'c9': {'}': 'q0'}}

    start_state = 'q0'
    final_states = (['q0'])
    machine = (alphabet, trans_func, start_state, final_states)
    strings = entrada

    result = process_string(machine, strings)

    if result is not False and result is not None:
        for string in strings:
            print(f'{result}: {string}')
    else:
        print("\nERROR")


def obaguieesse(entrada):

    alphabet = ['obaguieesse', 'variável', 'número', 'texto', '(', ')', '<', '>', '#', ';', '"']

    trans_func = {'q0': {'obaguieesse': 'p0'},
                  'p0': {'(': 'p1'},
                  'p1': {'"': 'p2', 'variável': 'p4', '#': 'p6'},
                  'p2': {'texto': 'p3'},
                  'p3': {'"': 'p4'},
                  'p4': {')': 'p5'},
                  'p5': {';': 'q0'},
                  'p6': {'"': 'p7'},
                  'p7': {'texto': 'p8', '<': 'p9'},
                  'p8': {'<': 'p9', '"': 'p12'},
                  'p9': {'variável': 'p10'},
                  'p10': {'>': 'p11'},
                  'p11': {'texto': 'p8', '<': 'p9', '"': 'p12'},
                  'p12': {')': 'p5'}}

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
