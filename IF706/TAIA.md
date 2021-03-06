# Algoritmos Bioinspirados

### Aula 3:
#### Um algoritmo evolutivo deve possuir, pelo menos:
    População (e Combinação)
    Reprodução
    Mutação (e Recombinação)
    Seleção (aumento de fitness)
    Condição de térmico
    
#### Características de um AE:
    São da categoria geração e teste.
    São estocásticos (estados indeterminados por eventos aleatórios) e baseados na população.
    Operadores de Variação (Mutação e Recombinação) criam diversidade da população.
    Seleção reduz a diversidade e atua como a força propulsora para a qualidade.

#### Esquema:
    Inicialização gera uma ⟹ População ⟹
    Seleção dos pais atua nos ⟹ Pais ⟹
    Recombinação dos genes dos pais e mutação nos mesmos atuam gerando ⟹ 
    Descendentes ⟹ 
    Seleção dos sobreviventes atua na ⟹ População ⟹ 
    Até condição de parada estar satisfeita.
    
#### Os conceitos de: 
Algoritmos Genéticos, Estratégias Evolutivas, Programação Evolutiva e Programação Genética; são bastantes semelhantes conceitualmente, entretanto, quando se trata das técnicas de implementação, é essencial escolher operadores de variação adequados as representações escolhidas. Em contra partida, os operadores de seleção, em todos os casos, uusam apensa informações do fitness e são independentes das representações.

#### Análise de representações:
    
    Dado que existe uma solução candidata pertencente a um espaço fenotípico.
    
    E os indivíduos são codificados em cromossomos pertencentes a um espaço genotípico.
    
    E que a operação codificação: fenótipo ⟹ genótico está definida (não necessariamente 1 ⟹ 1).
    
    E que a operação de decodificação: genótipo ⟹ fenótipo (não necessariamente 1 ⟹ 1).
    
    E que os cromossomos contêm genes, os quais são posições (normalmente fixadas) chamadas locus, e tais posições possuem um valor.
    
    Logo, de forma a garantir um ótimo global, toda possível solução deve ser representada no espaço genótipo.
    
#### Função de Avaliação (Função fitness):
Representa conceitualmente as condições as quais a população deve se adaptar. Representa numericamente a função qualidade ou função objetivo. Assinala um valor real para a adaptação (ou fitness) de cada fenótipo, formando o critério base para a seleção. Logo, quanto maior o poder de discriminação, melhor resultado apresentará da aplicação da função fitness.

#### População
É um conjunto de possíveis soluções (estáticas), normalmente tem um tamanho fixo e é um multi-conjunto de genótipos. Em alguns algoritmos é possível adicionar estruturas espaciais (obstáculos, relevo, etc) sobre a população. É o caso de Algoritmos Evolutivos que estão sobre arquiteturas paralelas de processamento (interação população x ambiente), podendo ser usado para se referir à questões como distâncica e vizinhança. <br>
Os operadores de seleção geralmente usam informações adquiridas exclusivamente da população, de forma que as probabilidades de seleção são referentes à geração atual. <br>
A diversidade de uma população diz respeito aos diferentes números de:

    Fitness
    Fenótipos
    Genótipos
Existentes em uma população. <br>

#### Mecanismos de seleção dos pais
Diz respeito a probabilidade dos indivíduos atuarem como pais, o que depende dos seus respectivos valoress de fitness, dado que quanto mais apto, maior poder de reprodução. <br>
O mecanismo de seleção é geralmente probabilístico, logo, as melhores soluções tem maiores chances de se tornarem pais do que as piores soluções. Entretanto, vale a pena ressaltar que nenhum indivíduo tem probabilidade zero de seleção, isso evita que "máximos locais" (possibilitado pela natureza estocástica do processo seletivo).

#### Operadores de variação
Sua função é gerar novas soluções candidatas. Normalmente é divido entre dois tipos (quanto a aridade, ou seja, inputs):

    Aridade = 1: operadores de mutação
    Aridade > 1: operadores de recombinação
    Aridade = 2: operadores de cruzamento ou crossover
<br>
A maioria dos Algoritmos Evolutivos usam ambos operadores, porém há um grande debate a respeito da importância relativa de mutação e recombinação. Optar por apenas um dos operadores é uma escolha que depende da representação trabalhada.

#### Mutação
Atua sobre um genótipo gerando outro genótipo, sendo esta ação um elemento essencial de aleatoriedade (no caso diversidade) para população. A importância atribuída a mutação dependa da representação e do campo de aplicação:

    Algoritmo Genético Binário: operador responsável pela introdução e preservação da diversidade.
    Programação Genética: usado frequentemente.
