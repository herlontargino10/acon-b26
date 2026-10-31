# Simulado Oficial de Hidrodinâmica I — P1 (Padrão Direcionamento do Professor)

> **Status:** Versão Revisada Pós-Auditoria — Etapa 2  
> **Fundamentação Estrutural:** [`direcionamento_do_professor_prova_1.txt`](file:///c:/Users/Herlon%20Targino/Documents/quartz/content/Config/2.%20HID%20P1/Resumo_P1/direcionamento_do_professor_prova_1.txt) e [`AUDITORIA_DIRECIONAMENTO_PROFESSOR_P1.md`](file:///c:/Users/Herlon%20Targino/Documents/quartz/content/Config/2.%20HID%20P1/Resumo_P1/AUDITORIA_DIRECIONAMENTO_PROFESSOR_P1.md)  
> **Escopo Documental Auditado:** `Questionário P1.pdf` (DOC-00), Apostilas Teóricas U1 (DOC-01 a DOC-08) e Apostila Teórica U2 (DOC-09)  
> **Estrutura da Avaliação:** 7 questões efetivas nas posições originais Q1 a Q8 (com Q3 formalmente não cobrada).  
> **Instruções ao Estudante:** Leia atentamente o enunciado de cada questão. As questões de múltipla escolha possuem uma única alternativa correta. A Questão 6 deve ser respondida preenchendo as lacunas com os termos técnicos exatos. A Questão 7 requer julgamento de Verdadeiro (V) ou Falso (F). A Questão 8 é reservada para o cálculo canônico em seis passos.

---

## Bloco 1 — Questões de Múltipla Escolha

---

### Questão 1 — Escoamento Incompressível em Duto Divergente

Considere o escoamento de água líquida através de um duto divergente ($\frac{dA}{dx} > 0$) operando em regime permanente, admitindo escoamento unidimensional na direção axial $x$ com velocidade positiva ($u(x) > 0$) e fluido incompressível ($\rho = \text{constante}$).

A respeito do comportamento da velocidade, da aceleração local e da aceleração convectiva da partícula fluida ao longo do duto, assinale a alternativa **correta**:

- [ ] Por se tratar de um escoamento em regime permanente ($\frac{\partial u}{\partial t} = 0$), a aceleração total da partícula fluida é identicamente nula ($\frac{Du}{Dt} = 0$), de modo que a velocidade permanece invariável.
- [ ] Pela conservação da massa ($Q = A(x) \cdot u(x) = \text{constante}$), o aumento da área transversal acarreta a diminuição da velocidade axial ($\frac{\partial u}{\partial x} < 0$). Como o regime é permanente ($\frac{\partial u}{\partial t} = 0$), a aceleração local é nula e a aceleração convectiva $a_{\text{conv}} = u \frac{\partial u}{\partial x}$ é negativa, caracterizando a desaceleração da partícula fluida sob essas condições.
- [ ] A expansão da área transversal provoca aumento de velocidade no sentido do escoamento ($\frac{\partial u}{\partial x} > 0$), resultando em aceleração convectiva positiva ($a_{\text{conv}} > 0$).
- [ ] Em escoamentos unidimensionais com trajetória retilínea, o termo convectivo é sempre nulo, de forma que variações de velocidade só podem ocorrer se houver aceleração local ($\frac{\partial u}{\partial t} \neq 0$).
- [ ] A velocidade axial é constante em qualquer seção do duto divergente, pois a hipótese de fluido incompressível impede variações espaciais do campo de velocidades.

---

### Questão 2 — Equação da Continuidade Tridimensional e Densidade Absoluta

A Equação da Continuidade para um escoamento tridimensional incompressível de água líquida é expressa por:

$$\nabla \cdot \mathbf{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$

Assinale a alternativa que explica de forma **correta** por que a **densidade absoluta** (massa específica $\rho$) não figura nessa equação:

- [ ] Porque a conservação da massa deixa de ser aplicada a fluidos incompressíveis, sendo substituída pela conservação da energia mecânica.
- [ ] Porque a massa específica da água é numericamente pequena e foi desprezada em relação aos gradientes de velocidade.
- [ ] Porque, sendo o fluido incompressível, a massa específica $\rho$ é constante no espaço e no tempo, o que anula sua derivada temporal ($\frac{\partial \rho}{\partial t} = 0$) e permite que $\rho$ seja fatorada para fora das derivadas espaciais ($\rho \nabla \cdot \mathbf{V} = 0$); dividindo ambos os membros por $\rho \neq 0$, a densidade é cancelada algebricamente.
- [ ] Porque a densidade absoluta foi convertida em peso específico ($\gamma = \rho g$), grandeza que passa a atuar unicamente na Equação da Quantidade de Movimento.
- [ ] Porque a eliminação da densidade só é matematicamente válida para escoamentos unidimensionais, mantendo-se $\rho$ obrigatoriamente presente no caso tridimensional genérico.

---

### Questão 3 — Professor não informou

> [!NOTE]
> **Posição Oficial: **Profesor não quis passar informações dessa questão.

---

### Questão 4 — Segunda Lei de Newton em Volume Infinitesimal e Força de Pressão

Considere a aplicação da Segunda Lei de Newton a um elemento diferencial de fluido de dimensões $dx, dy, dz$ e volume $dVol = dx\,dy\,dz$. As forças normais compressivas de pressão atuantes nas faces opostas na direção $x$ são:
- Face de entrada (em $x$): $F_{\text{in}} = + p\,dy\,dz$ (atuando no sentido $+x$);
- Face de saída (em $x + dx$): $F_{\text{out}} = - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$ (atuando no sentido $-x$).

A respeito da força de pressão resultante diferencial e da força por unidade de volume, assinale a alternativa **correta**:

- [ ] A força resultante diferencial é $dF_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$ e a força por unidade de volume é $f_{p,x} = -\frac{\partial p}{\partial x}$. O sinal negativo decorre diretamente do balanço algébrico das forças compressivas opostas nas faces, já que a força na face de saída atua no sentido negativo ($-x$) e introduz o termo $-\frac{\partial p}{\partial x}$ na soma diferencial.
- [ ] A força resultante diferencial é $dF_{p,x} = +\frac{\partial p}{\partial x}dx\,dy\,dz$ e a força por unidade de volume é $f_{p,x} = +\frac{\partial p}{\partial x}$, com sinal positivo.
- [ ] A força resultante diferencial é $dF_{p,x} = -\frac{\partial p}{\partial x}$ e a força por unidade de volume é $f_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$, com dimensões trocadas entre força líquida e força volumétrica.
- [ ] A força diferencial de pressão nas faces opostas anula-se identicamente pelo Princípio de Pascal, atuando apenas forças de atrito viscoso.
- [ ] O termo $-\frac{\partial p}{\partial x}$ só é não nulo para fluidos compressíveis, anulando-se em fluidos incompressíveis como a água líquida.

---

### Questão 5 — Condições de Contorno Cinemáticas em Fronteiras Sólidas Impermeáveis

Nas soluções das equações diferenciais de escoamento ao longo de fronteiras sólidas rígidas e impermeáveis, aplicam-se condições de contorno cinemáticas no campo de velocidades.

A respeito dessas condições, assinale a alternativa **correta**:

- [ ] A condição de não-escorregamento anula a velocidade normal relativa ($v_{n,\text{rel}} = 0$) e a impenetrabilidade anula a velocidade tangencial relativa ($u_{\text{rel}} = 0$).
- [ ] Em fluidos ideais invíscidos, a condição de não-escorregamento é plenamente satisfeita na fronteira sólida, originando tensões de cisalhamento viscoso.
- [ ] A **condição de impenetrabilidade** estabelece que a componente de velocidade normal relativa através da parede sólida é nula ($\mathbf{V}_{\text{rel}} \cdot \mathbf{n} = 0$), impedindo o escoamento através da fronteira sólida; e a **condição de aderência (não-escorregamento)** estabelece que a componente de velocidade tangencial relativa na parede é nula ($\mathbf{V}_{\text{rel}} \times \mathbf{n} = \mathbf{0}$), de modo que o fluido viscoso adquire a velocidade tangencial da superfície sólida.
- [ ] As condições de aderência e de impenetrabilidade são condições dinâmicas de tensões, não impondo restrições cinemáticas diretas às velocidades na parede.
- [ ] A condição de aderência decorre da gravidade e aplica-se indistintamente a fluidos viscosos, gases ideais e fluidos invíscidos.

---

## Bloco 2 — Questão de Completar Lacunas

---

### Questão 6 — Conceitos Estruturantes de Hidrodinâmica I

Preencha as lacunas das frases curtas e diretas abaixo utilizando a terminologia técnica das fontes oficiais da disciplina:

1. No estudo de análise dimensional da hidrodinâmica naval no sistema $MLT$, destacam-se propriedades físicas dos fluidos como a massa específica ($\rho$, $[ML^{-3}]$), a viscosidade dinâmica ($\mu$, $[ML^{-1}T^{-1}]$), a pressão ($p$, $[ML^{-1}T^{-2}]$) e a ________________________________________ ($\sigma$, $[MT^{-2}]$).
2. O princípio da conservação da massa aplicado a um volume de controle diferencial fixo no espaço dá origem à Equação da ________________________________________.
3. Na descrição cinemática ________________________________________, o escoamento é observado fixando-se coordenadas espaciais estáticas $(x, y, z)$ no espaço ao longo do tempo.
4. Na descrição cinemática ________________________________________, o escoamento é analisado acompanhando-se o movimento de partículas fluidas individuais ao longo de suas trajetórias.
5. De acordo com a derivada material, a aceleração de uma partícula fluida decompõe-se na aceleração ________________________________________ (variação temporal no ponto fixo) e na aceleração ________________________________________ (variação espacial no campo).
6. As forças que atuam sobre um elemento diferencial de fluido dividem-se em forças de ________________________________________ (como pressão e tensões cisalhantes viscosas nas fronteiras) e forças de ________________________________________ (como o peso gravitacional agindo sobre a massa à distância).
7. O escoamento laminar permanente de um fluido viscoso entre duas placas planas paralelas conduzido por ________________________________________ denomina-se escoamento plano de ________________________________________.
8. O número de ________________________________________ representa a razão adimensional entre as forças de inércia e as forças ________________________________________.
9. Os ensaios em tanques de provas consistem na medição de forças em um ________________________________________ (em escala reduzida) para extrapolação ao ________________________________________ (navio real em escala plena).
10. A semelhança completa entre o modelo em tanque e o navio real exige o cumprimento simultâneo das similaridades geométrica, ________________________________________ e ________________________________________.
11. Na similaridade cinemática, as trajetórias das partículas são geometricamente semelhantes e a razão entre as velocidades de pontos homólogos é rigorosamente ________________________________________ ($\frac{V_m}{V_p} = \text{constante}$).
12. Na teoria de similaridade naval, as posições espacialmente correspondentes na proporção geométrica de escala $\alpha = L_m / L_p$ entre o modelo e o protótipo denominam-se formalmente ________________________________________.

---

> [!NOTE]
> **Nota sobre os itens 7 e 8:** O preenchimento dos itens 7 e 8 depende de condições de contorno e grandezas de comparação não especificadas no direcionamento original do professor. Suas possibilidades documentadas encontram-se analisadas no gabarito comentado.

---

## Bloco 3 — Questão de Verdadeiro ou Falso

---

### Questão 7 — Princípio da Homogeneidade Dimensional e Teorema $\Pi$ de Buckingham

Julgue as afirmações a seguir em **Verdadeiro (V)** ou **Falso (F)**, com base na Apostila Teórica da Unidade 2 (`2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, pp. 2 e 6–7) e no `Questionário P1.pdf` (Q29 a Q33):

- [ ] **Item 7.1:** Pelo Princípio da Homogeneidade Dimensional, todos os termos aditivos de uma equação que descreve um fenômeno físico devem possuir rigorosamente as mesmas dimensões primárias fundamentais (como massa, comprimento e tempo nos sistemas $MLT$, ou força, comprimento e tempo no sistema $FLT$).
- [ ] **Item 7.2:** O procedimento formal de adimensionalização de uma equação física consiste em dividir cada termo por uma combinação de variáveis que detenha as mesmas dimensões desses termos, convertendo coeficientes e variáveis em grandezas adimensionais.
- [ ] **Item 7.3:** De acordo com o Teorema $\Pi$ de Buckingham, se um fenômeno físico é governado por $n$ variáveis dimensionais e $m$ dimensões primárias, o número exato de agrupamentos adimensionais independentes ($\Pi$) é dado pela soma algébrica $k = n + m$.
- [ ] **Item 7.4:** Na Etapa 1 do procedimento de Buckingham, devem-se listar as variáveis dimensionais do problema e contá-las ($n$), assegurando-se de que sejam independentes.
- [ ] **Item 7.5:** Na Etapa 2 do procedimento de Buckingham, identificam-se e listam-se as dimensões primárias fundamentais ($m$) presentes no conjunto de variáveis; na hidrodinâmica naval, empregam-se tipicamente as três dimensões primárias massa ($M$), comprimento ($L$) e tempo ($T$).
- [ ] **Item 7.6:** Na Etapa 4 do procedimento de Buckingham, a seleção das variáveis repetidas deve atender a três requisitos obrigatórios: serem em número igual a $m$; conterem, juntas, todas as dimensões primárias do problema; e não formarem um grupo adimensional entre si.
- [ ] **Item 7.7:** É permitido selecionar três variáveis repetidas puramente geométricas (como comprimento, largura e raio), pois a exigência de conter todas as dimensões fundamentais só é verificada após a determinação dos expoentes.
- [ ] **Item 7.8:** Na Etapa 6 do procedimento de Buckingham, os expoentes algébricos das variáveis repetidas em cada grupo $\Pi$ são obtidos aplicando-se a condição de homogeneidade dimensional, assumindo-se expoentes nulos ($M^0 L^0 T^0$) para as dimensões fundamentais do grupo adimensional.

---

## Bloco 4 — Cálculo Fixo

---

## Questão 8 — CÁLCULO FIXO — SEIS PASSOS

> [!IMPORTANT]
> **VAGA RESERVADA PARA O CÁLCULO CANÔNICO EM SEIS PASSOS:**  
> Conforme a diretriz estrutural permanente e mandatória da avaliação de Hidrodinâmica I (P1), esta vaga é rigorosamente destinada ao exercício discursivo e dedutivo de análise dimensional guiado pelos seis passos canônicos de Buckingham–$\Pi$.  
> O problema encontra-se consolidado no repositório oficial da disciplina e permanece preservado sem qualquer alteração.
