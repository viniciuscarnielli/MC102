# Leitura de dados
score = int(input())
idade = int(input())
saldo = float(input())
salario = float(input())

# Verificação se o cartão de crédito será concedido ou não

if score < 300:
    print("Cartao nao concedido")

if score >= 600: 
    if idade >= 50:
        print("Cartao concedido")
    if idade < 50:
        if salario >= 2000:
            print("Cartao concedido")
        if salario < 2000:
            if saldo < 5000:
                print("Cartao nao concedido")
            if saldo >= 5000:
                print("Cartao concedido")

if score >= 300 and score < 600:
    if idade < 30:
        print("Cartao nao concedido")
    if idade >= 30:
        if salario < 3000:
            print("Cartao nao concedido")
        if salario >= 3000:
            if saldo >= 7000:
                print("Cartao concedido")
            if saldo < 7000:
                print("Cartao nao concedido")