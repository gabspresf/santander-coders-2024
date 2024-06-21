# > ESTRUTUAS CONDICIONAIS

# Exemplo 1: Informe a idade, dependendo da idade execute tal coisa
idade = int(input('Digite a sua idade: '))

# Se a idade for maior ou igual a 18, ENTÃO (:) execute isso
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
# Do contrário, ENTÃO (:) execute aquilo


# Exemplo 2: Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior ou igual a 7,
# e "Reprovado(a)", caso a média seja inferior a 7.

media_aluno = float(input('Digite a sua média: '))

if media_aluno >= 7:
    print('Você está aprovado(a).')
elif media_aluno >= 5:
    print('Você está de recuperação.')
else:
    print('Você está reprovado(a).')

# "Elif" é como se fosse um else + if

# Outra forma de usar condições de comparação: média superior a 7 e uma presença nas aulas superior a 70 %
# media = 10
# presenca = 100

# if media >= 7 and presenca >= 70:
#   print('Aprovado(a).')
# else:
#   print('Reprovado(a).')

# Pode-se usar o "and" ou o "or"
# Nesse caso, as duas condições precisam acontecer
