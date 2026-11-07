# Resumo Completo de Preparação para a Prova de Hidrodinâmica I (P1)

> **Documento de Estudo para Prova Discursiva e Teórica — Versão Auditada e Revisada**  
> **Roteiro Estruturador:** `Questionário P1.pdf` (40 Perguntas e Respostas Oficiais)  
> **Fontes Consultadas e Auditadas:** Apostilas Teóricas da Unidade 1 (`1_Leis_de_conservação-001-006.pdf` a `031-034.pdf`), Apostila Teórica da Unidade 2 (`2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf` do Prof. Edson Mesquita), Exercício Resolvido (`Resolução Q.5 - Passo 6.md`), Banco Conceitual (`44_QUESTÕES_P1_SEM_CÁLCULO.json`) e Transcrições de Aula (`Hid260807_080417`, `HidVoz 260728_102746`, `HidVoz 260814_091758`, etc.).

---

# Bloco 1: Cinemática Euleriana, Regime Permanente e Aceleração Convectiva

---

## 1.1. Definição Formal de Regime Permanente na Perspectiva Euleriana
*Relação com o Questionário: Pergunta 1*

### Definição e Explicação Conceitual Completa
Na cinemática dos fluidos sob a ótica Euleriana, o observador fixa sua atenção em coordenadas espaciais estáticas $(x, y, z)$ no interior do volume de controle, registrando a passagem sucessiva de diferentes partículas fluidas. 

Um escoamento é formalmente classificado em **regime permanente** (ou estacionário) quando **nenhuma propriedade do fluido em qualquer coordenada espacial fixa varia com o tempo**. Isso significa que a taxa de variação temporal local em uma janela de observação fixa é identicamente nula para todas as variáveis de estado e de escoamento: vetor velocidade, pressão, massa específica, temperatura e tensões cisalhantes.

### Hipóteses e Condições de Validade
- Referencial espacial estático (observador euleriano fixo);
- Derivada parcial temporal estritamente nula em todos os pontos do domínio;
- O escoamento pode ser espacialmente uniforme ou não uniforme, compressível ou incompressível, laminar ou turbulento em termos de médias temporais.

### Equações Fundamentais
A condição vetorial e matemática exata que governa o regime permanente é:

$$\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$$

Em coordenadas cartesianas tridimensionais, desmembra-se nas três componentes escalares de velocidade $\mathbf{V} = (u, v, w)$:

$$\frac{\partial u}{\partial t} = 0, \quad \frac{\partial v}{\partial t} = 0, \quad \frac{\partial w}{\partial t} = 0$$

Para os demais campos escalares:

$$\frac{\partial \rho}{\partial t} = 0, \quad \frac{\partial p}{\partial t} = 0$$

### Significado Físico das Variáveis
- $\mathbf{V}(x, y, z)$: Vetor velocidade no ponto fixo $(x, y, z)$ ($[L T^{-1}]$);
- $t$: Variável temporal independente ($[T]$);
- $\frac{\partial}{\partial t}$: Operador de derivada parcial temporal local (avaliada mantendo $(x, y, z)$ constantes);
- $\rho$: Massa específica local do fluido ($[M L^{-3}]$);
- $p$: Campo de pressão hidrodinâmica local ($[M L^{-1} T^{-2}]$).

### Interpretação Física e de Sinais
Dizer que $\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$ não significa que as partículas fluidas não sofrem aceleração. Significa unicamente que uma sonda ou sensor instalado permanentemente no ponto $(x_0, y_0, z_0)$ medirá uma velocidade invariável a cada segundo. Se uma partícula fluida se deslocar de $(x_0, y_0, z_0)$ para outro ponto $(x_1, y_1, z_1)$ onde o campo de velocidades é mais veloz, essa partícula sofrerá aceleração física ao longo de sua trajetória, apesar de o escoamento ser estritamente permanente em cada ponto fixo.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Sob o ponto de vista matemático e de campo vetorial, um escoamento em regime permanente caracteriza-se pelo fato de que as propriedades do fluido (vetor velocidade, pressão, massa específica) em qualquer coordenada fixa $(x, y, z)$ não variam com o tempo. A derivada temporal local é identicamente nula: $\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$, $\frac{\partial p}{\partial t} = 0$ e $\frac{\partial \rho}{\partial t} = 0$. Isso implica que o campo de velocidades é função exclusiva das coordenadas espaciais, isto é, $\mathbf{V} = \mathbf{V}(x, y, z)$."

### Erros Clássicos de Interpretação
- **Erro de prova:** Afirmar que "regime permanente" significa que a partícula fluida não acelera ou que a velocidade da partícula é constante. Isso confunde a derivada local $\frac{\partial \mathbf{V}}{\partial t}$ com a derivada substantiva $\frac{D\mathbf{V}}{Dt}$.
- **Erro de prova:** Confundir regime permanente ($\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$) com escoamento uniforme ($\frac{\partial \mathbf{V}}{\partial s} = \mathbf{0}$ ao longo do espaço).

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 8–10; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 5; Questionário P1, Pergunta 1.

---

## 1.2. Aceleração Convectiva em Bocal Convergente com Fluxo Permanente
*Relação com o Questionário: Pergunta 2*

### Definição e Explicação Conceitual Completa
Considere um bocal convergente horizontal operando em fluxo permanente com vazão mássica constante. Embora a velocidade registrada em qualquer posição fixa do bocal não varie ao longo do tempo ($\frac{\partial u}{\partial t} = 0$), uma boia flutuante ou um elemento infinitesimal de fluido sofre aceleração real ao percorrer o duto em direção à garganta estrangulada.

Esse fenômeno é governado pela **aceleração convectiva**. A aceleração total experimentada por uma porção de matéria não depende apenas da variação temporal no ponto em que ela se encontra, mas também do fato de que a matéria se desloca no espaço através de regiões com intensidades de velocidade progressivamente distintas.

### Hipóteses e Condições de Validade
- Fluido incompressível ($\rho = \text{constante}$);
- Escoamento permanente ($\frac{\partial}{\partial t} = 0$);
- Escoamento predominantemente unidimensional ao longo do eixo longitudinal $x$;
- Paredes sólidas rígidas e convergentes ($A(x)$ decresce com $x$).

### Equações Fundamentais e Desenvolvimento Passo a Passo
1. Pela Lei de Conservação da Massa (Continuidade 1D) para fluido incompressível:

$$Q = u(x) A(x) = \text{constante}$$

$$u_1 A_1 = u_2 A_2 \implies u(x) = \frac{Q}{A(x)}$$

2. Como a seção transversal diminui ao longo de $x$ no bocal convergente:

$$\frac{dA}{dx} < 0 \implies \frac{\partial u}{\partial x} = -\frac{Q}{[A(x)]^2}\frac{dA}{dx} > 0$$

3. A aceleração substantiva total do elemento fluido na direção $x$ é dada pela Derivada Material:

$$a_x = \frac{Du}{Dt} = \underbrace{\frac{\partial u}{\partial t}}_{\text{aceleração local}} + \underbrace{u \frac{\partial u}{\partial x}}_{\text{aceleração convectiva}}$$

4. Aplicando a hipótese de regime permanente ($\frac{\partial u}{\partial t} = 0$):

$$\frac{Du}{Dt} = u \frac{\partial u}{\partial x}$$

Como a velocidade $u > 0$ e o gradiente espacial de velocidade é estritamente positivo ($\frac{\partial u}{\partial x} > 0$), o produto convectivo resulta positivo e não nulo:

$$\frac{Du}{Dt} = u \frac{\partial u}{\partial x} > 0$$

### Significado Físico das Variáveis
- $u(x)$: Componente longitudinal da velocidade do fluido no ponto $x$ ($[L T^{-1}]$);
- $\frac{\partial u}{\partial x}$: Gradiente espacial longitudinal de velocidade (taxa com que a velocidade cresce ao avançar em $x$, unidade $[T^{-1}]$);
- $u \frac{\partial u}{\partial x}$: Parcela inercial convectiva (aceleração provocada pelo transporte espacial da partícula, unidade $[L T^{-2}]$);
- $A(x)$: Área da seção transversal do bocal no ponto $x$ ($[L^2]$).

### Interpretação Física e de Sinais
O sinal positivo de $\frac{\partial u}{\partial x}$ traduz o estrangulamento das linhas de corrente: para transferir o mesmo volume de água incompressível por uma fresta transversal menor por unidade de tempo, as partículas fluidas precisam aumentar sua velocidade de translação. Conforme a boia viaja no sentido positivo de $x$, ela penetra continuamente em seções com linhas de corrente mais densas e campos de velocidade mais intensos, exigindo uma aceleração física real sustentada pela força de gradiente de pressão forçante.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A boia ou elemento fluido acelera ao passar pela garganta porque a aceleração total de uma partícula fluida na mecânica do contínuo depende também da aceleração convectiva. Conforme a partícula avança no espaço, ela penetra em seções de área reduzida onde o campo de velocidade é mais intenso ($\frac{\partial u}{\partial x} > 0$), gerando aceleração pela parcela $u \frac{\partial u}{\partial x} \neq 0$, mesmo sendo a aceleração local nula ($\frac{\partial u}{\partial t} = 0$)."

### Erros Clássicos de Interpretação
- Afirmar que a boia só aceleraria se a vazão de entrada da bomba estivesse variando no tempo ($\frac{\partial Q}{\partial t} \neq 0$).
- Esquecer de multiplicar o gradiente $\frac{\partial u}{\partial x}$ pela velocidade de transporte $u$, descaracterizando a dimensão de aceleração ($[L T^{-2}]$).

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 7–8; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 3; Questionário P1, Pergunta 2.

---

## 1.3. A Expressão Unidimensional da Derivada Material e a Inércia Convectiva
*Relação com o Questionário: Pergunta 3*

### Definição e Explicação Conceitual Completa
Na formulação Euleriana, a derivada temporal convencional de uma partícula em movimento não pode ser calculada por uma simples derivada parcial em relação ao tempo, pois as partículas mudam simultaneamente de tempo e de posição no espaço tridimensional. 

Para capturar a verdadeira taxa de variação temporal de qualquer propriedade que acompanha a trajetória de uma partícula fluida, emprega-se a **Derivada Material** (também denominada derivada substantiva ou derivada total). No caso unidimensional, ela desmembra a taxa de variação da velocidade longitudinal $u(x, t)$ em duas parcelas fundamentais: a **inércia temporal local** e a **inércia puramente espacial (convectiva)**.

