# Registro de Pendências, Divergências e Auditoria Documental — Hidrodinâmica P1

> **Status:** Documento de Auditoria Técnica e Dossiê de Verificação Rigorosa  
> **Objetivo:** Registro exaustivo de reconciliação de contagens, deduções matemáticas completas de Buckingham–$\Pi$, comparação de definições/normalizações e reconfirmação individual das questões Q34 a Q39.

---

## 1. Estrutura Lógica da Auditoria: Classificação Principal e Etiquetas

### 1.1. Errata e Correção da Inconsistência de Contagem
Na versão preliminar do relatório, o intervalo **Q36 a Q39** foi inadvertidamente referido como contendo 5 questões. 
- **Correção Matemática:** O intervalo fechado $[36, 39]$ em $\mathbb{N}$ compreende estritamente **4 questões**: $\{36, 37, 38, 39\}$, pois $39 - 36 + 1 = 4$.
- **Reconciliação da Questão 40:** A questão **Q40** (sensibilidade de $\Delta p$ à redução de $D/2$, gerando aumento de $2^4 = 16$ vezes) possui dedução algébrica imediata e confirmada no `Questionário P1.pdf` e no banco `44_QUESTÕES_P1_SEM_CÁLCULO.json`. Ela pertence ao conjunto de questões com suporte direto das fontes.

---

### 1.2. Dimensão A: Classificação Principal Exclusiva por Questão (Total = 40)
Para sanar qualquer contradição entre partição e sobreposição, a auditoria adota uma **classificação primária mutuamente exclusiva**. Cada uma das 40 questões do questionário é atribuída a uma única categoria principal, de modo que a soma é rigorosa e exatamente igual a 40:

| Categoria Principal Exclusiva | Questões Abrangidas | Quantidade | Percentual | Critério de Classificação |
| :--- | :--- | :---: | :---: | :--- |
| **1. Suporte Direto sem Divergência** | Q1 a Q33 e Q40 | **34** | 85,0% | Conteúdo conceitual, equações e gabaritos confirmados diretamente tanto nas apostilas quanto no questionário oficial, sem divergências documentais. |
| **2. Divergência Documental Identificada** | Q34 e Q35 | **2** | 5,0% | Suporte teórico presente nas apostilas, porém com divergência documental explícita de notação ou de valores de contorno em relação ao questionário. |
| **3. Gabarito no Questionário com Dedução Complementada** | Q36, Q37, Q38 e Q39 | **4** | 10,0% | Gabarito oficial e expressões finais constam no `Questionário P1.pdf`, mas a dedução formal em coordenadas cilíndricas foi complementada no resumo de estudos. |
| **Total Geral da Classificação Principal** | **Q1 a Q40** | **40** | **100,0%** | **Partição 1-para-1 exaustiva e sem sobreposição na Dimensão A.** |

$$\text{Soma da Dimensão A}: 34 + 2 + 4 = 40 \text{ questões (100\% do universo auditado)}$$

---

### 1.3. Dimensão B: Etiquetas Complementares de Auditoria (Metadados Transversais Não Excludentes)
As categorias de auditoria não se sobrepõem na contagem de questões porque a sobreposição pertence exclusivamente à **Dimensão B**. As **Etiquetas Complementares** são atributos qualitativos independentes que registram aspectos específicos de verificação sobre as questões, sem alterar sua categoria principal nem sua contagem unitária:

1. **`[DIV]` — Existência de Divergência nas Fontes (2 questões: Q34, Q35):**  
   - *Q34:* Notação da apostila de U2 ($Rn, Fn, Wn$ e $R_{\text{forma}} / (\rho L^2 U^2)$) versus notação clássica do Questionário P1 ($Re, Fr, We$ e $C_T$).  
   - *Q35:* Faixa crítica de transição no duto: menção genérica de $(Re_D)_{cr} \cong 2300$ na apostila de U2 (p. 4) versus critério tripartido rigoroso do Questionário P1 ($<2300$, $2300-4000$, $>4000$).
2. **`[COMP]` — Presença de Dedução Analítica Complementar (4 questões: Q36 a Q39):**  
   - Incide sobre as questões do escoamento de Hagen–Poiseuille em tubos circulares (perfil $u(r)$, relação $u_{\max}=2U$, tensão $\tau(r)$ e queda de pressão $\Delta p$). A dedução em coordenadas polares cilíndricas $(r, \theta, x)$ foi estruturada como suporte analítico no resumo porque a Apostila de U1 limitou-se ao caso cartesiano de placas planas.
3. **`[CONF]` — Necessidade de Confirmação com o Professor (7 questões: Q34, Q35, Q36–Q39 e premissa de $R_{\text{forma}}$):**  
   - Recomendações pontuais para o estudante consultar o docente sobre critérios de correção na prova discursiva (exigência de desenvolvimento em coordenadas cilíndricas, aceitação das faixas de transição e escopo do coeficiente de resistência).
