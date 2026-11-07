___

## O Princípio da Homogeneidade e Análise Dimensional

### 1. Por que estudar Análise Dimensional?
O estudo da análise dimensional se justifica pois as equações de conservação na forma diferencial (aplicadas a problemas como as forças atuantes sobre o casco, o propulsor e o leme do navio) são muito complexas e não lineares, impossibilitando uma resolução analítica de solução única.

Isso força a necessidade de testes experimentais reais ou numéricos através da CFD (Computational Fluid Dynamics). A análise dimensional surge como a ferramenta natural para intermediar a inter-relação entre experimento e teoria, permitindo prever o comportamento do navio em escala real a partir de ensaios com modelos em tanques físicos.

### 2. Dimensão, unidade e sistemas dimensionais

> [!NOTE] O que significa fisicamente?
> A **dimensão** é a medida de uma quantidade física, enquanto a **unidade de medida** é apenas a forma de atribuir um número a essa dimensão. Por exemplo: comprimento é a dimensão, e o metro é a unidade.

> ⚠️ **ÊNFASE DO PROFESSOR — PROVA**
> O professor destacou este ponto durante a aula. Exemplo enfatizado: diferenciar variável dimensional (ex: dimensão de comprimento) e sua unidade (ex: metros).

Existem 7 dimensões primárias (ou fundamentais/básicas). No entanto, para a **hidrodinâmica do navio**, apenas 3 dimensões básicas são estritamente necessárias, atuando como parâmetros de escala globais do problema:
- Massa ($M$)
- Comprimento ($L$)
- Tempo ($T$)

> ⚠️ **ÊNFASE DO PROFESSOR — PROVA**
> O sistema MLT (massa, comprimento e tempo) foi explicitamente destacado como fundamental para a prova.

A fonte também cita a existência do sistema $FLT$ (Força-Comprimento-Tempo), onde a força assume o papel primário no lugar da massa.

### 3. Lei da Homogeneidade Dimensional
A Lei da Homogeneidade Dimensional postula que **todo termo aditivo de uma equação deve obrigatoriamente possuir as mesmas dimensões**.

Ao dividir cada termo da equação por uma coleção de variáveis e constantes cujo produto detenha as mesmas dimensões, a equação se transforma em uma **equação adimensional** (os termos perdem as unidades e tornam-se adimensionais).

> [!IMPORTANT] O que não confundir?
> Se, além de a equação ser adimensionalizada, os termos resultantes forem da *ordem de unidade*, a equação adquire o status de **normalizada**. A normalização é uma condição matemática mais restritiva do que a simples adimensionalização.

### 4. Força de inércia
A força de inércia opera como a base para avaliar e normalizar as demais forças na mecânica dos fluidos. A sua construção nasce a partir da relação com a energia cinética ($K_e$).

A energia cinética da partícula é expressa como:
$$ K_e \cong m u^2 $$
Como a energia também pode ser compreendida através da relação de força vezes distância ($K_e = F \cdot L$), a força de inércia a ser vencida para parar totalmente uma partícula dentro de uma distância $L$ será:
$$ F_{inércia} = \frac{mu^2}{L} = \frac{\rho u^2 L^3}{L} = \rho u^2 L^2 $$

> [!TIP] Como interpretar a fórmula?
> Na obtenção de $F_{inércia} = \rho u^2 L^2$, a grandeza $\rho$ é a densidade, e $u$ representa a velocidade. Fisicamente, essa equação representa que quanto mais densa for a partícula ou maior for sua velocidade, mais difícil será pará-la na distância de referência $L$.

### 5. Números adimensionais
Os parâmetros adimensionais originam-se em hidrodinâmica quando comparamos a Força de Inércia contra as outras forças que compõem o escoamento.

