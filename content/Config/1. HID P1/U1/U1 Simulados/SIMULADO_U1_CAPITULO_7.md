# Simulado de Hidrodinâmica — Unidade 1 — Capítulo 7

---

### 1ª Questão — Assinale a alternativa correta.

Analise as afirmativas abaixo referentes ao escoamento plenamente desenvolvido em canal inclinado dominado por forças de corpo, conforme deduzido no material:

**I.** No escoamento de um fluido em canal inclinado estudado, uma das hipóteses assumidas é que o escoamento é permanente e bidimensional.
**II.** A condição de contorno de impenetrabilidade impõe que a velocidade tangencial do fluido ao longo da direção do escoamento seja nula nas paredes.
**III.** O grande diferencial do modelo adotado neste capítulo em relação aos cenários horizontais simples é a atuação ativa e explícita da força de corpo ($\rho g_x \neq 0$).
**IV.** Graças a uma substituição geométrica, o termo motriz do escoamento passa a aglutinar tanto o gradiente de pressão quanto o termo gravitacional, sendo expresso pela derivada parcial $\frac{\partial(p + \rho g h)}{\partial x}$.
**V.** A equação deduzida indica que a velocidade máxima no miolo do canal inclinado diminui à medida que a inclinação do canal ($\theta$) aumenta e a viscosidade reduz.

**São corretas:**

- (a) I, II e IV.
- (b) I, III e IV.
- (c) II, IV e V.
- (d) III, IV e V.
- (e) I, III e V.

---

### 2ª Questão — Complete as Lacunas

Preencha as lacunas das frases abaixo utilizando os conceitos e termos correspondentes.

1. O sistema de coordenadas define a direção $h$ alinhada exclusivamente com a _________.

2. A hipótese de escoamento incompressível estabelece que a densidade do fluido $\rho$ seja _________.
3. O modelo no Capítulo 7 destaca explicitamente que, em um canal inclinado, existem forças de _________ ($\rho g_x \neq 0$).
4. A condição que afirma não existirem velocidades perpendiculares às paredes ($v = 0$) é a condição de contorno de _________.
5. Através da Lei de Conservação da _________, conclui-se que $\partial v / \partial y = 0$ para esse escoamento bidimensional e totalmente desenvolvido.
6. A componente longitudinal da força da gravidade projetada na direção do escoamento é expressa por $g_x = g \sin$ _________.
7. Na dedução da equação motriz, a razão para se trocar o seno é para poder reescrever a força da ladeira acoplada à derivada em relação a _________.
8. Na modelagem de Navier-Stokes para esse caso, a equação evidencia o balanço propulsor da pressão e do peso agrupados na derivada parcial $\frac{\partial(p + \rho g h)}{\partial x}$, considerada _________.
9. O perfil de velocidades assumido pelo fluido no interior do canal fechado e inclinado é geometricamente _________.
10. Segundo a equação final adaptada para o canal, mantendo-se os outros parâmetros inalterados, quanto menor for a _________ do fluido, maior será a velocidade máxima alcançada.

---

### 3ª Questão — Verdadeiro ou Falso

Classifique as afirmativas abaixo como Verdadeiras (V) ou Falsas (F).

(  ) 1. O escoamento tratado no Capítulo 7 considera o canal inclinado, onde as coordenadas $x$ e $y$ acompanham a parede inclinada, e a coordenada $h$ atua como o eixo vertical estrito gravitacional.

(  ) 2. No procedimento adotado para esse canal inclinado, as forças de corpo não são negligenciadas, significando que a gravidade empurra ativamente o fluido ladeira abaixo.

(  ) 3. A condição de não escorregamento é aplicada em $y=0$ e $y=a$, e estipula que as velocidades perpendiculares $v$ sejam nulas nas paredes.

(  ) 4. Ao integrar a equação da continuidade para esse perfil, encontra-se que a velocidade $v$ tem um perfil linear que atinge um valor máximo e constante no centro do canal.

(  ) 5. A Lei da Conservação da Quantidade de Movimento (Navier-Stokes) reduz-se no eixo $x$ a uma igualdade entre o cisalhamento viscoso e a soma dos diferenciais de pressão e gravidade.

