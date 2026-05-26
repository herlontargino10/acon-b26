# NAV51 — Navegação Estimada e Costeira

> **Professor:** Franco | **Data:** 30/04/2026 | **Disciplina:** Navegação-1 (NAV51)

> [!important] Informações da Disciplina
> 
> - Haverá **duas provas**: uma no meio do período e outra no final.
> - As provas têm como base as **listas de exercícios**.
> - Resolver todos os exercícios das listas é essencial para aprovação.

---

## 1. Unidades de Medida na Navegação

### 1.1 Milha Náutica (MN ou NM)

**Definição:** Unidade de distância utilizada na navegação náutica e aeronáutica.

**Valor:** `1 MN = 1.852 metros`

> [!note] Como calcular 1 Milha Náutica? A milha náutica é definida como o comprimento de **1 minuto de arco** ao longo de um meridiano terrestre (círculo máximo).
> 
> Como a Terra tem circunferência ~40.000 km e possui 360° × 60' = **21.600 minutos de arco**:
> 
> $$40.000   \div 360 = 111.111  \div 60 \approx 1.852 , m$$
> 
> Portanto: **1 MN = 1.852 m** (por definição internacional desde 1929)

**Interpretação simples:** Imagine dividir o meridiano (que passa pelo polo norte e sul) em 21.600 partes iguais. Cada parte mede exatamente 1 milha náutica.

---

### 1.2 Nó (Knot — kn)

**Definição:** Unidade de velocidade náutica.

**Valor:** `1 nó = 1 milha náutica por hora (MN/h)`

> [!example] Exemplo Prático — Navegação Estimada Se um navio navega a **15 nós** durante **2 horas**:
> 
> $$D = V \times T = 15 , kn \times 2 , h = 30 , MN$$
> 
> Este é o cálculo base da **navegação estimada**: partindo de uma posição conhecida + velocidade + tempo + rumo → estima-se a nova posição.

> [!warning] Pegadinha de Prova
> 
> - **Nó ≠ Milha Náutica.** O nó é uma **taxa (velocidade)**, não uma distância.
> - Dizer _"15 nós por hora"_ é **ERRADO** — já está implícito o "/hora".
> - Correto: _"navegando a 15 nós"_
> - `1 nó = 1 MN/h` | Milha náutica = unidade de **DISTÂNCIA**

---

## 2. Tipos e Métodos de Navegação

A navegação é classificada de acordo com a **distância da costa** e os **recursos disponíveis**.

|Tipo|Faixa|Referência|Características|
|---|---|---|---|
|**Costeira**|3 a 50 NM|Vista da terra|Acidentes naturais e artificiais|
|**Estimada**|Qualquer|Posição anterior|Rumo + velocidade + tempo|
|**Astronômica**|> 50 NM|Estrelas / Astros|Observação celeste, alto mar|
|**Eletrônica**|Qualquer|GPS / Radar / Satélites|Equipamentos eletrônicos|
|**Águas Restritas / Interior**|< 3 NM|Costa / Balizamento|Portos, rios, profundidade média|

---

### 2.1 Navegação Costeira

- **Faixa:** 3 a 50 milhas náuticas da costa
- **Definição:** Navegação realizada mantendo a terra à vista, utilizando acidentes geográficos como referências de posicionamento.

**Características:**

- Realizada com a **vista da terra** (litoral visível ou próximo)
- Utiliza **acidentes naturais**: montanhas, penhascos, cabos, pontas
- Utiliza **acidentes artificiais**: faróis, torres, igrejas, pontes, edifícios marcantes
- O navegante determina a posição por **marcações (bearings)** em dois ou mais pontos

> [!example] Exemplo Prático O navegante observa simultaneamente:
> 
> - O farol do Cabo Frio com marcação de **045°**
> - A torre da cidade com marcação de **090°**
> 
> Traçando essas duas linhas na carta náutica, a **interseção** indica a posição do navio. Quanto mais referências (3+), mais precisa é a posição (**triângulo de erro**).

