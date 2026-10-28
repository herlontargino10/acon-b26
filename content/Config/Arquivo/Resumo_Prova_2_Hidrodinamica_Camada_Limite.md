# RESUMO COMPLETO PARA A PROVA 2 — HIDRODINÂMICA
**Fonte Principal:** *3_Camada_limite_e_Resistência_Friccional_de_Navios_Prof_Mesquita.pdf* (Prof. Edson Mesquita, D.Sc.) [1]

---

## SEÇÃO I: INTRODUÇÃO E FUNDAMENTOS DA CAMADA LIMITE
*(Páginas 1 a 2 do PDF)* [1, 2]

### 1.1 Contexto Histórico e o Paradoxo de d'Alembert
Antes da formulação da teoria da camada limite em 1904, a mecânica dos fluidos apoiava-se na teoria dos **escoamentos potenciais** (fluido ideal, incompressível, irrotacional e sem viscosidade) [4]. Embora algebricamente elegante, essa teoria previa que um corpo totalmente imerso sofria **força de arrasto estritamente nula** — contradição empírica conhecida como **Paradoxo de d'Alembert** [4]. Em virtude dessa falha, a hidrodinâmica teórica manteve-se afastada da engenharia prática, e o projeto de navios dependia de metodologias empíricas, como a formulada por William Froude em 1864 [4, 7].

### 1.2 O Conceito de Ludwig Prandtl (1904)
Em 1904, Ludwig Prandtl propôs que o escoamento ao redor de um corpo sólido imerso pode ser dividido em duas regiões [5]:
1. **Escoamento Potencial Externo:** Região afastada do corpo onde os efeitos da viscosidade do fluido são desprezíveis e a teoria clássica de escoamento potencial aplica-se perfeitamente [5].
2. **Camada Limite (Boundary Layer):** Uma fina camada fluida imediatamente adjacente à parede sólida onde os **efeitos viscosos e os efeitos inerciais possuem a mesma ordem de grandeza** [5, 10].

Sob a ótica matemática, as equações da camada limite correspondem às soluções limites das equações completas de Navier-Stokes para altos números de Reynolds ($Re \to \infty$) [6].

### 1.3 Condição de Não Escorregamento e Tensão Cisalhante
A camada limite surge devido à **condição de não escorregamento** (*no-slip condition*): as moléculas do fluido em contato direto com a parede aderem à superfície, apresentando velocidade nula em relação ao corpo ($u(y=0) = 0$) [2, 9].

- **Perfil de Velocidade $u(y)$:** Curva que descreve o crescimento da velocidade longitudinal $u$ em função da distância normal $y$, partindo de zero na parede até atingir a velocidade não perturbada da corrente livre $V_0$ [3].
- **Tensão de Cisalhamento na Parede ($\tau_w$):** Força tangencial por unidade de área exercida pelo fluido sobre a superfície devido à viscosidade dinâmica $\mu$ [1, 2]:
  $$\tau_w = \mu \left. \frac{\partial u}{\partial y} \right|_{y=0} \quad [\text{Pa ou N/m}^2]$$
- **Coeficiente de Fricção Local ($c_{f,x}$):** Parâmetro adimensional que representa a tensão cisalhante local relativa à pressão dinâmica do escoamento livre [3]:
  $$c_{f,x} = \frac{\tau_w}{\frac{1}{2} \rho V_0^2}$$

### 1.4 Regimes Laminar e Turbulento
A camada limite apresenta dois regimes principais ao longo do comprimento da placa $x$ [3]:
- **Laminar:** Ocorre no bordo de ataque ($x=0$). O fluido desliza em lâminas paralelas ordenadas [3, 4].
- **Turbulento:** Ocorre mais a jusante. Apresenta movimento caótico e vórtex tridimensionais que promovem intensa mistura macroscópica de quantidade de movimento [3, 4].
- **Comparativo de Gradientes e Fricção:** O perfil turbulento médio $\bar{u}(y)$ é mais "assentado" (uniforme no centro) e possui um gradiente de velocidade na parede muito mais elevado do que o perfil laminar [4, 50]:
  $$\left. \frac{\partial u}{\partial y} \right|_{y=0, \text{lam}} < \left. \frac{\partial \bar{u}}{\partial y} \right|_{y=0, \text{turb}} \implies \tau_{w,\text{turb}} > \tau_{w,\text{lam}}$$

---

### Perguntas Conceituais e Respostas — Seção I

**P1. Como a hipótese da camada limite de Prandtl (1904) resolveu o Paradoxo de d'Alembert?**
> **Resposta:** O Paradoxo de d'Alembert previa arrasto nulo em fluidos ideais [4]. Prandtl resolveu essa inconsistência demonstrando que a viscosidade não precisa afetar todo o campo de escoamento, mas fica restrita a uma camada muito fina junto ao corpo (a camada limite), onde forças viscosas e inerciais se equivalem [5, 10]. Fora dela, o escoamento potencial permanece válido [5].

