# Gabarito Comentado — Simulado P2 de Hidrodinâmica

Este gabarito apresenta as respostas corretas, as justificativas fundamentadas no resumo da disciplina e a explicação dos conceitos físicos envolvidos.

---

## 1. Múltipla escolha

| Questão | Resposta | Assunto Central e Respaldo no Resumo |
|:---:|:---:|:---|
| **1** | **B** | Hipótese de Prandtl (1904) e comparativo de gradientes na parede (Seção I, itens 1.1, 1.2 e 1.4). |
| **2** | **C** | Simplificação de Navier-Stokes, difusão longitudinal e acoplamento com Bernoulli (Seção II, itens 2.3 e 2.4). |
| **3** | **C** | Balanço de quantidade de movimento no volume de controle e perfil parabólico (Seção III, itens 3.1 a 3.4). |
| **4** | **C** | Significado físico de $\delta^*$ e $\theta$ e justificativa do fator 2 em Von Kármán (Seção IX, itens 9.1 a 9.3). |
| **5** | **C** | Equação de Schoenherr ($0,24213$), Granville na popa e linha ITTC-1957 (Seções XI e XII). |

### Justificativas teóricas detalhadas:

#### Questão 1 — Alternativa B
* **Fundamentação teórica:** Ludwig Prandtl (1904) estabeleceu que a viscosidade atua de forma decisiva apenas em uma camada delgada junto à parede sólida onde os efeitos viscosos e inerciais possuem a mesma ordem de grandeza ($O(1)$), enquanto fora dela o escoamento comporta-se como potencial invíscido. Além disso, o perfil médio turbulento é mais "assentado" (uniforme no centro) e varia bruscamente junto à parede, gerando um gradiente de velocidade muito maior do que no escoamento laminar:
  $$\left. \frac{\partial u}{\partial y} \right|_{y=0, \text{lam}} < \left. \frac{\partial \bar{u}}{\partial y} \right|_{y=0, \text{turb}} \implies \tau_{w,\text{turb}} > \tau_{w,\text{lam}}$$
* **Análise dos distratores:**  
  * A é falsa: a viscosidade não atua uniformemente em todo o campo; fora da camada limite o escoamento potencial é válido.  
  * C é falsa: fluidos reais sofrem arrasto devido à tensão cisalhante na parede ($\tau_w \neq 0$).  
  * D é falsa: o gradiente laminar na parede é menor do que o turbulento, de modo que $\tau_{w,\text{lam}} < \tau_{w,\text{turb}}$.  
  * E é falsa: a espessura varia ao longo de $x$ e escala inversamente com $\sqrt{Re_x}$.

#### Questão 2 — Alternativa C
* **Fundamentação teórica:** A análise de escalas de Prandtl revela que:  
  1. O termo de difusão viscosa longitudinal ($\frac{1}{Re}\frac{\partial^2 u}{\partial x^2} \sim O(1/Re)$) é muito menor do que a difusão transversal ($\frac{1}{Re}\frac{\partial^2 u}{\partial y^2} \sim O(1)$), sendo eliminado na equação de quantidade de movimento em $x$.  
  2. Na direção normal ($y$), todos os termos são de ordem $O(\bar{\delta}) \ll 1$, resultando em $\partial p/\partial y \approx 0$, o que comprova que a variação de pressão através da espessura da camada limite é negligenciável e que a pressão interna é imposta pelo escoamento potencial externo ($p(x,y) \approx p_e(x)$).  
  3. No escoamento potencial externo, a Equação de Bernoulli estabelece que o gradiente longitudinal de pressão relaciona-se diretamente à aceleração da corrente livre: $-\partial p/\partial x = \rho V dV/dx$.
* **Análise dos distratores:**  
  * A é falsa: a difusão longitudinal é desprezada por ser muito menor que a transversal.  
  * B é falsa: pela equação da continuidade, $v^* \sim O(\delta/L) \ll 1$.  
  * D é falsa: a Equação de Bernoulli não se aplica no interior viscoso da camada limite.  
  * E é falsa: a pressão transversal é praticamente constante ($\partial p/\partial y \approx 0$).

