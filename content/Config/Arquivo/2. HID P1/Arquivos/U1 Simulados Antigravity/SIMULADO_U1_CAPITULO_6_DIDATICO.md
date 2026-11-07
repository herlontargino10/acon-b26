# Simulado de Hidrodinâmica — Unidade 1 (Capítulo 6)

---

### 1ª Questão — Assinale a alternativa correta.

Analise as afirmativas abaixo referentes ao escoamento plenamente desenvolvido dominado por forças de pressão e ao método analítico de resolução.

**I.** A hipótese de que o escoamento é independente do tempo caracteriza um escoamento permanente ($\frac{\partial (.)}{\partial t} = 0$).

**II.** A condição de não escorregamento estipula que a velocidade do escoamento junto à parede possui o seu máximo valor absoluto.

**III.** O modelo de escoamento plenamente desenvolvido conduzido por pressão apresentado no material estabelece um balanço fundamental entre a força de pressão e a força gravitacional.

**IV.** Ao se integrar a equação da conservação da massa com a condição de impenetrabilidade, prova-se analiticamente que a componente transversal da velocidade ($v$) é nula em toda e qualquer posição do duto.

**V.** A solução analítica deduzida no capítulo, conhecida como equação de Poiseuille, determina que o perfil de velocidades do escoamento é parabólico.

**São corretas:**

- (a) I, II e III.
- (b) II, III e V.
- (c) I, IV e V.
- (d) I, III e IV.
- (e) III, IV e V.

---

### 2ª Questão — Complete as Lacunas

Preencha as lacunas das frases abaixo utilizando os conceitos e termos correspondentes.

1. No passo de hipóteses básicas, considerar que o fluido pode ser um líquido ou um gás se movendo lentamente justifica a hipótese de escoamento ________.

2. A hipótese de escoamento ________ é representada matematicamente pela anulação da derivada parcial em relação ao tempo.

3. A restrição de contorno de não ________ exige que o fluido em contato com as fronteiras sólidas possua a mesma velocidade delas ($u_{y=0}=0$ e $u_{y=a}=0$).

4. A condição física que impõe que não podem existir velocidades perpendiculares ou normais às paredes é denominada de ________.

5. A ausência de atuação do peso do fluido no equacionamento principal, refletida em $\rho g_x = 0$, indica que as forças de ________ foram negligenciadas.

6. A resolução inicia-se pela conservação da ________, que comprova precocemente que $\frac{\partial v}{\partial y} = 0$, reduzindo a complexidade do sistema.

7. Na equação simplificada de Navier-Stokes para a condução por pressão, a força induzida pelo gradiente de pressão é balanceada unicamente pela força ________ da água (relacionada ao termo $\mu \frac{\partial^2 u}{\partial y^2}$).

8. O método matemático invocado para igualar duas expressões independentes dependentes de $x$ e de $y$ a uma constante comum é a ________ de variáveis.

9. Na equação de Poiseuille final, constata-se fisicamente que quanto maior for a ________ do fluido ($\mu$), menor será a velocidade máxima atingida.

10. A equação resultante da derivação abordada no capítulo, que descreve um arranjo onde a velocidade máxima ocorre no centro do canal, é batizada de equação de ________.

---

### 3ª Questão — Verdadeiro ou Falso

Classifique as afirmativas abaixo como Verdadeiras (V) ou Falsas (F).

(  ) 1. Conforme a dica de prova, o professor não aceitará a resposta "escoamento desenvolvido" em avaliações, exigindo obrigatoriamente o termo completo "totalmente desenvolvido" sob pena de decréscimo na pontuação.

(  ) 2. A primeira equação diferencial explorada no procedimento (Passo 4) é a conservação da quantidade de movimento, pois nela a componente $v$ é primeiramente anulada.

(  ) 3. A integração inicial da conservação da massa resulta que a velocidade normal às paredes, $v$, é constante, com seu valor fixado em zero pela condição de impenetrabilidade nas paredes $y=0$ e $y=a$.

