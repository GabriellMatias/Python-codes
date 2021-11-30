import math as mt
import random

num = input("Digite o numero:")
raiz = mt.sqrt(int(num))
print('A raiz do {} e igual e {}\n'.format(num, mt.ceil(raiz)))
num2 = random.randint(1, 1000)
print('Numero aleatorio {}'.format(num2))



