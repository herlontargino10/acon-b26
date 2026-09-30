---
title: "Mecânica dos Fluidos — Capítulo 3"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-011-018.pdf"
pages: "011–018"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - estudo
---

# Mecânica dos Fluidos — Capítulo 3
## Forças atuantes em um elemento fluido

> [!warning] Conteúdo tachado na fonte (Página 011)
> A fonte inicia com fórmulas residuais de aceleração nas direções $y$ e $z$ ($a_y$ e $a_z$) e a condição para escoamento permanente ($\frac{\partial u}{\partial t} = 0$, etc.). **Todo esse bloco inicial encontra-se tachado por um risco vermelho contínuo na fonte**. O conteúdo válido começa a partir do subtítulo destacado em amarelo "Forças atuantes em um elemento fluido".

## 1. A Segunda Lei de Newton por Unidade de Volume

### Explicação
Em mecânica dos fluidos, é comum pensar em termos relacionados à **unidade de volume**, onde o observador estabelece uma janela de observação arbitrária no interior desse volume.

A Segunda Lei de Newton para esse elemento de fluido passa a ser descrita dividindo a força e a massa pelo volume ($Vol$):
$$
\frac{D(\frac{m}{Vol}V)}{Dt} = \frac{F}{Vol}
$$

Como a densidade é a massa pelo volume ($\frac{m}{Vol} = \rho$), a derivada material passa a ser:
$$
\frac{D(\rho V)}{Dt} = \frac{F}{Vol}
$$

> [!important] Observação
> Do lado esquerdo, tem-se a aceleração total do fluido. Do lado direito, qualquer força que tenha alterado o seu movimento.

Na hidrodinâmica do navio, o escoamento é considerado incompressível, logo a densidade $\rho$ sai da derivada:
$$
\rho \frac{D(V)}{Dt} = \frac{F}{Vol}
$$

### Possível pergunta do professor
**Pergunta:** A equação $\rho \frac{D(V)}{Dt} = \frac{F}{Vol}$ é aparentemente simples. Mas de onde vêm as forças externas representadas no lado direito?
**Resposta:** Apesar desta equação ser aparentemente simples, existe uma série de complexidades do lado direito. De onde as forças externas podem vir? Considerando um objeto sólido, por exemplo, um cubo, como é possível fazer este cubo se mover?

---

## 2. Tipos de Forças no Fluido

Considerando a analogia de mover um cubo, existem basicamente duas categorias de atuação de forças:

| Categoria | Descrição | Exemplos |
| :--- | :--- | :--- |
| **Forças superficiais** | Exigem tocar o cubo. Dividem-se em **forças normais** e **forças tangenciais**. | Empurrar (normal) ou tracionar lateralmente (tangencial) as superfícies. |
| **Forças de corpo** | Movem o cubo sem a necessidade de tocá-lo fisicamente (forças de campo). | Forças eletromagnéticas, força gravitacional. |

Em mecânica dos fluidos, as grandezas são tipicamente associadas da seguinte forma:
- **Forças normais:** Geralmente associadas às forças de **pressão**.
- **Forças tangenciais:** Associadas à **tensão de cisalhamento** (ou fricção), dada pela **viscosidade**.
- **Forças de corpo:** Associadas a forças gravitacionais, magnéticas, etc.

---

## 3. As Forças Normais ou de Pressão

### Definição
A força de pressão resulta das colisões das partículas do fluido com as superfícies de controle com as quais está em contato. 

A **Lei de Pascal** mostra que as forças de pressão exercidas por um fluido em equilíbrio sobre as superfícies atuam de forma **perpendicular** a essas superfícies.

### Nomenclatura ($\sigma_{ij}$)
As forças superficiais normais atuam perpendicularmente às superfícies do cubo e são denotadas pela letra grega $\sigma$, geralmente com dois índices ($\sigma_{ij}$):
- O primeiro índice ($i$) denota o **sentido normal da superfície** escolhida.
- O segundo índice ($j$) denota o **sentido da componente de força**.

