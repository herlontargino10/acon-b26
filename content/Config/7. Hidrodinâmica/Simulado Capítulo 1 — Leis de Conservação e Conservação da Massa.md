Sim. Analisei o **Capítulo 1** anexado e ele tem conteúdo suficiente para montar uma prova completa sem precisar recorrer a nenhuma fonte externa. O próprio arquivo cobre desde as leis de conservação até a interpretação física da continuidade nos casos 1D, 2D e 3D. 001-006_Mecanica_dos_Fluidos_Ca…

Vou estruturar a prova **exclusivamente a partir deste `.md`**, preservando a lógica e a terminologia dele. 001-006_Mecanica_dos_Fluidos_Ca…

# Simulado — Mecânica dos Fluidos

## Capítulo 1 — Leis de Conservação e Conservação da Massa

**Instruções:** responda sem consultar o gabarito. Quando houver cálculo, apresente o raciocínio.

### Parte I — Conceitos fundamentais

**1.** Quais são as três propriedades fundamentais conservadas quando um fluido se move?

a) Massa, velocidade e pressão  
b) Massa, quantidade de movimento e energia  
c) Massa, volume e densidade  
d) Energia, pressão e temperatura

---

**2.** No contexto apresentado para a Hidrodinâmica do Navio, quais princípios de conservação são tipicamente empregados?

Explique também em que situação a conservação da energia passa a ser especialmente relevante segundo o material.

---

**3.** Diferencie:

- massa \(m\);
- massa específica \(\rho\);
- volume \(V\).

Apresente a relação matemática entre essas grandezas.

---

**4.** O que é um **volume de controle**?

Explique por que ele é considerado uma região fixa no espaço e o que acontece com o fluido em relação a essa região. 001-006_Mecanica_dos_Fluidos_Ca…

---

**5.** Explique o que significa dizer que a conservação da massa é uma **lei de conservação local**.

Não basta repetir a expressão "é local"; explique fisicamente a ideia.

---

### Parte II — Interpretação física

**6.** Considere um volume de controle no qual entra determinada quantidade de massa e sai uma quantidade maior.

O que necessariamente acontece com a massa armazenada dentro do volume de controle?

Explique o significado físico do sinal negativo que aparece no desenvolvimento da equação.

---

**7.** A expressão da vazão mássica é:

\[ \dot m=\rho uA \]

Explique fisicamente o significado de cada uma das três grandezas presentes no lado direito.

---

**8.** Um estudante afirma:

> "Para aplicar a conservação da massa, basta conhecer a velocidade do fluido."

Com base no capítulo, explique por que essa afirmação está incompleta ou incorreta.

---

**9.** No caso incompressível, o material chega à relação:

\[ \nabla\cdot\mathbf V=0 \]

O que essa relação significa fisicamente no contexto apresentado?

---

**10.** O material enfatiza que o importante não é simplesmente conhecer \(u\), \(v\) e \(w\), mas suas **variações espaciais**.

Explique essa diferença utilizando as grandezas:

\[ \frac{\partial u}{\partial x}, \qquad \frac{\partial v}{\partial y}, \qquad \frac{\partial w}{\partial z}. \]

Essa é uma questão particularmente importante porque o próprio capítulo termina destacando essa interpretação. 001-006_Mecanica_dos_Fluidos_Ca…

---

### Parte III — Equações e desenvolvimento

**11.** Escreva a forma diferencial geral da equação da continuidade.

---

**12.** Escreva a forma vetorial da conservação da massa apresentada no capítulo.

Identifique o significado de \(\mathbf V\).

---

**13.** Qual é a diferença entre a forma geral da continuidade e sua forma para um fluido incompressível?

Mostre matematicamente a simplificação apresentada no material. 001-006_Mecanica_dos_Fluidos_Ca…

---

**14.** Para um fluido incompressível, escreva a equação da continuidade em coordenadas cartesianas.

---

**15.** Relacione corretamente cada caso à sua equação:

|Caso|Equação|
|---|---|
|1D|?|
|2D|?|
|3D|?|

Utilize somente as relações apresentadas no capítulo.

---

### Parte IV — Aplicação e raciocínio

**16.** Um escoamento incompressível é considerado unidimensional.

O material estabelece:

\[ \frac{\partial u}{\partial x}=0 \]

Explique fisicamente o que isso significa para a entrada e a saída do volume de controle.

---

**17.** Em determinado caso 2D, o material apresenta:

\[ -\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \]

Por que aparece o sinal negativo associado à direção \(x\)?

A resposta deve considerar a **orientação da normal da superfície** e a direção da velocidade. 001-006_Mecanica_dos_Fluidos_Ca…

---

**18.** Em um caso 3D, a conservação da massa é expressa por:

\[ -\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \]

Explique, fisicamente, o que essa equação está dizendo sobre o balanço entre as diferentes direções.

---

**19.** Um volume de controle possui:

\[ \frac{\partial u}{\partial x}>0 \]

Segundo a interpretação apresentada no capítulo, o que isso representa?

---

**20.** Um estudante observa:

\[ u=5\;m/s \]

e conclui:

> "Como a velocidade é positiva, existe necessariamente massa saindo na direção \(x\)."

Essa conclusão está de acordo com a interpretação apresentada no capítulo? Justifique utilizando a diferença entre \(u\) e \(\partial u/\partial x\).

---

### Parte V — Questões integrativas

**21.** Reconstitua a sequência lógica utilizada no desenvolvimento da conservação da massa:

\[ \text{leis de conservação} \rightarrow ? \rightarrow ? \rightarrow ? \rightarrow ? \]

Utilize os conceitos apresentados no fechamento do capítulo. 001-006_Mecanica_dos_Fluidos_Ca…

---

**22.** Explique como o desenvolvimento parte de um caso **1D** e chega à formulação **3D**.

Sua resposta deve mencionar o papel de \(u\), \(v\) e \(w\).

---

**23.** Explique a passagem da expressão em diferenças para a forma diferencial da conservação da massa.

O que acontece quando:

\[ \Delta\rightarrow0? \]

---

**24.** Explique a relação entre:

\[ \nabla\cdot(\rho\mathbf V) + \frac{\partial\rho}{\partial t}=0 \]

e

\[ \frac{\partial(\rho u)}{\partial x} + \frac{\partial(\rho v)}{\partial y} + \frac{\partial(\rho w)}{\partial z} + \frac{\partial\rho}{\partial t}=0. \]

---

**25.** Explique a relação entre **conservação da massa**, **equação da continuidade** e **incompressibilidade**.

A resposta deve deixar claro que esses três termos não significam exatamente a mesma coisa.

---

## Parte VI — Questões numéricas

**26.** Um fluido possui massa específica:

\[ \rho=1000\;kg/m^3 \]

e atravessa uma área:

\[ A=2\;m^2 \]

com velocidade:

\[ u=3\;m/s. \]

Determine a vazão mássica utilizando a expressão apresentada no capítulo.

---

**27.** Uma seção de escoamento possui:

\[ \rho_1=1000\;kg/m^3, \qquad u_1=2\;m/s, \qquad A_1=3\;m^2. \]

Determine:

\[ \dot m_{in}. \]

---

**28.** Considere um escoamento incompressível 2D em que:

\[ \frac{\partial u}{\partial x}=4\;s^{-1}. \]

Utilizando:

\[ -\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \]

determine:

\[ \frac{\partial v}{\partial y}. \]

Interprete o sinal obtido.

---

**29.** Em um escoamento incompressível 3D:

\[ \frac{\partial u}{\partial x}=2\;s^{-1}, \qquad \frac{\partial v}{\partial y}=-0,5\;s^{-1}. \]

Determine:

\[ \frac{\partial w}{\partial z}. \]

Utilize a equação:

\[ \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}=0. \]

---

**30.** Um estudante recebe o seguinte conjunto de informações:

\[ \frac{\partial u}{\partial x}=3, \qquad \frac{\partial v}{\partial y}=-1, \qquad \frac{\partial w}{\partial z}=-2. \]

Determine se essas informações são compatíveis com a conservação da massa para um escoamento incompressível.

Justifique matematicamente.

---

# Gabarito resumido

1. **b**.
2. Massa e quantidade de movimento; energia para casos mais complicados em que a temperatura é geralmente importante. 001-006_Mecanica_dos_Fluidos_Ca…
3. \(m\) é massa, \(\rho\) é massa específica e \(V\) é volume; \(m=\rho V\).
4. Região fixa no espaço usada para análise; o fluido pode atravessá-la.
5. A massa não pode desaparecer de um ponto e aparecer em outro sem atravessar o espaço intermediário.
6. A massa interna diminui; daí o sinal negativo no desenvolvimento.
7. \(\rho\): massa específica; \(u\): velocidade; \(A\): área da face.
8. É necessário considerar a variação espacial das velocidades, além do balanço de massa.
9. As variações espaciais das componentes da velocidade se balanceiam.
10. A continuidade depende de derivadas espaciais, não simplesmente dos valores de \(u,v,w\).
11. \(\frac{\partial(\rho u)}{\partial x}+\frac{\partial(\rho v)}{\partial y}+\frac{\partial(\rho w)}{\partial z}+\frac{\partial\rho}{\partial t}=0\).
12. \(\nabla\cdot(\rho\mathbf V)+\frac{\partial\rho}{\partial t}=0\), com \(\mathbf V=(u,v,w)\).
13. No incompressível, \(\rho\) é constante e chega-se a \(\nabla\cdot\mathbf V=0\).
14. \(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=0\).
15. 1D: \(\partial u/\partial x=0\); 2D: \(-\partial u/\partial x=\partial v/\partial y\); 3D: \(-\partial u/\partial x=\partial v/\partial y+\partial w/\partial z\).
16. Não há variação de \(u\) em \(x\); o que entra deve sair.
17. Pela orientação da normal em relação à velocidade \(u\).
18. A variação em \(x\) é equilibrada pelas variações nas direções \(y\) e \(z\).
19. Segundo o material, representa massa saindo na direção \(x\).
20. Não. O capítulo relaciona essa interpretação a \(\partial u/\partial x\), não simplesmente ao valor de \(u\).
21. Leis de conservação → massa específica → volume de controle → balanço → vazão mássica.
22. Começa-se pela direção \(x\), depois são incorporadas as direções \(y\) e \(z\), representadas por \(v\) e \(w\).
23. As diferenças tendem a derivadas parciais quando \(\Delta\to0\).
24. A segunda é a expansão cartesiana da divergência da primeira.
25. Conservação da massa é a lei; continuidade é sua forma de expressão; incompressibilidade é uma hipótese que permite a simplificação para \(\nabla\cdot\mathbf V=0\).
26. \(\dot m=6000\;kg/s\).
27. \(\dot m=6000\;kg/s\).
28. \(-4\;s^{-1}\).
29. \(-1,5\;s^{-1}\).
30. Sim, pois \(3+(-1)+(-2)=0\).

### Observação sobre a estrutura

Eu **não colocaria questões sobre assuntos que não aparecem neste arquivo**, mesmo que sejam assuntos de Mecânica dos Fluidos que eu conheça. O capítulo fornece material suficiente para questões conceituais, interpretação de sinais, desenvolvimento matemático e aplicações numéricas simples. 001-006_Mecanica_dos_Fluidos_Ca…

Também há uma característica importante deste resumo: ele contém explicitamente uma seção **“Perguntas que o Professor Pode Fazer”**. Essas perguntas são uma excelente base para o estilo de cobrança conceitual, mas a prova acima não se limita a copiá-las; ela transforma parte delas em situações que exigem interpretação. 001-006_Mecanica_dos_Fluidos_Ca…