# Simulado — P2 de Hidrodinâmica

**Nível médio**  
**Nome:** __________________________________________  
**Data:** ____/____/______

**Orientação:** responda às questões sem consultar o gabarito. O simulado avalia o entendimento dos fundamentos físicos, modelos teóricos e equações da camada limite e resistência friccional de navios. Não é necessária a realização de cálculos numéricos nas seções objetivas. A última questão permanece reservada para o exercício de cálculo do professor.

---

## 1. Múltipla escolha

**1.** Antes de 1904, a mecânica dos fluidos apoiava-se na teoria dos escoamentos potenciais, que previa que um corpo em movimento em um fluido ideal não sofria nenhuma força de resistência ao avanço — resultado conhecido como o Paradoxo de d'Alembert. Ludwig Prandtl resolveu essa contradição propondo a teoria da camada limite. De acordo com a hipótese de Prandtl e a comparação entre os regimes laminar e turbulento apresentada no resumo, qual afirmação está correta?

A) A viscosidade atua de forma homogênea em todo o escoamento, invalidando totalmente o uso da teoria dos escoamentos potenciais ao redor do corpo.  
B) O escoamento pode ser dividido em duas regiões: um escoamento potencial externo, onde os efeitos viscosos são desprezíveis, e uma fina camada limite junto ao corpo, onde as forças inerciais e viscosas possuem a mesma ordem de grandeza. Além disso, o perfil turbulento médio apresenta um gradiente de velocidade na parede muito mais elevado do que o laminar ($\left.\frac{\partial u}{\partial y}\right|_{y=0,\text{lam}} < \left.\frac{\partial \bar{u}}{\partial y}\right|_{y=0,\text{turb}}$), gerando maior tensão de cisalhamento na parede ($\tau_{w,\text{turb}} > \tau_{w,\text{lam}}$).  
C) O arrasto sobre o corpo é nulo mesmo em fluidos reais, pois a condição de não escorregamento na parede anula as forças tangenciais de atrito.  
D) No regime laminar, o gradiente de velocidade na parede é superior ao do regime turbulento, fazendo com que a tensão cisalhante laminar seja maior do que a turbulenta ($\tau_{w,\text{lam}} > \tau_{w,\text{turb}}$).  
E) A espessura da camada limite permanece constante ao longo de toda a superfície da placa, sendo independente da velocidade da corrente livre e do número de Reynolds.

**2.** Ao simplificar as equações de Navier-Stokes para o escoamento laminar permanente sobre uma placa plana, Prandtl realizou uma análise de ordem de grandeza das forças atuantes na camada limite. Com base nessa análise e na conexão entre a camada limite e o escoamento potencial externo, qual conclusão física está correta?

A) A difusão viscosa longitudinal ($\partial^2 u/\partial x^2$) é o termo dominante da equação de movimento, sendo muito maior do que a difusão transversal ($\partial^2 u/\partial y^2$).  
B) A componente de velocidade normal à parede ($v$) possui a mesma ordem de grandeza da velocidade da corrente livre ($V_0$).  
C) A difusão viscosa longitudinal ($\partial^2 u/\partial x^2$) é desprezível quando comparada à difusão transversal ($\partial^2 u/\partial y^2$). Além disso, a variação de pressão através da espessura da camada limite é aproximadamente nula ($\partial p/\partial y \approx 0$), o que significa que a pressão interna é imposta pelo escoamento potencial externo. Nesse escoamento externo, o gradiente longitudinal de pressão ($-\partial p/\partial x$) relaciona-se diretamente à aceleração da corrente livre pela Equação de Bernoulli ($\rho V dV/dx$).  
D) A Equação de Bernoulli pode ser aplicada diretamente no interior da camada limite para calcular a tensão cisalhante na parede a partir da velocidade local.  
E) A pressão varia intensamente entre a parede e o bordo exterior da camada limite devido à rotação das partículas fluidas junto à superfície.

