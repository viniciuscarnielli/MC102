# Leitura do número de meses

n = int(input())
D2 = 0 #Pessoas completamente imunizadas
D1 = 0 #Pessoas imunizadas apenas com uma dose
D2A = 0 #Pessoas que tomaram a segunda dose com atraso
D1A = 0 #Pessoas esperando a segunda dose com atraso

# Processamento de cada mês:

for i in range(n):
  vacinas = int(input())
  if D1A > 0: # (1) existem pessoas com a segunda dose atrasada?
    if vacinas >= D1A:
      vacinas = vacinas - D1A # Excedente
      D2 = D2 + D1A 
      D2A = D2A + D1A  # Quantidade de D1A --> (vai para) D2A
      D1A = 0  
    else:
      if vacinas < D1A:
        D2 = D2 + vacinas
        D2A = D2A + vacinas 
        D1A = D1A - vacinas  # Pessoas que ainda não tomaram a 2º Dose
        vacinas = 0

  if vacinas > 0 and D1 > 0: # (2)  2° dose em dia 
    if vacinas >= D1:
      vacinas = vacinas - D1 # Excedente
      D2 = D2 + D1 
      D1 = 0 # 
    else:
      if vacinas < D1:
        D2 = D2 + vacinas
        D1A = D1 - vacinas # (quantidade de D1 -->(vai para) D1A)
        D1 = 0  
        vacinas = 0

  if vacinas > 0: # (3) vacinas restantes são aplicadas como 1º dose.
    D1 = vacinas
 
if D1A > 0:
  D1 = D1 + D1A
#Impressão da saída

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas apenas com uma dose:", D1)
print("Pessoas que tomaram a segunda dose com atraso:", D2A)
print("Pessoas esperando a segunda dose com atraso:", D1A)