#### 5.1 Número de Euler ($Eu$)
O Número de Euler demonstra a relação comparando a **Força de Pressão versus a Força de Inércia**.
- **O que significa fisicamente?** O $Eu$ atua como a adimensionalização natural da força de pressão.
- **Aplicações na fonte:** Tem efeito dominante nas forças de sustentação e no arrasto induzido presente no casco do navio. É essencial para a teoria de manobra do navio e aerodinâmica. Em propulsores, nas situações envolvendo escoamentos próximos à cavitação, passa a ser conhecido como índice de cavitação.

**Dedução:**
Derivando as forças de pressão para isolamento:
$$ \Delta p = \frac{F}{A} = \frac{F}{L^2} \rightarrow F_{pressão} = \Delta p L^2 $$
Normalizando essa força de pressão obtida contra a força de inércia base ($F_{inércia} = \rho {V_0}^2 L^2$):
$$ \frac{F_{pressão}}{F_{inércia}} = \frac{\Delta p L^2}{\rho {V_0}^2 L^2} = \frac{\Delta p}{\rho {V_0}^2} $$
Chega-se ao Número de Euler:
$$ Eu = \frac{\Delta p}{\rho {V_0}^2} $$

### Pergunta destacada pelo professor
**"O que é cavitação?"**
**Resposta no PDF:** parcialmente desenvolvida na fonte. O PDF cita que em escoamentos próximos à cavitação o Número de Euler atua como índice de cavitação, mas não desenvolve profundamente o conceito físico em si do que é cavitação.
[INDICAÇÃO DO PROFESSOR — REQUER CONFIRMAÇÃO/COMPLEMENTO]

#### 5.2 Número de Reynolds ($Re$)
O Número de Reynolds descreve a relação da **Força de Inércia versus a Força Viscosa**.
- **O que significa fisicamente?** Governa a maioria dos fenômenos da mecânica dos fluidos, indicando a importância relativa entre a inércia do fluido e a viscosidade que freia o movimento.
- **Aplicações na fonte:** Determina a transição entre o regime laminar e o regime turbulento nos escoamentos. O PDF apresenta o experimento clássico de Reynolds utilizando o traço de um corante ("dye filament") que demonstra visualmente quando o regime muda de laminar para turbulento. Em dutos comerciais, a transição ocorre em torno de $(Re_D)_{cr} \cong 2,3 \times 10^3$. Em escalas muito altas ($Re \approx 10^9$ ocorrentes na manobra de navios reais), as forças de inércia dominam, e as forças viscosas podem ser negligenciadas.

### Perguntas destacadas pelo professor sobre escoamento e atrito:
**"O fluido tem cisalhamento, por que?"**
**"Posso ter atrito entre líquidos?"**
**"Posso ter cisalhamento entre líquidos?"**
**Resposta no PDF:** parcialmente desenvolvida na fonte. O material cita a lei da viscosidade de Newton e que a tensão de cisalhamento resulta em força viscosa (atrito interno que freia o movimento), mas a explicação mais detalhada do mecanismo físico sobre como ocorre o escoamento e o porquê o fluido tem cisalhamento não é plenamente expandida.
[INDICAÇÃO DO PROFESSOR — REQUER CONFIRMAÇÃO/COMPLEMENTO]

**Dedução:**
A fonte estabelece que as forças viscosas seguem a lei da viscosidade de Newton, onde a tensão de cisalhamento ($\tau$) sobre uma área resulta em força viscosa:
$$ \tau = \frac{F_{viscosa}}{A} \rightarrow F_{viscosa} = \tau A $$
Sabendo que $\tau = \mu \frac{\Delta u}{\Delta y}$, deduzimos $F_{viscosa} = \left(\mu \frac{\Delta u}{\Delta y}\right) A$.
Traduzindo dimensionalmente ($\Delta u \rightarrow u$, $\Delta y \rightarrow L$ e $A \rightarrow L^2$):
$$ F_{viscosa} = \mu \frac{u L^2}{L} = \mu u L $$
Normalizando a inércia sobre a viscosidade:
$$ \frac{F_{inércia}}{F_{viscosa}} = \frac{\rho u^2 L^2}{\mu \frac{V_0 L^2}{L}} = \frac{\rho u L}{\mu} $$
Resultando na equação do Número de Reynolds:
$$ Re = \frac{\rho u L}{\mu} $$

