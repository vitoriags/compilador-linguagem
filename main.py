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
# ocorre(mano x>0; x<5;  ++x)
# ocorre(mano x=0; x<=5; x++)
# ocorre(mano x>0; x<=5; x+=2)
# ocorre(mano x>0; x<=5; x+=x)


flag = False
indice = 0
listavariaveis = []
listalexico = []

while indice < len(entrada):
    print(f'{lista}, indice: {indice}')
    flag = False
    if lista in listareservadas and lista not in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = palavra reservada]')
        flag = True

    elif lista in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = símbolo]')
        flag = True

    elif lista in listavariaveis:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        flag = True

    elif lista.isnumeric():
        listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
        flag = True

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        flag = True

    elif entrada[indice + 1] in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        flag = True

    else:
        if indice < len(entrada):
            lista = lista + entrada[indice + 1]

    if flag == True:
        if indice < len(entrada) - 1:
            lista = entrada[indice + 1]
        else:
            pass

    indice += 1

print()
stringlexico = ', '.join(map(str, listalexico))
print(f'Léxico: {stringlexico}')
