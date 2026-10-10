# Simulado de Hidrodinâmica — Unidade 1 — Capítulo 7

---

### 1ª Questão — Assinale a alternativa correta.

Analise as afirmativas abaixo sobre o modelo de escoamento em um canal inclinado, conforme deduzido no Capítulo 7:

**I.** O modelo assume que o escoamento é permanente (não muda ao longo do tempo) e bidimensional (não há movimento ao longo do eixo $z$).
**II.** A condição de contorno de impenetrabilidade afirma que o fluido não escorrega nas paredes do canal, fazendo com que sua velocidade paralela ao escoamento seja nula ($u=0$).
**III.** O grande diferencial do estudo de um canal inclinado em relação aos canais horizontais é a atuação ativa da força da gravidade, considerada como uma força de corpo presente no equacionamento ($\rho g_x \neq 0$).
**IV.** Graças a uma substituição matemática, o termo que representa a força que empurra o fluido passa a juntar tanto a variação de pressão quanto o efeito da gravidade: $\frac{\partial(p + \rho g h)}{\partial x}$.
**V.** A equação final do perfil de velocidades indica que, quanto mais inclinado o canal for, menor será a velocidade atingida pelo fluido.

**São corretas:**

- (a) I, II e IV.
- (b) I, III e IV.
- (c) II, IV e V.
- (d) III, IV e V.
- (e) I, III e V.

---

### 2ª Questão — Complete as Lacunas

Preencha as lacunas das frases abaixo utilizando os conceitos e termos apropriados.

1. O sistema de coordenadas adotado cria um eixo $h$ que está alinhado exclusivamente com a direção da _________.
2. Ao adotar a hipótese de escoamento incompressível, estabelecemos matematicamente que a densidade do fluido ($\rho$) é _________.
3. Diferente dos casos anteriores, o escoamento em canal inclinado não despreza as forças de _________ ($\rho g_x \neq 0$).
4. A condição matemática que afirma não existir velocidade atravessando as paredes ($v = 0$) é chamada de condição de contorno de _________.
5. Analisando a Lei de Conservação da _________, o modelo conclui que $\partial v / \partial y = 0$ para esse escoamento bidimensional e totalmente desenvolvido.
6. A parcela da gravidade que atua na direção do escoamento pelo canal é dada por $g_x = g \sin$ _________.
7. Na dedução da equação matemática, o seno é substituído por $-dh/dx$ para que o efeito da gravidade possa ser agrupado dentro da mesma derivada parcial em relação a _________.
8. Após as substituições na equação de Navier-Stokes, o termo que empurra o fluido, $\frac{\partial(p + \rho g h)}{\partial x}$, é considerado uma _________ para fins de integração.
9. Ao final das integrações, o perfil de velocidades do fluido no interior do canal fechado apresenta um formato geométrico _________.
10. Olhando para a equação final deduzida, se um fluido tiver menor _________ (menor resistência ao fluxo), ele atingirá uma velocidade máxima maior.

---

### 3ª Questão — Verdadeiro ou Falso

Classifique as afirmativas abaixo como Verdadeiras (V) ou Falsas (F).

(  ) 1. No modelo do canal inclinado, os eixos $x$ e $y$ acompanham a direção do escoamento, enquanto a direção $h$ atua como o eixo vertical que aponta para baixo, acompanhando a gravidade.

(  ) 2. Neste problema, a componente da força da gravidade ao longo do eixo $x$ é fundamental, pois ela ajuda a empurrar ativamente o fluido para baixo ao longo do canal.

(  ) 3. A condição de não escorregamento determina que as velocidades perpendiculares às paredes ($v$) sejam iguais a zero em $y=0$ e $y=a$.

(  ) 4. Após integrar o balanço de massa para esse escoamento, descobre-se que a velocidade $v$ tem um perfil linear que atinge um valor máximo constante no centro do canal.

(  ) 5. A aplicação da equação de Navier-Stokes neste caso se resume a encontrar um equilíbrio entre a viscosidade (que tenta frear o fluido) e as forças da pressão e da gravidade (que tentam empurrá-lo).

(  ) 6. A hipótese de escoamento "totalmente desenvolvido" indica que o fluxo já se estabilizou no tubo, o que elimina a variação da velocidade longitudinal ao longo da direção do fluxo ($\partial u/\partial x = 0$).

(  ) 7. A substituição de $\sin\theta$ por $-dh/dx$ é um truque usado exatamente para impedir que a gravidade e a pressão se misturem na mesma equação.

