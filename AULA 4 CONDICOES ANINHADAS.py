nome = str(input('Digite seu nome '))
if nome == 'Matias':
    print('Bem Vindo {}\n'.format(nome))
elif nome == 'Gabriel':
    print(nome.upper())
else:
    exit(1)

print('EXERCICIOS\n')
valor = float(input('Digite o valor do imovel '))
salario = float(input('Digite seu salario '))
anos = int(input('Em quantos anos deseja financiar o imovel? '))

prestacao = valor / (anos*12)
if prestacao >= salario*0.03:
    print('[EMPRESTIMO NEGADO, RISCO DE CREDITO ALTO]\n')
else: print('EMPRESTIMO APROVADO!\n')

print('EXERCICIO 02\n')