#### 5.3 Número de Froude ($Fr$)
O Número de Froude exprime a relação comparando **Forças de Inércia versus Forças Gravitacionais**.
- **O que significa fisicamente?** O Froude governa os escoamentos em que a superfície livre é deformada pela gravidade.
- **Aplicações na fonte:** Tem efeito dominante na formação de ondas de superfície, em canais abertos e determina grande parte da resistência em navios. As figuras do material ilustram como as ondas na superfície podem interagir e se somar ("waves reinforce each other") ou se anular ("waves cancel out") dependendo do número de Froude.

**Dedução:**
As forças físicas correspondentes à atração da gravidade exercem peso sobre o volume:
$$ F_{gravidade} = mg = \rho \cdot Vol \cdot g = \rho L^3 g $$
Efetuando a normalização divisória:
$$ \frac{F_{inércia}}{F_{gravidade}} = \frac{\rho {V_0}^2 L^2}{\rho L^3 g} = \frac{{V_0}^2}{g L} $$
O material adota a raiz do termo analítico como a representação tradicional:
$$ Fr = \sqrt{\frac{{V_0}^2}{gL}} = \frac{V_0}{\sqrt{gL}} $$

### Ênfase do professor — Reynolds e Froude
**Pergunta destacada:** **"Por que Reynolds e Froude são importantes na engenharia?"**
**Resposta baseada no PDF:** Reynolds é fundamental na engenharia porque governa a transição entre regime laminar e turbulento e determina a resistência friccional (atrito). Froude é importante porque governa a formação de ondas de superfície e determina a resistência de formação de ondas, aspectos críticos para a operação de navios e resistência do casco.

#### 5.4 Número de Weber ($Wn$)
O Número de Weber estabelece a proporção entre **Forças de Inércia versus Forças de Tensão Superficial**.
- **O que significa fisicamente?** Relaciona-se com forças intermoleculares de coesão que formam uma fina membrana na interface dos fluidos.
- **Aplicações na fonte:** Importante no estudo da interface gás-líquido, na formação de spray, gotas e bolhas.

**Dedução:**
A força a ser superada originada da tensão superficial é:
$$ F_{superf} = \sigma L $$
Promovendo a relação analítica comparada contra a inércia:
$$ \frac{F_{inércia}}{F_{superf}} = \frac{\rho u^2 L^2}{\sigma L} = \frac{\rho u^2 L}{\sigma} $$
Alcançando a unificação final como Número de Weber ($Wn$):
$$ Wn = \frac{\rho u^2 L}{\sigma} $$

---

### 6. Análise Dimensional e o Teorema $\pi$ de Buckingham

A análise dimensional é o método prático base para compactar o número de variáveis que afetam o fenômeno.

**Finalidades:**
1. Gerar parâmetros adimensionais que auxiliam na solução do problema.
2. Obter leis de escala para prever o desempenho do protótipo a partir de um modelo em tanque.
3. Prever tendências de variação entre os parâmetros.

#### O Teorema $\pi$ de Buckingham (1914)
> ⚠️ **ÊNFASE DO PROFESSOR — PROVA**
> O Teorema $\pi$ de Buckingham foi expressamente indicado pelo professor como assunto da prova!

Este teorema declara que as leis da física não dependem de um sistema específico de unidades. Qualquer lei física pode ser expressa utilizando apenas combinações adimensionais formadas pelas variáveis ligadas à lei (os grupos $\pi s$).