(  ) 8. Após integrar a equação de Navier-Stokes duas vezes no eixo espacial $y$, surgem as constantes de integração $C_1$ e $C_2$, que são descobertas aplicando a condição de contorno de não escorregamento.

(  ) 9. De acordo com a equação final obtida, se aumentarmos a inclinação do canal ($\theta$), a velocidade máxima do escoamento não será afetada.

(  ) 10. Nas anotações originais de sala, o professor desenhou o ângulo de inclinação do peso utilizando o símbolo $\phi$, embora o texto e as equações tenham sido escritos utilizando $\theta$.

---

### 4ª Questão — Múltipla Escolha

Selecione a alternativa correta para cada uma das questões a seguir.

**Questão 4.1.** Em relação às "forças de corpo" no escoamento do Capítulo 7, assinale a constatação correta:

(a) Foram abandonadas da modelagem matemática para simplificar as equações do escoamento bidimensional.
(b) São matematicamente anuladas porque o escoamento ocorre em regime permanente (sem mudança no tempo).
(c) Atuam de forma perpendicular ao canal (no eixo $y$), empurrando o fluido contra a parede inferior e gerando compressão.
(d) São explicitamente incluídas na equação ($\rho g_x \neq 0$), já que a gravidade exerce um papel ativo em puxar o fluido ladeira abaixo.
(e) São totalmente convertidas em energia térmica para compensar o atrito excessivo com as paredes do duto.

**Questão 4.2.** O que a Lei da Conservação da Massa nos informa sobre a velocidade perpendicular às paredes ($v$) nesse modelo de escoamento?

(a) A massa do fluido se acumula perto das paredes, aumentando localmente a densidade do fluido ao descer o canal.
(b) Ela simplifica a equação para $\partial v/\partial y = 0$. Juntando isso com a regra de que o fluido não atravessa a parede (impenetrabilidade), prova-se que $v = 0$ em qualquer ponto do canal.
(c) Ela mostra que o fluido ganha velocidade no eixo vertical para compensar a força gravitacional da ladeira.
(d) A velocidade $u$ precisa chegar a zero nas paredes para garantir que a quantidade de massa se conserve no eixo transversal $z$.
(e) O escoamento gera ilhas de recirculação perto das paredes porque o fluido é incompressível.

**Questão 4.3.** O modelo matemático substitui o termo $\sin\theta$ por $-dh/dx$. Qual foi a principal utilidade dessa substituição?

(a) Separar a influência da bomba de pressão da influência natural da gravidade, para estudá-las em contas diferentes.
(b) Modificar o eixo de coordenadas para que ficasse totalmente alinhado com a direção do peso, ignorando a inclinação do tubo.
(c) Juntar o efeito da gravidade e o efeito da pressão sob uma mesma derivada matemática, criando um único termo que descreve a força que empurra o fluido: $\frac{\partial(p+\rho g h)}{\partial x}$.
(d) Validar as unidades de medida das equações, garantindo que as forças de cisalhamento da viscosidade se igualassem ao peso da água.
(e) Explicar por que a água sofre compressibilidade repentina quando desce em alta velocidade.

**Questão 4.4.** A equação final para a velocidade do fluido é $u = \frac{1}{2\mu}\frac{\partial(p+\rho g h)}{\partial x}(y^2 - ay)$. O que essa fórmula nos diz sobre como o fluido se comporta?

(a) O fluido tem um perfil de velocidade reto (linear), dependente da densidade e sem sofrer atrito no centro do tubo.
(b) A velocidade é nula no centro geométrico do canal e atinge valores máximos encostando diretamente nas paredes inferior e superior.
(c) O fluido tem um perfil em forma de parábola. A sua velocidade máxima aumenta se o canal for mais inclinado, mas diminui se o fluido for mais grosso e resistente ao movimento (maior viscosidade $\mu$).
(d) A velocidade do fluido continua aumentando indefinidamente ao longo do canal porque a gravidade é constante e não encontra resistência suficiente.
(e) A inclinação do tubo freia o movimento da água, funcionando como um obstáculo mecânico para a pressão da bomba.

**Questão 4.5.** Na simplificação da equação de Navier-Stokes, por que eliminamos os termos de aceleração convectiva (como $u \frac{\partial u}{\partial x}$)?