(  ) 4. A premissa de um escoamento bidimensional (2D) assegura que não há variações de velocidade ao longo do eixo $z$, anulando as derivadas espaciais e a componente $w$.

(  ) 5. O perfil de velocidades construído pela equação de Poiseuille possui distribuição estritamente linear, decrescendo a uma taxa constante do centro até as paredes.

(  ) 6. No escoamento plenamente desenvolvido, a equação de Navier-Stokes é reduzida drasticamente pois não existe nenhum termo de aceleração convectiva ou temporal atuando sobre o fluido.

(  ) 7. A seção tachada transcrita no material evidencia que a dedução do "escoamento plenamente desenvolvido dominado por força de corpo (gravidade)" foi descontinuada/abortada na apostila original.

(  ) 8. As constantes de integração $C_1$ e $C_2$ da conservação da quantidade de movimento puderam ser ignoradas e removidas sem a necessidade de aplicação formal de condições de contorno.

(  ) 9. Escoamentos portadores das características permanente, totalmente desenvolvido e 2D representam, em conjunto, o clássico escoamento laminar modelável.

(  ) 10. O escoamento abordado no capítulo ocorre estritamente pela diferença de velocidade mecânica imposta entre duas paredes translatórias.

---

### 4ª Questão — Múltipla Escolha

Selecione a alternativa correta para cada uma das questões a seguir.

**Questão 4.1.** Sobre a simplificação da Equação de Conservação da Massa, qual aspecto metodológico foi determinante para se deduzir a anulação dos gradientes $\frac{\partial w}{\partial z}$ e $\frac{\partial u}{\partial x}$?

(a) O reconhecimento de que o fluido é compressível anula as derivadas espaciais em volumes fechados.

(b) A substituição antecipada da pressão na equação de Navier-Stokes forçou as variações vetoriais a zero.

(c) A anulação ocorreu exclusivamente pela impenetrabilidade da placa inferior localizada em $y=0.

(d) A hipótese de escoamento totalmente desenvolvido zera a variação de $u$ ao longo de $x$, e a característica puramente bidimensional (2D) zera as variações de propriedades ao longo do eixo $z$.

(e) O método de separação de variáveis dividiu as derivadas até extinguir as componentes longitudinais.

**Questão 4.2.** No arranjo do escoamento duto a duto abordado no Capítulo 6, o que justifica fisicamente o sumiço dos componentes de inércia na equação reduzida de Navier-Stokes $\frac{\partial p}{\partial x} = \mu \frac{\partial^2 u}{\partial y^2}$?

(a) O escoamento ocorre com um gradiente severo em declive livre, tornando o arrasto preponderante.

(b) O escoamento está em regime permanente (anulando variações temporais) e plenamente desenvolvido (anulando variações convectivas espaciais), o que significa que não existe aceleração fluida, restando apenas o equilíbrio estático entre pressão e atrito.

(c) A viscosidade tranca a movimentação hídrica ao longo de todo o canal, mantendo o corpo hídrico imobilizado sem inércia.

(d) As forças de corpo compensam exatamente as perdas do fluido na entrada do canal fechado.

(e) Trata-se de uma simplificação restrita a fluidos não-newtonianos sem massa específica controlável.

**Questão 4.3.** Após a aplicação rigorosa das condições de contorno, a equação de Poiseuille revelou a expressão $u = \frac{1}{2\mu} \frac{\partial p}{\partial x} (y^2 - ay)$. Observando essa formulação e a representação visual na lousa, onde o escoamento atinge a sua velocidade máxima?

(a) O máximo concentra-se colado na parede superior ($y=a$), impulsionado pela menor resistência pressórica.

(b) Ocorre precisamente na fronteira inferior ($y=0$), devido à conservação do não escorregamento da malha.

(c) A velocidade desponta maximizada no limite exato de impenetrabilidade vertical em $x=0$.