**A Regra da Redução de Buckingham ($j = n - k$):**
A quantidade de agrupamentos $\pi s$ resultantes da análise é igual ao número máximo de variáveis que não formam um $\pi$ entre si, e é sempre menor ou igual ao número de dimensões fundamentais da análise.
Na equação, $n$ representa o total de variáveis do problema, e $k$ (ou $m$) representa as dimensões primárias operantes.

**As Seis Etapas do Procedimento de Buckingham:**
> ⚠️ **ÊNFASE DO PROFESSOR — PROVA**
> O passo a passo das etapas envolvidas no teorema, incluindo a listagem inicial das variáveis, foram destacados para a prova.

1. Liste as variáveis dimensionais do problema e conte-as ($n$), certificando-se de que são independentes.
2. Liste as dimensões primárias presentes nessas variáveis ($m$). Na hidrodinâmica naval, tipicamente $M, L, T$.
3. Descubra o número de agrupamentos adimensionais da análise calculando $\pi s = n - m$.
4. Escolha as variáveis repetidas.
5. Gere os $\pi s$ agrupando os parâmetros com o uso de expoentes algébricos.
6. Determine o valor de cada expoente aplicando a condição de homogeneidade dimensional, assumindo os expoentes zero no lado esquerdo do grupo.

### Ênfase do professor — Arqueação Bruta (AB)
A anotação do professor trouxe um exemplo expresso no quadro relacionado a Arqueação Bruta:
$$ AB = K \cdot V $$
A anotação indica $V$ em $m^3$ e associa $K$ à dimensão/unidade de $1/m^3$.
Expressão anotada pelo professor durante a aula — requer confirmação.
**Resposta no PDF:** não consta no PDF (exemplo exclusivo da aula e requer complementação quanto à sua implicação).
[INDICAÇÃO DO PROFESSOR — REQUER CONFIRMAÇÃO/COMPLEMENTO]

---

### 7. Exemplo de Euler
A resolução matemática a seguir, oriunda da fonte, mostra as seis etapas em funcionamento.

Consideramos 4 varáveis: $\Delta p, u, \rho, L$ ($n = 4$). Sendo as dimensões básicas $m = 3$ ($M, L, T$).
O número de grupos será $\pi_1 = 4 - 3 = 1$.
Variável não repetida: $\Delta p$.
Variáveis repetidas: $u, \rho, L$.
Montamos o grupo $\pi_1$:
$$ \pi_1 = \Delta p u^a \rho^b L^c $$
Para que o sistema seja adimensional, substituímos com as dimensões:
$$ [M^0 L^0 T^0] = [ML^{-1}T^{-2}] [LT^{-1}]^a [ML^{-3}]^b [L]^c $$
Combinando os expoentes agrupados das grandezas equivalentes:
$$ [M^0 L^0 T^0] = [M]^{1+b} [L]^{-1+a-3b+c} [T]^{-2-a} $$
Montando o sistema dimensional M, L, T:
M:
$0 = 1 + b \rightarrow b = -1$
T:
$0 = -2 - a \rightarrow a = -2$
L:
$0 = -1 + a - 3b + c$
Ao substituir as raízes na equação L, obtém-se $c = 0$.
A substituição algébrica dos expoentes leva a:
$$ \pi_1 = \Delta p u^{-2} \rho^{-1} L^0 $$
E, finalmente:
$$ \pi_1 = Eu = \frac{\Delta p}{\rho {V_0}^2} $$

**Interpretação física:**
O que esse cálculo está fazendo? O método combinou as quatro variáveis listadas de tal forma que as dimensões primárias (M, L e T) se cancelassem perfeitamente, gerando um número sem unidade. O resultado prático é a formação algébrica exata do Número de Euler, provando a relação unificada adimensional entre força de pressão e inércia.

---

### 8. Exemplo de Reynolds no Duto

Este exemplo avalia o escoamento no interior de um duto circular de diâmetro de referência $D$.

