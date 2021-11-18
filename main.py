# compilador

from funcoes import *

listareservadas = gerarlista('palavrasreservadas.cha', 'r')
listasimbolos = gerarlista('simbolos.cha', 'r')
listatipos = gerarlista('tipos.cha', 'r')
dicionario = gerarlista('dicionario.cha', 'r')

entrada = input().replace(" ", "")
lista = entrada[0]

# ocorre(        ; x<5;  x++){}
# ocorre(     x=0; x<5;  x++){}
# ocorre(mano x=x; x<x;  x++){}
# ocorre(mano x=0; x<5;  ++x){}
# ocorre(mano x=0; x<=5; x++){}
# ocorre(mano x=0; x<=5; x+=2){}
# ocorre(mano x=0; x<=5; x+=x){}

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

# meteoloco(a > 5 ){}
# meteoloco(a < 5 ){}
# meteoloco(a == 5 ){}
# meteoloco(a <= 5 ){}
# meteoloco(a >= 5 ){}
# meteoloco(a > b ){}
# meteoloco(a < b ){}
# meteoloco(a >= b ){}
# meteoloco(a <= b ){}
# meteoloco(a == b ){}

# mano brown = 5;
# mano brown = 10;
# mano brown = 100;
# mano brown = b;
# truta brown = "aloalo";
# truta brown = 'aloalo';

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
        cont = 0
        for i in entrada:
            if i.isnumeric():
                num += i
                cont += 1

        listalexico.append(f'Símbolo [frag = {num}, tipo = numérico]')
        numericos.append(num)
        inp.append('número')
        indice += cont - 1
        flag = True
        # if entrada[indice + 1].isnumeric():
        #     num += lista + entrada[indice + 1]
        #     listalexico.append(f'Símbolo [frag = {num}, tipo = numérico]')
        #     numericos.append(num)
        #     indice += 1
        # else:
        #     listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
        #     numericos.append(lista)
        #     inp.append('número')
        #     num = ''
        #
        # flag = True

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        tipos.append(lista)
        inp.append('tipo')
        flag = True

    elif entrada[indice + 1] in listasimbolos:
        if 'obaguieesse' in reservadas or 'truta' in tipos:
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

# print(f'entrada: {inp}')
# print('')
#
# print(f'reservadas: {reservadas}')
# print(f'tipos: {tipos}')
# print(f'números: {numericos}')
# print(f'simbolos: {simbolos}')
# print(f'textos: {listatextos}')
# print(f'variáveis: {listavariaveis}')


if inp[0] == 'sepa':
    sepa(inp)
elif inp[0] == 'obaguieesse':
    obaguieesse(inp)
elif inp[0] == 'ocorre':
    ocorre(inp)
elif inp[0] == 'vaivenafita':
    vaivenafita(inp)
elif inp[0] == 'meteoloco':
    if meteoloco(inp):
        print(f'para a tradução: {traducao}')
elif inp[0] == 'tipo':
    if atribuicao(inp):
        print(f'para a tradução: {traducao}')