(d) No centro livre do canal transversal, posicionado no miolo afastado e intocado pelas bordas (formando o pico livre da curva parabólica).

(e) Nas extremidades, devido à predominância vetorial estrita da força de corpo.

**Questão 4.4.** Durante o equacionamento estruturado do modelo de Poiseuille (Passo 3 e Passo 6b), como a condição de "não escorregamento" se manifestou matematicamente na manipulação da matriz física?

(a) Foi demonstrado que os fluidos de maior viscosidade escorregam paralelamente à placa inferior de $y=-a$.

(b) A premissa definiu taxativamente que a velocidade do escoamento junto às duas paredes fixas precisaria ser idêntica a elas, estabelecendo-se $u_{y=0}=0$ e $u_{y=a}=0$.

(c) Impôs que o escorregamento compensasse a falta de parede móvel no topo ($y=a$), operando a uma velocidade $V$.

(d) Condicionou a variação cartesiana do eixo vertical a se estender ao infinito, gerando contornos virtuais abertos.

(e) Garantiu apenas a nulidade no instante inicial $t=0$, pois o sistema desvia-se com o passar do tempo.

**Questão 4.5.** A técnica da "separação de variáveis" foi o argumento algébrico principal evocado na derivação da quantidade de movimento. Qual assertiva define, com base na fonte, o fundamento mecânico para o uso desta ferramenta naquele ponto do cálculo?

(a) O princípio impõe que duas quantidades distintas que dependem exclusivamente de eixos isolados diferentes (uma variando só em $x$ e a outra só em $y$) e que permanecem algebricamente iguais sob qualquer coordenada, necessariamente precisam ser constantes uniformes.

(b) Exige a atuação ativa da força da gravidade projetada para conseguir desagregar as variáveis mássicas.

(c) Assegura que o fluido possa ser fracionado entre compressível numa parede e incompressível na vizinhança paralela.

(d) Aplica-se unicamente para separar os fluidos na equação da continuidade (massa), evitando o cálculo na Navier-Stokes.

(e) Subtrai uma das paredes do cálculo para transmutar o formato da linha da corrente em modelo retilíneo uniforme (1D).

---

### 5ª Questão — Cálculo de Análise Dimensional

Avalie a dinâmica de comportamento do escoamento da água no interior de um duto circular de diâmetro D, sendo a densidade e a viscosidade da água parâmetros conhecidos.

Considere as variáveis dimensionais do problema como a velocidade $u$, o diâmetro $D$, a viscosidade $\mu$ e a densidade $\rho$.

Utilize o método de Buckingham-Π para determinar o grupo adimensional resultante, estruturando a sua resolução nos seis passos fundamentais.

<br><br>

---

# Gabarito Comentado

### Questão 1 — Marque X

**Resposta correta:** (c) I, IV e V.

**O que a questão está perguntando:**
A questão avalia a compreensão sobre o modelo de escoamento conduzido por pressão (Equação de Poiseuille), suas hipóteses de contorno e implicações analíticas.

**Explicação passo a passo:**
- **Afirmativa I:** Correta. A hipótese de que o escoamento é permanente significa que suas propriedades são independentes do tempo, o que matematicamente anula a derivada temporal ($\frac{\partial (.)}{\partial t} = 0$).
- **Afirmativa IV:** Correta. A integração da equação da massa ($\frac{\partial v}{\partial y} = 0$) diz que $v$ é constante. Aplicando a condição de impenetrabilidade nas paredes ($v = 0$), conclui-se que $v$ é zero em qualquer posição, simplificando imensamente a próxima equação.
- **Afirmativa V:** Correta. Após a dupla integração de Navier-Stokes (agora focada apenas em pressão vs. atrito), a equação final deduzida (Poiseuille) evidencia que o perfil das velocidades assume um formato parabólico.

