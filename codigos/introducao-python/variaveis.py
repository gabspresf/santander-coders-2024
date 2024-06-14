# > VARIÁVEIS

# 1. Variáveis

idade = 26  # Criando uma variável

print(idade)

nome = "Gabriela"  # Texto sempre entre áspas (simples ou dupla)

print(nome)

# Tipos de variáveis
# 1. int: números inteiros, ou seja, 0, 5, -1, 1000..
# 2. float: números decimais, ou seja, 1.0, -2.7, 3.14..
# 3. str: cadeia de caracteres, ou seja, dados textuais (string)
# 4. bool: valores lógicos (booleanos), ou seja, True ou False

idade = 23
altura = 1.60
nome = "Gabriela"
estudando = True

# Imprimir (print) o tipo das variáveis: type e entre () o nome da variável

print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))


# Obtendo os dados do usuário e salvando em variáveis

linguagem = input(
    "Qual é a linguagem de programação que você está estudando? ")
# Linguagem recebe o que o usuário digitar na entrada!

print("A linguagem que você está estudando é", linguagem)
# Para imprimir várias variáveis no print é só separar usando a vírgula
