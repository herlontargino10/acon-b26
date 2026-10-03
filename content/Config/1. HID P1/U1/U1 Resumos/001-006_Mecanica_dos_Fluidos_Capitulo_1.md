---
title: "Mecânica dos Fluidos — Capítulo 1 — Leis de Conservação e Conservação da Massa"
chapter: 1
source_pdf: "1_Leis_de_conservação-001-006.pdf"
tags:
  - mecanica-dos-fluidos
  - leis-de-conservacao
  - conservacao-da-massa
  - equacao-da-continuidade
  - hidrodinamica
---

# Capítulo 1 — Leis de Conservação e Conservação da Massa

> [!info] Fonte e escopo
> Este capítulo foi revisado com base exclusivamente no PDF **`1_Leis_de_conservação-001-006.pdf`**, páginas 1–6. Cada PDF dividido pelo professor corresponde a um capítulo; portanto, o conteúdo deste arquivo pertence a este capítulo. Não foram antecipados conteúdos do PDF seguinte.

# 1. Leis de Conservação

O material apresenta três propriedades fundamentais conservadas quando um fluido se move:

1. **Conservação da massa**
2. **Conservação da quantidade de movimento**
3. **Conservação da energia**

Na Hidrodinâmica do Navio, o material afirma que tipicamente são empregados os princípios de conservação da massa e da quantidade de movimento. A conservação de energia é indicada para casos mais complicados, nos quais a **temperatura** é geralmente uma variável importante. O PDF remete esse assunto a outra nota de aula relacionada à geração de força em propulsores marítimos.

| Lei | Ideia apresentada |
|---|---|
| Massa | A massa não pode ser criada ou desaparecer |
| Quantidade de movimento | Relacionada à lei fundamental da dinâmica de Newton |
| Energia | Assim como a massa, não pode ser criada ou desaparecer |

> [!important] Foco deste capítulo
> O desenvolvimento matemático das páginas 1–6 começa pela **conservação da massa**.

# 2. Massa e Massa Específica

O material relaciona a massa \(m\) de um fluido ao volume por meio da densidade absoluta ou massa específica \(\rho\):

$$
m=\rho\,\Delta x\,\Delta y\,\Delta z
$$

Assim, para o pequeno elemento:

$$
V=\Delta x\,\Delta y\,\Delta z
$$

e:

$$
m=\rho V
$$

A massa específica é a grandeza que relaciona massa e volume.

> [!tip] Interpretação simples
> Massa é a quantidade total considerada; massa específica relaciona essa massa ao volume considerado.

# 3. Volume de Controle

A conservação da massa é aplicada a um **volume fixo no espaço**, de forma arbitrária, que contém fluido. Esse volume é chamado de **volume de controle**. O fluido pode entrar ou sair dele.

Inicialmente o material considera um escoamento **unidirecional (1D)**, na direção \(x\), usando um cubo como volume de controle.

Suas dimensões são:

$$
\Delta x,\quad\Delta y,\quad\Delta z
$$

e as velocidades de entrada e saída são:

$$
u_1,\quad u_2
$$

> [!important] O que entender
> O cubo é uma região de análise fixa. O fluido atravessa suas superfícies.

# 4. Balanço Inicial de Massa

O material apresenta inicialmente:

$$
\dot m_{out}-\dot m_{in}=\dot m_{cubo}
$$

e explica que uma diferença entre a quantidade de massa que entra e a quantidade que sai produz variação de massa no interior do volume.

> [!warning] Atenção ao sinal
> Nas etapas seguintes o material introduz explicitamente um sinal negativo para representar a situação física em que existe mais massa saindo do que entrando: nesse caso, a massa interna diminui.

# 5. Vazão Mássica

A vazão mássica é definida como a taxa de quantidade de fluido por unidade de tempo que passa por uma face da superfície de controle.

$$
\boxed{\dot m=\rho uA}
$$

Para a face do cubo:

$$
A=\Delta y\,\Delta z
$$

e o material relaciona:

$$
u=\frac{\Delta x}{\Delta t}
$$

As vazões de saída e entrada são:

$$
\boxed{\dot m_{out}=\rho_2u_2A_2}
$$

$$
\boxed{\dot m_{in}=\rho_1u_1A_1}
$$



> [!important] Memorizar
> A expressão fundamental apresentada nesta etapa é:
>
> $$
> \boxed{\dot m=\rho uA}
> $$