#### Questão 3 — Alternativa C
* **Fundamentação teórica:** No método integral, a integração do fluxo de quantidade de movimento na direção $x$ fornece a força que a placa exerce sobre o fluido:
  $$\vec{F}_{\text{placa}\to\text{fluido}} = -\rho b \int_0^\delta u(V_0 - u)\,dy\,\hat{i}$$
  O sinal negativo indica retardo no fluido. Pela Terceira Lei de Newton (ação e reação), a força exercida pelo fluido sobre a placa (o arrasto friccional sofrido pelo corpo) possui o mesmo módulo e sentido oposto ($+x$). O perfil parabólico ($u/V_0 = 2(y/\delta) - (y/\delta)^2$) é uma aproximação polinomial que adota $u(\delta) = V_0$ e $\partial u/\partial y = 0$ como condições matemáticas simplificadoras de contorno no topo do volume de controle para permitir o fechamento analítico global.
* **Análise dos distratores:**  
  * A é falsa: devido à desaceleração do fluido no interior da camada limite, há vazão de massa que escapa pela fronteira superior ($\dot{m}_{A'B'} > 0$).  
  * B é falsa: a força sobre o fluido atua em sentido negativo (retarda o escoamento).  
  * D é falsa: o perfil parabólico é uma aproximação simplificada, e não uma solução exata.  
  * E é falsa: a condição $0,99 V_0$ é uma convenção física experimental, não sendo adotada no cálculo dos coeficientes do perfil parabólico no método integral.

#### Questão 4 — Alternativa C
* **Fundamentação teórica:**  
  * A espessura de deslocamento $\delta^* = \int_0^\infty (1 - \bar{u}/V_0) dy$ representa a distância física pela qual as linhas de corrente externas são defletidas para fora em virtude da redução de vazão de massa provocada pelo atrito.  
  * A espessura de quantidade de movimento $\theta = \int_0^\infty \frac{\bar{u}}{V_0}(1 - \frac{\bar{u}}{V_0}) dy$ quantifica a perda total de fluxo de quantidade de movimento linear no escoamento.  
  * A dedução de Von Kármán fornece diretamente $\frac{\tau_w}{\rho V_0^2} = \frac{d\theta}{dx}$. Como o coeficiente de fricção local é padronizado com a pressão dinâmica no denominador ($c_{f,x} = \frac{\tau_w}{\frac{1}{2}\rho V_0^2}$), o fator $1/2$ no denominador gera o fator multiplicativo 2:
  $$c_{f,x} = 2 \frac{\tau_w}{\rho V_0^2} = 2 \frac{d\theta}{dx}$$
* **Análise dos distratores:**  
  * A e B são falsas: o fator 2 não decorre de duas faces nem do grau de polinômio.  
  * D é falsa: para perfis reais, $\delta^* > \theta$.  
  * E é falsa: a equação aplica-se perfeitamente sobre placa plana lisa com $dp/dx = 0$.

#### Questão 5 — Alternativa C
* **Fundamentação teórica:**  
  * A equação implícita de Schoenherr ($\frac{0,24213}{\sqrt{C_F}} = \log_{10}(Re_L \cdot C_F)$) foi deduzida com base na lei logarítmica de parede para representar a resistência friccional de placas planas em regime turbulento.  
  * A fórmula de Granville para a popa ($x = L$) emprega a constante de Von Kármán $k = 0,41$ para estimar o coeficiente de atrito local especificamente na extremidade de ré ($c_{f,L}$) a partir do coeficiente global $C_F$.  
  * A linha ITTC-1957 incorporou os efeitos de forma elevando o numerador de Hughes em 12% ($0,066 \times 1,12 \approx 0,075$) e alterando o denominador para $(\log_{10}Re - 2)^2$ para compensar modelos pequenos. O professor ressalta que essas formulações são linhas de correlação pragmáticas convencionadas internacionalmente para extrapolação modelo-navio, e não a fricção física real do casco 3D.
