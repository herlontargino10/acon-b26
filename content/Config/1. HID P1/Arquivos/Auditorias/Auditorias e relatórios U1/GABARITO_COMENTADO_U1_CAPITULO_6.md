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