(a) Porque decidimos ignorar totalmente o efeito da massa do fluido ao longo do problema.
(b) Porque o atrito das paredes freia as laterais da água, impedindo que o volume total acelere.
(c) Porque o modelo considera o escoamento como totalmente desenvolvido ($\partial u/\partial x = 0$) e bidimensional ($w = 0$), significando que a velocidade do fluido já se estabilizou e não muda ao avançar pelo tubo.
(d) Porque a impenetrabilidade nas laterais, combinada com a incompressibilidade geral, cancelou o ganho de aceleração em curvas.
(e) Porque a pressão externa foi totalmente anulada pela gravidade na direção paralela às paredes.

---

### 5ª Questão — Cálculo de Análise Dimensional

Avalie o escoamento de água pelo interior de um duto circular de diâmetro $D$. 

Sabe-se que a dinâmica do problema depende das seguintes variáveis dimensionais: a velocidade $u$, o diâmetro $D$, a viscosidade dinâmica $\mu$ e a densidade $\rho$.

Utilizando o método de Buckingham-Π estruturado nos seus seis passos fundamentais, determine o grupo adimensional resultante que governa esse problema (Dica: o resultado deve ser o Número de Reynolds).

<br><br>

---

# Gabarito Comentado — Respostas Corretas e Incorretas

### Questão 1 — Assinale a alternativa correta

**Resposta:** (b) I, III e IV.

**O que a questão está perguntando:** O aluno precisa identificar quais afirmações descrevem corretamente as regras e deduções usadas no material para explicar o escoamento em um canal inclinado.

**Explicação:**
- **Intuição física:** Quando a água escoa descendo uma rampa ou ladeira, o seu peso ajuda a empurrá-la para baixo. Assim, não dependemos só de uma bomba de pressão.
- A afirmação **I** está correta porque o modelo estuda um regime ideal, onde o fluxo já estabilizou no tempo (permanente) e o canal é considerado largo o suficiente para ignorarmos os efeitos nas laterais do eixo $z$ (bidimensional).
- A afirmação **III** está correta porque o grande diferencial do Capítulo 7 é admitir que a gravidade atua ativamente, chamando-a de "força de corpo" ($\rho g_x \neq 0$).
- A afirmação **IV** está correta porque o professor usa um truque matemático (a substituição de $\sin \theta$ por $-dh/dx$) para juntar pressão e gravidade no pacote $\frac{\partial(p + \rho g h)}{\partial x}$.

**Por que as outras alternativas estão incorretas:**
- **II está incorreta:** A afirmação confunde os termos. Dizer que o fluido tem velocidade paralela nula nas paredes (não escorrega) é a condição de **não escorregamento**. Já a **impenetrabilidade** significa que a velocidade *perpendicular* (de atravessar a parede) é zero.
- **V está incorreta:** Pela física e pela equação, se a inclinação for maior, a gravidade ajuda mais, logo a velocidade será *maior* (e não menor).

**O que lembrar para a prova:** No canal inclinado, usamos a força de corpo (gravidade) no balanço, e agrupamos essa gravidade à diferença de pressão.
**Fonte:** Capítulo 7, Passo 2 (Hipóteses Básicas) e Passo 3 (Condições de Contorno).

---

### Questão 2 — Complete as Lacunas

**Respostas:**
1. **gravidade**
2. **constante**
3. **corpo**
4. **impenetrabilidade**
5. **Massa**
6. **$\theta$**
7. **$x$**
8. **constante**
9. **parabólico**
10. **viscosidade**

**Explicação dos termos:**
- **Lacuna 1:** O eixo $h$ é criado especialmente para medir a profundidade real na vertical (apontando para onde a gravidade atua).
- **Lacuna 2:** "Incompressível" significa que não podemos espremer a água para ela ocupar menos espaço; portanto, sua densidade é **constante**.
- **Lacuna 3:** Na hidrodinâmica, forças que atuam no volume todo do fluido (como a gravidade) são chamadas forças de **corpo**.
- **Lacuna 4:** Se o fluido não atravessa o material da parede, dizemos que a parede impõe a condição de **impenetrabilidade**.
- **Lacuna 5:** A Lei da Conservação da **Massa** garante que, se não há mudança na velocidade ao longo do eixo $x$ ou $z$, também não pode haver ao longo de $y$.
- **Lacuna 6:** Um simples triângulo de forças mostra que a força ao longo do tubo é o peso projetado usando o seno da inclinação **$\theta$**.
- **Lacuna 7 e 8:** O agrupamento de pressão e gravidade é possível porque ambas passam a ser derivadas em relação a **$x$**. Como todo esse bloco empurra o fluido por igual, no processo de integração ele é tratado como uma grande **constante**.
- **Lacuna 9:** Matematicamente, a equação termina com a variável $y$ elevada ao quadrado ($y^2$), criando um desenho **parabólico** para a velocidade.
- **Lacuna 10:** A **viscosidade** atua como um "atrito interno". Quanto menor ela for, menos resistência haverá e maior será a velocidade.

