"""
Formatação básica de Strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100, .1f
Conersion flags - !r !s !a
"""

aux = "Jair"
print(f"{aux}")
print(f"{aux: >10}")
print(f"{aux: <10}.")
print(f"{aux:ç^10}.")