> [!tip] Observação do Professor O GPS "deu para fora" perto da costa — ou seja, a navegação eletrônica pode ser usada mesmo em navegação costeira para confirmar a posição e determinar a direção (rumo) do navio.

---

### 2.2 Navegação Estimada

- **Faixa:** Qualquer parte da navegação (não restrita por distância)
- **Definição:** Método de determinação de posição a partir de uma posição anterior **conhecida**, utilizando rumo, velocidade e tempo decorrido — sem necessidade de observação externa.

**Características:**

- Pode ser realizada com ou sem vista da terra
- A posição é **determinada em função de outra conhecida** (posição anterior)
- Realizada em **qualquer parte** da navegação
- Depende da precisão dos instrumentos de bordo (agulha, log, cronômetro)

**Fórmula base:**

$$D = V \times T$$

Onde: `D` = distância (MN) | `V` = velocidade (nós) | `T` = tempo (horas)

> [!example] Exemplo do Professor **Situação:** Partiu da posição X (conhecida) às 12h00.
> 
> - Velocidade: **15 nós** | Rumo: **090° (Leste)**
> - Após **2 horas** (14h00):
> 
> $$D = 15 \times 2 = 30 , MN \text{ para Leste}$$
> 
> **Posição Estimada** = P₀ + 30 MN a 090°

> [!warning] Atenção **Correntes marinhas** podem deslocar o navio da posição estimada — aumentando ou diminuindo a velocidade real sobre o fundo. Por isso, é fundamental realizar marcações frequentes para **corrigir a posição**.

> [!important] Lógica da Navegação Estimada O navegante deve registrar a posição periodicamente (a cada 30 min, 1h, etc.) para não acumular erros. Quanto mais tempo sem confirmar a posição, **maior o erro acumulado**.

---

### 2.3 Navegação Astronômica (Celestial)

- **Faixa:** Acima de 50 milhas náuticas da costa
- **Definição:** Método que utiliza a observação de **astros celestes** (estrelas, Sol, Lua, planetas) para determinar a posição do navio.

**Características:**

- Utilizada em **alto mar** (>50 NM)
- Baseia-se na **observação celeste** de estrelas e outros astros
- Instrumento principal: **sextante**
- Requer conhecimento de tabelas náuticas e cálculo de altitude de astros
- Independe de equipamentos eletrônicos (robustez para emergências)

**Interpretação simples:** Quando o navio está longe da costa, não há referências terrestres visíveis. As estrelas se tornam os "marcos de referência" — sua posição no céu é conhecida e permite calcular onde o navio está na Terra.

---

### 2.4 Navegação Eletrônica

- **Definição:** Navegação com auxílio de **equipamentos eletrônicos** para posicionamento e orientação.

**Principais equipamentos:**

- **GPS** (Global Positioning System) — satélites
- **Radar** — detecção de obstáculos e posicionamento por eco
- **AIS** (Automatic Identification System)
- **ECDIS** — cartas eletrônicas
- LORAN / DECCA — sistemas de radionavegação

> [!tip] Nota do Professor O GPS é classificado como navegação eletrônica (também chamada _"canta eletro"_). A navegação eletrônica **complementa**, mas não substitui integralmente os métodos tradicionais. Em caso de falha eletrônica, o navegante deve estar apto a usar navegação estimada e astronômica.

---

### 2.5 Navegação em Águas Restritas / Navegação Interior

- **Faixa:** Menos de 3 milhas náuticas da costa
- **Também chamada:** Navegação em rios e portos / Navegação Interior

**Características:**

- Realizada em **portos** e proximidades de portos
- Considera a **profundidade média** do canal
- Maior risco de encalhe — atenção constante ao calado e à rota
- Uso intensivo de **balizamento** (boias, marcas de canal, faróis)
- Inclui rios, baías, estuários, lagoas — vias interiores

---

## 3. Plano de Referência na Esfera Terrestre

Para determinar a posição de qualquer ponto na superfície terrestre, é necessário um sistema de referência geométrico baseado em **círculos traçados na esfera**.

Existem **três** categorias principais.

---

### 3.1 Círculo Máximo