# 6. Variação da Massa no Cubo

Como o cubo tem dimensões fixas, o material escreve:

$$
\dot m_{cubo}
=
\frac{\Delta m}{\Delta t}
=
\frac{\Delta\rho}{\Delta t}\,
\Delta x\,\Delta y\,\Delta z
$$



# 7. Conservação Local da Massa

O material destaca que a conservação da massa é uma **lei de conservação local**.

Além da massa total ser conservada, uma quantidade de massa não pode simplesmente ir de um ponto A para um ponto B sem passar pelo espaço entre esses pontos. Portanto, é possível relacionar a variação de massa de uma região ao fluxo total de massa para fora dela.

> [!important] Ideia central
> A conservação da massa pode ser analisada localmente em um pequeno volume de controle.

# 8. Conservação da Massa — Caso 1D

O material substitui as vazões no balanço e obtém:

$$
\boxed{
\rho_2u_2A_2-\rho_1u_1A_1
=
-\frac{\Delta\rho}{\Delta t}
\Delta x\,\Delta y\,\Delta z
}
$$

O sinal negativo é explicado fisicamente: se há mais massa saindo do que entrando, a massa dentro do cubo deve diminuir.

Como:

$$
A_2=A_1=\Delta y\,\Delta z
$$

tem-se:

$$
(\rho_2u_2-\rho_1u_1)\Delta y\,\Delta z
=
-\frac{\Delta\rho}{\Delta t}
\Delta x\,\Delta y\,\Delta z
$$

O material passa então a trabalhar com a variação. Nesse ponto, o PDF observa que, em cálculo, há interesse particular na **variação de uma quantidade**, e não necessariamente apenas no seu valor.

$$
(\rho_2u_2-\rho_1u_1)=-\Delta(\rho u)
$$

resultando em:

$$
\boxed{
\Delta(\rho u)\Delta y\,\Delta z
=
-\frac{\Delta\rho}{\Delta t}
\Delta x\,\Delta y\,\Delta z
}
$$



> [!warning] Pegadinha
> **Mais saída que entrada → massa interna diminui.** O sinal negativo deve ser interpretado fisicamente, não apenas decorado.

# 9. Generalização para 3D

Para o caso 3D, o material soma as variações nas outras faces:

$$
\boxed{
\Delta(\rho u)\Delta y\,\Delta z
+
\Delta(\rho v)\Delta x\,\Delta z
+
\Delta(\rho w)\Delta x\,\Delta y
=
-\frac{\Delta\rho}{\Delta t}
\Delta x\,\Delta y\,\Delta z
}
$$

onde:

- \(u\) = velocidade na direção \(x\);
- \(v\) = velocidade na direção \(y\);
- \(w\) = velocidade na direção \(z\).



Dividindo pelo volume:

$$
\Delta x\,\Delta y\,\Delta z
$$

obtém-se:

$$
\frac{\Delta(\rho u)}{\Delta x}
+
\frac{\Delta(\rho v)}{\Delta y}
+
\frac{\Delta(\rho w)}{\Delta z}
=
-\frac{\Delta\rho}{\Delta t}
$$



# 10. Forma Diferencial da Conservação da Massa

Fazendo:

$$
\Delta\rightarrow0
$$

e usando:

$$
\frac{\Delta(\cdot)}{\Delta(\cdot)}
\rightarrow
\frac{\partial(\cdot)}{\partial(\cdot)}
$$

o material obtém:

$$
\boxed{
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
=
-\frac{\partial\rho}{\partial t}
}
$$

ou:

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



# 11. Forma Vetorial

O PDF apresenta graficamente a forma compacta como:

$$
\nabla(\rho\mathbf V)+\frac{\partial\rho}{\partial t}=0
$$

A expansão das três derivadas espaciais apresentada imediatamente antes indica a operação de divergência. Por isso, a mesma relação pode ser escrita explicitamente como:

e define \(\mathbf V\) como o vetor velocidade com componentes \(u,v,w\).

> [!note] Notação do PDF
> O PDF mostra graficamente \(\nabla(\rho V)\). Como a expressão corresponde às três derivadas espaciais apresentadas imediatamente antes, neste material a operação é explicitada como divergência:
>
> $$
> \boxed{
>\nabla\cdot(\rho\mathbf V)+\frac{\partial\rho}{\partial t}=0
> }
> $$
>
> Essa observação apenas torna explícita a operação indicada pelo desenvolvimento do próprio PDF.

