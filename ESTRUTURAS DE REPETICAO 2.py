#estruturas de repeticao
from time import sleep
from random import randint
from math import factorial
num = 1
par = impar = 0
print('[CASO DESEJE SAIR DO PROGRAMA DIGITE 0]\n')
while num != 0:
    num = int(input('Digite um valor: \n'))
    if num != 0:
        if num % 2 == 0:
            par += par+1
        else:
            impar += impar+1
print('Digitou {} impar, e {} Pares\n'.format(impar, par))


print('EXERCICIO 01\n')
sexo = str(input('Digite seu sexo [F/M]\n')).upper()

while sexo != 'F' and sexo != 'M':
    sexo = str(input('SEXO INVALIDO! Digite seu sexo Novamente [F/M]\n')).upper()

print('EXERCICIO 02\n')
aleatorio = randint(0, 1)
print('[PENSAREI EM UM NUMERO DE 1 A 10, TENTE ADIVINHAR]\n')
print('[BEM VINDO AO MEU JOGO, TENTE ADIVINHAR O NUMERO QUE EU PENSEI]\n')
user = int(input('Digite sua aposta: '))
cont = 0
while user != aleatorio:
    print('Processando...')
    sleep(0.5)
    if user != aleatorio:
        cont += 1
        print('[VOCE ERROU]\n')
        user = int(input('Digite sua aposta: '))
print('tentativas totais {}'.format(cont))

print('EXERCICIO 03')
numero = int(input('Digite o numero fatorial: '))
fatorial = factorial(numero)
print('Fatorial de {} e {}'.format(numero, fatorial))


print('EXERCICIO 04')
total = 0
contador = 0
maior= 0
menor = 0
num2 = int(input('Digite um numero: '))
opcao = str(input('Deseja digitar mais algum nuemro? [S/N]: ')).upper()
maior = menor = num2
while opcao != 'S' and opcao != 'N':
    opcao = input('OPCAO DESEJADA INVALIDA, DIGITE NOVAMENTE: ').upper()
while opcao == 'S':
    total += num2
    contador += 1
    num2 = int(input('Digite o proximo numero: '))
    opcao = str(input('Deseja digitar mais algum nuemro? [S/N]: ')).upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input('OPCAO DESEJADA INVALIDA, DIGITE NOVAMENTEL: ').upper()
    if num2 > maior:
        maior = num2
    elif num2 < menor:
        menor = num2

media = (total/contador)
print('Menor Numero {}'.format(menor))
print('Maior Numero {}'.format(maior))
print('Media {}'.format(round(media, 2)))