Usar de mutação garante conectividade ao espaço de busca, garantindo uma prova de convergência, estudada em Teoria dos Esquemas.

#### Recombinação
Mistura informações no sentido: Pais (misturam) ⟹ Prole (nascem misturados). O processo de mistura é estocástico. A maior parte da prole é esperada ser pior ou de mesma qualidade dos pais. Entretanto o processo também garante que alguns filhos serão melhores que os pais devido a combinações de genótipos com boas características. Tal procedimento descrito é exatamente o mesmo que ocorre na nossa natureza.

#### Seleção por sobrevivência
Também chamado de recolocação. A maior parte dos Algoritmos Evolutivos usa uma população de tamanho fixo, e portanto, precisa de uma forma de garantir novas gerações.
Este tipo de seleção é geralmente determinístico:

    Baseado no fitness: por exemplo, descarte do menos apto.
    Baseado na geração: extingue pais para sobrevivência dos filhos.
Algumas vezes realiza combinação (elitismo: é feita a cópia dos melhores genótipos).

#### Inicialização
Geralmente a inicialização da população dos Algoritmos Evolutivos é aleatória. <br> Necessita que seja garantida a possibilidade da varredura e mistura de todos os possíveis valores dos genes. Vale ressaltar que é possível usar a inicialização para incluir soluções existentes, ou heurísticas específicas relativas ao problema para "semear" (direcionar) a população.

#### Condição de término
Esta condição deve ser checada a cada geração. Algumas condições:

    Buscar por fitness mínimo.
    Quantidade máxima de gerações permitidas.
    Queda a nível mínimo de diversidade.
    Quantidade máxima de gerações sem aumento de fitness.
    Busca por alguma característica específica do problema.

### Aula 4:
#### Usando Algoritmos Evolutivos


#### Introdução a 8-Rainhas
Podemos usar do problema das 8 rainhas em conjunto com algoritmos genéticos para solucioná-lo de forma não trivial. Com os conhecimentos já vistos anteriormente sabemos que é necessária a existência de fenótipos e genes para nossa população. Para esta situação particular, tomemos como fenótipos as configurações de cada rainha no tabuleiro; Como genótipos, temos: as permutações de 1 à 8 num vetor de tamanho 8, onde cada valor representa a posição de cada rainha em sua respectiva linha. Desta forma, teremos como representar todas as situações do tabuleiro (válidas e inválidas) e assim usar AEs para resolver o problema. <br>

#### Definindo fenótipo e genótipo
Para sabermos o fit, precisamos definir a penalidade, dadas as configurações das rainhas.
Sabemos que uma solução é inválida quando uma rainha está atacando outra. Quanto mais rainhas estiverem em uma posição de ataque a outra rainha, maior penalidade ela deve ter, logo, a penalidade de dada rainha (no nosso genótipo representado em array) é justamente a quantidade de rainhas que ela acaba, e a qualidade de uma configuração (fenótipo), é a soma das penalidades. Nessa abordagem estamos tentando maximizar a configuração, logo: Fitness = 1 / (1 + penalidade).


#### Seleção

Para seleção dos pais, poderemos usar, por exemplo, as abordagens: 
    Torneio, a partir de 5 indivíduos escolhidos de forma aleatória, escolheremos os 2 melhores como pais.
    Roleta, dê uma chance para cada indivíduo da população, sendo a probabilidade proporcional ao seu fitness, para então escolher de 2 pais.


#### Recombinação

Como precisamos garantir que seja encontrada uma solução, optamos por definir que a recombinação gerará 2 indivíduos. Para definir como funciona o nosso crossover:
    Escolhemos aleatoriamente um ponto (posição do array);
    Os valores de antes do ponto serão copiados dos pais;
    Os valores depois do ponto serão os valores, na ordem de aparição, trocados entre os pais;

#### Mutação

Algumas alternativas que podemos usar para simular a mutação seriam:
    Permutando aleatoriamente dois valores de posição do genótipo(array);
    Modificando aleatorialmente algum(s) valor(es) do genótipo(array);
    
   
#### Seleção de sobrevivência

A abordagem que vamos utilizar consistem em trocar indivíduos ruins por novos na população (fixa), logo:
    Ordenar a população pelo fitness (decrescente);
    Substitua um indivíduo que tenha fitness menor que o fitness do filho recém gerado;
    

#### Tabela com nossas escolhas tomadas para abordar problema das 8-Rainhas

