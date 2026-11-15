---
source_reference:
- tópico-7-est2-p2.txt
- tópico-8-est2-p2.txt
- tópico-13-est2-p2.txt
- tópico-14-est2-p2.txt
subject: Estabilidade do Navio II (EST-2)
tags:
- est-2
- estabilidade-naval
- draft-survey
- esforcos-estruturais
- estabilidade-dinamica
- guia-de-estudos
- prova
title: Guia Didático e Intuitivo de EST-2 --- Tópicos 7, 8, 13 e 14
type: Material Didático Intuitivo e Progressivo
---

# Guia Didático e Intuitivo de EST-2

## Tópicos 7, 8, 13 e 14

### Da intuição física à definição técnica --- preparação para a prova

> \[!IMPORTANT\] **Como este material está organizado**
>
> Cada assunto segue uma sequência didática: 1. **Entenda a ideia:**
> explicação simples do fenômeno. 2. **Visualize:** representação mental
> ou diagrama. 3. **Entenda o funcionamento:** relação entre os
> conceitos. 4. **Definição técnica:** formulação adequada para estudo.
> 5. **O que memorizar:** regras, sinais e valores essenciais. 6.
> **Atenção para a prova:** confusões e pegadinhas possíveis.
>
> O conteúdo foi construído a partir dos quatro arquivos de trechos
> selecionados das apostilas. Quando um assunto depende de informações
> que não aparecem nesses arquivos, isso é indicado em vez de inventar
> dados.

------------------------------------------------------------------------

## Mapa geral dos assuntos

``` mermaid
flowchart TD
    A["EST-2"] --> B["Tópico 7<br/>Correção da leitura do calado"]
    A --> C["Tópico 8<br/>Draft Survey"]
    A --> D["Tópico 13<br/>Esforços estruturais"]
    A --> E["Tópico 14<br/>Estabilidade dinâmica"]
    B --> B1["Marcas, compasso e deflexão"]
    B --> B2["Calado correspondente"]
    C --> C1["Sequência da operação"]
    C --> C2["Densidade, constante e consumíveis"]
    D --> D1["Peso, empuxo e esforços"]
    D --> D2["Ondas, Bonjean e momento fletor"]
    E --> E1["Estática x dinâmica"]
    E --> E2["Área GZ, energia e critérios"]
```

------------------------------------------------------------------------

# BLOCO 1 --- TÓPICO 7: CORREÇÃO DA LEITURA DO CALADO

## 1.1. Por que as marcas de calado podem precisar de correção?

### A. Entenda a ideia

As marcas de calado são referências usadas para observar quanto o navio
está mergulhado na água. O ideal seria que essas marcas estivessem
exatamente sobre as perpendiculares do navio. Na prática, devido às
formas do casco, isso nem sempre acontece.

Imagine que uma régua esteja colocada alguns centímetros afastada do
ponto exato em que você gostaria de medir. Se a régua estiver paralela
ao nível do chão, essa diferença de posição pode não alterar a leitura.
Mas, se a régua estiver inclinada, a posição afastada passa a produzir
uma diferença na medida.

Com as marcas de calado acontece algo semelhante: quando o navio está em
águas parelhas, a posição deslocada das marcas não gera o erro de
defasagem descrito no material. Quando o navio está compassado, a
diferença de posição pode produzir erro e exigir correção.

### B. Visualize o fenômeno

``` mermaid
flowchart TD
    A["Marcas de calado fora das perpendiculares"] --> B{"Como está o navio?"}
    B -->|"Águas parelhas, sem compasso"| C["Não há erro de defasagem por essa posição"]
    B -->|"Compassado pela proa ou pela popa"| D["Surge defasagem na leitura"]
    D --> E["É necessário aplicar correção"]
```

-   **Águas parelhas:** proa e popa estão no mesmo nível de calado, sem
    compasso.
-   **Navio compassado:** existe diferença entre os calados de vante e
    de ré.
-   **Defasagem:** diferença provocada pela leitura em uma marca que não
    coincide com a perpendicular de referência.

### C. Entenda o funcionamento

A correção do calado devido ao compasso é utilizada para determinar o
calado do navio no centro de flutuação, tomando como referência o calado
médio.

O ponto essencial é perceber que a leitura feita na marca não representa
necessariamente, sem correção, o calado na posição de referência
desejada.

### D. Definição técnica

> **Correção de leitura do calado:** ajuste aplicado à leitura observada
> nas marcas quando a posição dessas marcas, fora das perpendiculares,
> combinada com o compasso do navio, provoca uma defasagem que altera o
> calado de referência.

### E. O que precisa memorizar

-   As marcas deveriam estar sobre as perpendiculares.
-   Devido às formas do navio, isso pode não ocorrer.
-   Em águas parelhas, a posição deslocada das marcas não provoca o erro
    de defasagem indicado.
-   Com o navio compassado, pela proa ou pela popa, pode surgir erro que
    precisa ser corrigido.
-   A correção permite determinar o calado no centro de flutuação, tendo
    como referência o calado médio.

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas clássicas** - Dizer que as marcas de calado
> sempre estão exatamente sobre as perpendiculares. - Afirmar que a
> posição deslocada das marcas produz erro mesmo em águas parelhas. -
> Dizer que o erro só aparece quando o navio está compassado pela popa.
> O material menciona compasso pela proa ou pela popa. - Confundir a
> leitura observada na marca com o calado já corrigido no centro de
> flutuação.

------------------------------------------------------------------------

## 1.2. Deflexão do casco: alquebramento e contra-alquebramento

### A. Entenda a ideia

O casco do navio é uma estrutura longa. Assim como uma régua comprida
pode se curvar quando recebe esforços, o casco também pode sofrer
deformações ao longo do comprimento.

Quando isso acontece, o calado observado a meio-navio pode deixar de
corresponder ao calado médio calculado pelas leituras de vante e ré.

Para identificar essa deformação, compara-se o calado a meio-navio com o
calado médio.

### B. Visualize o fenômeno

A diferença entre o calado a meio-navio e o calado médio é chamada de
deflexão do casco:

$$\delta Z = d_m - d_{med}$$

Onde:

-   $\delta Z$ = deflexão do casco a meio-navio;
-   $d_m$ = calado a meio-navio;
-   $d_{med}$ = calado médio.

