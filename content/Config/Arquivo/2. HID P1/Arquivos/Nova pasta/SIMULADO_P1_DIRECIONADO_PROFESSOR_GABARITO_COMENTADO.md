# Gabarito Comentado e Auditoria Técnica — Simulado Oficial P1 (Padrão Direcionamento do Professor)

> **Status:** Gabarito Oficial Revisado Pós-Auditoria — Etapa 2  
> **Arquivos Auditados de Referência:** `Questionário P1.pdf` (DOC-00), Apostilas Teóricas U1 (DOC-01 a DOC-08), Apostila Teórica U2 (DOC-09), `direcionamento_do_professor_prova_1.txt` e `AUDITORIA_DIRECIONAMENTO_PROFESSOR_P1.md`  
> **Finalidade Pedagógica:** Fornecer a resolução comentada das questões, separando com clareza o que consta nas fontes originais, o desenvolvimento matemático formal, a interpretação física e a análise detalhada dos distratores.

---

## Grade Resumo do Gabarito

| Posição | Formato de Avaliação | Assunto Temático | Gabarito Oficial |
| :---: | :--- | :--- | :---: |
| **Questão 1** | Múltipla Escolha | Escoamento incompressível em duto divergente permanente | **Alternativa [B]** |
| **Questão 2** | Múltipla Escolha | Equação da continuidade 3D e cancelamento da densidade absoluta | **Alternativa [C]** |
| **Questão 3** | — | **NÃO SERÁ COBRADA, conforme orientação do professor** | *Não Cobrada* |
| **Questão 4** | Múltipla Escolha | 2ª Lei de Newton em VC infinitesimal, balanço de pressão e sinal negativo | **Alternativa [A]** |
| **Questão 5** | Múltipla Escolha | Condições de contorno cinemáticas (aderência vs. impenetrabilidade) | **Alternativa [C]** |
| **Questão 6** | Completar Lacunas | Frases curtas e diretas sobre os 12 conceitos estruturantes | **10 itens com resposta determinada + 2 itens sem resposta única (7 e 8)** |
| **Questão 7** | Verdadeiro ou Falso | Princípio da Homogeneidade e Procedimento Canônico de Buckingham | **V – V – F – V – V – V – F – V** |
| **Questão 8** | Cálculo Fixo | **CÁLCULO FIXO — SEIS PASSOS** | *Vaga Reservada* |

---

## Resolução Detalhada e Comentada por Questão

---

### Questão 1 — Escoamento Incompressível em Duto Divergente

**GABARITO OFICIAL: ALTERNATIVA [B]**

#### 1. O que está escrito na fonte
- **`Questionário P1.pdf` (Pergunta 4, p. 1):**  
  > "Em um duto divergente operando em regime permanente com fluido incompressível, a área aumenta no sentido do escoamento ($dA/dx > 0$). Pela conservação da massa, a velocidade diminui ($\partial u/\partial x < 0$). Como o regime é permanente ($\partial u/\partial t = 0$), a aceleração local é nula e a aceleração convectiva $a_{\text{conv}} = u \frac{\partial u}{\partial x}$ é negativa, o que representa uma desaceleração da partícula fluida."
- **Apostila Teórica U1 (`1_Leis_de_conservação-007-011.pdf`, pp. 7–9):**  
  A derivada material de $u$ é dada por $\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x}$. No regime permanente com escoamento unidimensional, a aceleração reduz-se à parcela convectiva $u\frac{\partial u}{\partial x}$.

#### 2. Explicação Matemática
1. Pela Equação da Continuidade unidimensional para fluido incompressível:
   $$Q = A(x) \cdot u(x) = \text{constante} \implies u(x) = \frac{Q}{A(x)}$$
2. Derivando em relação a $x$:
   $$\frac{\partial u}{\partial x} = -\frac{Q}{[A(x)]^2}\frac{dA}{dx}$$
   Como $Q > 0$, $A^2 > 0$ e a área é divergente ($\frac{dA}{dx} > 0$), conclui-se que:
   $$\frac{\partial u}{\partial x} < 0$$
