# Simulado de Hidrodinâmica — Unidade 1

**Instruções Gerais:**
- Este simulado avalia os conceitos do Capítulo 1: Leis de Conservação e Conservação da Massa.
- Leia atentamente todas as questões.
- Responda com base no material estudado.

---

### 1ª Questão — Marque X

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

