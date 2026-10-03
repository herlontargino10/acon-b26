# MATERIAL DIDÁTICO — 02 MARÉ

## 1. Teoria das Marés

### 1.1 O que é Maré?
**Em termos simples:** É a oscilação periódica do nível do mar, causada principalmente pela atração gravitacional da Lua e do Sol, associada à rotação da Terra.
- **Movimento Periódico:** Repete-se em intervalos regulares e pode ser decomposto em componentes harmônicas.
- **Variação Diária:** Alternância entre preamares e baixa-mares.
- **Ciclo Sizígia-Quadratura:** Variação aproximadamente quinzenal da amplitude das marés.

**Figura 1: Sistema Terra-Lua e Ciclo de Maré**
- **O que mostra:** Um diagrama da Terra e da Lua, com o invólucro de água deformado (maré) e um gráfico de linha do Nível do mar x Tempo.
- **Como interpretar:** O diagrama espacial demonstra como a água acompanha a direção lunar. O gráfico temporal demonstra o ciclo completo de subida e descida da água.
- **O que observar:** O gráfico exibe Preamar, Baixa-mar, Amplitude e o Ciclo quinzenal de Sizígia-Quadratura.
- **Relação com o texto:** Ilustra simultaneamente os três conceitos básicos: oscilação, movimento periódico e ciclo quinzenal.

### 1.2 Fatores Causadores das Marés
A maré é gerada pelo equilíbrio entre duas forças fundamentais:
1. **Atração Gravitacional:** Lua e Sol atraem a Terra e seus oceanos. 
2. **Força Centrífuga:** A força de um corpo em trajetória circular (no sentido do centro para fora, proporcional à velocidade).

**Relação causa $\rightarrow$ processo $\rightarrow$ consequência:**
A diferença entre a força de atração gravitacional e a força centrífuga gera a **Força Geradora de Maré**.

#### Equações Associadas
**Fórmula 1: Atração Gravitacional**
- **O que a fórmula representa:** A atração gravitacional direta de astros sobre a Terra.
- **Para que é usada:** Explicar a base da atração que puxa os oceanos.
- **Significado das variáveis:** $F$ = Força; $G$ = Constante gravitacional; $M, m$ = massas; $r$ = distância.
- **Fórmula:** $F = G \frac{(Mm)}{r^2}$
- **Observação da fonte:** A gravidade é proporcional a $1/r^2$.

**Fórmula 2: Força Geradora de Maré (Conceitual)**
- **O que a fórmula representa:** A resultante das forças envolvidas na maré.
- **Fórmula:** FORÇA GERADORA DE MARÉ = ATRAÇÃO GRAVITACIONAL + FORÇA CENTRÍFUGA
- **Observação da fonte:** A intensidade da força geradora é uma força diferencial e varia aproximadamente com o inverso do cubo da distância ($1/d^3$).

#### A Regra do Inverso do Cubo: Por que a Lua domina?
**Tabela 1: Comparação Lua x Sol**
- **O que a tabela mostra:** Massa, Distância média e a Força de maré relativa dos dois astros.
- **Como ler:** Comparar as linhas: a Lua representa 100% da força de referência, enquanto o Sol representa $\approx$ 46%.
- **O que observar:** Embora o Sol tenha massa imensamente maior, sua distância também é enorme. Como a força de maré decai com o cubo da distância ($1/d^3$), a Lua governa a maior parte das marés.
- **Relação com o texto:** Sustenta que a Lua é responsável por $\approx$ 70% das marés, e o Sol por $\approx$ 30%.

### 1.3 Ciclos Lunares e Amplitudes
A posição dos astros define a magnitude da maré:
- **Maré de Sizígia — Marés Vivas:** Ocorrem durante a Lua nova e Lua cheia. O Sol, a Terra e a Lua estão alinhados, somando forças.
- **Maré de Quadratura — Marés Mortas:** Ocorrem no Quarto crescente e Quarto minguante. O alinhamento forma um ângulo de 90°.

