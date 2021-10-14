(ALPHABET, TRANSITION_FUNCTION, START_STATE, FINAL_STATES) = range(4)


def manipularArquivo(arquivo, tipo):
    abrirarquivo = (open(arquivo, tipo))
    lerarquivo = abrirarquivo.read()
    abrirarquivo.close()
    return lerarquivo


def gerarLista(arquivo, tipo):
    lista = manipularArquivo(arquivo, tipo)
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


def vaivenafita(entrada):
    alphabet = ['vaivenafita', '(', 'variável', ')', ';']
    trans_func = {'q0': {'vaivenafita': 'sc1'},
                  'sc1': {'(': 'sc2'},
                  'sc2': {'variável': 'sc3'},
                  'sc3': {')': 'sc4'},
                  'sc4': {';': 'q0'}}

    start_state = 'q0'
    final_states = {'q0'}
    machine = (alphabet, trans_func, start_state, final_states)

    result = process_string(machine, entrada)
    if result is not None and result is not False:
        for string in entrada:
            print(f'{result}: {string}')
    else:
        print("Entrada não válida")


def ocorre(entrada):
    alphabet = ['ocorre', '(', 'tipo', 'variável', ';', '=', 'número', '<', '>', ')', '{', '}', '+']
    trans_func = {'q0': {'ocorre': 'f0'},
                  'f0': {'(': 'f1'},
                  'f1': {'tipo': 'f2', ';': 'f7', 'variável': 'f3'},
                  'f2': {'variável': 'f3'},
                  'f3': {'=': 'f4'},
                  'f4': {'número': 'f5', 'variável': 'f6'},
                  'f5': {';': 'f7'},
                  'f6': {';': 'f7'},
                  'f7': {'variável': 'f8'},
                  'f8': {'<': 'f9', '>': 'f9'},
                  'f9': {'=': 'f10', 'número': 'f11', 'variável': 'f12'},
                  'f10': {'número': 'f11', 'variável': 'f12'},
                  'f11': {';': 'f13'},
                  'f12': {';': 'f13'},
                  'f13': {'variável': 'f14', '+': 'f17', '-': 'f17'},
                  'f14': {'+': 'f15', '-': 'f15'},
                  'f15': {'=': 'f16', '+': 'f20', '-': 'f20'},
                  'f16': {'variável': 'f19', 'número': 'f20'},
                  'f17': {'+': 'f18', '-': 'f18'},
                  'f18': {'variável': 'f20'},
                  'f19': {')': 'f21'},
                  'f20': {')': 'f21'},
                  'f21': {'{': 'f22'},
                  'f22': {'}': 's6'}}

    start_state = 'q0'
    final_states = {'s6'}
    machine = (alphabet, trans_func, start_state, final_states)

    result = process_string(machine, entrada)
    if result is not None and result is not False:
        for string in entrada:
            print(f'{result}: {string}')
    else:
        print("Entrada não válida")
