---
title: "Mecânica dos Fluidos — Capítulo 7"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-027-031.pdf"
pages: "027–031"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - forca-de-corpo
  - gravidade
  - deducao-analitica
---

# Mecânica dos Fluidos — Capítulo 7
## Escoamento plenamente desenvolvido dominado pela força de corpo

> [!warning] Conteúdo sobreposto descartado (Página 027)
> A primeira metade da folha inicial deste documento contém a conclusão da equação de Poiseuille pertencente ao capítulo anterior. O trecho a seguir encontra-se firmemente riscado de vermelho na fonte original:
> 
> 6-b Existem 2 constantes a serem determinadas portanto são necessárias duas condições de contorno
> $u_{y=0} = 0 \text{ e, } u_{y=a} = 0$
> Empregando 
> $u_{y=0} \rightarrow \frac{1}{2\mu} \frac{\partial p}{\partial x} 0^2 + C_1 0 + C_2 = 0$
> Então $C_2 = 0$ 
> Com
> $u_{y=a} \rightarrow \frac{1}{2\mu} \frac{\partial p}{\partial x} a^2 + C_1 a + 0 = 0$
> Então $C_1 = - \frac{1}{\mu} \frac{\partial p}{\partial x} \frac{a}{2}$
> Colocando $C_1$ e $C_2$ na equação original
> $u = \frac{1}{2\mu} \frac{\partial p}{\partial x} y^2 - \frac{1}{\mu} \frac{\partial p}{\partial x} \frac{a y}{2}$
> $u = \frac{1}{2\mu} \frac{\partial p}{\partial x} (y^2 - ay)$
> O perfil de velocidades então é parabólico e quanto maior a diferença de pressão maior a velocidade máxima e quanto menor a viscosidade maior a velocidades máxima. A equação acima é conhecida como equação de Poiseuille.
>
> *(O conteúdo válido do Capítulo 7 inicia-se rigorosamente a partir do título abaixo).*

O escoamento entre duas paredes conduzidos pelas forças de gravidade, executando o passo a passo recomendado no procedimento geral é dado pela sequência

## 1. Passo 1 — Configuração Geométrica e de Eixos

1 – Existem duas paredes estacionárias paralelas, existe um escoamento entre elas, a componente ortogonal da força de gravidade possui um ângulo ($\theta$) com a linha de centro do canal; o sistema de coordenadas adotado é cartesiano orientados em relação ao escoamento como indicado na figura abaixo, a distância entre as paredes é $a$, sendo $y = 0$, na parede de baixo e $y = a$ na parede de cima, tem-se uma nova direção, $h$, alinhada com a direção da força de gravidade

> [!tip] Interpretação da Geometria Visual
> A lousa ilustra um canal inclinado. Existem dois referenciais distintos operando simultaneamente:
> 1. Os eixos $x, y$ estão alinhados com o fluxo (inclinados, descendo paralelamente à parede).
> 2. A direção $h$ está alinhada exclusivamente com a gravidade (uma seta vermelha $g$ apontando verticalmente para baixo, independente da inclinação do canal).

---

## 2. Passo 2 — Hipóteses Básicas

2 - Por hipótese o escoamento é incompressível, que pode ser um líquido um gás se movendo lentamente, então $\rho = const.$

Por hipótese o escoamento é permanente, ou seja independente do tempo, $\frac{\partial (.)}{\partial t} = 0$

O escoamento é totalmente desenvolvido, ou seja, $\frac{\partial (u_i)}{\partial x} = 0$

O escoamento é bidimensional, 2D, ou seja, $\frac{\partial (.)}{\partial z} = 0$, $w = 0$

As hipóteses do escoamento ser permanente, totalmente desenvolvido e 2D, são características de um escoamento laminar

> [!important] Atenção à força gravitacional
> Diferente dos casos anteriores, o professor destaca explicitamente nesta etapa que:
> **Existem forças de corpo**

---

## 3. Passo 3 — Condições de Contorno

3 - O próximo passo é identificar as condições de contorno,

A primeira condição é a de não escorregamento, ou seja, a velocidade do escoamento junto a parede tem de possuir a velocidade da parede, ou seja, $u_{y=0} = 0$ e , $u_{y=a} = 0$ e $w_{y=0} = 0$ e , $w_{y=a} = 0$

A segunda condição de contorno é a de impenetrabilidade, ou seja, não podem existir velocidades perpendiculares ou normais às paredes, ou seja, $v_{y=0} = 0$ e , $v_{y=a} = 0$

---

## 4. Passo 4a — Lei de Conservação de Massa

4 - O objetivo é obter o campo de velocidades no espaço dadas pelas variáveis $u$, $v$ e $w$ a partir de funções conhecidas, 

4a - começando pela Lei de Conservação de massa

$$ \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0 $$