(  ) 6. A hipótese de escoamento totalmente desenvolvido implica que as componentes da velocidade não se alteram mais conforme se avança ao longo do tubo, eliminando a aceleração convectiva $\partial u/\partial x$.

(  ) 7. Na equação simplificada, a substituição trigonométrica do termo de seno por $-dh/dx$ impede matematicamente que a força gravitacional seja incorporada à derivada da pressão, dificultando o agrupamento algebraico.

(  ) 8. Após realizar duas integrações espaciais da equação de Navier-Stokes, obtém-se as constantes $C_1$ e $C_2$, cujos valores são determinados respectivamente pela adoção da condição de não escorregamento nos contornos.

(  ) 9. Diferentemente do caso horizontal genérico, a velocidade máxima desenvolvida por esse escoamento ladeira abaixo não sofre qualquer aumento ao se ampliar a declividade angular $\theta$.

(  ) 10. Apesar da tese principal utilizar fielmente a notação em $\theta$, constata-se no registro original de aula uma disparidade ilustrativa que denotou o ângulo de peso como $\phi$ na lousa.

---

### 4ª Questão — Múltipla Escolha

Selecione a alternativa correta para cada uma das questões a seguir.

**Questão 4.1.** Sobre as forças de corpo no escoamento equacionado no Capítulo 7, assinale a constatação correta:

(a) Foram abandonadas da modelagem em prol de viabilizar a integração analítica 2D.
(b) São matematicamente anuladas pela vigência da hipótese de escoamento em regime permanente.
(c) Atuam transversalmente ao canal alinhadas ao eixo $y$, provocando severa compressibilidade nas paredes.
(d) São explicitamente destacadas no equacionamento ($\rho g_x \neq 0$), consolidando o vetor motriz gravitacional que propulsiona a massa pelo declive.
(e) São convertidas estritamente em energia térmica para dissipar a velocidade excedente gerada pelo plano inclinado.

**Questão 4.2.** De que modo a conservação da massa governa o escoamento nesse modelo plenamente desenvolvido e bidimensional?

(a) A densidade do gás atua inflando a vazão progressivamente à medida que ele escorre e absorve força gravitacional.
(b) A equação simplifica-se ao balanço $\partial v/\partial y = 0$, que, casado com a condição de contorno de impenetrabilidade, atesta inexistir escoamento normal ($v=0$) em toda a secção transversal.
(c) O empuxo na ladeira faz com que o fluxo passe de estado laminar estacionário a uma propagação turbulenta de perfil oscilatório.
(d) A velocidade motriz principal $u$ tem de atingir marca zero nas extremidades unicamente para satisfazer ao balanço inercial na coordenada $z$.
(e) O escoamento gera uma concentração residual de massa próxima à superfície $y=0$ motivada pela aderência tridimensional.

**Questão 4.3.** A substituição algébrica do fator $\sin\theta$ por $-dh/dx$ promoveu um recurso analítico essencial. Qual foi a principal finalidade dessa relação?

(a) Segregar as parcelas motrizes para se observar isoladamente se o propulsor exclusivo é a bomba ou se o canal funciona apenas por queda natural.
(b) Redirecionar todo o cálculo vetorial de forma a alinhar integralmente o eixo $y$ com o baricentro gravitacional e anular as componentes laterais.
(c) Congregar o impulso gravitacional projetado sob a mesma derivada parcial da pressão ao longo de $x$, estruturando o termo trator total único $\partial(p+\rho g h)/\partial x$.
(d) Fornecer lastro dimensional que validasse as restrições impostas por Navier-Stokes relativas às condições limites do escoamento não-aderente.
(e) Promover um desvio que justificasse a compressibilidade repentina da água ao ganhar cota negativa durante o declive intenso.

**Questão 4.4.** Baseando-se na equação da velocidade estruturada para o declive, $u = \frac{1}{2\mu}\frac{\partial(p+\rho g h)}{\partial x}(y^2 - ay)$, o que se constata quanto às variáveis de influência?