**Por que as demais estão erradas:**
- **Afirmativa II (Incorreta):** A condição de não escorregamento não estipula que o fluido atinge o máximo valor, mas sim que o fluido *gruda* na parede sólida, adquirindo a sua velocidade (no caso, $u = 0$, velocidade nula).
- **Afirmativa III (Incorreta):** O modelo é conduzido estritamente por pressão em oposição ao atrito viscoso. As forças de corpo (gravitacionais) são explicitamente anuladas no passo 2 ($\rho g_x = 0$).

**O que lembrar para a prova:**
- Escoamento Permanente = Independe do tempo ($\frac{\partial (.)}{\partial t} = 0$).
- Não escorregamento = Fluido tem a mesma velocidade da parede (neste caso, $0$).
- Impenetrabilidade = Velocidade perpendicular $v = 0$.
- Poiseuille = Perfil parabólico entre placas empurrado por diferença de pressão.

**Fonte:** Resumo Oficial, seções 2, 3, 4, 5 e 8.

---

### Questão 2 — Complete as Lacunas

**Respostas corretas:**
1. **incompressível**
2. **permanente**
3. **escorregamento**
4. **impenetrabilidade**
5. **corpo**
6. **massa**
7. **friccional** (ou viscosa)
8. **separação**
9. **viscosidade**
10. **Poiseuille**

**O que a questão está perguntando:**
Requer a identificação de termos específicos que fundamentam a dedução de escoamento analítico a partir das leis de conservação.

**Explicação passo a passo:**
1. **Incompressível:** Líquidos movem-se com densidade constante ($\rho = const.$), definindo a hipótese de incompressibilidade.
2. **Permanente:** A independência do tempo, expressa por $\frac{\partial (.)}{\partial t} = 0$, caracteriza o escoamento permanente.
3. **Escorregamento:** A restrição de "não escorregamento" exige que o fluido em contato com as fronteiras estáticas zere a sua velocidade paralela ($u = 0$).
4. **Impenetrabilidade:** Evita que o fluxo vaze pelas fronteiras sólidas, anulando vetores transversais ($v = 0$).
5. **Corpo:** Ao igualar $\rho g_x = 0$, despreza-se a influência do peso, caracterizado fisicamente como "forças de corpo".
6. **Massa:** O roteiro impõe calcular a conservação da massa antes de qualquer outra equação para eliminar incógnitas prematuramente.
7. **Friccional:** Sem acelerações inerciais ativas, a indução originária da pressão fica disputando espaço (balanceada) unicamente com a resistência friccional (viscosidade) atuante na parede interior.
8. **Separação:** A justificativa para igualar fatores dependentes de variáveis independentes (x e y) a uma constante embasa-se na "separação de variáveis".
9. **Viscosidade:** A equação final ($\mu$ no denominador) comprova que o aumento do grau de viscosidade atrita o movimento e refreia a magnitude da velocidade máxima.
10. **Poiseuille:** A parábola entre dutos movida a tensão é classificada historicamente como Equação de Poiseuille.

**O que lembrar para a prova:**
Incompressível ($\rho=cte$); Permanente ($dt=0$); Desenvolvido ($dx=0$). Não escorregamento ($u=0$ na parede) e Impenetrabilidade ($v=0$ na parede). Separação de variáveis é o artifício matemático da dedução.

**Fonte:** Resumo Oficial, seções 2, 3, 4, 6, 7 e 8.

---

### Questão 3 — Verdadeiro ou Falso

**Resposta correta:** F, F, V, V, F, V, V, F, V, F.

**O que a questão está perguntando:**
Confirmação dos fundamentos, premissas de contorno e do resultado da equação de Poiseuille, além de advertências feitas em sala pelo professor.

**Por que as afirmativas são Verdadeiras (V) ou Falsas (F):**

