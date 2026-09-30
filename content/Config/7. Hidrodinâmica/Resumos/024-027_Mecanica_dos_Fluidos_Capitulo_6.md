---
title: "Mecânica dos Fluidos — Capítulo 6"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-024-027.pdf"
pages: "024–027"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - equacao-de-poiseuille
  - deducao-analitica
---

# Mecânica dos Fluidos — Capítulo 6
## Escoamento plenamente desenvolvido dominado pelas forças de pressão

> [!warning] Conteúdo sobreposto descartado (Página 024)
> O topo da primeira página deste documento contém resquícios sobrepostos do capítulo anterior. O texto a seguir encontra-se firmemente riscado de vermelho na fonte original: 
> "Já para o escoamento totalmente desenvolvido conduzido pelas forças viscosas, o escoamento está entre duas paredes, mas as paredes possuem velocidades diferentes entre elas. Na figura abaixo, uma das paredes esta fixa e outra se move. A força viscosa gera a variação da quantidade de movimento entre as placas. Todos estes casos possuem solução analítica"
> O conteúdo válido e estruturado deste capítulo inicia-se rigorosamente a partir do título abaixo.

Iniciando com o escoamento entre duas paredes conduzidos pelas forças de pressão, executando o passo a passo recomendado no procedimento geral

## 1. Passo 1 — Configuração do Problema

1 – Existem duas paredes estacionárias, existe um escoamento entre elas, uma diferença de pressão na entrada, $p_1$ e a na saída $p_2$, sendo $p_1 > p_2$; o sistema de coordenadas adotado é cartesiano orientados em relação ao escoamento como indicado na figura abaixo, a distância entre as paredes é $a$, sendo $y = 0$, na parede de baixo e $y = a$ na parede de cima.

> [!tip] Representação Visual (Lousa do Professor)
> A lousa delimita o escoamento confinado por limites horizontais "WALL". O eixo cartesiano baseia-se na quilha esquerda, indicando a altura total $a$ em laranja do ponto $y=0$ ao ponto $y=a$. O gradiente que empurra o fluido é ilustrado pelas setas vermelhas mostrando $P_1 > P_2$. As correntes de velocidade azuis escoam unidirecionalmente pelo eixo $x$.

---

## 2. Passo 2 — Hipóteses Básicas

2 - Por hipótese o escoamento é incompressível, que pode ser um líquido ou um gás se movendo lentamente, então $\rho = const.$

Por hipótese o escoamento é permanente, ou seja, independente do tempo, $\frac{\partial (.)}{\partial t} = 0$

O escoamento é totalmente desenvolvido, ou seja, $\frac{\partial (u_i)}{\partial x} = 0$

O escoamento é bidimensional, 2D, ou seja, $\frac{\partial (.)}{\partial z} = 0$, $w = 0$

As hipóteses de escoamentos com características permanente, totalmente desenvolvido e 2D, são características de um escoamento laminar

A última hipótese é que não existem forças de corpo atuando no escoamento, $\rho g_x = 0$

---

## 3. Passo 3 — Identificação das Condições de Contorno

3 - O próximo passo é identificar as condições de contorno,

A primeira condição é a de não escorregamento, ou seja, a velocidade do escoamento junto a parede tem de possuir a velocidade da parede, ou seja, $u_{y=0} = 0$ e , $u_{y=a} = 0$ e $w_{y=0} = 0$ e , $w_{y=a} = 0$

A segunda condição de contorno é a de impenetrabilidade, ou seja, não podem existir velocidades perpendiculares ou normais às paredes, ou seja, $v_{y=0} = 0$ e , $v_{y=a} = 0$

---

## 4. Passo 4a — Lei de Conservação da Massa

4 - O objetivo é obter o campo de velocidades no espaço dadas pelas variáveis u, v e w a partir de funções conhecidas, 

4a - começando pela Lei de Conservação de massa

$$ \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0 $$