(a) Desenha um perfil linear cujas inclinações são estritamente regidas pela função da aderência de Poiseuille e pela densidade transiente.
(b) O perfil alcançado revela velocidade mínima exatamente na linha central imaginária e cristas maximizadas aderidas na parede adjacente aos pontos 0 e $a$.
(c) Trata-se de uma parábola concisa de fluxo impulsionado cuja intensidade de deslocamento cresce com o aumento do declive angular e regride à medida que o arrasto do fluido espesso amplia (maior $\mu$).
(d) Trata-se de um vetor cuja derivada angular demonstra que o fluido ganha aceleração infinitamente graças a estagnação perene da inércia em condutos descendentes verticais puros.
(e) Comprova que a ladeira freia dinamicamente a coluna d'água ao instigar conflito direto com as pressões de recalque.

**Questão 4.5.** Quais condições supressoras embasaram a eliminação sistêmica das parcelas da aceleração conectiva/inercial inerentes na expansão de Navier-Stokes desse modelo laminar?

(a) A ausência de tridimensionalidade e as considerações generalistas que desprezaram inteiramente as massas fluidas viscosas.
(b) Apenas a atuação irredutível das paredes que freiam localmente o avanço temporal das camadas perimetrais do fluido.
(c) Escoamento fixado em regime totalmente desenvolvido (onde $\partial u/\partial x = 0$) atrelado ao formato bidimensional que silencia o eixo $z$ ($w=0$), eliminando a convectividade da força e estabilizando o fluxo.
(d) A conversão imposta pela impenetrabilidade lateral da lâmina combinada à incompressibilidade global transicional que desidratou a aceleração angular vetorialmente.
(e) O cancelamento da pressão nominal pela ação direta imposta pela gravidade anuladora operando exclusivamente em $y$.

---

### 5ª Questão — Cálculo de Análise Dimensional

Avalie a dinâmica de comportamento do escoamento da água no interior de um duto circular de diâmetro D, sendo a densidade e a viscosidade da água parâmetros conhecidos.

Considere as variáveis dimensionais do problema como a velocidade $u$, o diâmetro $D$, a viscosidade $\mu$ e a densidade $\rho$.

Utilize o método de Buckingham-Π para determinar o grupo adimensional resultante, estruturando a sua resolução nos seis passos fundamentais.

<br><br>

---

# Gabarito Comentado — Respostas Corretas e Incorretas

### Questão 1 — Marque X

**Resposta correta:** (b) I, III e IV.

- **I. Verdadeira:** A modelagem estabelece como passos fundamentais a atuação de um modelo permanente ($\partial(.)/\partial t=0$) e bidimensional ($w=0, \partial(.)/\partial z=0$).
- **II. Falsa:** A condição de contorno que impõe velocidade tangencial nula nas paredes estacionárias ($u=0$) não se trata da impenetrabilidade, mas sim do **não escorregamento**. (A impenetrabilidade anula a velocidade ortogonal, normal ao anteparo físico).
- **III. Verdadeira:** A novidade apresentada na estrutura motriz desse equacionamento é o destaque à vigência de uma força de corpo atuante ($\rho g_x \neq 0$) sobre uma geometria inclinada.
- **IV. Verdadeira:** Substituindo a relação do $\sin\theta = -dh/dx$, a matemática acopla as forças e unifica o gradiente motriz integral na derivada parcial sobre $x$ da energia de $(p + \rho g h)$.
- **V. Falsa:** O arcabouço deduzido afirma claramente a proporção direta para o declive: "quanto *maior* for a inclinação do canal ($\theta$), *maior* a velocidade máxima", e para a resistência: "quanto *menor* a viscosidade, maior a velocidade máxima".

### Questão 2 — Complete as Lacunas

