
from random import randint
print('EXERCICIO 1')
extenso = ('um', 'dois', 'tres', 'quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
print('\t\tPara sair do programa digite o numero 999\n')
while True:
    num = int(input('Digite um Numero: \n'))
    if num == 999:
        break
    while num < 0 or num > 10:
        num = input('Tente novamente, por favor digite um numero \n')
        print('Para sair do programa digite o numero 999\n')
    for c in range(num):
        if c+1 == num:
            print(f'Voce digitou o numero {extenso[c]}')

#print('EXERCICIO 2')
#for c in range(0, 5):
 #   aleatorio = (randint(1, 5))
#maior = menor = 1

#for c in range(0, 5):
    #if maior < aleatorio[c]:
        #maior = aleatorio[c]
    #elif menor > aleatorio[c]:
        #menor = aleatorio[c]
#print(menor)
#print(maior)

print('Exercicio 03')
produtos = ('Pao', 1.50, 'Leite', 4, 'Arroz', 30, 'Frango', 40)
for c in range(0, len(produtos)):
    if c != len(produtos):
        print(f'{produtos[c]}..................R$: {produtos[c+1]}')

print('Exercicio 04')
tupla = ( )