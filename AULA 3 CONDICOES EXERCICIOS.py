import random
import datetime #importar data do pc
num2 = int(random.randrange(1, 5))
print('Pensei em um numero, adivinhe ele!\n')
num = int(input('Digite sua aposta:\n'))
while num != num2:
    print('\033[31mErrado, por favor tente novamente:\033[m\n')
    num=int(input('Digite o numero novamente:\n'))
if num==num2:
    print('-=-' * 10)
    print('Voce acertou o numero! [{}]'.format(num))
    print('-=-' * 10)


print('[EXERCICIO 02]')
vel = int(input('Digite a velocidade:\n'))
if vel >=80:
    print('-=-'*10)
    print('ULTRAPASSOU O LIMITE!')
    print('-=-' * 10)
    multa = (vel-80)*7
    print('Multa gerada {}'.format(multa))
    print('-=-' * 10)


print('[EEXRCICIO 03]')
num3 = int(input('Digite um numero:\n'))
if (num3%2)==0:
    print('Numero PAR\n')
else:print('Numero IMPAR\n')

print('[EXERCICIO 04')
viagem=int(input('Digite a distancia da viagem:\n'))
if viagem <= 200:
    passagem = viagem*0.50
    print('preco da Passagem = {}'.format(passagem))
else:
    passagem = viagem*0.45
    print('preco da Passagem = {}'.format(passagem))

print('[EXERCICIO 05]')
ano = int(input('Digite o Ano:\n'))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e BISSEXTO!\n'.format(ano))
else:
    print('O ano {} NAO E BISSEXTO!\n'.format(ano))