O problema lista $n=4$ variáveis: $u, D, \mu, \rho$.
Com $m = 3$ dimensões fundamentais, obteremos apenas 1 grupo adimensional ($\pi_1$).
A matriz se estrutura da seguinte forma:
$$ \pi_1 = D \rho^a \mu^b u^c $$
Substituindo com as dimensões conhecidas:
$[D] = [L]$
$[\rho] = [ML^{-3}]$
$[\mu] = [ML^{-1}T^{-1}]$
$[u] = [LT^{-1}]$
Exigindo a condição adimensional do lado esquerdo do grupo $\pi$:
$$ [M^0 L^0 T^0] = [L] [ML^{-3}]^a [ML^{-1}T^{-1}]^b [LT^{-1}]^c $$
Montando o sistema apresentado pela fonte:
M:
$0 = a + b \rightarrow a = -b$
L:
$0 = 1 - 3a - b + c$
T:
$0 = -b - c \rightarrow c = -b$
Efetuando a substituição algébrica na equação L:
$$ 1 - 3(-b) - b + (-b) = 0 $$
$$ 1 + 3b - b - b = 0 $$
A resolução determina:
$$ \rightarrow b = -1 $$
E com isso, o restante do sistema retorna:
$$ \rightarrow a = 1 $$
$$ \rightarrow c = 1 $$
Substituindo de volta na equação original inicial:
$$ \pi_1 = D \rho^1 \mu^{-1} u^1 = \frac{\rho u D}{\mu} = Re $$

#### Interpretação física
O que esse agrupamento representa? A fonte demonstrou que, ao agrupar matematicamente as variáveis puras atuando no tubo ($u, D, \mu, \rho$) sob a lei de Buckingham, a matriz resultou exatamente na formação matemática do Número de Reynolds. A relação exprime diretamente a oposição das forças de inércia e forças viscosas no modelo do duto circular.

---

### 9. Resistências na Hidrodinâmica do Navio
Organizando as incógnitas de arrasto em torno do casco, a avaliação laboratorial do navio necessita cobrir **as 7 variáveis dimensionais**: Resistência de Forma ($R_{forma}$), densidade da água ($\rho$), viscosidade dinâmica ($\mu$), velocidade ($U$), comprimento ($L$), gravidade ($g$), e a tensão superficial ($\sigma$).

Como listamos $n=7$ variáveis adentrando o cálculo de Buckingham (onde $m=3$), o método originará matematicamente $4$ grupos $\pi s$. As deduções resultantes explicitadas na fonte são:

- **$\pi_1$ (Arrasto de Forma):**
$$ \pi_1 = \frac{R_{forma}}{\rho L^2 U^2} $$
*(Nota textual da fonte: "este coeficiente é conhecimento [conhecido] como coeficiente de arrasto").*

- **$\pi_2$ (Atrito/Reynolds):**
$$ \pi_2 = \frac{\mu}{\rho L U} = Re^{-1} $$

- **$\pi_3$ (Ondas/Froude):**
$$ \pi_3 = \frac{g L}{U^2} = Fr^{-2} $$

- **$\pi_4$ (Capilaridade/Weber):**
$$ \pi_4 = \frac{\sigma}{\rho L U^2} = We^{-1} $$

> [!IMPORTANT] Conclusão do Professor sobre as Resistências
> Analisando o $\pi_1$ em oposição ao $\pi_2$, a aula estabelece categoricamente a lição estrutural de resistência hidrodinâmica: **A resistência friccional é dependente do número de Reynolds, enquanto a resistência de forma (form drag net, viscous pressure resistance), conforme apresentada na fonte, não é dependente do número de Reynolds.**

Para representar isso visualmente, a fonte descreve o gráfico *"Reynolds number dependence of section drag"*. O gráfico plota o coeficiente de arrasto, $C_D$, em função de $8 \log R_n$. As curvas ilustram o comportamento para um cilindro circular ("Circular cylinder") e para fatias progressivas de espessura de asa de 6%, 12% e 25%. Essa referência gráfica também inclui indicações demarcadoras de placa laminar ("Laminar plate") e placa turbulenta ("Turbulent plate"), evidenciando onde ocorrem as transições operacionais do arrasto dependentes da variação no número de Reynolds.