### Dedução da Força de Pressão
A pressão é responsável pela alteração do movimento dos fluidos. Considerando inicialmente um volume de controle cúbico (dimensões $\Delta x, \Delta y, \Delta z$) e movimento apenas na direção $x$:
- Na superfície de entrada, existe uma pressão maior ($p_1$).
- Na superfície de saída, existe uma pressão menor ($p_2$).

A diferença de pressão gera uma força, que gera aceleração, que altera o movimento. Lembrando que $p = \frac{F}{A}$ ou $F = pA$, a força na direção $x$ é:
$$
F_x = p_2 A_2 - p_1 A_1
$$

No caso particular do cubo, as áreas de entrada e saída são idênticas: $A_2 = A_1 = \Delta y \Delta z$.
$$
F_x = (p_2 - p_1)\Delta y \Delta z
$$
Fazendo a substituição $(p_2 - p_1) = \Delta p$, tem-se a força discreta:
$$
F_x = \Delta p \Delta y \Delta z
$$

> [!warning] Atenção ao sinal
> Se o sinal da força for negativo, significa que a força começou com uma intensidade maior na entrada ($p_1$) e terminou com uma intensidade menor na saída ($p_2$). A força efetiva acelera o fluido no sentido da queda de pressão.

### Força de Pressão por Unidade de Volume
Na mecânica dos fluidos, trabalha-se por unidade de volume ($Vol = \Delta x \Delta y \Delta z$). Dividindo a força de pressão encontrada pelo volume:
$$
\frac{F_x}{\Delta x \Delta y \Delta z} = \frac{\Delta p}{\Delta x}
$$

Fazendo o limite $\Delta \to 0$, a força de pressão por unidade de volume na direção $x$ torna-se a derivada parcial (gradiente):
$$
\frac{F_x}{Vol} = \frac{\partial p}{\partial x}
$$
> [!tip] Interpretação sobre a grafia da fonte
> Na fonte (Página 014), o termo denominador do volume aparece grafado com um "V" manuscrito cortado horizontalmente para diferenciá-lo da velocidade. O termo representa o Volume ($Vol$), alinhando-se com a nomenclatura textual utilizada na página 011. O OCR tende a confundir com $D_{Vol}$.

De forma similar, existem ainda duas outras forças para as componentes nas direções $y$ e $z$:
$$
\frac{F_y}{Vol} = \frac{\partial p}{\partial y}
$$
$$
\frac{F_z}{Vol} = \frac{\partial p}{\partial z}
$$

A Segunda Lei de Newton (para escoamento incompressível), considerando apenas as forças de pressão (com pressão maior na entrada e a convenção de aceleração fluida inserindo o sinal negativo), passa a ser descrita como:
$$
\rho \frac{Du}{Dt} = - \frac{\partial p}{\partial x}
$$
$$
\rho \frac{Dv}{Dt} = - \frac{\partial p}{\partial y}
$$
$$
\rho \frac{Dw}{Dt} = - \frac{\partial p}{\partial z}
$$

---

## 4. As Forças Tangenciais (Friccionais ou Viscosas)

### Definição
As forças tangenciais (também conhecidas como friccionais ou viscosas) atuam paralelamente à superfície. São denotadas pela letra grega $\tau$, com os mesmos dois índices $\tau_{ij}$ (normal e direção da força), e estão diretamente relacionadas aos **efeitos viscosos**.

### Exemplo da Fonte: A Analogia dos Trens
Para ilustrar a força viscosa, imagine **dois trens viajando em velocidades diferentes ($u_1$ e $u_2$)**.
- Você se encontra no trem errado (Trem 1) com velocidade $u_1$.
- O seu trem desejado (Trem 2) com velocidade $u_2$ está passando ao lado.
- Você decide saltar de um trem para o outro. Com isso, realiza uma **alteração de quantidade de movimento** em ambos os trens (sua velocidade original $u_1$ passou para $u_2$).
- Pela Segunda Lei de Newton, se existe alteração de velocidade, existe uma força atuando.
- **Se os dois trens tivessem a mesma velocidade, essa força não existiria.**