**P2. Por que a tensão cisalhante na parede ($\tau_w$) é maior na camada limite turbulenta do que na laminar?**
> **Resposta:** Devido à troca vigorosa de quantidade de movimento promovida pelos vórtex, o perfil turbulento de velocidade média $\bar{u}(y)$ é mais preenchido no interior do escoamento e sofre uma variação abrupta de velocidade muito próxima à parede [4, 53]. Isso torna o gradiente na parede ($\partial \bar{u}/\partial y|_{y=0}$) muito mais íngreme no regime turbulento do que no laminar, resultando em maior $\tau_w$ e maior $c_f$ [4, 51].

---

## SEÇÃO II: DEDUÇÃO DAS EQUAÇÕES DE CAMADA LIMITE LAMINAR DE PRANDTL
*(Páginas 2 a 6 do PDF)* [8]

### 2.1 Metodologia e Hipóteses Simplificadoras
Para derivar as equações simplificadas a partir de Navier-Stokes, Prandtl adotou uma análise dimensional baseada em escalas características de uma placa plana de comprimento $L$ imersa em um escoamento $V_0$ [9, 12]:
1. **Escoamento Bidimensional (2D):** Componente transversal $w = 0$ e $\partial/\partial z = 0$ [10].
2. **Escoamento Permanente e Incompressível:** Densidade $\rho$ e viscosidade $\mu$ constantes; $\partial/\partial t = 0$ [10].
3. **Escalas e Variáveis Adimensionais:** $u^* = \frac{u}{V_0} \sim O(1)$; $x^* = \frac{x}{L} \sim O(1)$; $y^* = \frac{y}{L} \sim O(\bar{\delta}) = O\left(\frac{\delta}{L}\right)$ [12, 14].

### 2.2 Observação Histórico-Matemática sobre Navier-Stokes 3D (Pág. 3–4)
Ao apresentar o sistema de equações de Navier-Stokes, o professor destaca que a solução dentro de contornos livres não é trivial [8].
- **Observação do Professor na Apostila:** O professor ressalta que enquanto no caso 2D é possível obter simplificações e soluções sob certas condições [8, 9], **no caso tridimensional (3D) completo, demonstrar matematicamente a existência e regularidade/unicidade de solução suave para qualquer condição inicial nunca foi feito na história da ciência**. Esse desafio constitui um dos sete *Prêmios do Milênio* do **Instituto Clay de Matemática**, oferecendo um prêmio de um milhão de dólares.

### 2.3 Dedução Passo a Passo via Adimensionalização e Ordem de Grandeza

#### 1. Equação da Continuidade 2D Adimensional:
$$\frac{\partial u^*}{\partial x^*} + \frac{\partial v^*}{\partial y^*} = 0 \implies \frac{O(1)}{O(1)} + \frac{O(v^*)}{O(\bar{\delta})} = 0 \implies O(v^*) = O(\bar{\delta})$$
Assim, a velocidade normal adimensional $v^*$ é de ordem de grandeza muito pequena $O(\bar{\delta}) = O(\delta/L)$ [14].

#### 2. Equação da Quantidade de Movimento em $x$ Adimensionalizada:
Prandtl escreveu a equação adimensionalizada da quantidade de movimento na direção $x$ [13, 16]:
$$u^* \frac{\partial u^*}{\partial x^*} + v^* \frac{\partial u^*}{\partial y^*} = -\frac{\partial p^*}{\partial x^*} + \frac{1}{Re} \left( \frac{\partial^2 u^*}{\partial x^{*2}} + \frac{\partial^2 u^*}{\partial y^{*2}} \right)$$
- Termos Inerciais (lado esquerdo): $u^* \frac{\partial u^*}{\partial x^*} \sim O(1) \cdot \frac{O(1)}{O(1)} = O(1)$ e $v^* \frac{\partial u^*}{\partial y^*} \sim O(\bar{\delta}) \cdot \frac{O(1)}{O(\bar{\delta})} = O(1)$ [14].
- Termos Viscosos (lado direito): $\frac{1}{Re} \frac{\partial^2 u^*}{\partial x^{*2}} \sim \frac{1}{Re} \cdot O(1)$ vs. $\frac{1}{Re} \frac{\partial^2 u^*}{\partial y^{*2}} \sim \frac{1}{Re \cdot \bar{\delta}^2}$ [14].

Para que haja equilíbrio entre forças inerciais e viscosas na camada limite [14]:
$$\frac{1}{Re \cdot \bar{\delta}^2} \sim O(1) \implies \bar{\delta} \sim O\left(\frac{1}{\sqrt{Re}}\right) \implies O\left(\frac{\delta}{L}\right) = O\left(\frac{1}{\sqrt{Re_L}}\right)$$
Como $Re \gg 1$, o termo de difusão longitudinal $\frac{1}{Re}\frac{\partial^2 u^*}{\partial x^{*2}} \sim O(1/Re) \ll 1/\sqrt{Re}$ é desprezível perante $\frac{1}{Re}\frac{\partial^2 u^*}{\partial y^{*2}} \sim O(1)$, sendo descartado [15, 16].