1. **gravidade**: Como demonstrado no Passo 1, a direção auxiliar $h$ atua de forma perfeitamente alinhada com o prumo magnético gravitacional descensional em vez do fundo plano.
2. **constante**: A premissa de um fluido atuar de modo incompressível consolida intrinsecamente um $\rho = \text{constante}$.
3. **corpo**: Trata-se da matriz motriz externa que diferiu a etapa atual, acionando uma tração paralela descrita como a força de corpo atuante volumétrica.
4. **impenetrabilidade**: Definição literal exposta no Passo 3, impõe o valor de $v=0$ vedando assim qualquer vazamento trans-material perpendicular.
5. **Massa**: O balanço de massas unidimensional expõe perfeitamente o corte no interior limitando as derivadas e entregando a afirmação $v=0$ de forma constante analiticamente.
6. **$\theta$**: A relação projeta com exatidão a componente $x$ descendente com trigonometria plana $g_x = g \sin\theta$.
7. **$x$**: Como a pressão opera derivada na variável estrutural $x$, o termo $dh/dx$ consolida um encaixe operatório fluído e exato ao longo da base.
8. **constante**: Essa união motora unificada torna-se uma razão equacionável constante capaz de se equiparar às segundas integrações parciais no plano espacial transversal sem sofrer restrições transitórias.
9. **parabólico**: A geometria algébrica da velocidade expressa pela curva dupla $u(y)$ engloba variáveis de equação formadoras de concha parabólica pura na saída matemática.
10. **viscosidade**: O coeficiente que representa o fator estático reverso. Em relação geométrica ao vetor principal quanto mais fina for (menor densidade atrativa de camadas), mais avanço impõe.

### Questão 3 — Verdadeiro ou Falso

**Sequência correta:** V, V, F, F, V, V, F, V, F, V

- **1. (V) Verdadeira.** A separação dos eixos foi crucial na explicação do professor, delimitando $x$ para o fluido e $h$ unicamente vertical.
- **2. (V) Verdadeira.** O passo da dedução faz referência imediata a existência atuante ($\rho g_x \neq 0$).
- **3. (F) Falsa.** *Correção:* A condição de não escorregamento determina que as velocidades **tangenciais** (no eixo $x$ ou seja, o $u$, e no eixo $z$ transversamente) sejam iguais as da parede. A perpendicular $v$ provém da impenetrabilidade.
- **4. (F) Falsa.** *Correção:* Ao integrar, encontra-se que $v = 0$ ao longo de absolutamente todo o espaço do tubo.
- **5. (V) Verdadeira.** Exatamente. O balanço do lado que permaneceu em Navier-Stokes representa a disputa entre a viscosidade frenante e a soma empurradora da ladeira e da pressão.
- **6. (V) Verdadeira.** Em escoamento sem aceleração convectiva ($\partial u/\partial x = 0$) a inércia deixa de atuar porque o formato linear da velocidade lateral se fixou estavelmente.
- **7. (F) Falsa.** *Correção:* Muito pelo contrário; a substituição trigonométrica foi feita unicamente e **propositalmente** para englobar a gravidade dentro da mesma derivada da pressão de forma algébrica.
- **8. (V) Verdadeira.** O passo a passo matemático mostra $C_2$ e $C_1$ retirados diretamente na borda onde se aplica que em $y=0$ a velocidade zera e $y=a$ igualmente.
- **9. (F) Falsa.** *Correção:* A fórmula dita que quanto maior a declividade angular, maior a capacidade e velocidade final descensional devido à gravidade.
- **10. (V) Verdadeira.** O professor anotou $\phi$ no rascunho de tela, porém registrou e prosseguiu em todas as deduções textualmente na variável $\theta$, preservada integralmente nas equações base.

### Questão 4 — Múltipla Escolha

**Questão 4.1.** Alternativa correta: **(d)**
- (a) Não foram abandonadas, são o destaque do capítulo.
- (b) A permanência afeta o transiente temporal $\partial/\partial t$, e não a existência estática de campo gravitacional.
- (c) Atuam e geram $g_x$ (o fluxo é inclinado e desce longitudinalmente, não perpendicularmente em colapso nas bordas limitantes laterais).
- (d) Representa perfeitamente a premissa de Navier-Stokes modelada onde o peso atua efetivamente como um trator propulsor não negligenciável ($\rho g_x \neq 0$).
- (e) A força de gravidade provê aceleração e não atua em escoamentos de trocas de fase térmica neste modelo teórico em questão.

