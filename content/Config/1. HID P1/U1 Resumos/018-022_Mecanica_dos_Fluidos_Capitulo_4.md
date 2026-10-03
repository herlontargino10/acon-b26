---
title: "Mecânica dos Fluidos — Capítulo 4"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-018-022.pdf"
pages: "018–022"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - energia
  - hipoteses
---

# Mecânica dos Fluidos — Capítulo 4
## A lei de conservação de energia e Hipóteses fundamentais

## 1. Fechamento da Quantidade de Movimento (Conteúdo da Página 018)

> [!warning] Conteúdo sobreposto e tachado
> A primeira página deste material é uma sobreposição exata do final do material anterior, completando o sistema cartesiano das forças viscosas, seguido da seção "As forças de corpo". Toda a seção discursiva e as equações tridimensionais a partir do trecho de forças de corpo encontram-se **tachadas por linhas vermelhas na fonte**. O conteúdo está preservado abaixo por fidelidade.

A fonte apresenta o fechamento das componentes (nas direções y e z):
$$
\rho \frac{Dv}{Dt} = - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2} \right)
$$
$$
\rho \frac{Dw}{Dt} = - \frac{\partial p}{\partial z} + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2} \right)
$$

Com isto tem-se a visão geral de onde surgem as forças de pressão e viscosa que atuam em um fluido e como elas se apresentam no sistema de coordenadas cartesiano, faltando ainda incluir as forças de corpo.

**As forças de corpo**

Em hidrodinâmica do navio as forças de corpo comuns são a gravidade e o empuxo, em manobra do navio as forças de Coriolis e Centrípetas são incluídas. Outro exemplo de força de corpo são as magnéticas, elétricas. Ou seja, as forças de corpo, podem ser de diferentes fontes dependendo da situação.

A inclusão das forças gravitacionais na lei de conservação de quantidade de movimento é dada por
$$
F_x = m g = \rho \Delta x \Delta y \Delta z g_x
$$
Onde $g_x$ é a componente da aceleração gravitacional na direção x.

Fazendo a força por unidade de volume tem-se
$$
\frac{F_x}{\Delta x \Delta y \Delta z} = \rho g_x
$$

Combinando agora as forças superficiais com as forças de corpo tem-se
$$
\rho \frac{Du}{Dt} = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x
$$
Ou
$$
\rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x
$$

De forma similar nas direções y e z, serão respectivamente
$$
\rho \left( \frac{\partial y}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right) = - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2} \right) + \rho g_y
$$
> [!warning] Fiel à fonte — expressão aparentemente incomum preservada
> Observa-se que na equação acima, o termo de aceleração local em y está grafado como $\frac{\partial y}{\partial t}$ no lugar de $\frac{\partial v}{\partial t}$. O erro foi replicado fidedignamente.

$$
\rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right) = - \frac{\partial p}{\partial z} + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2} \right) + \rho g_z
$$

---

## 2. A Equação de Navier-Stokes (Fechamento vetorial)

As três equações acima correspondem a famosa Equção de Navier-Stokes, que na forma vetorial é apresentada por:
$$
\rho \frac{DV}{Dt} = -\nabla p + \mu \nabla^2 V + \rho \nabla g
$$

---

## 3. A Lei de Conservação de Energia (1ª Lei da Termodinâmica)

Pode-se dividir a energia de um sistema em duas classes distintas: a energia armazenada e a energia em transição. A primeira está relacionada diretamente com a massa do próprio sistema, e envolve as energias interna, cinética e potencial, a segunda classe se relaciona com a energia trocada entre sistemas, incluindo o calor e o trabalho. 

Considerando $E$ a energia total armazenada por um sistema que, num intervalo de tempo, recebeu uma quantidade de calor $Q$ e executou um trabalho $W$, a conservação desse sistema é traduzida através da expressão:
$$
E = Q - W
$$
A expressão acima é a "primeira lei da termodinâmica".

