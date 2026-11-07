---
title: "Mecânica dos Fluidos — Capítulo 8"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-031-034.pdf"
pages: "031–034"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - forcas-friccionais
  - equacao-de-couette
  - escoamento-laminar
---

# Mecânica dos Fluidos — Capítulo 8
## Escoamento plenamente desenvolvido dominado pelas forças friccionais

> [!warning] Conteúdo sobreposto descartado (Página 031)
> A metade superior da folha inicial deste documento contém a conclusão do cálculo do capítulo anterior (perfil parabólico conduzido pela gravidade). O trecho a seguir encontra-se firmemente riscado de vermelho na fonte original e não pertence à matéria desta etapa:
> 
> Então $C_2 = 0$
> Com
> $u_{y=a} \rightarrow \frac{1}{\mu} \frac{\partial(p+\rho g h)}{\partial x} \frac{a^2}{2} + C_1 a + 0 = 0$
> Então $C_1 = -\frac{1}{\mu} \frac{\partial(p+\rho g h)}{\partial x} \frac{a}{2}$
> Colocando $C_1$ e $C_2$ na equação original
> $u = \frac{1}{2\mu} \frac{\partial(p+\rho g h)}{\partial x} y^2 - \frac{1}{\mu} \frac{\partial(p+\rho g h)}{\partial x} \frac{ay}{2}$
> $u = \frac{1}{2\mu} \frac{\partial(p+\rho g h)}{\partial x} (y^2 - ay)$
> O perfil de velocidades então é parabólico, como apresentado na figura abaixo. Quanto maior for a inclinação do canal ($\theta$) maior a velocidade máxima e quanto menor a viscosidade maior a velocidades máxima.
>
> *(O conteúdo válido do Capítulo 8 inicia-se rigorosamente a partir do título abaixo).*

Iniciando com o escoamento entre duas paredes conduzidos pelas forças friccionais, executando o passo a passo recomendado no procedimento geral

## 1. Passo 1 — Configuração do Problema

1 – Existem duas paredes, uma estacionária em baixo e outra se movendo em cima com a velocidade $V_0$, existe um escoamento entre elas, a pressão na entrada, $p_1$ e a na saída $p_2$, são iguais $p_1 = p_2$; o sistema de coordenadas adotado é cartesiano orientados em relação ao escoamento como indicado na figura abaixo, a distância entre as paredes é $a$, sendo $y = 0$, na parede de baixo e $y = a$ na parede de cima.

> [!tip] Interpretação da Geometria Visual
> A lousa ilustra a configuração de "Couette". A calota superior ("MOVING PLATE") é tracionada para a direita com velocidade $V_0$. O fluido que está em contato com ela é arrastado pelas forças friccionais, criando um perfil de fluxo sobre a placa inferior estacionária ("WALL").

---

## 2. Passo 2 — Hipóteses Básicas

2 - Por hipótese o escoamento é incompressível, que pode ser um líquido um gás se movendo lentamente, então $\rho = const.$

Por hipótese o escoamento é permanente, ou seja, independente do tempo, $\frac{\partial (.)}{\partial t} = 0$

O escoamento é totalmente desenvolvido, ou seja, $\frac{\partial (u_i)}{\partial x} = 0$

O escoamento é bidimensional, 2D, ou seja, $\frac{\partial (.)}{\partial z} = 0$, $w = 0$

As hipóteses do escoamento ser permanente, totalmente desenvolvido e 2D, são características de um escoamento laminar

As forças de corpo podem ser negligenciadas

> [!important] Atenção ao regresso das forças nulas
> Ao contrário do Capítulo 7 (onde existiam forças de gravidade), aqui o professor reafirma que as forças de corpo são negligenciadas. O motor do movimento é puramente o deslizamento da tampa mecânica.

---

## 3. Passo 3 — Identificação das Condições de Contorno

3 - O próximo passo é identificar as condições de contorno,

A primeira condição é a de não escorregamento, ou seja, a velocidade do escoamento junto a parede tem de possuir a velocidade da parede, ou seja, $u_{y=0} = 0$ e , $u_{y=a} = V_0$ e $w_{y=0} = 0$ e , $w_{y=a} = 0$