Tem-se $\frac{\partial u}{\partial x} = 0$ (o escoamento é totalmente desenvolvido) e $\frac{\partial w}{\partial z} = 0$ (o escoamento é 2D), então

$$ \frac{\partial v}{\partial y} = 0 $$

---

## 5. Passos 5a e 6a — Integração da Massa e Contorno

5a - Integrando o resultado acima

$$ \int \frac{\partial v}{\partial y} dy \rightarrow v = const = C_1 $$

6a - Aplicando a condição de contorno de impenetrabilidade, na parede, $v_{y=0,a} = 0$, tem-se $C_1 = 0$, ou seja, em qualquer posição $v = 0$

---

## 6. Passo 4b — Conservação da Quantidade de Movimento (Navier-Stokes)

4b - Fazendo o passo a passo para a próxima equação a ser analisada a Lei da conservação da quantidade de movimento, na direção $x$

$$ \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x $$

$\frac{\partial u}{\partial t} = 0$, o escoamento é permanente

$u \frac{\partial u}{\partial x} = 0$ e $\frac{\partial^2 u}{\partial x^2} = 0$, o escoamento é totalmente desenvolvido

$w \frac{\partial u}{\partial z} = 0$ e $\frac{\partial^2 u}{\partial z^2} = 0$, o escoamento é 2D

$\rho g_x \neq 0$, as forças de corpo não podem ser negligenciadas

> [!tip] Explicação do professor (Gravidade Projetada e Avaliação)
> O professor ressaltou que a força propulsora real aqui é a gravidade projetada ($g_x = g \sin \theta$). Porém, ele declarou na aula que não vai cobrar o desenvolvimento dessa modelagem gravitacional inclinada na prova (considerando-a algebricamente mais difícil que as demais).
> **Fonte:** Transcrição `HidVoz 260814_091758_original.txt`.

Da análise da conservação de massa tem-se que $v = 0$, então $v \frac{\partial u}{\partial y} = 0$

A equação de Navier-Stokes, fica reduzida a

$$ 0 = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial y^2} \right) + \rho g_x $$

Ou

$$ \mu \left( \frac{\partial^2 u}{\partial y^2} \right) = \frac{\partial p}{\partial x} - \rho g_x $$

onde 

$$ g_x = g \sin \theta $$

> [!warning] Divergência Visual de Notação
> Na lousa da fonte original (página 030), o triângulo que decompõe a gravidade mostra o cateto oposto como $g_x = g \sin \phi$ (utilizando a letra grega *phi*). No entanto, o texto digitado imediatamente abaixo pelo autor utiliza a letra *theta*, afirmando "Mas $\sin \theta = \frac{-dh}{dx}$". O documento preserva a transcrição textual exata em $\theta$ para manter a integridade com as equações finais.

Mas $\sin \theta = \frac{-dh}{dx}$

A razão para se fazer a troca do seno pela derivada em relação a $x$ é porque já existe uma derivada parcial da pressão em relação a $x$ na equação de Navier-Stokes, fazendo com que ela possa a ser reescrita na forma

$$ \frac{\partial^2 u}{\partial y^2} = \frac{1}{\mu} \frac{\partial (p + \rho g h)}{\partial x} = const $$

---

## 7. Passo 5b — Integrações Sucessivas

5b - Integrando com relação a $y$

$$ \frac{\partial u}{\partial y} = \frac{1}{\mu} \frac{\partial (p + \rho g h)}{\partial x} y + C_1 $$

Integrando novamente em relação a $y$ para obter $u(y)$

$$ u = \frac{1}{2\mu} \frac{\partial (p + \rho g h)}{\partial x} y^2 + C_1 y + C_2 $$

---

## 8. Passo 6b — Condições de Contorno e Equação Final

6-b Existem 2 constantes a serem determinadas portanto são necessárias duas condições de contorno

$u_{y=0} = 0$ e , $u_{y=a} = 0$

Empregando 

$$ u_{y=0} \rightarrow \frac{1}{2\mu} \frac{\partial (p + \rho g h)}{\partial x} 0^2 + C_1 0 + C_2 = 0 $$

Então $C_2 = 0$

Com

$$ u_{y=a} \rightarrow \frac{1}{\mu} \frac{\partial (p + \rho g h)}{\partial x} \frac{a^2}{2} + C_1 a + 0 = 0 $$

Então $C_1 = - \frac{1}{\mu} \frac{\partial (p + \rho g h)}{\partial x} \frac{a}{2}$

Colocando $C_1$ e $C_2$ na equação original

$$ u = \frac{1}{2\mu} \frac{\partial (p + \rho g h)}{\partial x} y^2 - \frac{1}{\mu} \frac{\partial (p + \rho g h)}{\partial x} \frac{ay}{2} $$

$$ u = \frac{1}{2\mu} \frac{\partial (p + \rho g h)}{\partial x} (y^2 - ay) $$