**3.** O método integral estabelece balanços globais de conservação de massa e de quantidade de movimento sobre um volume de controle que envolve a camada limite. Para aplicar esse método ao escoamento sobre uma placa plana, costuma-se aproximar a variação da velocidade no interior da camada por um perfil polinomial parabólico. Sobre os fundamentos do método integral e a adoção desse perfil, é correto afirmar que:

A) A vazão de massa que cruza a fronteira superior do volume de controle é nula, pois essa fronteira coincide com uma linha de corrente impermeável.  
B) A força exercida pela placa sobre o fluido atua no sentido positivo do escoamento, impulsionando a massa de fluido para compensar a perda de velocidade.  
C) A força que a placa exerce sobre o fluido tem sinal negativo por representar uma ação retardadora. Pela Terceira Lei de Newton, essa força é igual em módulo e oposta em sentido ao arrasto friccional sofrido pelo corpo. Além disso, o perfil parabólico é uma aproximação matemática adotada para satisfazer globalmente as condições de contorno no topo do volume de controle ($u = V_0$ e derivada nula).  
D) O perfil parabólico é uma solução analítica exata das equações de Navier-Stokes, coincidindo rigorosamente com a curva obtida por Blasius.  
E) O método integral só pode ser aplicado se a condição na borda superior do volume de controle for fixada experimentalmente em 99% da velocidade livre ($0,99 V_0$).

**4.** Para avaliar os efeitos globais da camada limite sem precisar calcular a velocidade ponto a ponto, empregam-se a espessura de deslocamento ($\delta^*$) e a espessura de quantidade de movimento ($\theta$). A partir dessas grandezas, a Equação do Momento de Von Kármán para placa plana estabelece a relação:

$$
c_{f,x} = 2 \frac{d\theta}{dx}
$$

Qual é a interpretação física dessas espessuras e a justificativa para a presença do fator 2 nessa relação?

A) A espessura $\delta^*$ mede a espessura geométrica total da camada limite, enquanto $\theta$ mede a subcamada viscosa; o fator 2 indica que o atrito atua simultaneamente nas duas faces da placa.  
B) O fator 2 provém da integração de uma função polinomial parabólica de segundo grau adotada para o perfil de velocidades.  
C) A espessura de deslocamento ($\delta^*$) representa o afastamento das linhas de corrente externas decorrente da redução de vazão de massa junto à parede. Já a espessura de quantidade de movimento ($\theta$) quantifica a perda total de fluxo de quantidade de movimento no escoamento. O fator 2 surge porque o coeficiente local ($c_{f,x}$) é normalizado pela pressão dinâmica ($\frac{1}{2}\rho V_0^2$), cujo denominador contém o fator $1/2$, enquanto o balanço de momento fornece diretamente $\frac{\tau_w}{\rho V_0^2} = \frac{d\theta}{dx}$.  
D) A espessura $\theta$ é sempre maior do que $\delta^*$ porque as perdas de energia superam as perdas de vazão em qualquer escoamento incompressível.  
E) A relação de Von Kármán exige que o gradiente longitudinal de pressão seja positivo, sendo inválida para escoamentos sobre placa plana lisa.

**5.** No projeto de navios, a previsão da resistência friccional do casco utiliza formulações clássicas, como a equação implícita de Schoenherr (1932), a fórmula de Granville para a popa e a linha de correlação modelo-navio ITTC-1957:

$$
\frac{0,24213}{\sqrt{C_F}} = \log_{10}(Re_L \cdot C_F) \qquad \text{e} \qquad c_{f,L} = \frac{C_F}{1 - 2,439\sqrt{\frac{C_F}{2}}}
$$

Considerando a finalidade dessas relações e as observações da apostila sobre as formulações práticas de correlação, qual afirmação está correta?

