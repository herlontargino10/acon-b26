---
title: "Simulado — Mecânica dos Fluidos — Capítulo 1"
chapter: 1
subject: "Mecânica dos Fluidos"
type: "simulado"
format: "Obsidian"
---

# Simulado — Mecânica dos Fluidos
## Capítulo 1 — Leis de Conservação e Conservação da Massa

> [!info] Instruções
> Responda sem consultar o gabarito. Quando houver cálculo, apresente o raciocínio.

---

# Parte I — Conceitos Fundamentais

### 1. 
Quais são as três propriedades fundamentais conservadas quando um fluido se move?

- **(a)** Massa, velocidade e pressão
- **(b)** Massa, quantidade de movimento e energia
- **(c)** Massa, volume e densidade
- **(d)** Energia, pressão e temperatura

### 2.
No contexto apresentado para a Hidrodinâmica do Navio, quais princípios de conservação são tipicamente empregados?

Explique também em que situação a conservação da energia passa a ser especialmente relevante segundo o material.

### 3.
Diferencie:

- massa $m$;
- massa específica $\rho$;
- volume $V$.

Apresente a relação matemática entre essas grandezas.

### 4.
O que é um **volume de controle**?

Explique por que ele é considerado uma região fixa no espaço e o que acontece com o fluido em relação a essa região.

### 5.
Explique o que significa dizer que a conservação da massa é uma **lei de conservação local**.

Não basta repetir a expressão "é local"; explique fisicamente a ideia.

---

# Parte II — Interpretação Física

### 6.
Considere um volume de controle no qual entra determinada quantidade de massa e sai uma quantidade maior.

O que necessariamente acontece com a massa armazenada dentro do volume de controle?

Explique o significado físico do sinal negativo que aparece no desenvolvimento da equação.

### 7.
A expressão da vazão mássica é:

$$
\dot m=\rho uA
$$
Explique fisicamente o significado de cada uma das três grandezas presentes no lado direito.

### 8.
Um estudante afirma:

> "Para aplicar a conservação da massa, basta conhecer a velocidade do fluido."

Com base no capítulo, explique por que essa afirmação está incompleta ou incorreta.

### 9.
No caso incompressível, o material chega à relação:
$$
\nabla\cdot\mathbf V=0
$$
O que essa relação significa fisicamente no contexto apresentado?

### 10.
O material enfatiza que o importante não é simplesmente conhecer $u$, $v$ e $w$, mas suas **variações espaciais**.

Explique essa diferença utilizando:
$$
\frac{\partial u}{\partial x},
\qquad
\frac{\partial v}{\partial y},
\qquad
\frac{\partial w}{\partial z}.
$$
---

# Parte III — Equações e Desenvolvimento

### 11.
Escreva a forma diferencial geral da equação da continuidade.

### 12.
Escreva a forma vetorial da conservação da massa apresentada no capítulo.

Identifique o significado de $\mathbf V$.

### 13.
Qual é a diferença entre a forma geral da continuidade e sua forma para um fluido incompressível?

Mostre matematicamente a simplificação apresentada no material.

### 14.
Para um fluido incompressível, escreva a equação da continuidade em coordenadas cartesianas.

### 15.
Relacione corretamente cada caso à sua equação:

| Caso | Equação |
|---|---|
| 1D | ? |
| 2D | ? |
| 3D | ? |

Utilize somente as relações apresentadas no capítulo.

---

# Parte IV — Aplicação e Raciocínio

### 16.
Um escoamento incompressível é considerado unidimensional.

O material estabelece:
$$
\frac{\partial u}{\partial x}=0
$$
Explique fisicamente o que isso significa para a entrada e a saída do volume de controle.

### 17.
Em determinado caso 2D, o material apresenta:
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
$$
Por que aparece o sinal negativo associado à direção $x$?

A resposta deve considerar a **orientação da normal da superfície** e a direção da velocidade.

### 18.
Em um caso 3D, a conservação da massa é expressa por:
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
$$
Explique, fisicamente, o que essa equação está dizendo sobre o balanço entre as diferentes direções.

