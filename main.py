# compilador
from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')

entrada = input().replace(" ", "")
lista = entrada[0]

# ocorre(        ; x<5;  x++)
# ocorre(     x=0; x<5;  x++)
# ocorre(mano x=x; x<x;  x++)
# ocorre(mano x=0; x<5;  ++x)
# ocorre(mano x=0; x<=5; x++)
# ocorre(mano x=0; x<=5; x+=2)
# ocorre(mano x=0; x<=5; x+=x)

# vaivenafita(x);


flag = False
indice = 0
listavariaveis = []
listalexico = []
inp = []

while indice < len(entrada):
    print(f'{lista}, indice: {indice}')
    flag = False
    if lista in listareservadas and lista not in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = palavra reservada]')
        flag = True
        inp.append(lista)

    elif lista in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = símbolo]')
        flag = True
        inp.append(lista)

    elif lista in listavariaveis:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        flag = True
        inp.append('variável')

    elif lista.isnumeric():
        listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
        flag = True
        inp.append('número')

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        lista = entrada[indice + 1]
        flag = True
        inp.append('tipo')
        # if lista.isnumeric():
        #     listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')

    elif entrada[indice + 1] in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        listavariaveis.append(lista)
        inp.append('variável')
        flag = True

    else:
        if indice < len(entrada):
            lista = lista + entrada[indice + 1]
    if flag == True:
        if indice < len(entrada) - 1:
            # print(f'passou {lista}, {indice}, {len(entrada)}')
            lista = entrada[indice + 1]
        else:
            # print("pass")
            pass
    indice += 1

# print(inp)

stringlexico = ', '.join(map(str, listalexico))
print(f'Léxico: {stringlexico}')

if inp[0] == 'vaivenafita':
    print('entrou vaivenafita')
    vaivenafita(inp)
else:
    print('entrou ocorre')
    ocorre(inp)