**Definição:** Círculo traçado na superfície terrestre cujo plano **passa pelo centro da Terra**.

**Características:**

- É o maior círculo possível numa esfera
- Divide a Terra em **dois hemisférios iguais**
- A menor distância entre dois pontos na superfície esférica é sempre um **arco de círculo máximo**
- Todo meridiano é um círculo máximo

**Exemplos de círculos máximos:**

- **Equador** (único paralelo que é também círculo máximo)
- **Todos os meridianos** (e seus antimeridanos)

> [!warning] Pegadinha de Prova
> 
> - O **Equador É** um círculo máximo (seu plano passa pelo centro da Terra).
> - Os **paralelos (exceto o Equador) NÃO** são círculos máximos.
> - **Todos os meridianos SÃO** círculos máximos.

---

### 3.2 Círculo Menor (Paralelo)

**Definição:** Círculo traçado na superfície terrestre cujo plano **NÃO passa pelo centro da Terra**. Corresponde a um corte horizontal que não divide a Terra ao meio.

**Características:**

- São menores que os círculos máximos
- Seu plano é paralelo ao plano do Equador
- NÃO dividem a Terra em partes iguais (exceto o Equador)
- Representam a **latitude** de um ponto
- Ficam menores conforme se afastam do Equador

**Interpretação simples:** Imagine fatiar a Terra como uma laranja em cortes horizontais. Cada "fatia" gera um círculo menor (paralelo). Somente o corte pelo meio (Equador) é círculo máximo.

---

### 3.3 Meridiano

**Definição:** Nome dado ao círculo máximo **vertical** que passa pelos polos Norte e Sul da Terra.

**Características:**

- É um **círculo máximo** (seu plano passa pelo centro da Terra)
- Passa pelo **Polo Norte e pelo Polo Sul**
- Cada meridiano forma um par com seu antimeridano (180° oposto), completando o círculo
- Representam a **longitude** de um ponto
- O **Meridiano de Greenwich (0°)** é o meridiano de referência universal

> [!note] Memorizar — Meridianos vs. Paralelos
> 
> |Característica|Meridiano (Círculo Máximo)|Paralelo (Círculo Menor)|
> |---|---|---|
> |Plano passa pelo centro?|**SIM**|NÃO (exceto Equador)|
> |Direção principal|Vertical (Norte-Sul)|Horizontal (Leste-Oeste)|
> |Passa pelos polos?|**SIM**|NÃO|
> |Grandeza que representa|**Longitude**|**Latitude**|
> |Exemplo|Meridiano de Greenwich (0°)|Trópico de Capricórnio (23,5°S)|
> 
> **EXCEÇÃO CRÍTICA:** O **Equador** é tanto paralelo (0°) quanto **círculo máximo**!

---

## 4. Resumo Ultra-Rápido

- `1 MN = 1.852 m` — comprimento de 1 minuto de arco no meridiano
- `1 nó = 1 MN/h` — velocidade; não confundir com distância
- **GPS** = navegação eletrônica (_"canta eletro"_)
- **Nav. Costeira:** 3–50 NM | vista da terra | marcos naturais e artificiais
- **Nav. Estimada:** qualquer distância | cálculo por rumo + velocidade + tempo
- **Nav. Astronômica:** > 50 NM | observação celeste | alto mar | sextante
- **Nav. Eletrônica:** qualquer distância | radar, GPS, satélites
- **Nav. Águas Restritas / Interior:** < 3 NM | portos | rios
- **Círculo Máximo:** plano passa pelo centro | meridianos | Equador
- **Círculo Menor / Paralelo:** plano NÃO passa pelo centro | representa latitude
- **Meridiano:** círculo máximo vertical | passa pelos polos | representa longitude

---

## 5. Prováveis Assuntos de Prova