**Gráfico 1: Variação Esqumática x Fases da Lua**
- **O que o gráfico mostra:** A envoltória das ondas de maré variando de altura em um mês. Eixo horizontal corresponde aos dias/fases da lua; eixo vertical sem escala numérica representa a altura.
- **Como interpretar:** O desenho da onda "incha" e "desincha" ao longo do mês.
- **O que observar:** As marés com a maior amplitude (picos mais altos e fundos mais baixos) batem perfeitamente com a Lua Cheia e Lua Nova. A menor variação coincide com o Quarto Crescente e Minguante.
- **Relação com o texto:** Visualização do ciclo de Sizígia (marés vivas) e Quadratura (marés mortas).

### 1.4 Tipos de Maré
A classificação ocorre conforme o número de preamares e baixa-mares ocorridos em um **dia lunar** ($\approx$ 24h50min).
- **Maré Diurna:** 1 preamar e 1 baixa-mar por dia lunar.
- **Maré Semidiurna:** 2 preamares e 2 baixa-mares por dia lunar.
- **Maré Mista:** 2 preamares e 2 baixa-mares, com forte desigualdade de alturas.

**Gráfico 2: Curvas de Tipos de Maré**
- **O que os gráficos mostram:** Três subgráficos de Nível do Mar x Tempo em um período de pouco mais de 24 horas.
- **Como interpretar:** Contar quantos picos (PM) e vales (BM) ocorrem dentro do ciclo demonstrado.
- **O que observar:** A maré mista possui preamares visivelmente diferentes em tamanho num mesmo dia.
- **Relação com o texto:** Validação visual da classificação técnica de cada maré.

### 1.5 Principais Componentes de Maré e Critério de Courtier
A maré real não é simples, é a soma de dezenas de componentes astronômicos.
**Em termos simples:** Constituintes harmônicos são parcelas matemáticas isoladas da atração celeste.

**Tabela 2: Principais Componentes Constituintes**
- **Para que serve:** Apresentar a nomenclatura e o período das influências orbitais adaptadas de Pugh (2004).
- **Como ler:** Listagem de sigla (M2, S2, K1, etc.) com seu respectivo tempo em horas.
- **O que observar:** Existem componentes Semidiurnas, Diurnas e de Longo Período. A **M2** (Lunar Principal) é o constituinte mais forte e fundamental do sistema.
- **Relação com o texto:** A base de dados que a Tábua de Marés usará posteriormente.

**Fórmula 3: Critério de Courtier**
- **O que a fórmula representa:** O índice para classificar o tipo físico da maré.
- **Para que é usada:** Definir matematicamente se a maré é diurna, mista ou semidiurna.
- **Significado das variáveis:** Usa apenas as 4 componentes principais mais cobradas: K1, O1 (diurnas) e M2, S2 (semidiurnas).
- **Fórmula:** $F = \frac{K_1 + O_1}{M_2 + S_2}$

**Tabela 3: Classificação de Courtier**
- **Como ler:** Pega-se o valor $F$ calculado.
  - $F < 0,25 \rightarrow$ maré SEMIDIURNA
  - $0,25 \le F < 1,5 \rightarrow$ maré MISTA SEMIDIURNA
  - $1,5 \le F < 3,0 \rightarrow$ maré MISTA DIURNA
  - $F \ge 3,0 \rightarrow$ maré DIURNA

### 1.6 Classificação por Altura e Importância Costeira
O conhecimento da altura máxima (Hmáx) classifica as áreas costeiras e é essencial à navegação.

**Tabela 4: Classificação de Maré por Altura**
- **Como ler e o que observar:**
  - **Micromaré:** Hmáx < 2 m
  - **Mesomaré:** 2 m $\le$ Hmáx < 4 m
  - **Macromaré:** 4 m $\le$ Hmáx < 6 m
  - **Hipermaré:** Hmáx $\ge$ 6 m

**Importância:** Produtividade de ecossistemas, gestão costeira, mistura de massas de água, navegação, e geração de energia (maremotrizes).

### 1.7 Maré Meteorológica e Riscos
**Riscos principais:** Encalhe, correntes de maré fortes, janela de tempo restrita, redução da manobrabilidade, sobrecarga de estruturas.