**Fonte:** Capítulo 7, deduções passo a passo (Passos 1 a 6b).

---

### Questão 3 — Verdadeiro ou Falso

**Respostas:** 1(V), 2(V), 3(F), 4(F), 5(V), 6(V), 7(F), 8(V), 9(F), 10(V).

**Justificativas para as falsas:**
- **3. (Falsa):** A condição de não escorregamento determina que as velocidades **paralelas/tangenciais** (no eixo $x$ ou seja, $u$, e no eixo $z$, $w$) sejam iguais às da parede (nulas, se a parede for fixa). A velocidade perpendicular ($v$) é anulada pela impenetrabilidade.
- **4. (Falsa):** A integração mostra que $v = 0$ ao longo de todo o espaço do tubo. O perfil de velocidade que atinge valor máximo no centro do canal é o da velocidade $u$ (paralela ao tubo).
- **7. (Falsa):** A substituição de $\sin\theta$ por $-dh/dx$ tem a intenção de **facilitar** o agrupamento algébrico da gravidade com a derivada da pressão, e não impedir.
- **9. (Falsa):** Pela intuição e pela equação, aumentar a declividade ($\theta$) fornece mais ajuda da gravidade, o que **aumenta** a velocidade máxima.

**Fonte:** Capítulo 7, Passo 3, Passo 4a e Passo 6b.

---

### Questão 4 — Múltipla Escolha

**Questão 4.1.**
**Resposta:** (d)
**O que a questão está perguntando:** Como o material trata o peso da água descendo o canal inclinado.
**Explicação:** Como a água está em uma ladeira, o peso dela puxa o escoamento para baixo. Na equação, isso é representado pelas "forças de corpo", expressas por $\rho g_x \neq 0$.
**Por que as outras alternativas estão incorretas:** A gravidade não foi abandonada (a), não é anulada pelo regime permanente (b), não atua perpendicularmente ao ponto de esmagar o fluido (c) e não vira energia térmica nesse modelo (e).
**Fonte:** Capítulo 7, Passo 2.

**Questão 4.2.**
**Resposta:** (b)
**O que a questão está perguntando:** Como usamos o conceito de Conservação da Massa na dedução matemática.
**Explicação:** Ao usar a Lei de Conservação de Massa para o nosso escoamento (onde nada muda nos eixos $x$ e $z$), sobra apenas a equação $\partial v/\partial y = 0$. Como sabemos que a água não atravessa a parede ($v=0$ nos contornos por impenetrabilidade), a matemática nos garante que $v=0$ no canal inteiro.
**Por que as outras alternativas estão incorretas:** Fluido incompressível não acumula massa (a), o fluxo continua calmo (laminar) e sem "espirais" ou "turbulências normais" inventadas (c, e), e $u$ zerar nas paredes é não-escorregamento, não Conservação da Massa para o eixo transversal $z$ (d).
**Fonte:** Capítulo 7, Passo 4a.

**Questão 4.3.**
**Resposta:** (c)
**O que a questão está perguntando:** Para que serve o "truque" matemático de trocar o seno da inclinação.
**Explicação:** A equação de Navier-Stokes já tem uma derivada da pressão em relação ao eixo $x$. O professor troca o $\sin \theta$ pela derivada da altura $h$ em relação a $x$ ($-dh/dx$). Dessa forma, fica fácil escrever um "pacotão" único: $\frac{\partial(p+\rho g h)}{\partial x}$, que é a força total que empurra a água.
**Fonte:** Capítulo 7, Passo 4b.

**Questão 4.4.**
**Resposta:** (c)
**O que a questão está perguntando:** Como interpretar fisicamente a equação do perfil de velocidade.
**Explicação:** A equação é do segundo grau (tem o termo $y^2$), o que no gráfico gera uma curva em forma de parábola. Se olharmos os termos da equação, quanto maior a ajuda da ladeira (maior $\theta$) maior o resultado. E a viscosidade $\mu$ está no divisor: fluido grosso (maior $\mu$) divide a força, resultando em menor velocidade.
**Fonte:** Capítulo 7, Passo 6b.