A segunda condição de contorno é a de impenetrabilidade, ou seja, não podem existir velocidades perpendiculares ou normais às paredes, ou seja, $v_{y=0} = 0$ e , $v_{y=a} = 0$

---

## 4. Passo 4a — Lei de Conservação de Massa

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

$\frac{\partial u}{\partial t} = 0$, o escoamento é permanente<br>
$u \frac{\partial u}{\partial x} = 0$ e $\frac{\partial^2 u}{\partial x^2} = 0$, o escoamento é totalmente desenvolvido<br>
$w \frac{\partial u}{\partial z} = 0$ e $\frac{\partial^2 u}{\partial z^2} = 0$, o escoamento é 2D<br>
$\rho g_x = 0$, as forças de corpo podem ser negligenciadas<br>
Da análise da conservação de massa tem-se que $v = 0$, então $v \frac{\partial u}{\partial y} = 0$

A equação de Navier-Stokes, fica reduzida a

$$ 0 = \mu \left( \frac{\partial^2 u}{\partial y^2} \right) $$

> [!tip] Interpretação Didática: O Sumiço da Pressão
> A fonte não listou expressamente a anulação do termo $\frac{\partial p}{\partial x}$ no rol acima. Todavia, isso é justificado de antemão no Passo 1, onde foi firmado que $p_1 = p_2$, configurando ausência de gradiente de pressão forçante.

---

## 7. Passo 5b — Integrações Sucessivas

5b - Integrando com relação a $y$

$$ \frac{\partial u}{\partial y} = C_1 $$

Integrando novamente em relação a $y$ para obter $u(y)$

$$ u = C_1 y + C_2 $$

---

## 8. Passo 6b — Condições de Contorno e Equação de Couette

6-b Existem 2 constantes a serem determinadas portanto são necessárias duas condições de contorno

$u_{y=0} = 0$ e , $u_{y=a} = V_0$

Empregando 

$$ u_{y=0} \rightarrow C_1 0 + C_2 = 0 $$

Então $C_2 = 0$ 

Com

$$ u_{y=a} \rightarrow C_1 a + 0 = V_0 $$

Então $C_1 = \frac{V_0}{a}$

$$ u = \frac{V_0}{a} y \quad 0 \leq y \leq a $$

Ou, seja, o perfil do escoamento é linear. Esta equação é conhecida como equação de Couette

> [!tip] Representação Visual
> A fonte inclui o desenho do novo diagrama de vetores do fluido. Em detrimento da forma parabólica habitual, a equação afim (grau 1) tece um triângulo isósceles escalando rigidamente rumo ao teto em linha reta.

---

## 9. Apêndice Complementar: Developing Flow

A aula extra "A Brief Side Comment: Developing Flow" esclarece o conceito fenomenológico central de toda a teoria: por qual motivo se assume $\frac{\partial u}{\partial x} = 0$. O slide importado atesta:

- The velocity profile is initially uniform at the inlet. (O perfil de velocidade é inicialmente uniforme na entrada).
- Boundary layers grow on both walls due to viscous drag. (Camadas limite crescem em ambas as paredes devido ao arrasto viscoso).
- Boundary layers merge on the centre line. (As camadas limite se fundem na linha central).
- Velocity profile stops changing in x-direction, $\frac{\partial u}{\partial x} = 0$. (O perfil de velocidade para de mudar na direção x).
- Current exact solution is for flow that is fully developed, $\frac{\partial u}{\partial x} = 0$. (A solução exata atual aplica-se a um escoamento que está plenamente desenvolvido).

> [!tip] Interpretação Visual da Entrada do Tubo
> O gráfico em anexo exibe o "Irrotational (core) flow region" (núcleo fluídico livre) colidindo progressivamente com a "Velocity boundary layer" (camada de atrito gerada na borda) ao longo da "Hydrodynamic entrance region". Apenas quando essas franjas colidem no centro as águas estabilizam e engatam a eterna repetição de seu formato, penetrando finalmente na "Hydrodynamically fully developed region".

