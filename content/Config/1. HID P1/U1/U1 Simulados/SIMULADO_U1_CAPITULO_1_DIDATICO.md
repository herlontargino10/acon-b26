# Simulado de Hidrodinâmica — Unidade 1

---

### 1ª Questão — Assinale a alternativa correta.
Analise as afirmativas abaixo sobre a equação da continuidade e a conservação da massa.

**I.** Na Hidrodinâmica do Navio, utilizamos principalmente os princípios de conservação da massa e da quantidade de movimento.
**II.** A vazão mássica é a quantidade de fluido por unidade de área que passa por um volume.
**III.** A equação da continuidade vale para qualquer fluido e representa a conservação da massa.
**IV.** Para água e ar tratados como incompressíveis, a densidade absoluta varia muito com o tempo.
**V.** A conservação da massa é uma lei local, o que significa que a massa não pode ir de um ponto A para um B sem passar pelo espaço entre eles (não há "teletransporte").

**São corretas:**
- (a) I, II e IV.
- (b) I, III e V.
- (c) II, III e IV.
- (d) III, IV e V.
- (e) I, IV e V.

---

### 2ª Questão — Complete as Lacunas
Preencha as lacunas das frases abaixo utilizando os conceitos e termos correspondentes.

1. Quando um fluido se move, três propriedades fundamentais se conservam: a massa, a quantidade de movimento e a _________.
2. A grandeza que relaciona a massa de um fluido ao volume que ele ocupa é a _________ (ou massa específica).
3. A conservação da massa é aplicada a uma região fixa no espaço escolhida para análise, chamada de _________.
4. A vazão mássica é a quantidade de fluido por unidade de _________ que atravessa uma superfície.
5. No balanço de massa do cubo, o sinal negativo indica a situação em que há mais massa _________ do que entrando, diminuindo a massa interna.
6. A conservação da massa é uma lei de conservação _________, pois a massa não "teletransporta" de um ponto a outro.
7. A lei de conservação da massa também é chamada de equação da _________ e vale para qualquer fluido.
8. Na Hidrodinâmica do Navio, a água e o ar são tratados como fluidos _________, ou seja, com densidade constante.
9. No balanço do escoamento unidirecional (1D) incompressível, a interpretação física é que não pode haver variação da _________ entre a entrada e a saída.
10. Ao aplicar a conservação da massa, o que importa são as variações da velocidade no _________, e não os valores isolados das velocidades.

---

### 3ª Questão — Verdadeiro ou Falso
Classifique as afirmativas abaixo como Verdadeiras (V) ou Falsas (F).

(  ) 1. A conservação da energia é a mais usada nos casos simples da Hidrodinâmica do Navio.
(  ) 2. Podemos calcular a massa de um elemento de fluido multiplicando sua massa específica pelo volume do cubo ($\Delta x \cdot \Delta y \cdot \Delta z$).
(  ) 3. O volume de controle se move junto com o fluido e muda de forma o tempo todo.
(  ) 4. A vazão mássica que passa por uma face é calculada pela fórmula $\dot m = \rho u A$.
(  ) 5. A forma integral da conservação da massa relaciona o fluxo de massa que passa pela superfície com a variação de massa dentro do volume.
(  ) 6. Para um fluido incompressível, a conservação da massa na forma vetorial fica simplificada como $\nabla \cdot \mathbf{V} = 0$.
(  ) 7. A derivada $\frac{\partial u}{\partial x} > 0$ significa que a massa está entrando na direção $x$ do volume de controle.
(  ) 8. No exemplo 2D incompressível do resumo, a variação da velocidade na direção $x$ é equilibrada pela variação na direção $y$.
(  ) 9. As velocidades nas direções $x$, $y$ e $z$ são representadas pelas letras $u$, $v$ e $w$, respectivamente.
(  ) 10. A forma geral da equação da continuidade mostra que a densidade do fluido nunca importa no balanço de massa ao longo do tempo.

---

### 4ª Questão — Múltipla Escolha
Selecione a alternativa correta para cada uma das questões a seguir.

**Questão 4.1.** Sobre as derivadas espaciais na conservação da massa para fluidos incompressíveis, assinale a alternativa correta:
(a) A expressão $\frac{\partial v}{\partial y} > 0$ indica que a massa está entrando na direção $y$.
(b) O mais importante é saber o valor absoluto da velocidade no centro do volume.
(c) Quando $\frac{\partial u}{\partial x} = 0$ no caso 1D, quer dizer que o fluido está parado.
(d) No caso 3D incompressível, a variação da velocidade na direção $x$ é equilibrada apenas pela direção $z$.
(e) No fluido incompressível, a densidade é constante e não aparece na equação final, que vira apenas um balanço das variações espaciais das velocidades.

