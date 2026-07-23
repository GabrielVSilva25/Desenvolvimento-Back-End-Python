contador_notas = 1
soma_notas = 0
media = 0

nota = float(input('Digite uma nota: '))
print('Digite -1 para encerrar o programa.\n')

while nota != -1:
    contador_notas +=1
    soma_notas += nota

    nota = float(input('Digite uma nota: '))
    print(contador_notas)

if nota == -1 and contador_notas == 1:
    print('Programa encerrado.')

else:
    print(f'\nQuantidade de Notas: {contador_notas-1}')
    print(f'Soma das notas: {soma_notas}')
    print(f'Média das notas: {soma_notas/(contador_notas-1)}')