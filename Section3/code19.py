# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = "Jair"
print(nome[1])
print(nome[-3])

print("Ja" in nome) # True
print("ch" in nome) # False
print("ir" not in nome) #False
print("tch" not in nome) #True

frase = input("Digite uma frase que desejar: ")
procurar = input("Escreva o que deseja encontrar na frase: ")

if procurar in frase:
    print(f"A palavra {procurar} está na frase")
else:
    print(f"A palavra {procurar} não foi encontrada na frase")