A) A equação implícita de Schoenherr aplica-se unicamente ao regime laminar de Blasius, sendo substituída pela teoria do escoamento potencial para altos números de Reynolds.  
B) A fórmula de Granville foi proposta para calcular o atrito local no bordo de ataque ($x=0$), onde a camada limite inicia seu crescimento.  
C) A equação de Schoenherr foi deduzida com base na lei logarítmica de parede para estimar a resistência de placas planas. A fórmula de Granville tem como finalidade calcular o coeficiente de atrito local na popa do navio ($x = L$) a partir do coeficiente total ($C_F$). Já a linha ITTC-1957 constitui uma convenção pragmática internacional para extrapolação entre modelo e navio (com elevação de 12% no numerador de Hughes e denominador ajustado), não representando o atrito físico real do casco tridimensional.  
D) A linha ITTC-1957 é estritamente 12% superior à linha de Hughes em qualquer número de Reynolds, pois manteve exatamente o mesmo denominador.  
E) A fórmula de Granville substitui a necessidade de avaliar a resistência viscosa global do navio, fornecendo diretamente a potência propulsiva requerida.

---

## 2. Complete as lacunas

Complete cada frase com o termo ou expressão adequada.

**6.1.** Em um fluido viscoso, a condição de contorno em que o fluido em contato com a parede adquire a mesma velocidade da superfície sólida, apresentando velocidade relativa nula, é a condição de ______________________________.

**6.2.** A força de atrito por unidade de área exercida tangencialmente pelo fluido sobre a superfície do corpo, calculada pelo produto da viscosidade dinâmica pelo gradiente de velocidade na parede ($\mu \left.\frac{\partial u}{\partial y}\right|_{y=0}$), é a ______________________________.

**6.3.** No escoamento bidimensional incompressível, a função matemática cujas derivadas fornecem as componentes de velocidade ($u = \partial\psi/\partial y$ e $v = -\partial\psi/\partial x$) e garantem a satisfação idêntica da conservação da massa é a ______________________________.

**6.4.** Na solução analítica de Blasius para a placa plana laminar, a combinação adimensional entre as coordenadas espaciais definida por $\eta = y\sqrt{\frac{V_0}{\nu x}}$ é denominada variável de ______________________________.

**6.5.** A confirmação em laboratório da teoria laminar de Blasius por meio de medições diretas da força de atrito na parede foi realizada em 1953 pelo pesquisador ______________________________.

**6.6.** O início da transição do regime laminar para o turbulento é determinado pelo número de Reynolds crítico, definido por $Re_{cr} = \frac{\rho V_0 x_{cr}}{\mu}$, em que $x_{cr}$ representa a distância da borda de ataque até a posição de transição; enquanto em condições ideais de laboratório com baixíssima turbulência esse parâmetro atinge cerca de $3 \times 10^6$ (e historicamente Blasius indicou $4,5 \times 10^5$), na prática da engenharia e hidrodinâmica naval adota-se comumente o valor de ______________________________.

**6.7.** Nas equações médias de Reynolds (RANS), o termo adicional $-\rho\overline{u'v'}$, que representa o transporte de quantidade de movimento provocado pelas flutuações turbulentas e introduz novas incógnitas gerando o problema de fechamento, é denominado ______________________________.

**6.8.** Na camada limite turbulenta, a escala com dimensão de velocidade definida por $u_\tau = \sqrt{\frac{\tau_w}{\rho}}$, utilizada para construir as variáveis adimensionais de parede ($u^+$ e $y^+$), é denominada ______________________________.

**6.9.** Na estrutura da camada limite turbulenta sobre parede lisa, a região mais delgada imediatamente adjacente à fronteira sólida ($y^+ < 5$), dominada pela viscosidade molecular segundo a relação linear $u^+ = y^+$, é a ______________________________.

**6.10.** Na formulação da conferência ATTC-1947, o valor fixo $\Delta C_F = 0,0004$ é adicionado ao coeficiente de Schoenherr para compensar o efeito da ______________________________ do casco do navio em escala real.

---

## 3. Verdadeiro ou falso

Assinale **V** para verdadeiro ou **F** para falso.

