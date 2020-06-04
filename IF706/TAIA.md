# Algoritmos Bioinspirados

### Aula 3:
#### Um algoritmo evolutivo deve possuir, pelo menos:
    População (e Combinação)
    Reprodução
    Mutação (e Recombinação)
    Seleção (aumento de fitness)
    Condição de térmico
    
#### Características de um AE:
    São da categoria geração e teste
    São estocásticos (estados indeterminados por eventos aleatórios) e baseados na população
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
Representa conceitualmente as condições as quais a população deve se adaptar. Representa numericamente a função qualdiade ou função objetivo. Assinala um valor real para a adaptação (ou fitness) de cada fenótipo, formando o critério base para a seleção. Logo, quanto maior o poder de discriminação, melhor resultado apresentará da aplicação da função fitness.
