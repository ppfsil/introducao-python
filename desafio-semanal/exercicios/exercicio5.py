# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

#Solicitar ao usuario o preco original do produto e o desconto percentual
preco_original = float(input("Digite o preco original do produto: "))
desconto_percentual = float(input("Digite o desconto em porcentagem: "))
#Calcular o preco final subtraindo o valor do desconto ao preco original
preco_final = preco_original - (preco_original * (desconto_percentual / 100))
#Imprimir o preco final 
print("O preço final do produto é: ", preco_final)
