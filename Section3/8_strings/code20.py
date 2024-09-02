"""
Interpolação básica de Strings
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)
"""

nome = "Jair"
preco = 100.125
variavel = '%s, o preço do jogo é R$%.3f' % (nome, preco)
print(variavel)
print("O hexadecimal de %s é %04X" % (2024, 2024))