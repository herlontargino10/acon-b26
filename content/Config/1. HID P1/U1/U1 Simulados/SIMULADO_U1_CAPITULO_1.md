# Simulado de Hidrodinâmica — Unidade 1

---

### 1ª Questão — Assinale a alternativa correta.

Analise as afirmativas abaixo referentes à equação da continuidade e conservação da massa.

**I.** Na Hidrodinâmica do Navio, os princípios de conservação da massa e da quantidade de movimento são tipicamente empregados.
**II.** A vazão mássica é a taxa de quantidade de fluido por unidade de área que passa por um volume.
**III.** A equação da continuidade aplica-se a qualquer fluido e representa a lei de conservação da massa.
**IV.** Para a água ou o ar tratados como incompressíveis, a densidade absoluta varia significativamente no tempo.
**V.** A conservação da massa é uma lei de conservação local, indicando que uma quantidade de massa não pode ir de um ponto A para um ponto B sem passar pelo espaço intermediário.

**São corretas:**

- (a) I, II e IV.
- (b) I, III e V.
- (c) II, III e IV.
- (d) III, IV e V.
- (e) I, IV e V.

---

### 2ª Questão — Complete as Lacunas

Preencha as lacunas das frases abaixo utilizando os conceitos e termos correspondentes.

1. As três propriedades fundamentais conservadas quando um fluido se move são a massa, a quantidade de movimento e a _________.

2. A grandeza que relaciona a massa de um fluido ao seu volume é a _________ absoluta ou massa específica.

3. A conservação da massa é aplicada a um volume fixo no espaço, de forma arbitrária, chamado de _________.

4. A vazão mássica é definida como a taxa de quantidade de fluido por unidade de _________ que passa por uma face da superfície de controle.

5. O desenvolvimento da conservação da massa no cubo apresenta um sinal negativo que representa a situação física em que existe mais massa _________ do que entrando.

6. A conservação da massa é considerada uma lei de conservação _________, pois a massa não pode simplesmente sumir ou ir de um ponto A para um ponto B sem passar pelo espaço entre eles.

7. A lei de conservação da massa também é conhecida como equação da _________ e se aplica a qualquer fluido.

8. No contexto da Hidrodinâmica do Navio, a água e o ar são tratados como _________, considerando-se a densidade absoluta constante.

9. No balanço da equação para o caso 1D incompressível, a interpretação física é que não pode existir variação de _________ entre a entrada e a saída.

10. Para aplicar a lei de conservação da massa, o foco recai sobre as variações da velocidade no _________, e não simplesmente sobre os valores isolados das velocidades.

---

### 3ª Questão — Verdadeiro ou Falso

Classifique as afirmativas abaixo como Verdadeiras (V) ou Falsas (F).

(  ) 1. A conservação da energia é sempre indicada para os casos mais simples da Hidrodinâmica do Navio.

(  ) 2. A massa de um elemento de fluido pode ser calculada pelo produto entre a massa específica e as dimensões $\Delta x, \Delta y, \Delta z$ do cubo.

(  ) 3. O volume de controle é uma região que se move junto com o fluido pelo espaço, mudando sua forma continuamente.

(  ) 4. A expressão fundamental para calcular a vazão mássica de um escoamento através de uma face é $\dot m = \rho u A$.

(  ) 5. A forma integral da conservação da massa relaciona o fluxo de massa através da superfície com a variação da massa dentro do volume.

(  ) 6. No caso de um fluido incompressível, a equação de conservação da massa em sua forma vetorial simplifica-se para $\nabla \cdot \mathbf{V} = 0$.

(  ) 7. A derivada parcial $\frac{\partial u}{\partial x} > 0$ é interpretada fisicamente no material como massa entrando na direção $x$ do volume de controle.

(  ) 8. No caso 2D incompressível exemplificado no material, a variação da componente de velocidade na direção $x$ é equilibrada pela variação na direção $y$.

