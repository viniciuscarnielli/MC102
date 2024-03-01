# Leitura da primeira linha
olimpiada = {} 
final = {}
N, O, P, B = [int(x) for x in input().split()]
for i in range(N):
  (prova, ouro, prata, bronze) = input().split()
  olimpiada[prova] = {ouro:O, prata: P, bronze: B}
  final[prova] = ouro


# olimpiada[partida]
#{'Tailandia': 6, 'Japao': 0, 'Africa_do_Sul': 0}

#olimpiada[prova].items())
#dict_items([('Brunei', 6), ('Malta', 0), ('Africa_do_Sul', 0)])

#olimpiada[prova].keys())
#dict_keys(['Brunei', 'Malta', 'Africa_do_Sul'])

# Leitura e processamento das provas

tocha = {} 
for partida in olimpiada:
  for (pais,peso) in olimpiada[partida].items():
    if pais in tocha:
      tocha[pais] = tocha.get(pais) + peso #atualiza
    else:
      tocha[pais] = peso # add

#tocha = {'Tailandia': 12, 'Japao': 6, 'Africa_do_Sul': 6, 'Catar': 0, 'Venezuela': 6, 'Suecia': 6, 'Brunei': 6, 'Essuatini': 12, 'Malta': 0, 'Bielorrussia': 0, 'Iemen': 0}

# Impressão da saída
ponderado = {} # paises com maior pontuação pondera
for (pais1, peso1) in tocha.items():
  if peso1 == max(list(tocha.values())):
    ponderado[pais1] = peso1
    #ponderadp = {'Tailandia': 12, 'Essuatini': 12}

alfabetica = list(ponderado.keys())  
a = alfabetica.sort() #['Essuatini', 'Tailandia']

ordenado = dict(zip(alfabetica,ponderado.values())) 
#{'Essuatini': 12, 'Tailandia': 12}

# print(final)
#{'Ginastica_ritmica_individual_geral': 'Tailandia', 'Tenis_simples_masculino': 'Tailandia'}

#elemento
#{'Tailandia': 'Tenis_simples_masculino'}


# Impressão da saída
for (pais2, peso2) in ordenado.items():
  print(pais2, peso2)
  for elemento in final:
    if final[elemento] == pais2:
      print(elemento)