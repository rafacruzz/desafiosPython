# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1: int = int(input('Informe o primeiro número: '))
n2: int = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor informado foi {}.'.format(menor))
print('O maior valor informado foi {}.'.format(maior))
