# Leitura de dados

dna = input()
prime = input()

# Verificação da ligação dos primers na fita

primer = prime[::-1] # primer invertido
primer1 = primer[1:len(primer)-1]

prim = []# lista de strings

for i in primer1:
  if i == 'A':
    prim.append("T")
  elif i == 'C':
    prim.append("G")
  elif i == 'T':
    prim.append("A")
  else:
    if i == 'G':
      prim.append("C")

primer2 = "".join(prim)


# Impressão da saída do programa

flag = True
removido = 0
while primer2 in dna:
  posicao = dna.find(primer2)
  print('Ligacao na posicao', removido + posicao)
  dna = dna[posicao + 1:]
  removido = removido + (posicao + 1)
  flag = False

if flag:
  print("Nenhuma ligacao")