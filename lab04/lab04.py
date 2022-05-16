# Inicialização das variáveis

entrada = input() # Entrada do programa (W, E, F, A)
w = 0 # Water
f = 0 # Fire
e = 0 # Earth
a = 0 # air

# Leitura da sequência de treinamento

while entrada != 'X':
    pontos = int(input())

    if entrada == 'W': # Water <--> Fire (Opostos)
        w = w + pontos
        f = f - pontos/2
        if f <= 0:
            f = 0
        
    elif entrada == 'F': # Water <--> Fire 
        f = f + pontos
        w = w - pontos/2
        if w <= 0:
            w = 0

    elif entrada == 'E': # Earth <--> Air 
        e = e + pontos
        a = a - pontos/2
        if a <= 0:
            a = 0

    elif entrada == 'A': # Earth <--> Air 
        a = a + pontos
        e = e - pontos/2
        if e <= 0:
            e = 0 
   
    entrada = input()

# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(w))
print("Terra: {:.1f}".format(e))
print("Fogo: {:.1f}".format(f))
print("Ar: {:.1f}".format(a))

if w > 0 and e > 0 and f > 0 and a > 0:
    print("Treinamento realizado com sucesso.")
else:
    print("Realize mais treinamentos.")