### Interpretação Física no Fluido
Isto é análogo ao escoamento em torno de uma parede. Próximo à parede, o escoamento tem velocidade menor; mais distante, velocidade maior. 
As pessoas dentro do trem podem ser vistas como **partículas fluidas saltando de uma camada para outra**. Quando saltam, têm de ser aceleradas, impactando em uma força: a **força viscosa**.
> [!important]
> Para que exista força viscosa é expressamente **necessária a existência de diferentes velocidades adjacentes** (um gradiente de velocidade).

### Dedução Analógica da Viscosidade Dinâmica ($\mu$)
A tensão de cisalhamento também é uma força dividida por unidade de área, assim como a pressão:
$$
\tau = \frac{F}{A} \quad \text{ou} \quad F = \tau A
$$
Para o escoamento na direção $x$:
$$
\tau_{yx} = \frac{F_x}{A} = \frac{m \Delta u}{A \Delta t}
$$
O termo $\frac{\Delta u}{\Delta t}$ é puramente temporal e é relacionado a $\Delta y$ na física intercamadas. Multiplicando a equação por $\frac{\Delta y}{\Delta y}$ (sem alterar o resultado):
$$
\frac{\Delta u}{\Delta t} = \frac{\Delta u \Delta y}{\Delta t \Delta y} \to \frac{\Delta y \Delta u}{\Delta t \Delta y}
$$
$$
\tau_{yx} = \frac{m \Delta u}{A \Delta t} = \frac{m \Delta y \Delta u}{A \Delta t \Delta y}
$$
Em física, o valor central isolado $\frac{m \Delta y}{A \Delta t}$ não tem significado teórico direto ou explicação subjacente. Ele é obtido empiricamente através de medidas, resultando em uma constante conhecida como **viscosidade dinâmica**, simbolizada por $\mu$.
$$
\mu = \frac{m \Delta y}{A \Delta t}
$$
Resultando na equação fundamental:
$$
\tau_{yx} = \mu \frac{\Delta u}{\Delta y}
$$
Todo fluido real possui viscosidade dinâmica, podendo ela variar com temperatura, pressão, altitude ou tensão cisalhante local.

### A Condição de Aceleração (Rotação vs. Translação)
> [!warning] Atenção (Diferença de Tensão)
> Assim como no caso de pressões, é necessário que exista **diferença** entre tensões cisalhantes para que exista aceleração. Se a tensão cisalhante for exatamente a mesma em cima ($\tau_2$) e embaixo ($\tau_1$) do cubo de controle, **não existirá aceleração de translação em y**. O cubo apenas irá girar. É necessária a diferença entre as tensões para o aparecimento da força viscosa efetiva.

### Força Viscosa por Unidade de Volume
Assim como na pressão, a força viscosa 1D em $x$ é a diferença de tensões cisalhantes:
$$
F_{yx} = \tau_2 A_2 - \tau_1 A_1
$$
Usando a condição $A_2 = A_1 = \Delta x \Delta z$:
$$
F_{yx} = (\tau_2 - \tau_1)\Delta x \Delta z
$$
Sendo $\tau_2 - \tau_1 = \Delta \tau$:
$$
F_{yx} = \Delta \tau \Delta x \Delta z
$$
Dividindo pelo volume ($\Delta x \Delta y \Delta z$):
$$
\frac{F_{yx}}{\Delta x \Delta y \Delta z} = \frac{\Delta \tau}{\Delta y}
$$
Fazendo uso da equação calculada anteriormente ($\tau_{yx} = \mu \frac{\Delta u}{\Delta y}$):
$$
\frac{\Delta}{\Delta y}\left(\mu \frac{\Delta u}{\Delta y}\right) = \mu \frac{\Delta^2 u}{\Delta y^2}
$$
> [!tip] Observação Matemática
> A fonte utiliza um abuso de notação pedagógico elevando a variação finita a "quadrado" ($\Delta^2$) para denotar a derivada de segunda ordem.