### 19.
Um volume de controle possui:
$$
\frac{\partial u}{\partial x}>0
$$
Segundo a interpretação apresentada no capítulo, o que isso representa?

### 20.
Um estudante observa:
$$
u=5\;m/s
$$
e conclui:

> "Como a velocidade é positiva, existe necessariamente massa saindo na direção $x$."

Essa conclusão está de acordo com a interpretação apresentada no capítulo?

Justifique utilizando a diferença entre $u$ e $\partial u/\partial x$.

---

# Parte V — Questões Integrativas

### 21.
Reconstitua a sequência lógica utilizada no desenvolvimento da conservação da massa:
$$
\text{leis de conservação}
\rightarrow
\text{massa específica}
\rightarrow
\text{volume de controle}
\rightarrow
\text{balanço}
\rightarrow
\text{vazão mássica}
$$
Utilize os conceitos apresentados no fechamento do capítulo.

### 22.
Explique como o desenvolvimento parte de um caso **1D** e chega à formulação **3D**.

Sua resposta deve mencionar o papel de $u$, $v$ e $w$.

### 23.
Explique a passagem da expressão em diferenças para a forma diferencial da conservação da massa.

O que acontece quando:
$$
\Delta\rightarrow0?
$$
### 24.
Explique a relação entre:
$$
\nabla\cdot(\rho\mathbf V)
+
\frac{\partial\rho}{\partial t}=0
$$
e
$$
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
+
\frac{\partial\rho}{\partial t}=0.
$$
### 25.
Explique a relação entre **conservação da massa**, **equação da continuidade** e **incompressibilidade**.

A resposta deve deixar claro que esses três termos não significam exatamente a mesma coisa.

---

# Parte VI — Questões Numéricas

### 26.
Um fluido possui massa específica:
$$
\rho=1000\;kg/m^3
$$
e atravessa uma área:
$$
A=2\;m^2
$$
com velocidade:
$$
u=3\;m/s.
$$
Determine a vazão mássica utilizando:
$$
\dot m=\rho uA.
$$
### 27.
Uma seção de escoamento possui:
$$
\rho_1=1000\;kg/m^3,
\qquad
u_1=2\;m/s,
\qquad
A_1=3\;m^2.
$$
Determine:
$$
\dot m_{in}.
$$
### 28.
Considere um escoamento incompressível 2D em que:
$$
\frac{\partial u}{\partial x}=4\;s^{-1}.
$$
Utilizando:
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y},
$$
determine:
$$
\frac{\partial v}{\partial y}.
$$
Interprete o sinal obtido.

### 29.
Em um escoamento incompressível 3D:
$$
\frac{\partial u}{\partial x}=2\;s^{-1},
\qquad
\frac{\partial v}{\partial y}=-0,5\;s^{-1}.
$$
Determine:
$$
\frac{\partial w}{\partial z}.
$$
Utilize:
$$
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}=0.
$$
### 30.
Um estudante recebe o seguinte conjunto de informações:
$$
\frac{\partial u}{\partial x}=3,
\qquad
\frac{\partial v}{\partial y}=-1,
\qquad
\frac{\partial w}{\partial z}=-2.
$$
Determine se essas informações são compatíveis com a conservação da massa para um escoamento incompressível.

Justifique matematicamente.

---

# Gabarito

> [!warning] Antes de consultar
> Tente resolver todas as questões antes de abrir esta seção.

## 1

**Resposta: (b).**

As três propriedades fundamentais são:

- conservação da massa;
- conservação da quantidade de movimento;
- conservação da energia.

## 2

Conservação da massa e conservação da quantidade de movimento.

A conservação da energia é indicada para casos mais complicados, nos quais a **temperatura** é geralmente uma variável importante.

## 3

- $m$ = massa;
- $\rho$ = massa específica;
- $V$ = volume.

Relação:
$$
m=\rho V
$$
## 4

Um volume de controle é uma **região fixa no espaço**, utilizada para analisar o fluido. O fluido pode entrar ou sair através de suas superfícies.

## 5

A conservação local significa que uma quantidade de massa não pode simplesmente desaparecer em um ponto e aparecer em outro sem atravessar o espaço entre os dois pontos.

## 6

