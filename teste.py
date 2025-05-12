from main import analisar_lista

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

resultado = analisar_lista(numeros)

print(f"Média: {resultado['media']}")
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
print(f"Quantidade de números pares: {resultado['pares']}")
