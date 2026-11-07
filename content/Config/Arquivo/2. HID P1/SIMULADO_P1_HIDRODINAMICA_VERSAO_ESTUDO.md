# Simulado P1 de Hidrodinâmica I — Versão de Estudo

> **Direcionamento:** Baseado nas orientações orais do professor em sala de aula (`Bizu hidroVoz 261030_104750_original.txt` e `direcionamento_do_professor_prova_1.txt`)  
> **Conferência Técnica:** Alinhado rigorosamente às fontes oficiais da disciplina (`SIMULADO_P1_DIRECIONAMENTO_PROFESSOR.md` e `SIMULADO_P1_DIRECIONAMENTO_PROFESSOR_GABARITO_COMENTADO.md`)  
> **Estrutura:** Questões de Múltipla Escolha (Q1 a Q5), Completar Lacunas (Q6), Verdadeiro ou Falso (Q7) e Cálculo Fixo Reservado (Q8).

---

## Bloco 1 — Questões de Múltipla Escolha

---

### Questão 1 — Escoamento Incompressível em Duto Divergente

Considere o escoamento permanente de água líquida através de um duto divergente ($\frac{dA}{dx} > 0$), admitindo escoamento unidimensional na direção axial $x$ com velocidade positiva ($u(x) > 0$) e fluido incompressível ($\rho = \text{constante}$).

A respeito do comportamento da velocidade, da aceleração local e da aceleração convectiva da partícula fluida ao longo do duto, assinale a alternativa **correta**:

- [A] Por se tratar de um escoamento em regime permanente ($\frac{\partial u}{\partial t} = 0$), a aceleração total da partícula fluida é identicamente nula ($\frac{Du}{Dt} = 0$), de modo que a velocidade permanece invariável ao longo do duto.
- [B] Pela conservação da massa ($Q = A(x) \cdot u(x) = \text{constante}$), o aumento da área transversal acarreta a diminuição da velocidade axial ($\frac{\partial u}{\partial x} < 0$). Como o regime é permanente ($\frac{\partial u}{\partial t} = 0$), a aceleração local é nula e a aceleração convectiva $a_{\text{conv}} = u \frac{\partial u}{\partial x}$ é negativa, caracterizando a desaceleração da partícula fluida.
- [C] A expansão da área transversal provoca aumento da velocidade no sentido do escoamento ($\frac{\partial u}{\partial x} > 0$), gerando uma aceleração convectiva positiva ($a_{\text{conv}} > 0$).
- [D] Em escoamentos unidimensionais de trajetória retilínea, o termo convectivo é sempre nulo, de forma que variações de velocidade só podem ocorrer se houver aceleração local ($\frac{\partial u}{\partial t} \neq 0$).
- [E] A velocidade axial é constante em qualquer seção do duto divergente, pois a hipótese de fluido incompressível impede variações espaciais do campo de velocidades.

---

### Questão 2 — Equação da Continuidade e Densidade Absoluta

A Equação da Continuidade para o escoamento tridimensional incompressível de água líquida é expressa em coordenadas cartesianas por:

$$\nabla \cdot \mathbf{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$

Assinale a alternativa que explica **corretamente** por que a **densidade absoluta** (massa específica $\rho$) não figura explicitamente nessa equação:

- [A] Porque a lei de conservação da massa deixa de ser aplicada a fluidos incompressíveis, sendo substituída pela conservação da energia mecânica.
- [B] Porque a massa específica da água é numericamente pequena em relação às velocidades e foi desprezada por simplificação.
- [C] Porque, sendo o fluido incompressível, a massa específica $\rho$ é constante no espaço e no tempo, o que anula sua derivada temporal ($\frac{\partial \rho}{\partial t} = 0$) e permite que $\rho$ seja fatorada para fora das derivadas espaciais ($\rho \nabla \cdot \mathbf{V} = 0$); dividindo ambos os membros por $\rho \neq 0$, a densidade é cancelada algebricamente.
- [D] Porque a densidade absoluta foi convertida em peso específico ($\gamma = \rho g$), grandeza que substitui a massa na equação da continuidade.
- [E] Porque o cancelamento da densidade absoluta só é matematicamente válido para escoamentos unidimensionais, mantendo-se $\rho$ presente no caso tridimensional genérico.

---

### Questão 3 — NÃO SERÁ COBRADA (Posição Oficial do Professor)

> [!NOTE]
> **Status:** O professor informou oralmente em sala que não irá cobrar esta questão ("*E o terceiro, não vou falar*").  
> A numeração original foi preservada para manter a correspondência com a prova e as anotações. Não há conteúdo nem questão substituta para esta posição.

---

### Questão 4 — Segunda Lei de Newton e Força de Pressão

Considere a aplicação da Segunda Lei de Newton a um elemento diferencial de fluido de volume $dVol = dx\,dy\,dz$. As forças normais compressivas de pressão atuantes nas faces opostas na direção $x$ são dadas por:
- Face de entrada (em $x$): $F_{\text{in}} = + p\,dy\,dz$ (sentido $+x$);
- Face de saída (em $x + dx$): $F_{\text{out}} = - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$ (sentido $-x$).

A respeito da força resultante diferencial de pressão e da força de pressão por unidade de volume, assinale a alternativa **correta**:

- [A] A força resultante diferencial é $dF_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$ e a força por unidade de volume é $f_{p,x} = -\frac{\partial p}{\partial x}$. O sinal negativo decorre do fato de a pressão externa atuar sempre de modo compressivo, empurrando a face de saída no sentido negativo ($-x$).
- [B] A força resultante diferencial é $dF_{p,x} = +\frac{\partial p}{\partial x}dx\,dy\,dz$ e a força por unidade de volume é $f_{p,x} = +\frac{\partial p}{\partial x}$, com sinal positivo.
- [C] A força diferencial de pressão nas faces opostas anula-se identicamente pelo Princípio de Pascal, restando apenas forças viscosas.
- [D] A força resultante diferencial é $dF_{p,x} = -\frac{\partial p}{\partial x}$ e a força por unidade de volume é $f_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$, invertendo-se as grandezas física e volumétrica.
- [E] O termo de gradiente de pressão $-\frac{\partial p}{\partial x}$ só atua em gases compressíveis, anulando-se em escoamentos de líquidos incompressíveis.

---

### Questão 5 — Condições de Contorno Cinemáticas em Fronteiras Sólidas

Nas soluções das equações diferenciais de escoamento ao longo de fronteiras sólidas rígidas e impermeáveis, aplicam-se condições de contorno cinemáticas no campo de velocidades.

A respeito dessas condições, assinale a alternativa **correta**:

- [A] A condição de não-escorregamento anula a velocidade normal relativa e a impenetrabilidade anula a velocidade tangencial relativa.
- [B] Em fluidos ideais invíscidos ($\mu = 0$), a condição de não-escorregamento é plenamente satisfeita na fronteira sólida, gerando tensões de cisalhamento.
- [C] A **condição de impenetrabilidade** estabelece que a componente de velocidade normal relativa através da parede sólida é nula ($\mathbf{V}_{\text{rel}} \cdot \mathbf{n} = 0$), impedindo o escoamento através da fronteira; e a **condição de aderência (não-escorregamento)** estabelece que a componente de velocidade tangencial relativa na parede é nula ($\mathbf{V}_{\text{rel}} \times \mathbf{n} = \mathbf{0}$), de modo que o fluido viscoso adquire a velocidade tangencial da superfície sólida.
- [D] As condições de aderência e impenetrabilidade são condições dinâmicas de tensões, não impondo restrições diretas às velocidades na parede.
- [E] A condição de aderência decorre da ação da gravidade e aplica-se indistintamente a fluidos viscosos e a fluidos ideais invíscidos.

---

> [!WARNING]
> **Pendência Documentada (Bloco de Múltipla Escolha):**  
> O professor anunciou oralmente cinco questões de múltipla escolha ("*São 5 múltiplas escolhas aí tá ah?*"). Contudo, declarou expressamente sobre a terceira: "*E o terceiro, não vou falar*". Dessa forma, identificam-se apenas **quatro conteúdos efetivos** (Q1, Q2, Q4 e Q5). Em estrito cumprimento à regra de não inventar questões, a 3ª posição permanece não preenchida como pendência oficial de confirmação com o docente.

---

## Bloco 2 — Questão de Completar Lacunas

---

### Questão 6 — Conceitos Estruturantes de Hidrodinâmica I

Preencha as lacunas das frases curtas e diretas abaixo utilizando a terminologia técnica das fontes oficiais da disciplina:

1. No estudo de análise dimensional da hidrodinâmica naval no sistema $MLT$, destacam-se propriedades físicas como a massa específica ($\rho$, $[ML^{-3}]$), a viscosidade dinâmica ($\mu$, $[ML^{-1}T^{-1}]$), a pressão ($p$, $[ML^{-1}T^{-2}]$) e a ________________________________________ ($\sigma$, $[MT^{-2}]$).
2. O princípio da conservação da massa aplicado a um volume de controle infinitesimal fixo no espaço dá origem à Equação da ________________________________________.
3. Na perspectiva cinemática ________________________________________, o escoamento é observado fixando-se coordenadas espaciais estáticas $(x, y, z)$ no espaço ao longo do tempo.
4. Na perspectiva cinemática ________________________________________, o escoamento é analisado acompanhando-se o movimento de partículas fluidas individuais ao longo de suas trajetórias.
5. De acordo com a derivada material na concepção euleriana, a aceleração total de uma partícula fluida decompõe-se na aceleração ________________________________________ (variação temporal no ponto fixo) e na aceleração ________________________________________ (variação espacial devida ao deslocamento no campo).
6. As forças que atuam sobre um elemento diferencial de fluido dividem-se em forças de ________________________________________ (como pressão e tensões cisalhantes viscosas nas fronteiras) e forças de ________________________________________ (como o peso gravitacional agindo sobre a massa à distância).
7. O escoamento laminar permanente de fluido viscoso entre duas placas planas paralelas conduzido por ________________________________________ denomina-se escoamento plano de ________________________________________. *(Nota: item com ambiguidade documental registrada no direcionamento oral).*
8. O número adimensional de ________________________________________ representa a razão entre as forças de inércia e as forças ________________________________________. *(Nota: item com ambiguidade documental registrada no direcionamento oral).*
9. Os ensaios em tanques de provas consistem na medição de forças em um ________________________________________ (em escala reduzida) para extrapolação ao ________________________________________ (navio real em escala plena).
10. Na similaridade cinemática entre modelo e protótipo, a razão entre as velocidades de partículas ou pontos correspondentes é rigorosamente ________________________________________ ($V_m / V_p = \text{constante}$), sendo essas posições espacialmente correspondentes denominadas formalmente ________________________________________.

---

## Bloco 3 — Questão de Verdadeiro ou Falso

---

### Questão 7 — Princípio da Homogeneidade e Teorema $\Pi$ de Buckingham (Teoria Pura)

Julgue as afirmações a seguir em **Verdadeiro (V)** ou **Falso (F)**:

- [ ] **Item 7.1:** Pelo Princípio da Homogeneidade Dimensional, todos os termos aditivos de uma equação que descreve um fenômeno físico válido devem possuir rigorosamente as mesmas dimensões primárias fundamentais ($MLT$ ou $FLT$).
- [ ] **Item 7.2:** O procedimento formal de adimensionalização de uma equação consiste em dividir cada termo por uma combinação de variáveis que possua as mesmas dimensões físicas desses termos, convertendo coeficientes e variáveis em parâmetros adimensionais.
- [ ] **Item 7.3:** De acordo com o Teorema $\Pi$ de Buckingham, se um fenômeno físico envolve $n$ variáveis dimensionais e $m$ dimensões primárias, o número exato de agrupamentos adimensionais independentes ($k$) é dado pela soma algébrica $k = n + m$.
- [ ] **Item 7.4:** Na identificação das dimensões primárias fundamentais ($m$) para problemas de hidrodinâmica naval, adota-se tipicamente o sistema $MLT$, composto pelas três dimensões fundamentais massa ($M$), comprimento ($L$) e tempo ($T$).
- [ ] **Item 7.5:** Na seleção das variáveis repetidas (Etapa 4 de Buckingham), é permitido escolher três variáveis puramente geométricas (como comprimento, largura e raio), pois a exigência de conter todas as dimensões primárias só é verificada após a resolução dos expoentes.
- [ ] **Item 7.6:** Na determinação dos expoentes das variáveis repetidas (Etapa 6 de Buckingham), impõe-se que cada grupo $\Pi$ seja estritamente adimensional, atribuindo-se expoentes nulos ($M^0 L^0 T^0$) às dimensões fundamentais para a montagem do sistema algébrico de equações lineares.

---

## Bloco 4 — Cálculo Fixo

---

### Questão 8 — CÁLCULO FIXO — SEIS PASSOS

> [!IMPORTANT]
> **VAGA RESERVADA PARA O CÁLCULO CANÔNICO EM SEIS PASSOS:**  
> Conforme a orientação expressa do professor em sala de aula ("*a oitava é aquela questão de cálculo que a gente fez aqui... cálculo dos 6 passos*"), esta questão é fixa e reservada para o exercício de aplicação prática do método de Buckingham–$\Pi$.  
> O espaço permanece preservado sem alteração de enunciado ou substituição por outro cálculo.