**7.1.** A redução de Blasius para a camada limite laminar sobre placa plana conduz à equação diferencial ordinária $f''' + \frac{1}{2}ff'' = 0$ (ou $2f''' + ff'' = 0$), sendo governada na parede pelas condições de aderência e impermeabilidade ($f(0) = 0$ e $f'(0) = 0$) e, no bordo exterior assintótico, pela condição de corrente livre ($f'(\infty) = 1$). ( )

**7.2.** Na solução exata de Blasius para placa plana laminar, o valor $0,332$ expressa a derivada de segunda ordem da função de corrente na parede ($f''(0)$) e o coeficiente de atrito local é $c_{f,x} = 0,664 Re_x^{-1/2}$; contudo, a constante $5$ na expressão da espessura ($\delta = \frac{5x}{\sqrt{Re_x}}$) indica a posição onde o perfil atinge rigorosamente a velocidade não perturbada da corrente livre ($u = V_0$), e o coeficiente médio total de atrito da placa é $C_F = 0,664 Re_L^{-1/2}$. ( )

**7.3.** As linhas de corrente são curvas tangentes ao vetor velocidade em cada ponto do espaço; para escoamentos bidimensionais no plano $xy$, sua equação diferencial é $v\,dx - u\,dy = 0$, enquanto no caso tridimensional genérico a condição vetorial $\vec{V} \times d\vec{s} = \mathbf{0}$ expressa-se na forma simétrica $\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$. ( )