(  ) 9. As componentes do vetor velocidade $\mathbf{V}$ nas coordenadas cartesianas $x$, $y$ e $z$ são representadas, respectivamente, por $u$, $v$ e $w$.

(  ) 10. A forma geral da equação da continuidade demonstra que a densidade do fluido nunca participa do balanceamento da massa ao longo do tempo.

---

### 4ª Questão — Múltipla Escolha

Selecione a alternativa correta para cada uma das questões a seguir.

**Questão 4.1.** Sobre a interpretação das derivadas espaciais no contexto da conservação da massa para o caso incompressível, assinale a alternativa correta segundo o material:

(a) A expressão $\frac{\partial v}{\partial y} > 0$ indica que a massa está entrando pela direção $y$.
(b) O foco da análise deve recair no valor absoluto da velocidade no centro do volume de controle.
(c) Quando $\frac{\partial u}{\partial x} = 0$ no caso 1D, significa que o fluido está parado dentro do volume de controle.
(d) No caso 3D incompressível, a variação da componente da velocidade na direção $x$ é equilibrada exclusivamente pela variação na direção $z$.
(e) No caso incompressível, a densidade não aparece nos termos finais da equação da conservação da massa, que passa a ser expressa pelo balanceamento das derivadas espaciais das velocidades locais.

**Questão 4.2.** Considere as afirmações presentes no material sobre a forma integral e diferencial da equação da continuidade. Qual das opções é a representação correta da forma diferencial da continuidade (caso geral)?
(a) $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$
(b) $\nabla \cdot \mathbf{V} = 0$
(c) $\frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} + \frac{\partial(\rho w)}{\partial z} + \frac{\partial\rho}{\partial t} = 0$
(d) $\dot m = \rho u A$
(e) $\iint \rho (\mathbf{V} \cdot \hat n) dA = -\frac{d}{dt} \iiint \rho dVol$

**Questão 4.3.** A respeito do volume de controle abordado no capítulo, assinale a alternativa que descreve corretamente sua finalidade e característica:
(a) Trata-se de uma quantidade fixa de massa que acompanha o escoamento, variando seu tamanho no espaço.
(b) É um volume fixo no espaço, definido de forma arbitrária, através do qual o fluido pode entrar ou sair.
(c) Representa uma superfície fechada hipotética onde a vazão mássica é sempre igual a zero em todas as direções.
(d) É uma região do espaço destinada exclusivamente à análise da variação da temperatura e conservação de energia.
(e) O volume de controle expande-se fisicamente de forma proporcional ao aumento da vazão de saída.

**Questão 4.4.** Ao realizar o balanço inicial de massa no cubo, o material introduz um sinal negativo no desenvolvimento da equação. Assinale a alternativa que explica corretamente a justificativa física para esse sinal:

(a) Ele ocorre porque o vetor velocidade tem sempre sentido oposto à direção da gravidade.

(b) Representa a situação física em que existe mais massa saindo do que entrando, indicando que a massa interna no volume de controle deve diminuir.

(c) Surge devido à característica incompressível do fluido, onde a densidade diminui linearmente com o tempo.

(d) Indica que a vazão de entrada é sempre matematicamente negativa, independentemente da direção real do escoamento.

(e) Ocorre devido a um erro de aproximação que aparece ao se considerar um escoamento estritamente unidirecional (1D).

**Questão 4.5.** No estudo do escoamento 2D incompressível, o balanço de massa resultou na expressão $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$. De acordo com o material, qual é a justificativa para a variação da velocidade associada à direção $x$ aparecer com o sinal negativo?

(a) Porque o eixo $x$ é adotado convencionalmente como negativo na análise de volumes 2D.

(b) Porque a componente $u$ é sempre menor do que a componente $v$ nesse tipo de escoamento.

(c) Porque a normal da superfície aponta em sentido oposto ao da velocidade $u$ na respectiva face de entrada.