* **Análise dos distratores:**  
  * A é falsa: Schoenherr é formulada para escoamento turbulento em placas planas.  
  * B é falsa: Granville aplica-se especificamente à popa ($x=L$), e não à proa ($x=0$).  
  * D é falsa: o denominador foi modificado (de $-2,03$ para $-2$), logo a elevação não é 12% em todos os $Re$.  
  * E é falsa: Granville fornece a fricção local na popa, não substituindo o cálculo global de resistência.

---

## 2. Complete as lacunas

| Item | Termo Correto | Justificativa Teórica e Respaldo no Resumo |
|:---:|:---|:---|
| **6.1** | **Não escorregamento** (ou *no-slip*) | Condição física em que as moléculas fluidas aderem à fronteira sólida com velocidade relativa nula ($u(y=0)=0$) (Seção I, item 1.3). |
| **6.2** | **Tensão de cisalhamento na parede** (ou tensão cisalhante) | Força tangencial por unidade de área calculada pela lei de Newton da viscosidade na superfície: $\tau_w = \mu \left.\frac{\partial u}{\partial y}\right\|_{y=0}$ (Seção I, item 1.3). |
| **6.3** | **Função de corrente** | Função escalar $\psi$ cujas derivadas cruzadas anulam identicamente a equação da continuidade 2D incompressível: $\frac{\partial^2\psi}{\partial x\partial y} - \frac{\partial^2\psi}{\partial y\partial x} \equiv 0$ (Seção IV, itens 4.2 e 4.3). |
| **6.4** | **Similaridade** (ou semelhança) | Variável adimensional $\eta = y\sqrt{V_0/(\nu x)}$ que reduz o sistema de equações diferenciais parciais a uma única EDO ordinária (Seção V, item 5.1). |
| **6.5** | **Satish Dhawan** | Pesquisador que realizou, em 1953, a validação em laboratório da teoria de Blasius por medição direta da força de atrito de parede (Seção V, item 5.5). |
| **6.6** | **$5 \times 10^5$** (ou **$5 \cdot 10^5$** / **500.000**) | O número de Reynolds crítico é definido por $Re_{cr} = \frac{\rho V_0 x_{cr}}{\mu}$, em que $\rho$ é a massa específica, $V_0$ é a velocidade da corrente livre, $x_{cr}$ é a posição longitudinal da transição e $\mu$ é a viscosidade dinâmica. Enquanto em condições ideais de laboratório com baixíssima turbulência esse parâmetro alcança cerca de $3 \times 10^6$ (e historicamente Blasius indicou $4,5 \times 10^5$), na prática da engenharia e hidrodinâmica naval adota-se comumente o valor de $5 \times 10^5$ (Seção VI, item 6.1). |
| **6.7** | **Tensão de Reynolds** (ou tensão turbulenta / tensão aparente de Reynolds) | Nas equações médias RANS, o termo adicional $-\rho\overline{u'v'}$ representa o transporte de quantidade de movimento provocado pelas flutuações turbulentas e introduz incógnitas que não podem ser determinadas apenas pelas equações médias de conservação, gerando o clássico problema de fechamento da turbulência (Seção VII, item 7.3). |
| **6.8** | **Velocidade de atrito** | Escala de velocidade de parede $u_\tau = \sqrt{\tau_w/\rho}$, que normaliza $u^+ = \bar{u}/u_\tau$ e $y^+ = y u_\tau / \nu$ (Seção VIII, item 8.1). |
| **6.9** | **Subcamada viscosa** | Região extremamente fina junto à parede ($y^+ < 5$) onde a viscosidade molecular impõe o perfil linear de Taylor $u^+ = y^+$ (Seção VIII, item 8.1). |
| **6.10** | **Rugosidade** | Margem adicional fixa $\Delta C_F = 0,0004$ introduzida na conferência ATTC-1947 para representar a rugosidade do casco real em relação ao modelo liso (Seção XI, item 11.2). |

---

## 3. Verdadeiro ou falso

