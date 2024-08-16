nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(" " in nome)
    print(f"Seu nome tem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou um ou mais campos vazios")