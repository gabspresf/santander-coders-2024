# > CONVERSÃO DE TIPOS

idade = '26'

print(idade, type(idade))

# agora eu estou pegando a variável idade, que está em str, e convertendo ela para int
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# > TIPOS E CONVERSÃO:
# int()
# str()
# float()
# bool()

# coloquei o input dentro do float para que o dado recebido seja de fato um float
altura = float(input('Digite a sua altura: '))
print(altura, type(altura))

# o input sempre lê como str, então é quase que necessário fazer a conversão antes