Tem-se $\frac{\partial u}{\partial x} = 0$ (o escoamento é totalmente desenvolvido) e $\frac{\partial w}{\partial z} = 0$ (o escoamento é 2D), então

$$ \frac{\partial v}{\partial y} = 0 $$

---

## 5. Passos 5a e 6a — Integrando e Aplicando o Contorno

5a - Integrando o resultado acima
$$ \int \frac{\partial v}{\partial y} dy \rightarrow v = const = C_1 $$

6a - Aplicando a condição de contorno de impenetrabilidade, na parede, $v_{y=0,a} = 0$, tem-se $C_1 = 0$, ou seja, em qualquer posição $v = 0$

---

## 6. Passo 4b — Conservação da Quantidade de Movimento (Direção $x$)

4b - Fazendo o passo a passo para a próxima equação a ser analisada a Lei da conservação da quantidade de movimento, na direção $x$

$$ \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x $$

$\frac{\partial u}{\partial t} = 0$, o escoamento é permanente

$u \frac{\partial u}{\partial x} = 0 , \frac{\partial^2 u}{\partial x^2} = 0$, o escoamento é totalmente desenvolvido

$w \frac{\partial u}{\partial z} = 0$ e $\frac{\partial^2 u}{\partial z^2} = 0$, o escoamento é 2D

$\rho g_x = 0$, as forças de corpo podem ser negligenciadas

Da análise da conservação de massa tem-se que $v = 0$, então $v \frac{\partial u}{\partial y} = 0$

A equação de Navier-Stokes, fica reduzida a

$$ \frac{\partial p}{\partial x} = \mu \left( \frac{\partial^2 u}{\partial y^2} \right) $$

Ou seja, a força de pressão é balanceada com a força friccional, porque não existe aceleração no escoamento. Observando a equação acima, neste caso especial a componente da velocidade na direção $x$, $u$, só depende da coordenada $y$, ou seja, $u = u(y)$

$$ \frac{\partial^2 u}{\partial y^2} = \frac{1}{\mu} \frac{\partial p}{\partial x} = const $$

A razão da expressão acima ser uma constante é que duas quantidades, uma dependendo apenas de $x$, $p(x)$ e outra dependendo apenas de $y$, $u(y)$, empregando o método de separação de variáveis, só podem ser iguais, se as quantidades foram constantes, de outra forma elas seriam independentes.

---

## 7. Passo 5b — Integrações Sucessivas

5b - Integrando com relação a $y$

$$ \frac{\partial u}{\partial y} = \frac{1}{\mu} \frac{\partial p}{\partial x} y + C_1 $$

Integrando novamente em relação a $y$ para obter $u(y)$

$$ u = \frac{1}{2\mu} \frac{\partial p}{\partial x} y^2 + C_1 y + C_2 $$

---

## 8. Passo 6b — Condições de Contorno e Equação de Poiseuille

6-b Existem 2 constantes a serem determinadas portanto são necessárias duas condições de contorno

$u_{y=0} = 0$ e , $u_{y=a} = 0$

Empregando 

$$ u_{y=0} \rightarrow \frac{1}{2\mu} \frac{\partial p}{\partial x} 0^2 + C_1 0 + C_2 = 0 $$

Então $C_2 = 0$ 

Com

$$ u_{y=a} \rightarrow \frac{1}{2\mu} \frac{\partial p}{\partial x} a^2 + C_1 a + 0 = 0 $$

Então $C_1 = - \frac{1}{\mu} \frac{\partial p}{\partial x} \frac{a}{2} $

Colocando $C_1$ e $C_2$ na equação original

$$ u = \frac{1}{2\mu} \frac{\partial p}{\partial x} y^2 - \frac{1}{\mu} \frac{\partial p}{\partial x} \frac{a y}{2} $$

$$ u = \frac{1}{2\mu} \frac{\partial p}{\partial x} (y^2 - ay) $$

O perfil de velocidades então é parabólico e quanto maior a diferença de pressão maior a velocidade máxima e quanto menor a viscosidade maior a velocidades máxima. A equação acima é conhecida como equação de Poiseuille.

