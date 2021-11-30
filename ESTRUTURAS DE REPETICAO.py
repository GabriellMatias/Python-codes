#estruturas de repeticao
from time import sleep
for c in range(0, 3):
    nome=str(input('Digite seu nome '))
for c in range(0, 10, 2):
    print(c)

num=int(input('Digite a quantidade de alunos na sala: '))
for c in range(num):
    not1 = float(input('Digite a primeira nota do aluno numero {} '.format(c+1)))
    not2 = float(input('Digite a segunda nota do aluno numero {} '.format(c+1)))
    media = (not1 + not2 / 2)

print('Media final igual a {}' .format(media))
print('Exercicios')
cont = 10
for c in range(0, 10):
    cont -= 1
    print(cont)
    sleep(1)

print('exercicio 02')
for c in range(0, 50, 2):
    print(c)

print('Exexrcicio 3')
total = 0
for c in range(0, 6, 2):
    total = int(total + c)
    print(total)

print('Exercicio 04')
numP = int(input('Digite quantas pessoas irao participar da pesquisa: '))
for c in range(numP):
    data = int(input('Digite o ano dde nascimento do usuario numero {}'.format(c)))
    if 2019-data < 21:
        print('Pessoa menor de idade\n')
    else: print('Pessoa Maior de Idade!\n')

print('Exercicio 05')
contM=0
for c in range(0, 4):
    nome = str(input('Digite seu nome '))
    idade = int(input('Digite sua idade '))
    sexo = str(input('Digite seu sexo '))
    if idade < 20:
        contM += 1
    Velho = idade
    if idade > Velho:
        Velho = idade

    if Velho > idade:
        print('Pessoa Mais velha')
        print(nome)
        print(sexo)
        print(idade)
media = idade/4
print('Media total das idades {} '.format(media))
print('Quantidade de pessoas maiores de idade: '.format(contM))