**Relação causa $\rightarrow$ processo $\rightarrow$ consequência:**
Ventos fortes + Baixa Pressão Atmosférica $\rightarrow$ elevação anormal da água (sobrelevação) $\rightarrow$ Maré Meteorológica Positiva.
Ventos específicos + Alta Pressão $\rightarrow$ afastamento da água (depressão) $\rightarrow$ Maré Meteorológica Negativa.

> [!warning] Inconsistência da fonte
> **O que aparece:** Dois mapas da costa sul do Brasil indicando "Maré meteorológica positiva (HS)" e "negativa (HS)", com vetores "FC e Ekman" e áreas "BP" e "AP".
> **Inconsistência/Problema:** As legendas para as siglas "HS" e "FC" não são traduzidas em texto explícito no material, o que gera ambiguidade (presume-se Hemisfério Sul e Força de Coriolis, mas a leitura autônoma pelo aluno exige dedução).

### Em resumo — Bloco 1
- Marés originam-se pela interação da Força Gravitacional (Lua e Sol) com a Força Centrífuga.
- A Lua manda em 70% da maré devido à proximidade (Regra do Inverso do Cubo, $1/d^3$).
- Fases novas e cheias geram marés vivas (Sizígia); quartos crescentes/minguantes geram marés mortas (Quadratura).
- Existem marés diurnas, semidiurnas e mistas, categorizadas pelo Critério de Courtier.
- Fatores meteorológicos alteram a previsão astronômica da maré.

---

## 2. Elementos e Características das Curvas de Marés

### 2.1 O que são Curvas de Maré
**Em termos simples:** São as representações gráficas que demonstram a variação do nível da água subindo e descendo com o tempo. Identificam os instantes exatos de subida (enchente) e descida (vazante).

**Gráfico 3: Curva de Maré Mensal**
- **O que mostra:** Oscilação real do nível (Eixo Y de elevação em m, de -0.8 a 0.8) ao longo de um mês (Eixo X de 0 a 30 dias).
- **Como interpretar:** Demonstra visualmente que a amplitude da maré sofre variações gradativas constantes, englobando as fases da lua durante os 30 dias.

### 2.2 Os Elementos Formadores
**Em termos simples:** A onda de maré possui "nomes técnicos" para cada pedaço geométrico de seu formato.

**Fórmulas 4 a 6: Elementos da Curva**
- **Preamar (PM):** O pico ou nível máximo da maré cheia.
- **Baixa-mar (BM):** O vale ou nível mínimo da maré vazante.
- **Amplitude da Maré (A):** Diferença geométrica total entre Preamar e Baixa-mar.
  - **Fórmula:** $A = PM - BM$
- **Nível Médio (NM):** Ponto exato da metade geométrica entre PM e BM.
  - **Fórmula:** $NM = \frac{PM + BM}{2}$
- **Altura da Maré (h):** Distância vertical entre a água no instante analisado e a linha de referência da marinha (NR).
  - **Fórmula:** $h = \text{nível instantâneo} - NR$
- **Nível de Redução (NR ou ZH):** O "chão cartográfico". Referência oficial zero para as medições. É a média das baixa-mares de sizígia.
- **Ciclo:** O tempo gasto de uma preamar até a preamar seguinte.

**Gráfico 4: Elementos das Curvas de Maré (Diagrama Explicativo)**
- **O que mostra:** Onda senoidal simplificada com todas as variáveis apontadas.
- **Como interpretar:** Observa-se que a linha do NR fica abaixo da BM, e o NM corta a onda na metade. A Amplitude é uma seta inteira que cobre de BM a PM.

### 2.3 Exemplo Introdutório dos Elementos
#### Situação
Demonstrar a aplicação básica das definições geométricas em uma curva.
#### Dados
$PM = 10$ m e $BM = 5$ m.
#### O que o exemplo demonstra
A fonte não elabora os cálculos matemáticos passo a passo, mas utiliza blocos e setas para comprovar visualmente que o cálculo do Nível Médio resulta no eixo mediano e a Amplitude indica a variação total entre 10 e 5 metros, treinando a fixação da fórmula.