3. Calculando a derivada material (aceleração da partícula na direção $x$):
   $$a_x = \frac{Du}{Dt} = \underbrace{\frac{\partial u}{\partial t}}_{= 0\text{ (permanente)}} + \underbrace{u \frac{\partial u}{\partial x}}_{a_{\text{conv}}}$$
   Como $u > 0$ e $\frac{\partial u}{\partial x} < 0$, o produto de sinais resulta em:
   $$a_{\text{conv}} = u \frac{\partial u}{\partial x} < 0$$

#### 3. Interpretação Física Complementar
O vetor velocidade aponta no sentido positivo do eixo axial ($u > 0$). Como a aceleração da partícula aponta no sentido oposto ($a_x < 0$), a taxa de variação da velocidade com o tempo de percurso da partícula resulta na diminuição de sua intensidade escalar ao avançar pelo duto, caracterizando fisicamente a **desaceleração da partícula fluida sob essas condições específicas**.

#### 4. Análise dos Distratores
- **[A] Incorreta:** Confunde regime permanente ($\frac{\partial u}{\partial t} = 0$, invariância temporal em um ponto fixo do espaço) com aceleração nula da partícula ($\frac{Du}{Dt} = 0$). Mesmo sem variação no tempo no ponto fixo, a partícula sofre aceleração convectiva ao se mover por um campo com gradiente espacial de velocidade.
- **[C] Incorreta:** Viola a conservação da massa ($A_1 u_1 = A_2 u_2$). No fluido incompressível, o aumento da área transversal acarreta redução da velocidade ($\frac{\partial u}{\partial x} < 0$), e não aumento.
- **[D] Incorreta:** O termo convectivo $u \frac{\partial u}{\partial x}$ é puramente espacial e unidimensional, operando perfeitamente ao longo de uma linha de corrente retilínea quando há variação de área.
- **[E] Incorreta:** Incompressibilidade significa massa específica constante ($\rho = \text{cte}$), e não velocidade constante. A velocidade varia com a seção transversal do duto.

---

### Questão 2 — Equação da Continuidade Tridimensional e Densidade Absoluta

**GABARITO OFICIAL: ALTERNATIVA [C]**

#### 1. O que está escrito na fonte
- **`Questionário P1.pdf` (Pergunta 7, p. 2):**  
  > "Na água líquida, por ser considerada incompressível, a densidade é constante ($\rho = \text{constante}$). Logo, $\partial\rho/\partial t = 0$, e $\rho$ pode ser colocada em evidência e cancelada por divisão, resultando em $\nabla \cdot \mathbf{V} = 0$."
- **Apostila Teórica U1 (`1_Leis_de_conservação-001-006.pdf`, pp. 4–6):**  
  A equação geral da continuidade é $\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$. Sob $\rho = \text{constante}$, $\frac{\partial \rho}{\partial t} = 0$ e $\nabla \cdot (\rho \mathbf{V}) = \rho (\nabla \cdot \mathbf{V}) = 0$. Dividindo por $\rho$, obtém-se $\nabla \cdot \mathbf{V} = 0$.

#### 2. Explicação Matemática
1. A equação da conservação da massa tridimensional geral é:
   $$\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x} + \frac{\partial (\rho v)}{\partial y} + \frac{\partial (\rho w)}{\partial z} = 0$$
2. Aplicando a hipótese de fluido incompressível ($\rho = \text{constante}$ no espaço e no tempo):
   $$\frac{\partial \rho}{\partial t} = 0 \quad \text{e} \quad \frac{\partial \rho}{\partial x} = \frac{\partial \rho}{\partial y} = \frac{\partial \rho}{\partial z} = 0$$
3. As derivadas espaciais simplificam-se por fatoração da constante $\rho$:
   $$\rho \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \right) = \rho (\nabla \cdot \mathbf{V}) = 0$$
