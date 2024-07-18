primeiro_valor = input("Insira um valor: ")
segundo_valor = input("Insira outro valor: ")

if primeiro_valor < segundo_valor:
    print(f"O {primeiro_valor=} é menor que o {segundo_valor=}")
elif primeiro_valor > segundo_valor:
    print(f"O {segundo_valor=} é menor que o {primeiro_valor=}")
else:
    print("Os valores são iguais")