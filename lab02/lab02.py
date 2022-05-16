# Leitura de dados

t = float(input()) # tempo 2º --> saida boxes
dist_a = int(input()) # entrada boxes --> pit stop
vel_a = float(input())/3.6 # Vel. entrada --> pit stop
t_pit_stop = float(input()) # Tempo de parada no pit stop
dist_b = int(input()) # Pit stop --> saida 
vel_b = float(input())/3.6 # Vel. pit stop --> saida 

# Cálculo do tempo total gasto para realizar o pit stop

Tentrada = dist_a/vel_a
Tsaida = dist_b/vel_b
Ttotal = t_pit_stop + Tentrada + Tsaida

# Impressão da resposta

print( t > Ttotal)