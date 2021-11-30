#cores
vermelho = '\033[1;31m'
reset = '\033[m'
verde = '\033[1;32m'


print('[EXERCICIO 01]')
soma = contador = 0
while True:
    num  = int(input('Digite um numero: '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'A soma total foi de {soma}, e a quantidade de numeros digitados foi {contador}')

print('[EXERCICIO 02]')
multiplicador = 0
while True:
    numero = int(input('Digite um valor para ser multiplicado: '))
    if numero < 0:
        break
    while multiplicador < 10:
        multiplicador += 1
        total = numero * multiplicador
        print(f'{numero} X {multiplicador} = {total}')
    multiplicador = 0

print(f'{verde}[EXERCICIO 03]{reset}')
contIdade = 0
homens = 0
mulheres = 0
mulherMaior = 0
while True:
    nome = str(input('Digite o nome para cadastro '))
    idade = int(input('Digite a idade para cadastro '))
    sexo = str(input('Digite seu sexo [F/M] ')).upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input(f'{vermelho}SEXO INVALIDO, POR FAVOR DIGITE NOVAMENTE O SEXO: [F/M] {reset} ').upper()
    if sexo == 'F':
        mulheres += 1
    else: homens += 1
    opcao = str(input('Deseja continuar cadastrando usuarios? [S/N] ')).upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input(f'{vermelho}Opcao invalida, por favor digite sua opcao novamente [S/N] {reset} ').upper()
    if opcao == 'N':
        break
    if idade > 18:
        contIdade +=1
    if idade > 20 and sexo == 'F':
        mulherMaior += 1
print('-'*35)
print(f'Quantidade de mulheres {mulheres}')
print('-'*35)
print(f'Quantidade de Homens {homens}')
print('-'*35)
print(f'Quantidade de mulheres Maiores de 20 anos {mulherMaior}')
print('-'*35)
print(f'Quantidade de Pessoas maiores de idade {contIdade}')
print('-'*35)
