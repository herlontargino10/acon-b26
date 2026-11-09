# Gabarito Comentado — Simulado P2 de Hidrodinâmica

**Nível:** Fácil a Médio  
Este gabarito apresenta as respostas corretas, as fundamentações teóricas baseadas no resumo da disciplina e a explicação dos conceitos físicos envolvidos.

---

## 1. Múltipla escolha

| Questão | Resposta | Assunto Central e Respaldo no Resumo |
|:---:|:---:|:---|
| **1** | **B** | Hipótese de Prandtl (1904) e superação do Paradoxo de d'Alembert (Seção I, itens 1.1 e 1.2). |
| **2** | **A** | Simplificações de Navier-Stokes: difusão transversal dominante e $\partial p/\partial y \approx 0$ (Seção II, itens 2.3 e 2.4). |
| **3** | **A** | Balanço de forças no método integral e Terceira Lei de Newton (Seção III, itens 3.1 a 3.3). |
| **4** | **A** | Significado físico de $\delta^*$ (déficit de vazão) e $\theta$ (déficit de momento) (Seção IX, itens 9.1 e 9.2). |
| **5** | **A** | Finalidade de Granville na popa e caráter pragmático da linha ITTC-1957 (Seções XI e XII). |

### Justificativas didáticas detalhadas:

#### Questão 1 — B) Divisão do escoamento segundo Prandtl
* **Por que está correta:** Ludwig Prandtl (1904) superou o Paradoxo de d'Alembert mostrando que os efeitos do atrito viscoso não se espalham de forma homogênea por todo o fluido: eles ficam confinados a uma delgada camada limite colada à parede sólida, onde as forças viscosas e inerciais se equilibram em ordem de grandeza ($O(1)$). Fora dessa região, o escoamento comporta-se como potencial (invíscido).
* **Por que as demais alternativas estão incorretas:**
  * **A:** A viscosidade não afeta uniformemente todo o escoamento; longe do corpo, o escoamento potencial continua válido.
  * **C:** Fluidos reais sofrem arrasto devido à tensão de cisalhamento não nula na parede sólida.
  * **D:** A pressão varia sobre o corpo (não é nula) e a velocidade varia no interior da camada limite.
  * **E:** A camada limite desenvolve-se sobre todas as superfícies molhadas pelo escoamento real.

#### Questão 2 — A) Simplificações físicas de Prandtl
* **Por que está correta:** Como a camada limite é muito delgada ($\delta \ll L$), os gradientes de velocidade na direção normal à parede são muito mais intensos do que os longitudinais. Isso torna a difusão viscosa longitudinal ($\partial^2 u/\partial x^2$) desprezível perante a difusão transversal ($\partial^2 u/\partial y^2$). Além disso, a análise na direção normal fornece $\partial p/\partial y \approx 0$, comprovando que a pressão é constante através da espessura da camada limite e imposta pelo escoamento potencial externo.
* **Por que as demais alternativas estão incorretas:**
  * **B:** Pela conservação da massa, a velocidade normal $v$ é muito menor que a velocidade livre $V_0$ ($v \sim O(\delta/L) \ll 1$).
  * **C:** A difusão longitudinal é o termo descartado por ser desprezível.
  * **D:** A pressão é praticamente uniforme ao longo da espessura da camada limite ($\partial p/\partial y \approx 0$).
  * **E:** Forças inerciais e viscosas mantêm a mesma ordem de grandeza na camada limite; os termos inerciais não são eliminados.

#### Questão 3 — A) Ação e reação no método integral
* **Por que está correta:** A integração do fluxo de quantidade de movimento mostra que a placa sólida exerce uma força negativa (retardadora) sobre o fluido, freando a corrente livre. Pela Terceira Lei de Newton (ação e reação), o fluido reage sobre a placa com uma força de igual módulo e sentido oposto ($+x$), que constitui o arrasto de atrito friccional sofrido pelo corpo.
* **Por que as demais alternativas estão incorretas:**
  * **B:** Como o fluido desacelera no interior da camada limite, parte da massa escapa pela fronteira superior do volume de controle ($\dot{m}_{topo} > 0$).
  * **C:** O método integral é aproximado e baseia-se em balanços globais, dispensando a resolução diferencial ponto a ponto.
  * **D:** A placa retarda o fluido (força em $-x$), e não o acelera.
  * **E:** O perfil parabólico é uma aproximação polinomial simplificada, e não a solução exata de Navier-Stokes.