4. **`[LIM]` — Limitações de Verificação Documental (5 questões: Q34, Q36–Q39):**  
   - Registra passagens em que o acervo documental local do docente não apresenta a dedução matemática ou a fórmula explícita fechada (ex.: ausência da fórmula de normalização de $C_T$ no Questionário P1 Q34 e omissão do capítulo de tubos cilíndricos na Apostila de U1).

---

## 2. Deduções Completas de Buckingham–$\Pi$: Duto e Casco Naval

### 2.1. Caso 1: Escoamento em Duto Circular (Apostila U2 p. 8 e `Resolução Q.5 - Passo 6.md`)

#### A. Identificação das Variáveis e Dimensões Primárias ($MLT$)
- Número total de grandezas físicas: $n = 4$.
- Dimensões fundamentais envolvidas: Massa ($M$), Comprimento ($L$), Tempo ($T$) $\implies m = 3$.

| Variável | Símbolo | Dimensão Fundamental | Significado Físico |
| :--- | :---: | :---: | :--- |
| Velocidade média do escoamento | $u$ | $[L T^{-1}]$ | Cinemática do escoamento |
| Diâmetro interno do duto | $D$ | $[L]$ | Geometria da seção transversal |
| Viscosidade dinâmica do fluido | $\mu$ | $[M L^{-1} T^{-1}]$ | Propriedade de transporte viscoso |
| Massa específica do fluido | $\rho$ | $[M L^{-3}]$ | Propriedade inercial do fluido |

#### B. Teorema de Buckingham e Seleção das Variáveis Repetidas
Pelo teorema $\Pi$, o número de grupos adimensionais independentes é:
$$k = n - m = 4 - 3 = 1 \text{ grupo adimensional } (\Pi_1)$$

- **Variáveis repetidas selecionadas ($m = 3$):** $\rho, \mu, u$.
- **Verificação de Independência Dimensional:**  
  A matriz dos expoentes dimensionais de $\{\rho, \mu, u\}$ no sistema $(M, L, T)$ é:
  $$A = \begin{pmatrix}
  & M & L & T \\
  \rho & 1 & -3 & 0 \\
  \mu & 1 & -1 & -1 \\
  u & 0 & 1 & -1
  \end{pmatrix}$$
  O determinante desta matriz é:
  $$\det(A) = 1 \cdot [(-1)(-1) - (-1)(1)] - (-3) \cdot [1(-1) - 0] + 0 = 1 \cdot (1 + 1) + 3 \cdot (-1) = 2 - 3 = -1 \neq 0$$
  Como $\det(A) \neq 0$, o conjunto $\{\rho, \mu, u\}$ é linearmente independente e contém as três dimensões básicas $M, L, T$.

- **Variável não repetida:** $D$.

#### C. Montagem do Grupo $\Pi_1$ e Resolução do Sistema de Expoentes
O monômio adimensional $\Pi_1$ é formulado como:
$$\Pi_1 = D \cdot \rho^a \cdot \mu^b \cdot u^c$$

Substituindo as dimensões fundamentais:
$$[M^0 L^0 T^0] = [L]^1 \cdot [M L^{-3}]^a \cdot [M L^{-1} T^{-1}]^b \cdot [L T^{-1}]^c$$
$$M^0 L^0 T^0 = M^{a+b} \cdot L^{1 - 3a - b + c} \cdot T^{-b - c}$$

Para que $\Pi_1$ seja estritamente adimensional, os expoentes de cada dimensão fundamental devem ser identicamente nulos:
1. **Equação da Massa ($M$):**
   $$a + b = 0 \implies a = -b$$
2. **Equação do Tempo ($T$):**
   $$-b - c = 0 \implies c = -b$$
3. **Equação do Comprimento ($L$):**
   $$1 - 3a - b + c = 0$$

Substituindo $a = -b$ e $c = -b$ na equação do comprimento:
$$1 - 3(-b) - b + (-b) = 0 \implies 1 + 3b - b - b = 0 \implies 1 + b = 0 \implies b = -1$$

Determinando os valores de $a$ e $c$:
$$a = -(-1) = 1$$
$$c = -(-1) = 1$$

Substituindo os expoentes calculados $(a = 1, b = -1, c = 1)$ na expressão de $\Pi_1$:
$$\Pi_1 = D^1 \cdot \rho^1 \cdot \mu^{-1} \cdot u^1 = \frac{\rho u D}{\mu}$$

$$\Pi_1 \equiv Re_D \quad (\text{Número de Reynolds no Duto})$$

---

### 2.2. Caso 2: Resistência de Avanço do Casco Naval (Apostila U2 pp. 9–12 e Questionário P1 Q34)

#### A. Identificação das Variáveis e Dimensões Primárias ($MLT$)
- Número total de variáveis físicas: $n = 7$.
- Dimensões fundamentais ($MLT$): $m = 3$.
- Número de monômios independentes: $k = n - m = 7 - 3 = 4$ grupos ($\Pi_1, \Pi_2, \Pi_3, \Pi_4$).