Então, a taxa de variação da energia por unidade de tempo é $\frac{dE}{dt} = \dot{E}$, as trocas de energia efetuadas com o exterior sob forma de calor, $\frac{dQ}{dt} = \dot{Q}$, e a de trabalho, $\frac{dW}{dt} = \dot{W}$ resultando em:
$$
\frac{dE}{dt} = \dot{Q} - \dot{W}
$$

O que significa dizer que a taxa de entrada, por unidade de tempo, de energia térmica e mecânica num sistema menos a correspondente taxa de saída deverá igualar a taxa de acumulação de energia no interior desse mesmo sistema.

---

## 4. A Energia Armazenada no Volume de Controle

Para relacionar estes conceitos acima com a noção de volume de controle, emprega-se o conceito de densidade mássica de energia armazenada pelo sistema, $e$.

A energia do sistema, $e$, por unidade de massa pode ser de vários tipos:
$$
e = e_{interna} + e_{cin\acute{e}tica} + e_{potencial} + e_{outros}
$$
Onde $e_{outros}$ pode abranger reações químicas, nucleares, eletrostáticas ou de campos magnéticos. Considerando apenas os 3 primeiros termos
$$
e = \hat{u} + \frac{1}{2}V^2 + gz
$$
> [!warning] Atenção à Nomenclatura ($\hat{u}$)
> A fonte utiliza o símbolo $\hat{u}$ (com chapéu) para denotar a **energia interna** da partícula fluida, evitando assim a confusão com a componente escalar da velocidade no eixo x (normalmente chamada apenas de u).

Então a energia do sistema armazenada no interior do volume de controle é dada por
$$
E_{sist} = \iiint e \rho \, dvol
$$

Por definição a energia de um sistema não varia, ou seja,
$$
\frac{dE}{dt} = \frac{\partial}{\partial t} \iiint e \rho \, dvol + \iint e \rho (V.n) dA
$$

Ou seja, a taxa de transferência de energia, sob forma de calor e trabalho, para um instante coincidente, em um dado instante t, em um volume de controle, é igual a soma da taxa de aumento de energia armazenada no interior do volume com a efluxo líquido da referida energia através da superfície de controle.

---

## 5. A Energia em Transição (Calor e Trabalho)

### 5.1. O Calor ($\dot{Q}$)
Os termos de calor podem ser examinados em detalhes. Se existe transferência de calor, ele será dividido em efeitos de condução, convecção e radiação, como aplicados em termodinâmica, mas para fins da hidrodinâmica do navio estes termos não são considerados importantes por serem de ordem muito pequena, sendo mencionados apenas ocasionalmente.

### 5.2. O Trabalho ($\dot{W}$)
A energia oriunda do trabalho realizado por instante de tempo, $\dot{W}$ pode ser divido em duas partes, o produzido por máquina, $\dot{W}_m$ e qualquer forma de trabalho por instante de tempo efetuado pelo sistema sobre a sua vizinhança e para ela transferido através de uma corrente de transmissão, $\dot{W}_e$, então
$$
\dot{W} = \dot{W}_m + \dot{W}_e
$$

$\dot{W}_e$ pode ser dividido em dois: a variação do trabalho destinado a vencer as forças de pressão e de tensão viscosa, a fim de assegurar o escoamento do fluido.
$$
\dot{W}_e = \dot{W}_{press\tilde{a}o} + \dot{W}_{viscosas}
$$

Para $\dot{W}_e$ importa apenas o que ocorre na superfície de controle, já que o trabalho efetuado sobre elementos de fluido no interior do volume de controle resulta da ação de forças iguais e diretamente opostas.

O trabalho da máquina, $\dot{W}_m$, isola a parte do trabalho que é deliberadamente feita por uma máquina (impulsor da bomba, pá do ventilador, pistão ou semelhante) projetando-se através da superfície de controle no volume de controle.

### 5.3. O Trabalho de Pressão ($\dot{W}_{press\tilde{a}o}$)
A taxa de variação de trabalho feito pelas forças de pressão $\dot{W}_{press\tilde{a}o}$ ocorre apenas na superfície; todo o trabalho nas porções internas do material no volume de controle é igual e oposta forças e é auto cancelada. O trabalho de pressão é igual à força de pressão sobre um pequeno elemento de superfície $dA$ vezes a componente de velocidade normal no volume de controle:

### Forma apresentada na fonte
$$
d\dot{W}_{press\tilde{a}o} = -(p - V.n)dA
$$
### Observação (Inconsistência da fonte preservada)
A apostila apresenta a equação acima textualmente com um traço de subtração $-(p - V.n)$, o que é dimensionalmente anômalo. Isso se trata de um provável **erro tipográfico** onde o traço deveria ser removido ou ser um ponto de multiplicação para refletir o produto $-p(V.n)dA$. A equação foi integralmente preservada para manter a fidelidade documental.

O trabalho total da pressão é a integral ao longo de toda a superfície de controle
$$
\dot{W}_{press\tilde{a}o} = \iint p(V.n)dA
$$

### 5.4. O Trabalho Viscoso ($\dot{W}_{viscosas}$)
O trabalho de cisalhamento devido a tensões viscosas, $\dot{W}_{viscosas}$, ocorre na superfície de controle e consiste no produto de cada tensão viscosa (uma normal e duas tangenciais) e a um respectivo componente de velocidade:
$$
d\dot{W}_{viscosas} = -\tau.V dA
$$
$$
\dot{W}_{viscosas} = -\iint \tau.V dA
$$
onde $\tau$ é o vetor de tensão na superfície elementar dA.

---

## 6. A Equação Completa da Conservação de Energia

Substituindo todos os termos na equação original, chega-se a:

$$
\dot{Q} - \dot{W}_m - \iint p(V.n)dA - \iint \tau.V dA = \frac{\partial}{\partial t} \iiint_{Vol} \left(\hat{u} + \frac{1}{2}V^2 + gz\right) \rho \, dvol + \iint_{Sc} \left(\hat{u} + \frac{1}{2}V^2 + gz\right) \rho (V.n) dA
$$

---

## 7. Hipóteses comum na mecânica dos fluidos

**1 - Incompressibilidade**

**2 – Escoamento 2D ( uma dimensão não é considerada, geralmente z)** que leva a hipótese de apenas duas componentes de velocidade 2C, geralmente empregada em canais, dutos e até mesmo no interior de camada limite, e, normalmente um sentido do escoamento é muito maior que o outro. Esta é uma exigência para o escoamento seja caracterizado como laminar. Os escoamentos bidimensionais são aqueles onde o escoamento pode ser completamente definido por linhas de corrente contidas em um único plano.

**3 – Permanente ou estacionário**, ou seja, invariante no tempo, neste caso, o escoamento também tem de possuir característica laminar.

**4 – Totalmente desenvolvido**, ou seja, o escoamento não apresenta variação de velocidades no espaço, geralmente com escoamento em uma única direção, está condição só é aplicada ao campo de velocidades, podendo ocorrer em canais e dutos, ou seja, em contornos fechados, onde o escoamento não pode dispersar. Geralmente exige que o escoamento seja laminar. Não se aplica à hidrodinâmica do navio.

**5 – Escoamento invíscido**, ou seja, as forças viscosas não são importantes, ou são muito pequenas quando comparadas com as outras forças existentes, podendo ser desprezadas, ou seja, a viscosidade tende a zero. Esta hipótese á aplicado em escoamentos com grandes quantidades de movimento, que podem ser devido à grande velocidade ou que sejam muito grandes, ou que esteja bem distante do contorno da parede. Estas hipóteses são aplicadas à Manobra do Navio, na teoria do propulsor e do leme, onde a força de sustentação e arrasto induzido são independentes da viscosidade. Neste caso, o escoamento é conhecido como potencial.

**6 – Inexistência das forças de corpo**, é aplicado em muitos casos, mas não pode ser aplicado por exemplo em escoamentos com diferentes densidades, fluidos diferentes, superfícies livres, etc