| Característica                | Tipo                                  |
|-------------------------------|---------------------------------------|
| Representação                 | Permutação                            |
| Probabilidade de recombinação | 100%                                  |
| Técnica de mutação            | Swap                                  |
| Probabilidade de mutação      | 80%                                   |
| Método de seleção dos pais    | Melhor de 2 entre 5 aleatórios        |
| Seleção dos sobreviventes     | Substitua o pior                      |
| Tamanho da população          | 100                                   |
| Número de filhos por pais     | 2                                     |
| Inicialização                 | Aleatória                             |
| Condição de término           | Solução encontrada ou 10.000 seleções |

#### Comportamento e fases típicas de um Algoritmo Evolutivo

* Fases iniciais <br>
    Temos no conjunto uma distribuição populacional quase aleatória.

* Fase intermediárias <br>
    A população encontrará-se arrumada em torno das "colinas" (regiões com pontuação da população mais próxima do objetivo).
    
* Fase finais <br>
    População concentrada nos picos das colinas (a população está concentrada majoritariamente no melhor objetivo, ou arredores,  encontrados).

#### Tempo de espera

A relação entre melhor fitness populacional X número de inerações parece, usualmente, o gráfico de uma função logarítmica. 
Ou seja, há um crescimento rápido do fitness nas primeiras iterações e um crescimento mínimo depois de várias iterações. <br>
O tempo de espera depende basicamente do quão necessário é a melhoria para a solução do problema, ou a quantidade de tempo disponível.
    
#### Inicialização esperta

Podemos poupar iterações, e consequentemente tempo, através de uma inicialização direcionada (ou seja, não aleatória). 
Entretanto, devemos ter o cuidado para não se restrigir o espaço de genótipo, 
por exemplo, enviesando a solução (ou, no caso, nos restringindo a um máximo local). 
Também devemos nos atentar se há possibilidade, pois é possível que não existam boas soluções.
    
    
#### Algoritmos Evolutivos no Contexto Global - Considerações

Algoritmos evolutivos são ferramentas robustas de resolução de problemas. 
Na maioria dos casos, tais ferramentas aplicadas especificamente a um problema podem ter melhor desempenho que um algoritmo genérico, entretanto, 
sua utilização será limitada a situação e sua execução (geralmente) não será boa para todas as instâncias do problema. <br>
Dado que existem muitas abordagens sobre o uso dos Algoritmos Evolutivos, 
a meta é ter uma ferramenta robusta que tenha um desempenho tão bom quanto a abordagem específica e que consiga abranger um grande espectrode problemas e instâncias.
    
#### Algoritmos Evolutivos e Conhecimentos de Domínios

Nos anos 90 surgiram correntes que tinha como ideal adicionar conhecimento específico dos problemas junto aos AEs, na tentativa de beneficiá-los com conhecimento prévio, por exemplo, uso de métodos guiados. Ainda que o montate de conhecimento pudesse ser variável, resultado da inserção do mesmo não foi a esperada. Houve uma deformação na curva de desempenho que causou picos, uma vez que o algoritmo atuava de forma ótima em casos específicos, mas perdia tanto para os algoritmos evolutivos sem conhecimento prévio, como para busca aleatória, em casos gerais. <br>
    Apesar da aparente estagnação, teorias recentes sugerem que a busca por um algoritmo de propósito geral pode ser frutífera.
    
#### Computação Evolutiva - Considerações Finais

Podemos resumir que a computação evolutiva trata-se de obter uma otimização global. Esta otimização é a busca pela melhor solução X sobre um conjunto fixo S. Ela pode fazer uso de duas abordagens: <br>
* Determinística <br> Garante encontrar X, porém pode ter custo de tempo superpolinomial (ou seja, sem tempo de conclusão determinado).
* Heurística <br> Regras de decisão são aplicadas para gerar a próxima solução, tal que, solução X pertence ao conjunto fixo S, mas nada garante que as soluções encontradas são ótimas.
    
Algumas heurísticas impõem uma estrutura local sobre o conjunto S, de tal forma que elas podem garantir o melhor ponto em uma estrutura (são Algorítmos do tipo [Hill Climb](https://en.wikipedia.org/wiki/Hill_climbing)). Esta abordagem normalmente encontra vários ótimos locais (podendo não achar o global), mas é considerada pois encontra tais soluções rapidamente. Outras heurísticas utilizadas visam atuar em: <br>
* Uso de população
* Uso de múltiplos operadores de busca estocásticos (indeterminados, especialmente variando os operadores, fornecendo mais de um parâmetro)
* Seleção estocástica