---

## Resumo Ultra-Rápido
- **Força Motriz Pura:** Sem a intervenção de bombas de pressão ($p_1 = p_2$) e sem ajuda gravitacional ($\rho g_x = 0$), a massa fluida é rebocada unicamente por forças de cisalhamento.
- **A Tampa Móvel:** O diferencial imposto jaz puramente nas bordas. $u_{y=0} = 0$, mas $u_{y=a} = V_0$.
- **Navier-Stokes Vazia:** Despida de pressão e acelerações, a brutal matriz tridimensional decai numa pífia $\frac{\partial^2 u}{\partial y^2} = 0$. 
- **Equação de Couette:** O desfecho da integração produz a elementar equação afim: $u = \frac{V_0}{a} y$. Um perfil de escoamento irretocavelmente linear.
- **Developing Flow:** É a região turbulenta incipiente onde as camadas-limite crescem das extremidades para o núcleo. Apenas findo o embate das bordas, o fluxo cimenta $\frac{\partial u}{\partial x} = 0$ (tornando-se totalmente desenvolvido).

## Pontos que preciso saber
- Ter afiada a distinção: em escoamentos de Couette (força puramente friccional), o campo vetor assenta-se numa reta de geometria triangular, ao invés da barriga parabólica do escoamento de Poiseuille.
- A "equação de Couette" exige o cancelamento absoluto das forças de corpo e a estagnação gradiente transversal de pressão.
- Dominar conceitualmente que o "fully developed" $\frac{\partial u}{\partial x} = 0$ só passa a vigorar legitimamente muito depois do fluido invadir a boca da tubulação ("entrance region").

## Possíveis assuntos de prova
1. **Pergunta:** Explique através do decaimento da Equação de Navier-Stokes como o arranjo de duas placas com arrasto friccional simples desemboca num escoamento linear?
   **Resposta Baseada na Fonte:** Partindo de $\rho (\dots) = - \frac{\partial p}{\partial x} + \mu (\frac{\partial^2 u}{\partial y^2}) + \rho g_x$, eliminamos a parcela inercial (fluido totalmente desenvolvido e permanente), suprimimos o peso $\rho g_x = 0$, e excluímos o gradiente pressórico pois o enunciado postula que $p_1 = p_2$. Assim, Navier-Stokes afunila brutalmente para $0 = \mu (\frac{\partial^2 u}{\partial y^2})$. A primeira integração expele uma constante $\partial u/\partial y = C_1$ e a segunda integra-se a uma função de grau um universal ($u = C_1 y + C_2$). Como o grau máximo residual de $y$ é $1$, atesta-se sem cerimônia matemática a inclinação geométrica do campo de velocidade (linear, não parabólica).
2. O professor também poderá cobrar discursivamente a evolução do perfil cinemático desde a injeção plana na entrada ("inlet uniform") até o fundir das camadas ("merge on the centre line") consolidando a estabilidade direcional analítica ($\frac{\partial u}{\partial x} = 0$).

## Pontos Confusos ou Incompletos
- Ao listar os cortes analíticos em N-S na página 033, o professor não declarou ativamente o cancelamento do termo de pressão. O fato precisou ser importado semanticamente da Pág 031 ("as pressões são iguais $p_1 = p_2$").
- A inserção didática da página final transita de forma crua de português p/ inglês, sendo colada uma imagem de livro ou slide externo para amparar a teoria do desenvolvimento longitudinal, de tal modo que optamos por blindar essa lâmina externa dentro de um anexo isolado ("Side Comment").

---

## Flashcards para Anki

### Essenciais

| Frente | Verso |
|---|---|
| No escoamento puramente friccional conduzido por placa (Couette), o que ocorre com o gradiente de pressão e com a força da gravidade? | Ambos são anulados. As pressões na entrada e na saída são iguais ($p_1 = p_2$) e as forças de corpo são negligenciadas ($\rho g_x = 0$). |
| Qual é a condição de contorno de não escorregamento aplicada à parede superior no modelo de escoamento de Couette descrito na aula? | A velocidade tangencial do fluido possui o mesmo deslocamento mecânico da placa deslizante, fixando-se como $u_{y=a} = V_0$. |
| Como a Equação de Navier-Stokes reage à modelagem do fluxo de Couette após aplicadas todas as hipóteses de cancelamento (permanente, 2D, totalmente desenvolvido, gravidade zero e isobárico)? | Reduz-se drasticamente à simples equação diferencial ordinária de grau dois atrelada apenas à viscosidade: $0 = \mu \left( \frac{\partial^2 u}{\partial y^2} \right)$. |