``` mermaid
flowchart TD
    A["Calcular δZ = dm - dmed"] --> B{"Qual o sinal de δZ?"}
    B -->|"Negativo"| C["Alquebrado"]
    B -->|"Positivo"| D["Contra-alquebrado"]
    D --> E["Correção aditiva"]
```

### C. Entenda o funcionamento

A operação é uma comparação:

1.  Identifica-se o calado a meio-navio.
2.  Determina-se o calado médio.
3.  Subtrai-se o calado médio do calado a meio-navio.
4.  Observa-se o sinal do resultado.

Se o resultado for negativo, o navio está alquebrado. Se for positivo,
está contra-alquebrado.

O sinal é decisivo. Não se deve decorar apenas os nomes: é necessário
associar cada condição ao sinal correto.

### D. Definição técnica

> **Deflexão do casco a meio-navio ($\delta Z$):** diferença entre o
> calado a meio-navio ($d_m$) e o calado médio ($d_{med}$). Uma deflexão
> negativa caracteriza o navio alquebrado; uma deflexão positiva
> caracteriza o navio contra-alquebrado.

### E. O que precisa memorizar

  Resultado de $\delta Z$   Condição do casco
  ------------------------- -------------------
  Negativo ($-$)            Alquebrado
  Positivo ($+$)            Contra-alquebrado

-   No contra-alquebramento, a correção é **aditiva**.
-   O calado médio pode não corresponder ao calado lido a meio-navio
    quando há deflexão.
-   Isso pode ocorrer mesmo com o centro de flutuação a meio-navio e/ou
    sem compasso.

### F. Atenção para a prova

> \[!WARNING\] **Não inverta os sinais** - Deflexão negativa =
> alquebrado. - Deflexão positiva = contra-alquebrado. -
> Contra-alquebrado = correção aditiva.
>
> Uma questão pode trocar apenas uma dessas associações e tornar a
> afirmação falsa.

------------------------------------------------------------------------

## 1.3. Calado correspondente ou calado médio real

### A. Entenda a ideia

O calado lido diretamente nas marcas pode precisar de mais de um ajuste.
É como medir a altura de um objeto com uma régua que está inclinada e
posicionada fora do ponto de referência: primeiro é preciso corrigir os
efeitos que distorcem a leitura.

No navio, o calado correspondente é o resultado após as correções
indicadas no material.

### B. Visualize a sequência

``` mermaid
flowchart TD
    A["Calado lido nas marcas"] --> B["Correção para as perpendiculares"]
    B --> C["Correção devido ao compasso"]
    C --> D["Correção para a deflexão do casco"]
    D --> E["Calado correspondente<br/>ou calado médio real"]
```

### C. Entenda o funcionamento

O calado correspondente não é simplesmente uma leitura isolada. Ele
representa o calado lido nas marcas depois de corrigido:

1.  Para as perpendiculares;
2.  Devido ao compasso do navio;
3.  Para a deflexão do casco.

Essas correções tratam de efeitos diferentes. Não se deve eliminar uma
delas nem trocar sua finalidade.

### D. Definição técnica

> **Calado correspondente ou calado médio real:** calado lido nas marcas
> e corrigido para as perpendiculares, para o compasso do navio e para a
> deflexão do casco.

### E. O que precisa memorizar

-   Nome alternativo: **calado médio real**.
-   Parte da leitura nas marcas.
-   Recebe três correções: perpendiculares, compasso e deflexão.

### F. Atenção para a prova

> \[!TIP\] **Resposta curta para memorizar**
>
> "Calado correspondente é o calado lido nas marcas, corrigido para as
> perpendiculares, para o compasso e para a deflexão do casco."

------------------------------------------------------------------------

# BLOCO 2 --- TÓPICO 8: DRAFT SURVEY

## 2.1. O que é o Draft Survey e para que serve?

### A. Entenda a ideia

Imagine que um navio carregue milhares de toneladas de granéis sólidos.
Nem sempre é prático pesar cada porção da carga individualmente. Uma
alternativa é determinar indiretamente o peso da carga observando a
variação do deslocamento do navio.

O Draft Survey utiliza as leituras de calado e informações do navio para
determinar o deslocamento e, a partir dele, calcular o peso da carga
embarcada ou desembarcada.

Além disso, a operação permite calcular a constante de bordo.

### B. Visualize os métodos de determinação do peso

O material apresenta cinco possibilidades:

1.  Pesar cada volume embarcado, como na carga geral, usando os pesos
    indicados nos conhecimentos de embarque.
2.  Pesar a carga em terra, por meio de balança.
3.  Medir indiretamente o volume dos tanques de terra, para granéis
    líquidos.
4.  Medir indiretamente o volume ocupado nos tanques de bordo, para
    granéis líquidos.
5.  Determinar o peso por meio da medida do calado, no caso de granéis
    sólidos.

### C. Entenda o funcionamento

O peso calculado a bordo pode apresentar diferença em relação ao cálculo
do terminal. Isso ocorre devido aos processos utilizados e às
aproximações dos cálculos.

A diferença, porém, deve respeitar uma tolerância máxima de **0,2% do
total da carga movimentada**, embarcada ou desembarcada, tomando-se o
maior valor.

Exemplo apresentado no material:

-   Carga movimentada: 30.000 t.
-   Tolerância: 0,2%.
-   Diferença aceitável: 60 t.

Se a diferença superar a tolerância, um dos cálculos está equivocado e
os cálculos devem ser refeitos.

### D. Definição técnica

> **Draft Survey:** operação de determinação indireta do peso da carga
> por meio das leituras de calado e do cálculo do deslocamento do navio.
> Seus objetivos são calcular o peso da carga embarcada ou desembarcada
> e determinar a constante de bordo.

### E. O que precisa memorizar

  Informação            Regra
  --------------------- ------------------------------------
  Objetivos             Peso da carga e constante de bordo
  Tolerância            0,2%
  Base de cálculo       Total da carga movimentada
  Referência            Maior valor
  Acima da tolerância   Refazer os cálculos

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - A tolerância não é 2%; é **0,2%**. - A
> tolerância é calculada sobre o total da carga movimentada. - Deve-se
> tomar o maior valor. - Se a diferença superar a tolerância, não se
> aceita simplesmente o resultado: os cálculos devem ser refeitos. - O
> Draft Survey não serve apenas para calcular o peso da carga; também
> permite determinar a constante de bordo.

------------------------------------------------------------------------

## 2.2. A operação deve ser continuada

