# compilador
from funcoes import *

listareservadas = gerarlista('palavrasreservadas.cha', 'r')
listasimbolos = gerarlista('simbolos.cha', 'r')
listatipos = gerarlista('tipos.cha', 'r')

entrada = input().replace(" ", "")
lista = entrada[0]

# ocorre(        ; x<5;  x++)
# ocorre(     x=0; x<5;  x++)
# ocorre(mano x=x; x<x;  x++)
# ocorre(mano x>0; x<5;  ++x)
# ocorre(mano x=0; x<=5; x++)
# ocorre(mano x>0; x<=5; x+=2)
# ocorre(mano x>0; x<=5; x+=x)

# sepa(mano x <= 9){}
# sepa(mano x <= y){}
# sepa(mano x < 9){}
# sepa(mano x < y){}
# sepa(x < 9){}
# sepa(x < y){}
# sepa(x <= 9){}
# sepa(x <= y){}
# sepa(1 < 9){}
# sepa(1 < y){}
# sepa(1 <= 9){}
# sepa(1 <= y){}

# obaguieesse(x);
# obaguieesse("oiiii");
# obaguieesse(#"<x> oi");
# obaguieesse(#"oi <x>");
# obaguieesse(#"oioivitoria");

flag = False
indice = 0
listavariaveis = []
listatextos = []
listalexico = []

reservadas = []
simbolos = []
numericos = []
tipos = []
inp = []

while indice < len(entrada):
    # print(f'{lista}, indice: {indice}')
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
        flag = True

    elif lista.isnumeric():
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
        if 'obaguieesse' in reservadas:
            if entrada[12] == '#' and entrada[indice + 1] == '>':
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

    if flag == True:
        if indice < len(entrada) - 1:
            lista = entrada[indice + 1]
        else:
            pass

    indice += 1

stringlexico = ', '.join(map(str, listalexico))
print(f'Léxico: {stringlexico}')
print()

# print(f'reservadas: {reservadas}')
# print(f'símbolos: {simbolos}')
# print(f'numericos: {numericos}')
# print(f'tipos: {tipos}')
# print(f'variaveis: {listavariaveis}')
# print(f'texto: {listatextos}')
print(f'entrada: {inp}')
print()

if inp[0] == 'sepa':
    sepa(inp)
else:
    obaguieesse(inp)