**7.4.** A decomposição de Reynolds separa as variáveis do escoamento em parcelas médias e flutuantes ($u = \bar{u} + u'$); as equações médias resultantes (RANS) são recomendadas de modo irrestrito para todas as análises de engenharia naval, prestando-se com exatidão para prever esforços decorrentes de forças de pico instantâneas que geram cavitação e rupturas estruturais. ( )

**7.5.** Na camada limite turbulenta sobre parede lisa, a estrutura do escoamento apresenta as delimitações aproximadas reportadas no material: a subcamada viscosa ($y^+ < 5$) ocupa cerca de 1% de $\delta$; a subcamada viscosa somada à região de transição ($y^+ < 30$) ocupa cerca de 5% de $\delta$; a região interna corresponde a cerca de 15% de $\delta$; a camada logarítmica de sobreposição ocupa cerca de 20% de $\delta$; e a região externa abrange os 85% restantes de $\delta$. Na camada logarítmica, a expressão $u^+ = 2,439 \ln y^+ + 5,0$ decorre da dedução teórica de Prandtl ($k = 0,41$), enquanto Monin e Yaglom propuseram os ajustes empíricos $u^+ = 2,5 \ln y^+ + 5,1$ (para $y^+ > 30$) e a relação da região externa $\frac{V_0 - \bar{u}}{u_\tau} = -2,5 \ln\left(\frac{y}{\delta}\right) + 2,35$ (para $y/\delta < 0,15$). ( )

**7.6.** Na dedução de Prandtl baseada na lei da potência $1/7$ ($\bar{u}/V_0 = (y/\delta)^{1/7}$), a integração do perfil fornece a fração de quantidade de movimento $\theta = \frac{7}{72}\delta$. A partir dessa relação e da fórmula empírica local, obtêm-se a espessura $\delta(x) \approx 0,38 x Re_x^{-1/5}$, o coeficiente de atrito local $c_{f,x} = 0,58693 Re_x^{-1/5}$ e o coeficiente médio $C_F \approx 0,734 Re_L^{-1/5}$. Contudo, essa formulação é universalmente aplicável a navios reais operando em números de Reynolds na faixa de $10^8$ a $10^9$. ( )

---

## 4. Cálculo fixo

**Espaço reservado para o exercício de cálculo fixo fornecido pelo professor para a P2.**

Esta posição permanece mantida sem alteração de enunciado, substituição por outro exercício ou inserção de dados não fornecidos, aguardando o envio do cálculo original trabalhado em sala de aula.

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

---

**Fim do simulado**

---

## Matriz de cobertura do simulado

| Tópico do Resumo da P2 | Subtópicos Efetivamente Avaliados | Questão / Item | Conteúdo e Critério Exigido do Estudante |
| :--- | :--- | :---: | :--- |
| **I. Fundamentos e Paradoxo** | • Paradoxo de d'Alembert e Hipótese de Prandtl (1904)<br>• Condição de não escorregamento<br>• Tensão de cisalhamento na parede $\tau_w$<br>• Comparativo dos gradientes na parede nos regimes laminar e turbulento | **Questão 1**<br>**Item 6.1**<br>**Item 6.2** | Compreender a divisão do escoamento e a ordem de grandeza; identificar a condição cinemática $u(y=0)=0$; definir a tensão tangencial $\tau_w$; comparar matematicamente os gradientes de velocidade na parede ($\left.\partial u/\partial y\right|_{y=0,\text{lam}} < \left.\partial \bar{u}/\partial y\right|_{y=0,\text{turb}}$). |
| **II. Dedução de Prandtl 2D** | • Análise de ordem de grandeza transversal ($\partial p/\partial y \approx 0$)<br>• Descarte da difusão longitudinal ($\partial^2 u/\partial x^2 \ll \partial^2 u/\partial y^2$)<br>• Acoplamento de Bernoulli no escoamento externo ($-\partial p/\partial x = \rho V dV/dx$) | **Questão 2** | Identificar que a difusão longitudinal é desprezada frente à transversal; reconhecer que a pressão é constante na transversal e imposta pelo escoamento potencial externo através de Bernoulli. |
| **III. Método Integral do VC** | • Balanço de quantidade de movimento no VC retangular<br>• Terceira Lei de Newton (força da placa no fluido vs. arrasto no casco)<br>• Significado e condições de contorno do perfil parabólico | **Questão 3** | Distinguir o sinal da ação retardadora da placa e a reação de arrasto sobre o corpo; identificar que o perfil parabólico é aproximação matemática com $u(\delta)=V_0$ e derivada nula no topo. |
| **IV. Visualização e Função de Corrente** | • Função de corrente $\psi$ e continuidade 2D<br>• Linhas de corrente em 2D ($v dx - u dy = 0$)<br>• Linhas de corrente em 3D ($\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$) | **Item 6.3**<br>**Item 7.3** | Identificar a função $\psi$ e sua satisfação idêntica da continuidade 2D; julgar a formulação matemática diferencial das linhas de corrente em duas e três dimensões. |
| **V. Solução Exata de Blasius** | • Variável de similaridade $\eta = y\sqrt{V_0/(\nu x)}$<br>• Validação experimental de Satish Dhawan (1953)<br>• EDO de Blasius e condições de contorno assintóticas<br>• Significado físico das constantes $0,332$, $5$, $0,664$ e $1,328$ | **Item 6.4**<br>**Item 6.5**<br>**Item 7.1**<br>**Item 7.2** | Nomear a variável $\eta$; reconhecer a medição direta de atrito de Dhawan; validar a forma da EDO e suas condições de contorno; julgar o significado de 5 ($0,99 V_0$ e não $V_0$) e a relação entre $c_{f,x}$ e $C_F$. |
| **VI. Transição e Reynolds Crítico** | • Definição analítica $Re_{cr} = \frac{\rho V_0 x_{cr}}{\mu}$ e papel de $x_{cr}$<br>• Valor prático na engenharia naval ($5 \times 10^5$) vs. laboratório ($3 \times 10^6$) e Blasius ($4,5 \times 10^5$) | **Item 6.6** | Compreender o significado de cada variável na definição de $Re_{cr}$; identificar o valor de projeto adotado na engenharia naval ($5 \times 10^5$) em contraste com os valores de laboratório e histórico. |
| **VII. Equações RANS e Turbulência** | • Tensão de Reynolds ($-\rho\overline{u'v'}$) e transporte de momento por flutuações<br>• Problema de fechamento da turbulência<br>• Exceção das médias RANS para forças de pico em cavitação e danos estruturais | **Item 6.7**<br>**Item 7.4** | Nomear a tensão de Reynolds e explicar seu significado como transporte turbulento gerador de fechamento; julgar a inadequação de médias temporais para impactos extremos instantâneos. |
| **VIII. Estrutura Turbulenta e Leis de Parede** | • Velocidade de atrito ($u_\tau = \sqrt{\tau_w/\rho}$) e variáveis $u^+, y^+$<br>• Subcamada viscosa ($y^+ < 5$) e lei linear $u^+ = y^+$<br>• Delimitações das 5 regiões da apostila (1%, 5%, 15%, 20% e 85%)<br>• Prandtl teórico vs. Monin & Yaglom empírico (logarítmico e região externa) | **Item 6.8**<br>**Item 6.9**<br>**Item 7.5** | Nomear $u_\tau$; identificar a subcamada viscosa e a lei de Taylor; validar as delimitações aproximadas de todas as cinco regiões; diferenciar a dedução de Prandtl dos ajustes empíricos de Monin & Yaglom (lei interna e relação externa em $y/\delta < 0,15$). |
| **IX. Parâmetros Integrais e Von Kármán** | • Interpretação física da espessura de deslocamento ($\delta^*$)<br>• Interpretação física da espessura de quantidade de movimento ($\theta$)<br>• Equação de Von Kármán ($c_{f,x} = 2 d\theta/dx$) e justificativa física do fator 2 | **Questão 4** | Explicar $\delta^*$ como deflexão de linhas de corrente por perda de vazão mássica e $\theta$ como déficit de momento; justificar o fator 2 pela definição de $c_{f,x}$ baseada na pressão dinâmica $\frac{1}{2}\rho V_0^2$. |
| **X. Resistência Turbulenta de Prandtl (1/7)** | • Fundamentos: lei $\bar{u}/V_0 = (y/\delta)^{1/7}$ e relação $\theta = \frac{7}{72}\delta$<br>• Resultados integrados: $c_{f,x} = 0,58693 Re_x^{-1/5}$, $\delta(x)$ e $C_F$<br>• Limite estrito de validade ($Re_L < 10^7$) frente a navios reais ($10^8 - 10^9$) | **Item 7.6** | Julgar a cadeia lógica da dedução de Prandtl (perfil $1/7$, $\theta = \frac{7}{72}\delta$, $c_{f,x}$ exato com expoente $-1/5$) e identificar que a validade é restrita a $Re < 10^7$, sendo insuficiente para navios em escala real. |
| **XI. Schoenherr e ATTC-1947** | • Equação implícita de Schoenherr com $0,24213$<br>• Constante aditiva de rugosidade $\Delta C_F = 0,0004$ da ATTC-1947 | **Questão 5**<br>**Item 6.10** | Compreender a finalidade da formulação implícita de Schoenherr com a constante $0,24213$; identificar o termo "rugosidade" referente ao acréscimo da ATTC-1947. |
| **XII. ITTC-1957 e Linhas Modernas** | • Fórmula de Granville para a popa ($c_{f,L}$ a partir de $C_F$)<br>• Linha ITTC-1957 vs. Hughes (acréscimo no numerador e ajuste no denominador)<br>• Ressalva do professor: correlação internacional pragmática vs. atrito 3D real | **Questão 5** | Compreender a finalidade de Granville para avaliar o atrito local na popa ($x=L$); identificar as alterações entre ITTC e Hughes; compreender o caráter pragmático das linhas de correlação modelo-navio e distingui-las da representação do atrito físico real do casco tridimensional. |
| **Cálculo Fixo** | Exercício prático fornecido pelo professor em sala de aula | **Questão 8** | Posição mantida estritamente pendente com espaço reservado para inserção futura do enunciado original. |
