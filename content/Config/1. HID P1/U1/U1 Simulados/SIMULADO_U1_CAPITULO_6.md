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

- **I. Verdadeira:** No Passo 2, a fonte enuncia exatamente isso: "o escoamento é permanente, ou seja, independente do tempo, $\frac{\partial (.)}{\partial t} = 0$".
- **II. Falsa:** A condição de não escorregamento impõe que a velocidade do fluido seja nula (igual à da parede fixa), ou seja, alcança o valor zero, e não seu "máximo valor absoluto". (Passo 3)
- **III. Falsa:** A resolução é explícita: "a força de pressão é balanceada com a força friccional" (Passo 4b). As forças de corpo ($\rho g_x$) foram isoladas/negligenciadas, não gravitacionais.
- **IV. Verdadeira:** Através da simplificação da equação de massa acoplada à condição de impenetrabilidade nas duas paredes, a fonte conclui no Passo 6a que "em qualquer posição $v = 0$".
- **V. Verdadeira:** A conclusão do Passo 6b crava que "O perfil de velocidades então é parabólico", equação conhecida como Poiseuille.

### Questão 2 — Complete as Lacunas

1. **incompressível**: O Passo 2 associa fluidos que movem-se lentamente à densidade constante ($\rho = const.$), definindo-os como incompressíveis.
2. **permanente**: Ausência de mudança com o transcorrer temporal aciona o regime permanente ($\frac{\partial (.)}{\partial t} = 0$).
3. **escorregamento**: Fenômeno onde a camada fluida se fixa à restrição sólida lindeira. (Passo 3)
4. **impenetrabilidade**: Norma de contorno que cessa componentes normais à área confinante, forçando que em $y=0$ e $y=a$ o fluido não fure as placas ($v=0$).
5. **corpo**: No Passo 2, consta expressamente: "não existem forças de corpo atuando no escoamento, $\rho g_x = 0$".
6. **massa**: Seguindo o roteiro, a conservação de massa atua na vanguarda do raciocínio analítico (Passo 4a).
7. **friccional**: No Passo 4b, o vetor pressórico iguala-se à força friccional retentora que deriva da viscosidade (termo de ordem dois espacial $\mu$).
8. **separação**: O método de separação de variáveis é formalmente nomeado e aplicado após a constatação de dupla independência ($x$ vs $y$).
9. **viscosidade**: Consta na dedução da equação final: "quanto menor a viscosidade maior a velocidades máxima", portanto, inversamente, mais viscosidade tolhe a velocidade.
10. **Poiseuille**: Nome conferido historicamente ao modelo analítico entre placas induzidas por diferença de pressão deduzido no Capítulo 6.

### Questão 3 — Verdadeiro ou Falso

**Sequência correta:** F, F, V, V, F, V, V, F, V, F

- **1. (F) Falsa.** *Correção:* A dica de prova registra exatamente o oposto: o professor assegurou verbalmente que aceitará a grafia simplificada "escoamento desenvolvido" sem retirar nota.
- **2. (F) Falsa.** *Correção:* A primeira lei tratada no Passo 4a é a "Lei de Conservação de massa".
- **3. (V) Verdadeira.** A integração final em "5a" e a impenetrabilidade "6a" decretam a nulidade universal de $v$ para o sistema.
- **4. (V) Verdadeira.** Hipótese descrita matematicamente por $\frac{\partial (.)}{\partial z} = 0$ e $w = 0$ no Passo 2.
- **5. (F) Falsa.** *Correção:* A seção 8 comprova que "o perfil de velocidades então é parabólico", ostentando concavidade não-linear.
- **6. (V) Verdadeira.** O passo 4b justifica a redução a um mero embate pressórico-viscoso exatamente "porque não existe aceleração no escoamento".
- **7. (V) Verdadeira.** A transcrição contém uma anotação confirmando que o bloco de Força de Corpo encontrava-se "anulado por traços vermelhos na fonte".
- **8. (F) Falsa.** *Correção:* $C_1$ e $C_2$ não puderam ser abstraídas; o Passo 6b inteiro relata o emprego da imposição geométrica $y=0$ e $y=a$ para solucionar as constantes de integração ($C_2=0$ e $C_1$ com balanço pressórico).
- **9. (V) Verdadeira.** O texto afirma (Passo 2) que tais premissas consubstanciam as características elementares "de um escoamento laminar".
- **10. (F) Falsa.** *Correção:* O Passo 1 define de forma inequívoca que o cenário envolve "duas paredes estacionárias" controladas por pressão ($p_1 > p_2$).

### Questão 4 — Múltipla Escolha