Em coordenadas cartesianas:

$$
\nabla=
\left(
\frac{\partial}{\partial x},
\frac{\partial}{\partial y},
\frac{\partial}{\partial z}

\right)
$$

e:

$$
\mathbf V=(u,v,w)
$$

# 12. Forma Integral

O material apresenta:

$$
\boxed{
\iint \rho(\mathbf V\cdot\hat n)\,dA
=
-\frac{d}{dt}
\iiint\rho\,dVol
}
$$

onde \(\hat n\) é o vetor unitário ortogonal à face da área escolhida.

O material informa ainda que essa equação pode ser obtida pelo **princípio da divergência de Gauss**.

> [!important] Interpretação
> A forma integral relaciona o fluxo de massa através da superfície com a variação da massa dentro do volume.

# 13. Equação da Continuidade

O material afirma que a lei de conservação da massa também é conhecida como **equação da continuidade** e que ela se aplica a qualquer fluido.

Forma geral:

$$
\boxed{
\nabla\cdot(\rho\mathbf V)
+
\frac{\partial\rho}{\partial t}
=0
}
$$

ou:

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

# 14. Caso Incompressível

No contexto da Hidrodinâmica do Navio, o material trata água ou ar como **incompressíveis**, isto é, considera a densidade absoluta constante.

Assim:

$$
\boxed{\frac{\partial\rho}{\partial t}=0}
$$

e:

$$
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
=
\rho
\left(
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}

\right)
$$

Resultando em:

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

ou:

$$
\boxed{\nabla\cdot\mathbf V=0}
$$



> [!important] Fórmula essencial
> Para o caso incompressível apresentado:
>
> $$
> \boxed{\nabla\cdot\mathbf V=0}
> $$

# 15. Interpretação Física das Derivadas

O material observa que, no caso incompressível, a densidade não aparece nos termos finais da conservação da massa; a lei passa a ser expressa pelo balanceamento das derivadas espaciais das velocidades locais.

Quando:

$$
\frac{\partial u}{\partial x}>0
$$

o material interpreta como massa saindo na direção \(x\).

Analogamente:

$$
\frac{\partial v}{\partial y}>0
$$

indica massa saindo na direção \(y\), e:

$$
\frac{\partial w}{\partial z}>0
$$

indica massa saindo na direção \(z\).

> [!warning] Pegadinha
> O foco está nas **variações espaciais da velocidade**, não simplesmente no valor da velocidade.

# 16. Caso 1D Incompressível

No caso 1D apresentado:

$$
\boxed{\frac{\partial u}{\partial x}=0}
$$

O material interpreta isso como:

- o que entra no volume de controle deve ser exatamente o que sai;
- não pode existir variação de velocidade entre entrada e saída nesse caso.

# 17. Caso 2D Incompressível

No exemplo 2D:

- a entrada ocorre na direção \(x\);
- a saída em \(x\) é fechada;
- a saída ocorre por uma janela na direção \(y\).

O material destaca que a velocidade associada à direção \(x\) aparece com sinal negativo porque a normal da superfície aponta em sentido oposto ao da velocidade \(u\).

O balanço é:

$$
\boxed{
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
}
$$



> [!warning] Pegadinha de sinal
> O sinal deve ser relacionado à orientação da normal da superfície e à direção da velocidade. Não memorize o sinal isoladamente.

# 18. Caso 3D Incompressível

No exemplo 3D, a entrada ocorre na direção \(x\), enquanto existem saídas em \(y\) e \(z\).

O material apresenta:

$$
\boxed{
-\frac{\partial u}{\partial x}
=
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
}
$$



Equivalentemente:

$$
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
=0
$$

# 19. Comparação entre 1D, 2D e 3D

| Caso | Equação | Interpretação |
|---|---|---|
| 1D | \(\frac{\partial u}{\partial x}=0\) | A variação de \(u\) em \(x\) é nula |
| 2D | \(-\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}\) | A variação em \(x\) é equilibrada pela variação em \(y\) |
| 3D | \(-\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}\) | A variação em \(x\) é equilibrada pelas variações em \(y\) e \(z\) |

A forma geral que reúne os casos é:

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

# 20. Observação Final do Professor/Material

O material termina destacando:

> Nos três casos, para aplicar a lei de conservação da massa, são necessárias as **variações da velocidade no espaço**, e não a velocidade propriamente dita.

Portanto, o foco está em:

$$
\frac{\partial u}{\partial x},
\qquad
\frac{\partial v}{\partial y},
\qquad
\frac{\partial w}{\partial z}
$$

e não simplesmente em \(u,v,w\).

# 21. Perguntas que o Professor Pode Fazer

### "Quais são as três leis de conservação?"

**Resposta:** Conservação da massa, conservação da quantidade de movimento e conservação da energia.

### "Quais princípios são tipicamente empregados na Hidrodinâmica do Navio?"

**Resposta:** Conservação da massa e conservação da quantidade de movimento.

### "O que é massa específica?"

**Resposta:** É a densidade absoluta, representada por \(\rho\).

### "Qual é a relação entre massa, densidade e volume?"

$$
m=\rho V
$$

### "O que é um volume de controle?"

**Resposta:** Um volume fixo no espaço, de forma arbitrária, utilizado para analisar o fluido.

### "O que é vazão mássica?"

**Resposta:** É a taxa de quantidade de fluido por unidade de tempo que passa por uma face.

### "Qual é a fórmula da vazão mássica?"

$$
\dot m=\rho uA
$$

### "Por que aparece o sinal negativo no desenvolvimento da conservação de massa?"

**Resposta:** Porque, se houver mais massa saindo do que entrando, a massa dentro do cubo deve diminuir.

### "Quais são as componentes do vetor velocidade?"

**Resposta:** \(u\), \(v\) e \(w\), nas direções \(x\), \(y\) e \(z\).

### "Como é chamada também a conservação da massa?"

**Resposta:** Equação da continuidade.

### "Qual é a forma diferencial da continuidade?"

$$
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
+
\frac{\partial\rho}{\partial t}=0
$$

### "O que acontece no caso incompressível?"

**Resposta:** A densidade é tratada como constante e a equação reduz-se a:

$$
\nabla\cdot\mathbf V=0
$$

### "O que significa \(\partial u/\partial x>0\)?"

**Resposta:** Segundo a interpretação apresentada no material, existe massa saindo na direção \(x\).

### "Qual é a diferença entre os casos 1D, 2D e 3D?"

**Resposta:** No 1D participa apenas a variação de \(u\) em \(x\); no 2D participam as variações em \(x\) e \(y\); no 3D participam as variações em \(x\), \(y\) e \(z\).

# 22. Pegadinhas e Pontos de Atenção

> [!warning] Massa × massa específica
> \(m\) é massa; \(\rho\) é massa específica.

> [!warning] Massa × vazão mássica
> \(m\) é massa; \(\dot m\) é taxa de massa por unidade de tempo.

> [!warning] Volume de controle × fluido
> O volume de controle é a região fixa utilizada para análise; o fluido atravessa suas superfícies.

> [!warning] Saída − entrada e sinal
> O material inicialmente apresenta a diferença entre saída e entrada e, no desenvolvimento, introduz o sinal negativo para representar a redução da massa interna quando a saída supera a entrada.

> [!warning] Velocidade × variação da velocidade
> \(u\) é uma componente da velocidade; \(\partial u/\partial x\) é sua variação espacial.

> [!warning] Continuidade geral × incompressível
> A forma geral contém \(\rho\) e \(\partial\rho/\partial t\); a forma \(\nabla\cdot V=0\) é a forma simplificada para o caso incompressível tratado.

> [!warning] Sinal no caso 2D
> O material relaciona o sinal à orientação da normal da superfície em relação à velocidade.

# 23. Fórmulas Essenciais

### Massa

$$
\boxed{m=\rho V}
$$

### Massa no elemento

$$
\boxed{m=\rho\,\Delta x\,\Delta y\,\Delta z}
$$

### Vazão mássica

$$
\boxed{\dot m=\rho uA}
$$

### Saída

$$
\boxed{\dot m_{out}=\rho_2u_2A_2}
$$

### Entrada

$$
\boxed{\dot m_{in}=\rho_1u_1A_1}
$$

### Continuidade — forma diferencial

$$
\boxed{
\frac{\partial(\rho u)}{\partial x}
+
\frac{\partial(\rho v)}{\partial y}
+
\frac{\partial(\rho w)}{\partial z}
+
\frac{\partial\rho}{\partial t}=0
}
$$

