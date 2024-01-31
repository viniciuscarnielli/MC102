Lembre-se que o ataque do pokémon com maior velocidade é considerado primeiro ao diminuir o `hp` do oponente. O `hp` de cada pokémon nunca será negativo, sendo que seu valor mínimo é zero. No momento que o `hp` de um dos pokémon chega em zero o mesmo é considerado como derrotado e a batalha é considerada encerrada, mesmo que isso ocorra no meio de um turno. Ao final da batalha, após imprimir o `hp` de cada pokémon, seu programa deve imprimir o nome e o `hp` do pokémon que venceu a batalha:

    Pokémon Vencedor: <nome pokémon vencedor>
    HP do Vencedor: <HP do pokémon vencedor>
    

Exemplos de entradas e saídas esperadas pelo seu programa:

### [](#teste-01)Teste 01

[Entrada](dados/arq01.in)

    80
    80
    100
    70
    10
    0.5
    20
    1
    10
    0.5
    10
    2
    20
    0.5
    10
    1
    20
    2
    10
    0.5
    20
    1
    10
    2
    

[Saída](dados/arq01.out)

    HP Ivysaur = 60
    HP Pikachu = 75
    HP Ivysaur = 40
    HP Pikachu = 70
    HP Ivysaur = 30
    HP Pikachu = 60
    HP Ivysaur = 25
    HP Pikachu = 20
    HP Ivysaur = 25
    HP Pikachu = 0
    Pokémon Vencedor: Ivysaur
    HP do Vencedor: 25
    
