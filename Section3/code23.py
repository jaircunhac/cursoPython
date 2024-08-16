"""
Introdução ao try/except
try - tentar executar o código
except - ocorreu algum erro ao tentar executar
"""

numero_str = input("Digite um número que você quer dobrar: ")

try:
    numero_float = float(numero_str)
    print("Float: ", numero_float)
    print("Seu número vezes dois é: ", numero_float * 2)
except:
    print("Isso não é um número")