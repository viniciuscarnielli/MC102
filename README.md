Laboratório 04    .markdown-body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; font-family: 'Noto Sans', sans-serif; } .markdown-body h6 { margin-bottom: 0; } .markdown-body h6 + ul li { display: inline-block; width: 100%; max-width: 426px; vertical-align: top; } .markdown-body h6 + ul li pre { max-height: 400px; }

[](#batalha-pokémon)Batalha Pokémon
===================================

[![Pokémon](images/pokemon.png)](pokemon.png)

Pokémon é uma franquia de mídia, incluindo jogos de vídeo-game, criada na década de 90. Os jogos são bastante famosos e fazem sucesso até os dias atuais. Em todos os jogos, os personagens treinam e cuidam das criaturas que dão nome ao jogo, os pokémon (o nome Pokémon vem da junção de palavras do título original japonês: "Pocket Monsters" – o que explica também por que o termo "pokémon" não tem plural). Existem várias espécies de pokémon e cada uma aprende vários ataques distintos.

Apesar de existirem vários mecanismos de batalhas nos diferentes jogos de Pokémon, o mais famoso é o sistema de turnos. Nesse mecanismo de batalha, um pokémon `A` enfrenta um pokémon `B`, e cada pokémon tem um valor de pontos de vida (`hp`, do inglês _Health Points_). A cada turno cada pokémon lança um ataque, sendo que o primeiro ataque é realizado pelo pokémon mais rápido, e cada ataque diminui os pontos de vida do pokémon sendo atacado. A batalha continua até que um dos pokémon não tenha mais pontos de vida.

Cada ataque tem um valor `x`, que indica a força do ataque, e um multiplicador `y`, que indica se o ataque foi efetivo `(y=2)`, normal `(y=1)`, ou não efetivo `(y=0.5)`. Um ataque diminui em `x*y` unidades o `hp` do pokémon adversário. Os valores de ataque são sempre pares, o que garante que `x*y` é um número inteiro.

Você foi chamado para criar um programa que simula uma batalha em turnos do jogo Pokémon. Nessa batalha, o pokémon Ivysaur enfrenta o pokémon Pikachu. Inicialmente, seu programa deve ler dois valores inteiros que indicam a quantidade inicial de `hp` dos pokémon Ivysaur e Pikachu, respectivamente. Após isso, seu programa deve ler dois valores inteiros que indicam a velocidade dos pokémon Ivysaur e Pikachu, respectivamente. Em seguida, o seu programa deve ler os ataques de cada turno, sendo que cada ataque é indicado por dois valores, sendo o primeiro a força do ataque e o segundo o multiplicador de efetividade. Os valores correspondentes ao primeiro ataque são do pokémon mais rápido, enquanto os valores correspondentes ao segundo ataque são do pokémon mais lento. Ao final de cada turno, você deverá imprimir o `hp` de cada pokémon.

    HP Ivysaur = 
    HP Pikachu = 
    

Lembre-se que o ataque do pokémon com maior velocidade é considerado primeiro ao diminuir o `hp` do oponente. O `hp` de cada pokémon nunca será negativo, sendo que seu valor mínimo é zero. No momento que o `hp` de um dos pokémon chega em zero o mesmo é considerado como derrotado e a batalha é considerada encerrada, mesmo que isso ocorra no meio de um turno. Ao final da batalha, após imprimir o `hp` de cada pokémon, seu programa deve imprimir o nome e o `hp` do pokémon que venceu a batalha:

    Pokémon Vencedor: 
    HP do Vencedor: 
    

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
    

### [](#teste-02)Teste 02

[Entrada](dados/arq02.in)

    50
    100
    79
    80
    20
    2
    20
    1
    20
    0.5
    20
    1
    20
    0.5
    20
    1
    10
    0.5
    10
    2
    20
    2
    10
    0.5
    

[Saída](dados/arq02.out)

    HP Ivysaur = 10
    HP Pikachu = 80
    HP Ivysaur = 0
    HP Pikachu = 80
    Pokémon Vencedor: Pikachu
    HP do Vencedor: 80
    

### [](#teste-03)Teste 03

[Entrada](dados/arq03.in)

    100
    90
    90
    60
    20
    1
    20
    2
    20
    1
    10
    0.5
    20
    0.5
    10
    2
    20
    1
    20
    1
    10
    1
    10
    0.5
    20
    1
    20
    2
    

[Saída](dados/arq03.out)

    HP Ivysaur = 60
    HP Pikachu = 70
    HP Ivysaur = 55
    HP Pikachu = 50
    HP Ivysaur = 35
    HP Pikachu = 40
    HP Ivysaur = 15
    HP Pikachu = 20
    HP Ivysaur = 10
    HP Pikachu = 10
    HP Ivysaur = 10
    HP Pikachu = 0
    Pokémon Vencedor: Ivysaur
    HP do Vencedor: 10
    

[](#código-base)Código Base
---------------------------

No arquivo auxiliar lab04.py você irá encontrar um código base para dar início ao processo de submissão desse laboratório.

[](#orientações)Orientações
---------------------------

*   Veja [aqui](../04) a página de submissão da tarefa.
*   O arquivo a ser submetido deve se chamar lab04.py.
*   No link "Arquivos auxiliares" há um arquivo compactado (aux04.zip) que contém todos os arquivos de testes abertos (entradas e saídas esperadas).
*   O laboratório é composto de 10 testes abertos e 10 testes fechados.
*   O limite máximo será de 20 submissões.
*   Acesse o sistema SuSy com seu RA (apenas números) e a senha que você utiliza para fazer acesso ao sistema da DAC.
*   Você deve seguir as instruções de submissão descritas no enunciado.
*   Serão considerados apenas os resultados da última submissão.
*   Esta tarefa tem peso 2.
*   O prazo final para submissão é dia 17/09/2023 (domingo).