### A. Entenda a ideia

O Draft Survey é uma operação composta por etapas que precisam ser
executadas em sequência. Imagine uma investigação em que cada medição
depende das condições observadas naquele momento. Se as etapas forem
interrompidas e realizadas em momentos diferentes, as condições podem
mudar e comprometer a consistência dos resultados.

Por isso, a operação deve ser feita de forma continuada, isto é, de uma
só vez.

### B. Visualize a sequência das sete etapas

``` mermaid
flowchart TD
    A["1. Ler os calados nas marcas do costado"] --> B["2. Determinar a densidade da água"]
    B --> C["3. Determinar a constante do navio"]
    C --> D["4. Determinar o peso dos consumíveis"]
    D --> E["5. Calcular o calado correspondente"]
    E --> F["6. Determinar o deslocamento real"]
    F --> G["7. Determinar o peso da carga"]
```

### C. Entenda o funcionamento

A sequência tem uma lógica:

-   Primeiro, observam-se os calados.
-   Depois, determina-se a densidade da água em que o navio flutua.
-   Em seguida, levantam-se a constante e os consumíveis.
-   Com esses dados, calcula-se o calado correspondente.
-   A partir dele, determina-se o deslocamento real.
-   Por fim, determina-se o peso da carga.

### D. Definição técnica

> A operação de Draft Survey deve ser realizada de forma continuada, ou
> seja, de uma só vez, respeitando a sequência de sete etapas
> apresentada na apostila.

### E. O que precisa memorizar

**Ordem das sete etapas:**

1.  Calados;
2.  Densidade;
3.  Constante;
4.  Consumíveis;
5.  Calado correspondente;
6.  Deslocamento real;
7.  Peso da carga.

### F. Atenção para a prova

> \[!WARNING\] **A ordem é matéria de prova** Uma questão pode manter
> todas as etapas, mas trocar duas posições. Outra pode afirmar que a
> operação deve ser interrompida e retomada em outro momento. A
> operação, conforme o material, é continuada e feita de uma só vez.

------------------------------------------------------------------------

## 2.3. Documentos necessários a bordo

### A. Entenda a ideia

Para realizar o Draft Survey, não basta observar o calado. É necessário
consultar documentos técnicos do navio, pois eles fornecem informações
sobre deslocamento, capacidade e quantidade de líquidos nos tanques.

### B. Relação dos documentos

Além das informações fornecidas pelo Imediato ou pelo Comandante, o
material lista:

1.  Tabela ou plano de curvas hidrostáticas;
2.  Tabelas de sondagens dos tanques de óleo combustível, lubrificante,
    diesel, água e outros tanques da máquina;
3.  Tabelas de ulagens ou sondagens dos tanques laterais elevados e de
    outros tanques que possam levar carga ou lastro;
4.  Caderno de estabilidade ou livro de dados do navio (*Data Book*);
5.  Plano de capacidade;
6.  Plano de arranjo geral.

### C. O que precisa memorizar

-   Curvas hidrostáticas;
-   Tabelas de sondagens;
-   Tabelas de ulagens;
-   Caderno de estabilidade / *Data Book*;
-   Plano de capacidade;
-   Plano de arranjo geral.

### D. Atenção para a prova

> \[!TIP\] **Pegadinha** Não confunda plano de capacidade com plano de
> arranjo geral. Ambos aparecem na lista e são documentos distintos.

------------------------------------------------------------------------

## 2.4. Leitura do trim e determinação da densidade

### A. Entenda a ideia

O trim nas marcas indica a diferença entre o calado de ré e o calado de
vante. A densidade da água também precisa ser medida corretamente, pois
o navio pode flutuar em águas com densidades diferentes.

A leitura da densidade deve representar as condições do local e do
momento em que os calados foram observados.

### B. Fórmula do trim nas marcas

$$TM = H_{MAR} - H_{MAV}$$

Onde:

-   $TM$ = trim nas marcas;
-   $H_{MAR}$ = calado na marca de ré;
-   $H_{MAV}$ = calado na marca de vante.

Portanto, a ordem é **ré menos vante**.

### C. Como medir a densidade

O procedimento descrito no material é:

1.  Coletar amostras de água na proa, a meio-navio e a ré.
2.  Utilizar um balde para retirar as amostras.
3.  Passar a água para uma proveta.
4.  Colocar o densímetro calibrado em kg/m³.
5.  Fazer a leitura das três amostras.
6.  Calcular a média das três leituras, considerada a densidade real.

A coleta deve ocorrer no mesmo instante e no mesmo local das leituras de
calado.

``` mermaid
flowchart TD
    A["Amostra na proa"] --> D["Leitura no densímetro"]
    B["Amostra a meio-navio"] --> E["Leitura no densímetro"]
    C["Amostra na ré"] --> F["Leitura no densímetro"]
    D --> G["Média das três leituras"]
    E --> G
    F --> G
    G --> H["Densidade real"]
```

### D. O que precisa memorizar

  Item                     Regra
  ------------------------ ---------------------------------------
  Trim nas marcas          Ré menos vante
  Momento da coleta        Mesmo instante das leituras de calado
  Local da coleta          Mesmo local das leituras
  Quantidade de amostras   Três
  Posições                 Proa, meio-navio e ré
  Instrumento              Densímetro
  Unidade indicada         kg/m³
  Densidade real           Média das três leituras

### E. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Inverter o trim para vante menos ré. -
> Dizer que basta uma amostra de água. - Trocar as posições de coleta. -
> Afirmar que a densidade pode ser medida em outro momento e local. -
> Trocar o densímetro por outro instrumento. - Esquecer que a densidade
> real é a média das três leituras.

------------------------------------------------------------------------

## 2.5. Constante do navio e consumíveis

### A. Entenda a ideia

Durante a operação, é necessário separar dois grupos de pesos:

-   Pesos pequenos que praticamente não variam: **constante do navio**.
-   Materiais cujos pesos variam bastante e podem ter seus valores
    determinados: **consumíveis**.

Uma analogia simples é separar os itens fixos de uma embarcação dos
materiais que são utilizados e repostos durante a viagem.

### B. Constante do navio

O material define a constante como a soma dos pequenos pesos que quase
não variam.

O deslocamento leve pode ser consultado no Livro de Dados, no Caderno de
Estabilidade, no Plano de Capacidade e em outros documentos do navio.

### C. Consumíveis

O arquivo selecionado lista:

-   Óleo combustível;
-   Óleo diesel;
-   Óleo lubrificante;
-   Água de lastro;
-   Água doce;
-   Água destilada.

### D. Quadro comparativo

  -----------------------------------------------------------------------
  Constante do navio                  Consumíveis
  ----------------------------------- -----------------------------------
  Soma de pequenos pesos que quase    Materiais cujos pesos variam
  não variam                          bastante

  Representa pesos praticamente       Seus valores podem ser determinados
  constantes                          na operação

  Associada à constante de bordo      Inclui óleos e águas listados no
                                      material
  -----------------------------------------------------------------------

### E. Atenção para a prova

> \[!WARNING\] **Não misture as classificações** O arquivo selecionado
> apresenta a definição resumida da constante e a lista de consumíveis.
> Para a composição completa da constante --- incluindo itens como
> guarnição, pertences, líquidos em redes, caldeiras, condensadores e
> cárteres --- consulte também a apostila integral do Tópico 8. Esses
> itens não estão detalhados no trecho selecionado usado nesta seção.

------------------------------------------------------------------------

## 2.6. Calado correspondente e correções de trim no Draft Survey

### A. Entenda a ideia

No cálculo do Draft Survey, o calado usado para entrar nas tabelas não
recebe simplesmente todas as correções de uma vez. O material destaca
que a correção para o trim será transformada em peso e aplicada ao
deslocamento.

Isso significa que é necessário distinguir a correção do calado das
correções que são tratadas diretamente como peso.

### B. Entenda a sequência

-   Entra-se nas tabelas com o calado médio corrigido para as
    perpendiculares e para a deflexão.
-   A correção para o trim é transformada em peso: primeira correção
    para o trim.
-   Pode ser necessária uma segunda correção para o trim, também
    aplicada em peso.
-   Se o trim for maior que 1% do comprimento entre perpendiculares
    (Lpp), aplica-se a segunda correção devido ao trim ao deslocamento.

### C. O que precisa memorizar

  -----------------------------------------------------------------------
  Item                                Regra
  ----------------------------------- -----------------------------------
  Calado para entrada nas tabelas     Corrigido para perpendiculares e
                                      deflexão

  1ª correção para trim               Transformada em peso

  2ª correção para trim               Também aplicada em peso

  Condição citada para a 2ª correção  Trim maior que 1% do Lpp
  -----------------------------------------------------------------------

### D. Atenção para a prova

> \[!WARNING\] **Pegadinha de procedimento** Não afirme que o calado
> usado para entrar nas tabelas já deve incluir a correção do trim.
> Segundo o trecho, a correção para o trim é transformada em peso e
> aplicada ao deslocamento.

------------------------------------------------------------------------

# BLOCO 3 --- TÓPICO 13: ESFORÇOS ESTRUTURAIS

## 3.1. O navio como uma viga flutuante

### A. Entenda a ideia

Um navio é uma estrutura muito comprida, apoiada pela água ao longo de
seu comprimento. Por isso, pode ser comparado a uma viga flutuante.

Imagine uma régua apoiada em vários pontos. Se as forças que atuam sobre
ela estiverem distribuídas de maneira equilibrada, a régua tende a
permanecer sem deformação significativa. Se algumas regiões receberem
mais carga que outras, a régua pode se curvar.

No navio, os pesos da carga e o empuxo da água atuam ao longo do
comprimento. Quando essas forças não estão distribuídas de maneira
equilibrada, surgem esforços estruturais.

### B. Visualize o fenômeno

``` mermaid
flowchart TD
    A["Navio como viga flutuante"] --> B["Distribuição de pesos"]
    A --> C["Distribuição de empuxo"]
    B --> D{"Peso e empuxo estão equilibrados ao longo do navio?"}
    C --> D
    D -->|"Sim, seção a seção"| E["Não há tendência à deformação global descrita"]
    D -->|"Não"| F["Surgem esforços estruturais"]
    F --> G["Força cortante e momento fletor"]
```

### C. Entenda o funcionamento

Pelo Princípio de Arquimedes, quando os pesos estão distribuídos de
forma que, em todos os pontos, a força do peso seja igual à força do
empuxo, nenhuma deformação se produzirá.

Entretanto, se a distribuição não for equitativa ao longo do
comprimento, em cada parte do navio pode haver predominância do peso
sobre o empuxo ou do empuxo sobre o peso.

Uma carga distribuída de maneira desigual nos porões e tanques faz com
que os blocos do navio apresentem condições de flutuação diferentes.

### D. Definição técnica

> **Esforços estruturais:** esforços que atuam sobre a estrutura do
> navio e tendem a deformá-la. No estudo longitudinal, estão
> relacionados principalmente à distribuição não uniforme dos pesos e do
> empuxo ao longo do comprimento da embarcação.

### E. O que precisa memorizar

-   O navio pode ser considerado uma viga flutuante.
-   O convés resistente e o fundo funcionam como abas da viga-navio.
-   A distribuição desigual de peso e empuxo provoca esforços.
-   A estrutura precisa ter resistência e rigidez para suportar as
    cargas.
-   A continuidade de resistência do casco é importante para que as
    partes trabalhem em conjunto.

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Dizer que o navio não sofre esforços
> quando está em repouso. - Afirmar que a distribuição desigual de pesos
> não interfere na estrutura. - Dizer que o navio não pode ser comparado
> a uma viga. - Confundir equilíbrio global com equilíbrio das forças ao
> longo de cada seção.

------------------------------------------------------------------------

## 3.2. Flexão: tração e compressão

### A. Entenda a ideia

Quando uma viga se curva, uma de suas faces tende a ficar mais curta e a
outra tende a ficar mais comprida.

-   A face interna da curvatura sofre **compressão**.
-   A face externa da curvatura sofre **tração**.

Pense em uma régua flexionada: na parte interna da curva, o material é
comprimido; na parte externa, é esticado.

### B. Visualize o fenômeno

``` mermaid
flowchart TD
    A["Viga submetida à flexão"] --> B["Face interna da curvatura"]
    A --> C["Face externa da curvatura"]
    B --> D["Compressão<br/>tende a encurtar"]
    C --> E["Tração<br/>tende a alongar"]
```

### C. O que memorizar

  Esforço      Efeito
  ------------ -------------------------
  Compressão   Tende a encurtar a face
  Tração       Tende a alongar a face

### D. Atenção para a prova