### Continuidade — forma vetorial

$$
\boxed{
\nabla\cdot(\rho\mathbf V)+\frac{\partial\rho}{\partial t}=0
}
$$

### Continuidade — incompressível

$$
\boxed{\nabla\cdot\mathbf V=0}
$$

### Continuidade cartesiana — incompressível

$$
\boxed{
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}=0
}
$$

# 24. Resumo Ultra-Rápido

- Três leis: **massa, quantidade de movimento e energia**.
- Na Hidrodinâmica do Navio, o material destaca massa e quantidade de movimento.
- Massa específica: \(\rho\).
- Massa:
  $$
  m=\rho V
  $$
- Volume de controle: volume fixo usado para analisar o fluido.
- Vazão mássica:
  $$
  \dot m=\rho uA
  $$
- A conservação da massa é uma lei **local**.
- O caso 1D é generalizado para 3D usando \(u,v,w\).
- Forma diferencial:
  $$
  \frac{\partial(\rho u)}{\partial x}
  +
  \frac{\partial(\rho v)}{\partial y}
  +
  \frac{\partial(\rho w)}{\partial z}
  +
  \frac{\partial\rho}{\partial t}=0
  $$
- Conservação da massa = equação da continuidade.
- Para o caso incompressível:
  $$
\nabla\cdot\mathbf V=0
  $$
- Em coordenadas cartesianas:
  $$
  \frac{\partial u}{\partial x}
  +
  \frac{\partial v}{\partial y}
  +
  \frac{\partial w}{\partial z}=0
  $$
- O material destaca as **variações espaciais da velocidade**, e não simplesmente os valores das velocidades.
# 26. Pontos Confusos ou Incompletos

> [!tip] Explicação do professor (Teletransportação)
> A justificativa para a "conservação local" ganhou cor pela expressão figurada de que a "quantidade de massa não pode ir de A para B sem atravessar o espaço intermediário" (não pode sumir nem teletransportar).
> **Fonte:** Transcrição das aulas.

## 26.1 Balanço inicial e convenção de sinais

O PDF apresenta inicialmente:

$$
\dot m_{out}-\dot m_{in}=\dot m_{cubo}
$$

e depois, ao desenvolver a expressão, introduz:

$$
\rho_2u_2A_2-\rho_1u_1A_1
=
-\frac{\Delta\rho}{\Delta t}
\Delta x\,\Delta y\,\Delta z
$$

O próprio PDF explica que o sinal negativo representa a diminuição da massa interna quando há mais massa saindo que entrando.

## 26.2 Notação de \(\nabla\)

O PDF mostra \(\nabla(\rho V)\). Neste capítulo, a operação é explicitada como divergência:

$$
\nabla\cdot(\rho\mathbf V)
$$

porque o desenvolvimento imediatamente anterior é a soma das três derivadas espaciais.

## 26.3 Incompressibilidade

A afirmação de que água ou ar serão tratados como incompressíveis é apresentada como **hipótese do material** para o contexto da Hidrodinâmica do Navio. Não foram acrescentadas condições externas a essa afirmação.

# 28. Flashcards para Anki

## Essenciais

| Frente | Verso |
|---|---|
| Quais são as três leis de conservação apresentadas? | Conservação da massa; conservação da quantidade de movimento; conservação da energia. |
| Quais princípios são tipicamente empregados na Hidrodinâmica do Navio? | Conservação da massa e conservação da quantidade de movimento. |
| O que é massa específica? | Densidade absoluta do fluido, representada por \(\rho\). |
| Qual é a relação entre massa, massa específica e volume? | \(m=\rho V\). |
| O que é um volume de controle? | Um volume fixo no espaço usado para analisar o fluido. |
| O que é vazão mássica? | Taxa de quantidade de fluido por unidade de tempo que passa por uma face. |
| Qual é a expressão da vazão mássica? | \(\dot m=\rho uA\). |
| Quais são as componentes do vetor velocidade? | \(u\) em \(x\), \(v\) em \(y\) e \(w\) em \(z\). |
| Como também é chamada a conservação da massa? | Equação da continuidade. |
| Qual é a forma diferencial da continuidade? | \(\frac{\partial(\rho u)}{\partial x}+\frac{\partial(\rho v)}{\partial y}+\frac{\partial(\rho w)}{\partial z}+\frac{\partial\rho}{\partial t}=0\). |
| Qual é a forma da continuidade para o caso incompressível? | \(\nabla\cdot\mathbf V=0\). |
| Qual é a forma cartesiana da continuidade incompressível? | \(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=0\). |
| O que significa \(\partial u/\partial x>0\) segundo o material? | Existe massa saindo na direção \(x\). |
| O que é necessário conhecer para aplicar a conservação de massa nos três casos? | As variações da velocidade no espaço. |