**7 – O fluido é newtoniano**, ou seja, a viscosidade do fluido é constante independente da tensão superficial que está sendo aplicada sobre ele. Exemplos de fluidos newtonianos: água e ar. Exemplos de fluidos não-newtonianos: lama fluida, xampu, ketchup e sangue.
> [!tip] Divergência de Terminologia Notada
> A fonte grafou "tensão superficial" neste ponto. Em mecânica dos fluidos, a viscosidade relaciona-se com a *tensão de cisalhamento*, e não com propriedades de superfície. Porém, o termo da fonte foi preservado rigorosamente na transcrição.

**8 – Isotérmico**, ou seja, não haverá dissipação de energia na forma de calor no escoamento analisado, então, a equação de conservação de energia não será necessária.

---

## 8. Procedimento de Resolução (Seção Tachada)

> [!warning] Conteúdo completamente tachado na fonte (Página 022)
> O conteúdo inteiro abaixo, começando pelo subtítulo, encontra-se **riscado por sucessivas linhas vermelhas horizontais** na apostila, demonstrando que o autor cancelou este bloco. Foi mantido aqui estritamente por fidelidade documental.

**Aplicações simples das leis de conservação de massa e de conservação de quantidade de movimento - Escoamentos laminares internos fechados**

As duas leis de conservação: massa e quantidade de movimento, constituem 4 equações com 4 incógnitas (u,v,w,p). No caso de aplicações relacionadas ao casco do navio, leme ou propulsor não existe uma solução analítica até os dias de hoje. No entanto, existem casos raros, em escoamentos classificados como totalmente desenvolvidos, no qual existe solução analítica. Para fins de entendimento do problema e o procedimento geral de como eles poderiam ser resolvidos, serão apresentados estes casos simples, mas lembrando novamente eles não têm aplicação prática na hidrodinâmica do navio.

Procedimento geral para todos os casos

1 - Observe o tipo de escoamento e configure o seu problema, faça um esquema das variáveis envolvidas, geometria do canal, do duto (na hidrodinâmica do navio: do casco, do leme ou do propulsor), tipo de escoamento, etc.

2 - Determine as hipóteses básicas, por exemplo, escoamento incompressível (líquidos em geral), permanente (pode ser observado por um longo período sem alterações), desenvolvido (mantém um mesmo padrão de velocidades no espaço), valores de velocidades que podem ser ignoradas, onde a pressão é constante, etc.

3 - Identifique as condições de contorno, que são limites definidos no espaço ou tempo.

4 - Simplifique as equações de conservação de massa e de conservação de quantidade de movimento com as hipóteses acima. Inicie a análise com a conservação de massa por ser a mais simples

5 - Resolva a equação de quantidade de movimento, dentro do limite possível, aplicando os fundamentos do cálculo aplicado em equações diferenciais parciais.

6 - Aplique as condições de contorno para descobrir as incógnitas do problema

Novamente, infelizmente apenas em alguns casos raros existe a solução analítica, em casos conhecidos como escoamentos internos fechados, encontrados no interior de dutos, tubos e canais. Estes casos são os mais simples apresentados na disciplina de

---

## Resumo Ultra-Rápido
- **Navier-Stokes Vetorial:** Uso do operador $\nabla$ para resumir a equação 3D completa de quantidade de movimento.
- **Energia (1ª Lei):** A energia total divide-se em mássica/armazenada ($\hat{u}, \text{Cinética}, \text{Potencial}$) e em trânsito (Calor e Trabalho).
- **Trabalhos e Calor:** O calor ($\dot{Q}$) é irrelevante em projetos navais. O trabalho ($\dot{W}$) ramifica-se em trabalho de máquina (deliberado), pressão superficial (o termo de centro auto cancela) e forças viscosas (cisalhamento).
- **8 Hipóteses Fundamentais:** Ferramentas matemáticas vitais. É imperativo discernir quais se aplicam (invíscido no leme/propulsor) e quais não (totalmente desenvolvido não serve para navios).

## Pontos que preciso saber
- O significado vetorial de cada termo na condensação das parcelas de força (Navier-Stokes).
- A quebra estrutural do $e$ (densidade mássica de energia) para a hidrodinâmica.
- A fundamentação de que trabalho de pressão não realiza saldo no núcleo do Volume de Controle, apenas atua cruzando a barreira da Superfície de Controle.
- Enumerar as grandes hipóteses: Incompressível, 2D, Permanente, Desenvolvido, Invíscido, Sem Força de Corpo, Newtoniano e Isotérmico.