> \[!TIP\] **Associação direta** Face interna = compressão.\
> Face externa = tração.

------------------------------------------------------------------------

## 3.3. Esforços transversais, cavername, vaus e sloshing

### A. Entenda a ideia

Os esforços transversais estão relacionados aos balanços e aos
movimentos oscilatórios do navio. Quando o navio balança, sua estrutura
sofre ações que tendem a deformá-la transversalmente.

O material usa a comparação do navio com uma caixa: o cavername e os
vaus garantem a resistência transversal.

### B. Visualize o fenômeno

``` mermaid
flowchart TD
    A["Balanço e movimentos oscilatórios"] --> B["Movimento da massa do navio"]
    B --> C["Ações estruturais transversais"]
    C --> D["Alteração dos ângulos entre vaus e cavernas"]
    D --> E["Agudos em um bordo"]
    D --> F["Obtusos no outro bordo"]
```

Sob o movimento oscilatório da água, a massa do navio entra em
movimento. A princípio, existe sincronismo, que tende a desaparecer pela
inércia. Em determinado ponto, o movimento do navio passa a ocorrer em
sentido oposto sob a ação das vagas, contrariando a ação da inércia.

Como consequência, os ângulos formados pelos vaus com as cavernas tendem
a ficar agudos em um bordo e obtusos no outro.

### C. O que é Sloshing?

Imagine um tanque parcialmente cheio de água. Quando o navio se
movimenta, o líquido também se movimenta e sua superfície livre oscila.
Se essa oscilação for violenta, o líquido pode bater nas paredes do
tanque.

Esse fenômeno é chamado de **sloshing**.

### D. Definição técnica

> **Sloshing:** movimento violento e oscilação da superfície livre de um
> líquido dentro de um recipiente parcialmente preenchido, causado por
> perturbações externas. Pode provocar impactos nas paredes do tanque,
> afetar a estabilidade e causar danos estruturais devido à ressonância.

### E. O que precisa memorizar

-   Esforços transversais: relacionados aos balanços e movimentos
    oscilatórios.
-   Resistência transversal: cavername e vaus.
-   Ângulos vaus-cavernas: agudos em um bordo e obtusos no outro.
-   Sloshing: líquido em recipiente parcialmente cheio.
-   Consequências do sloshing: impactos, possível efeito na estabilidade
    e danos estruturais por ressonância.
-   Os esforços transversais são menos significativos que os
    longitudinais.

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Dizer que o sloshing ocorre apenas em
> tanques completamente cheios. - Trocar cavername e vaus por
> componentes que não aparecem na explicação. - Afirmar que os ângulos
> ficam agudos nos dois bordos. - Dizer que os esforços transversais são
> mais significativos que os longitudinais.

------------------------------------------------------------------------

## 3.4. Efeito das ondas e comprimento de onda

### A. Entenda a ideia

Quando o navio navega, não sofre apenas os efeitos da distribuição
irregular dos pesos. As ondas também alteram a flutuação ao longo do
casco.

Cada seção do navio pode deslocar uma quantidade diferente de água
conforme a posição da onda. Isso modifica a distribuição do empuxo e
pode aumentar os esforços estruturais.

### B. Relação entre comprimento da onda e comprimento do navio

O trecho selecionado destaca três situações:

  -----------------------------------------------------------------------
  Comprimento da onda                 Efeito descrito
  ----------------------------------- -----------------------------------
  Igual ao comprimento do navio       Condição em que os valores máximos
                                      dos esforços e do momento fletor
                                      são significativos

  Muito menor que o comprimento do    Alterações de calado com frequência
  navio                               muito alta; efeitos mais locais que
                                      globais

  Muito maior que o comprimento do    Pouca alteração no calado, com
  navio                               frequência muito baixa
  -----------------------------------------------------------------------

O material destaca que o momento fletor máximo ocorre quando o navio se
desloca em ondas cujo comprimento é igual ao seu comprimento, podendo
estar na condição de alquebrado ou contra-alquebrado.

### C. O que precisa memorizar

-   Comprimento de onda igual ao comprimento do navio: condição de maior
    significância para os esforços globais descritos.
-   Onda muito curta: efeitos mais locais.
-   Onda muito longa: pouca alteração no calado e frequência muito
    baixa.
-   O navio pode estar alquebrado ou contra-alquebrado.

### D. Atenção para a prova

> \[!WARNING\] **Pegadinha** Não troque "comprimento de onda igual ao
> comprimento do navio" por "comprimento de onda muito menor" ou "muito
> maior". O trecho associa a condição de maior momento fletor ao
> comprimento igual.

------------------------------------------------------------------------

## 3.5. Alquebramento e contra-alquebramento na estrutura

### A. Entenda a ideia

O casco pode se deformar longitudinalmente. O material selecionado
descreve explicitamente o alquebramento como uma deformação com
concavidade voltada para baixo.

Nessa condição, o convés fica tracionado e o fundo fica comprimido.

### B. O que memorizar

**Alquebramento:** - Concavidade voltada para baixo; - Tração no
convés; - Compressão no fundo.

### C. Atenção para a prova

> \[!WARNING\] **Cuidado com a troca de faces** No alquebramento
> descrito no trecho, o convés está sob tração e o fundo sob compressão.
> Não inverta essas duas condições.

------------------------------------------------------------------------

## 3.6. Curvas de Bonjean

### A. Entenda a ideia

Para estudar a distribuição do empuxo ao longo do navio, é necessário
conhecer as áreas submersas de suas seções transversais.

As curvas de Bonjean fornecem essas áreas para diferentes linhas d'água.
Com elas, é possível desenvolver cálculos relacionados ao volume de
carena e à distribuição longitudinal do empuxo.

### B. Visualize a aplicação

``` mermaid
flowchart TD
    A["Curvas de Bonjean"] --> B["Áreas das seções transversais"]
    B --> C["Volume de carena"]
    B --> D["Posição do centro de flutuação"]
    B --> E["Diagrama de empuxo"]
    F["Linha d'água"] --> A
    G["Navio em águas parelhas ou compassado"] --> A
```

### C. Definição técnica

> **Curvas de Bonjean:** curvas que fornecem as áreas das seções
> transversais do navio, em espaçamentos iguais, para diferentes linhas
> d'água. Permitem calcular o volume de carena, a posição do centro de
> flutuação e traçar o diagrama de empuxo.