> [!danger] Temas para Revisão
> 
> 1. Converter milha náutica para metros e vice-versa
> 2. Distinguir "nó" (velocidade) de "milha náutica" (distância)
> 3. Calcular posição estimada: `D = V × T`
> 4. Identificar o tipo de navegação adequado para uma situação descrita
> 5. Diferença entre círculo máximo e círculo menor
> 6. Definir e identificar meridianos e paralelos
> 7. Saber qual paralelo é também círculo máximo (Equador)
> 8. Descrever quando usar navegação astronômica vs. costeira
> 9. Listar exemplos de acidentes naturais e artificiais usados na nav. costeira
> 10. Efeitos da corrente marítima na navegação estimada

---

## 6. Flashcards para Anki

### Tabela

|Frente (Pergunta)|Verso (Resposta)|
|---|---|
|Quanto mede 1 milha náutica em metros?|1.852 metros|
|O que é um nó (kn)?|1 milha náutica por hora (MN/h) — unidade de velocidade|
|Faixa de distância da navegação costeira?|3 a 50 milhas náuticas da costa|
|Faixa da navegação astronômica?|Acima de 50 milhas náuticas (alto mar)|
|Faixa da navegação em águas restritas?|Menos de 3 milhas náuticas|
|O que caracteriza a navegação estimada?|Posição calculada a partir de posição anterior conhecida + rumo + velocidade + tempo|
|Quais equipamentos caracterizam a navegação eletrônica?|GPS, Radar, satélites, AIS, ECDIS|
|O que é um círculo máximo?|Círculo cujo plano passa pelo centro da Terra; divide a esfera em dois hemisférios iguais|
|O que é um círculo menor (paralelo)?|Círculo cujo plano NÃO passa pelo centro da Terra; corte horizontal|
|O que é um meridiano?|Círculo máximo vertical que passa pelos polos Norte e Sul; representa longitude|
|Qual paralelo é também círculo máximo?|O Equador (único paralelo cujo plano passa pelo centro da Terra)|
|Os paralelos representam que grandeza?|Latitude|
|Os meridianos representam que grandeza?|Longitude|
|Qual é o meridiano de referência?|Meridiano de Greenwich (0°)|
|Por que a navegação estimada pode ter erros?|Correntes marinhas e ventos deslocam o navio da posição calculada|
|Qual instrumento é usado na navegação astronômica?|Sextante|
|Nomeie 3 tipos de acidentes usados na nav. costeira|Naturais: montanha, cabo, ponta. Artificiais: farol, torre, igreja|
|Fórmula da distância percorrida em nav. estimada|D = V × T (D em MN, V em nós, T em horas)|
|Quantos minutos de arco tem 1 grau?|60 minutos de arco (1° = 60')|
|Quantas milhas náuticas tem 1 grau de latitude?|60 milhas náuticas (1° = 60' = 60 MN)|

---

### CSV para importação no Anki

```csv
Quanto mede 1 milha náutica em metros?,1.852 metros
O que é um nó (kn)?,1 milha náutica por hora (MN/h) — unidade de velocidade
Faixa da navegação costeira?,3 a 50 MN da costa
Faixa da navegação astronômica?,Acima de 50 MN (alto mar)
Faixa da navegação em águas restritas?,Menos de 3 MN da costa
O que é navegação estimada?,Posição calculada: posição anterior + rumo + velocidade + tempo
Quais equipamentos caracterizam a nav. eletrônica?,GPS, Radar, satélites, AIS, ECDIS
O que é um círculo máximo?,Círculo cujo plano passa pelo centro da Terra
O que é um meridiano?,Círculo máximo vertical que passa pelos polos; representa longitude
Qual paralelo é círculo máximo?,O Equador
Paralelos representam que grandeza?,Latitude
Meridianos representam que grandeza?,Longitude
Qual é o meridiano de referência?,Meridiano de Greenwich (0°)
Fórmula da distância na nav. estimada?,D = V × T (MN = nós × horas)
1 grau de latitude = quantas MN?,60 milhas náuticas
Instrumento da nav. astronômica?,Sextante
Por que a nav. estimada pode ter erros?,Correntes marinhas e ventos deslocam o navio da posição calculada
Nomeie 3 acidentes usados na nav. costeira,Naturais: montanha/cabo/ponta | Artificiais: farol/torre/igreja
```