O perfil de velocidades então é parabólico, como apresentado na figura abaixo. Quanto maior for a inclinação do canal ($\theta$) maior a velocidade máxima e quanto menor a viscosidade maior a velocidades máxima.

> [!tip] Representação Visual (Lâmina Final)
> A fonte conclui com uma modelagem 3D do "Velocity profile" de um fluido imprensado entre a placa superior e inferior de um duto em ladeira. A base do canal aponta num mergulho de ângulo $\theta$ enquanto o prumo $\vec{g}$ puxa verticalmente para baixo, acelerando o miolo parabólico das águas desprovido do arrasto aderente ($C_1, C_2$) das paredes estacionárias.

> [!warning] Conteúdo tachado no encerramento (Página 031)
> O último bloco da apostila contém a introdução para um novo cenário de escoamento. Todo o texto a seguir se encontra cruzado por duras linhas vermelhas na fonte e não compõe a matriz de forças de corpo deste capítulo:
> 
> Escoamento plenamente desenvolvido dominado pelas forças friccionais
> Iniciando com o escoamento entre duas paredes conduzidos pelas forças friccionais, executando o passo a passo recomendado no procedimento geral
> 1 – Existem duas paredes, uma estacionária em baixo e outra se movendo em cima com a velocidade $V_0$, existe um escoamento entre elas, a pressão na entrada, $p_1$ e a na saída $p_2$, são iguais $p_1 = p_2$; o sistema de coordenadas adotado é cartesiano orientados em relação ao escoamento como indicado na figura abaixo, a distância entre as paredes é $a$, sendo $y = 0$, na parede de baixo e $y = a$ na parede de cima.

---

## Resumo Ultra-Rápido
- **Força de corpo ativada:** A gravidade não é mais zero. O vetor $\rho g_x$ atua no fluido descendo um canal inclinado de ângulo $\theta$.
- **Dois referenciais lógicos:** Enquanto $x$ e $y$ acompanham a parede inclinada, um eixo autônomo $h$ vigia o prumo da gravidade.
- **O truque da Fusão:** O $\sin \theta$ é convertido em $-dh/dx$. Isso unifica a tração da ladeira junto à derivada da pressão, originando o termo único propulsor: $\frac{\partial (p + \rho g h)}{\partial x}$.
- **Resultado Parabólico:** A equação de Poiseuille renasce, pilotada não apenas pelo diferencial mecânico de bombas ($p$), mas reforçada pela queda natural gravitacional.

## Pontos que preciso saber
- Lembrar que a hipótese que difere este capítulo dos anteriores é abertamente: **"Existem forças de corpo"** ($\rho g_x \neq 0$).
- Compreender que a substituição de $\sin \theta$ por $-dh/dx$ permite aglutinar a gravidade na mesma derivada parcial da pressão em relação a $x$.
- A velocidade máxima no centro aumenta com a inclinação ($\theta$) e a pressão, sendo amortecida pela viscosidade ($\mu$).

## Possíveis assuntos de prova
1. **Pergunta:** Como a força da gravidade foi acoplada à variação da pressão no escoamento de canal inclinado?
   **Resposta Baseada na Fonte:** A componente longitudinal da força de corpo ($\rho g_x = \rho g \sin \theta$) foi manipulada substituindo-se o seno pela derivada de altura vertical em relação ao eixo $x$ ($-dh/dx$). Isso fez com que pudesse ser reescrita na mesma derivada parcial da pressão, originando o pacote motriz acoplado: $\frac{\partial(p + \rho g h)}{\partial x}$.

## Pontos Confusos ou Incompletos
- Na página 030 da fonte, há uma dessincronia visual: o esboço do triângulo de força peso ilustra o ângulo interno com a letra grega $\phi$, mas a tese descritiva e as equações utilizam $\theta$.

---

## Flashcards para Anki

### Essenciais

| Frente | Verso |
|---|---|
| Quais são as quatro hipóteses fundamentais que caracterizam o escoamento laminar descritas na dedução do canal inclinado? | 1. Incompressível ($\rho = const.$)<br>2. Permanente ($\partial(.)/\partial t = 0$)<br>3. Totalmente desenvolvido ($\partial(u_i)/\partial x = 0$)<br>4. Bidimensional ($\partial(.)/\partial z = 0, w = 0$). |
| Qual hipótese difere radicalmente o modelo de escoamento no Capítulo 7 (canal inclinado) em relação à Equação de Poiseuille simples? | A hipótese de que **existem forças de corpo** ($\rho g_x \neq 0$), significando que a gravidade atua ativamente para empurrar o fluxo. |
| O que ditam as condições de contorno de **não escorregamento** e **impenetrabilidade** nas paredes ($y=0$ e $y=a$)? | **Não escorregamento:** a velocidade tangencial do fluido é nula ($u = 0, w = 0$).<br>**Impenetrabilidade:** a velocidade normal à parede é nula ($v = 0$). |