(d) Porque a saída de fluido em $y$ anula completamente a entrada em $x$, não restando variação em $z$.

(e) Porque a densidade absoluta varia negativamente ao longo do eixo horizontal de análise.

---

### 5ª Questão — Cálculo de Análise Dimensional

Avalie a dinâmica de comportamento do escoamento da água no interior de um duto circular de diâmetro D, sendo a densidade e a viscosidade da água parâmetros conhecidos.

Considere as variáveis dimensionais do problema como a velocidade $u$, o diâmetro $D$, a viscosidade $\mu$ e a densidade $\rho$.

Utilize o método de Buckingham-Π para determinar o grupo adimensional resultante, estruturando a sua resolução nos seis passos fundamentais.

<br><br>

---

# Gabarito Comentado — Respostas Corretas e Incorretas

### Questão 1 — Marque X

**Resposta correta:** (b) I, III e V.

- **I. Verdadeira:** A seção 1 do material-fonte afirma textualmente que "Na Hidrodinâmica do Navio [...] tipicamente são empregados os princípios de conservação da massa e da quantidade de movimento".
- **II. Falsa:** A seção 5 define que a vazão mássica é a taxa de quantidade de fluido por unidade de *tempo* (e não por área) que passa por uma face.
- **III. Verdadeira:** A seção 13 destaca que a "conservação da massa também é conhecida como equação da continuidade e que ela se aplica a qualquer fluido".
- **IV. Falsa:** A seção 14 estabelece a incompressibilidade exatamente como o caso em que a densidade absoluta é constante ($\frac{\partial \rho}{\partial t} = 0$), ou seja, não varia no tempo.
- **V. Verdadeira:** A seção 7 explica a "conservação local", ressaltando que a massa não pode ir de um ponto A para um ponto B sem passar pelo espaço intermediário.

### Questão 2 — Complete as Lacunas

1. **energia**: A seção 1 apresenta as três leis: massa, quantidade de movimento e energia.
2. **densidade**: A seção 2 define a massa específica como "densidade absoluta ou massa específica".
3. **volume de controle**: A seção 3 nomeia como volume de controle a região "fixa no espaço, de forma arbitrária".
4. **tempo**: A seção 5 define a vazão em relação à unidade de tempo.
5. **saindo** (ou *de saída*): As seções 4 e 8 justificam o sinal negativo na equação pela diminuição de massa no interior do volume quando há mais massa saindo do que entrando.
6. **local**: A seção 7 define a conservação da massa como uma lei de "conservação local", vedando o "teletransporte" da matéria.
7. **continuidade**: A seção 13 relaciona a conservação da massa à "equação da continuidade".
8. **incompressíveis**: A seção 14 trata água e ar como incompressíveis, o que anula a derivada temporal da densidade.
9. **velocidade**: A seção 16 interpreta fisicamente que, no escoamento 1D incompressível, a igualdade de fluxo exige que não haja variação de velocidade ao atravessar o duto.
10. **espaço**: A seção 20 alerta que, nos três casos citados, a ênfase recai nas variações da velocidade no espaço ($\frac{\partial u}{\partial x}$, etc.).

### Questão 3 — Verdadeiro ou Falso

**Sequência correta:** F, V, F, V, V, V, F, V, V, F