#### Questão 4 — A) Significado físico de $\delta^*$ e $\theta$
* **Por que está correta:** A espessura de deslocamento $\delta^*$ representa a distância pela qual as linhas de corrente externas são empurradas para fora para compensar a perda de vazão de massa causada pela desaceleração viscosa junto à parede. Já a espessura de quantidade de movimento $\theta$ quantifica a perda total de fluxo de momento linear sofrida pelo escoamento.
* **Por que as demais alternativas estão incorretas:**
  * **B:** A espessura geométrica total é $\delta$, e a subcamada viscosa ocupa uma fração muito menor ($y^+ < 5$).
  * **C:** $\delta^*$ refere-se ao déficit de vazão de massa, e $\theta$ não indica separação.
  * **D:** Para qualquer perfil real de camada limite sobre placa plana, tem-se $\delta^* > \theta$.
  * **E:** Ambas dependem diretamente do perfil de velocidade e do número de Reynolds, não sendo propriedades puramente geométricas.

#### Questão 5 — A) Finalidade prática das formulações navais
* **Por que está correta:** A linha de correlação ITTC-1957 foi estabelecida como uma convenção internacional pragmática para transpor a resistência friccional medida em modelos de tanque para o navio em escala real. Já a fórmula de Granville foi deduzida especificamente para avaliar o coeficiente de atrito local na popa da embarcação ($x = L$), onde a camada limite é mais espessa.
* **Por que as demais alternativas estão incorretas:**
  * **B:** A formulação de Schoenherr foi deduzida para placas planas em regime turbulento.
  * **C:** Granville destina-se ao atrito de ré (popa, $x=L$), e não à resistência de ondas da proa.
  * **D:** A linha ITTC-1957 é uma convenção bidimensional equivalente de correlação, e não a medição física real do atrito no casco 3D.
  * **E:** Navios reais exigem a consideração da rugosidade do casco (como a margem $\Delta C_F = 0,0004$ da ATTC-1947).

---

## 2. Complete as lacunas

| Item | Resposta Esperada | Conceito Avaliado |
|:---:|:---|:---|
| **6.1** | **não escorregamento** (ou *no-slip* / aderência) | Condição cinemática em que as moléculas fluidas aderem à parede com velocidade relativa nula ($u=0$). |
| **6.2** | **tensão de cisalhamento na parede** (ou tensão cisalhante / $\tau_w$) | Força tangencial por unidade de área na parede calculada pela lei de Newton da viscosidade ($\mu \left.\frac{\partial u}{\partial y}\right|_{y=0}$). |
| **6.3** | **função de corrente** ($\psi$) | Função matemática escalar cujas derivadas fornecem $u = \partial\psi/\partial y$ e $v = -\partial\psi/\partial x$, satisfazendo identicamente a continuidade 2D. |
| **6.4** | **similaridade** (ou semelhança) | Variável adimensional $\eta = y\sqrt{V_0/(\nu x)}$ que reduz o sistema de equações diferenciais parciais a uma EDO ordinária. |
| **6.5** | **Satish Dhawan** | Pesquisador que realizou em laboratório (1953) a confirmação da teoria de Blasius por medição direta da tensão cisalhante de parede. |
| **6.6** | **$5 \times 10^5$** (ou $500.000$ / $5 \cdot 10^5$) | Valor comumente adotado na engenharia naval para o número de Reynolds crítico ($Re_{cr}$) no início da transição sobre placas lisas. |
| **6.7** | **tensão de Reynolds** (ou tensão turbulenta) | Termo adicional $-\rho\overline{u'v'}$ gerado pelas flutuações de velocidade que representa o transporte turbulento de quantidade de movimento. |
| **6.8** | **velocidade de atrito** ($u_\tau$) | Escala dinâmica de velocidade definida por $u_\tau = \sqrt{\tau_w/\rho}$, utilizada para adimensionalizar as variáveis de parede ($u^+$ e $y^+$). |
| **6.9** | **subcamada viscosa** | Região colada à parede sólida ($y^+ < 5$) onde a viscosidade molecular domina e o perfil é linear ($u^+ = y^+$). |
| **6.10** | **rugosidade** | Margem aditiva fixa $\Delta C_F = 0,0004$ introduzida pela conferência ATTC-1947 para representar o acabamento real do casco de aço. |

---

## 3. Verdadeiro ou falso