Se sai mais massa do que entra, a massa armazenada dentro do volume de controle **diminui**.

O sinal negativo representa justamente essa diminuição da massa interna.

## 7

Na expressão
$$
\dot m=\rho uA
$$
- $\rho$ = massa específica;
- $u$ = velocidade;
- $A$ = área da face.

## 8

A afirmação está incompleta porque o capítulo destaca que são necessárias as **variações espaciais das velocidades**, e não simplesmente os valores de $u$, $v$ e $w$.

## 9

No caso incompressível,
$$
\nabla\cdot\mathbf V=0
$$
representa o balanceamento das variações espaciais das componentes da velocidade.

## 10

O foco está nas variações espaciais:
$$
\frac{\partial u}{\partial x},
\qquad
\frac{\partial v}{\partial y},
\qquad
\frac{\partial w}{\partial z}
$$
e não simplesmente nos valores de $u$, $v$ e $w$.

## 11
$$
\boxed{
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
+
\frac{\partial\rho}{\partial t}
=0
}
$$
## 12
$$
\boxed{
\nabla\cdot(\rho\mathbf V)
+
\frac{\partial\rho}{\partial t}
=0
}
$$
com
$$
\mathbf V=(u,v,w).
$$
## 13

No caso incompressível, a massa específica é considerada constante e:
$$
\frac{\partial\rho}{\partial t}=0.
$$
A equação reduz-se a:
$$
\boxed{\nabla\cdot\mathbf V=0}
$$
## 14
$$
\boxed{
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
=0
}
$$
## 15

**1D:**
$$
\frac{\partial u}{\partial x}=0
$$
**2D:**
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
$$
**3D:**
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
$$
## 16

No caso 1D incompressível:
$$
\frac{\partial u}{\partial x}=0.
$$
Isso significa que não há variação de $u$ ao longo de $x$. O que entra no volume de controle deve ser exatamente o que sai.

## 17

O sinal negativo está relacionado à **orientação da normal da superfície** em relação à direção da velocidade $u$.

## 18

A variação na direção $x$ é equilibrada pelas variações nas direções $y$ e $z$.

## 19

Segundo a interpretação apresentada no material:
$$
\frac{\partial u}{\partial x}>0
$$
indica massa saindo na direção $x$.

## 20

**Não.**

O valor
$$
u=5\;m/s
$$
não é, por si só, a grandeza usada nessa interpretação.

O capítulo relaciona essa situação a:
$$
\frac{\partial u}{\partial x}>0.
$$
A velocidade e sua variação espacial são grandezas diferentes.

## 21

A sequência é:
$$
\boxed{
\text{Leis de conservação}
\rightarrow
\text{massa específica}
\rightarrow
\text{volume de controle}
\rightarrow
\text{balanço}
\rightarrow
\text{vazão mássica}
}
$$
## 22

O desenvolvimento começa considerando um escoamento 1D na direção $x$, representado por $u$.

Depois são incorporadas as demais direções:

- $v$ na direção $y$;
- $w$ na direção $z$.

Assim chega-se à formulação 3D.

## 23

Quando:
$$
\Delta\rightarrow0
$$
as diferenças utilizadas no desenvolvimento passam a representar derivadas parciais.

## 24

A expressão vetorial
$$
\nabla\cdot(\rho\mathbf V)
+
\frac{\partial\rho}{\partial t}
=0
$$
é a forma compacta da expressão cartesiana:
$$
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
+
\frac{\partial\rho}{\partial t}
=0.
$$
## 25

- **Conservação da massa:** é a lei física de conservação.
- **Equação da continuidade:** é a forma matemática usada para expressar essa conservação.
- **Incompressibilidade:** é a hipótese que permite simplificar a equação para o caso tratado no capítulo.

No caso incompressível:
$$
\nabla\cdot\mathbf V=0.
$$
## 26
$$
\dot m=\rho uA
$$
$$
\dot m=(1000)(3)(2)
$$
$$
\boxed{\dot m=6000\;kg/s}
$$
## 27
$$
\dot m_{in}=\rho_1u_1A_1
$$
$$
\dot m_{in}=(1000)(2)(3)
$$
$$
\boxed{\dot m_{in}=6000\;kg/s}
$$
## 28
$$
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
$$
Como:
$$
\frac{\partial u}{\partial x}=4\;s^{-1},
$$
então:
$$
\boxed{
\frac{\partial v}{\partial y}
=
-4\;s^{-1}
}
$$
## 29