---

### 10. Similaridade
> ⚠️ **ÊNFASE DO PROFESSOR — PROVA**
> O fator de escala de modelo (escalonamento) foi expressamente listado pelo professor para a prova!

Ao testar navios reduzidos em laboratório, é obrigatório utilizar três similaridades simultâneas estruturais de extrapolação:

#### Similaridade Geométrica (Geosim)
Exige exatamente a mesma forma e proporções entre o modelo pequeno e o protótipo gigante, devendo haver correspondência completa nos pontos homólogos.
*Observação Visual da Fonte:* O PDF exibe figuras com perfis homólogos, indicando pontos $a$ e $a'$ correspondentes na mesma proporção geométrica de escalonamento. A fonte nota apenas uma exceção de limitação técnica: a rugosidade da chapa de aço do casco real não é perfeitamente miniaturizada e escalonável na água, exigindo ajustes empíricos.

#### Similaridade Cinemática
Acontece quando há correspondência proporcional exata das velocidades ao longo das áreas do modelo e protótipo, ocorrendo nos mesmos pontos homólogos em tempos homólogos.
*Observação Visual da Fonte:* Observando a gravura ilustrativa apresentando os fluxos em volta das esferas testadas, o estudante visualiza que os vetores de direção no modelo exibem um fator de proporcionalidade decrescente e contínuo da velocidade referente ao protótipo real.

#### Similaridade Dinâmica
Requisito teórico que estabelece que todas as forças de diversas naturezas aplicadas e operantes mantenham total correspondência proporcional nos vetores, preservando direção e sentido iguais entre as duas escalas do teste.

---

### 11. O Dilema da Similaridade
Este dilema relata a impossibilidade experimental laboratorial em piscinas de prova. A fonte deduz matematicamente que tentar satisfazer Reynolds simultaneamente à Igualdade de Froude causa falha experimental de fluidez laboratorial.

**1. Modelo e protótipo (Fator de Escala):**
O ensaio baseia a dimensão laboratorial com o escalar de tamanho $\alpha$:
$$ L_m = L_p \alpha $$

**2. Igualdade de Froude:**
Testando barcos em superfície livre com gravidade, é obrigatório reproduzir corretamente a geração de onda. Assim, o laboratório impõe a obrigação e fixa que $Fr_m = Fr_p$:
$$ \frac{{V_m}^2}{g L_m} = \frac{{V_p}^2}{g L_p} $$

**3. Obtenção das Velocidades ($V_m/V_p$):**
Isolando os elementos do Froude igualado, a velocidade de tração do experimento da máquina atinge:
$$ \frac{{V_m}^2}{{V_p}^2} = \frac{L_m}{L_p} \rightarrow \frac{V_m}{V_p} = \sqrt{\alpha} $$

**4. Relação Temporal ($T_m/T_p$):**
A correspondência de tempo inerente da cinemática obedece ao percurso das distâncias base:
$$ \frac{T_m}{T_p} = \frac{L_m/V_m}{L_p/V_p} = \frac{\alpha}{\sqrt{\alpha}} = \sqrt{\alpha} $$

**5. Tentativa de Impor Igualdade de Reynolds:**
Sabendo que o atrito também existe, o laboratório tenta simultaneamente estabelecer a premissa de equivalência viscosa impondo $Re_m = Re_p$.

**6. Obtenção da Viscosidade Resultante:**
Para manter Reynolds associado à exata velocidade de laboratório forçada do cálculo anterior ($V_m/V_p = \sqrt{\alpha}$), as variáveis exigem a seguinte correspondência na taxa cinemática viscosa operante do teste:
$$ \frac{V_m L_m}{\nu_m} = \frac{V_p L_p}{\nu_p} \rightarrow \frac{\nu_m}{\nu_p} = \frac{L_m V_m}{L_p V_p} = \alpha \cdot \sqrt{\alpha} = \alpha^{3/2} $$

