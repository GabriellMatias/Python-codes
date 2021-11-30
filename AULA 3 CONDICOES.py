tempo = int(input('Quantos anos tem seu carro?\n'))
if tempo <=5:
    print('Carro novo!\n')
else:
    print('Carro velho!\n')\

print('CONDICAO COM STRING\n')
nome= str(input('Digite seu Nome\n'))
if nome == 'Matias':
    print('Bom dia {}' .format(nome))
else:
    print('Quem e vc?\n')

print('PROX EXERCICIO')
n1=float(input('Digite a nota 1:\n'))
n2=float(input('Digite a nota 2:\n'))
media=n1+n2/2
if media >= 6:
    print('Aluno APROVADO, Media= {}\n' .format(media))
else: print('Aluno REPROVADO, Media = {}\n' .format(media))