| Variável | Símbolo | Dimensão | Significado Físico no Escoamento Naval |
| :--- | :---: | :---: | :--- |
| Resistência total / Força de arrasto | $R$ | $[M L T^{-2}]$ | Força hidrodinâmica resistente oposta ao avanço |
| Massa específica da água | $\rho$ | $[M L^{-3}]$ | Propriedade inercial do fluido circundante |
| Velocidade de avanço da embarcação | $U$ | $[L T^{-1}]$ | Cinemática global da embarcação |
| Comprimento de linha d'água | $L$ | $[L]$ | Escala geométrica longitudinal do casco |
| Viscosidade dinâmica da água | $\mu$ | $[M L^{-1} T^{-1}]$ | Efeitos de atrito viscoso e camada limite |
| Aceleração da gravidade | $g$ | $[L T^{-2}]$ | Força de restauração de ondas de superfície livre |
| Tensão superficial da interface água-ar | $\sigma$ | $[M T^{-2}]$ | Forças capilares na interface livre ($[\text{Força}]/[\text{Comprimento}]$) |

#### B. Seleção da Tríade de Variáveis Repetidas
Na mecânica dos fluidos e na apostila de U2 (p. 9), adota-se a tríade canônica $\{\rho, U, L\}$ (fluido, cinemática, geometria):
$$B = \begin{pmatrix}
& M & L & T \\
\rho & 1 & -3 & 0 \\
U & 0 & 1 & -1 \\
L & 0 & 1 & 0
\end{pmatrix} \implies \det(B) = 1 \cdot [1 \cdot 0 - (-1) \cdot 1] = 1 \neq 0$$
As três grandezas são dimensionalmente independentes e contêm $M, L, T$.

Variáveis não repetidas para cada monômio: $R, \mu, g, \sigma$.

---

#### C. Dedução Passo a Passo dos Quatro Grupos Adimensionais

