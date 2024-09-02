# Operadores Lógicos
# and(e) or (ou) not(não)
# or - Uma das condições precisa ser verdadeiras.
# se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São consideradas falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor.

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_verdadeira = "Jair"
if (entrada == "E" or "e") and senha_digitada == senha_verdadeira:
    print("Acesso concedido")
elif entrada == "S":
    print("Saindo")
elif entrada == "E" and senha_digitada != senha_verdadeira:
    print("Acesso Negado")
else:
    print("Error")

# Avaliação de curto circuito
senha = input("Senha: ") or "Sem Senha"
print(senha) # Caso você não coloque nada o código mostrará "Sem Senha"