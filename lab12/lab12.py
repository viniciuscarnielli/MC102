def flip_horizontal(B):
  copia = [x.copy() for x in B]
  m_horizontal = []
  for x in range(len(copia)):
    nova_fila = []
    for y in range(len(copia[0])):
      x2 = x 
      y2 = len(copia[0]) -1 - y
      nova_fila.append(B[x2][y2])
    m_horizontal.append(nova_fila)

  return m_horizontal

def flip_vertical(B):

  copia = [x.copy() for x in B]
  m_vertical = []
  for x in range(len(copia)):
    nova_fila = []
    for y in range(len(copia[0])):
      x2 = len(copia) - 1 - x 
      y2 = y
      nova_fila.append(copia[x2][y2])
    m_vertical.append(nova_fila)

  
  return m_vertical

def rotacao_90(B):
  copia = [x.copy() for x in B]
  transposta = []
  for j in range(len(copia[0])):
    linha = []
    for i in range(len(copia)):
      linha.append(copia[i][j])
    transposta.append(linha)

  rot90 = flip_horizontal(transposta)
  return rot90
 
def rotacao_180(B):

  copia = [x.copy() for x in B]
  op1 = rotacao_90(copia)
  op2 = rotacao_90(op1)

  return op2
  
# leitura da imagem A
_ = input() #P2 - linha a ser ignorada

m_A, n_A = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

A = []
for i in range(n_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# leitura da imagem B
_ = input() #P2 - linha a ser ignorada

m_B, n_B = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

B = []
for i in range(n_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)

#print(rotacao_180([[1,1,1],[2,2,2],[3,3,3]]))

a = False
for i in range(len(A) - len(B) + 1 ):
  for j in range(len(A[0]) - len(B[0]) + 1):
    cont = 0 
    for k in range(len(B)):
      if A[i+k][j:j+len(B[0])] == B[k]:
        cont+=1
      else:
        break

      if cont == len(B):
        print('Original: Contido')
        a = True
        break

if a == False:  
  print('Original: Nao contido')
      

b = False
f_H = flip_horizontal(B)
for i in range(len(A) - len(f_H) + 1 ):
  for j in range(len(A[0]) - len(f_H[0]) + 1):
    cont = 0 
    for k in range(len(f_H)):
      if A[i+k][j:j+len(f_H[0])] == f_H[k]:
        cont+=1
      else:
        break

      if cont == len(f_H):
        print('Flip horizontal: Contido')
        b = True
        break

if b == False:
  print('Flip horizontal: Nao contido')
  
c = False
f_V = flip_vertical(B)
for i in range(len(A) - len(f_V) + 1 ):
  for j in range(len(A[0]) - len(f_V[0]) + 1):
    cont = 0 
    for k in range(len(f_V)):
      if A[i+k][j:j+len(f_V[0])] == f_V[k]:
        cont+=1     
      else:
        break

      if cont == len(f_V):
        print('Flip vertical: Contido')
        c = True
        break

if c == False:
  print('Flip vertical: Nao contido')

d = False
r90 = rotacao_90(B)
for i in range(len(A) - len(r90) + 1 ):
  for j in range(len(A[0]) - len(r90[0]) + 1):
    cont = 0 
    for k in range(len(r90)):
      if A[i+k][j:j+len(r90[0])] == r90[k]:
        cont+=1   
      else:
        break
        
      if cont == len(r90):
        print('Rotacao 90: Contido')
        d = True
        break

if d == False:
  print('Rotacao 90: Nao contido')

e = False
r180 = rotacao_180(B)
for i in range(len(A) - len(r180) + 1 ):
  for j in range(len(A[0]) - len(r180[0]) + 1):
    cont = 0 
    for k in range(len(r180)):
        if A[i+k][j:j+len(r180[0])] == r180[k]:
          cont+=1
        else:
          break

        if cont == len(r180):
            print('Rotacao 180: Contido')
            e = True
            break

if e == False:
  print('Rotacao 180: Nao contido')
  