### D. O que precisa memorizar

-   Fornecem áreas de seções transversais.
-   As seções são consideradas em espaçamentos iguais.
-   Permitem calcular o volume de carena.
-   Permitem determinar a posição do centro de flutuação.
-   Permitem traçar o diagrama de empuxo.
-   Podem ser utilizadas para qualquer linha d'água, com o navio em
    águas parelhas ou compassado.

### E. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Dizer que as curvas de Bonjean fornecem
> diretamente o peso da carga. - Afirmar que só podem ser usadas com o
> navio em águas parelhas. - Confundir áreas das seções transversais com
> áreas da superfície externa do casco.

------------------------------------------------------------------------

## 3.7. Momento fletor e força cortante

### A. Entenda a ideia

O momento fletor é o esforço que tende a curvar a estrutura em relação
ao seu eixo longitudinal. A força cortante e o momento fletor são
representações dos esforços globais ao longo da viga-navio.

Uma forma de compreender a relação entre eles é pensar que a curva do
momento fletor é obtida pela integração da curva da força cortante.

### B. Relação fundamental

``` mermaid
flowchart TD
    A["Curva da Força Cortante"] --> B["Integração"]
    B --> C["Curva do Momento Fletor"]
    C --> D["Representação dos esforços globais ao longo da viga-navio"]
```

### C. Definição técnica

> **Momento fletor:** soma dos momentos relativos a uma seção, contidos
> no eixo de uma peça e gerados por cargas aplicadas transversalmente ao
> eixo longitudinal. Produz um esforço que tende a curvar a estrutura,
> provocando tensões normais de tração e compressão.

### D. Convenção de sinal apresentada no trecho

O material selecionado adota a seguinte convenção:

-   Momento fletor **positivo** quando traciona a parte de baixo da
    viga;
-   E comprime a parte de cima.

> \[!IMPORTANT\] **Convenção de sinal** Esta é a convenção registrada no
> trecho selecionado. Ao resolver questões, use a convenção indicada no
> enunciado ou na apostila correspondente. Não misture convenções
> diferentes.

### E. O que precisa memorizar

  -----------------------------------------------------------------------
  Conceito                            Ideia central
  ----------------------------------- -----------------------------------
  Momento fletor                      Tende a curvar a estrutura

  Tração                              Alongamento

  Compressão                          Encurtamento

  Força cortante                      Sua curva é integrada para obter o
                                      momento fletor

  Curvas de esforços                  Representam esforços globais ao
                                      longo da viga-navio
  -----------------------------------------------------------------------

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Inverter a relação entre força cortante
> e momento fletor. - Dizer que o momento fletor é obtido pela
> integração da própria curva de momento. - Trocar a convenção positiva
> apresentada no trecho. - Esquecer que sociedades classificadoras,
> obedecendo às regras da IMO, impõem limites aos esforços no casco de
> cada embarcação.

------------------------------------------------------------------------

# BLOCO 4 --- TÓPICO 14: ESTABILIDADE DINÂMICA

## 4.1. Estabilidade estática e estabilidade dinâmica

### A. Entenda a ideia

Imagine que uma força externa incline um navio. Para avaliar seu
comportamento, existem duas perguntas diferentes:

1.  **Naquele ângulo, qual é a capacidade de retorno indicada pelo braço
    de endireitamento?**
2.  **Quanto trabalho ou energia está envolvido durante o movimento
    entre o ângulo inicial e o ângulo considerado?**

A primeira pergunta está ligada à estabilidade estática. A segunda está
ligada à estabilidade dinâmica.

A estabilidade estática observa a condição em um ângulo. A estabilidade
dinâmica considera o trabalho realizado durante o movimento.

### B. Visualize a diferença

``` mermaid
flowchart TD
    A["Navio inclinado por ação externa"] --> B["Estabilidade estática"]
    A --> C["Estabilidade dinâmica"]
    B --> D["Analisa o momento em um ângulo"]
    B --> E["Associada ao valor de GZ"]
    C --> F["Analisa trabalho e energia"]
    C --> G["Associada à área sob a curva GZ"]
```

### C. Quadro comparativo

  -----------------------------------------------------------------------
  Estabilidade estática               Estabilidade dinâmica
  ----------------------------------- -----------------------------------
  Analisa o momento em cada ângulo    Considera o trabalho durante o
                                      movimento

  Associada ao valor de GZ em         Associada à área sob a curva GZ
  determinado ângulo                  

  Não considera a energia acumulada   Envolve trabalho e energia
  no intervalo de movimento           

  Avalia a condição em uma posição    Avalia a reserva energética até
  angular                             determinado ângulo
  -----------------------------------------------------------------------

### D. Definição técnica

> **Estabilidade dinâmica:** medida da capacidade do navio de resistir a
> inclinações e retornar à posição de equilíbrio, considerando o
> trabalho ou energia associado ao movimento. É representada pela área
> sob a curva de braços de endireitamento (GZ) entre o ângulo inicial e
> o ângulo final considerado.

### E. O que precisa memorizar

-   Estática = momento em determinado ângulo.
-   Dinâmica = trabalho e energia durante o movimento.
-   Estática = valor de GZ.
-   Dinâmica = área sob a curva GZ.
-   A estabilidade dinâmica é importante para avaliar a capacidade de
    resistir a grandes inclinações.

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Dizer que estabilidade dinâmica é apenas
> o valor de GZ em um ângulo. - Afirmar que estabilidade estática mede a
> área sob a curva. - Dizer que estabilidade dinâmica não envolve
> energia. - Confundir a área sob a curva com o valor isolado da GM.

------------------------------------------------------------------------

## 4.2. Área sob a curva GZ e reserva de estabilidade dinâmica

### A. Entenda a ideia

A curva GZ relaciona o ângulo de inclinação do navio ao braço de
endireitamento. A área sob essa curva, até determinado ângulo,
representa a reserva de estabilidade dinâmica.

Uma comparação simples: o valor de GZ em um ponto é como observar a
força restauradora em uma posição específica. A área sob a curva é como
considerar o efeito acumulado ao longo de todo o intervalo angular.

Quanto maior a área, maior a reserva de estabilidade dinâmica indicada
para aquele intervalo.

### B. Visualize o conceito

``` mermaid
flowchart TD
    A["Curva GZ"] --> B["Área sob a curva até o ângulo escolhido"]
    B --> C["Trabalho / energia"]
    C --> D["Reserva de estabilidade dinâmica"]
    D --> E["Maior área = maior reserva energética"]
```