- **1. (F) Falsa:** O professor (vide Dica de Prova) advertiu que *aceitará* a grafia encurtada "escoamento desenvolvido" em vez de "totalmente desenvolvido" sem causar prejuízo na nota.
- **2. (F) Falsa:** A primeira lei usada (Passo 4a) é a Conservação da *Massa* (continuidade), e não a da Quantidade de Movimento.
- **3. (V) Verdadeira:** Integrando $\frac{\partial v}{\partial y} = 0$, obtemos $v = constante$. A condição de impenetrabilidade dita que na parede $v = 0$, logo a constante é nula em todo lugar.
- **4. (V) Verdadeira:** A restrição impõe bidimensionalidade (2D), garantindo que as mudanças ao longo da terceira profundidade não existem (as funções perdem o diferencial em $z$ e as componentes de velocidade ali anulam-se).
- **5. (F) Falsa:** O escoamento não tem distribuição estritamente linear, mas apresenta comportamento *parabólico*.
- **6. (V) Verdadeira:** A equação fica restrita apenas às derivadas espaciais de pressão e ao diferencial atritante $\mu$. Todas as parcelas inerentes à aceleração (tempo e posição longitudinal) colapsam para zero.
- **7. (V) Verdadeira:** Como anotado textualmente, a tentativa original de modelar o arranjo impulsionado unicamente pela gravidade (força de corpo) sofreu rasura definitiva (cancelamento) ao fim daquele capítulo.
- **8. (F) Falsa:** A seção 8 demonstra minuciosamente a inserção dos limites físicos $y = 0$ e $y = a$ a fim de atribuir um valor efetivo às duas constantes abstratas surgidas ($C_1$ e $C_2$).
- **9. (V) Verdadeira:** A fonte confirma no passo 2 que as características de escoamento permanente, 2D e desenvolvido são a assinatura típica do "escoamento laminar".
- **10. (F) Falsa:** O caso que induz movimento por translação das paredes baseia-se na força viscosa (Viscosity-driven/Couette). O capítulo atual modela a condução induzida unicamente pela força de *pressão* (Pressure-driven).

**O que lembrar para a prova:**
No modelo de Poiseuille (pressão): A aceleração convectiva e local são nulas. O arranjo é 2D laminar. A distribuição de velocidades é curva (parabólica), não reta (linear).

**Fonte:** Resumo Oficial, seções 1, 2, 3, 5, 6, 8 e notas extras.

---

### Questão 4 — Múltipla Escolha

**Questão 4.1.** 
**Resposta correta:** (d)
**O que a questão está perguntando:** Como as hipóteses iniciais anularam os termos na equação da Massa antes de integrar $v$.
**Explicação passo a passo:** 
A equação de conservação da massa é $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$. Como o escoamento é assumido *totalmente desenvolvido*, o gradiente longitudinal de velocidade zera ($\frac{\partial u}{\partial x} = 0$). Sendo assumido *2D* infinito, o terceiro eixo sofre do mesmo bloqueio ($\frac{\partial w}{\partial z} = 0$). 
**Por que as demais estão erradas:**
O fluido assumido é incompressível (e não compressível como na letra a); a equação de Navier-Stokes ainda não foi invocada para misturar pressão (letra b); a impenetrabilidade anula a constante, mas a anulação dos gradientes ocorre antes, pelas hipóteses geométricas (c); o método matemático não foi acionado nessa fase simplista primária (e).
**O que lembrar para a prova:** Conservação de massa + Desenvolvido (elimina $x$) + 2D (elimina $z$) = Apenas $v$ variando em $y$ sobra, mas que depois será isolada e nula.
**Fonte:** Resumo Oficial, Passo 4a.

**Questão 4.2.** 
**Resposta correta:** (b)
**O que a questão está perguntando:** A razão mecânica da completa ausência do componente inerente de aceleração (quantidade de movimento) em Navier-Stokes.
**Explicação passo a passo:** 
No Passo 4b, o documento mostra que a aceleração global é a soma da taxa de variação no tempo (nula devido à hipótese de ser "permanente") e as derivadas longitudinais de deslocamento convectivo (nulas pela condição puramente "desenvolvida"). Sem variação global, resta no sistema o embate cru entre o motor (pressão) e o freio (atrito viscoso da parede).
**Por que as demais estão erradas:**
A declividade livre aponta para arrasto gravitacional rechaçado no passo anterior (a). A parede tranca parte das correntes, mas não paralisa o fluido integralmente (c). Forças de corpo estão riscadas/ignoradas, logo não compensam nada (d).
**O que lembrar para a prova:** Totalmente desenvolvido + Permanente = Sem Aceleração. Navier-Stokes reduz-se a: Força de Pressão = Força Friccional.
**Fonte:** Resumo Oficial, Passo 4b e Resumo Ultra-Rápido.