**Questão 4.1.** Alternativa correta: **(d)**
- **(a) Incorreta:** A hipótese fundamental elencada no material era, na realidade, que o escoamento provava-se incompressível ($\rho = const.$).
- **(b) Incorreta:** A anulação de componentes precede Navier-Stokes, ocorrendo primariamente no âmbito isolado da Continuidade/Massa (Passo 4a).
- **(c) Incorreta:** O eixo $z$ reflete largura transversal em 3D, sendo cortado pela condição global 2D teórica de placa infinita, não se limitando pontualmente a placa $y=0$.
- **(d) Correta:** Descreve em minúcias as alegações descritas no passo 4a, onde a variação temporal ou espacial é dizimada pelos postulados de escoamento constante no desenvolvimento (vetor $u$ no eixo $x$) e no eixo em profundidade ($z$).
- **(e) Incorreta:** O material lida com limites definidos e não utiliza anomalias infinitas como pressão ilimitada para isolar a álgebra da conservação de massa.

**Questão 4.2.** Alternativa correta: **(b)**
- **(a) Incorreta:** A gravidade consta perfeitamente explicitada como nula ($\rho g_x = 0$), sendo ausente e não compensatória.
- **(b) Correta:** O texto expõe no Passo 4b os pormenores: sendo $\frac{\partial u}{\partial t} = 0$ e $u \frac{\partial u}{\partial x} = 0$, anulam-se as taxas locais e convectivas do diferencial, reduzindo-se à premissa de que a aceleração global cessa e atua num balanço estático.
- **(c) Incorreta:** Se o fluido ficasse engessado integralmente estacionário, não existiria velocidade máxima nem um arranjo parabólico ($u_{max}$).
- **(d) Incorreta:** Decorreu de eliminação mecânica das derivadas nulas pelo modelo de desenvolvimento fluido, e não um lapso algébrico de separação.
- **(e) Incorreta:** Navier-Stokes ali repousa na dependência explícita do termo de atrito/viscoso $\mu$, não sendo um estado ideal desprovido do fenômeno newtoniano.

**Questão 4.3.** Alternativa correta: **(d)**
- **(a) Incorreta:** Na placa $y=a$ a equação desfecha em $u=0$ em função da imobilização sólida e aderência local.
- **(b) Incorreta:** A placa em base $y=0$ experimenta zero velocidade da mesma forma ($u=0$).
- **(c) Incorreta:** A impenetrabilidade regula a inibição da faceta normal ($v$), mas a velocidade $u$ continua colapsada por não escorregamento nos domínios laterais.
- **(d) Correta:** O esboço gráfico e a análise parabólica mostram que, livre da tensão obstrutiva direta das paredes, o meio-termo transversal engloba o ápice vetorial veloz (núcleo máximo, $u_{max}$).
- **(e) Incorreta:** Como previamente fixado no material, as forças de corpo sequer operam na indução ($g_x=0$).

**Questão 4.4.** Alternativa correta: **(b)**
- **(a) Incorreta:** Impenetrável denota estritamente obstrução contínua da massa fluida; não há brechas de escape sob pressurização na dedução efetuada.
- **(b) Correta:** O conceito físico delineado no Passo 3 dita que a placa adere o filme hídrico adjacente de modo a compatibilizar as velocidades, o que, com peças imóveis, reflete em $u=0$ para ambos.
- **(c) Incorreta:** O arranjo é balizado por "duas paredes estacionárias" (Passo 1), o que rechaça placas motorizadas.
- **(d) Incorreta:** Os limiares cartesianos que sofrem constrição tangível situam-se do valor nulo ao valor superior $a$ na altura de eixo $y$.
- **(e) Incorreta:** Tange aos limites tangíveis geográficos da parede ao invés de meras faixas temporais.

**Questão 4.5.** Alternativa correta: **(a)**
- **(a) Correta:** Extraída diretamente do Passo 4b/5a; o autor infere matematicamente que dois componentes variando independentemente ($x$ e $y$) sem coligação indireta apenas perfazem igualdade perene caso consubstanciem isoladamente instâncias numéricas fixas (constantes).
- **(b) Incorreta:** É um recurso derivativo integral que flui desatrelado de acelerações da gravidade.
- **(c) Incorreta:** Todo o fluxo subordina-se à modelagem constante da incompressibilidade original e permanente ($\rho = \text{const}$).
- **(d) Incorreta:** A separação pauta a quebra geométrica operada tardiamente em Navier-Stokes (quantidade de movimento), não na conservação mássica.
- **(e) Incorreta:** Transforma as retas tangentes locais e isoladas numa parábola concisa ao reintegrar as taxas duas vezes com os limites $C_1, C_2$.

### Questão 5 — Cálculo de Análise Dimensional

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