**Questão 4.5.**
**Resposta:** (c)
**O que a questão está perguntando:** Por que os pedaços da fórmula gigante de Navier-Stokes que tratam de aceleração foram cortados para dar zero.
**Explicação:** Aceleração convectiva indica que a velocidade mudaria de um ponto a outro da tubulação. Como adotamos a hipótese de "totalmente desenvolvido", isso significa que o fluido já está "em velocidade de cruzeiro", o que matematicamente diz que as derivadas da velocidade de fluxo são zero ($\partial u/\partial x = 0$).
**Fonte:** Capítulo 7, Passo 4b.

---

### Questão 5 — Cálculo de Análise Dimensional

**Resposta Discursiva:**

**O que a questão está perguntando:** O aluno deve aplicar o Método de Buckingham-Π, em 6 passos, para achar um número adimensional que relaciona velocidade ($u$), diâmetro ($D$), densidade ($\rho$) e viscosidade ($\mu$).

**Explicação passo a passo:**

- **Passo 1:** Listar e contar as variáveis do problema.
  Temos $u$, $D$, $\mu$, e $\rho$. Total: $n = 4$ variáveis.

- **Passo 2:** Determinar as dimensões fundamentais de cada variável (em termos de Massa [M], Comprimento [L] e Tempo [T]):
  - $u$ (velocidade) = $[L T^{-1}]$
  - $D$ (diâmetro) = $[L]$
  - $\rho$ (densidade) = $[M L^{-3}]$
  - $\mu$ (viscosidade) = $[M L^{-1} T^{-1}]$
  Como usamos M, L e T, temos $m = 3$ dimensões fundamentais.

- **Passo 3:** Calcular a quantidade de grupos adimensionais ($\pi$).
  Quantidade = $n - m = 4 - 3 = 1$. Portanto, acharemos apenas um grupo $\pi$.

- **Passo 4:** Escolher as variáveis repetitivas (devem ser $m=3$).
  Geralmente escolhemos uma variável geométrica, uma cinemática e uma propriedade do fluido. Pela resolução original desse exercício em aula, as repetitivas escolhidas foram $\rho, \mu, u$, restando $D$ como a variável não-repetitiva.
  Variáveis repetitivas: $u, \mu, \rho$.
  Variável não-repetitiva: $D$.

- **Passo 5:** Escrever a equação do grupo $\pi$.
  Ele é formado multiplicando a variável isolada pelas repetitivas, cada uma elevada a um expoente desconhecido:
  $\pi_1 = D^1 \cdot \rho^a \cdot \mu^b \cdot u^c$

- **Passo 6:** Achar os valores de $a, b, c$ equilibrando as dimensões de forma que tudo resulte zero (afinal, é a-dimensional).
  $[M^0 L^0 T^0] = [L]^1 \cdot [M L^{-3}]^a \cdot [M L^{-1} T^{-1}]^b \cdot [L T^{-1}]^c$
  
  Separando e somando os expoentes por dimensão:
  **M:** $0 = a + b \rightarrow a = -b$
  **T:** $0 = -b - c \rightarrow c = -b$
  **L:** $0 = 1 - 3a - b + c$
  
  Substituindo $a$ e $c$ pelo valor de $-b$ na equação de L:
  $0 = 1 - 3(-b) - b + (-b)$
  $0 = 1 + 3b - b - b$
  $0 = 1 + b \rightarrow b = -1$
  
  Com $b = -1$, calculamos $a$ e $c$:
  $a = -(-1) \rightarrow a = 1$
  $c = -(-1) \rightarrow c = 1$
  
  A fórmula final do nosso grupo é:
  $\pi_1 = D^1 \cdot \rho^1 \cdot \mu^{-1} \cdot u^1$
  
  $\pi_1 = \frac{\rho \cdot u \cdot D}{\mu}$

**O que lembrar para a prova:** Esse grupo adimensional que relaciona as forças de inércia com as forças de viscosidade é extremamente famoso, e se chama **Número de Reynolds ($Re$)**.
**Fonte:** Trata-se de uma aplicação de Análise Dimensional (Capítulo de Teorema de Buckingham-Pi), inserida para praticar as propriedades do fluido que governam Navier-Stokes.