### Importantes

| Frente | Verso |
|---|---|
| Geometricamente, qual é o formato do perfil de velocidades gerado pela dedução da "equação de Couette" ($u = \frac{V_0}{a}y$)? | O perfil do escoamento é perfeitamente linear, formatando um triângulo de vetores ao invés do perfil parabólico de Poiseuille. |
| Segundo o slide "Developing Flow", o que acarreta a formação e o encontro das camadas limite (Boundary layers) no centro do tubo? | Elas crescem em ambas as paredes devido ao arrasto viscoso ("viscous drag") até se fundirem na linha central ("centre line"), decretando o fim das oscilações em $x$. |
| Qual exigência geométrica cessa o comportamento caótico da "Entrance region" e legitima matematicamente a premissa de um Escoamento Totalmente Desenvolvido? | A anulação total da derivada direcional do escoamento longitudinal ao longo do trajeto axial, modelada algebricamente como $\frac{\partial u}{\partial x} = 0$. |

### Práticos

| Frente | Verso |
|---|---|
| Na modelagem de Couette, por que a constante de base $C_2$ desaba para zero na integração $u = C_1 y + C_2$? | Pois aplica-se o contorno imposto de adesão estática na parede inferior ("WALL"), que exige que em $y=0$, a velocidade seja $u=0$. Resultando matematicamente em $C_2 = 0$. |

---

## CSV para Anki

No escoamento puramente friccional conduzido por placa (Couette), o que ocorre com o gradiente de pressão e com a força da gravidade?;Ambos são anulados. As pressões na entrada e na saída são iguais ($p_1 = p_2$) e as forças de corpo são negligenciadas ($\rho g_x = 0$).
Qual é a condição de contorno de não escorregamento aplicada à parede superior no modelo de escoamento de Couette descrito na aula?;A velocidade tangencial do fluido possui o mesmo deslocamento mecânico da placa deslizante, fixando-se como $u_{y=a} = V_0$.
Como a Equação de Navier-Stokes reage à modelagem do fluxo de Couette após aplicadas todas as hipóteses de cancelamento (permanente, 2D, totalmente desenvolvido, gravidade zero e isobárico)?;Reduz-se drasticamente à simples equação diferencial ordinária de grau dois atrelada apenas à viscosidade: $0 = \mu \left( \frac{\partial^2 u}{\partial y^2} \right)$.
Geometricamente, qual é o formato do perfil de velocidades gerado pela dedução da "equação de Couette" ($u = \frac{V_0}{a}y$)?;O perfil do escoamento é perfeitamente linear, formatando um triângulo de vetores ao invés do perfil parabólico de Poiseuille.
Segundo o slide "Developing Flow", o que acarreta a formação e o encontro das camadas limite (Boundary layers) no centro do tubo?;Elas crescem em ambas as paredes devido ao arrasto viscoso ("viscous drag") até se fundirem na linha central ("centre line"), decretando o fim das oscilações em $x$.
Qual exigência geométrica cessa o comportamento caótico da "Entrance region" e legitima matematicamente a premissa de um Escoamento Totalmente Desenvolvido?;A anulação total da derivada direcional do escoamento longitudinal ao longo do trajeto axial, modelada algebricamente como $\frac{\partial u}{\partial x} = 0$.
Na modelagem de Couette, por que a constante de base $C_2$ desaba para zero na integração $u = C_1 y + C_2$?;Pois aplica-se o contorno imposto de adesão estática na parede inferior ("WALL"), que exige que em $y=0$, a velocidade seja $u=0$. Resultando matematicamente em $C_2 = 0$.
