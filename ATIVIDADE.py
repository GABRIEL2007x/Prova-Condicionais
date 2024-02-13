# Pergunta a velocidade do carro ao usuário
velocidade = float(input("Qual é a velocidade do carro em km/h? "))

# Verifica se a velocidade é superior a 80 km/h
if velocidade > 80:
    # Calcula a quantidade de km/h excedidos
    km_excedidos = velocidade - 80
    # Calcula o valor da multa
    multa = km_excedidos * 20
    # Exibe a mensagem de multa e o valor da multa
    print("Você foi multado por excesso de velocidade!")
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")