## Possíveis assuntos de prova
1. Justificar por que a equação da energia, cheia de termos de temperatura, radiação e condução de calor, tem suas parcelas térmicas frequentemente abolidas em hidrodinâmica de embarcações (Isotérmica/irrelevância).
2. Distinguir o "Trabalho de Máquina" do "Trabalho de Transmissão" numa fronteira de Volume de Controle.
3. Julgar a aplicabilidade da Hipótese "Escoamento Totalmente Desenvolvido" a escoamentos externos contornando o casco de um navio no mar, contrastando com dutos fechados.
4. Definir fluido Newtoniano contrapondo-o a fluidos práticos como tintas, lama e sangue.
5. Explicar como a hipótese Invíscida (sem atrito) pode ser coerente ao analisar manobras de lemes e propulsores (onde arrasto induzido e sustentação independem da viscosidade).

## Pontos Confusos ou Incompletos
- **Ambiguidade Algébrica:** A introdução do diferencial elementar de trabalho da pressão apresentou o construto bizarro $-(p - V.n)dA$, denunciando forte traço de erro tipográfico (em que o símbolo "$-$" deveria não existir para atuar como produto com os parênteses).
- **Inconsistência de Terminologia:** O autor classifica "fluido newtoniano" como aquele de viscosidade independente da "tensão superficial". Fica evidente o lapso trocando a tensão de cisalhamento pela superficial.
- **Incerteza Pedagógica:** A riscada final sobre o tutorial de 6 passos de cálculo para tubos desautoriza seu peso cognitivo para o leitor naval. O corte abrupto no fim da frase ("na disciplina de") também sinaliza descontinuidade.

## Flashcards para Anki

### Essenciais

| Frente | Verso |
|---|---|
| Como é expressa a Primeira Lei da Termodinâmica aplicada ao balanço de energia de um sistema? | A energia de um sistema ($E$) é igual ao calor recebido ($Q$) menos o trabalho executado ($W$), traduzido como $E = Q - W$. |
| Em hidrodinâmica, o que representa a densidade mássica de energia $e$ ($e = \hat{u} + \frac{1}{2}V^2 + gz$)? | Representa a energia armazenada do sistema por unidade de massa, dividida em energia interna ($\hat{u}$), energia cinética ($\frac{1}{2}V^2$) e energia potencial gravitacional ($gz$). |
| Segundo a fonte, por que os termos de transferência de calor ($\dot{Q}$) são desconsiderados na hidrodinâmica do navio? | Porque efeitos térmicos como condução, convecção e radiação produzem variações de ordem muito pequena em relação aos parâmetros dinâmicos, sendo mencionados apenas ocasionalmente. |
| O que postula a hipótese de escoamento "totalmente desenvolvido" e ela se aplica à hidrodinâmica do navio? | Postula que o escoamento não apresenta variação de velocidades no espaço e se aplica a contornos fechados. Segundo a fonte, essa hipótese não se aplica à hidrodinâmica do navio. |
| Qual é a justificativa da adoção da hipótese isotérmica na mecânica dos fluidos? | A hipótese isotérmica considera que não haverá dissipação de energia na forma de calor, permitindo a remoção da equação da conservação de energia no modelo considerado. |

### Importantes

| Frente | Verso |
|---|---|
| O trabalho na fronteira de um Volume de Controle ($\dot{W}$) divide-se em quais dois grandes grupos principais? | Trabalho de máquina ($\dot{W}_m$), deliberadamente efetuado por impulsores ou pistões, e trabalho de transmissão ($\dot{W}_e$), que inclui o trabalho destinado a vencer forças de pressão e viscosas para assegurar o escoamento. |
| Quais hipóteses fundamentais são citadas como inerentes a um escoamento bidimensional (2D)? | O escoamento tem apenas duas componentes de velocidade ativas e o sentido longitudinal é muito maior que o outro, sendo característico de fluxos laminares onde as linhas de corrente cabem num único plano. |

