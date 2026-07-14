# Peça um ano.

# Informe se ele é bissexto.

# Desafio: pesquise a regra de ano bissexto e implemente a lógica usando if.

ano = int(input('Informe um ano: '))

if ano % 4 == 0 or ano % 400 and ano % 4 ==0:
    print('Ano bissexto')

else:
    print('Ano não é bissexto')
