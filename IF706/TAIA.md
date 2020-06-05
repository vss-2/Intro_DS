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