**Questão 4.3.** 
**Resposta correta:** (d)
**O que a questão está perguntando:** Pela parábola ilustrada na lousa, em que coordenada ocorre o valor mais extremo da velocidade do duto?
**Explicação passo a passo:** 
A dedução algébrica ancorada em $C_1$ e $C_2$ (Passos 5b e 6b) traça a equação de Poiseuille em que as pontas de bloqueio físico tangenciam a placa fixa e sofrem restrição de contato ($u=0$). Sendo assim, é no coração central do hiato estrutural ($y = a/2$), o local de menor cisalhamento estático oriundo das paredes laterais opostas, que se manifesta o vetor azul principal ($u_{max}$).
**Por que as demais estão erradas:**
Nas beiradas da matriz superior e basal impera o não-escorregamento ($u=0$), vetando a ocorrência de limites propulsivos no contorno.
**O que lembrar para a prova:** No fluxo de Poiseuille o perfil é parabólico; logo, a velocidade é nula nas bordas e atinge o máximo (pico da parábola) perfeitamente no centro geométrico.
**Fonte:** Resumo Oficial, Seção 8 (Dica visual da lousa e equação final).

**Questão 4.4.** 
**Resposta correta:** (b)
**O que a questão está perguntando:** Qual restrição puramente matemática se associou ao fato de o fluido "não escorregar" sobre superfícies rígidas.
**Explicação passo a passo:** 
A imposição conceitual dita que a água na interface direta obedece ao vetor veloz e orientacional do artefato estático (chapa/parede). Como as paredes descritas nesse escoamento pressionado não realizam arrasto rotatório nem propulsor (estão estáticas), a água fixada a elas perde impulso ($u=0$) nos patamares extremos delimitadores $y=0$ (chão) e $y=a$ (teto).
**Por que as demais estão erradas:**
O plano estático prescinde de escorregamento transversal. E a restrição não anula a velocidade só num instante passageiro $t=0$ (pois o fluxo é permanente).
**O que lembrar para a prova:** Condição de não-escorregamento significa que Velocidade do fluido na parede = Velocidade da parede (que é zero em dutos conduzidos por pressão).
**Fonte:** Resumo Oficial, Passo 3.

**Questão 4.5.** 
**Resposta correta:** (a)
**O que a questão está perguntando:** Qual é o pressuposto algébrico formal do método de separação de variáveis utilizado durante a dedução da fórmula.
**Explicação passo a passo:** 
No Passo 4b (e resumo Ultra-Rápido), o material descreve exaustivamente esse embate analítico: ao reduzir Navier-Stokes a dois grupamentos onde um é estritamente de pressões longitudinais $f(x)$ e o outro unicamente transversal tangencial $\mu f(y)$, a igualdade eterna entre as expressões que dependem de variáveis alheias é possível somente sob a limitação de que ambos os componentes não flutuam e perfazem constantes lineares numéricas ($= const.$).
**Por que as demais estão erradas:**
O método foca equações diferenciais, não possuindo vinculação à gravitação projetada (b), ao arranjo de fluidos compressíveis ou paralelos (c), ou mera subtração de chapas para arrancar propriedades do duto original (e). Ele também operou primariamente na quantidade de movimento e não na continuidade (d).
**O que lembrar para a prova:** Separação de Variáveis: Se uma função que só depende de $x$ é igual a outra que só depende de $y$, então ambas obrigatoriamente precisam ser iguais a uma *constante*.
**Fonte:** Resumo Oficial, Passo 4b e Resumo Ultra-Rápido.

