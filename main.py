def analisar_lista(numeros):
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = len([num for num in numeros if num % 2 == 0])
    
    return {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "pares": pares
    }