**Questão 4.2.** Qual é a forma diferencial geral (para qualquer fluido) da equação da continuidade?
(a) $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$
(b) $\nabla \cdot \mathbf{V} = 0$
(c) $\frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} + \frac{\partial(\rho w)}{\partial z} + \frac{\partial\rho}{\partial t} = 0$
(d) $\dot m = \rho u A$
(e) $\iint \rho (\mathbf{V} \cdot \hat n) dA = -\frac{d}{dt} \iiint \rho dVol$

**Questão 4.3.** O que é o volume de controle?
(a) Uma quantidade de massa que viaja com o escoamento, mudando de tamanho.
(b) Uma região fixa no espaço, escolhida de forma arbitrária, por onde o fluido entra e sai.
(c) Uma superfície fechada imaginária onde não passa nenhuma vazão.
(d) Um espaço usado apenas para calcular a conservação de energia e temperatura.
(e) Um volume que aumenta de tamanho físico conforme a vazão de saída cresce.

**Questão 4.4.** Por que o balanço de massa no cubo usa um sinal negativo?
(a) Porque a velocidade sempre vai contra a gravidade.
(b) Para indicar que, se sair mais massa do que entrar, a quantidade de massa dentro do volume vai diminuir.
(c) Porque em fluidos incompressíveis a densidade diminui com o tempo.
(d) Porque a vazão de entrada é sempre um número negativo na matemática.
(e) É um erro de aproximação que só acontece no escoamento em uma direção (1D).

**Questão 4.5.** No escoamento 2D incompressível, temos a expressão $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$. Por que a variação na direção $x$ ganha um sinal negativo?
(a) Porque o eixo $x$ é sempre negativo em problemas 2D.
(b) Porque a velocidade $u$ é sempre menor que a velocidade $v$.
(c) Porque a normal (seta perpendicular) da superfície de entrada aponta no sentido contrário ao da velocidade $u$.
(d) Porque a saída em $y$ cancela a entrada em $x$, então não sobra nada para $z$.
(e) Porque a densidade diminui ao longo do eixo horizontal.

---

### 5ª Questão — Cálculo de Análise Dimensional
Vamos analisar o escoamento de água dentro de um tubo circular de diâmetro $D$. Sabemos a densidade ($\rho$) e a viscosidade ($\mu$) da água.
As variáveis dimensionais são a velocidade $u$, o diâmetro $D$, a viscosidade $\mu$ e a densidade $\rho$.
Usando o método de Buckingham-Π, determine o grupo adimensional do problema. Mostre a resolução seguindo os seis passos fundamentais.

<br><br>

---

# Gabarito Comentado — Respostas Corretas e Incorretas

### Questão 1 — Marque X

**Resposta correta:** (b) I, III e V.

- **O que a questão está perguntando:** Pede para identificar as afirmações verdadeiras sobre os conceitos básicos de conservação da massa e equação da continuidade com base no resumo.
- **Explicação passo a passo:** 
  - A afirmativa **I é correta**, pois a Hidrodinâmica do Navio foca principalmente na conservação da massa e da quantidade de movimento. A energia fica para casos com variação de temperatura.
  - A afirmativa **III é correta**, pois a conservação da massa e a equação da continuidade são sinônimos e valem para qualquer fluido.
  - A afirmativa **V é correta**. A lei é local, ou seja, a massa precisa passar pelo espaço entre dois pontos e não se "teletransporta".
- **Por que as demais erradas:** 
  - A afirmativa II está errada porque a vazão mássica é a taxa por unidade de *tempo*, não por área.
  - A afirmativa IV está errada porque, para fluidos incompressíveis (como água e ar nesse contexto), a densidade é constante e *não* varia no tempo.
- **O que lembrar:** Em fluidos incompressíveis, a densidade ($\rho$) é constante no tempo e no espaço. Vazão mássica envolve tempo.

### Questão 2 — Complete as Lacunas

1. **energia** (São três leis: massa, quantidade de movimento e energia).
2. **densidade** (ou densidade absoluta/massa específica).
3. **volume de controle** (A região fixa analisada).
4. **tempo** (A definição de vazão mássica é quantidade de fluido por unidade de tempo).
5. **saindo** (Se sai mais do que entra, a massa lá dentro diminui, daí o sinal de menos).
6. **local** (A massa não se teletransporta, precisa fluir pelo espaço).
7. **continuidade** (Conservação da massa = equação da continuidade).
8. **incompressíveis** (Densidade constante = fluido incompressível).
9. **velocidade** (Em 1D incompressível, a velocidade de entrada precisa ser igual à de saída, logo a variação é zero).
10. **espaço** (O foco das derivadas $\frac{\partial u}{\partial x}$, etc., é a variação da velocidade ao longo do espaço, e não apenas o seu valor absoluto).