Partindo de:
$$
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}=0
$$
temos:
$$
2+(-0,5)+\frac{\partial w}{\partial z}=0
$$
Logo:
$$
\boxed{
\frac{\partial w}{\partial z}
=
-1,5\;s^{-1}
}
$$
## 30

Para um escoamento incompressível:
$$
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}=0.
$$
Substituindo:
$$
3+(-1)+(-2)=0.
$$

Portanto, as informações são **compatíveis** com a conservação da massa.

---

# Resumo da Estrutura

> [!success] Padrão para os próximos capítulos
> Este simulado mantém a estrutura de estudo do capítulo e pode servir como base de organização no Obsidian.

1. **Parte I — Conceitos Fundamentais**
2. **Parte II — Interpretação Física**
3. **Parte III — Equações e Desenvolvimento**
4. **Parte IV — Aplicação e Raciocínio**
5. **Parte V — Questões Integrativas**
6. **Parte VI — Questões Numéricas**
7. **Gabarito separado**

> [!important] Regra de conteúdo
> O conteúdo do simulado deve ser construído exclusivamente a partir do `.md` correspondente ao capítulo.

# Gabarito Comentado

## Questão 1
**Resposta correta:** (b)

**Por que está correta:**
O material afirma explicitamente que as três propriedades fundamentais conservadas quando um fluido se move são a conservação da massa, da quantidade de movimento e da energia.

**Análise das alternativas:**
- **(a)** Errada — O resumo não elenca "velocidade e pressão" como propriedades de conservação fundamentais.
- **(b)** Correta — Elenca as três leis corretas: massa, quantidade de movimento e energia.
- **(c)** Errada — "Volume e densidade" não são leis de conservação listadas no resumo.
- **(d)** Errada — Embora a energia seja conservada, "pressão e temperatura" não são leis de conservação apresentadas, sendo temperatura citada apenas como uma variável.

**Conceito cobrado:** Leis de Conservação
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 2
**Resposta correta:** Discursiva

**Por que está correta:**
Na Hidrodinâmica do Navio, empregam-se tipicamente a conservação da massa e da quantidade de movimento. A conservação da energia passa a ser relevante em casos mais complicados onde a temperatura é uma variável importante.

**Conceito cobrado:** Leis de Conservação
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 3
**Resposta correta:** Discursiva

**Por que está correta:**
Massa ($m$) é a quantidade total considerada; massa específica ($\rho$) é a densidade absoluta que relaciona a massa ao volume; e o volume ($V$) é o espaço ocupado. A relação matemática apresentada no material é $m = \rho V$.

**Conceito cobrado:** Massa e Massa Específica
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 4
**Resposta correta:** Discursiva

**Por que está correta:**
Um volume de controle é uma região fixa no espaço, de forma arbitrária, utilizada para analisar o fluido. Ele é fixo para permitir o balanço do fluxo, sendo que o fluido atravessa suas superfícies de entrada e saída.

**Conceito cobrado:** Volume de Controle
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 5
**Resposta correta:** Discursiva

**Por que está correta:**
A conservação da massa é local porque uma quantidade de massa não pode ir de um ponto A para um ponto B sem passar pelo espaço intermediário (não pode desaparecer nem teletransportar). Isso permite que seja analisada através de um pequeno volume de controle.

**Conceito cobrado:** Conservação Local da Massa
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 6
**Resposta correta:** Discursiva

**Por que está correta:**
A massa armazenada dentro do volume de controle necessariamente diminui. O sinal negativo que aparece no balanço de massa representa fisicamente essa diminuição da massa interna quando há mais massa saindo do que entrando.

**Conceito cobrado:** Balanço Inicial de Massa / Conservação da Massa - Caso 1D
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 7
**Resposta correta:** Discursiva