> [!tip] Representação Visual (Lousa do Professor)
> A fonte apresenta o gráfico do perfil de velocidades desenhando uma parábola robusta. O arco parabólico está estendido entre o eixo horizontal inferior `$y = 0$` e o eixo superior `$y = a$`. Nas extremidades sólidas, a curva pontua `$u(y=0)=0$` (Fixed) e `$u(y=a)=0$` (Fixed), ilustrando o confinamento tangencial. O vetor principal estoura com intensidade `$u_{max}$` estritamente no meio do canal livre das paredes.

> [!warning] Conteúdo tachado no encerramento (Página 027)
> Escoamento plenamente desenvolvido dominado pela força de corpo
> O escoamento entre duas paredes conduzidos pelas forças de gravidade, executando o passo a passo recomendado no procedimento geral é dado pela sequência
> 1 – Existem duas paredes estacionárias paralelas, existe um escoamento entre elas, a componente ortogonal da força de gravidade possui um ângulo ($\theta$) com a linha de
> *(O bloco supracitado encontra-se anulado por traços vermelhos na fonte).*

---

## Resumo Ultra-Rápido
- **Ponto de Partida:** $p_1 > p_2$ empurrando um escoamento bidimensional, estacionário, plenamente desenvolvido entre chapas rígidas travadas em $y=0$ e $y=a$.
- **O Truque da Conservação de Massa:** Zera a velocidade transversal $v$ do sistema, simplificando drasticamente o caos de Navier-Stokes.
- **A Lógica de Navier-Stokes para Poiseuille:** A ausência de aceleração determina que o gradiente de pressão forcejado ($\partial p / \partial x$) empate perfeitamente com a viscosidade resistiva da água ($\mu \cdot \partial^2 u / \partial y^2$).
- **Separação de Variáveis:** Como uma fração é exclusiva de $y$ e a outra de $x$, a igualdade mútua assegura que ambas operam contra uma constante. Duas integrais desovam a parábola.
- **Fechamento Parabólico:** A velocidade nos contornos estacionários zera as constantes. O miolo livre do tubo absorve o *boost* máximo ($u_{max}$).

## Pontos que preciso saber
- Decorar que as premissas "Permanente + Totalmente desenvolvido + 2D" forjam a espinha dorsal de um escoamento **laminar** modelável analiticamente.
- Explicar por que não há componente $v$ na Equação de Momentum (a Conservação de Massa acoplada à restrição de impenetrabilidade prova isso previamente).
- Evidenciar a relação da Equação de Poiseuille com o mundo macroscópico: $+$ Pressão eleva a parábola; $+$ Viscosidade (óleo grosso) cessa a velocidade.

## Possíveis assuntos de prova
1. **Pergunta:** Por que a equação da continuidade (massa) é resolvida ANTES da equação do momentum em tubos?
   **Resposta Baseada na Fonte:** Para eliminar variáveis ociosas. A massa prova que o gradiente $\partial v / \partial y = 0$. Ao injetar o contorno (impenetrabilidade da parede que proíbe velocidade normal), conclui-se que o componente da velocidade transversal $v=0$ globalmente, poupando imenso esforço algébrico ao se enfrentar a Navier-Stokes subsequente.
2. Demonstrar o cancelamento analítico do "Cabo de Guerra" em NS: por que $\partial p / \partial x = \mu \partial^2 u / \partial y^2$? Porque, sendo a velocidade constante (plenamente desenvolvida), a "aceleração é nula", logo a pressão só gasta sua energia lutando contra a fricção viscosa.

## Pontos Confusos ou Incompletos
- Nenhum salto algorítmico obscuro foi deixado para trás nesta derivação; os 6 passos matemáticos de Poiseuille fecham com clareza a topologia teórica da apostila. A ponta solta deixada ("força de corpo/gravidade") foi literalmente tachada/cancelada pelo professor.