Fazendo $\Delta \to 0$, obtém-se o termo diferencial de segunda ordem:
$$
\frac{F_{yx}}{Vol} = \mu \frac{\partial^2 u}{\partial y^2}
$$

Esta componente é apenas um terço da força viscosa na direção $x$ (considerando saltos apenas na direção $y$). No caso 3D, as partículas podem saltar em qualquer direção, resultando no Laplaciano completo:

### Forma apresentada na fonte
$$
\frac{F_{yx}}{Vol} = \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)
$$
### Observação de inconsistência técnica (preservada da fonte)
A fonte generaliza o comportamento físico da força viscosa para as 3 direções, porém mantém a notação restritiva $\frac{F_{yx}}{Vol}$ no lado esquerdo da igualdade, o que indicaria estritamente a tensão do plano $yx$. Fisicamente, o termo direito corresponde à totalidade da difusão 3D. A equação original foi mantida.

---

## 5. A Lei de Conservação da Quantidade de Movimento (Pressão + Viscosidade)

Incluindo as forças de pressão e as forças viscosas (e omitindo até aqui as de corpo), as leis de conservação nas três direções passam a ser modeladas como:

Na direção $x$:
$$
\rho \frac{Du}{Dt} = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)
$$

Nas direções $y$ e $z$, respectivamente:
$$
\rho \frac{Dv}{Dt} = - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2} \right)
$$
$$
\rho \frac{Dw}{Dt} = - \frac{\partial p}{\partial z} + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2} \right)
$$
> [!tip] Correção tipográfica
> A equação do eixo $z$ reflete corretamente a derivada direcional $x^2$ no Laplaciano (conforme a imagem visual do PDF), corrigindo desvios pregressos de transcrição.

---

## 6. As Forças de Corpo e as Equações Finais (Seção Tachada)

> [!warning] Conteúdo completamente tachado na fonte (Página 018)
> Todo o conteúdo listado abaixo, incluindo os textos, exemplos e as equações completas de Navier-Stokes, encontra-se **completamente tachado** (riscado por linhas vermelhas contínuas horizontais) no material original. O conteúdo está sendo preservado abaixo estritamente para não apagar o registro histórico do documento.

### O texto cancelado da fonte
Em hidrodinâmica do navio as forças de corpo comuns são a gravidade e o empuxo, em manobra do navio as forças de Coriolis e Centrípetas são incluídas. Outro exemplo de força de corpo são as magnéticas, elétricas. Ou seja, as forças de corpo, podem ser de diferentes fontes dependendo da situação.

A inclusão gravitacional é dada por:
$$
F_x = m g = \rho \Delta x \Delta y \Delta z g_x
$$
Onde $g_x$ é a componente da aceleração gravitacional na direção $x$. A força por unidade de volume tem-se:
$$
\frac{F_x}{\Delta x \Delta y \Delta z} = \rho g_x
$$

### As Equações combinadas (Tachadas)
Combinando as forças superficiais com as forças de corpo:
$$
\rho \frac{Du}{Dt} = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x
$$

Ou expandindo a derivada material $\frac{Du}{Dt}$:
$$
\rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) + \rho g_x
$$

De forma similar nas direções $y$ e $z$, serão respectivamente:
### Forma apresentada na fonte (Tachada)
$$
\rho \left( \frac{\partial y}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right) = - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2} \right) + \rho g_y
$$
### Observação
A fonte perseverou na manutenção do erro de notação anterior grafando o termo de aceleração local em $y$ como $\frac{\partial y}{\partial t}$ no lugar da componente da velocidade correta $\frac{\partial v}{\partial t}$. O erro foi replicado fidedignamente.

$$
\rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right) = - \frac{\partial p}{\partial z} + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2} \right) + \rho g_z
$$

---