**Por que está correta:**
Na expressão $\dot m = \rho u A$, $\rho$ é a massa específica (densidade absoluta), $u$ é a velocidade na qual o fluido se move, e $A$ é a área da face da superfície de controle que está sendo atravessada.

**Conceito cobrado:** Vazão Mássica
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 8
**Resposta correta:** Discursiva

**Por que está correta:**
A afirmação está incompleta porque o material destaca que, para aplicar a lei da conservação da massa, o mais importante são as variações espaciais da velocidade ($\partial u/\partial x$, etc.), e não simplesmente os valores da velocidade propriamente dita.

**Conceito cobrado:** Observação Final do Professor/Material
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 9
**Resposta correta:** Discursiva

**Por que está correta:**
No contexto de fluido incompressível, a equação $\nabla\cdot\mathbf V=0$ representa o balanceamento das variações espaciais das componentes da velocidade, já que a massa específica é constante.

**Conceito cobrado:** Caso Incompressível / Interpretação Física das Derivadas
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 10
**Resposta correta:** Discursiva

**Por que está correta:**
As variáveis $u$, $v$ e $w$ são apenas os valores das componentes de velocidade. As derivadas $\partial u/\partial x$, $\partial v/\partial y$ e $\partial w/\partial z$ representam as variações espaciais da velocidade nessas direções, que são as grandezas efetivamente requeridas para aplicar o balanço de massa no escoamento.

**Conceito cobrado:** Interpretação Física das Derivadas
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 11
**Resposta correta:** Discursiva

**Por que está correta:**
A forma diferencial geral, também chamada de equação da continuidade, é: $\frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} + \frac{\partial(\rho w)}{\partial z} + \frac{\partial\rho}{\partial t} = 0$.

**Conceito cobrado:** Forma Diferencial da Conservação da Massa
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 12
**Resposta correta:** Discursiva

**Por que está correta:**
A forma vetorial é expressa por $\nabla\cdot(\rho\mathbf V) + \frac{\partial\rho}{\partial t} = 0$, onde $\mathbf V = (u,v,w)$ representa o vetor velocidade.

**Conceito cobrado:** Forma Vetorial
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 13
**Resposta correta:** Discursiva

**Por que está correta:**
A forma geral contém o termo referente à variação temporal da densidade ($\partial\rho/\partial t$). No caso de um fluido incompressível, a massa específica é constante ($\partial\rho/\partial t = 0$), simplificando a equação para $\nabla\cdot\mathbf V = 0$.

**Conceito cobrado:** Caso Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 14
**Resposta correta:** Discursiva

**Por que está correta:**
Para um escoamento incompressível em coordenadas cartesianas, a equação da continuidade se reduz a: $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$.

**Conceito cobrado:** Caso Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 15
**Resposta correta:** Discursiva

**Por que está correta:**
Segundo o material, as relações incompressíveis são: 1D: $\frac{\partial u}{\partial x}=0$; 2D: $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$; 3D: $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}$.

**Conceito cobrado:** Comparação entre 1D, 2D e 3D
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 16
**Resposta correta:** Discursiva

**Por que está correta:**
Fisicamente, a nulidade da variação em $x$ ($\frac{\partial u}{\partial x}=0$) significa que o que entra no volume de controle deve ser exatamente igual ao que sai, não havendo variação da velocidade entre a entrada e a saída.

**Conceito cobrado:** Caso 1D Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 17
**Resposta correta:** Discursiva

**Por que está correta:**
O sinal negativo aparece devido à orientação da normal da superfície: a normal da face de entrada aponta no sentido oposto ao da velocidade $u$.

**Conceito cobrado:** Caso 2D Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 18
**Resposta correta:** Discursiva

**Por que está correta:**
A equação reflete o balanço tridimensional: a variação do escoamento na direção $x$ é equilibrada pelas variações decorrentes nas direções $y$ e $z$.

**Conceito cobrado:** Caso 3D Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 19
**Resposta correta:** Discursiva

**Por que está correta:**
De acordo com a interpretação apresentada no capítulo, uma derivada positiva ($\frac{\partial u}{\partial x}>0$) indica massa saindo do volume de controle na direção $x$.

**Conceito cobrado:** Interpretação Física das Derivadas
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 20
**Resposta correta:** Discursiva

