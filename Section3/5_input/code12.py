# How to use
nome = input('Qual o seu nome? ')
print(f'O seu {nome=}')

# How not to use input
number = input('Digite um numero: ')
number2 = input('Digite um numero: ')

print(f'Os numeros somados: {number + number2}')

# How to "solve" the int problem
num = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

# This way do not work because if the user type a "a" in the code it will break instantly

print(f'A some dos numeros: {num + num2}')

# How to actually solve the int problem
numb = input('Digite um numero: ')
numb2 = input('Digite um numero: ')

# With this way you can make a way to check what the user type before the conversion

int_numb_1 = int(numb)
int_numb_2 = int(numb2)

print(f'A soma dos numeros: {int_numb_1 + int_numb_2}')