#### 3. Equação da Quantidade de Movimento em $y$:
$$u^* \frac{\partial v^*}{\partial x^*} + v^* \frac{\partial v^*}{\partial y^*} = -\frac{\partial p^*}{\partial y^*} + \frac{1}{Re} \left( \frac{\partial^2 v^*}{\partial x^{*2}} + \frac{\partial^2 v^*}{\partial y^{*2}} \right)$$
Todos os termos inerciais e viscosos em $y$ são de ordem $O(\bar{\delta})$ [16, 17]. Portanto:
$$\frac{\partial p^*}{\partial y^*} \sim O(\bar{\delta}) \approx 0 \implies p(x,y) \approx p_e(x)$$
A variação de pressão através da espessura da camada limite é negligenciável [18, 19].

### 2.4 Relação com a Equação de Bernoulli Externa e Sistema de Prandtl
Aplica-se a Equação de Bernoulli no escoamento potencial externo: $-\frac{\partial p}{\partial x} = \rho V(x) \frac{dV(x)}{dx}$ [19, 20].

Para uma placa plana alinhada ao escoamento livre ($dV/dx = 0 \implies \partial p/\partial x = 0$), o sistema final de Prandtl em variáveis dimensionais resulta em [20, 21]:

$$\begin{cases}
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0 \\[8pt]
u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = \nu \frac{\partial^2 u}{\partial y^2}
\end{cases}$$

- **Condições de Contorno:**
  - Na parede ($y = 0$): $u(x,0) = 0$ e $v(x,0) = 0$ (não escorregamento e impermeabilidade) [9, 21].
  - Na borda exterior ($y = \delta(x)$): $u(x,\delta) = 0,99 V_0$ [21].

---

## SEÇÃO III: MÉTODO INTEGRAL DO VOLUME DE CONTROLE (ABORDAGEM INTEGRAL)
*(Páginas 6 a 8 do PDF)* [21]

### 3.1 O Conceito do Método Integral
A abordagem integral é um método aproximado que não exige a satisfação ponto a ponto das equações diferenciais no interior do escoamento [21]. Exige que as leis de conservação de massa e quantidade de movimento sejam satisfeitas globalmente sobre um Volume de Controle $AA'B'B$ de altura $\delta$, comprimento $L$ e largura $b$ [21].

### 3.2 Balanço de Massa nas Quatro Fronteiras do Volume de Controle
Analisando as quatro fronteiras do retângulo $AA'B'B$ [21]:
1. **Fronteira $AA'$ (Entrada):** $\dot{m}_{AA'} = -\rho (\delta b) V_0$ (sinal negativo indica entrada de massa na superfície de controle, $\rho \vec{V} \cdot d\vec{A} < 0$) [22].
2. **Fronteira $AB$ (Parede Sólida):** $\dot{m}_{AB} = 0$ (impermeabilidade) [22].
3. **Fronteira $BB'$ (Saída com Perfil $u(y)$):** $\dot{m}_{BB'} = +\rho b \int_0^\delta u(y) dy$ [22, 23].
4. **Fronteira $A'B'$ (Topo):** Pelo balanço total ($\sum \dot{m} = 0$), a vazão que escapa pelo topo é [23]:
   $$\dot{m}_{A'B'} = \rho (\delta b) V_0 - \rho b \int_0^\delta u(y) dy > 0$$

### 3.3 Balanço de Quantidade de Movimento e Sinal das Forças
Aplicando a 2ª Lei de Newton em regime permanente na direção $x$ [23]:
$$\sum F_x = \int_{CS} \rho u (\vec{V} \cdot d\vec{A})$$

Somando os fluxos de quantidade de movimento das quatro fronteiras [24]:
- $AA'$: $-\rho (\delta b) V_0^2$ [24]
- $AB$: $0$ [24]
- $BB'$: $+\rho b \int_0^\delta u^2(y) dy$ [24]
- $A'B'$ (com velocidade longitudinal $V_0$): $+V_0 \dot{m}_{A'B'} = \rho (\delta b) V_0^2 - \rho b V_0 \int_0^\delta u(y) dy$ [24]

Somando os fluxos líquidos obtém-se a força de reação da placa sobre o fluido [24]:
$$\vec{F}_{\text{placa}\to\text{fluido}} = -\rho b \int_0^\delta u(V_0 - u) dy \,\, \hat{i}$$
- **Explicação Física do Sinal:** O sinal negativo indica que a placa aplica uma força de retardo no fluido na direção $-x$ para compensar a perda de quantidade de movimento [24]. Pela Terceira Lei de Newton (ação e reação), a força de atrito exercida pelo fluido sobre a placa (arrasto friccional do casco) possui o mesmo módulo e sentido oposto ($+x$):
  $$\vec{F}_{\text{fluido}\to\text{placa}} = +\rho b \int_0^\delta u(V_0 - u) dy \,\, \hat{i}$$