##### 1. Dedução de $\Pi_1$ (Variável não repetida: Força de Resistência $R$):
$$\Pi_1 = R \cdot \rho^a L^b U^c$$
$$[M^0 L^0 T^0] = [M L T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{1 - 3a + b + c} \cdot T^{-2 - c}$$

Montagem e resolução do sistema de expoentes:
1. $M: 1 + a = 0 \implies a = -1$
2. $T: -2 - c = 0 \implies c = -2$
3. $L: 1 - 3a + b + c = 0 \implies 1 - 3(-1) + b + (-2) = 0 \implies 1 + 3 + b - 2 = 0 \implies b + 2 = 0 \implies b = -2$

Grupo resultante:
$$\Pi_1 = R \cdot \rho^{-1} L^{-2} U^{-2} = \frac{R}{\rho U^2 L^2}$$

##### 2. Dedução de $\Pi_2$ (Variável não repetida: Viscosidade Dinâmica $\mu$):
$$\Pi_2 = \mu \cdot \rho^a L^b U^c$$
$$[M^0 L^0 T^0] = [M L^{-1} T^{-1}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{-1 - 3a + b + c} \cdot T^{-1 - c}$$

Montagem e resolução do sistema de expoentes:
1. $M: 1 + a = 0 \implies a = -1$
2. $T: -1 - c = 0 \implies c = -1$
3. $L: -1 - 3a + b + c = 0 \implies -1 - 3(-1) + b + (-1) = 0 \implies -1 + 3 + b - 1 = 0 \implies b + 1 = 0 \implies b = -1$

Grupo resultante:
$$\Pi_2 = \mu \cdot \rho^{-1} L^{-1} U^{-1} = \frac{\mu}{\rho U L}$$

##### 3. Dedução de $\Pi_3$ (Variável não repetida: Aceleração da Gravidade $g$):
$$\Pi_3 = g \cdot \rho^a L^b U^c$$
$$[M^0 L^0 T^0] = [L T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^a \cdot L^{1 - 3a + b + c} \cdot T^{-2 - c}$$

> [!note] Nota de Auditoria sobre Lapso Tipográfico da Apostila U2 (p. 11):
> Na linha intermediária da página 11, a apostila do professor agrupa os termos como $M^a L^{1-3a+b+c} T^{-1-c}$, com $-1-c$ no expoente de $T$. Trata-se de erro de digitação evidente, pois $g$ tem dimensão $[L T^{-2}]$. Na linha imediatamente posterior, o professor resolve corretamente $0 = -2 - c \implies c = -2$.

Montagem e resolução do sistema de expoentes:
1. $M: a = 0$
2. $T: -2 - c = 0 \implies c = -2$
3. $L: 1 - 3(0) + b + (-2) = 0 \implies 1 + b - 2 = 0 \implies b = 1$

Grupo resultante:
$$\Pi_3 = g \cdot \rho^0 L^1 U^{-2} = \frac{g L}{U^2}$$

##### 4. Dedução de $\Pi_4$ (Variável não repetida: Tensão Superficial $\sigma$):
Como $[\sigma] = [\text{Força}] / [\text{Comprimento}] = [M L T^{-2}] / [L] = [M T^{-2}]$:
$$\Pi_4 = \sigma \cdot \rho^a L^b U^c$$
$$[M^0 L^0 T^0] = [M T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{-3a + b + c} \cdot T^{-2 - c}$$

Montagem e resolução do sistema de expoentes:
1. $M: 1 + a = 0 \implies a = -1$
2. $T: -2 - c = 0 \implies c = -2$
3. $L: -3a + b + c = 0 \implies -3(-1) + b + (-2) = 0 \implies 3 + b - 2 = 0 \implies b + 1 = 0 \implies b = -1$

Grupo resultante:
$$\Pi_4 = \sigma \cdot \rho^{-1} L^{-1} U^{-2} = \frac{\sigma}{\rho U^2 L}$$

---

## 3. Confronto Detalhado de Definições, Normalizações e Equivalência Física

Não basta afirmar que um grupo é o inverso do outro para postular equivalência. O Teorema $\Pi$ de Buckingham estabelece que se uma relação física é descrita por $f(\Pi_1, \Pi_2, \dots, \Pi_k) = 0$, qualquer conjunto de transformações bijetoras monótonas $\Pi'_i = \phi_i(\Pi_i)$ que preserve a adimensionalidade e a monotonicidade física é rigorosamente equivalente. Abaixo demonstra-se a compatibilidade física, dinâmica e matemática de cada parâmetro.

### 3.1. Número de Reynolds: $Rn$ (Apostila U2 p. 11) versus $Re$ (Questionário P1 Q34)

| Aspecto | Formulação da Apostila U2 (Prof. Edson Mesquita) | Formulação do Questionário P1 (Gabarito Oficial) |
| :--- | :--- | :--- |
| **Símbolo adotado** | $Rn$ | $Re$ |
| **Definição analítica** | $Rn = \frac{1}{\Pi_2} = \frac{\rho U L}{\mu}$ | $Re = \frac{\rho U L}{\mu}$ |
| **Monômio bruto de Buckingham** | $\Pi_2 = \frac{\mu}{\rho U L}$ | $\Pi_2 = \frac{\mu}{\rho U L}$ |
| **Balanço dinâmico de forças** | $\frac{\text{Força de Inércia}}{\text{Força Viscosa}} = \frac{\rho U^2 L^2}{\mu U L} = \frac{\rho U L}{\mu}$ | $\frac{\text{Força de Inércia}}{\text{Força Viscosa}} = \frac{\rho U^2 L^2}{\mu U L} = \frac{\rho U L}{\mu}$ |
| **Veredito de Equivalência** | **RIGOROSAMENTE IDÊNTICOS ($Rn \equiv Re$)** | |

**Fundamentação Mecânica:**  
A inversão $\Pi_2 \to \Pi_2^{-1}$ é fisicamente indispensável para alinhar o parâmetro com a convenção canônica da Mecânica dos Fluidos de que números adimensionais devem expressar o predomínio da **inércia** sobre as forças resistentes. Como $\Pi_2$ puro quantifica $(\text{Viscosidade})/(\text{Inércia})$, seu inverso $1/\Pi_2 = \frac{\rho U L}{\mu}$ traduz diretamente o crescimento da turbulência à medida que o valor numérico se eleva. A diferença entre $Rn$ e $Re$ é puramente de nomenclatura notacional.

---

### 3.2. Número de Froude: $Fn$ (Apostila U2 p. 11) versus $Fr$ (Questionário P1 Q34)

| Aspecto | Formulação da Apostila U2 | Formulação do Questionário P1 |
| :--- | :--- | :--- |
| **Símbolo adotado** | $Fn$ | $Fr$ |
| **Definição analítica** | $Fn = \frac{1}{\sqrt{\Pi_3}} = \frac{U}{\sqrt{g L}}$ | $Fr = \frac{U}{\sqrt{g L}}$ |
| **Monômio bruto de Buckingham** | $\Pi_3 = \frac{g L}{U^2}$ | $\Pi_3 = \frac{g L}{U^2}$ |
| **Balanço dinâmico de forças** | $\sqrt{\frac{\text{Força de Inércia}}{\text{Força Gravitacional}}} = \sqrt{\frac{\rho U^2 L^2}{\rho g L^3}} = \frac{U}{\sqrt{g L}}$ | $\sqrt{\frac{\text{Força de Inércia}}{\text{Força Gravitacional}}} = \sqrt{\frac{\rho U^2 L^2}{\rho g L^3}} = \frac{U}{\sqrt{g L}}$ |
| **Veredito de Equivalência** | **RIGOROSAMENTE IDÊNTICOS ($Fn \equiv Fr$)** | |

**Fundamentação Mecânica:**  
O monômio dimensional direto obtido pelo método é $\Pi_3 = \frac{g L}{U^2}$, que representa a razão inversa da inércia em relação à gravidade elevada ao quadrado ($1/Fr^2$). Para compatibilizar o parâmetro com a velocidade de propagação de ondas de gravidade em águas rasas ($c = \sqrt{g h}$), a hidrodinâmica naval padronizou a raiz quadrada do inverso: $\Pi_3^{-1/2} = \frac{U}{\sqrt{g L}}$. Assim, $Fr = 1$ indica velocidade de avanço igual à velocidade crítica da onda (*escoamento crítico*). Tanto $Fn$ quanto $Fr$ compartilham rigorosamente esta mesma formulação.

---

### 3.3. Número de Weber: $Wn$ (Apostila U2 p. 12) versus $We$ (Questionário P1 Q34)

| Aspecto | Formulação da Apostila U2 | Formulação do Questionário P1 |
| :--- | :--- | :--- |
| **Símbolo adotado** | $Wn$ | $We$ |
| **Definição analítica** | $Wn = \frac{1}{\Pi_4} = \frac{\rho U^2 L}{\sigma}$ | $We = \frac{\rho U^2 L}{\sigma}$ |
| **Monômio bruto de Buckingham** | $\Pi_4 = \frac{\sigma}{\rho U^2 L}$ | $\Pi_4 = \frac{\sigma}{\rho U^2 L}$ |
| **Balanço dinâmico de forças** | $\frac{\text{Força de Inércia}}{\text{Força de Tensão Superficial}} = \frac{\rho U^2 L^2}{\sigma L} = \frac{\rho U^2 L}{\sigma}$ | $\frac{\text{Força de Inércia}}{\text{Força de Tensão Superficial}} = \frac{\rho U^2 L^2}{\sigma L} = \frac{\rho U^2 L}{\sigma}$ |
| **Veredito de Equivalência** | **RIGOROSAMENTE IDÊNTICOS ($Wn \equiv We$)** | |

**Fundamentação Mecânica:**  
A inversão $\Pi_4 \to 1/\Pi_4$ coloca as forças inerciais desestabilizadoras no numerador em contraposição às forças coesivas de tensão superficial estabilizadoras no denominador. Governa a formação de borrifos (*spray*) e quebra de ondas na proa. As definições são integralmente idênticas.

---

### 3.4. Coeficiente de Resistência do Casco: Grupo de Buckingham ($\Pi_1$) versus Coeficiente Naval da ITTC ($C_T$)

| Aspecto Analítico | Formulação da Apostila U2 (Prof. Edson Mesquita, p. 10) | Formulação do Questionário P1 (DOC-00, Pergunta 34) | Convenção Internacional da Hidrodinâmica Naval (ITTC) |
| :--- | :--- | :--- | :--- |
| **Definição Matemática** | $\Pi_1 = \frac{R_{\text{forma}}}{\rho U^2 L^2}$ | $C_T$ *(termo nominal citado no gabarito, fórmula omitida)* | $C_T = \frac{R_T}{\frac{1}{2} \rho S U^2}$ |
| **Escopo da Força $R$** | Força de arrasto de pressão/forma ($R_{\text{forma}}$) | Resistência Total de avanço do casco ($R$ ou $R_T$) | Resistência Total medida no dinamômetro ($R_T$) |
| **Área de Referência** | $L^2$ (escala de comprimento ao quadrado) | Implícita em Buckingham como $L^2$ | $S$ (área da superfície molhada real do casco) |
| **Fator Inercial $1/2$** | Ausente (não emerge do sistema $MLT$) | Ausente na análise dimensional pura | Presente (pressão dinâmica $\frac{1}{2}\rho U^2$) |
| **Veredito Dimensional** | **Equivalência Dimensional Rigorosa $[M^0 L^0 T^0]$** | **Equivalência Dimensional Rigorosa $[M^0 L^0 T^0]$** | **Equivalência Dimensional Rigorosa $[M^0 L^0 T^0]$** |
| **Veredito Numérico** | **NUMERICAMENTE DISTINTOS** ($\Pi_1 \neq C_T$) | Relacionados pelo fator geométrico $\frac{2}{c_s}$ | **NUMERICAMENTE DISTINTOS** ($C_T = \frac{2}{c_s} \Pi_1$) |

#### A. Relação Algébrica Exata Passo a Passo (sem Omissão de Fatores Constantes)
Partindo da definição convencional do coeficiente de resistência da ITTC e introduzindo a relação geométrica $S = c_s L^2$:
$$C_T = \frac{R}{\frac{1}{2} \rho S U^2}$$

Substituindo $S = c_s L^2$ explicitamente:
$$C_T = \frac{R}{\frac{1}{2} \rho (c_s L^2) U^2} = \frac{R}{\left(\frac{1}{2} c_s\right) \rho U^2 L^2} = \frac{1}{\frac{1}{2} c_s} \cdot \left( \frac{R}{\rho U^2 L^2} \right)$$

Como $\Pi_1 = \frac{R}{\rho U^2 L^2}$, obtém-se rigorosamente:
$$C_T = \left( \frac{2}{c_s} \right) \cdot \Pi_1 \iff \Pi_1 = \left( \frac{c_s}{2} \right) \cdot C_T$$

#### B. Natureza de $c_s = S/L^2$ e Condições de Constância
- **Conceito:** O parâmetro $c_s = \frac{S}{L^2}$ é um coeficiente de forma geométrico puro e adimensional, representando a razão entre a área molhada tridimensional do casco imerso e o quadrado do seu comprimento de referência (ex.: $L_{wl}^2$).
- **Condições de Validade como Constante:**  
  1. *Similaridade geométrica estrita (geosim):* O modelo em tanque e o navio real devem possuir exatamente as mesmas proporções geométricas e de escala linear.
  2. *Condição de flutuação e calado invariantes:* O calado e o caimento estático devem ser rigorosamente os mesmos.
  3. *Regime hidrodinâmico com deformação moderada da superfície livre:* Assume-se que a geração do trem de ondas, o caimento dinâmico (*running trim*) e o afundamento da popa (*sinkage*) não alterem expressivamente a área molhada em relação à condição estática. Caso o navio navegue em Froude elevado ($Fr > 0,35$), a variação dinâmica da área molhada $S(U)$ faz com que $c_s$ deixe de ser rigorosamente constante.

#### C. Diferenciação Explícita entre as Grandezas
1. **Grupo Adimensional Direto de Buckingham ($\Pi_1 = \frac{R}{\rho U^2 L^2}$):**  
   Monômio obtido exclusivamente pelo cancelamento das dimensões primárias $M, L, T$. Utiliza $L^2$ como escala de área e não incorpora fatores arbitrários como $1/2$, pois constantes adimensionais puras não emergem de sistemas homogêneos de expoentes.
2. **Coeficiente Normalizado pela Superfície Molhada ($C_T = \frac{R}{\frac{1}{2} \rho S U^2}$):**  
   Coeficiente prático e normativo da engenharia naval. Normaliza a força pela pressão dinâmica livre ($\frac{1}{2}\rho U^2$) e pela área real de atrito viscoso ($S$).
3. **Equivalência Dimensional:**  
   Ambos são estritamente adimensionais ($[M^0 L^0 T^0]$) e traduzem o mesmo princípio mecânico: a razão entre uma força hidrodinâmica resistente e a inércia do escoamento.
4. **Diferença Numérica Categórica:**  
   **$\Pi_1$ e $C_T$ NÃO são numericamente iguais.**  
   Em navios mercantes e militares de deslocamento típicos, a área de superfície molhada escala de modo que $c_s = S/L^2$ situa-se historicamente no intervalo de $0,10$ a $0,30$. Consequentemente:
   $$\frac{2}{c_s} \approx \frac{2}{0,15} \approx 13,3 \quad (\text{variando tipicamente entre } 6,7 \text{ e } 20)$$
   Portanto, o valor numérico de $C_T$ é de uma a duas ordens de grandeza maior que o valor numérico de $\Pi_1$. Não se deve declarar igualdade numérica entre eles.

#### D. Registro de Limitação Documental
No acervo documental do professor:
- A Apostila de U2 (p. 10) restringe a dedução a $\Pi_1 = \frac{R_{\text{forma}}}{\rho L^2 U^2}$ e chama-o de coeficiente de arrasto de forma ($C_D$).
- O `Questionário P1.pdf` (Pergunta 34) cita nominalmente o "Coeficiente de Resistência Total ($C_T$)", sem registrar sua fórmula analítica de cálculo.
- *Diretriz de integridade:* Não se deve substituir silenciosamente o monômio de Buckingham pela fórmula da ITTC como se esta constasse na apostila. No resumo, mantém-se a dedução de $\Pi_1$ e documenta-se a relação algébrica exata $C_T = \frac{2}{c_s}\Pi_1$ para enriquecimento analítico do estudante.

---

## 4. Reconfirmação Individual e Detalhada das Questões Q34 a Q39

Confrontou-se individualmente cada uma das questões de Q34 a Q39 com o texto do `Questionário P1.pdf`, as apostilas teóricas e a física dos escoamentos.

### Ficha de Verificação — Questão 34
- **Enunciado Oficial (DOC-00, p. 5):**  
  *"Na análise da resistência de avanço do casco, considerando as variáveis $R, \rho, U, L, \mu, g, \sigma$ no sistema massa-comprimento-tempo ($MLT$), quantos e quais são os grupos adimensionais clássicos formados?"*
- **Gabarito Oficial do Professor (DOC-00, p. 5):**  
  *"Como temos $n = 7$ e $m = 3$, formam-se $k = 7 - 3 = 4$ grupos adimensionais: o Coeficiente de Resistência Total ($C_T$), o Número de Reynolds ($Re$), o Número de Froude ($Fr$) e o Número de Weber ($We$)."*
- **Evidência nas Fontes:**  
  Apostila U2 (DOC-09), pp. 9–12: dedução exata das variáveis e dos 4 grupos, usando $Rn, Fn, Wn$ e $R_{\text{forma}}/(\rho L^2 U^2)$.
- **Classificação Principal (Exclusiva):** **`[DIVERGÊNCIA DOCUMENTAL]`**  
- **Etiquetas Complementares:** `[DIV]`, `[CONF]`, `[LIM]`  
- **Pendência Real:** Nenhuma pendência física/matemática. Registrar em prova ambas as notações caso o professor solicite a nomenclatura de aula ($Rn, Fn, Wn$). Limitação: fórmula explícita de $C_T$ omitida no questionário.

---

### Ficha de Verificação — Questão 35
- **Enunciado Oficial (DOC-00, p. 5):**  
  *"Para o escoamento de água em um conduto cilíndrico de diâmetro interno $D$ com velocidade média $U$, densidade $\rho$ e viscosidade $\mu$, como é definido o Número de Reynolds e quais são as faixas críticas de transição interna?"*
- **Gabarito Oficial do Professor (DOC-00, p. 5–6):**  
  *"Define-se como $Re_D = \frac{\rho U D}{\mu}$. O escoamento em duto circular é:  
  • Laminar: para $Re_D < 2300$;  
  • De transição: para $2300 \le Re_D \le 4000$;  
  • Turbulento: para $Re_D > 4000$."*
- **Evidência nas Fontes:**  
  Apostila U2 (DOC-09), p. 4: define $Re_D = \frac{\rho u d}{\mu}$ e cita apenas $(Re_d)_{cr} \cong 2,3 \times 10^3$. Não discrimina o limite superior $4000$.
- **Classificação Principal (Exclusiva):** **`[DIVERGÊNCIA DOCUMENTAL]`**  
- **Etiquetas Complementares:** `[DIV]`, `[CONF]`  
- **Pendência Real:** Confirmar com o professor se em questões conceituais ele exige a faixa tripartida do questionário ($<2300$, $2300-4000$, $>4000$) ou a citação simples de $2300$ da apostila.

---

### Ficha de Verificação — Questão 36
- **Enunciado Oficial (DOC-00, p. 6):**  
  *"Partindo do equilíbrio diferencial entre gradiente de pressão e tensões viscosas no interior de um tubo cilíndrico, qual é o formato geométrico do perfil radial de velocidades $u(r)$ no regime laminar?"*
- **Gabarito Oficial do Professor (DOC-00, p. 6):**  
  *"O perfil é parabólico, onde a velocidade varia em função do raio $r$ a partir do centro segundo a equação:  
  $$u(r) = u_{\max} \left[ 1 - \left( \frac{r}{R} \right)^2 \right]$$  
  sendo $R = D/2$ o raio interno do duto."*
- **Evidência nas Fontes:**  
  O `Questionário P1.pdf` fornece a fórmula e a caracterização física. A Apostila de U1 (DOC-06, pp. 24–27) deduz apenas o perfil cartesiano entre placas planas $u(y) = u_{\max}[1 - (y/h)^2]$. A dedução cilíndrica axial $\tau(r) = \frac{r}{2}\frac{\Delta p}{L} \implies u(r) = \frac{\Delta p R^2}{4\mu L}[1-(r/R)^2]$ é canônica da mecânica dos fluidos e foi desenvolvida no resumo para dar sustentação ao gabarito.
- **Classificação Principal (Exclusiva):** **`[DEDUÇÃO COMPLEMENTAR]`**  
- **Etiquetas Complementares:** `[COMP]`, `[CONF]`, `[LIM]`  
- **Pendência Real:** Como o simulado de avaliação foi ajustado para focar estritamente em questões conceituais (5 questões), verificar com o professor se na prova teórica oficial haverá exigência de dedução formal em coordenadas cilíndricas ou se as questões cobrarão a aplicação conceitual e qualitativa das equações.

---

### Ficha de Verificação — Questão 37
- **Enunciado Oficial (DOC-00, p. 6):**  
  *"Em um escoamento laminar totalmente desenvolvido em duto circular (Hagen-Poiseuille), qual é a relação numérica exata entre a velocidade na linha de centro ($u_{\max}$) e a velocidade média ($U$) do fluxo?"*
- **Gabarito Oficial do Professor (DOC-00, p. 6):**  
  *"A velocidade máxima no centro é exatamente o dobro da velocidade média:  
  $$u_{\max} = 2U$$"*
- **Evidência nas Fontes:**  
  Questionário P1, p. 6. Contraste documental: para placas planas paralelas (Apostila U1 DOC-06 p. 26), a relação deduzida é $u_{\max} = 1,5 U$. No tubo cilíndrico, a integração radial $Q = \int_0^R u_{\max}[1-(r/R)^2] 2\pi r dr = \frac{\pi R^2}{2} u_{\max} \implies U = Q/(\pi R^2) = u_{\max}/2 \implies u_{\max} = 2U$.
- **Classificação Principal (Exclusiva):** **`[DEDUÇÃO COMPLEMENTAR]`**  
- **Etiquetas Complementares:** `[COMP]`  
- **Pendência Real:** Nenhuma pendência física; relação analítica exata e comprovada.

---

### Ficha de Verificação — Questão 38
- **Enunciado Oficial (DOC-00, p. 6):**  
  *"Como se comporta a tensão de cisalhamento viscosa $\tau(r)$ ao longo da seção transversal de um duto circular preenchido por escoamento em regime permanente?"*
- **Gabarito Oficial do Professor (DOC-00, p. 6):**  
  *"A tensão de cisalhamento varia linearmente com o raio $r$: ela é nula no centro do tubo ($r = 0$, onde o gradiente de velocidade $\frac{du}{dr} = 0$) e atinge seu valor máximo na parede sólida ($r = R = D/2$)."*
- **Evidência nas Fontes:**  
  Questionário P1, p. 6. A dedução por balanço de quantidade de movimento no volume cilíndrico de raio $r$ e comprimento $L$ fornece:
  $$\Delta p (\pi r^2) = \tau(r) (2\pi r L) \implies \tau(r) = \frac{r}{2}\frac{\Delta p}{L}$$
  comprovando a linearidade estrita com $r$, nula em $r=0$ e máxima em $r=R$.
- **Classificação Principal (Exclusiva):** **`[DEDUÇÃO COMPLEMENTAR]`**  
- **Etiquetas Complementares:** `[COMP]`  
- **Pendência Real:** Nenhuma pendência física; equilíbrio estático de forças axiais verificado.

---

### Ficha de Verificação — Questão 39
- **Enunciado Oficial (DOC-00, p. 6):**  
  *"Qual é a expressão analítica da perda de carga ou queda de pressão longitudinal ($\Delta p$) ao longo de um tubo circular de comprimento $L$ em regime laminar (Equação de Hagen-Poiseuille) em função da vazão volumétrica $Q$?"*
- **Gabarito Oficial do Professor (DOC-00, p. 6):**  
  *"A queda de pressão é proporcional à viscosidade e à vazão, e inversamente proporcional à quarta potência do diâmetro:  
  $$\Delta p = \frac{128\,\mu L Q}{\pi D^4}$$"*
- **Evidência nas Fontes:**  
  Questionário P1, p. 6. Substituindo $u_{\max} = \frac{\Delta p R^2}{4\mu L}$ na vazão $Q = \frac{\pi R^2}{2} u_{\max} = \frac{\pi R^4 \Delta p}{8\mu L}$. Com $R = D/2 \implies R^4 = D^4/16$:
  $$Q = \frac{\pi (D^4/16) \Delta p}{8\mu L} = \frac{\pi D^4 \Delta p}{128\mu L} \implies \Delta p = \frac{128\,\mu L Q}{\pi D^4}$$
- **Classificação Principal (Exclusiva):** **`[DEDUÇÃO COMPLEMENTAR]`**  
- **Etiquetas Complementares:** `[COMP]`  
- **Pendência Real:** Nenhuma dúvida matemática.

---

### Ficha de Verificação — Questão 40
- **Enunciado Oficial (DOC-00, p. 6):**  
  *"Pela equação analítica de Hagen–Poiseuille, se o diâmetro do duto for reduzido pela metade ($D/2$), mantendo-se a mesma vazão de água, por quanto multiplica a perda de carga?"*
- **Gabarito Oficial do Professor (DOC-00, p. 6):**  
  *"Como $\Delta p$ é inversamente proporcional à quarta potência do diâmetro ($\Delta p \propto D^{-4}$), ao reduzir o diâmetro pela metade, a perda de carga multiplica por:
  $$\left(\frac{1}{2}\right)^{-4} = 2^4 = 16\text{ vezes}$$"*
- **Evidência nas Fontes:**  
  Questionário P1, p. 6; `44_QUESTÕES_P1_SEM_CÁLCULO.json`. A relação decorre diretamente de $\Delta p = \frac{128\mu LQ}{\pi D^4}$.
- **Alinhamento Pedagógico no Simulado:**  
  No simulado do estudante (`SIMULADO_P1_HIDRODINAMICA.md`), a Questão 4.10 foi estruturada como uma **adaptação conceitual** da Pergunta 40, avaliando diretamente o domínio da lei de proporcionalidade funcional ($\Delta p \propto D^{-4}$) e a sensibilidade física da perda de carga em relação ao diâmetro, sem exigir a realização de contas aritméticas manuais pelo estudante, em perfeita consonância com a diretriz de avaliação puramente teórica e conceitual.
- **Classificação Principal (Exclusiva):** **`[SUPORTE DIRETO]`**  
- **Etiquetas Complementares:** `[CONF]`  
- **Pendência Real:** Nenhuma pendência física; relação de quarta potência confirmada nas fontes e no banco conceitual.

---

## 5. Pontos Finais de Consulta Recomendados para o Estudante com o Professor

1. **Exigência de Dedução Cilíndrica na Folha de Respostas (Q36–Q39):**  
   Consultar o docente se na prova teórica/discursiva será cobrado o desenvolvimento dedutivo formal em coordenadas polares cilíndricas do balanço de cascas fluidas, ou se as questões serão focadas na identificação qualitativa e aplicação direta das expressões do questionário ($u_{\max}=2U$, $\tau(r)$ linear, dependência $D^{-4}$).
2. **Critério de Faixas de Reynolds em Dutos (Q35):**  
   Esclarecer se o docente adota estritamente a convenção do questionário ($Re < 2300$, $2300 \le Re \le 4000$, $Re > 4000$) ou se aceita a menção genérica de $Re_{cr} \cong 2300$ constante na apostila teórica de U2.
3. **Independência de $Re$ na Resistência de Forma Naval (U2 p. 10):**  
   Confirmar se o aluno deve citar a premissa didática da apostila de que a resistência de forma independe de $Re$, diferenciando-a das formulações mais modernas da hidrodinâmica naval (método do fator de forma $1+k$).