## Importantes

| Frente | Verso |
|---|---|
| Como é expressa a vazão de saída? | \(\dot m_{out}=\rho_2u_2A_2\). |
| Como é expressa a vazão de entrada? | \(\dot m_{in}=\rho_1u_1A_1\). |
| Qual é a área da face considerada? | \(A=\Delta y\Delta z\). |
| Como o material relaciona \(u\), \(\Delta x\) e \(\Delta t\)? | \(u=\Delta x/\Delta t\). |
| O que significa conservação local da massa? | A massa não pode desaparecer em um ponto e aparecer em outro sem passar pelo espaço entre eles. |
| Por que aparece o sinal negativo no desenvolvimento? | Porque mais massa saindo que entrando implica diminuição da massa interna. |
| O que representa \(\hat n\)? | O vetor unitário normal à face da área escolhida. |
| O que ocorre com \(\rho\) no caso incompressível tratado? | É considerada constante e \(\partial\rho/\partial t=0\). |
| Qual é a equação do caso 1D incompressível? | \(\partial u/\partial x=0\). |
| Qual é a equação do caso 2D apresentado? | \(-\partial u/\partial x=\partial v/\partial y\). |
| Qual é a equação do caso 3D apresentado? | \(-\partial u/\partial x=\partial v/\partial y+\partial w/\partial z\). |

## Aplicação e interpretação

| Frente | Verso |
|---|---|
| Se entra mais massa do que sai, o que acontece à massa interna? | A massa interna aumenta. |
| Se sai mais massa do que entra, o que acontece à massa interna? | A massa interna diminui. |
| Se entrada e saída são iguais, o que ocorre? | Não há acúmulo de massa. |
| No caso 2D, por que aparece um sinal negativo associado à direção \(x\)? | Porque a normal da superfície aponta em sentido oposto ao da velocidade \(u\). |
| O que \(\nabla\cdot\mathbf V=0\) representa no contexto do material? | O balanceamento das variações espaciais das componentes da velocidade no escoamento incompressível. |

# 29. Resumo de Fechamento

O desenvolvimento das páginas 1–6 segue esta sequência:

$$
\boxed{
	ext{Leis de conservação}
\rightarrow
	ext{massa específica}
\rightarrow
	ext{volume de controle}
\rightarrow
	ext{balanço}
\rightarrow
	ext{vazão mássica}
}
$$

depois:

$$
\boxed{
	ext{1D}
\rightarrow
	ext{3D}
\rightarrow
	ext{forma diferencial}
\rightarrow
	ext{forma vetorial}
\rightarrow
	ext{forma integral}
}
$$

e finalmente:

$$
\boxed{
	ext{continuidade}
\rightarrow
	ext{incompressibilidade}
\rightarrow
	ext{casos 1D/2D/3D}
\rightarrow
	ext{interpretação física}
}
$$

Este capítulo, portanto, **não termina na introdução ao volume de controle**: ele inclui todo o desenvolvimento da conservação da massa e da equação da continuidade apresentado no PDF `001–006`.


---

# Auditoria de fidelidade — PDF 001–006

> [!success] Status
> Esta versão foi revisada após a auditoria do conteúdo e da formatação contra o PDF **001–006**.

### Correções realizadas

- Corrigidas as ocorrências quebradas de `\right)` no LaTeX.
- Mantidas as fórmulas em blocos matemáticos compatíveis com Obsidian.
- Recuperada a observação do PDF sobre a conservação da energia e a temperatura.
- Recuperada a observação do PDF sobre o interesse na variação de uma quantidade.
- Explicitado que, no caso 2D apresentado, a velocidade de saída em \(y\) é positiva.
- Mantida a distinção entre a notação compacta mostrada no PDF e a forma explícita com divergência.
- Não foram acrescentados conteúdos técnicos externos ao desenvolvimento das páginas 1–6.
