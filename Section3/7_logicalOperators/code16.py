# Operadores Lógicos
# and(e) or (ou) not(não)
# and - Todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São consideradas falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor.

entrada = input("[E]ntrar [S]air")
senha_digitada = input("Senha: ")

senha_verdadeira = "Jair"
if entrada == "E" and senha_digitada == senha_verdadeira:
    print("Acesso concedido")
elif entrada == "S":
    print("Saindo")
elif entrada == "E" and senha_digitada != senha_verdadeira:
    print("Acesso Negado")
else:
    print("Error")

# Avaliação de curto circuito
print(True and False and True) # False

print(False and True and 1) # False

print(0 and 1 and True) # 0

print(1 and 1 and True) # True