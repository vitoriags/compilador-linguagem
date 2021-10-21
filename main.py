# compilador
from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')
dicionario = gerarLista('dicionario.cha', 'r')

entrada = input().replace(" ", "")
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
        reservadas.append(lista)
        listalexico.append(f'Símbolo [frag = {lista}, tipo = palavra reservada]')
        flag = True
        inp.append(lista)
        traducao += dicionario[dicionario.index(lista)+1]

    elif lista in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = símbolo]')
        simbolos.append(lista)
        inp.append(lista)
        traducao += lista + ' '
        flag = True

    elif lista in listavariaveis:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        inp.append('variável')
        traducao += lista + ' '
        flag = True

    elif lista.isnumeric():
        if entrada[indice + 1].isnumeric():
            num += lista + entrada[indice + 1]
            listalexico.append(f'Símbolo [frag = {num}, tipo = numérico]')
            numericos.append(num)

        else:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
            numericos.append(lista)
            inp.append('número')
            traducao += lista + ' '
            num = ''
        flag = True

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        tipos.append(lista)
        inp.append('tipo')
        print(f'lista: {lista}')
        traducao += dicionario[dicionario.index(lista)+1] + ' '
        flag = True

    elif entrada[indice + 1] in listasimbolos:
        if 'obaguieesse' in reservadas:
            if entrada[12] == '#' and entrada[indice + 1] == '>':
                listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                listavariaveis.append(lista)
                inp.append('variável')
                traducao += lista + ' '

            elif entrada[indice + 1] == '"' or entrada[indice + 1] == "'" or entrada[indice + 1] == '<':
                listalexico.append(f'Símbolo [frag = {lista}, tipo = texto]')
                listatextos.append(lista)
                inp.append('texto')
                traducao += lista + ' '

            else:
                listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
                listavariaveis.append(lista)
                inp.append('variável')
                traducao += lista + ' '

        else:
            listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
            listavariaveis.append(lista)
            inp.append('variável')
            traducao += lista + ' '

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

print('')
print(f'para a tradução: {traducao}')
print('')

# if inp[0] == 'sepa':
#     sepa(inp)
# elif inp[0] == 'obaguieesse':
#     obaguieesse(inp)
# elif inp[0] == 'ocorre':
#     ocorre(inp)
# elif inp[0] == 'vaivenafita':
#     vaivenafita(inp)
# elif inp[0] == 'meteoloco':
#     meteoloco(inp)
# elif inp[0] in listatipos:
#     atribuicao(inp)