### 2.4 Relação Barco x Fundo do Mar
Para não encalhar o navio, é fundamental associar a maré ao fundo do mar.
- **Sondagem (profundidade cartografada):** A distância vertical registrada na carta náutica, que vai do Nível de Redução (NR) até a rocha/areia do fundo.

**Fórmula 7: Profundidade Real**
- **O que a fórmula representa:** A quantidade real de água sob o navio no mundo real.
- **Para que é usada:** Para segurança da navegação e evitar colisão.
- **Fórmula:** Profundidade real = Sondagem + Altura da maré

**Diagrama 1: Superfície da Água, Carta e Fundo**
- **O que o diagrama mostra:** Um navio na água, com a altura da maré somando-se à sondagem.
- **O que observar:** A carta náutica sempre assume o pior cenário hídrico, chamado de **Zero Hidrográfico**. Isso significa que a sondagem na carta já prevê o nível no NR.
- **Como interpretar:** Exemplo visual do diagrama: se a Carta diz que o fundo é 11,5 m (Sondagem) e a Maré naquele momento adicionou +0,5 m (Altura da Maré), a Profundidade Real que o barco tem disponível é 12,0 m.

### Em resumo — Bloco 2
- PM = topo máximo; BM = vale mínimo.
- Nível de Redução (NR) e Zero Hidrográfico (ZH) são o mesmo referencial seguro.
- A carta náutica traz a profundidade do pior cenário (Sondagem); para navegar deve-se somar a Altura da maré daquele momento.

---

## 3. Tábua de Marés (TM)

### 3.1 O que é a Tábua de Marés?
**Em termos simples:** É a "agenda oficial" anual da Marinha para os portos, que divulga de antemão os horários exatos das preamares e baixa-mares e suas alturas para cada dia do ano.
Ela nasce da medição de dados históricos do mar (Marégrafo) combinada à modelagem dos constituintes harmônicos daquela região costeira.

### 3.2 Equação de Previsão da Maré
**Fórmula 8: Equação da Previsão da Maré**
- **O que a fórmula representa:** A complexa soma de todas as oscilações astronômicas para calcular o nível futuro da água.
- **Para que é usada:** Para produzir os números listados na Tábua de Marés oficial.
- **Significado das variáveis:**
  - $\eta(t)$: Elevação (altura) prevista no instante t (metros).
  - $Z_0$: Nível médio do mar local.
  - $H_j$: Amplitude média daquela constituinte específica.
  - $\sigma_j$: Velocidade angular da constituinte.
  - $t$: Tempo percorrido.
  - $g_j$: Fase (época).
- **Fórmula:** $\eta(t) = Z_0 + \sum_j H_j \cos(\sigma_j t + g_j)$

### 3.3 Interpretando a Tábua de Marés
**Tabela 5: Recortes Oficiais da Tábua**
- **Para que serve:** Ensinar o aluno a ler o material da Marinha (Exemplos do Rio de Janeiro e Antártica).
- **Como ler:** 
  - O documento é dividido em 2 grandes blocos horizontais por mês (dias de 1-15 e de 16-31).
  - Na linha do dia (ex: 01, QUA), verificam-se as colunas de "HORA" e "ALT (m)".
  - A tábua traz apenas os instantes de "virada" da maré (só mostra as PMs e BMs).
- **O que observar:** O cabeçalho possui o Porto, Latitude/Longitude, Fuso Horário associado e símbolos das Fases da Lua ao lado de datas cruciais.

### Em resumo — Bloco 3
- Tábua de Marés predetermina as PM e BM de portos cruciais.
- É feita modelando as influências orbitais (constituintes harmônicos) através de uma equação de previsão somatória de cossenos.
- Lê-se buscando o dia do mês e anotando as horas de inversão de maré com as alturas.

---

## 4. Determinação da Altura da Maré em um Dado Instante

### 4.1 Ideia Principal
Como a Tábua de Marés só mostra o "teto" e o "fundo" (PM e BM), o navegador precisa de cálculos matemáticos para descobrir qual é a altura d'água num **horário intermediário**.

