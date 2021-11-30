import random
from time import sleep
#cores
verde = '\033[1;32m'
vermelho = 	'\033[1;31m'
reset = '\033[m'
ref = ("Pedra", "Papel", "Tesoura")
print('\t\tBEM VINDO AO SISTEMA DE JOGOS MATIEZE\n')
print('[JOGO SELECIONADO : \033[32mJOKENPO\033[m]')
print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")
sleep(1)
comp = random.randint(0, 2)
user = int(input('''Escolha uma opcao para se jogar 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

if user < 0 or user > 2:
    print('OPCAO INVALIDA!\n')
    exit(1)
print("-=" * 20)
print("O computador escolheu: {}".format(ref[comp]))
print("-=" * 20)
print("O jogador escolheu: {}".format(ref[user]))
print("-=" * 20)
if comp == user:
    print('Empate!\n')
elif comp == 0 and user == 1:
    print(verde+'Usuario VENCEU!!\n'+reset)
    print('PC: [PEDRA] X USUARIO: [PAPEL]\n')
elif comp == 1 and user == 2:
    print(verde+'Usuario VENCEU!!\n'+reset)
    print('PC: [PAPEL] X USUARIO: [TESOURA]\n')
elif comp == 2 and user == 0:
    print(verde+'Usuario VENCEU!!\n'+reset)
    print('PC: [TESOURA] X USUARIO: [PEDRA]\n')
elif user == 0 and comp == 1:
    print(vermelho+'COMPUTADOR VENCEU!!\n'+reset)
    print('PC: [PAPEL] X USUARIO: [PEDRA]\n')
elif user == 1 and comp == 2:
    print(vermelho+'COMPUTADOR VENCEU!!\n'+reset)
    print('PC: [TESOURA] X USUARIO: [PAPEL]\n')
elif user == 2 and comp == 0:
    print(vermelho+'COMPUTADOR VENCEU!!\n'+reset)
    print('PC: [PEDRA] X USUARIO: [TESOURA]\n')