| Item | Gabarito | Justificativa Teórica e Respaldo no Resumo |
|:---:|:---:|:---|
| **7.1** | **V** | **Verdadeiro.** A EDO de Blasius para placa plana laminar é expressa por $f''' + \frac{1}{2}ff'' = 0$ (ou $2f''' + ff'' = 0$), sendo submetida às condições de contorno de aderência na parede ($f(0)=0, f'(0)=0$) e velocidade livre no infinito ($f'(\infty)=1$) (Seção V, item 5.3). |
| **7.2** | **F** | **Falso.** O item contém erros conceituais estritos: (1) a constante $5$ na expressão $\delta = \frac{5x}{\sqrt{Re_x}}$ não corresponde a $u = V_0$ (atingida rigorosamente apenas no infinito assintótico), mas sim à convenção formal onde a velocidade atinge 99% da velocidade da corrente livre ($u = 0,99 V_0$); (2) o coeficiente médio total de atrito de toda a placa é $C_F = 1,328 Re_L^{-1/2}$, que equivale ao dobro de $0,664 Re_L^{-1/2}$ pela integração ao longo de $L$ (Seção V, itens 5.3 e 5.4). |
| **7.3** | **V** | **Verdadeiro.** As linhas de corrente são tangentes ao vetor velocidade em cada ponto; no plano bidimensional satisfazem $v dx - u dy = 0$, enquanto no espaço tridimensional a condição vetorial $\vec{V} \times d\vec{s} = \mathbf{0}$ assume a forma diferencial simétrica $\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$ (Seção IV, item 4.1). |
| **7.4** | **F** | **Falso.** A média temporal nas equações RANS filtra as flutuações, mascarando as forças extremas instantâneas. A apostila ressalta expressamente que em problemas onde o valor máximo instantâneo governa o fenômeno físico (como rupturas estruturais e cavitação), o emprego de RANS é inadequado (Seção VII, item 7.1). |
| **7.5** | **V** | **Verdadeiro.** A estrutura da camada limite turbulenta apresenta as delimitações aproximadas descritas na apostila: subcamada viscosa ($y^+ < 5$) ocupando cerca de 1% de $\delta$; subcamada viscosa somada à transição ($y^+ < 30$) ocupando cerca de 5% de $\delta$; região interna ocupando cerca de 15% de $\delta$; camada logarítmica de sobreposição ocupando cerca de 20% de $\delta$; e região externa abrangendo os 85% restantes de $\delta$. Na camada logarítmica, $u^+ = 2,439 \ln y^+ + 5,0$ decorre da dedução teórica de Prandtl ($k=0,41, A=5,0$), enquanto Monin e Yaglom propuseram os ajustes empíricos $u^+ = 2,5 \ln y^+ + 5,1$ (para $y^+ > 30$) e a relação da região externa $\frac{V_0 - \bar{u}}{u_\tau} = -2,5 \ln\left(\frac{y}{\delta}\right) + 2,35$ (para $y/\delta < 0,15$) (Seção VIII, itens 8.1 e 8.2). |
| **7.6** | **F** | **Falso.** Embora a fração $\theta = \frac{7}{72}\delta$, a espessura $\delta \approx 0,38 x Re_x^{-1/5}$, o coeficiente local $c_{f,x} = 0,58693 Re_x^{-1/5}$ e o coeficiente global $C_F \approx 0,734 Re_L^{-1/5}$ correspondam aos resultados analíticos da lei $1/7$, a afirmação de que a fórmula é universalmente aplicável a navios reais com $Re \sim 10^8 - 10^9$ é falsa: sua validade é estritamente limitada a $Re_L < 10^7$ devido às restrições da lei da $1/7$ potência (Seção X, item 10.1). |

**Sequência de Gabarito do V/F:** V – F – V – F – V – F.

---

## 4. Cálculo fixo

**Espaço reservado para o exercício de cálculo do professor.**

Sem resolução ou alteração de dados nesta versão. O espaço permanece resguardado para inclusão do enunciado e gabarito do cálculo original trabalhado em sala de aula, conforme a diretriz obrigatória do projeto.