### Questão 3 — Verdadeiro ou Falso

**Sequência correta:** F, V, F, V, V, V, F, V, V, F

- **O que a questão está perguntando:** Pede para validar detalhes e fórmulas da conservação da massa baseados no resumo.
- **Explicação passo a passo (e por que as Falsas estão erradas):**
  - **1. (F):** A energia é usada nos casos mais *complicados* (com variação de temperatura), e não nos mais simples.
  - **2. (V):** Massa = massa específica $\times$ volume. $V = \Delta x \cdot \Delta y \cdot \Delta z$.
  - **3. (F):** O volume de controle é *fixo* no espaço. Quem se move e muda é o fluido.
  - **4. (V):** A fórmula básica da vazão mássica é exatamente $\dot m = \rho u A$.
  - **5. (V):** A forma integral descreve que o fluxo pelas paredes é igual à variação da massa presa lá dentro.
  - **6. (V):** Correto. Quando a densidade é constante, a equação da continuidade vira $\nabla \cdot \mathbf{V} = 0$.
  - **7. (F):** Uma derivada positiva ($\frac{\partial u}{\partial x} > 0$) significa que tem mais massa *saindo* nessa direção, e não entrando.
  - **8. (V):** Em 2D, as variações em $x$ e $y$ se equilibram ($-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$).
  - **9. (V):** As componentes da velocidade $V$ em $x$, $y$ e $z$ chamam-se $u$, $v$ e $w$.
  - **10. (F):** A forma *geral* inclui a densidade sim, através do termo $\frac{\partial \rho}{\partial t}$. Ela só some no caso *incompressível*.
- **O que lembrar:** Volume de controle = caixa invisível e fixa no espaço. Forma geral tem o tempo e a densidade, incompressível só tem variação espacial da velocidade.

### Questão 4 — Múltipla Escolha

**Questão 4.1.**
**Resposta correta:** (e)
- **O que a questão está perguntando:** A interpretação correta das derivadas para fluidos incompressíveis.
- **Explicação passo a passo:** Num fluido incompressível, a densidade é constante e não muda com o tempo. Por isso, os termos com a densidade somem da equação, deixando apenas o balanço entre as derivadas espaciais das velocidades ($\nabla \cdot \mathbf{V} = 0$).
- **Por que as demais erradas:** (a) $\frac{\partial v}{\partial y} > 0$ indica massa *saindo*. (b) O foco são as *variações espaciais* ($\partial u/\partial x$, etc.) e não o valor da velocidade no meio. (c) A derivada nula em 1D significa que a velocidade não variou entre a entrada e a saída, não que está parado. (d) No 3D incompressível, a variação em $x$ é equilibrada por $y$ e $z$ juntos, e não só por $z$.
- **O que lembrar:** Derivada positiva = massa saindo. Derivada igual a zero (em incompressível 1D) = velocidade não variou no percurso.

**Questão 4.2.**
**Resposta correta:** (c) $\frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} + \frac{\partial(\rho w)}{\partial z} + \frac{\partial\rho}{\partial t} = 0$
- **O que a questão está perguntando:** Qual fórmula representa a forma diferencial *geral* (antes de virar incompressível).
- **Explicação passo a passo:** A forma geral precisa contabilizar a variação da massa nas três direções e também no tempo, por isso tem o termo $\frac{\partial\rho}{\partial t}$.
- **Por que as demais erradas:** (a) É a equação para incompressível (cartesianas). (b) É a equação para incompressível (vetorial). (d) É apenas a fórmula de vazão mássica. (e) É a forma *integral*.
- **O que lembrar:** "Geral" inclui densidade ($\rho$) e variação no tempo ($\frac{\partial \rho}{\partial t}$).

**Questão 4.3.**
**Resposta correta:** (b)
- **O que a questão está perguntando:** O que significa o conceito de "volume de controle".
- **Explicação passo a passo:** O volume de controle é literalmente uma região imaginária que você escolhe e mantém fixa no espaço. O fluido passa através dela (entra e sai).
- **Por que as demais erradas:** As alternativas (a) e (e) descrevem algo que muda de tamanho ou acompanha o fluido, o que contraria a definição de "fixo no espaço". A (c) sugere que o fluido não flui através dele, o que é falso. A (d) restringe à análise de temperatura.
- **O que lembrar:** O volume de controle é o nosso "cubo" ou região fixa e imaginária onde fazemos o balanço de massa.