## Resumo Ultra-Rápido
- **Newton por Volume:** A dinâmica dos fluidos modela as forças (contato e de campo) por unidade de volume ($Vol$).
- **Pressão:** Força normal que cria escoamento. Sua inserção no equacionamento se dá através do gradiente negativo espacial ($-\frac{\partial p}{\partial x}$).
- **Viscosidade:** Força tangencial de contato originada pelo atrito. Depende essencialmente de partículas "saltando" entre correntes adjacentes de velocidades diferentes. Produz os termos espaciais de segunda ordem (Laplaciano) multiplicados pela viscosidade dinâmica ($\mu$).
- **Giro x Translação:** Tensões iguais e opostas anulam a aceleração de translação (corpo gira). Só há movimento direcional com diferença de tensões.
- **Forças de corpo:** Modeladas externamente pelo termo genérico $\rho g_x$. Toda a seção final 3D foi riscada na apostila.

## Prováveis Assuntos de Prova
1. Explicar conceitualmente de onde vêm as forças normais e as tangenciais no interior de um escoamento, diferenciando o motivo físico da existência de cada uma.
2. Demonstrar o desenvolvimento (com a analogia dos trens) do porquê o gradiente espacial da velocidade justificar o surgimento da tensão de cisalhamento.
3. Explicar o que ocorre mecanicamente a um elemento cúbico de fluido caso sofra tensões cisalhantes rigorosamente iguais em faces opostas.
4. Distinguir quais parcelas dependem do volume e como ocorre a passagem da força discreta ($\Delta p, \Delta \tau$) para os operadores diferenciais nas equações de movimento.

## Pontos Confusos ou Incompletos
- **Uso não rigoroso de operadores de diferenças finitas:** $\Delta^2 u$ é usado como se fosse o quadrado do delta linear de uma derivada, em caráter totalmente heurístico e informal para a dedução das equações de estado.
- **Cancelamentos:** Todo o topo da primeira folha do documento (equações em $y$ e $z$) e todo o equacionamento em bloco de Navier-Stokes do final estão tachados.
- **Símbolos problemáticos:** O Volume em alguns momentos cruza uma linha graficamente análoga a $D_{Vol}$ e erros em variáveis locais como $a_y$ exibindo $\partial y$ em vez de $\partial v$.

## Flashcards para Anki

### CSV para Anki
```csv
Como é expressa a 2ª Lei de Newton por unidade de volume para escoamento incompressível?;"A equação passa a ser: $\rho \frac{D(V)}{Dt} = \frac{F}{Vol}$"
Na mecânica dos fluidos, como se classificam as forças superficiais que causam alteração de movimento?;"Classificam-se em forças normais (associadas à pressão) e forças tangenciais (associadas à tensão de cisalhamento ou viscosidade)."
Segundo a Lei de Pascal, como atuam as forças de pressão num fluido em equilíbrio em relação às superfícies?;"Elas se exercem perpendicularmente às superfícies de contato."
Na convenção de dois índices para tensões ($\sigma_{ij}$ ou $\tau_{ij}$), o que representam o primeiro e o segundo índice, respectivamente?;"O primeiro ($i$) denota o sentido normal da superfície e o segundo ($j$) denota o sentido da componente de força."
Na analogia dos trens (partículas saltando entre camadas), qual a condição fundamental para que exista força viscosa?;"É necessária a existência de velocidades adjacentes diferentes (um gradiente espacial de velocidade)."
Se a tensão cisalhante na face superior de um cubo for rigorosamente igual à da face inferior ($\tau_2 = \tau_1$), o que acontece com a aceleração de translação vertical?;"Ela é nula ($a_y = 0$). Sem diferença de tensões, o cubo apenas gira, mas não presenciará aceleração de translação."
O termo empírico que amarra matematicamente a força resistiva das partículas saltando entre camadas é a constante $\mu$. Como se chama?;"Viscosidade dinâmica."
Quais os termos espaciais que modelam a atuação da viscosidade nas 3 direções, formados pela expansão da diferença finita (Laplaciano)?;"Termos diferenciais de segunda ordem das velocidades, multiplicados por $\mu$. Exemplo na direção x: $\mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)$"
```