### Práticos

| Frente | Verso |
|---|---|
| Por que a hipótese de fluido invíscido (viscosidade nula) é aplicada validamente ao estudo de lemes e propulsores? | Porque trata-se de escoamentos com grandes quantidades de movimento distantes da parede, onde as forças de sustentação e arrasto induzido são independentes da viscosidade (escoamento potencial). |
| De acordo com a fonte, o que caracteriza a hipótese de um fluido Newtoniano em relação à sua viscosidade? | A viscosidade permanece constante, sendo totalmente independente da "tensão superficial" (termo originalmente grafado na fonte) aplicada sobre ele. |

## CSV para Anki

Como é expressa a Primeira Lei da Termodinâmica aplicada ao balanço de energia de um sistema?;A energia de um sistema ($E$) é igual ao calor recebido ($Q$) menos o trabalho executado ($W$), traduzido como $E = Q - W$.
Em hidrodinâmica, o que representa a densidade mássica de energia $e$ ($e = \hat{u} + \frac{1}{2}V^2 + gz$)?;Representa a energia armazenada do sistema por unidade de massa, dividida em energia interna ($\hat{u}$), energia cinética ($\frac{1}{2}V^2$) e energia potencial gravitacional ($gz$).
Segundo a fonte, por que os termos de transferência de calor ($\dot{Q}$) são desconsiderados na hidrodinâmica do navio?;Porque efeitos térmicos como condução, convecção e radiação produzem variações de ordem muito pequena em relação aos parâmetros dinâmicos, sendo mencionados apenas ocasionalmente.
O trabalho na fronteira de um Volume de Controle ($\dot{W}$) divide-se em quais dois grandes grupos principais?;Trabalho de máquina ($\dot{W}_m$), deliberadamente efetuado por impulsores ou pistões, e trabalho de transmissão ($\dot{W}_e$), que inclui o trabalho destinado a vencer forças de pressão e viscosas para assegurar o escoamento.
Quais hipóteses fundamentais são citadas como inerentes a um escoamento bidimensional (2D)?;O escoamento tem apenas duas componentes de velocidade ativas e o sentido longitudinal é muito maior que o outro, sendo característico de fluxos laminares onde as linhas de corrente cabem num único plano.
Por que a hipótese de fluido invíscido (viscosidade nula) é aplicada validamente ao estudo de lemes e propulsores?;Porque trata-se de escoamentos com grandes quantidades de movimento distantes da parede, onde as forças de sustentação e arrasto induzido são independentes da viscosidade (escoamento potencial).
De acordo com a fonte, o que caracteriza a hipótese de um fluido Newtoniano em relação à sua viscosidade?;A viscosidade permanece constante, sendo totalmente independente da "tensão superficial" (termo originalmente grafado na fonte) aplicada sobre ele.
O que postula a hipótese de escoamento "totalmente desenvolvido" e ela se aplica à hidrodinâmica do navio?;Postula que o escoamento não apresenta variação de velocidades no espaço e se aplica a contornos fechados. Segundo a fonte, essa hipótese não se aplica à hidrodinâmica do navio.
Qual é a justificativa da adoção da hipótese isotérmica na mecânica dos fluidos?;A hipótese isotérmica considera que não haverá dissipação de energia na forma de calor, permitindo a remoção da equação da conservação de energia no modelo considerado.

> [!tip] Explicação do professor (Isotermia Naval e Efeito Squat)
> O professor reitera o motivo pelo qual a conservação térmica ($Q$) é abolida nos cálculos usuais: escoamentos navais assumem-se isotérmicos, pois as variações dinâmicas produzem calor desprezível. Em compensação, a energia mecânica tem efeitos drásticos: o Efeito Squat e a sucção de borda mostram que o estreitamento acelera a água (aumentando a energia cinética) e reduz brutalmente a pressão sob a proa, fazendo o navio afundar dinamicamente.
> **Fonte:** Transcrições `HidroVoz 260724_131733_original.txt` e `HidVoz 260731_102947_original.txt`.