### 3.4 Perfil Parabólico vs. Convenção Formal de $\delta$
Aproxima-se o perfil $u(y)$ por uma função polinomial $u(y) = a y^2 + b y + c$ [25].
- *Distinção Crítica:* No método integral, adota-se $u(\delta) = V_0$ e $\partial u/\partial y|_{y=\delta} = 0$ como condições matemáticas simplificadoras de contorno no topo do volume de controle [25]. Isso difere da convenção física e experimental formal de espessura de camada limite ($u(\delta) = 0,99 V_0$) [21, 36], pois o perfil assintótico real só atinge $V_0$ rigorosamente em $y \to \infty$.

Aplicando as 3 condições de contorno em $u(y) = a y^2 + b y + c$ [25]:
1. $y=0 \implies u(0) = 0 \implies c = 0$ [25]
2. $y=\delta \implies u(\delta) = V_0 \implies a\delta^2 + b\delta = V_0$ [25]
3. $y=\delta \implies \left.\frac{\partial u}{\partial y}\right|_{y=\delta} = 0 \implies 2a\delta + b = 0 \implies b = -2a\delta$ [25]

Substituindo $b$ na equação (2) obtém-se $a = -\frac{V_0}{\delta^2}$ e $b = \frac{2V_0}{\delta}$, resultando em:
$$\frac{u(y)}{V_0} = 2\left(\frac{y}{\delta}\right) - \left(\frac{y}{\delta}\right)^2$$

---

## SEÇÃO IV: VISUALIZAÇÃO DE ESCOAMENTOS E FUNÇÃO DE CORRENTE (2D)
*(Páginas 8 a 10 do PDF)* [28]

### 4.1 Linhas de Corrente e Notação Tridimensional (Pág. 9)
As **linhas de corrente** (*streamlines*) são famílias de curvas tangentes ao vetor velocidade $\vec{V}$ em cada ponto [28].
- Para o escoamento **bidimensional (2D)** no plano $xy$: $v dx - u dy = 0$ [29].
- Para o escoamento **tridimensional (3D)** genérico, conforme registrado na Página 9 do PDF:
  $$w dy - v dz = 0, \quad u dz - w dx = 0, \quad v dx - u dy = 0 \iff \vec{V} \times d\vec{s} = 0 \iff \frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$$

### 4.2 Definição da Função de Corrente $\psi(x,y)$
Para escoamentos bidimensionais e incompressíveis, define-se a função escalar $\psi(x,y)$ [29]:
$$u = \frac{\partial \psi}{\partial y} \quad \text{e} \quad v = -\frac{\partial \psi}{\partial x}$$

### 4.3 Satisfação Automática da Continuidade
Substituindo $\psi$ na Equação da Continuidade 2D [29]:
$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = \frac{\partial^2 \psi}{\partial x \partial y} - \frac{\partial^2 \psi}{\partial y \partial x} \equiv 0$$
O uso de $\psi$ garante a conservação de massa automaticamente sem resolver a equação de continuidade [29, 30].

---

## SEÇÃO V: SOLUÇÃO EXATA DE BLASIUS PARA A CAMADA LIMITE LAMINAR
*(Páginas 10 a 18 do PDF)* [26]

### 5.1 Hipótese de Semelhança de Perfis e Limitação Teórica (Pág. 10)
Blasius (1907) resolveu as equações de Prandtl para placa plana assumindo a **hipótese de semelhança dos perfis de velocidade** [26, 31].
- **Limitação Teórica:** Blasius assumiu inicialmente que o escoamento potencial externo não sofria qualquer alteração [27]. Contudo, devido ao desaceleramento na camada limite, ocorre um pequeno deslocamento de massa na direção normal $y$ para fora da camada limite [27].

Define-se a variável adimensional de similaridade $\eta$ e a função de corrente $\psi$ [33]:
$$\eta = y \sqrt{\frac{V_0}{\nu x}} \quad \text{e} \quad \psi(x,\eta) = \sqrt{\nu x V_0} \cdot f(\eta)$$

### 5.2 Componentes de Velocidade e Derivadas
Diferenciando $\psi$ usando a regra da cadeia ($\frac{\partial \eta}{\partial y} = \sqrt{\frac{V_0}{\nu x}}$ e $\frac{\partial \eta}{\partial x} = -\frac{\eta}{2x}$) [34]:
$$u = V_0 f'(\eta), \quad v = \frac{1}{2}\sqrt{\frac{\nu V_0}{x}} (\eta f' - f)$$
$$\frac{\partial u}{\partial x} = -\frac{V_0 \eta}{2x} f''(\eta), \quad \frac{\partial u}{\partial y} = V_0 \sqrt{\frac{V_0}{\nu x}} f''(\eta), \quad \frac{\partial^2 u}{\partial y^2} = \frac{V_0^2}{\nu x} f'''(\eta)$$

### 5.3 A Equação Diferencial Ordinária (EDO) de Blasius
Substituindo na equação de quantidade de movimento de Prandtl ($u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = \nu \frac{\partial^2 u}{\partial y^2}$) e simplificando os termos [34, 35]:
$$f'''(\eta) + \frac{1}{2} f(\eta) f''(\eta) = 0$$