- **1. (F) Falsa.** *Correção:* A conservação da energia é indicada para os casos mais *complicados*, onde a temperatura é importante. (Seção 1)
- **2. (V) Verdadeira.** Demonstração explícita da relação massa, densidade e volume do cubo $V=\Delta x\Delta y\Delta z$. (Seção 2)
- **3. (F) Falsa.** *Correção:* O volume de controle é um volume *fixo no espaço*; o fluido é que se move através dele. (Seção 3)
- **4. (V) Verdadeira.** A equação da vazão é textualmente $\dot m = \rho u A$. (Seção 5)
- **5. (V) Verdadeira.** Na seção 12, a forma integral é explicada exatamente relacionando fluxo na superfície à variação de massa no volume interno.
- **6. (V) Verdadeira.** Para casos incompressíveis, $\nabla \cdot \mathbf{V} = 0$. (Seção 14)
- **7. (F) Falsa.** *Correção:* A derivada parcial $\frac{\partial u}{\partial x} > 0$ é interpretada como massa *saindo* na direção $x$. (Seção 15)
- **8. (V) Verdadeira.** No balanço 2D ($-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$), as variações espaciais das componentes se equilibram. (Seção 19)
- **9. (V) Verdadeira.** $u, v, w$ são listadas como as componentes espaciais da velocidade. (Seção 11)
- **10. (F) Falsa.** *Correção:* A forma geral da equação demonstra que a densidade do fluido *participa* do balanceamento de massa através do termo $\frac{\partial\rho}{\partial t}$. Apenas na forma incompressível é que ela deixa de atuar no tempo. (Seções 13 e 14)

### Questão 4 — Múltipla Escolha

**Questão 4.1.** Alternativa correta: **(e)**
- **(a) Incorreta:** $\frac{\partial v}{\partial y} > 0$ indica massa *saindo* por $y$, não entrando (Seção 15).
- **(b) Incorreta:** O foco não é o valor absoluto da velocidade, mas as *variações espaciais* dela (Seção 20).
- **(c) Incorreta:** Em 1D incompressível, a derivada nula significa que não há variação da velocidade entre a entrada e a saída, e não que o fluido está parado (Seção 16).
- **(d) Incorreta:** No 3D incompressível, a variação em $x$ é equilibrada simultaneamente pelas variações em $y$ e $z$, não exclusivamente por $z$ (Seção 18).
- **(e) Correta:** Conforme as seções 14 e 15, no escoamento incompressível a densidade torna-se constante, restando apenas o balanço entre as derivadas espaciais ($\nabla \cdot \mathbf{V} = 0$).

**Questão 4.2.** Alternativa correta: **(c)**
- **(a) Incorreta:** Esta é a forma diferencial incompressível e não a geral.
- **(b) Incorreta:** Esta é a forma vetorial incompressível.
- **(c) Correta:** É a exata forma diferencial geral detalhada nas seções 10 e 13.
- **(d) Incorreta:** Representa a fórmula da vazão mássica individual, e não a lei de continuidade.
- **(e) Incorreta:** Representa a formulação integral, não a diferencial.

**Questão 4.3.** Alternativa correta: **(b)**
- **(a) Incorreta:** Refere-se à abordagem de massa fixa acompanhando o escoamento, que não é a definição do material para volume de controle.
- **(b) Correta:** A seção 3 estipula expressamente que o VC é um volume "fixo no espaço, de forma arbitrária", por onde o fluido flui.
- **(c) Incorreta:** O material detalha escoamentos por faces abertas, contrariando a tese de vazão zero em todas as direções.
- **(d) Incorreta:** Destinado a analisar balanços de massa e momentum, sendo energia reservada para situações termicamente dependentes.
- **(e) Incorreta:** Como é fixo, o VC não sofre expansão física com o fluxo.

**Questão 4.4.** Alternativa correta: **(b)**
- **(a) Incorreta:** A explicação não se refere à ação gravitacional.
- **(b) Correta:** A seção 8 explica claramente que o sinal modela o fenômeno físico em que a massa interna decai se a taxa de saída superar a de entrada.
- **(c) Incorreta:** Fluidos incompressíveis não têm a densidade reduzida linearmente; a densidade ali é constante.
- **(d) Incorreta:** O balanço não fixa a entrada como um valor matematicamente negativo a priori, mas estabelece a relação em fluxo líquido (Seção 4).
- **(e) Incorreta:** Não é aproximação de erro 1D; a regra do sinal abrange a física tridimensional no modelo (Seção 9).