### Importantes

| Frente | Verso |
|---|---|
| Por qual razão algébrica o professor substitui $\sin \theta$ por $-dh/dx$ na Equação de Navier-Stokes reduzida? | Para fundir a parcela de força gravitacional junto com o gradiente de pressão, já que ambos podem ser operados por uma derivada parcial em $x$, gerando o termo motriz unificado $\partial(p + \rho g h)/\partial x$. |
| Ao final das integrações sucessivas no canal inclinado, qual formato geométrico o campo de velocidades assume? | Assume um perfil parabólico. |
| De acordo com a equação deduzida, o que ocorre com a velocidade máxima do canal quando se aumenta a inclinação ($\theta$) e a viscosidade ($\mu$)? | Quanto maior for a inclinação ($\theta$), maior a velocidade máxima; quanto menor a viscosidade ($\mu$), maior a velocidade máxima. |

### Práticos

| Frente | Verso |
|---|---|
| Como a Equação da Continuidade (Massa) consegue provar que a velocidade normal $v$ é zero em qualquer posição do canal? | Sendo o escoamento bidimensional e totalmente desenvolvido, $\partial u/\partial x = 0$ e $\partial w/\partial z = 0$, reduzindo a massa a $\partial v/\partial y = 0$. Integrando, tem-se $v = C_1$. Aplicando a impenetrabilidade nas paredes ($v = 0$), infere-se que $C_1 = 0$, logo $v = 0$ em toda parte. |
| Como ficam as duas constantes de integração $C_1$ e $C_2$ da quantidade de movimento após aplicar o contorno de não escorregamento em $y=0$ e $y=a$? | Em $y=0$, a velocidade zera determinando que $C_2 = 0$. Em $y=a$, a velocidade zera determinando $C_1 = -\frac{1}{\mu}\frac{\partial(p+\rho g h)}{\partial x}\frac{a}{2}$. |

---

## CSV para Anki

Quais são as quatro hipóteses fundamentais que caracterizam o escoamento laminar descritas na dedução do canal inclinado?;1. Incompressível ($\rho = const.$)<br>2. Permanente ($\partial(.)/\partial t = 0$)<br>3. Totalmente desenvolvido ($\partial(u_i)/\partial x = 0$)<br>4. Bidimensional ($\partial(.)/\partial z = 0, w = 0$).
Qual hipótese difere radicalmente o modelo de escoamento no Capítulo 7 (canal inclinado) em relação à Equação de Poiseuille simples?;A hipótese de que **existem forças de corpo** ($\rho g_x \neq 0$), significando que a gravidade atua ativamente para empurrar o fluxo.
O que ditam as condições de contorno de **não escorregamento** e **impenetrabilidade** nas paredes ($y=0$ e $y=a$)?;**Não escorregamento:** a velocidade tangencial do fluido é nula ($u = 0, w = 0$).<br>**Impenetrabilidade:** a velocidade normal à parede é nula ($v = 0$).
Por qual razão algébrica o professor substitui $\sin \theta$ por $-dh/dx$ na Equação de Navier-Stokes reduzida?;Para fundir a parcela de força gravitacional junto com o gradiente de pressão, já que ambos podem ser operados por uma derivada parcial em $x$, gerando o termo motriz unificado $\partial(p + \rho g h)/\partial x$.
Ao final das integrações sucessivas no canal inclinado, qual formato geométrico o campo de velocidades assume?;Assume um perfil parabólico.
De acordo com a equação deduzida, o que ocorre com a velocidade máxima do canal quando se aumenta a inclinação ($\theta$) e a viscosidade ($\mu$)?;Quanto maior for a inclinação ($\theta$), maior a velocidade máxima; quanto menor a viscosidade ($\mu$), maior a velocidade máxima.
Como a Equação da Continuidade (Massa) consegue provar que a velocidade normal $v$ é zero em qualquer posição do canal?;Sendo o escoamento bidimensional e totalmente desenvolvido, $\partial u/\partial x = 0$ e $\partial w/\partial z = 0$, reduzindo a massa a $\partial v/\partial y = 0$. Integrando, tem-se $v = C_1$. Aplicando a impenetrabilidade nas paredes ($v = 0$), infere-se que $C_1 = 0$, logo $v = 0$ em toda parte.
Como ficam as duas constantes de integração $C_1$ e $C_2$ da quantidade de movimento após aplicar o contorno de não escorregamento em $y=0$ e $y=a$?;Em $y=0$, a velocidade zera determinando que $C_2 = 0$. Em $y=a$, a velocidade zera determinando $C_1 = -\frac{1}{\mu}\frac{\partial(p+\rho g h)}{\partial x}\frac{a}{2}$.