**7. O Exemplo de Redução 1:10:**
A fonte submete um exemplo de dimensão laboratorial assumindo que o teste utilizará proporção escalar $\alpha = 0,1$.

**8. O Resultado de Compatibilidade Viscosa:**
Submetendo esse exemplo na relação estipulada de Reynolds da piscina, encontramos a absurda taxa $\alpha^{3/2} = 0,032$.

**9. Conclusão Apresentada (A Impossibilidade de Reynolds):**
A explicação física é clara: "Se o modelo precisa reproduzir corretamente os efeitos gravitacionais das ondas, sua velocidade precisa seguir a escala de velocidade ditada pelo Froude ($\sqrt{\alpha}$). Mas essa velocidade e a redução de comprimento alteram o comportamento natural de atrito de Reynolds. Para manter Reynolds também igual, o cálculo provou que seria necessário um fluido laboratorial exótico possuindo uma viscosidade equivalente a apenas 0,032 da normal." Como nem mesmo elementos caros como mercúrio atingem tais viscosidades exigidas sem prejuízos (tendo apenas em torno de 1/9 da equivalência comparada na água na vida real), os ensaios práticos operam e persistem operando em água comum. Logo, o teste impõe a conclusão final: na prática, a água é usada tanto para o modelo quanto para o protótipo, e a similaridade do número de Reynolds é inevitavelmente violada para que o número de Froude seja mantido constante de modo a dominar sobre os fenômenos de superfície livre.

---

> [!WARNING] Inconsistências da Fonte
> A transcrição didática base do PDF original exibe inconsistências visuais recorrentes relativas à falha do software gerador original na omissão contínua da partícula "ti". Faltam sílabas transcrevendo palavras para "quandade", "sica" (física), "cinéca" ou "parcula". Além de desvios textuais originais (ex: "este coeficiente é conhecimento como"), mantidos por fidelidade e registro da fonte original laboratorial de aula. Ocorreu também na formulação de deduções originais a troca silenciosa de notação por parte da prancheta autoral da aula entre $u$ e $V_0$ assumindo equivalência de referencial, que foi conservada inalterada neste rascunho de estudos de mecânica fluidodinâmica.

---

# Ênfases do Professor para a Prova

## Perguntas conceituais
- **Por que Reynolds e Froude são importantes na engenharia?** [PARCIALMENTE NO PDF]
- **O fluido tem cisalhamento, por que?** [PARCIALMENTE NO PDF]
- **Posso ter atrito entre líquidos?** [PARCIALMENTE NO PDF]
- **Posso ter cisalhamento entre líquidos?** [PARCIALMENTE NO PDF]
- **O que é cavitação?** [NÃO CONSTA/INSUFICIENTE NO PDF]

## Procedimentos
- **Teorema de Buckingham** [CONSTA NO PDF]
- **Passo a passo das etapas envolvidas** [CONSTA NO PDF]
- **Listagem das variáveis** [CONSTA NO PDF]
- **Sistema MLT (massa, comprimento e tempo)** [CONSTA NO PDF]
- **Exemplo de variável dimensional x unidade** [CONSTA NO PDF]
- **Fator de escala de modelo** [CONSTA NO PDF]

## Exercícios/expressões destacados
- **Expressão envolvendo Arqueação Bruta:** $AB = K \cdot V$ (onde $V$ foi indicado em $m^3$) [NÃO CONSTA/INSUFICIENTE NO PDF]
- **Indicação associada a $K$:** dimensão/unidade anotada como $1/m^3$ (expressão anotada pelo professor durante a aula — requer confirmação) [NÃO CONSTA/INSUFICIENTE NO PDF]