**Questão 4.5.** Alternativa correta: **(c)**
- **(a) Incorreta:** O sinal advém do equacionamento da face estudada, não por o eixo inteiro ser convencionalmente negativo.
- **(b) Incorreta:** O material não pressupõe limites em que a magnitude da velocidade horizontal seja menor do que a vertical.
- **(c) Correta:** A seção 17 detalha exatamente isso: o sinal acopla-se porque o vetor normal aponta no sentido oposto à componente da velocidade ($u$) na janela de entrada.
- **(d) Incorreta:** A variação não é anulada para não restar variação em $z$. Em 2D o duto simplesmente tem balanço fechado nas outras direções.
- **(e) Incorreta:** Num fluido incompressível (citado na alternativa e na questão) a densidade é constante, logo não varia negativamente.

### Questão 5 — Análise Dimensional

**Resolução completa nos seis passos (Baseada na Imagem):**

- **Passo 1:** As variáveis dimensionais do sistema listadas são $u$, $D$, $\mu$, $\rho$. Consequentemente, o número de variáveis é $n = 4$.
- **Passo 2:** As dimensões primárias adotadas para essas variáveis físicas são:
  - Velocidade ($u$): $[L T^{-1}]$
  - Diâmetro ($D$): $[L]$
  - Viscosidade dinâmica ($\mu$): $[M L^{-1} T^{-1}]$
  - Densidade ($\rho$): $[M L^{-3}]$
  As dimensões que constituem as variáveis pertencem aos conjuntos independentes M (massa), L (comprimento) e T (tempo). Logo, o número de dimensões fundamentais é $m = 3$.
- **Passo 3:** O número de grupos adimensionais ($\pi$) que compõem o sistema é estipulado por $n - m$.
  $N_\Pi = 4 - 3 = 1$. Portanto, existirá apenas um grupo adimensional no sistema.
- **Passo 4:** São selecionadas as $m = 3$ variáveis repetitivas e a variável que não se repete. 
  Foram escolhidas $u$, $\mu$ e $\rho$ como variáveis repetitivas. E $D$ como a variável não repetitiva.
- **Passo 5:** O agrupamento Π é estruturado compondo a variável não repetitiva com as repetitivas elevadas a expoentes desconhecidos:
  $\pi_1 = D \rho^a \mu^b u^c$
- **Passo 6:** Determinação dos expoentes igualando as equações das dimensões:
  $[M^0 L^0 T^0] = [L] [M L^{-3}]^a [M L^{-1} T^{-1}]^b [L T^{-1}]^c$
  
  Somando os expoentes das três bases primárias, tem-se a relação unificada:
  $[M^0 L^0 T^0] = [M]^{a+b} [L]^{1 - 3a - b + c} [T]^{-b - c}$
  
  Equacionando os expoentes a 0:
  **M:** $0 = a + b \rightarrow a = -b$
  **T:** $0 = -b - c \rightarrow c = -b$
  **L:** $0 = 1 - 3a - b + c$
  
  Substituindo $a = -b$ e $c = -b$ na expressão de $L$:
  $0 = 1 - 3(-b) - b + (-b)$
  $0 = 1 + 3b - b - b$
  $0 = 1 + b \rightarrow b = -1$
  
  Substituindo o valor numérico para achar $a$ e $c$:
  $a = -(-1) = 1$
  $c = -(-1) = 1$
  
  Alocando os numerais encontrados ao modelo de $\pi_1$:
  $\pi_1 = D^1 \rho^1 \mu^{-1} u^1 = \frac{\rho u D}{\mu}$
  
  *Verificação Final:* As dimensões de $\frac{\rho u D}{\mu}$ provam que é de fato um conjunto adimensional, pois cancelam completamente os fatores: $[(M L^{-3})(L T^{-1})(L)] / [M L^{-1} T^{-1}] = 1$. O grupo corresponde exatamente ao Número de Reynolds ($Re$).