**Passos Iniciais Obrigatórios:**
1. Encontrar o **horário desejado**.
2. Procurar na Tábua a **preamar imediatamente anterior** e a **baixa-mar seguinte** (ou vice-versa).
3. Calcular o **Intervalo de maré (T):** O tempo total transcorrido entre a PM e a BM.
4. Calcular a **Variação total da maré ($\Delta H$):** O tamanho total da "queda" ou "subida", sendo $\Delta H = H_{PM} - H_{BM}$.

### 4.2 Exemplo e Estudo de Caso Resolvido
#### Situação
"Vou sair do porto de SL às 10 h e quero saber qual a altura de maré neste momento."

> [!warning] Inconsistência da fonte
> **O que aparece:** O enunciado fala de "porto de SL". O trecho da tábua recortado em vermelho mostra o dia 01 de Julho com PM às 07h34 (5,45m) e BM às 13h57 (0,85m).
> **Inconsistência/Problema:** Essa tabela utilizada para o exercício não é o Porto do Rio de Janeiro nem a Estação Antártica, previamente explicadas no material. A sigla "SL" não é clarificada. O estudante deve focar apenas em extrair os números do recorte, ignorando a inconsistência geográfica das tábuas modelo para fins de treinamento.

#### Dados da Tábua para o dia 01:
- Preamar anterior: 07h34, com Altura = 5,45 m.
- Baixa-mar seguinte: 13h57, com Altura = 0,85 m.
- Horário desejado: 10h00.

#### Cálculos Iniciais (Intervalo e Variação)
- **T** = 13h57 - 07h34 = **6h23min**
- **$\Delta H$** = 5,45 - 0,85 = **4,60 m**

### 4.3 Método 1: A Regra dos 12 Avos
**Em termos simples:** A maré não sobe e desce em velocidade constante; a velocidade é menor perto dos picos e maior no meio. A regra divide o processo em 6 frações progressivas para simplificar o cálculo curvo.
> **Condição da Regra:** Ela pressupõe um intervalo aproximado de 6 horas entre a PM e a BM.

**Tabela 6: Divisão da Regra dos 12 Avos**
- **Para que serve:** Tabelar os pesos de cada hora.
- **Fração por Hora:**
  - 1ª hora: 1/12 da Variação Total
  - 2ª hora: 2/12 da Variação Total
  - 3ª hora: 3/12 da Variação Total
  - 4ª hora: 3/12 da Variação Total
  - 5ª hora: 2/12 da Variação Total
  - 6ª hora: 1/12 da Variação Total

#### Procedimento Passo a Passo
**O que se procura:** Altura da maré exatamente às 10h00.
1. Contabilizar o tempo percorrido desde a PM: De 07h34 até 10h00 são **2 horas e 26 minutos**.
2. Arredondamento da fonte para facilitar a regra horária: A fonte aplica o tempo como compreendendo as **duas primeiras horas completas**.
3. Somar as frações dessas duas horas: $1/12$ (da 1ª hora) + $2/12$ (da 2ª hora) = **$3/12$**.
4. Multiplicar pela Variação Total $\Delta H$: 
   **Cálculo:** $\frac{3}{12} \times \Delta H \rightarrow \frac{3}{12} \times 4,60 = \mathbf{1,15 m}$
5. Como a maré está vazando (saindo da Preamar em direção à Baixa-mar), o nível está descendo. Logo, **subtraímos** a variação da altura original da PM.
   **Cálculo Final:** Altura = 5,45 m - 1,15 m = **4,30 m**.
#### Resultado
Às 10h00, a altura será de **4,30 m**.

### 4.4 Método 2: Interpolação Gráfica
É a obtenção do mesmo resultado traçando o ponto fisicamente em uma curva de maré desenhada.