- *Esclarecimento Matemático:* Na Página 13 do PDF (passagem 35), o professor registra $2 f''' + f f'' = 0$ [35]. Trata-se da **mesmíssima equação diferencial**, obtida simplesmente multiplicando a EDO por $2$ [35].
- **Condições de Contorno de Blasius:** Em $\eta = 0 \implies f(0) = 0$ e $f'(0) = 0$; em $\eta \to \infty \implies f'(\infty) = 1$ [35].

### 5.4 Resultados Fundamentais de Blasius
Da integração numérica por *shooting method* [36]:
- Derivada na parede: $f''(0) = 0,332$ [36].
- Para $u = 0,99 V_0 \implies f'(\eta) = 0,99 \implies \eta \approx 5 \implies \delta(x) = \frac{5 x}{\sqrt{Re_x}}$ [36, 37].
- Tensão cisalhante local: $\tau_{w,x} = 0,332 \frac{\rho V_0^2}{\sqrt{Re_x}}$ [39].
- Coeficiente de fricção local: $c_{f,x} = \frac{0,664}{\sqrt{Re_x}} = 0,664 Re_x^{-1/2}$ [40].
- Coeficiente de resistência médio total: $C_F = \frac{1}{L} \int_0^L c_{f,x} dx = \frac{1,328}{\sqrt{Re_L}} = 1,328 Re_L^{-1/2}$ [40].

### 5.5 Validação Experimental de Satish Dhawan (1953)
Em 1953, no Caltech, Satish Dhawan realizou a primeira medição direta da força de atrito de parede em laboratório, confirmando com grande precisão a solução teórica de Blasius [38].

---

## SEÇÃO VI: TRANSIÇÃO LAMINAR-TURBULENTA E O NÚMERO DE REYNOLDS CRÍTICO
*(Páginas 18 a 20 do PDF)* [41]

### 6.1 Mecanismo e Valores Práticos do Reynolds Crítico
O ponto de transição é caracterizado pelo Número de Reynolds Crítico ($Re_{cr} = \frac{\rho V_0 x_{cr}}{\mu}$) [41, 42]:
- **Condições Ideais de Laboratório (Novo PNA):** $Re_{cr} \approx 3 \times 10^6$ [41].
- **Valor Prático em Engenharias e Hidrodinâmica:** $Re_{cr} \approx 5 \times 10^5$ [42].
- **Valor Histórico de Blasius:** $Re_{cr} \approx 4,5 \times 10^5$ [42].

---

## SEÇÃO VII: EQUAÇÕES MÉDIAS DE REYNOLDS (RANS) PARA A CAMADA LIMITE TURBULENTA
*(Páginas 20 a 29 do PDF)* [44]

### 7.1 A Decomposição de Reynolds e Exceção para Forças de Pico
Decompõe-se o escoamento em valor médio e flutuação: $u = \bar{u} + u'$, $v = \bar{v} + v'$, $p = \bar{p} + p'$ [45].
- **Exceção da Média RANS (Pág. 21):** O professor ressalta que em problemas onde o valor máximo instantâneo da força é o fator determinante — como em **rupturas estruturais** ou **cavitação** —, o uso de médias RANS é inadequado, devendo-se utilizar as forças picos extremas.

### 7.2 Passagem Algébrica da Aceleração Convectiva em 2D
Para escrever a aceleração convectiva na forma conservativa de fluxo (divergente), aplica-se a regra do produto para derivadas:
$$\frac{\partial (u^2)}{\partial x} = u \frac{\partial u}{\partial x} + u \frac{\partial u}{\partial x} = 2u \frac{\partial u}{\partial x}$$
$$\frac{\partial (uv)}{\partial y} = u \frac{\partial v}{\partial y} + v \frac{\partial u}{\partial y}$$

Somando os dois termos e reagrupando:
$$\frac{\partial (u^2)}{\partial x} + \frac{\partial (uv)}{\partial y} = u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + u \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \right)$$

Pela Equação da Continuidade para escoamento incompressível 2D ($\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0$), o último termo anula-se rigorosamente:
$$u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = \frac{\partial (u^2)}{\partial x} + \frac{\partial (uv)}{\partial y}$$

Aplicando a decomposição de Reynolds e a média temporal sobre a forma divergente, surgem os **tensores de tensão de Reynolds** ($-\rho \overline{u'v'}$), gerando o problema do fechamento da turbulência (6 incógnitas e 3 equações) [46, 47, 55].

---

## SEÇÃO VIII: ESTRUTURA DA CAMADA LIMITE TURBULENTA E LEIS DA PAREDE
*(Páginas 29 a 48 do PDF)* [50]

### 8.1 Proporções Físicas e Escalas da Camada Limite Turbulenta
Define-se a velocidade de atrito $u_\tau = \sqrt{\frac{\tau_w}{\rho}}$ [55, 82] e as variáveis de parede $u^+ = \frac{\bar{u}}{u_\tau}$ e $y^+ = \frac{y u_\tau}{\nu}$ [61, 75, 76].

As proporções físicas aproximadas reportadas na apostila são [59, 60, 63]:
1. **Subcamada Viscosa ($y^+ < 5$):** Ocupa cerca de **1% de $\delta$** [59]. Solução linear de G. I. Taylor (1916): $u^+ = y^+$ [62].
2. **Subcamada Viscosa + Transição ($y^+ < 30$):** Ocupa cerca de **5% de $\delta$** [60].
3. **Região Interna (*Inner Layer*):** Ocupa cerca de **15% de $\delta$**.
4. **Camada Logarítmica de Sobreposição ($30 < y^+$ e $y/\delta < 0,15$):** Ocupa cerca de **20% de $\delta$** [63, 93].
5. **Região Externa (*Outer Layer / Wake Region*):** Ocupa os **85% restantes de $\delta$**.

### 8.2 Dedução Teórica de Prandtl vs. Ajuste Empírico de Monin & Yaglom
- **Dedução Teórica de Prandtl (1925) via Comprimento de Mistura ($l = k y$, com $k=0,41$):** [65, 72]
  $$\tau_w = \rho (k y)^2 \left(\frac{d\bar{u}}{dy}\right)^2 \implies u_\tau = k y \frac{d\bar{u}}{dy} \implies u^+ = \frac{1}{k} \ln y^+ + C_1$$
  Tomando $k = 0,41 \implies 1/k \approx 2,439$ e constante teórica de parede lisa $A = 5,0$ [75]:
  $$u^+ = 2,439 \ln y^+ + 5,0$$
- **Ajuste Empírico de Monin & Yaglom (1971):** [92, 93]
  Ajuste estatístico experimental sobre dados de Nikuradse, Klebanoff e Schultz-Grunow [93]:
  $$u^+ = 2,5 \ln y^+ + 5,1 \quad (\text{para } y^+ > 30)$$
  $$\frac{V_0 - \bar{u}}{u_\tau} = -2,5 \ln\left(\frac{y}{\delta}\right) + 2,35 \quad (\text{para } y/\delta < 0,15)$$

---

## SEÇÃO IX: PARÂMETROS INTEGRAIS E EQUAÇÃO DO MOMENTO DE VON KÁRMÁN
*(Páginas 48 a 53 do PDF)* [95]

### 9.1 Espessura de Deslocamento ($\delta^*$) e Quantidade de Movimento ($\theta$)
$$\delta^* = \int_0^\infty \left( 1 - \frac{\bar{u}}{V_0} \right) dy \quad \text{e} \quad \theta = \int_0^\infty \frac{\bar{u}}{V_0} \left( 1 - \frac{\bar{u}}{V_0} \right) dy$$

### 9.2 Integração por Partes da Velocidade Normal $v(y)$
Pela continuidade, $v(y) = -\int_0^y \frac{\partial u}{\partial x} dy'$. Na integração da equação da quantidade de movimento, aplica-se a integração por partes ao termo com $v$ [98]:
$$\int_0^\delta v \frac{\partial u}{\partial y} dy = \left[ v u \right]_0^\delta - \int_0^\delta u \frac{\partial v}{\partial y} dy = -V_0 \int_0^\delta \frac{\partial u}{\partial x} dy + \int_0^\delta u \frac{\partial u}{\partial x} dy$$

Resultando na **Equação do Momento Integral de Von Kármán para placa plana ($dp/dx = 0$):** [99, 100]
$$\frac{\tau_w}{\rho V_0^2} = \frac{d\theta}{dx} \implies c_{f,x} = 2 \frac{d\theta}{dx}$$

---

## SEÇÃO X: RESISTÊNCIA FRICCIONAL TURBULENTA E SOLUÇÃO DE PRANDTL
*(Páginas 53 a 58 do PDF)* [100]

### 10.1 Dedução com a Lei da $1/7$ Potência
Prandtl combinou $c_{f,x} = 2 d\theta/dx$ com a lei da $1/7$ potência ($\frac{\bar{u}}{V_0} = (y/\delta)^{1/7}$) [102, 103, 104]:
1. Cálculo de $\theta$: $\theta = \frac{7}{72} \delta \implies \frac{d\theta}{dx} = \frac{7}{72} \frac{d\delta}{dx}$ [103].
2. Igualando à fórmula empírica local para a faixa $5 \cdot 10^5 < Re_x < 10^7$ ($c_{f,x} = 0,046 \left( \frac{\nu}{V_0 \delta} \right)^{1/4}$) [102, 104]:
   $$\frac{7}{36} \frac{d\delta}{dx} = 0,046 \left( \frac{\nu}{V_0 \delta} \right)^{1/4} \implies \delta^{1/4} d\delta = 0,23657 \left( \frac{\nu}{V_0} \right)^{1/4} dx$$
3. Integrando em $x$ obtém-se os coeficientes numéricos precisos e arredondados [105, 106, 107]:
   $$\delta(x) = 0,3773 \frac{x}{Re_x^{1/5}} \approx \frac{0,38 x}{Re_x^{1/5}}$$
   $$c_{f,x} = 0,58693 Re_x^{-1/5} \approx \frac{0,587}{Re_x^{1/5}}$$
   $$C_F = \frac{1}{L} \int_0^L c_{f,x} dx = 0,7336 Re_L^{-1/5} \approx \frac{0,734}{Re_L^{1/5}}$$

- **Condição de Validade:** Válido estritamente para $Re_L < 10^7$ devido ao uso da lei $1/7$ (insuficiente para navios reais $Re \sim 10^8 - 10^9$) [105, 107].

---

## SEÇÃO XI: FORMULAÇÃO DA PLACA PLANA DE SCHOENHERR (1932) E LINHA ATTC-1947
*(Páginas 58 a 63 do PDF)* [108]

### 11.1 Equação Implícita e Fórmula Explícita Prática (Pág. 61)
Karl Schoenherr (1932) derivou a formulação implícita baseada na lei logarítmica [108, 109]:
$$\frac{0,24213}{\sqrt{C_F}} = \log_{10} \left( Re_L \cdot C_F \right) \quad \text{ou} \quad \frac{0,242}{\sqrt{C_F}} = \log_{10} \left( Re_L \cdot C_F \right)$$

- **Fórmula Explícita Prática para Estimativas Preliminares (Pág. 61):** [111]
  $$C_F = \frac{1}{\left( 3,5 \log_{10}(Re_L) - 5,96 \right)^2}$$

### 11.2 ATTC-1947 e Adicional de Rugosidade ($\Delta C_F$)
Adotada em 1947 pela *American Towing Tank Conference*, utilizando a constante $\Delta C_F = 0,0004$ para representar a rugosidade do casco do navio em relação ao modelo [111]:
$$C_{\text{F, navio}} = C_{\text{F, Schoenherr}} + 0,0004$$

---

## SEÇÃO XII: LINHA DE CORRELAÇÃO MODELO-NAVIO ITTC-1957 E MÉTODOS MODERNOS
*(Páginas 63 a 77 do PDF)* [112]

### 12.1 Linhas de Hughes (1954) e ITTC-1957
- **Linha 2D de Placa Plana de Hughes (1954):** [112, 113]
  $$C_F = \frac{0,066}{\left( \log_{10} Re - 2,03 \right)^2}$$
- **Linha de Correlação Modelo-Navio ITTC-1957:** [112, 113]
  $$C_F = \frac{0,075}{\left( \log_{10} Re - 2 \right)^2}$$

- *Análise da Relação ITTC-1957 vs. Hughes:* A linha ITTC-1957 incorporou os efeitos do arrasto de forma do casco adicionando $12\%$ no numerador da fórmula de Hughes ($0,066 \times 1,12 = 0,07392 \approx 0,075$) **e também alterou o denominador de $(\log_{10} Re - 2,03)^2$ para $(\log_{10} Re - 2)^2$** [113]. Portanto, a linha ITTC-1957 não é estritamente $12\%$ maior que a de Hughes em todos os valores de $Re$, apresentando elevação pronunciada em baixos números de Reynolds para corrigir a superestimativa de potência que ocorria em modelos pequenos ao usar Schoenherr [114].

### 12.2 Fórmula de Granville e Ressalva Crítica do Professor
- **Fórmula de Granville para a popa ($x=L$):** [113]
  $$c_{f,L} = \frac{C_F}{1 - \frac{1}{k} \sqrt{\frac{C_F}{2}}} = \frac{C_F}{1 - 2,439 \sqrt{\frac{C_F}{2}}} \quad (\text{com } k = 0,41)$$
- **Ressalva Fundamental do Professor na Apostila (Pág. 77):** Nunca existiu, nem no ITTC nem na ATTC, nenhuma pretensão de que essas fórmulas representem a força friccional real (cisalhante tangencial) do casco 3D de um navio [114]. Elas são **linhas de correlação pragmáticas convencionadas internacionalmente** para permitir a extrapolação padronizada entre modelo e navio [112, 114]. A tendência futura reside na **Dinâmica dos Fluidos Computacional (CFD)** para solução RANS 3D direta no casco.

---

## COMPÊNDIO DE EQUAÇÕES IMPORTANTES, SÍMBOLOS E APLICAÇÕES

| Equação | Símbolos e Parâmetros | Condições de Aplicação / Validade | Páginas de Origem |
| :--- | :--- | :--- | :---: |
| $\tau_w = \mu \left.\frac{\partial u}{\partial y}\right|_{y=0}$ | $\tau_w$: tensão de parede; $\mu$: viscosidade; $u$: velocidade. | Fluido newtoniano na parede. | Pág. 1 [1] |
| $c_{f,x} = \frac{\tau_w}{\frac{1}{2} \rho V_0^2}$ | $c_{f,x}$: coef. fricção local; $\rho$: densidade; $V_0$: vel. livre. | Adimensionalização da tensão local. | Pág. 1 [3] |
| $O(\delta/L) = O(1/\sqrt{Re_L})$ | $\delta$: espessura; $L$: comprimento; $Re_L$: Reynolds. | Ordem de grandeza da camada limite laminar. | Pág. 5 [14] |
| $\vec{V} \times d\vec{s} = 0 \iff \frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$ | $\vec{V}$: vetor velocidade; $d\vec{s}$: elemento de linha. | Equação diferencial das linhas de corrente 3D. | Pág. 9 |
| $f''' + \frac{1}{2} f f'' = 0 \iff 2f''' + ff'' = 0$ | $f(\eta)$: função corrente; $\eta = y\sqrt{V_0/\nu x}$. | EDO de Blasius (placa plana laminar). | Págs. 12–13 [34, 35] |
| $\delta(x) = \frac{5 x}{\sqrt{Re_x}}$ | $\delta$: espessura laminar ($u=0,99 V_0$). | Solução de Blasius em placa plana. | Pág. 14 [37] |
| $c_{f,x} = \frac{0,664}{\sqrt{Re_x}}, \ C_F = \frac{1,328}{\sqrt{Re_L}}$ | $c_{f,x}$: coef. local; $C_F$: coef. médio total laminar. | Fricção em placa plana laminar. | Págs. 15–16 [40] |
| $u^+ = y^+$ | $u^+ = \bar{u}/u_\tau$; $y^+ = y u_\tau / \nu$. | Subcamada viscosa turbulenta ($y^+ < 5$). | Pág. 32 [62] |
| $u^+ = 2,439 \ln y^+ + 5,0$ | $k = 0,41$ (Von Kármán); $A = 5,0$ (parede lisa). | Dedução teórica da lei logarítmica de Prandtl. | Pág. 41 [75] |
| $u^+ = 2,5 \ln y^+ + 5,1$ | Monin & Yaglom (1971). | Ajuste empírico experimental ($y^+ > 30$). | Pág. 47 [93] |
| $c_{f,x} = 2 \frac{d\theta}{dx}$ | $c_{f,x}$: coef. local; $\theta$: espessura de movimento. | Equação do momento de Von Kármán ($dp/dx=0$). | Pág. 53 [100] |
| $\delta(x) = \frac{0,38 x}{Re_x^{1/5}}, \ C_F = \frac{0,734}{Re_L^{1/5}}$ | $\delta$: espessura; $C_F$: coef. total (Prandtl). | Camada limite turbulenta (lei $1/7$, $Re_L < 10^7$). | Págs. 56–57 [105, 107] |
| $\frac{0,24213}{\sqrt{C_F}} = \log_{10}(Re_L C_F)$ | $C_F$: coef. total implícito de Schoenherr. | Linha ATTC-1947 ($10^5 < Re < 10^9$). | Pág. 59 [109] |
| $C_F = \frac{1}{(3,5 \log_{10}(Re_L) - 5,96)^2}$ | $C_F$: coef. explícito de Schoenherr. | Estimativas preliminares de potência. | Pág. 61 [111] |
| $C_F = \frac{0,075}{(\log_{10} Re_L - 2)^2}$ | $C_F$: coef. de correlação ITTC-1957. | Padrão internacional modelo-navio. | Pág. 64 [113] |

---

## PERGUNTAS INTEGRADORAS DA DISCIPLINA

**PI1. Como se conecta a solução teórica de Blasius (1907) para placa plana laminar com a formulação de correlação ITTC-1957 utilizada no projeto de navios reais?**
> **Resposta:** A solução de Blasius demonstrou que o coeficiente de resistência $C_F$ depende do Número de Reynolds ($Re$) [7, 40]. Isso permitiu superar os métodos empíricos de Froude de 1864 e buscar linhas universais de atrito $C_F(Re)$ [7]. Como a solução de Blasius aplica-se apenas ao regime laminar [39], derivaram-se linhas para o regime turbulento [100, 108]. A linha ITTC-1957 representa a aplicação desse conceito: uma linha de correlação modelo-navio que combina a física do escoamento $C_F(Re)$ com uma elevação de $12\%$ no numerador e ajuste no denominador para englobar o efeito de forma do casco 3D do navio e corrigir a escala de modelos pequenos [113, 114].

**PI2. Explique como o conceito de espessura de quantidade de movimento ($\theta$) de Von Kármán permitiu a Prandtl derivar a resistência friccional turbulenta $C_F = 0,734 Re_L^{-1/5}$.**
> **Resposta:** Von Kármán demonstrou que a tensão cisalhante na parede relaciona-se com a taxa de variação da quantidade de movimento ($c_{f,x} = 2 d\theta/dx$) [100, 104]. Prandtl aplicou essa relação assumindo o perfil turbulento pela lei da $1/7$ potência ($\bar{u}/V_0 = (y/\delta)^{1/7}$), obtendo a fração $\theta = \frac{7}{72}\delta$ [103]. Igualando $2 d\theta/dx$ à expressão empírica da fricção e integrando em $x$, Prandtl obteve a espessura turbulenta $\delta(x) = 0,3773 x Re_x^{-1/5} \approx 0,38 x Re_x^{-1/5}$ e o coeficiente global $C_F = 0,7336 Re_L^{-1/5} \approx 0,734 Re_L^{-1/5}$ [105, 107].
