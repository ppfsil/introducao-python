# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = ["maca" , "banana" , "maca" , "laranja" , "uva" , "banana" , "maca"]
ocorrencias =  {}

for fruta in frutas:
    if fruta in ocorrencias:
        ocorrencias[fruta] += 1
    else:
        ocorrencias[fruta] = 1
print(ocorrencias)