**Gráfico 5: Gráfico de Interpolação**
- **O que mostra:** Uma curva de maré completa e sinuosa conectando os pontos PM (07h34 | 5,45m) e BM (13h57 | 0,85m).
- **Como utilizar no procedimento:** O usuário busca no eixo do tempo inferior a marca de 10h00. Sobe-se uma linha pontilhada perfeitamente reta até encostar na onda azul. Dali, puxa-se uma linha reta horizontal para o eixo Y de Altura, para efetuar a leitura visual da altura.
- **Resultado demonstrado:** A linha atinge exatamente **4,30 m**, chancelando e validando os cálculos da Regra dos 12 Avos da seção anterior.

### Em resumo — Bloco 4
- Para saber o nível em hora quebrada, usa-se Regra dos 12 Avos ou Interpolação Gráfica.
- Precisa calcular $\Delta H$ (Variação de altura) e extrair os dados da tábua.
- A Regra dos 12 Avos exige somar a fração correspondente às horas transcorridas e multiplicar pelo $\Delta H$. Depois, soma ou subtrai da altura de referência dependendo se for enchente ou vazante.

---

## 5. Método Expedito de Previsão e Estabelecimento do Porto (EP)

### 5.1 Culminação da Lua
**O que é:** Culminação ou Passagem Meridiana é o momento do dia em que a Lua cruza a linha imaginária do meridiano do observador, alcançando a sua maior elevação no céu.
- **O que o diagrama demonstra (Movimento Aparente):** Mostra um observador em terra enxergando a lua nascer a Leste, culminar sobre sua cabeça, e se pôr a Oeste. 

**Relação com a Maré e a "Analogia do Ônibus":**
A preamar **não ocorre exatamente na mesma hora** da culminação lunar. A água do mar possui inércia e sofre resistências dos fundos marinhos, demorando para formar o monte da preamar na praia. O professor usa a analogia do ônibus (que tem tempo de trânsito para chegar e encontrar o colega) para justificar o atraso natural da maré.

### 5.2 Almanaque Náutico
Para saber a hora que a lua culmina, a Marinha elabora tabelas próprias chamadas "Almanaque Náutico".

**Tabela 7: Almanaque Náutico**
- **Para que serve:** Encontrar as informações precisas do trânsito astronômico da Lua para uso neste método.
- **Como ler:** Busca-se a data na coluna "Data / Dia", identifica-se o bloco da "LUA", e encontra-se o horário da subcoluna "Passagem Meridiana".
- **Aplicação no exemplo:** Para o dia 15 (Terça-feira), o material aponta que a Passagem Meridiana (Culminação) da Lua será às **15h41**.

### 5.3 O Estabelecimento do Porto (EP)
**Em termos simples:** O Estabelecimento do Porto é um "atraso tabelado constante" que cada porto possui em relação à passagem da Lua.

**Fórmula 9: Estabelecimento do Porto**
- **O que a fórmula representa:** O intervalo temporal fixo e padronizado do local.
- **Para que é usada:** Em dias de previsão rápida ou se a Tábua de Marés não estiver disponível, para achar a PM através dos astros.
- **Fórmula de Definição:** $EP = PM - \text{Culminação da Lua}$

**Tabela 8: Tabela de Estabelecimento do Porto (EP)**
- **Como ler:** Tabela com nome de Portos Brasileiros (Belém, Fortaleza, RJ, Santos, etc.) e sua respectiva constante.
- **Exemplos de valores:** Rio de Janeiro (EP = 5 h 01); Rio Grande (EP = 4 h 28).

**Sequência de Aplicação (O Método Expedito):**
Se você está sem tábuas de marés, o método orienta:
1. Olhe o Almanaque Náutico e anote a Culminação da Lua.
2. Olhe a tabela de Estabelecimento do Porto da sua cidade e anote o atraso (EP).
3. Some a Culminação com o EP, e o resultado será, grosso modo, a hora que a próxima Preamar chegará naquele dia.

### Em resumo — Bloco 5
- A água da maré sofre atraso em relação à passagem do astro principal. Esse tempo de atraso entre a passagem da Lua e a Enchente máxima se chama Estabelecimento do Porto (EP).
- Pega-se a Passagem Meridiana no Almanaque Náutico e soma-se o EP tabelado do porto para prever rapidamente o horário da preamar.