### C. Relação apresentada no material

A estabilidade dinâmica para determinado ângulo de banda é determinada
pelo produto da área sob a curva de estabilidade, até o ângulo desejado,
pelo deslocamento.

$$E_D = \Delta \cdot A$$

Onde:

-   $E_D$ = estabilidade dinâmica;
-   $\Delta$ = deslocamento do navio;
-   $A$ = área sob a curva GZ até o ângulo considerado.

### D. Como calcular a área

O material indica que a área sob a curva GZ pode ser calculada:

-   Pela fórmula dos trapézios;
-   Pelas regras de Simpson.

Não é necessário desenhar a curva para realizar esse cálculo, desde que
se disponha dos dados necessários.

### E. O que precisa memorizar

-   Área sob GZ = trabalho/energia por unidade de deslocamento angular,
    conforme a representação do material.
-   Estabilidade dinâmica = área × deslocamento.
-   Maior área = maior reserva de estabilidade dinâmica.
-   A área pode ser calculada pelos trapézios ou pelas regras de
    Simpson.
-   Não é obrigatório desenhar a curva para calcular a área.

### F. Atenção para a prova

> \[!WARNING\] **Pegadinhas** - Dizer que a estabilidade dinâmica é
> apenas a área, sem considerar o deslocamento, quando a questão pede a
> grandeza indicada no material. - Afirmar que é obrigatório desenhar a
> curva. - Dizer que uma área menor representa maior reserva de
> estabilidade. - Confundir área sob GZ com o valor de GZ em um único
> ângulo.

------------------------------------------------------------------------

## 4.3. Conversão de graus para radianos

### A. Entenda a ideia

As regras de Simpson trabalham com os intervalos angulares em radianos
no cálculo da área sob a curva de estabilidade. Portanto, quando os
ângulos estão em graus, é necessário convertê-los.

### B. Regra apresentada

Para converter graus em radianos, o material orienta dividir o número de
graus por **57,3**.

$$\theta_{rad} = \frac{\theta_{graus}}{57,3}$$

### C. O que precisa memorizar

-   Ângulos dos intervalos comuns devem estar em radianos para o cálculo
    pelas regras de Simpson.
-   Conversão indicada: dividir por 57,3.

### D. Atenção para a prova

> \[!WARNING\] **Pegadinha numérica** Não multiplique por 57,3. Para
> converter graus em radianos, divide-se por 57,3.

------------------------------------------------------------------------

## 4.4. GM alta não garante boa estabilidade dinâmica

### A. Entenda a ideia

A altura metacêntrica GM é um indicador importante da estabilidade
inicial do navio. Porém, ela não conta toda a história.

Imagine dois navios com GM inicial elevada. Isso, por si só, não garante
que ambos tenham uma grande área sob a curva GZ. Um deles pode
apresentar uma curva cuja área seja pequena, indicando pouca energia
disponível para resistir a grandes inclinações.

Por isso, é necessário analisar tanto a GM inicial quanto a área sob a
curva GZ.

### B. Visualize a relação

``` mermaid
flowchart TD
    A["GM inicial elevada"] --> B["Indica estabilidade inicial"]
    B --> C["Não garante, isoladamente, boa estabilidade dinâmica"]
    C --> D["Analisar a área sob a curva GZ"]
    D --> E["Avaliar a reserva de estabilidade dinâmica"]
```

### C. Definição técnica

> A altura metacêntrica inicial é um indicador da estabilidade inicial,
> mas não garante, isoladamente, boa estabilidade dinâmica. Um navio
> pode apresentar GM elevada e uma curva GZ com área pequena, dispondo
> de pouca energia para resistir a grandes adernamentos.

### D. O que precisa memorizar

-   GM alta não garante boa estabilidade dinâmica.
-   A GM é um indicador da estabilidade inicial.
-   A área sob GZ deve ser analisada.
-   Os critérios da IMO devem ser atendidos em todas as condições de
    carregamento, conforme o material.

### E. Atenção para a prova

> \[!WARNING\] **Pegadinha clássica** A afirmação "um navio com GM alta
> sempre possui grande estabilidade dinâmica" é falsa.

------------------------------------------------------------------------

## 4.5. Critérios de estabilidade e IMO

### A. Entenda a ideia

Os critérios de estabilidade estabelecem valores mínimos aceitáveis para
que o navio tenha condições de segurança. No contexto da estabilidade
dinâmica, eles procuram garantir que a embarcação tenha energia
suficiente para resistir e se recuperar de inclinações provocadas por
forças externas.

O material relaciona esses critérios à IMO e ao Código de Estabilidade
Intacta (IS Code).

### B. Definição técnica

> **Critério de estabilidade:** conjunto de valores mínimos aceitáveis
> que asseguram a estabilidade do navio nas condições consideradas. Os
> critérios da IMO representam requisitos mínimos de estabilidade
> intacta.

### C. O que precisa memorizar

-   Os critérios são definidos pela IMO.
-   Fazem parte dos requisitos mínimos de estabilidade intacta.
-   Estão relacionados ao Código de Estabilidade Intacta (IS Code).
-   Devem ser cumpridos em todas as condições de carregamento, conforme
    o trecho selecionado.
-   Visam assegurar energia suficiente para resistir e recuperar-se de
    inclinações provocadas por forças externas.

### D. Como os critérios foram fundamentados

O arquivo selecionado menciona estudos de:

-   Navios que naufragaram devido à distribuição incorreta da carga;
-   Tanques de prova;
-   Levantamentos estatísticos;
-   Experiência dos construtores de navios.

Também cita situações extraordinárias, como alagamento de compartimento
e encalhe, que não fazem parte do estudo específico apresentado no
trecho sobre estabilidade dinâmica.

### E. Atenção para a prova

> \[!WARNING\] **Limite deste arquivo** O trecho selecionado explica o
> conceito e a finalidade dos critérios, mas não apresenta a tabela
> completa de valores numéricos da IMO. Não memorize números de limites
> com base apenas neste arquivo: consulte a apostila integral do Tópico
> 14 para estudar áreas mínimas, ângulos e valores de GM/GZ.

------------------------------------------------------------------------

# BLOCO 5 --- REVISÃO GERAL PARA A PROVA

