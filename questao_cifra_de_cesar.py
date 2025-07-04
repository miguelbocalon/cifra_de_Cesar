from collections import deque

alfabeto = deque(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

C = int(input())

i = 0
while i < C:
    B = input().strip().upper()
    A = int(input())
    alfabeto2 = deque(alfabeto)
    alfabeto2.rotate(A)
    frase_cifrada = []
    for letra in B:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            letra_cifrada = alfabeto2[indice]
            frase_cifrada.append(letra_cifrada)
            
        else:
            frase_cifrada.append(letra)
    i = i + 1

print( "".join(frase_cifrada))