**Questão 4.4.**
**Resposta correta:** (b)
- **O que a questão está perguntando:** A razão física do sinal de menos no balanço de massa.
- **Explicação passo a passo:** Na matemática do balanço, se a taxa de saída for maior que a taxa de entrada, a massa total aprisionada dentro do cubo diminui. O sinal negativo é para garantir essa lógica: "mais saída do que entrada reduz a massa interna".
- **Por que as demais erradas:** Não tem relação com a gravidade (a). A densidade de um fluido incompressível não diminui (c). A matemática não obriga a vazão a ser negativa (d). E não é um erro de aproximação 1D, a regra vale para 3D também (e).
- **O que lembrar:** O sinal modela uma perda: saiu mais fluido do que entrou = tem menos fluido no volume.

**Questão 4.5.**
**Resposta correta:** (c)
- **O que a questão está perguntando:** O motivo do sinal negativo no balanço 2D ($-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$).
- **Explicação passo a passo:** Na face por onde o fluido entra, a seta de velocidade $u$ aponta para dentro do cubo, mas a seta "normal" da superfície sempre aponta para fora. Como as setas apontam para lados opostos, isso cria o sinal negativo na hora de deduzir a equação.
- **Por que as demais erradas:** O eixo $x$ não é sempre negativo (a). A velocidade $u$ não é obrigatoriamente menor que $v$ (b). Em 2D, a saída em $y$ equilibra a entrada em $x$, não zerando $z$ do nada (d). A densidade de fluidos incompressíveis não varia (e).
- **O que lembrar:** O sinal vem da direção da entrada (velocidade) indo contra a direção "para fora" (normal da face).

### Questão 5 — Cálculo de Análise Dimensional

- **O que a questão está perguntando:** Como achar o grupo adimensional que caracteriza o escoamento no tubo, usando o método de Buckingham-Π em seis passos.
- **Explicação passo a passo:**

**Passo 1: Quantas variáveis dimensionais?**
Temos 4 variáveis: velocidade ($u$), diâmetro ($D$), viscosidade ($\mu$) e densidade ($\rho$). Então, $n = 4$.

**Passo 2: Quantas dimensões fundamentais existem nessas variáveis?**
As dimensões são:
- Velocidade ($u$): $[L T^{-1}]$
- Diâmetro ($D$): $[L]$
- Viscosidade ($\mu$): $[M L^{-1} T^{-1}]$
- Densidade ($\rho$): $[M L^{-3}]$
Usamos massa (M), comprimento (L) e tempo (T). Logo, $m = 3$.

**Passo 3: Quantos grupos adimensionais ($\pi$) teremos?**
O número é $n - m = 4 - 3 = 1$. Portanto, acharemos apenas um grupo $\pi$.

**Passo 4: Escolha das variáveis repetitivas e da não repetitiva.**
Precisamos escolher $m = 3$ variáveis repetitivas. Escolhemos $u$, $\mu$ e $\rho$.
A variável não repetitiva que sobrou é $D$.

**Passo 5: Montagem da equação do grupo $\pi$.**
Juntamos a não repetitiva ($D$) com as repetitivas elevadas a expoentes $a$, $b$ e $c$:
$\pi_1 = D \cdot \rho^a \cdot \mu^b \cdot u^c$

**Passo 6: Descobrir os expoentes.**
Colocamos tudo em termos de dimensões e igualamos a um grupo sem dimensão $[M^0 L^0 T^0]$:
$[M^0 L^0 T^0] = [L] \cdot [M L^{-3}]^a \cdot [M L^{-1} T^{-1}]^b \cdot [L T^{-1}]^c$

Agrupando os termos M, L e T de cada lado:
$[M^0 L^0 T^0] = [M]^{a+b} \cdot [L]^{1 - 3a - b + c} \cdot [T]^{-b - c}$

Igualando as potências a zero:
- Para **M**: $0 = a + b \rightarrow a = -b$
- Para **T**: $0 = -b - c \rightarrow c = -b$
- Para **L**: $0 = 1 - 3a - b + c$

Substituindo $a = -b$ e $c = -b$ na equação do L:
$0 = 1 - 3(-b) - b + (-b)$
$0 = 1 + 3b - 2b$
$0 = 1 + b \rightarrow b = -1$

Agora achamos $a$ e $c$:
$a = -(-1) = 1$
$c = -(-1) = 1$

Finalmente, jogamos os expoentes de volta na equação do Passo 5:
$\pi_1 = D^1 \cdot \rho^1 \cdot \mu^{-1} \cdot u^1$
$\pi_1 = \frac{\rho \cdot u \cdot D}{\mu}$

- **O que lembrar:** Este grupo encontrado é o famoso **Número de Reynolds ($Re$)**. No método de Buckingham-Π, o truque principal é achar as dimensões de cada variável, montar o sistema linear dos expoentes e resolver para descobrir como as variáveis se dividem e multiplicam para "cortar" todas as dimensões.