## 5.1. Quadro de memorização rápida

  -----------------------------------------------------------------------
  Tópico                  Conceito                Regra essencial
  ----------------------- ----------------------- -----------------------
  7                       Marcas de calado        Em águas parelhas, não
                                                  há erro de defasagem
                                                  por estarem fora das
                                                  perpendiculares

  7                       Deflexão negativa       Alquebrado

  7                       Deflexão positiva       Contra-alquebrado

  7                       Contra-alquebrado       Correção aditiva

  7                       Calado correspondente   Corrigido para
                                                  perpendiculares,
                                                  compasso e deflexão

  8                       Tolerância              0,2% da carga
                                                  movimentada, tomando o
                                                  maior valor

  8                       Operação                Continuada, de uma só
                                                  vez

  8                       Trim nas marcas         Ré menos vante

  8                       Densidade               Três amostras: proa,
                                                  meio-navio e ré

  8                       Densidade real          Média das três leituras

  8                       Consumíveis             Óleo combustível,
                                                  diesel, lubrificante,
                                                  água de lastro, doce e
                                                  destilada

  8                       2ª correção de trim     Aplicada quando trim \>
                                                  1% do Lpp

  13                      Navio                   Viga flutuante

  13                      Esforços transversais   Balanços e movimentos
                                                  oscilatórios

  13                      Resistência transversal Cavername e vaus

  13                      Sloshing                Oscilação violenta em
                                                  tanque parcialmente
                                                  cheio

  13                      Esforços                Transversais menos
                                                  significativos que
                                                  longitudinais

  13                      Onda crítica descrita   Comprimento igual ao
                                                  comprimento do navio

  13                      Curvas de Bonjean       Áreas das seções
                                                  transversais

  13                      Momento fletor          Curva obtida pela
                                                  integração da força
                                                  cortante

  13                      Momento positivo no     Tração embaixo e
                          trecho                  compressão em cima

  14                      Estabilidade estática   Momento em determinado
                                                  ângulo

  14                      Estabilidade dinâmica   Trabalho/energia

  14                      Reserva dinâmica        Área sob a curva GZ

  14                      Estabilidade dinâmica   Área × deslocamento

  14                      Graus para radianos     Dividir por 57,3

  14                      GM alta                 Não garante boa
                                                  estabilidade dinâmica

  14                      Critérios               IMO / IS Code
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 5.2. Pegadinhas que merecem revisão

1.  **Tópico 7:** trocar deflexão negativa por positiva.
2.  **Tópico 7:** afirmar que o contra-alquebramento exige correção
    subtrativa.
3.  **Tópico 7:** esquecer uma das três correções do calado
    correspondente.
4.  **Tópico 8:** trocar 0,2% por 2%.
5.  **Tópico 8:** calcular a tolerância sem considerar o maior valor.
6.  **Tópico 8:** inverter ré menos vante.
7.  **Tópico 8:** afirmar que uma única amostra basta para determinar a
    densidade real.
8.  **Tópico 8:** confundir constante do navio com consumíveis.
9.  **Tópico 8:** colocar a correção de trim diretamente no calado de
    entrada das tabelas.
10. **Tópico 13:** afirmar que os esforços transversais são mais
    significativos que os longitudinais.
11. **Tópico 13:** dizer que sloshing ocorre em tanque completamente
    cheio.
12. **Tópico 13:** inverter tração e compressão no alquebramento.
13. **Tópico 13:** inverter a relação entre força cortante e momento
    fletor.
14. **Tópico 13:** trocar o sinal da convenção de momento fletor
    positivo.
15. **Tópico 14:** confundir GZ com a área sob a curva GZ.
16. **Tópico 14:** afirmar que GM alta garante grande estabilidade
    dinâmica.
17. **Tópico 14:** multiplicar por 57,3 em vez de dividir.
18. **Tópico 14:** esquecer que a estabilidade dinâmica é área
    multiplicada pelo deslocamento.

------------------------------------------------------------------------

## 5.3. Autoavaliação: sei explicar sem olhar?

Use esta lista para verificar se você realmente entendeu os quatro
tópicos.

-   [ ] Consigo explicar por que as marcas de calado fora das
    perpendiculares podem gerar erro quando o navio está compassado.
-   [ ] Sei diferenciar alquebrado e contra-alquebrado pelo sinal da
    deflexão.
-   [ ] Sei definir calado correspondente.
-   [ ] Sei explicar o objetivo do Draft Survey.
-   [ ] Sei reproduzir as sete etapas na ordem.
-   [ ] Sei explicar a tolerância de 0,2%.
-   [ ] Sei informar como e onde são coletadas as três amostras de
    densidade.
-   [ ] Sei diferenciar constante do navio e consumíveis.
-   [ ] Sei explicar a relação entre distribuição de peso, empuxo e
    deformação.
-   [ ] Sei diferenciar tração e compressão.
-   [ ] Sei explicar esforços transversais e sloshing.
-   [ ] Sei explicar a função das curvas de Bonjean.
-   [ ] Sei relacionar força cortante e momento fletor.
-   [ ] Sei diferenciar estabilidade estática e dinâmica.
-   [ ] Sei explicar por que a área sob GZ representa reserva de
    estabilidade dinâmica.
-   [ ] Sei converter graus em radianos dividindo por 57,3.
-   [ ] Sei explicar por que GM alta não garante boa estabilidade
    dinâmica.
-   [ ] Sei explicar a finalidade dos critérios da IMO.

------------------------------------------------------------------------

## 5.4. Fontes e limites deste guia

Este guia foi elaborado com base nos quatro arquivos de trechos
selecionados:

-   `tópico-7-est2-p2.txt`
-   `tópico-8-est2-p2.txt`
-   `tópico-13-est2-p2.txt`
-   `tópico-14-est2-p2.txt`

> \[!NOTE\] **Importante** Este material organiza e explica os trechos
> selecionados. Ele não substitui as apostilas completas. Em especial:
>
> -   No Tópico 8, consulte a apostila integral para a composição
>     detalhada da constante do navio e outros procedimentos.
> -   No Tópico 13, consulte a apostila integral para aprofundar os
>     métodos de cálculo de força cortante e momento fletor.
> -   No Tópico 14, consulte a apostila integral para os valores
>     numéricos dos critérios da IMO.
>
> Quando houver diferença entre uma explicação intuitiva e a formulação
> técnica da apostila, utilize a terminologia e a convenção do professor
> para responder à prova.
