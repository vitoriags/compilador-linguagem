# compilador
from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')
dicionario = gerarLista('dicionario.cha', 'r')

traducaointeira = open('entrada.txt', 'r')
traducaointeira = traducaointeira.read()
entrada = traducaointeira.replace(" ", "")

lista = entrada[0]

flag = False
indice = 0
aux = 0
listavariaveis = []
listatextos = []
listalexico = []

reservadas = []
simbolos = []
tipos = []
numericos = []
listaEntrada = []
saidaLexico = []
inp = []
listaTraducao = []

traducao = ''
num = ''
entry = ''

for cont in entrada:
    entry += cont
    if cont == '\n':
        entry = entry.replace("\n", "")
        listaEntrada.append(entry)
        entry = ''

entry = ''

for cont in traducaointeira:
    entry += cont
    if cont == '\n':
        entry = entry.replace("\n", "")
        listaTraducao.append(entry)
        entry = ''

print(f'listaEntrada: {(listaEntrada)}')

while aux < len(listaEntrada):
    indice = 0

    # Lexico
    while indice < len(listaEntrada[aux]):
        flag = False
        if lista in listareservadas and lista not in listatipos:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = palavra reservada]')
            reservadas.append(lista)
            inp.append(lista)
            flag = True

        elif lista in listasimbolos:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = símbolo]')
            simbolos.append(lista)
            inp.append(lista)
            flag = True

        elif lista in listavariaveis:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
            listavariaveis.append(lista)
            inp.append('variável')
            flag = True

        elif lista.isnumeric():
            if listaEntrada[aux][indice + 1].isnumeric():
                num += lista
            else:
                listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
                num += lista
                numericos.append(num)
                inp.append('número')
                num = ''

            flag = True

        elif lista in listatipos:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
            tipos.append(lista)
            inp.append('tipo')
            flag = True

        elif listaEntrada[aux][indice + 1] in listasimbolos:
            if 'obaguieesse' in reservadas or inp[0] == 'tipo':
                if listaEntrada[aux] == '#' and listaEntrada[aux][indice + 1] == '>':
                    listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                    listavariaveis.append(lista)
                    inp.append('variável')

                elif listaEntrada[aux][indice + 1] == '"' or listaEntrada[aux][indice + 1] == "'" or listaEntrada[aux][
                    indice + 1] == '<':
                    listalexico.append(f'Símbolo [frag = {lista}, tipo = texto]')
                    listatextos.append(lista)
                    inp.append('texto')

                else:
                    listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                    listavariaveis.append(lista)
                    inp.append('variável')

            else:
                listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                listavariaveis.append(lista)
                inp.append('variável')
                traducao += lista + ' '

            flag = True
        else:
            if indice < len(listaEntrada[aux]):
                lista = lista + listaEntrada[aux][indice + 1]

        if flag:
            if indice < len(listaEntrada[aux]) - 1:
                lista = listaEntrada[aux][indice + 1]
            else:
                pass
        indice += 1

    print()
    stringlexico = ', '.join(map(str, listalexico))
    print(f'Léxico: {stringlexico}')
    print('')

    print(f'entrada: {inp}')
    print('')

    print(f'reservadas: {reservadas}')
    print(f'tipos: {tipos}')
    print(f'números: {numericos}')
    print(f'simbolos: {simbolos}')
    print(f'textos: {listatextos}')
    print(f'variáveis: {listavariaveis}')
    print(f'entrada: {inp}\n')

    # Verificação Maquina de Estado


    if 'ocorre' in inp:
        if ocorre(inp):
            traducao = listaTraducao[aux].replace("ocorre", "for")
            for t in tipos:
                if t in listatipos:
                    traducao = traducao.replace(f'{t}', f'{dicionario[dicionario.index(t) + 1]}')
            print(f'tradução: {traducao}')

    elif 'vaivenafita' in inp:
        trad = ''
        if vaivenafita(inp):
            if vaivenafita(inp):
                for x in inp:
                    if x == 'variável':
                        trad += f"scanf('%s', &{listavariaveis[0]});"
                    else:
                        pass
                print(f'Tradução: {trad}')

            else:
                print('Error 489')

    elif 'sepa' in inp:
        if sepa(inp):
            traducao = listaTraducao[aux].replace("sepa", "if")
            for t in tipos:
                if t in listatipos:
                    traducao = traducao.replace(f'{t}', f'{dicionario[dicionario.index(t) + 1]}')
        print(f'Tradução: {traducao}')

    elif 'obaguieesse' in inp:
        trad = 'printf("'
        t = 0
        v = 0
        val = ', '.join(listavariaveis)
        if obaguieesse(inp):
            if '<' in inp and '"' in inp:
                for x in inp:
                    if x == 'variável':
                        trad += '%s '
                    elif x == 'texto':
                        trad += f'{listatextos[t]} '
                        t += 1

                trad += f'", {val});'
                print(f'Tradução: {trad}')

            elif len(listavariaveis) == 1:
                print(f'Tradução: printf("%s", {listavariaveis[0]})')

            else:
                print(f'Tradução: printf("{listatextos[0]}");')

    aux += 1
    try:
        lista = listaEntrada[aux][0]
    except:
        pass

    listalexico = []
    reservadas = []
    tipos = []
    numericos = []
    simbolos = []
    listatextos = []
    listavariaveis = []
    inp = []

