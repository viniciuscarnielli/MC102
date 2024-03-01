sequencia = [int(i) for i in input().split()]

entrada = sequencia.copy() 
sequencia.sort() # Ordem correta

i = 0
while i < len(entrada):
  entrada.append(entrada[0])
  entrada.pop(0)
  if entrada == sequencia:
    print('Klift, Kloft, Still, a porta se abriu')
    break

  i +=1

if not(entrada == sequencia):
  print('Senha incorreta')