| Item | Gabarito | Justificativa Didática |
|:---:|:---:|:---|
| **7.1** | **V** | **Verdadeiro.** A solução de Blasius reduz o escoamento laminar permanente sobre placa plana à EDO $f''' + \frac{1}{2}ff'' = 0$ (ou $2f''' + ff'' = 0$), sendo governada na parede sólida pela impermeabilidade ($f(0)=0$) e não escorregamento ($f'(0)=0$). |
| **7.2** | **F** | **Falso.** A constante $5$ na expressão da espessura ($\delta = \frac{5x}{\sqrt{Re_x}}$) não indica onde a velocidade atinge 100% de $V_0$ (o que ocorreria apenas no infinito assintótico), mas sim a convenção prática onde $u = 0,99 V_0$ (99% da velocidade livre). |
| **7.3** | **V** | **Verdadeiro.** As linhas de corrente são curvas instantâneas tangentes ao vetor velocidade em cada ponto do espaço; no plano bidimensional satisfazem formalmente a equação diferencial $v\,dx - u\,dy = 0$. |
| **7.4** | **F** | **Falso.** Como as equações RANS trabalham com médias temporais, elas mascaram flutuações de alta frequência, sendo inadequadas para prever esforços extremos de pico instantâneo associados a cavitação e rupturas estruturais. |
| **7.5** | **V** | **Verdadeiro.** Na camada limite turbulenta sobre parede lisa, a subcamada viscosa localiza-se na faixa $y^+ < 5$, onde as tensões moleculares predominam sobre o transporte turbulento e a velocidade segue o perfil linear de Taylor $u^+ = y^+$. |
| **7.6** | **F** | **Falso.** A lei da potência $1/7$ de Prandtl tem limite estrito de validade em números de Reynolds moderados ($Re_L < 10^7$, escala de modelos de laboratório), sendo inadequada para extrapolação direta a navios reais ($10^8$ a $10^9$). |

**Sequência de Gabarito do V/F:** V – F – V – F – V – F.

---

## 4. Questão 8 — Cálculo: arrasto sobre chapa de madeira compensada

### Dados fornecidos:
* Chapa de compensado: $4 \times 8\text{ ft}$
* Comprimento no sentido do escoamento: $L = 2,44\text{ m}$ (dimensão de $8\text{ ft}$)
* Largura transversal da chapa: $b = 1,22\text{ m}$ (dimensão de $4\text{ ft}$)
* Velocidade de deslocamento: $V = 56\text{ km/h}$
* Propriedades do ar a $20\ ^\circ\text{C}$ e $1\text{ atm}$:
  * Massa específica: $\rho = 1,2\text{ kg/m}^3$
  * Viscosidade dinâmica: $\mu = 1,8 \times 10^{-5}\text{ kg/(m}\cdot\text{s)}$

---

### Resolução passo a passo:

#### Passo 1: Conversão da velocidade e cálculo do número de Reynolds

1. **Conversão da velocidade para m/s:**
   $$
   V = \frac{56}{3,6} \approx 15,56\text{ m/s} \quad (15,5556\text{ m/s})
   $$

2. **Cálculo do número de Reynolds no bordo de fuga ($x = L = 2,44\text{ m}$):**
   $$
   Re_L = \frac{\rho V L}{\mu} = \frac{1,2 \cdot 15,5556 \cdot 2,44}{1,8 \times 10^{-5}} = \frac{45,547}{1,8 \times 10^{-5}} \approx \mathbf{2,53 \times 10^6}
   $$

---

#### Passo 2: Item a) Espessura da camada limite no final da chapa ($\delta$)

Pela correlação de Blasius para a camada limite laminar:
$$
\delta = \frac{5 L}{\sqrt{Re_L}}
$$
Calculando a raiz quadrada de $Re_L$:
$$
\sqrt{Re_L} = \sqrt{2,53 \times 10^6} \approx 1590,6
$$
Substituindo os valores:
$$
\delta = \frac{5 \cdot 2,44}{1590,6} = \frac{12,2}{1590,6} \approx 0,00767\text{ m} \approx \mathbf{7,67\text{ mm}}
$$

---

#### Passo 3: Parâmetros de área e pressão dinâmica

1. **Área total de atrito (considerando ambas as faces da chapa, superior e inferior):**
   $$
   A_{\text{total}} = 2 \cdot (b \cdot L) = 2 \cdot (1,22 \cdot 2,44) = 5,9536\text{ m}^2
   $$

2. **Pressão dinâmica da corrente livre:**
   $$
   q = \frac{1}{2}\rho V^2 = \frac{1}{2} \cdot 1,2 \cdot (15,5556)^2 = 0,6 \cdot 241,975 \approx 145,2\text{ Pa}
   $$

---

#### Passo 4: Item b) Força de arrasto considerando escoamento laminar ($F_L$)

1. **Coeficiente de atrito médio laminar de Blasius:**
   $$
   C_{f,L} = \frac{1,328}{\sqrt{Re_L}} = \frac{1,328}{1590,6} \approx \mathbf{0,000835}
   $$

2. **Força total de arrasto laminar:**
   $$
   F_L = C_{f,L} \cdot q \cdot A_{\text{total}} = 0,000835 \cdot 145,2\text{ Pa} \cdot 5,9536\text{ m}^2 \approx \mathbf{0,72\text{ N}}
   $$

---

#### Passo 5: Item c) Força de arrasto considerando escoamento turbulento ($F_T$) e comparação

1. **Coeficiente de atrito médio turbulento (madeira lisa):**
   $$
   C_{f,T} = \frac{0,074}{Re_L^{1/5}} = \frac{0,074}{Re_L^{0,2}}
   $$
   Calculando $Re_L^{0,2}$:
   $$
   (2,53 \times 10^6)^{0,2} \approx 19,08
   $$
   Portanto:
   $$
   C_{f,T} = \frac{0,074}{19,08} \approx \mathbf{0,00388}
   $$

2. **Força total de arrasto turbulento:**
   $$
   F_T = C_{f,T} \cdot q \cdot A_{\text{total}} = 0,00388 \cdot 145,2\text{ Pa} \cdot 5,9536\text{ m}^2 \approx \mathbf{3,36\text{ N}}
   $$
   *(Nota: com o arredondamento intermediário do professor, $C_{f,T} \approx 0,00377 \implies F_T \approx 3,3\text{ N}$).*

3. **Comparação entre os resultados:**
   $$
   \frac{F_T}{F_L} = \frac{3,36\text{ N}}{0,72\text{ N}} \approx \mathbf{4,65\text{ vezes}}
   $$
   **Conclusão física:** O arrasto no regime turbulento é aproximadamente **4,6 a 4,7 vezes superior** ao arrasto laminar. Isso ocorre porque o intenso transporte de quantidade de movimento gerado pelas flutuações turbulentas ($-\rho\overline{u'v'}$) energiza o fluido próximo à parede, gerando um gradiente de velocidade muito mais íngreme ($\left.\frac{\partial\bar{u}}{\partial y}\right|_{y=0,\text{turb}} \gg \left.\frac{\partial u}{\partial y}\right|_{y=0,\text{lam}}$) e, consequentemente, uma tensão cisalhante de atrito muito maior.

---

### Resumo das respostas numéricas:

| Grandeza Calculada | Símbolo | Fórmula | Valor | Unidade |
|:---|:---:|:---:|:---:|:---:|
| Velocidade de escoamento | $V$ | $56 / 3,6$ | $15,56$ | $\text{m/s}$ |
| Número de Reynolds | $Re_L$ | $\frac{\rho V L}{\mu}$ | $2,53 \times 10^6$ | Adimensional |
| Espessura da camada limite | $\delta$ | $\frac{5L}{\sqrt{Re_L}}$ | $7,67$ | $\text{mm}$ |
| Coeficiente de atrito laminar | $C_{f,L}$ | $\frac{1,328}{\sqrt{Re_L}}$ | $0,000835$ | Adimensional |
| Força de arrasto laminar (2 faces) | $F_L$ | $C_{f,L} \cdot q \cdot A$ | $0,72$ | $\text{N}$ |
| Coeficiente de atrito turbulento | $C_{f,T}$ | $\frac{0,074}{Re_L^{0,2}}$ | $0,00388$ *(ou $0,00377$)* | Adimensional |
| Força de arrasto turbulento (2 faces) | $F_T$ | $C_{f,T} \cdot q \cdot A$ | $3,36$ *(ou $3,30$)* | $\text{N}$ |
| Razão entre os arrastos | $F_T / F_L$ | $3,36 / 0,72$ | $\approx 4,65$ | Vezes |

---

### Como calcular na calculadora científica:

* **Notação científica ($1,8 \times 10^{-5}$):** Digite `1.8` $\rightarrow$ Tecla `EXP` (ou `EE`) $\rightarrow$ Tecla `+/-` $\rightarrow$ `5`.
* **Raiz quadrada ($\sqrt{2,53 \times 10^6}$):** Digite `√` $\rightarrow$ `(` $\rightarrow$ `2.53` `EXP` `6` $\rightarrow$ `)` $\rightarrow$ `=` $\implies \mathbf{1590,6}$.
* **Potência fracionária turbulenta ($Re_L^{0,2}$):** Digite `(` $\rightarrow$ `2.53` `EXP` `6` $\rightarrow$ `)` $\rightarrow$ Tecla `xʸ` (ou `^`) $\rightarrow$ `0.2` $\rightarrow$ `=` $\implies \mathbf{19,08}$.
* **Sequência mnemônica:**  
  $$\mathbf{REYNOLDS \longrightarrow ESPESSURA \longrightarrow COEFICIENTES \longrightarrow FORÇAS \longrightarrow RAZÃO}$$
