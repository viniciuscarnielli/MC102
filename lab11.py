# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 

def dimensao(M) :
    if M == [] :
        return (0,0)
    linhas = len(M)
    colunas = len(M[0])
    return (linhas, colunas)

mapa = []
while True:
  lista = input().split()
  string = ''.join(lista)
  if string.isnumeric(): # É um nº que estou lendo?
    coordenadas = []
    N = int(lista[0]) # nº de equipes
    for i in range(N):
      localizacao = [int(x) for x in input().split()]
      coordenadas.append(localizacao)
    break
  else:
    mapa.append(lista)


mapa2 = [linha[:] for linha in mapa]

for k in coordenadas :
  i = k[0]
  j = k[1]

  mapa = [linha[:] for linha in mapa2]

  (l,c) = dimensao(mapa) 

  while True : 
   
    if mapa[i][j] == "N": #-i
      if i == 0:
        print('Fuga pelo norte.')
        break
      else:
        mapa[i][j] = '*'
        i-=1

    elif mapa[i][j] == "S": # +i
      if i == l-1:
        print('Fuga pelo sul.')
        break
      else:
        mapa[i][j] = "*" 
        i+=1

    elif mapa[i][j] == "L": # +j
      if j == c-1:
        print('Fuga pelo leste.')
        break
      else:
        mapa[i][j] = '*'
        j+=1

    elif mapa[i][j] == "O": # -j
      if j == 0:
        print('Fuga pelo oeste.')
        break
      else:
        mapa[i][j] = '*'
        j-=1
    
    else:
      print('Resgate aereo solicitado.')
      break