**Questão 4.2.** Alternativa correta: **(b)**
- (a) O formato é incompressível e a massa mantêm a densidade estável em vez de inchar pelo escoamento propulsor.
- (b) Cobre com precisão algébrica: a equação $v=C_1$ e o contorno nulo geram a perenidade de que $v=0$ para sempre neste trajeto transversal ao fluxo impulsionado.
- (c) As hipóteses determinam a presença contínua de laminariedade plena na expansão teórica deduzida analiticamente pelo professor, sem oscilações e turbilhões.
- (d) A condição de parede e fronteira (inércia cruzada e limites) obriga a paralisação em $y$ para $u$, não para satisfazer variações e impulsos em um eixo restrito transverso.
- (e) Por ser plenamente incompressível ($\rho=\text{cte}$) não existe transição de massa gerando ilhas localizadas transversas ao longo da parede inferior do trajeto modelado.

**Questão 4.3.** Alternativa correta: **(c)**
- (a) Não separou; unificou-as estritamente em uma engrenagem linear equacionável única.
- (b) Manteve fiel e ortogonal em eixos e isolou vetores sem reestruturar inteiramente e sem anular por completo as forças reais sobre o plano descendente da parede de suporte $y=0$.
- (c) O intuito matemático uniu as frações motoras por partilharem as derivadas longitudinais resultando no agrupamento coerente em torno de um propulsor único no bloco derivativo parcial.
- (d) A aderência de limite independe do grau propulsor (no escorregamento as paredes estão rigorosamente inertes fixas e inalteradas na face do metal, desvinculadas das variáveis motrizes angulares em tela).
- (e) A hipótese incompressível veda que a fase fluida seja considerada termodinamicamente compressível nessa premissa hidrodinâmica específica abordada.

**Questão 4.4.** Alternativa correta: **(c)**
- (a) O formato da curva dita é estritamente de expansão de segunda ordem (parabólica) e o trânsito da densidade está permanente, em constância incompressível unificada em vez de linearizada e transiente solta no campo formador.
- (b) Pelo contrário, os contornos geram e preservam atrito estagnante ($u=0$), deixando a velocidade motriz máxima centralizada livre das paredes aderidas (não-escorregamento operante).
- (c) Expõe o núcleo da dedução do Capítulo 7: a geometria gera uma parábola com centro máximo impulsionado perante a declividade e refratado mediante a restrição da consistência mais viscosa (alta viscosidade).
- (d) Conduto desce alinhado em angulação em vez da plena perpendicular paralela, operando em formato balanceado estático entre trator e aderência ao longo do trecho retilíneo de avanço final sem impulsões contínuas acelerativas em expansão perene não balanceada.
- (e) A ladeira ($g_x = g \sin\theta$) atua propulsionando e tracionando por soma propulsora e não refreando inversamente.

**Questão 4.5.** Alternativa correta: **(c)**
- (a) O fluido mantém sim massa viscosa e a força da área se faz atuante (corpo não nulo ao redor da gravidade formadora do canal avaliado).
- (b) As marginais das estruturas estagnadas (limites e aderência) por si isoladamente na análise vetorial não operam os cancelamentos de massa interconectados nas vias dos desenvolvimentos vetoriais motrizes nas frações analíticas do gradiente central em tela.
- (c) Tradução estrita algébrica para escoamentos laminares permanentes deduzidos: um trajeto permanentemente linear ($\partial/\partial t = 0$), contínuo integral bidimensional ($w=0$), perfeitamente estável desenvolvido na reta contínua transicional ($\partial u/\partial x = 0$) onde todo o vetor motriz de aceleração zera na base convectiva/inercial de Navier-Stokes modelada em classe fechada.
- (d) A ausência tridimensional incompressível e a restrição ao vazamento restritivo transversal normalizado do conjunto atuam colaterais às inércias estritamente unificadas sobre a dimensão x convectiva de propagação tridimensional avaliativa de aceleração do volume real em marcha.
- (e) Cancelamento se deu sobre a inércia e convectividade propulsora do escoamento, e nunca pelo sumiço teórico do agrupador do propulsor da pressão por intermédio das influências do trajeto declivoso gravitacional e descendente modelado.

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
