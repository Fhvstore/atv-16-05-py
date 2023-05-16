#1) Calcular a média de um onjunto de números

numeros = input("Digite os números separados por vírgula: ")


numlist = numeros.split(',')


numeros_float = [float(numero) for numero in numlist]


soma = sum(numeros_float)
media = soma / len(numeros_float)


print("A média é: ", round(media, 2))