**Por que está correta:**
A conclusão está incorreta. O material ensina que a indicação de massa saindo está associada à variação espacial da velocidade ($\frac{\partial u}{\partial x} > 0$), e não apenas a uma velocidade ser positiva ($u = 5$ m/s), pois velocidade e variação espacial são grandezas diferentes.

**Conceito cobrado:** Interpretação Física das Derivadas / Observação Final
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 21
**Resposta correta:** Discursiva

**Por que está correta:**
O raciocínio do capítulo parte das "leis de conservação" físicas gerais, introduz a "massa específica" para relacionar ao volume, delimita um "volume de controle" fixo para analisar a conservação, equaciona o "balanço" entre entrada e saída, e quantifica as trocas pelo cálculo da "vazão mássica" através de suas faces.

**Conceito cobrado:** Resumo de Fechamento
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 22
**Resposta correta:** Discursiva

**Por que está correta:**
O material começa considerando o balanço num escoamento unidirecional (1D) apenas na direção $x$ (associado à velocidade $u$). Em seguida, incorpora a análise das demais direções do espaço, com a velocidade $v$ na direção $y$ e $w$ na direção $z$, chegando à formulação 3D do balanço.

**Conceito cobrado:** Generalização para 3D
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 23
**Resposta correta:** Discursiva

**Por que está correta:**
Quando o intervalo $\Delta\rightarrow 0$, as diferenças utilizadas no equacionamento inicial passam matematicamente a representar derivadas parciais, gerando assim a forma diferencial da conservação da massa.

**Conceito cobrado:** Forma Diferencial da Conservação da Massa
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 24
**Resposta correta:** Discursiva

**Por que está correta:**
A primeira equação é a notação vetorial compacta, empregando o operador de divergência $\nabla\cdot$. A segunda equação é a expansão dessa operação analiticamente em coordenadas cartesianas explícitas, somando as três derivadas espaciais e a derivada temporal.

**Conceito cobrado:** Forma Vetorial / Equação da Continuidade
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 25
**Resposta correta:** Discursiva

**Por que está correta:**
A "conservação da massa" é o princípio físico intrínseco. A "equação da continuidade" é a expressão matemática desta lei. Já a "incompressibilidade" é uma hipótese específica adotada que simplifica essa equação, considerando a massa específica constante para fluidos como água e ar.

**Conceito cobrado:** Equação da Continuidade / Caso Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 26
**Resposta correta:** Discursiva

**Por que está correta:**
Pela fórmula da vazão mássica $\dot m = \rho u A$, substituem-se os valores obtendo-se $\dot m = 1000 \times 3 \times 2 = 6000$ kg/s.

**Conceito cobrado:** Vazão Mássica
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 27
**Resposta correta:** Discursiva

**Por que está correta:**
Seguindo o princípio, a vazão de entrada é $\dot m_{in} = \rho_1 u_1 A_1 = 1000 \times 2 \times 3 = 6000$ kg/s.

**Conceito cobrado:** Vazão Mássica
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 28
**Resposta correta:** Discursiva

**Por que está correta:**
Substituindo em $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$, obtemos $-(4) = \frac{\partial v}{\partial y}$, logo $\frac{\partial v}{\partial y} = -4$ s$^{-1}$. Esse sinal indica a direção do fluxo necessário para manter o equilíbrio incompressível na região perante a variação verificada em $x$.

**Conceito cobrado:** Caso 2D Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 29
**Resposta correta:** Discursiva

**Por que está correta:**
Usando a relação incompressível 3D: $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$. Substituindo: $2 - 0,5 + \frac{\partial w}{\partial z} = 0 \implies 1,5 + \frac{\partial w}{\partial z} = 0 \implies \frac{\partial w}{\partial z} = -1,5$ s$^{-1}$.

**Conceito cobrado:** Caso 3D Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 30
**Resposta correta:** Discursiva

**Por que está correta:**
Para verificar a compatibilidade incompressível, a soma das derivadas deve ser nula: $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 3 + (-1) + (-2) = 0$. Logo, o fluxo é compatível com a conservação da massa incompressível.

**Conceito cobrado:** Caso Incompressível
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md
