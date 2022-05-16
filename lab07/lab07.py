vac = [] 
N = int(input()) # N >= 3  N == len(vac)
for i in range(N):
  vac.append(int(input())) # N linhas com a quant. de vac. disponiveis

D1 = []
D2 = []
X = []

# Processamento dos dados 

for i in range(N):
  if N == 3: 
    D1.append(vac[i])
    D2.append(0) 
    X.append(0)

  if N > 3:
 
    if len(vac[i:N]) <= 3: # ultimos 3 meses
      # aplicar vac. rest. como 1º dose
      
      if i<3: # não deu tempo 2º dose
        D2.append(0)
        D1.append(vac[i]) 
        X.append(0)

      if i >=3: # vacinar 2º dose
        D2.append(D1[i-3])
        D1.append(vac[i] - D2[i])
        X.append(0)
        
    if len(vac[i:N]) > 3: # inicio da lista

      if i<3: # não deu tempo 2º dose
        D2.append(0)
        if vac[i] >= vac[i+3]:
          D1.append(vac[i+3])
          X.append(vac[i] - vac[i+3])
        else:
          D1.append(vac[i])
          X.append(0)
      
      if i >= 3: # tomar a 2º dose 
        D2.append(D1[i-3])
        var = vac[i] - D2[i]
        vac[i] = var
        
        if vac[i] >= vac[i+3]:
          D1.append(vac[i+3])
          X.append(vac[i] - vac[i+3])
        else:
          D1.append(vac[i])
          X.append(0)


# Impressão do uso das vacinas mês a mês

for i in range(N):
    print("Mes " + str(i+1) + ":")
    print("Vacinados com a primeira dose:", D1[i])
    print("Vacinados com a segunda dose:", D2[i])
    print("Vacinas devolvidas:", X[i])

# Impressão do resumo final

print("Total:")
print("Vacinados apenas com a primeira dose:", sum(D1) - sum(D2))
print("Vacinados com as duas doses:",sum(D2))
print('Vacinas devolvidas:', sum(X))