'''import meu_pacote.modulo1 as modulo1


resultado = int(input("Digite um numero:"))

result = modulo1.dobro(resultado)

print(result)'''

'''import meu_pacote.modulo2 as modulo2


resultado = int(input("Digite um numero:"))

result = modulo2.triplo(resultado)

print(result)'''

'''from meu_pacote import modulo1, modulo2

print(modulo1.dobro(10))
print(modulo2.triplo(10))'''

from meu_pacote.subpacote import modulo3

resultado = int(input("Digite um numero:"))

result = modulo3.quadra(resultado)

print(result)