### Dedução Passo a Passo via Regra da Cadeia
Considere a velocidade longitudinal $u$ de uma partícula fluida descrita como uma função de sua coordenada de posição $x$ e do tempo $t$, ou seja, $u = u(x(t), t)$.

Diferenciando $u$ em relação ao tempo $t$ através da regra da cadeia do cálculo diferencial:

$$\frac{du}{dt} = \frac{\partial u}{\partial t}\frac{dt}{dt} + \frac{\partial u}{\partial x}\frac{dx}{dt}$$

Como $\frac{dt}{dt} = 1$ e a taxa temporal de variação da posição da partícula material no espaço define a sua própria velocidade instantânea ($\frac{dx}{dt} = u$), obtém-se formalmente o operador da derivada material:

$$\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x}$$

### Significado Físico dos Termos
A equação expressa a aceleração total unidimensional da partícula fluida:

$$\underbrace{\frac{Du}{Dt}}_{\text{Aceleração Substantiva Total}} = \underbrace{\frac{\partial u}{\partial t}}_{\text{Aceleração Local}} + \underbrace{u \frac{\partial u}{\partial x}}_{\text{Aceleração / Inércia Convectiva}}$$

- **$\frac{Du}{Dt}$**: Aceleração total efetiva sentida pela partícula material individual (unidade: $\text{m/s}^2$ ou $[L T^{-2}]$);
- **$\frac{\partial u}{\partial t}$**: Parcela temporal local. Representa a taxa de variação da velocidade em uma coordenada espacial estritamente fixa;
- **$u \frac{\partial u}{\partial x}$**: **Termo puramente espacial ou inércia convectiva**. Representa a taxa de variação de velocidade associada ao transporte espacial da matéria através de um campo com gradiente não homogêneo ($\frac{\partial u}{\partial x}$).

### Interpretação Física e Dimensional
Ambos os termos do lado direito possuem rigorosamente a dimensão de aceleração:
- $[\frac{\partial u}{\partial t}] = \frac{[L T^{-1}]}{[T]} = [L T^{-2}]$
- $[u \frac{\partial u}{\partial x}] = [L T^{-1}] \cdot \frac{[L T^{-1}]}{[L]} = [L T^{-2}]$

O termo puramente espacial $u \frac{\partial u}{\partial x}$ reflete a inércia mecânica da massa fluida ao ser forçada a navegar por regiões com campos de pressão ou áreas de geometria variável.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A expressão unidimensional da derivada material da velocidade longitudinal $u(x, t)$ é:
> $$\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x}$$
> O termo que representa a inércia puramente espacial (inércia convectiva) é $u \frac{\partial u}{\partial x}$."

### Erros Clássicos de Interpretação
- Apontar apenas o gradiente espacial $\frac{\partial u}{\partial x}$ como o termo de inércia. Sem o produto pela velocidade $u$, a grandeza é um gradiente cinemático ($[T^{-1}]$), não uma aceleração de inércia ($[L T^{-2}]$).
- Omitir o operador substantivo maiúsculo ($\frac{D}{Dt}$), confundindo a derivada material com a derivada parcial estática ($\frac{\partial}{\partial t}$).

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 8–10; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 2; Questionário P1, Pergunta 3.

---

## 1.4. Comportamento da Aceleração Convectiva em Duto Divergente Permanente
*Relação com o Questionário: Pergunta 4*

### Definição e Explicação Conceitual Completa
Em um conduto divergente, a seção de passagem do fluido expande-se gradativamente ao longo da direção do escoamento ($x$). Em regime permanente e com vazão mássica invariável, a conservação da massa dita que a velocidade média do fluido diminui à medida que a área aumenta.

A aceleração convectiva reflete essa desaceleração de maneira direta e elegante: o gradiente espacial longitudinal assume valor negativo ($\frac{\partial u}{\partial x} < 0$), resultando em um produto convectivo negativo que descreve matematicamente a frenagem da partícula fluida.

### Desenvolvimento Matemático e Análise de Sinais
1. Relação de área em duto divergente:

$$\frac{dA}{dx} > 0$$

2. Pela continuidade incompressível ($Q = u A = \text{constante}$):

$$\frac{\partial u}{\partial x} = -\frac{Q}{A^2}\frac{dA}{dx} < 0$$

3. Como o fluido está escoando para a frente (sentido positivo do eixo $x$), a velocidade é positiva:

$$u > 0$$

4. Calculando o termo convectivo na derivada material:

$$a_{\text{conv}} = u \frac{\partial u}{\partial x} = (+)\cdot(-) < 0$$

Como $\frac{\partial u}{\partial t} = 0$, a aceleração material total é:

$$\frac{Du}{Dt} = u \frac{\partial u}{\partial x} < 0$$

### Interpretação Física
Um valor negativo para a derivada material ($\frac{Du}{Dt} < 0$) significa que o vetor aceleração aponta no sentido oposto ao vetor velocidade da partícula. Fisicamente, as forças normais de pressão à frente da partícula tornam-se maiores do que a pressão a montante (recuperação de pressão hidrodinâmica em difusores), aplicando uma força líquida contrária ao deslocamento e freando continuamente o elemento fluido ao migrar para a área expandida.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Como a velocidade $u$ é positiva e o gradiente espacial longitudinal é negativo ($\frac{\partial u}{\partial x} < 0$), o produto convectivo $u \frac{\partial u}{\partial x}$ torna-se negativo, indicando desaceleração física da partícula ao se deslocar para a área maior."

### Erros Clássicos de Interpretação
- Supor que desaceleração exige necessariamente regime não permanente com variação de bomba ($\frac{\partial u}{\partial t} < 0$).
- Inverter o sinal do gradiente, assumindo erroneamente que "área maior implica gradiente positivo de velocidade".

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 7–9; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 3; Questionário P1, Pergunta 4.

---

## 1.5. O Erro Clássico da Cinemática: Aceleração Local Nula versus Aceleração Material
*Relação com o Questionário: Pergunta 5*

### Análise Epistemológica e Mecânica do Equívoco
Um dos erros conceituais mais recorrentes cometidos em avaliações de hidrodinâmica consiste na afirmação ingênua de que: *"se o escoamento está em regime permanente, nenhuma partícula fluida pode sofrer alteração em sua velocidade ou aceleração, pois a velocidade é constante"*.

A raiz desse erro reside na **incapacidade de distinguir o referencial da janela de observação euleriana estática da trajetória dinâmica da partícula material**.

### A Analogia da Bola na Rampa de Newton
Para elucidar essa distinção, o material didático apresenta a analogia clássica de uma bola descendo uma rampa sob a ação constante da gravidade:
- **Sob a abordagem Lagrangeana:** O observador acompanha a bola com uma câmera móvel acoplada à sua trajetória. Registram-se sucessivas velocidades $u_1 < u_2 < u_3$ ao longo do tempo. Conclui-se imediatamente que $\frac{\partial u}{\partial t} \neq 0$, identificando com facilidade a aceleração $a = \frac{\Delta u}{\Delta t}$ produzida pela força gravitacional.
- **Sob a abordagem Euleriana:** O observador monta um portão fotográfico ou sensor fixo no meio da rampa. A cada vez que uma bola passa exatamente por aquela janela geométrica fixa, o instrumento mede rigorosamente a mesma velocidade $u_0$. Sob o ponto de vista exclusivo do instrumento estático, a derivada temporal é zero:

$$\left(\frac{\partial u}{\partial t}\right)_{\text{janela fixa}} = 0$$

Concluir que "não existe força gravitacional atuando na rampa" apenas porque o sensor fixo registrou derivada temporal nula é um equívoco primário. A aceleração e a força continuam atuando na matéria; elas apenas se manifestam na formulação euleriana através do gradiente espacial: a bola chega à janela com velocidade ligeiramente menor e sai dela com velocidade ligeiramente maior.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O erro consiste em confundir a derivada temporal local euleriana em um ponto fixo ($\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$) com a derivada substantiva da partícula individual em movimento ($\frac{D\mathbf{V}}{Dt}$), que inclui a mudança de posição no espaço através dos termos de aceleração convectiva."

### Erros Clássicos de Interpretação
- Afirmar que a Segunda Lei de Newton para fluidos pode ser escrita simplesmente como $\mathbf{F} = m \frac{\partial \mathbf{V}}{\partial t}$. Essa expressão só seria válida se o volume de matéria permanecesse estático no ponto de cálculo.
- Julgar que a abordagem euleriana elimina a inércia; na verdade, ela apenas transfere a inércia para termos não lineares de transporte espacial ($u \frac{\partial u}{\partial x}$, etc.).

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 8–10; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 4; Questionário P1, Pergunta 5.

---

# Bloco 2: Conservação de Massa e Equação da Continuidade

---

## 2.1. Equação Diferencial Geral da Conservação de Massa (3D Compressível)
*Relação com o Questionário: Pergunta 6*

### Definição e Princípio Físico
O princípio da conservação da massa estabelece que a massa de um sistema material não pode ser criada nem destruída. Aplicado a um volume de controle infinitesimal estático de formato cúbico no espaço, o princípio dita que:

$$\left[\begin{matrix} \text{Taxa líquida de influxo} \\ \text{de massa através das} \\ \text{fronteiras de controle} \end{matrix}\right] - \left[\begin{matrix} \text{Taxa líquida de efluxo} \\ \text{de massa através das} \\ \text{fronteiras de controle} \end{matrix}\right] = \left[\begin{matrix} \text{Taxa de acúmulo} \\ \text{temporal de massa no} \\ \text{interior do volume} \end{matrix}\right]$$

### Dedução Matemática Passo a Passo no Volume de Controle Cúbico
Considere um elemento diferencial ortogonal de dimensões $\Delta x, \Delta y, \Delta z$ centrado em coordenadas cartesianas.

1. **Taxa de acúmulo de massa no interior do volume:**  
A massa armazenada no volume infinitesimal é $m = \rho\,\Delta x\,\Delta y\,\Delta z$. Sua taxa de variação temporal é:

$$\frac{\partial m}{\partial t} = \frac{\partial \rho}{\partial t}\,\Delta x\,\Delta y\,\Delta z$$

2. **Fluxos de massa nas faces normais ao eixo $x$:**  
A face de entrada em $x$ possui área $A_x = \Delta y\,\Delta z$. O fluxo de massa entrante é $(\rho u)\,\Delta y\,\Delta z$.  
Na face oposta em $x + \Delta x$, o fluxo mássico efluente é expresso pela expansão em série de Taylor:

$$\left[ \rho u + \frac{\partial (\rho u)}{\partial x}\Delta x \right]\Delta y\,\Delta z$$

O saldo líquido de massa (Entrada $-$ Saída) na direção $x$ é:

$$\text{Saldo}_x = (\rho u)\Delta y\Delta z - \left[ \rho u + \frac{\partial (\rho u)}{\partial x}\Delta x \right]\Delta y\Delta z = -\frac{\partial (\rho u)}{\partial x}\,\Delta x\,\Delta y\,\Delta z$$

3. **Generalização tridimensional para os eixos $y$ e $z$:**  
Analogamente, para as faces perpendiculares aos eixos $y$ e $z$:

$$\text{Saldo}_y = -\frac{\partial (\rho v)}{\partial y}\,\Delta x\,\Delta y\,\Delta z$$

$$\text{Saldo}_z = -\frac{\partial (\rho w)}{\partial z}\,\Delta x\,\Delta y\,\Delta z$$

4. **Igualando o balanço total à taxa de acúmulo:**

$$-\left[ \frac{\partial (\rho u)}{\partial x} + \frac{\partial (\rho v)}{\partial y} + \frac{\partial (\rho w)}{\partial z} \right]\Delta x\,\Delta y\,\Delta z = \frac{\partial \rho}{\partial t}\,\Delta x\,\Delta y\,\Delta z$$

5. Dividindo toda a equação pelo volume diferencial $\Delta x\,\Delta y\,\Delta z$ e reorganizando os termos, obtém-se a **Equação da Continuidade na Forma Geral**:

$$\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x} + \frac{\partial (\rho v)}{\partial y} + \frac{\partial (\rho w)}{\partial z} = 0$$

### Forma Vetorial Compacta
Empregando o operador nabla ($\nabla = \frac{\partial}{\partial x}\hat{i} + \frac{\partial}{\partial y}\hat{j} + \frac{\partial}{\partial z}\hat{k}$) e o operador divergente:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$$

### Significado Físico das Variáveis
- $\rho$: Massa específica instantânea do fluido ($[M L^{-3}]$);
- $\mathbf{V} = u\hat{i} + v\hat{j} + w\hat{k}$: Vetor velocidade do fluido ($[L T^{-1}]$);
- $\rho \mathbf{V}$: Vetor densidade de fluxo de massa ($[M L^{-2} T^{-1}]$);
- $\nabla \cdot (\rho \mathbf{V})$: Taxa líquida de perda de massa por escoamento para fora do volume por unidade de volume;
- $\frac{\partial \rho}{\partial t}$: Taxa de variação temporal da densidade dentro do ponto fixo.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Apresenta-se a equação diferencial da conservação de massa na forma geral para escoamentos tridimensionais compressíveis como:
> $$\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x} + \frac{\partial (\rho v)}{\partial y} + \frac{\partial (\rho w)}{\partial z} = 0$$
> ou, na forma vetorial invariante:
> $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$$"

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, páginas 4–6; `001-006_Mecanica_dos_Fluidos_Capitulo_1.md`, Seções 8 e 9; Questionário P1, Pergunta 6.

---

## 2.2. Redução da Equação da Continuidade para Água Líquida ($\nabla \cdot \mathbf{V} = 0$)
*Relação com o Questionário: Pergunta 7*

### Razão Matemática e Dedução Formal
Na engenharia naval e na hidrodinâmica clássica, os escoamentos de água líquida em condutos fechados ou ao redor de cascos e apêndices operam sob velocidades muito inferiores à velocidade do som no meio aquoso (número de Mach $Ma \ll 0,3$). Nessas condições, a água é tratada fisicamente como um **fluido incompressível**.

A incompressibilidade impõe que a massa específica $\rho$ seja rigorosamente constante tanto no espaço quanto no tempo:

$$\rho = \text{constante} \implies \frac{\partial \rho}{\partial t} = 0, \quad \nabla \rho = \mathbf{0}$$

### Desenvolvimento Algébrico
1. Partindo da equação diferencial geral da continuidade vetorial:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$$

2. Expandindo o divergente do produto escalar-vetor $\nabla \cdot (\rho \mathbf{V}) = \rho (\nabla \cdot \mathbf{V}) + \mathbf{V} \cdot \nabla \rho$:

$$\frac{\partial \rho}{\partial t} + \mathbf{V} \cdot \nabla \rho + \rho (\nabla \cdot \mathbf{V}) = 0$$

Nota-se que os dois primeiros termos formam exatamente a derivada material da densidade: $\frac{D\rho}{Dt} + \rho (\nabla \cdot \mathbf{V}) = 0$.

3. Como a água possui densidade rigorosamente constante e uniforme:

$$\frac{\partial \rho}{\partial t} = 0 \quad \text{e} \quad \nabla \rho = \mathbf{0} \implies \frac{D\rho}{Dt} = 0$$

A equação reduz-se a:

$$\rho (\nabla \cdot \mathbf{V}) = 0$$

4. Sendo a densidade da água um valor físico não nulo ($\rho \approx 1000\,\text{kg/m}^3 \neq 0$), divide-se toda a expressão por $\rho$, obtendo-se a forma simplificada fundamental:

$$\nabla \cdot \mathbf{V} = 0$$

Em termos cartesianos escalares:

$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Porque a água é considerada um fluido incompressível, cuja massa específica é rigorosamente constante no tempo e no espaço ($\rho = \text{constante}$ e $\frac{\partial \rho}{\partial t} = 0$). A densidade sai das derivadas parciais e divide-se toda a equação por $\rho$, eliminando-a e resultando em $\nabla \cdot \mathbf{V} = 0$."

### Erros Clássicos de Interpretação
- Afirmar que a condição $\nabla \cdot \mathbf{V} = 0$ exige que o escoamento seja permanente. **Não exige!** A incompressibilidade é suficiente para garantir $\nabla \cdot \mathbf{V} = 0$, mesmo em regimes transientes e pulsáteis de líquidos.
- Confundir fluido incompressível ($\rho = \text{constante}$) com escoamento uniforme ($\mathbf{V} = \text{constante}$).

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, página 6; `001-006_Mecanica_dos_Fluidos_Capitulo_1.md`, Seção 9; Questionário P1, Pergunta 7.

---

## 2.3. Significado Físico da Condição de Divergente Nulo ($\nabla \cdot \mathbf{V} = 0$)
*Relação com o Questionário: Pergunta 8*

### Interpretação Cinemática e Geométrica do Volume Material
Matematicamente, o divergente de um campo vetorial de velocidades representa a **taxa de dilatação volumétrica por unidade de volume** de uma partícula fluida infinitesimal que acompanha o escoamento:

$$\nabla \cdot \mathbf{V} = \frac{1}{\delta V}\frac{D(\delta V)}{Dt}$$

onde $\delta V$ representa o volume material instantâneo do elemento fluido.

Portanto, a imposição formal de divergente nulo:

$$\nabla \cdot \mathbf{V} = 0 \iff \frac{D(\delta V)}{Dt} = 0 \implies \delta V(t) = \text{constante}$$

### Distinção Crucial entre Deformação e Variação Volumétrica
A condição de divergente nulo **não impede o elemento de sofrer intensas alterações geométricas**. Uma partícula fluida submetida a $\nabla \cdot \mathbf{V} = 0$ pode:
1. **Esticar-se ou estirar-se** em uma direção espacial (deformação linear ou taxa de extensão longitudinal);
2. **Cisalhar-se angularmente** (deformação angular provocada pelo atrito entre camadas);
3. **Rotacionar** sobre seu próprio eixo (vorticidade);

Contudo, **o seu volume material total permanece estritamente constante e invariável ao longo do tempo**. Qualquer estiramento sofrido em um eixo deve ser rigidamente compensado pelo achatamento/convergência proporcional nos outros eixos ortogonais.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Significa que a taxa de variação volumétrica por unidade de volume é nula; o elemento de fluido pode deformar-se, estirar-se ou rotacionar, mas seu volume permanece absolutamente constante."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, página 6; `001-006_Mecanica_dos_Fluidos_Capitulo_1.md`, Seção 9; Questionário P1, Pergunta 8.

---

## 2.4. Resolução Analítica em Canal Bidimensional: Determinação de $\partial v/\partial y$
*Relação com o Questionário: Pergunta 9*

### Configuração do Problema
Considere um canal bidimensional restrito ao plano $(x, y)$ preenchido por um fluido incompressível, cujo perfil de velocidade longitudinal varia linearmente ao longo do comprimento segundo a função:

$$u(x) = C_1 + C_2 x \quad (\text{com } C_2 > 0)$$

Deseja-se determinar a taxa de deformação vertical $\frac{\partial v}{\partial y}$ necessária e suficiente para assegurar a conservação integral da massa.

### Resolução Passo a Passo
1. Para escoamento bidimensional incompressível, a equação diferencial da continuidade simplifica-se para:

$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0$$

2. Deriva-se a componente de velocidade longitudinal $u(x)$ em relação à coordenada espacial $x$:

$$\frac{\partial u}{\partial x} = \frac{d}{dx}(C_1 + C_2 x) = C_2$$

3. Substitui-se o resultado na equação da continuidade bidimensional:

$$C_2 + \frac{\partial v}{\partial y} = 0$$

4. Isola-se algebricamente a derivada parcial transversal $\frac{\partial v}{\partial y}$:

$$\frac{\partial v}{\partial y} = -C_2$$

Como $C_2 > 0$, conclui-se de forma direta que:

$$\frac{\partial v}{\partial y} < 0$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Pela continuidade 2D, $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0$. Derivando $u$ em relação a $x$ obtém-se $C_2$. Portanto, $\frac{\partial v}{\partial y} = -C_2$."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, páginas 5–6; `44_QUESTÕES_P1_SEM_CÁLCULO.json`, Questões 6 e 7; Questionário P1, Pergunta 9.

---

## 2.5. Interpretação Física da Convergência Transversal ($\partial v/\partial y = -C_2 < 0$)
*Relação com o Questionário: Pergunta 10*

### Fundamentação Física e Conservação Volumétrica
A obtenção de um gradiente negativo $\frac{\partial v}{\partial y} = -C_2 < 0$ enquanto a velocidade horizontal acelera longitudinalmente ($\frac{\partial u}{\partial x} = C_2 > 0$) tem um significado físico intuitivo e mandatório no regime incompressível:

1. **Estiramento Longitudinal:** Como $\frac{\partial u}{\partial x} > 0$, a extremidade dianteira de qualquer partícula fluida move-se mais rapidamente do que a sua extremidade traseira. Esse gradiente provoca um afastamento espacial das partículas adjacentes ao longo da direção $x$ (estiramento ou extensão horizontal).
2. **Preservação de Densidade e Volume:** Como o líquido não pode expandir-se para ocupar mais espaço (sua densidade $\rho$ é invariável e o volume do elemento cúbico não pode crescer), a única maneira física de repor o espaço interno e satisfazer o balanço de massa é puxar fluido lateralmente.
3. **Convergência Transversal:** O gradiente $\frac{\partial v}{\partial y} < 0$ indica que a velocidade transversal decresce ao longo do eixo vertical $y$, significando que as camadas fluidas superiores e inferiores convergem/aproximam-se entre si (achatamento na direção $y$).

Dessa forma, a contração física na direção transversal equilibra com exatidão matemática o estiramento na direção longitudinal, mantendo a densidade constante e a dilatação volumétrica estritamente nula.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Para compensar o estiramento e o afastamento das partículas na direção horizontal ($x$) sem alterar o volume nem a densidade do fluido incompressível, as camadas fluidas precisam aproximar-se/convergir na direção transversal ($y$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, páginas 5–6; `44_QUESTÕES_P1_SEM_CÁLCULO.json`, Questão 7; Questionário P1, Pergunta 10.

---

# Bloco 3: Balanço de Forças e Gradientes de Pressão

---

## 3.1. Cálculo da Força Líquida de Pressão em um Elemento Diferencial $dx\,dy\,dz$
*Relação com o Questionário: Pergunta 11*

### Definição e Hipóteses
Considere um elemento infinitesimal de fluido estático ou em movimento com dimensões espaciais $dx, dy, dz$ e volume elementar $dV = dx\,dy\,dz$.

A pressão $p(x, y, z)$ é uma força superficial normal compressiva que atua perpendicularmente contra todas as seis faces do paralelepípedo, apontando sempre do meio externo para dentro do elemento fluido (tensão normal de compressão).

### Balanço Diferencial Passo a Passo nas Faces Normais ao Eixo $x$
1. **Face em $x$ (Face de montante / esquerda):**  
A face perpendicular ao eixo $x$ localizada na cota espacial $x$ possui área $dA = dy\,dz$. A pressão nesta face é $p$.  
Como a pressão empurra o elemento para dentro (sentido positivo do eixo $x$), a força exercida sobre a face esquerda é positiva:

$$dF_{x,\text{esquerda}} = +p\,dy\,dz$$

2. **Face em $x + dx$ (Face de jusante / direita):**  
A face oposta localizada na cota $x + dx$ possui a mesma área diferencial $dA = dy\,dz$.  
A pressão nesta face é ligeiramente diferente devido à taxa espacial de variação da pressão, expressa pelo primeiro termo da expansão de Taylor:

$$p(x+dx) = p + \frac{\partial p}{\partial x}dx$$

Como a pressão atua empurrando para dentro da face direita (apontando no sentido negativo do eixo $x$), a força gerada é contrária:

$$dF_{x,\text{direita}} = -\left( p + \frac{\partial p}{\partial x}dx \right) dy\,dz$$

3. **Cálculo da Força Resultante Líquida de Pressão ($dF_{p,x}$):**  
Somam-se vetorialmente as forças que atuam nas duas faces paralelas:

$$dF_{p,x} = dF_{x,\text{esquerda}} + dF_{x,\text{direita}} = p\,dy\,dz - \left( p + \frac{\partial p}{\partial x}dx \right) dy\,dz$$

$$dF_{p,x} = p\,dy\,dz - p\,dy\,dz - \frac{\partial p}{\partial x}dx\,dy\,dz$$

$$dF_{p,x} = -\frac{\partial p}{\partial x}dx\,dy\,dz$$

4. **Força Resultante de Pressão por Unidade de Volume:**  
Dividindo a força líquida resultante pelo volume diferencial $dV = dx\,dy\,dz$:

$$f_{p,x} = \frac{dF_{p,x}}{dV} = \frac{-\frac{\partial p}{\partial x}dx\,dy\,dz}{dx\,dy\,dz} = -\frac{\partial p}{\partial x}$$

Generalizando para as três dimensões espaciais, o vetor de força de pressão resultante por unidade de volume é:

$$\mathbf{f}_p = -\left( \frac{\partial p}{\partial x}\hat{i} + \frac{\partial p}{\partial y}\hat{j} + \frac{\partial p}{\partial z}\hat{k} \right) = -\nabla p$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A face em $x$ recebe força positiva $p\,dy\,dz$, e a face em $x + dx$ recebe força contrária $-\left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$. A força líquida é $-\frac{\partial p}{\partial x}dx\,dy\,dz$. Dividindo pelo volume, obtém-se $-\frac{\partial p}{\partial x}$."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, páginas 12–14; `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`, Seção 3; Questionário P1, Pergunta 11.

---

## 3.2. A Origem e o Significado do Sinal Negativo ($-\partial p/\partial x$) em Navier–Stokes
*Relação com o Questionário: Pergunta 12*

### Razão Mecânica e Convenção de Tensões
Na equação diferencial da quantidade de movimento de Navier–Stokes, o termo forçante de pressão comparece rigorosamente acompanhado do sinal de menos:

$$\rho \frac{Du}{Dt} = -\frac{\partial p}{\partial x} + \mu \nabla^2 u + \rho g_x$$

A justificativa física para esse sinal negativo decorre da própria **natureza termodinâmica e mecânica da pressão**, que opera exclusivamente como uma tensão de compressão atuar de fora para dentro contra qualquer superfície de matéria:

1. **Sentido do Movimento e Aceleração:** Para que um elemento de fluido acelere para a frente (no sentido positivo do eixo $+x$), a força motora aplicada na face traseira deve ser superior à força resistiva da face frontal ($F_{\text{trás}} > F_{\text{frente}}$).
2. **Relação de Pressões:** Isso exige que a pressão a montante ($p_1$) seja maior do que a pressão a jusante ($p_2$), configurando uma queda longitudinal de pressão:

$$p_1 > p_2 \implies \Delta p = p_2 - p_1 < 0 \implies \frac{\partial p}{\partial x} < 0$$

3. **Inversão Algébrica de Sinal:** Se o gradiente espacial da pressão for negativo ($\frac{\partial p}{\partial x} < 0$), a multiplicação pelo sinal de menos converte o termo em um valor estritamente positivo:

$$-\frac{\partial p}{\partial x} = -(-) > 0$$

produzindo uma força líquida efetiva no sentido positivo do escoamento. Em síntese: fluidos aceleram naturalmente de zonas de alta pressão para zonas de baixa pressão; o sinal de menos é o operador matemático que expressa essa causalidade física fundamental.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Porque a pressão é uma tensão de compressão atuante de fora para dentro. Para que haja aceleração para a frente (sentido positivo), a pressão atrás deve ser maior que a pressão à frente ($\frac{\partial p}{\partial x} < 0$), empurrando o fluido de zonas de alta pressão para zonas de baixa pressão."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, página 13; `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`, Seção 3; Questionário P1, Pergunta 12.

---

## 3.3. Comportamento Dinâmico de um Fluido Hipotético com Força $+\partial p/\partial x$
*Relação com o Questionário: Pergunta 13*

### Análise Crítica e Violação de Princípios da Física
Se a dinâmica de um fluido fosse hipoteticamente governada pelo termo de pressão com sinal positivo ($+\frac{\partial p}{\partial x}$):

$$\rho \frac{Du}{Dt} = +\frac{\partial p}{\partial x}$$

Ocorreriam anomalias mecânicas inaceitáveis e violações diretas às leis da física clássica:
1. **Aceleração Espontânea para Alta Pressão:** Diante de uma região com gradiente positivo de pressão ($\frac{\partial p}{\partial x} > 0$, onde a pressão aumenta na direção do avanço), a aceleração resultante seria positiva ($\frac{Du}{Dt} > 0$). Isso faria com que o fluido fosse acelerado espontaneamente na direção onde a pressão cresce, ou seja, mover-se-ia de zonas de menor pressão para zonas de maior pressão sem qualquer fornecimento de trabalho mecânico externo.
2. **Violação do Princípio de Ação e Reação e Tensões Compressivas:** Significaria que uma superfície com pressão maior estaria "puxando" o fluido para dentro dela como se fosse uma tensão de tração, ou que o fluido seria repelido espontaneamente por zonas de vácuo, o que viola frontalmente a natureza física da pressão como força de contato compressiva estática.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O fluido seria acelerado espontaneamente na direção onde a pressão cresce, ou seja, mover-se-ia de zonas de menor pressão para zonas de maior pressão, o que viola o princípio mecânico de equilíbrio de tensões normais compressivas."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, páginas 13–14; `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`, Seção 3; Questionário P1, Pergunta 13.

---

## 3.4. As Duas Grandes Classes de Forças no Balanço Dinâmico de Fluidos
*Relação com o Questionário: Pergunta 14*

### Classificação Mecânica e Exemplos
No balanço de forças de um elemento de fluido infinitesimal (e na estruturação formal da equação da quantidade de movimento de Navier–Stokes), todas as forças externas atuantes dividem-se em duas grandes categorias fundamentais:

| Classe de Força | Mecanismo de Ação | Descrição Física | Componentes e Exemplos Típicos |
| :--- | :--- | :--- | :--- |
| **Forças de Superfície** (ou de Contato) | Contato mecânico direto | Atuam através das fronteiras e áreas que delimitam o volume de controle. Dependem da área do elemento ($dA$). | **Forças Normais:** Pressão hidrodinâmica ($p$).<br>**Forças Tangenciais:** Tensões viscosas cisalhantes ($\tau_{ij} = \mu \frac{\partial u_i}{\partial x_j}$). |
| **Forças de Corpo** (ou de Campo) | Ação volumétrica à distância | Atuam uniformemente sobre toda a massa de cada partícula no interior do volume, sem necessidade de contato superficial mecânico. Dependem do volume do elemento ($dV$). | **Gravidade:** Peso do fluido ($\rho \mathbf{g}$).<br>**Forças Inerciais de Referencial:** Força de Coriolis, força centrífuga.<br>**Forças Eletromagnéticas:** Força de Lorentz. |

### Integração nas Equações de Navier–Stokes
Essa divisão reflete-se na soma de forças por unidade de volume:

$$\rho \frac{D\mathbf{V}}{Dt} = \underbrace{-\nabla p + \mu \nabla^2 \mathbf{V}}_{\text{Forças de Superfície por Vol.}} + \underbrace{\rho \mathbf{g}}_{\text{Força de Corpo por Vol.}}$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "As forças de superfície (que dependem de contato direto, como pressões e tensões viscosas de cisalhamento) e as forças de corpo ou de campo (que atuam à distância sobre a massa inteira, como o peso devido à gravidade)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, páginas 11–12; `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`, Seção 2; Questionário P1, Pergunta 14.

---

# Bloco 4: Condições de Contorno e Hipóteses Hidrodinâmicas

---

## 4.0. Estrutura Metodológica: O Procedimento Geral dos 6 Passos
*(Fundamentação de Aula: Apostila U1, Cap. 5, pp. 22–24)*

Para resolver problemas analíticos de escoamentos laminares incompressíveis internos a partir das equações diferenciais fundamentais, o professor estruturou a metodologia dos **6 Passos**:
1. **Passo 1 — Configuração do Problema:** Desenho geométrico, definição do sistema de coordenadas e orientação dos eixos em relação ao fluxo.
2. **Passo 2 — Hipóteses Simplificadoras Básicas:** Incompressibilidade ($\rho = \text{cte}$), regime permanente ($\partial/\partial t = 0$), escoamento totalmente desenvolvido ($\partial u/\partial x = 0$), bidimensionalidade ($w=0, \partial/\partial z = 0$) e forças de corpo ($\rho g_x$).
3. **Passo 3 — Identificação das Condições de Contorno:** Não-escorregamento tangencial e impenetrabilidade normal nas paredes sólidas e interfaces livres.
4. **Passo 4 — Aplicação das Leis de Conservação:**
   - **4a:** Conservação da massa (Continuidade) para simplificar componentes secundárias ($v$);
   - **4b:** Conservação da quantidade de movimento (Navier–Stokes) na direção principal ($x$).
5. **Passo 5 — Integrações Sucessivas:** Resolução da EDO resultante via separação de variáveis, gerando as constantes de integração ($C_1, C_2$).
6. **Passo 6 — Aplicação das Condições de Contorno e Fechamento:** Substituição das coordenadas das fronteiras para calcular numericamente $C_1$ e $C_2$, obtendo o perfil final de velocidade $u(y)$ ou $u(r)$.

---

## 4.1. Condição Cinemática de Não-Escorregamento (*No-Slip Condition*)
*Relação com o Questionário: Pergunta 15*

### Fundamento Físico e Microatrito
A condição de contorno de **não-escorregamento** (*no-slip condition*) é a premissa fundamental da mecânica dos fluidos viscosos reais (newtonianos). Ela decorre da atração intermolecular e do aprisionamento de moléculas do fluido nas rugosidades microscópicas da parede sólida de contato.

Em termos cinemáticos, ela dita que **as moléculas de fluido em contato microscópico com uma superfície sólida adquirem rigorosamente a mesma velocidade vetorial da parede sólida**:

$$\mathbf{u}_{\text{fluido}}(\mathbf{x}_{\text{parede}}) = \mathbf{u}_{\text{parede}}$$

Em termos de velocidade relativa:

$$\mathbf{u}_{\text{rel}} = \mathbf{u}_{\text{fluido}} - \mathbf{u}_{\text{parede}} = \mathbf{0}$$

### Aplicação ao Chapeamento do Casco do Navio
Ao analisar o escoamento ao redor do casco de uma embarcação em avanço:
- Se o referencial adotado for o referencial hidrodinâmico fixo no navio (onde o casco encontra-se estacionário): a velocidade do fluido aderido ao chapeamento é **rigorosamente zero na parede** ($u_{\text{parede}} = 0$). Conforme a distância vertical $y$ ao casco aumenta, a velocidade cresce progressivamente a partir de zero até alcançar a velocidade do fluxo exterior não perturbado, formando a **camada limite viscosa**.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Impõe que as moléculas do fluido aderidas à superfície sólida adquirem a mesma velocidade vetorial da parede sólida ($u_{\text{rel}} = 0$). Se o casco for fixo no referencial, a velocidade tangencial do fluido na parede é zero."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-024-027.pdf`, página 25; `1_Leis_de_conservação-031-034.pdf`, página 32; `024-027_Mecanica_dos_Fluidos_Capitulo_6.md`, Seção 3; Questionário P1, Pergunta 15.

---

## 4.2. Condição de Contorno de Impenetrabilidade
*Relação com o Questionário: Pergunta 16*

### Definição Geométrica e Cinemática
A condição de contorno de **impenetrabilidade** aplica-se a qualquer fronteira sólida rígida e impermeável. Seu enunciado físico dita que **o fluido não pode atravessar a parede nem a parede pode penetrar no fluido**.

Cinematicamente, isso impõe que a **componente da velocidade do fluido perpendicular (normal) à superfície rígida deve ser identicamente nula**:

$$v_n = \mathbf{V} \cdot \mathbf{n} = 0$$

onde $\mathbf{n}$ é o vetor unitário perpendicular à fronteira sólida orientada para o interior do domínio fluido.

### Papel Algébrico nas Soluções Analíticas
Nas deduções passo a passo da apostila (como em Poiseuille e Couette entre placas planas em $y=0$ e $y=a$):
- A conservação da massa dita $\frac{\partial v}{\partial y} = 0 \implies v(y) = \text{constante} = C_1$;
- A aplicação da impenetrabilidade na parede inferior rígida impõe $v(0) = 0$;
- Consequentemente, $C_1 = 0 \implies v(y) = 0$ em **todo o domínio entre as placas**.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Impõe que o fluido não pode atravessar a parede nem a parede pode penetrar no fluido; logo, a componente da velocidade perpendicular (normal) à superfície rígida deve ser zero ($v_n = 0$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-024-027.pdf`, página 25; `024-027_Mecanica_dos_Fluidos_Capitulo_6.md`, Seção 3; Questionário P1, Pergunta 16.

---

## 4.3. Por que o Escoamento Exterior ao Casco não é "Totalmente Desenvolvido"
*Relação com o Questionário: Pergunta 17*

### Conceito de Escoamento Totalmente Desenvolvido
Na hidráulica clássica, um escoamento é chamado de "totalmente desenvolvido" quando o perfil transversal de velocidades torna-se invariante ao longo da direção do avanço longitudinal:

$$\frac{\partial u}{\partial x} = 0$$

### A Realidade Hidrodinâmica do Casco de um Navio
O escoamento exterior ao redor do casco de uma embarcação em avanço **jamais pode ser classificado como totalmente desenvolvido**:
1. **Crescimento Contínuo da Camada Limite:** A camada limite viscosa cresce continuamente desde a proa até a popa ($\delta(x)$ varia com $x$).
2. **Variação Geométrica das Formas do Casco:** As linhas de forma do casco variam geometricamente ao longo do comprimento (curvatura tridimensional).
3. **Existência de Gradientes Longitudinais:** Existem gradientes de velocidade na direção longitudinal do avanço ($\frac{\partial u}{\partial x} \neq 0$).

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Porque a camada limite viscosa cresce continuamente desde a proa até a popa, as linhas de forma do casco variam geometricamente e existem gradientes de velocidade na direção longitudinal do avanço ($\frac{\partial u}{\partial x} \neq 0$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-022-024.pdf`, página 23; `1_Leis_de_conservação-024-027.pdf`, página 24; `HidVoz 260814_091758_original.txt`; Questionário P1, Pergunta 17.

---

## 4.4. A Incapacidade do Fluido Ideal Invíscido em Calcular o Atrito Superficial
*Relação com o Questionário: Pergunta 18*

### O Modelo de Fluido Invíscido e Suas Limitações
A hipótese clássica de fluido ideal ou invíscido postula que a viscosidade do fluido é nula ($\mu = 0$). Contudo, essa premissa é incapaz de calcular o atrito superficial na parede do navio:

1. **Violação do Não-Escorregamento:** Fluidos invíscidos violam a condição de não-escorregamento, permitindo que o fluido deslize livremente sobre a chapa com velocidade não nula na parede ($u_{\text{parede}} \neq 0$).
2. **Anulação da Tensão Cisalhante:** Pela lei da viscosidade de Newton:

$$\tau_w = \mu \left( \frac{\partial u}{\partial y} \right)_{y=0}$$

Com $\mu = 0$, a tensão viscosa tangencial é matematicamente anulada ($\tau_w = 0$).
3. **Resistência Friccional Nula:** Sem tensão cisalhante na parede, a integral de atrito resulta identicamente zero ($R_F = \iint \tau_w dA = 0$).

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Porque fluidos invíscidos violam a condição de não-escorregamento, permitindo que o fluido deslize livremente sobre a chapa com velocidade não nula na parede, o que matematicamente anula a tensão viscosa tangencial ($\tau_w = \mu \frac{\partial u}{\partial y} = 0$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, páginas 15–16; `024-027_Mecanica_dos_Fluidos_Capitulo_6.md`, Seção 3; Questionário P1, Pergunta 18.

---

# Bloco 5: Conceitos Fundamentais, Couette, Poiseuille, Reynolds, Froude e Similaridade

---

## 5.1. Os Três Princípios Clássicos de Conservação
*Relação com o Questionário: Pergunta 19*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Os três princípios clássicos de conservação que formam a base matemática da termofluídica e da hidrodinâmica são:
> 1. A conservação da massa;
> 2. A conservação da quantidade de movimento (momento linear);
> 3. A conservação da energia."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-001-006.pdf`, página 1; `1_Leis_de_conservação-018-022.pdf`, páginas 18–20; `001-006_Mecanica_dos_Fluidos_Capitulo_1.md`, Seção 1; Questionário P1, Pergunta 19.

---

## 5.2. Descrição Cinemática: Lagrangeana versus Euleriana
*Relação com o Questionário: Pergunta 20*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A abordagem Lagrangeana persegue a história e o trajeto de partículas fluidas individuais identificadas no tempo. A abordagem Euleriana observa o que acontece em posições fixas do espaço por onde diferentes partículas passam."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 8–10; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 4; Questionário P1, Pergunta 20.

---

## 5.3. As Duas Parcelas da Derivada Material Euleriana
*Relação com o Questionário: Pergunta 21*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A derivada material euleriana subdivide a taxa de variação de qualquer grandeza em duas parcelas:
> 1. Na derivada/aceleração local: variação estritamente temporal no ponto fixo ($\frac{\partial}{\partial t}$);
> 2. Na derivada/aceleração convectiva: variação decorrente da mudança de posição do fluido no espaço através de gradientes espaciais ($(\mathbf{V} \cdot \nabla)$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-007-011.pdf`, páginas 8–10; `007-011_Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 2; Questionário P1, Pergunta 21.

---

## 5.4. Classificação das Forças por Mecanismo de Interação
*Relação com o Questionário: Pergunta 22*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Classificam-se em:
> 1. **Forças de superfície:** atuantes por contato mecânico através das fronteiras do volume de controle (pressões e tensões viscosas de cisalhamento);
> 2. **Forças de corpo:** atuantes em cada partícula por campos gravitacionais ou inerciais à distância, sem necessidade de contato superficial."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-011-018.pdf`, páginas 11–12; `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`, Seção 2; Questionário P1, Pergunta 22.

---

## 5.5. Distinção entre Condições de Aderência e de Impermeabilidade
*Relação com o Questionário: Pergunta 23*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A condição de não-escorregamento zera a velocidade tangencial relativa à superfície ($u_{\text{tan, rel}} = 0$), enquanto a condição de impenetrabilidade zera o fluxo e a velocidade perpendicular (normal) à superfície ($v_n = 0$)."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-024-027.pdf`, página 25; `024-027_Mecanica_dos_Fluidos_Capitulo_6.md`, Seção 3; Questionário P1, Pergunta 23.

---

## 5.6. Escoamento Plano de Poiseuille: Placas Fixas e Gradiente de Pressão
*Relação com o Questionário: Pergunta 24*

### Dedução Analítica Passo a Passo (Placas Planas)
1. **Navier–Stokes reduzida em $x$:**

$$\mu \frac{\partial^2 u}{\partial y^2} = \frac{\partial p}{\partial x} = \text{constante}$$

2. **Integrações sucessivas:**

$$\frac{du}{dy} = \frac{1}{\mu}\frac{\partial p}{\partial x}y + C_1$$

$$u(y) = \frac{1}{2\mu}\frac{\partial p}{\partial x}y^2 + C_1 y + C_2$$

3. **Condições de contorno de não-escorregamento:**
   - Em $y = 0$: $u(0) = 0 \implies C_2 = 0$;
   - Em $y = a$: $u(a) = 0 \implies C_1 = -\frac{1}{2\mu}\frac{\partial p}{\partial x}a$.
4. **Perfil parabólico cartesiano:**

$$u(y) = \frac{1}{2\mu}\frac{\partial p}{\partial x}(y^2 - ay) = \frac{1}{2\mu}\left(-\frac{\partial p}{\partial x}\right)(ay - y^2)$$

Velocidade máxima no plano médio ($y = a/2$):

$$u_{\max} = \frac{a^2}{8\mu}\left(-\frac{\partial p}{\partial x}\right)$$

Velocidade média: $U = \frac{2}{3}u_{\max} \implies u_{\max} = 1,5\,U$.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O escoamento em questão é o **escoamento plano de Poiseuille**. Trata-se do escoamento laminar entre duas placas planas paralelas fixas cujo perfil de velocidade é uma parábola perfeita provocada puramente por desnível de pressão."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-024-027.pdf`, páginas 24–27; `024-027_Mecanica_dos_Fluidos_Capitulo_6.md`, Seções 1 a 8; Questionário P1, Pergunta 24.

---

## 5.7. Escoamento Plano de Couette: Arraste Mecânico e Perfil Linear
*Relação com o Questionário: Pergunta 25*

### Dedução Analítica Passo a Passo
1. **Navier–Stokes reduzida em $x$ sem gradiente de pressão ($\frac{\partial p}{\partial x} = 0$):**

$$\mu \frac{d^2 u}{dy^2} = 0 \implies \frac{d^2 u}{dy^2} = 0$$

2. **Integrações sucessivas:**

$$u(y) = C_1 y + C_2$$

3. **Condições de contorno:**
   - Parede inferior fixa em $y = 0$: $u(0) = 0 \implies C_2 = 0$;
   - Placa superior móvel em $y = a$: $u(a) = V_0 \implies C_1 = \frac{V_0}{a}$.
4. **Perfil linear:**

$$u(y) = \frac{V_0}{a}y$$

Tensão de cisalhamento constante em toda a seção: $\tau = \mu \frac{V_0}{a} = \text{constante}$.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O escoamento em questão é o **escoamento de Couette**. Trata-se do escoamento laminar entre duas placas paralelas infinitas em que o fluido é arrastado unicamente pelo deslocamento mecânico de uma das fronteiras, gerando perfil linear."

> **Rastreabilidade da Fonte:** `1_Leis_de_conservação-031-034.pdf`, páginas 31–34; `031-034_Mecanica_dos_Fluidos_Capitulo_8.md`, Seções 1 a 8; Questionário P1, Pergunta 25.

---

## 5.8. Número de Reynolds ($Re$): Inércia versus Forças Viscosas
*Relação com o Questionário: Pergunta 26*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O número de Reynolds ($Re = \frac{\rho U L}{\mu}$). É o número adimensional que indica o predomínio entre forças de inércia e forças viscosas, ditando a transição laminar-turbulenta."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, páginas 3–4; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 5.2; Questionário P1, Pergunta 26.

---

## 5.9. Número de Froude ($Fr$): Inércia versus Gravidade e Ondas de Proa
*Relação com o Questionário: Pergunta 27*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "O número de Froude ($Fr = \frac{U}{\sqrt{gL}}$). É o parâmetro adimensional que compara a inércia do escoamento com o efeito da aceleração gravitacional, comandando o sistema de ondas gerado pela proa do navio."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, páginas 4–5; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 5.3; Questionário P1, Pergunta 27.

---

## 5.10. As Três Similaridades Físicas para Ensaios de Modelos em Tanque
*Relação com o Questionário: Pergunta 28*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "As três similaridades físicas necessárias para garantir equivalência integral de escoamento entre um modelo de testes em tanque e um navio em escala real são:
> 1. **Similaridade geométrica:** formas e dimensões em proporção constante ($\alpha$);
> 2. **Similaridade cinemática:** direções e razões de velocidades constantes ($\beta$);
> 3. **Similaridade dinâmica:** razões entre todas as forças homólogas constantes."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, páginas 13–17; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seções 10 e 11; Questionário P1, Pergunta 28.

---

# Bloco 6: Homogeneidade Dimensional e Teorema de Buckingham

---

## 6.1. A Regra da Homogeneidade Dimensional
*Relação com o Questionário: Pergunta 29*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Estabelece que uma equação só é fisicamente significativa e dimensionalmente coerente se todos os seus membros aditivos possuírem rigorosamente a mesma dimensão primária ($M, L, T$)."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, página 2; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 3; Questionário P1, Pergunta 29.

---

## 6.2. Procedimento de Adimensionalização e Normalização
*Relação com o Questionário: Pergunta 30*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Dividindo cada um dos seus termos por uma mesma combinação algébrica de variáveis do problema que possua essa mesma dimensão fundamental."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, página 2; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 3; Questionário P1, Pergunta 30.

---

## 6.3. O Teorema $\Pi$ de Buckingham e o Número de Monômios Independentes
*Relação com o Questionário: Pergunta 31*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Em termos do Teorema $\Pi$ de Buckingham, se um fenômeno hidrodinâmico é função de $n$ grandezas físicas e há $m$ dimensões fundamentais que as definem, serão obtidos exatamente:
> $$k = n - m$$
> monômios adimensionais independentes."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, páginas 6–7; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 6; Questionário P1, Pergunta 31.

---

## 6.4. Critério de Independência das Variáveis Repetidas
*Relação com o Questionário: Pergunta 32*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Não. As variáveis repetidas devem ser dimensionalmente independentes, sendo proibido que qualquer combinação entre elas forme um número adimensional isolado."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, página 7; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 6; Questionário P1, Pergunta 32.

---

## 6.5. Quantidade e Requisito Cumulativo das Grandezas Repetidas
*Relação com o Questionário: Pergunta 33*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Devem ser selecionadas exatamente $m$ variáveis (onde $m$ é o número de dimensões fundamentais, tipicamente 3 para o sistema $MLT$), e elas devem, juntas, conter todas as dimensões básicas do problema."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, página 7; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seção 6; Questionário P1, Pergunta 33.

---

## 6.6. Grupos Adimensionais na Resistência de Avanço do Casco ($R, \rho, U, L, \mu, g, \sigma$)
*Relação com o Questionário: Pergunta 34*

### Identificação das Variáveis e Aplicação do Teorema de Buckingham
- **Grandezas físicas envolvidas ($n = 7$):**
  1. Resistência ao avanço $R$: dimensão $[M L T^{-2}]$
  2. Massa específica da água $\rho$: dimensão $[M L^{-3}]$
  3. Velocidade de avanço $U$: dimensão $[L T^{-1}]$
  4. Comprimento do casco $L$: dimensão $[L]$
  5. Viscosidade dinâmica $\mu$: dimensão $[M L^{-1} T^{-1}]$
  6. Aceleração da gravidade $g$: dimensão $[L T^{-2}]$
  7. Tensão superficial $\sigma$: dimensão $[M T^{-2}]$ ($[\text{Força}]/[\text{Comprimento}]$)
- **Dimensões fundamentais ($m = 3$):** Massa ($M$), Comprimento ($L$), Tempo ($T$).
- **Número de grupos adimensionais independentes:**
  $$k = n - m = 7 - 3 = 4 \text{ grupos } (\Pi_1, \Pi_2, \Pi_3, \Pi_4)$$
- **Tríade de variáveis repetidas ($m = 3$):** $\{\rho, U, L\}$ (propriedade do fluido, cinemática, geometria).
  Verificação de independência dimensional: $\det\begin{pmatrix} 1 & -3 & 0 \\ 0 & 1 & -1 \\ 0 & 1 & 0 \end{pmatrix} = 1 \neq 0$.

### Dedução Matemática Completa dos Quatro Grupos Passo a Passo

1. **Grupo $\Pi_1$ — Força de Resistência ao Avanço ($R$):**
   $$\Pi_1 = R \cdot \rho^a L^b U^c$$
   $$[M^0 L^0 T^0] = [M L T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{1 - 3a + b + c} \cdot T^{-2 - c}$$
   - Equação em $M$: $1 + a = 0 \implies a = -1$
   - Equação em $T$: $-2 - c = 0 \implies c = -2$
   - Equação em $L$: $1 - 3a + b + c = 0 \implies 1 - 3(-1) + b + (-2) = 0 \implies b + 2 = 0 \implies b = -2$
   $$\Pi_1 = R \cdot \rho^{-1} L^{-2} U^{-2} = \frac{R}{\rho U^2 L^2}$$
   
   *Análise Crítica e Relação com o Coeficiente de Resistência ($C_T$):*
   - **Origem pelo Teorema de Buckingham:** A análise dimensional direta gera $\Pi_1 = \frac{R}{\rho U^2 L^2}$, normalizado pela área característica $L^2$ e sem constantes numéricas puras como $1/2$ (as quais não emergem do sistema linear de expoentes dimensionais).
   - **Definição na Hidrodinâmica Naval Canônica (ITTC):** O coeficiente de resistência total é convencionado como $C_T = \frac{R}{\frac{1}{2}\rho S U^2}$, onde a força é normalizada pela pressão dinâmica do escoamento ($\frac{1}{2}\rho U^2$) e pela área da superfície molhada real do casco ($S$).
   - **Relação Algébrica Exata:** Sob a relação geométrica $S = c_s L^2$, substituindo sem omissão de termos:
     $$C_T = \frac{R}{\frac{1}{2}\rho S U^2} = \frac{R}{\frac{1}{2}\rho (c_s L^2) U^2} = \frac{1}{\frac{1}{2}c_s} \cdot \left(\frac{R}{\rho U^2 L^2}\right) = \frac{2}{c_s} \cdot \Pi_1 \iff \Pi_1 = \frac{c_s}{2} \cdot C_T$$
   - **Significado de $c_s = S/L^2$ e Condições de Constância:** O parâmetro $c_s = S/L^2$ é um fator de forma geométrico adimensional. Ele pode ser tratado como rigorosamente constante se, e somente se, houver **similaridade geométrica estrita (*geosim*)** entre modelo e navio em escala real, com calado e linha de flutuação nominais estáticos inalterados, e desprezando-se deformações dinâmicas da superfície livre (afundamento dinâmico /*sinkage*, caimento /*trim* e perfil de ondas ao longo do costado). Caso a velocidade altere a área molhada relativa $S(U)$, $c_s$ não permanece estritamente invariante.
   - **Equivalência Dimensional versus Disparidade Numérica:**
     - *Equivalência Dimensional:* Ambos são monômios adimensionais puros de dimensão $[M^0 L^0 T^0]$.
     - *Disparidade Numérica:* **Não são numericamente iguais**. Como para cascos de navios de deslocamento típicos a razão geométrica situa-se na faixa $c_s \in [0,10; 0,30]$, o multiplicador $\frac{2}{c_s}$ assume valores entre $6,7$ e $20$. Assim, numericamente, $C_T$ é de uma a duas ordens de grandeza maior que $\Pi_1$.
   - **Registro de Limitação Documental:** No `Questionário P1.pdf` (Pergunta 34), o professor denomina o grupo como "Coeficiente de Resistência Total ($C_T$)", mas não explicita a sua fórmula analítica de normalização; já na Apostila de U2 (p. 10), o professor deduz estritamente $\Pi_1 = \frac{R_{\text{forma}}}{\rho L^2 U^2}$ e chama-o de coeficiente de arrasto de forma. Registra-se, portanto, que a análise dimensional pura fornece $\Pi_1$, enquanto a transposição para $C_T$ naval requer o fator $\frac{2}{c_s}$.

2. **Grupo $\Pi_2$ — Efeito Viscoso ($\mu$):**
   $$\Pi_2 = \mu \cdot \rho^a L^b U^c$$
   $$[M^0 L^0 T^0] = [M L^{-1} T^{-1}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{-1 - 3a + b + c} \cdot T^{-1 - c}$$
   - Equação em $M$: $1 + a = 0 \implies a = -1$
   - Equação em $T$: $-1 - c = 0 \implies c = -1$
   - Equação em $L$: $-1 - 3a + b + c = 0 \implies -1 - 3(-1) + b + (-1) = 0 \implies b + 1 = 0 \implies b = -1$
   $$\Pi_2 = \mu \cdot \rho^{-1} L^{-1} U^{-1} = \frac{\mu}{\rho U L}$$
   *Equivalência com Reynolds:* Como $\Pi_2$ expressa a razão $(\text{viscosidade})/(\text{inércia})$, toma-se o inverso para seguir o padrão canônico que coloca as forças inerciais desestabilizadoras no numerador:
   $$\Pi_2^{-1} = \frac{\rho U L}{\mu} \equiv Re \quad (\text{ou } Rn \text{ na apostila de U2})$$

3. **Grupo $\Pi_3$ — Efeito Gravitacional e Geração de Ondas ($g$):**
   $$\Pi_3 = g \cdot \rho^a L^b U^c$$
   $$[M^0 L^0 T^0] = [L T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^a \cdot L^{1 - 3a + b + c} \cdot T^{-2 - c}$$
   *(Nota: erro de digitação na linha intermediária da Apostila U2 p. 11 grafou $T^{-1-c}$, corrigido na linha seguinte pelo próprio docente).*
   - Equação em $M$: $a = 0$
   - Equação em $T$: $-2 - c = 0 \implies c = -2$
   - Equação em $L$: $1 - 3(0) + b + (-2) = 0 \implies b - 1 = 0 \implies b = 1$
   $$\Pi_3 = g \cdot \rho^0 L^1 U^{-2} = \frac{g L}{U^2}$$
   *Equivalência com Froude:* Para compatibilizar com a velocidade crítica de onda em canal aberto ($c = \sqrt{g h}$), a hidrodinâmica naval padronizou a raiz quadrada do inverso:
   $$\Pi_3^{-1/2} = \sqrt{\frac{U^2}{g L}} = \frac{U}{\sqrt{g L}} \equiv Fr \quad (\text{ou } Fn \text{ na apostila de U2})$$

4. **Grupo $\Pi_4$ — Efeito de Tensão Superficial e Capilaridade ($\sigma$):**
   $$\Pi_4 = \sigma \cdot \rho^a L^b U^c$$
   $$[M^0 L^0 T^0] = [M T^{-2}] \cdot [M L^{-3}]^a \cdot [L]^b \cdot [L T^{-1}]^c = M^{1+a} \cdot L^{-3a + b + c} \cdot T^{-2 - c}$$
   - Equação em $M$: $1 + a = 0 \implies a = -1$
   - Equação em $T$: $-2 - c = 0 \implies c = -2$
   - Equação em $L$: $-3a + b + c = 0 \implies -3(-1) + b + (-2) = 0 \implies 3 + b - 2 = 0 \implies b = -1$
   $$\Pi_4 = \sigma \cdot \rho^{-1} L^{-1} U^{-2} = \frac{\sigma}{\rho U^2 L}$$
   *Equivalência com Weber:* Invertendo o monômio para expressar $(\text{inércia})/(\text{tensão superficial})$:
   $$\Pi_4^{-1} = \frac{\rho U^2 L}{\sigma} \equiv We \quad (\text{ou } Wn \text{ na apostila de U2})$$

---

### Exemplo Comparativo: Dedução de Reynolds em Duto Circular via Buckingham
*(Fontes: Apostila U2 p. 8 e `Resolução Q.5 - Passo 6.md`)*

No problema do escoamento em duto cilíndrico com variáveis $u$ ($[L T^{-1}]$), $D$ ($[L]$), $\mu$ ($[M L^{-1} T^{-1}]$), $\rho$ ($[M L^{-3}]$) onde $n=4, m=3 \implies k = 1$:
- Variáveis repetidas: $\{\rho, \mu, u\}$.
- Variável não repetida: $D$.
- Montagem:
  $$\Pi_1 = D \cdot \rho^a \mu^b u^c \implies [M^0 L^0 T^0] = [L] \cdot [M L^{-3}]^a [M L^{-1} T^{-1}]^b [L T^{-1}]^c = M^{a+b} L^{1 - 3a - b + c} T^{-b - c}$$
- Sistema linear:
  1. $M: a + b = 0 \implies a = -b$
  2. $T: -b - c = 0 \implies c = -b$
  3. $L: 1 - 3a - b + c = 0 \implies 1 - 3(-b) - b + (-b) = 0 \implies 1 + b = 0 \implies b = -1$
  Logo: $a = 1$ e $c = 1$.
- Resultado:
  $$\Pi_1 = D^1 \rho^1 \mu^{-1} u^1 = \frac{\rho u D}{\mu} \equiv Re_D$$
Nesta formulação alternativa, o Número de Reynolds surge diretamente com expoente positivo sem necessidade de inversão posterior, comprovando que a estrutura algébrica de Buckingham preserva a integridade dimensional do agrupamento.

---

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Como temos $n = 7$ variáveis físicas e $m = 3$ dimensões fundamentais ($MLT$), formam-se $k = 7 - 3 = 4$ grupos adimensionais clássicos independentes:
> 1. **Coeficiente de Resistência Total ($C_T = \frac{R}{\rho U^2 L^2}$)**: relaciona a força resistente com a inércia do escoamento;
> 2. **Número de Reynolds ($Re = \frac{\rho U L}{\mu}$)**: governa a razão entre forças de inércia e forças viscosas na camada limite;
> 3. **Número de Froude ($Fr = \frac{U}{\sqrt{g L}}$)**: governa a razão entre forças inerciais e gravitacionais, comandando o sistema de ondas de proa;
> 4. **Número de Weber ($We = \frac{\rho U^2 L}{\sigma}$)**: quantifica a inércia em relação à tensão superficial na interface livre.  
> *(Nota: na notação da apostila de aula, esses grupos são expressos como $R_{\text{forma}}/(\rho L^2 U^2), Rn, Fn, Wn$)*."

> **Rastreabilidade da Fonte:** `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, páginas 9–12; `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md`, Seções 6 e 9; `Questionário P1.pdf`, Pergunta 34.

---

# Bloco 7: Escoamento em Dutos Circulares (Hagen–Poiseuille)

> [!important] Nota Metodológica de Auditoria Documental:
> O escoamento em dutos cilíndricos (Hagen–Poiseuille) é abordado diretamente no `Questionário P1.pdf` (Perguntas 35 a 40), com fórmulas e gabaritos oficiais. Contudo, sua dedução matemática formal em coordenadas cilíndricas $(r, \theta, x)$ não constava nas apostilas teóricas de U1 (que deduziram exclusivamente o caso cartesiano 2D de placas planas). A dedução detalhada apresentada nas seções a seguir foi desenvolvida com base mecânica canônica em coordenadas radiais para fornecer fundamentação analítica completa às respostas oficiais do professor.

---

## 7.1. Definição do Número de Reynolds em Duto e Faixas Críticas de Transição
*Relação com o Questionário: Pergunta 35*

### Definição Conceitual
Para o escoamento interno em condutos cilíndricos de seção circular, a dimensão linear característica do escoamento é o **diâmetro interno da tubulação ($D$)**, e a velocidade representativa é a **velocidade média volumétrica ($U$)**:

$$Re_D = \frac{\rho U D}{\mu} = \frac{U D}{\nu}$$

### Faixas Críticas de Transição no Duto Circular
Conforme estabelecido oficialmente no `Questionário P1.pdf` (Pergunta 35):
- **Laminar:** para $Re_D < 2300$;
- **De transição:** para $2300 \le Re_D \le 4000$;
- **Turbulento:** para $Re_D > 4000$.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Define-se como $Re_D = \frac{\rho U D}{\mu}$. O escoamento em duto circular é:
> - Laminar: para $Re_D < 2300$;
> - De transição: para $2300 \le Re_D \le 4000$;
> - Turbulento: para $Re_D > 4000$."

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, páginas 5–6; `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf`, página 4 (onde cita $(Re_D)_{cr} \cong 2,3 \times 10^3$).

---

## 7.2. Balanço Diferencial e Obtenção do Perfil Radial Parabólico $u(r)$
*Relação com o Questionário: Pergunta 36*

### Dedução Analítica em Coordenadas Cilíndricas (Suporte Canônico Complementar)
Considere um duto cilíndrico de raio interno $R = D/2$ e comprimento $L$. Tomando um cilindro coaxial de fluido de raio $r \le R$:
1. **Balanço de forças axiais em regime permanente e totalmente desenvolvido ($\sum F_x = 0$):**
   - Força de pressão motora: $\Delta p (\pi r^2)$;
   - Força resistente cisalhante na superfície lateral: $\tau(r) (2\pi r L)$;
   - Equilíbrio: $\Delta p (\pi r^2) - \tau(r) (2\pi r L) = 0 \implies \tau(r) = \frac{r}{2}\frac{\Delta p}{L}$.
2. **Lei de Newton em coordenadas radiais:**  
Como a velocidade decresce do centro para a parede ($\frac{du}{dr} < 0$):

$$\tau(r) = -\mu \frac{du}{dr}$$

3. **Equação diferencial:**

$$-\mu \frac{du}{dr} = \frac{r}{2}\frac{\Delta p}{L} \implies \frac{du}{dr} = -\left( \frac{\Delta p}{2\mu L} \right) r$$

4. **Integração:**

$$u(r) = -\frac{\Delta p}{4\mu L} r^2 + C$$

5. **Condição de contorno de não-escorregamento na parede ($u(R) = 0$):**

$$0 = -\frac{\Delta p}{4\mu L} R^2 + C \implies C = \frac{\Delta p}{4\mu L} R^2$$

6. **Perfil parabólico radial:**

$$u(r) = \frac{\Delta p R^2}{4\mu L} \left[ 1 - \left( \frac{r}{R} \right)^2 \right] = u_{\max} \left[ 1 - \left( \frac{r}{R} \right)^2 \right]$$

onde $u_{\max} = \frac{\Delta p R^2}{4\mu L}$ é a velocidade na linha de centro ($r = 0$).

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Partindo do equilíbrio diferencial entre gradiente de pressão e tensões viscosas no interior de um tubo cilíndrico, o perfil é parabólico, onde a velocidade varia em função do raio $r$ a partir do centro segundo a equação:
> $$u(r) = u_{\max} \left[ 1 - \left( \frac{r}{R} \right)^2 \right]$$
> sendo $R = D/2$ o raio interno do duto."

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, página 6; dedução analítica canônica em coordenadas cilíndricas.

---

## 7.3. Relação Numérica Exata entre Velocidade Máxima e Velocidade Média ($u_{\max} = 2U$)
*Relação com o Questionário: Pergunta 37*

### Dedução Analítica da Velocidade Média
1. **Integração da vazão volumétrica $Q$ em anéis concêntricos ($dA = 2\pi r dr$):**

$$Q = \int_0^R u(r) \cdot 2\pi r\,dr = 2\pi u_{\max} \int_0^R \left( r - \frac{r^3}{R^2} \right) dr = 2\pi u_{\max} \left[ \frac{R^2}{2} - \frac{R^4}{4R^2} \right] = \frac{\pi R^2}{2} u_{\max}$$

2. **Velocidade média ($U = Q / A$, com $A = \pi R^2$):**

$$U = \frac{\frac{\pi R^2}{2} u_{\max}}{\pi R^2} = \frac{u_{\max}}{2}$$

3. **Relação exata:**

$$u_{\max} = 2U$$

*(Contraste: em placas planas paralelas, a relação é $u_{\max} = 1,5\,U$).*

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A velocidade máxima no centro é exatamente o dobro da velocidade média:
> $$u_{\max} = 2U$$"

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, página 6; cálculo analítico da vazão em coordenadas radiais.

---

## 7.4. Distribuição Transversal da Tensão de Cisalhamento Viscosa $\tau(r)$
*Relação com o Questionário: Pergunta 38*

### Equação de Distribuição das Tensões
A partir do balanço fundamental:

$$\tau(r) = \frac{r}{2}\frac{\Delta p}{L}$$

A tensão de cisalhamento varia **linearmente com o raio $r$**:
1. **Na linha de centro ($r = 0$):**

$$\tau(0) = 0$$

pois no centro o gradiente de velocidade é nulo ($\frac{du}{dr} = 0$, vértice da parábola).
2. **Na parede sólida ($r = R = D/2$):**

$$\tau_w = \tau(R) = \frac{R}{2}\frac{\Delta p}{L} = \frac{D}{4}\frac{\Delta p}{L}$$

atingindo o seu valor **máximo absoluto**.

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A tensão de cisalhamento varia linearmente com o raio $r$: ela é nula no centro do tubo ($r = 0$, onde o gradiente de velocidade $\frac{du}{dr} = 0$) e atinge seu valor máximo na parede sólida ($r = R = D/2$)."

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, página 6; balanço diferencial de forças.

---

## 7.5. Equação Analítica de Hagen–Poiseuille: Queda de Pressão ($\Delta p$)
*Relação com o Questionário: Pergunta 39*

### Dedução da Expressão da Perda de Carga
1. Da vazão volumétrica:

$$Q = \frac{\pi R^2}{2} u_{\max} = \frac{\pi R^2}{2}\left( \frac{\Delta p R^2}{4\mu L} \right) = \frac{\pi R^4 \Delta p}{8\mu L}$$

2. Substituindo $R = D/2 \implies R^4 = D^4 / 16$:

$$Q = \frac{\pi D^4 \Delta p}{128\mu L}$$

3. Isolando a queda de pressão $\Delta p$:

$$\Delta p = \frac{128\,\mu L Q}{\pi D^4}$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "A queda de pressão é proporcional à viscosidade e à vazão, e inversamente proporcional à quarta potência do diâmetro:
> $$\Delta p = \frac{128\,\mu L Q}{\pi D^4}$$"

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, página 6; dedução clássica da Lei de Hagen-Poiseuille.

---

## 7.6. Sensibilidade ao Diâmetro: Efeito da Redução de $D$ pela Metade
*Relação com o Questionário: Pergunta 40*

### Resolução Passo a Passo
Como $\Delta p$ é inversamente proporcional a $D^4$:

$$\Delta p \propto \frac{1}{D^4}$$

Substituindo $D_{\text{novo}} = \frac{D}{2}$:

$$\Delta p_{\text{novo}} = \frac{128\,\mu L Q}{\pi (D/2)^4} = \frac{128\,\mu L Q}{\pi \frac{D^4}{16}} = 16 \cdot \left( \frac{128\,\mu L Q}{\pi D^4} \right) = 16\,\Delta p$$

### Resposta Discursiva para a Prova
> **Como responder em prova:**  
> "Como $\Delta p$ é inversamente proporcional a $D^4$, ao reduzir o diâmetro pela metade ($D/2$), a queda de pressão aumentará por um fator de $2^4 = 16$ vezes."

> **Rastreabilidade da Fonte:** `Questionário P1.pdf`, página 6; `44_QUESTÕES_P1_SEM_CÁLCULO.json`; Questionário P1, Pergunta 40.

---

# Pontos para Conferência com o Professor

1. **Faixas de Transição do Número de Reynolds em Dutos (Q35 vs. Apostila U2 p. 4):**  
   Na apostila de U2, cita-se $(Re_D)_{cr} \cong 2,3 \times 10^3$ para tubos comerciais. No `Questionário P1.pdf`, a resposta oficial delimita três faixas rígidas: Laminar ($<2300$), Transição ($2300 \le Re_D \le 4000$) e Turbulento ($>4000$). Adotou-se o padrão completo do questionário.
2. **Dedução de Hagen–Poiseuille em Dutos Cilíndricos (Bloco 7):**  
   A dedução em placas planas paralelas (Poiseuille plano) consta detalhada na apostila de U1 (Capítulo 6), mas a dedução em coordenadas cilíndricas para tubos circulares fechados não estava formalizada nas notas de U1, constando apenas os resultados e fórmulas no Questionário P1. Forneceu-se a dedução analítica canônica rigorosa por balanço de cascas cilíndricas coaxiais para pleno suporte ao estudante.
3. **Independência de $Re$ para a Resistência de Forma (Bloco 6, Q34 / Apostila U2 p. 10):**  
   A apostila de U2 pontua que a resistência de forma independe de $Re$, o que reflete uma simplificação adotada na aula para isolar a dependência friccional pura de $\pi_2$, divergindo da decomposição contemporânea da ITTC. Deve-se confirmar com o professor a expectativa de resposta teórica.
4. **Erros Tipográficos Originais nas Apostilas:**  
   Registrados detalhadamente no documento `Pendencias_Verificacao.md` para resguardo e integridade acadêmica.