---

### Questão 5 — Cálculo de Análise Dimensional

**Resposta correta:**
A demonstração dos 6 passos chega no Número de Reynolds: $Re = \frac{\rho u D}{\mu}$.

**O que a questão está perguntando:**
Solicita a aplicação passo a passo do Teorema de Buckingham-Pi para extrair um parâmetro adimensional (Pi) de um escoamento em duto, usando as variáveis $\rho, u, D, \mu$.

**Explicação passo a passo:**

**Passo 1: Variáveis envolvidas ($n$)**
O sistema possui 4 variáveis dimensionais:
$u$ (velocidade), $D$ (diâmetro), $\mu$ (viscosidade), $\rho$ (densidade). Logo, $n = 4$.

**Passo 2: Dimensões primárias ($m$)**
Em MLT, as variáveis possuem as dimensões:
- $\rho = M L^{-3}$
- $u = L T^{-1}$
- $D = L$
- $\mu = M L^{-1} T^{-1}$
As bases em uso são Massa (M), Comprimento (L) e Tempo (T). Logo, $m = 3$.

**Passo 3: Número de Grupos Pi ($\Pi$)**
Subtraímos: $\Pi = n - m \rightarrow 4 - 3 = 1$ grupo adimensional ($\pi_1$).

**Passo 4: Variáveis repetitivas e não-repetitivas**
Escolhe-se 3 variáveis para repetir. Por costume (e facilidade geométrica, cinemática e dinâmica), as repetitivas são $\rho, u, D$. A variável restante (não-repetitiva) é a viscosidade $\mu$.

**Passo 5: Formação do grupo $\pi_1$**
Montamos a relação:
$\pi_1 = \mu \cdot \rho^a \cdot u^b \cdot D^c$

**Passo 6: Resolução dos expoentes**
Substituímos as dimensões:
$M^0 L^0 T^0 = [M L^{-1} T^{-1}] \cdot [M L^{-3}]^a \cdot [L T^{-1}]^b \cdot [L]^c$

Agrupando M, L e T:
- **Para M:** $0 = 1 + a \rightarrow a = -1$
- **Para T:** $0 = -1 - b \rightarrow b = -1$
- **Para L:** $0 = -1 - 3a + b + c$

Substituindo $a$ e $b$ na equação de L:
$0 = -1 - 3(-1) + (-1) + c$
$0 = -1 + 3 - 1 + c$
$0 = 1 + c \rightarrow c = -1$

**Montagem final:**
Aplicando os expoentes $a=-1$, $b=-1$, $c=-1$:
$\pi_1 = \mu \cdot \rho^{-1} \cdot u^{-1} \cdot D^{-1} = \frac{\mu}{\rho u D}$

*(Nota: É perfeitamente comum inverter toda a fração para formatar o parâmetro final, obtendo o consagrado Número de Reynolds, $Re = \frac{\rho u D}{\mu}$. Ambas as formas são adimensionais válidas, mas o Reynolds é a resposta padrão em fluidos).*

**Por que a resposta está correta:**
Substituindo as unidades na resposta final, elas se anulam perfeitamente (resultando em grandeza escalar 1), provando que é um parâmetro adimensional válido.

**O que lembrar para a prova:**
Para agrupar $\mu$ com as propriedades do duto e fluido, o agrupamento sempre apontará para o Número de Reynolds ($Re = \frac{\rho V L}{\mu}$). Lembre-se da ordem de escolher as repetitivas (geralmente Geometria, Velocidade, Densidade).

**Fonte:**
Resumo Oficial, Conhecimento prévio exigido de Análise Dimensional de Fluidos. (Não há desenvolvimento explícito do Buckingham-Pi nas seções do material 6, mas **PENDENTE DE CONFIRMAÇÃO NO MATERIAL** quanto à página original que exigiu esse passo a passo como questão fixa da avaliação).