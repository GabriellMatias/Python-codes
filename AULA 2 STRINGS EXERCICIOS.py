
import string

frase = input('Digite Seu Nome Completo: \n')
print(frase.upper())
print(frase.lower())
frase = frase.split()
print(len(frase))
print('\nPrimeiro nome tem {} letras',len(frase[:len(frase)/2]))

print('[SEGUNDO EXERCICIO]\n')
frase2 = input('Digite sua cidade\n')
if frase2.find('SANTO')==0:
    print('Palavra santo encontrada\n')

print('[TERCEIRO EXERCICIO]\n')
frase3 = input('Digite um nome \n')
frase3 = frase3.upper()
print('SILVA' in frase)


