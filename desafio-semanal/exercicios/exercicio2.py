# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

preco_total = 0

while True:
    preco = float(input("Digite o preco da fruta (ou 0 para sair):"))
    if preco == 0:
        break
    preco_total += preco
    print("O preco total das frutas e R$ {:.2f}".format(preco_total))


