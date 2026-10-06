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

- massa \(m\);
- massa específica \(\rho\);
- volume \(V\).

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
O material enfatiza que o importante não é simplesmente conhecer \(u\), \(v\) e \(w\), mas suas **variações espaciais**.

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

Identifique o significado de \(\mathbf V\).

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

Por que aparece o sinal negativo associado à direção \(x\)?

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

> "Como a velocidade é positiva, existe necessariamente massa saindo na direção \(x\)."

Essa conclusão está de acordo com a interpretação apresentada no capítulo?

Justifique utilizando a diferença entre \(u\) e \(\partial u/\partial x\).

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

Sua resposta deve mencionar o papel de \(u\), \(v\) e \(w\).

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

- \(m\) = massa;
- \(\rho\) = massa específica;
- \(V\) = volume.

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

- \(\rho\) = massa específica;
- \(u\) = velocidade;
- \(A\) = área da face.

## 8

A afirmação está incompleta porque o capítulo destaca que são necessárias as **variações espaciais das velocidades**, e não simplesmente os valores de \(u\), \(v\) e \(w\).

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

e não simplesmente nos valores de \(u\), \(v\) e \(w\).

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

Isso significa que não há variação de \(u\) ao longo de \(x\). O que entra no volume de controle deve ser exatamente o que sai.

## 17

O sinal negativo está relacionado à **orientação da normal da superfície** em relação à direção da velocidade \(u\).

## 18

A variação na direção \(x\) é equilibrada pelas variações nas direções \(y\) e \(z\).

## 19

Segundo a interpretação apresentada no material:

$$
\frac{\partial u}{\partial x}>0
$$

indica massa saindo na direção \(x\).

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

O desenvolvimento começa considerando um escoamento 1D na direção \(x\), representado por \(u\).

Depois são incorporadas as demais direções:

- \(v\) na direção \(y\);
- \(w\) na direção \(z\).

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
