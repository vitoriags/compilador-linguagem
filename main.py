# compilador
from funcoes import *

listareservadas = gerarlista('palavrasreservadas.cha', 'r')
listasimbolos = gerarlista('simbolos.cha', 'r')
listatipos = gerarlista('tipos.cha', 'r')
dicionario = gerarlista('dicionario.cha', 'r')

traducaointeira = open('entrada.txt', 'r')
traducaointeira = traducaointeira.read()
entrada = traducaointeira.replace(" ", "")

lista = entrada[0]

flag = False
indice = 0
listavariaveis = []
listatextos = []
listalexico = []

reservadas = []
simbolos = []
tipos = []
numericos = []

num = ''
inp = []
traducao = ''

while indice < len(entrada):
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
        if entrada[indice - 1].isnumeric() or entrada[indice + 1].isnumeric():
            num += lista

        else:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
            numericos.append(lista)
            inp.append('número')

        flag = True

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        tipos.append(lista)
        inp.append('tipo')
        flag = True

    elif entrada[indice + 1] in listasimbolos:
        if 'obaguieesse' in reservadas or inp[0] == 'tipo':
            if '#' in entrada and entrada[indice + 1] == '>':
                listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                listavariaveis.append(lista)
                inp.append('variável')

            elif entrada[indice + 1] == '"' or entrada[indice + 1] == "'" or entrada[indice + 1] == '<':
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

        flag = True

    else:
        if indice < len(entrada):
            lista = lista + entrada[indice + 1]

    if flag:
        if indice < len(entrada) - 1:
            lista = entrada[indice + 1]
        else:
            pass

    indice += 1

if num != '':
    listalexico.append(f'Símbolo [frag = {num}, tipo = numérico]')
    numericos.append(num)


print()
stringlexico = ', '.join(map(str, listalexico))
print(f'Léxico: {stringlexico}')
print('')

# print(f'entrada: {inp}')
# print('')

print(f'reservadas: {reservadas}')
print(f'tipos: {tipos}')
print(f'números: {numericos}')
print(f'simbolos: {simbolos}')
print(f'textos: {listatextos}')
print(f'variáveis: {listavariaveis}')
print(f'entrada: {inp}')

trad = 'printf("'
t = 0
v = 0
val = ', '.join(listavariaveis)

if inp[0] == 'sepa':
    if sepa(inp):
        traducaointeira = traducaointeira.replace("sepa", "if")
        for t in tipos:
            if t in listatipos:
                traducaointeira = traducaointeira.replace(f'{t}', f'{dicionario[dicionario.index(t) + 1]}')
    print(f'Tradução: {traducaointeira}')

elif inp[0] == 'obaguieesse':
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


# elif inp[0] == 'ocorre':
#     ocorre(inp)
#
# elif inp[0] == 'vaivenafita':
#     vaivenafita(inp)
#
# elif inp[0] == 'meteoloco':
#     meteoloco(inp)
#
# elif inp[0] in listatipos:
#     atribuicao(inp)