4. Sendo a massa específica da água não nula ($\rho \neq 0$), divide-se ambos os membros por $\rho$:
   $$\nabla \cdot \mathbf{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$

#### 3. Interpretação Física Complementar
A densidade absoluta deixa de figurar explicitamente na equação final porque foi eliminada algebricamente. Em fluidos incompressíveis, a conservação da massa expressa-se geometricamente pela conservação de volume da partícula fluida: o divergente nulo do campo de velocidades ($\nabla \cdot \mathbf{V} = 0$) significa que a taxa de dilatação volumétrica unitária da partícula é nula ($\frac{1}{\delta V}\frac{D(\delta V)}{Dt} = 0$).

#### 4. Análise dos Distratores
- **[A] Incorreta:** A conservação da massa continua sendo a lei fundamental que origina a equação; ela apenas simplifica-se algebricamente sob densidade constante.
- **[B] Incorreta:** O cancelamento é uma operação algébrica exata resultante de $\rho = \text{cte} \neq 0$, e não um desprezo numérico por aproximação.
- **[D] Incorreta:** A densidade não se transforma em peso específico na continuidade. O peso específico $\gamma = \rho g$ surge como força de corpo na Equação da Quantidade de Movimento.
- **[E] Incorreta:** O cancelamento de $\rho$ é plenamente válido para escoamentos tridimensionais genéricos, não dependendo de hipótese unidimensional.

---

### Questão 3 — NÃO SERÁ COBRADA, conforme orientação do professor

> [!NOTE]
> **Registro Oficial de Auditoria:**  
> Conforme determinação do professor em sala de aula (`direcionamento_do_professor_prova_1.txt`), a Questão 3 não será aplicada na avaliação. Sua vaga e numeração original permanecem preservadas sem criação de questões substitutas.

---

### Questão 4 — Segunda Lei de Newton em Volume Infinitesimal e Força de Pressão

**GABARITO OFICIAL: ALTERNATIVA [A]**

#### 1. O que está escrito na fonte
- **Apostila Teórica U1 (`1_Leis_de_conservação-011-018.pdf`, pp. 12–14):**  
  > "Na face esquerda em $x$, a força de pressão é $p\,dy\,dz$. Na face direita em $x+dx$, a força é $-(p + \frac{\partial p}{\partial x}dx)dy\,dz$. Somando as forças de pressão na direção $x$:  
  > $dF_{p,x} = p\,dy\,dz - (p + \frac{\partial p}{\partial x}dx)dy\,dz = -\frac{\partial p}{\partial x}dx\,dy\,dz$.  
  > Por unidade de volume: $f_{p,x} = -\frac{\partial p}{\partial x}$."
- **`Questionário P1.pdf` (Perguntas 11, 12 e 13, pp. 2–3):**  
  A força líquida diferencial de pressão no elemento $dx\,dy\,dz$ é $-\frac{\partial p}{\partial x}dx\,dy\,dz$ e a força por unidade de volume é $-\frac{\partial p}{\partial x}$.

#### 2. Explicação Matemática
1. A pressão atua perpendicularmente e de forma compressiva sobre as faces do elemento diferencial de volume $dVol = dx\,dy\,dz$:
   - Face em $x$ (entrada): a força atua empurrando para o interior no sentido $+x$:
     $$F_{\text{in}} = + p\,dy\,dz$$
   - Face em $x+dx$ (saída): a força atua empurrando para o interior no sentido $-x$:
     $$F_{\text{out}} = - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$$
2. Somando algebricamente as forças compressivas atuantes nas duas faces opostas:
   $$dF_{p,x} = F_{\text{in}} + F_{\text{out}} = p\,dy\,dz - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$$
   $$dF_{p,x} = p\,dy\,dz - p\,dy\,dz - \frac{\partial p}{\partial x}dx\,dy\,dz = -\frac{\partial p}{\partial x}dx\,dy\,dz$$
3. Dividindo pelo volume do elemento diferencial $dVol = dx\,dy\,dz$, obtém-se a força por unidade de volume:
   $$f_{p,x} = \frac{dF_{p,x}}{dx\,dy\,dz} = -\frac{\partial p}{\partial x}$$

#### 3. Explicação do Sinal Negativo
O sinal negativo na expressão resultante:
$$dF_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$$
decorre diretamente do balanço mecânico entre as forças compressivas nas faces: a força na face de saída ($x+dx$) atua no sentido negativo ($-x$), e é essa oposição direcional compressiva que introduz algebricamente o sinal de menos no termo diferencial $-\frac{\partial p}{\partial x}dx\,dy\,dz$.

#### 4. Análise dos Distratores
- **[B] Incorreta:** Erra o sinal da força resultante e da força volumétrica, indicando $+ \frac{\partial p}{\partial x}$.
- **[C] Incorreta:** Inverte as dimensões físicas das duas grandezas (apresenta $dF_{p,x}$ sem o volume e $f_{p,x}$ multiplicado pelo volume).
- **[D] Incorreta:** Em escoamentos com gradiente de pressão, a pressão não é uniforme, de modo que a força líquida nas faces não se anula.
- **[E] Incorreta:** O gradiente de pressão atua como força motriz tanto em fluidos compressíveis quanto incompressíveis.

---

### Questão 5 — Condições de Contorno Cinemáticas em Fronteiras Sólidas Impermeáveis

**GABARITO OFICIAL: ALTERNATIVA [C]**

#### 1. O que está escrito na fonte
- **`Questionário P1.pdf` (Perguntas 15, 16 e 23, pp. 3–4):**  
  > "Condição de não-escorregamento: em fluidos viscosos, a velocidade relativa tangencial do fluido na parede é nula ($u_{\text{rel}} = 0$). Condição de impenetrabilidade: a componente normal da velocidade relativa através da fronteira é nula ($v_{n,\text{rel}} = 0$)."
- **Apostila Teórica U1 (`1_Leis_de_conservação-024-027.pdf`, p. 25; `1_Leis_de_conservação-031-034.pdf`, p. 32):**  
  Em superfícies sólidas impermeáveis, a impenetrabilidade impõe $\mathbf{V}\cdot\mathbf{n} = 0$, e a aderência impõe que o fluido acompanhe a velocidade da placa por atrito viscoso.

#### 2. Explicação Matemática
1. **Condição de Impenetrabilidade:**
   $$\mathbf{V}_{\text{rel}} \cdot \mathbf{n} = (\mathbf{V}_{\text{fluido}} - \mathbf{V}_{\text{parede}}) \cdot \mathbf{n} = 0$$
   Para fronteira rígida fixa em repouso ($\mathbf{V}_{\text{parede}} = \mathbf{0}$):
   $$v_n = \mathbf{V} \cdot \mathbf{n} = 0$$
   Essa condição restringe puramente a componente **normal** relativa de velocidade na interface.
2. **Condição de Aderência ou Não-Escorregamento (*No-Slip*):**
   $$\mathbf{V}_{\text{rel}} \times \mathbf{n} = \mathbf{0} \iff \mathbf{V}_{\text{tang,fluido}} = \mathbf{V}_{\text{tang,parede}}$$
   Para parede fixa em repouso:
   $$u_{\text{fluido}} = 0$$
   Essa condição restringe puramente a componente **tangencial** relativa de velocidade na interface.

#### 3. Interpretação Física Complementar e Ressalva Conceitual
- A condição de impenetrabilidade decorre do fato físico de a fronteira ser sólida e impermeável, impedindo o fluxo ou velocidade relativa normal através da parede.
- **Ressalva conceitual obrigatória:** A condição de impenetrabilidade restringe unicamente a componente normal relativa através da parede ($\mathbf{V}_{\text{rel}}\cdot\mathbf{n}=0$). Ela **não deve ser confundida com ausência de separação do escoamento**, visto que o descolamento da camada limite é um fenômeno de gradiente adverso de pressão no qual a velocidade normal na parede sólida continua sendo rigorosamente nula.
- A condição de aderência decorre dos efeitos da viscosidade e das forças intermoleculares, garantindo que o fluido viscoso não deslize livremente sobre a superfície sólida.

#### 4. Análise dos Distratores
- **[A] Incorreta:** Inverte os papéis cinemáticos das duas condições (atribui a velocidade normal ao não-escorregamento e a tangencial à impenetrabilidade).
- **[B] Incorreta:** Fluidos ideais invíscidos ($\mu = 0$) não satisfazem o não-escorregamento; eles deslizam livremente sobre a parede ($u_{\text{parede}} \neq 0$), satisfazendo apenas a impenetrabilidade.
- **[D] Incorreta:** São condições puramente cinemáticas, pois incidem diretamente sobre o campo de velocidades $\mathbf{V}$, e não sobre o estado de tensões na parede.
- **[E] Incorreta:** A aderência tem origem na viscosidade e interações microscópicas, não tendo relação com gravidade nem se aplicando a fluidos invíscidos.

---

### Questão 6 — Conceitos Estruturantes de Hidrodinâmica I

**GABARITO OFICIAL DOS 12 SUBITENS:**

1. **tensão superficial**.  
   *O que consta na fonte:* No enunciado, a propriedade está explicitamente identificada pelo símbolo $\sigma$ e pela dimensão $[MT^{-2}]$, já constando no texto a massa específica ($\rho$), a viscosidade dinâmica ($\mu$) e a pressão ($p$). Portanto, a única resposta correta é **tensão superficial** (Apostila U2, p. 2; `Questionário P1.pdf`, Q34).
2. **Continuidade**.  
   *O que consta na fonte:* O princípio da conservação da massa aplicado ao volume de controle origina a Equação da Continuidade (`Questionário P1.pdf`, Q6; Apostila U1, pp. 4–6).
3. **euleriana**.  
   *O que consta na fonte:* Observação em coordenadas espaciais fixas no espaço e no tempo (`Questionário P1.pdf`, Q20; Apostila U1, pp. 8–10).
4. **lagrangeana**.  
   *O que consta na fonte:* Acompanhamento individual de partículas fluidas ao longo do tempo (`Questionário P1.pdf`, Q20).
5. **local** ; **convectiva** (nesta ordem estrita).  
   *O que consta na fonte:* A derivada material particiona-se na taxa temporal local ($\frac{\partial \mathbf{V}}{\partial t}$) e na taxa espacial convectiva ($(\mathbf{V}\cdot\nabla)\mathbf{V}$) (`Questionário P1.pdf`, Q3 e Q21; Apostila U1, p. 9).
6. **superfície** ; **corpo**.  
   *O que consta na fonte:* Forças de superfície (contato: pressão e tensões cisalhantes viscosas nas fronteiras) e forças de corpo (ação sobre a massa à distância: peso gravitacional) (`Questionário P1.pdf`, Q14 e Q22; Apostila U1, pp. 11–12). Não se adota a terminologia "campo" por ausência de menção direta na fonte oficial.
7. **ITEM SEM RESPOSTA ÚNICA DOCUMENTALMENTE CONFIRMADA (AMBIGUIDADE NAS FONTES):**  
   O direcionamento original do professor em sala não especificou a condição de contorno do escoamento entre placas planas. Não se trata de uma questão de resposta única já resolvida, existindo duas possibilidades documentadas oficialmente na disciplina:  
   - **Possibilidade 1 (gradiente de pressão entre placas fixas):** conduzido por **gradiente de pressão** $\implies$ escoamento plano de **Poiseuille** (`Questionário P1.pdf`, Q24; Apostila U1, pp. 24–27);  
   - **Possibilidade 2 (placa móvel sob arraste viscoso puro com gradiente nulo):** conduzido por **arraste de placa móvel** $\implies$ escoamento plano de **Couette** (`Questionário P1.pdf`, Q25; Apostila U1, pp. 31–34).  
   *Não há suporte documental para eleger arbitrariamente uma única resposta como definitiva sem a especificação da condição de contorno pelo professor.*
8. **ITEM SEM RESPOSTA ÚNICA DOCUMENTALMENTE CONFIRMADA (AMBIGUIDADE NAS FONTES):**  
   O direcionamento original do professor em sala omitiu a força de oposição confrontada com a inércia. Não se trata de uma questão de resposta única já resolvida, comportando duas possibilidades oficiais registradas nas fontes:  
   - **Possibilidade 1 (inércia versus forças viscosas):** Número de **Reynolds** ... forças **viscosas** ($Re = \frac{\rho U L}{\mu}$) (`Questionário P1.pdf`, Q26; Apostila U2, pp. 3–4);  
   - **Possibilidade 2 (inércia versus forças gravitacionais):** Número de **Froude** ... forças **gravitacionais** ($Fr = \frac{U}{\sqrt{gL}}$) (`Questionário P1.pdf`, Q27; Apostila U2, pp. 4–5).  
   *Ambas as possibilidades possuem suporte documental equivalente, não havendo base para priorizar uma em detrimento da outra.*
9. **modelo** ; **protótipo**.  
   *O que consta na fonte:* O modelo é a embarcação em escala geométrica reduzida testada no tanque; o protótipo é o navio real em escala plena (`Questionário P1.pdf`, Q28; Apostila U2, pp. 13–15).
10. **cinemática** ; **dinâmica** (nesta ordem estrita).  
    *O que consta na fonte:* A ordem das lacunas corresponde rigorosamente à sequência conceitual e solicitada no enunciado: similaridades geométrica, **cinemática** e **dinâmica** (`Questionário P1.pdf`, Q28; Apostila U2, pp. 13–16).
11. **constante**.  
    *O que consta na fonte:* Na similaridade cinemática, as trajetórias são semelhantes e a razão de velocidades em pontos homólogos é constante: $\frac{V_m}{V_p} = \text{constante}$ (Apostila U2, pp. 13–14).
12. **pontos homólogos**.  
    *O que consta na fonte:* A terminologia canônica e oficial da Apostila U2 (pp. 13–15) é rigorosamente **pontos homólogos** (posições espacialmente correspondentes na proporção geométrica $\alpha = L_m / L_p$).  
    *Nota documental:* A locução "partícula homóloga" consta unicamente no registro informal das anotações de sala de aula do aluno (`direcionamento_do_professor_prova_1.txt`), não constituindo termo oficial da apostila.

---

### Dossiê Técnico das Ambiguidades Mapeadas (Itens 7 e 8)

> [!WARNING]
> **Ressalva Pedagógica de Correção (Itens 7 e 8):**  
> Os itens 7 e 8 não devem ser corrigidos como questões objetivas de resposta única enquanto não houver esclarecimento das condições omitidas pelo professor. A correção deve preservar as possibilidades documentadas:  
> - **Item 7:** Poiseuille ou Couette, conforme as condições de escoamento (Poiseuille plano sob gradiente de pressão entre placas fixas; Couette plano sob placa móvel com arraste viscoso).  
> - **Item 8:** Reynolds ou Froude, conforme as forças comparadas (Reynolds para inércia versus forças viscosas; Froude para inércia versus forças gravitacionais).

> [!NOTE]
> **Fundamentação das Duas Possibilidades Documentadas das Ambiguidades:**
> 
> 1. **Placas Planas (Subitem 7):**
>    - *Gradiente de pressão entre placas fixas:* escoamento de **Poiseuille plano** (`Questionário P1.pdf`, Q24; Apostila U1, pp. 24–27).
>    - *Placa móvel sob arraste viscoso:* escoamento de **Couette plano** (`Questionário P1.pdf`, Q25; Apostila U1, pp. 31–34).
>
> 2. **Número Adimensional de Inércia (Subitem 8):**
>    - *Inércia versus forças viscosas:* Número de **Reynolds** ($Re = \frac{\rho U L}{\mu}$) (`Questionário P1.pdf`, Q26; Apostila U2, pp. 3–4).
>    - *Inércia versus forças gravitacionais:* Número de **Froude** ($Fr = \frac{U}{\sqrt{gL}}$) (`Questionário P1.pdf`, Q27; Apostila U2, pp. 4–5).

---

### Questão 7 — Princípio da Homogeneidade Dimensional e Teorema $\Pi$ de Buckingham

**GABARITO OFICIAL (V ou F):**

| Item | Julgamento | Justificativa Documental e Conceitual |
| :---: | :---: | :--- |
| **7.1** | **VERDADEIRO (V)** | **O que consta na fonte:** Apostila U2 (p. 2) e `Questionário P1.pdf` (Q29) afirmam que todos os termos aditivos de uma equação física devem possuir as mesmas dimensões primárias ($MLT$ ou $FLT$).  <br>*Nota conceitual:* A homogeneidade dimensional é condição necessária para a consistência dimensional da equação, embora a validade física plena dependa também da correta representação das leis físicas e coeficientes. |
| **7.2** | **VERDADEIRO (V)** | **O que consta na fonte:** Apostila U2 (p. 2) e `Questionário P1.pdf` (Q30) definem que a adimensionalização é obtida dividindo-se cada termo por uma combinação de variáveis que possua a mesma dimensão física desses termos. |
| **7.3** | **FALSO (F)** | **O que consta na fonte:** O Teorema $\Pi$ de Buckingham (Apostila U2, p. 6; `Questionário P1.pdf`, Q31) estabelece que o número de agrupamentos adimensionais independentes é dado pela **diferença** $k = n - m$, e não pela soma $n + m$. |
| **7.4** | **VERDADEIRO (V)** | **O que consta na fonte:** Transcrição exata da Etapa 1 canônica de Buckingham (Apostila U2, p. 6): listar as variáveis dimensionais do problema e contá-las ($n$), assegurando que sejam independentes. |
| **7.5** | **VERDADEIRO (V)** | **O que consta na fonte:** Transcrição exata da Etapa 2 canônica de Buckingham (Apostila U2, p. 6): listar as dimensões primárias presentes ($m$), sendo tipicamente $M, L, T$ em hidrodinâmica naval. |
| **7.6** | **VERDADEIRO (V)** | **O que consta na fonte:** Transcrição dos três requisitos canônicos da Etapa 4 de Buckingham (Apostila U2, p. 7; `Questionário P1.pdf`, Q32 e Q33): exatamente $m$ variáveis repetidas, contendo todas as dimensões primárias e não formando grupo adimensional entre si. |
| **7.7** | **FALSO (F)** | **O que consta na fonte:** Apostila U2 (p. 7) e `Questionário P1.pdf` (Q33) proíbem a seleção de variáveis repetidas que contenham apenas grandezas geométricas, pois elas contêm unicamente a dimensão $L$, violando o requisito de conter todas as dimensões primárias do problema ($M, L, T$). |
| **7.8** | **VERDADEIRO (V)** | **O que consta na fonte:** Transcrição da Etapa 6 canônica de Buckingham (Apostila U2, p. 7): determinação dos expoentes aplicando a homogeneidade dimensional com expoentes zero no grupo adimensional ($M^0 L^0 T^0$). |

---

### Questão 8 — CÁLCULO FIXO — SEIS PASSOS

> [!IMPORTANT]
> **VAGA RESERVADA PARA O CÁLCULO CANÔNICO EM SEIS PASSOS:**  
> Conforme determinado, o problema de cálculo analítico e discursivo estruturado nas seis etapas canônicas de Buckingham–$\Pi$ permanece integralmente preservado no repositório oficial da disciplina sem qualquer modificação.
