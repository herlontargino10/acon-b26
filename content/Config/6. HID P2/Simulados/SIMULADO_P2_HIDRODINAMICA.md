# Simulado — P2 de Hidrodinâmica

**Nível:** Fácil a Médio  
**Nome:** __________________________________________  
**Data:** ____/____/______

**Orientação:** responda às questões sem consultar o gabarito. O simulado avalia o entendimento dos fundamentos físicos, modelos teóricos e equações da camada limite e resistência friccional de navios. Não é necessária a realização de cálculos numéricos nas seções objetivas. A última questão corresponde ao exercício de cálculo trabalhado em aula.

---

## 1. Múltipla escolha

**1.** Em 1904, Ludwig Prandtl propôs a teoria da camada limite, superando o Paradoxo de d'Alembert (que previa força de arrasto nula sobre corpos imersos em fluidos ideais). De acordo com a hipótese fundamental de Prandtl, como o escoamento ao redor de um corpo real imerso deve ser dividido?

A) Em uma região única e homogênea, onde a viscosidade molecular atua com a mesma intensidade em todo o campo fluido.  
B) Em duas regiões: um escoamento potencial externo, onde os efeitos viscosos são desprezíveis, e uma fina camada limite junto ao corpo, onde as forças viscosas e inerciais possuem a mesma ordem de grandeza.  
C) Em uma camada externa puramente turbulenta e uma camada interna invíscida sem resistência ao avanço.  
D) Em uma região onde a pressão é nula sobre toda a superfície e uma região onde a velocidade é constante.  
E) Em um escoamento laminar na face superior e um escoamento potencial exclusivamente na face inferior do corpo.

**2.** Ao aplicar uma análise de ordem de grandeza às equações de Navier-Stokes para o escoamento permanente sobre uma placa plana delgada ($\delta \ll L$), Prandtl introduziu simplificações fundamentais. Qual dessas simplificações físicas está correta?

A) A difusão viscosa longitudinal ($\partial^2 u/\partial x^2$) é desprezível em comparação com a difusão transversal ($\partial^2 u/\partial y^2$), e a variação de pressão através da espessura da camada limite é aproximadamente nula ($\partial p/\partial y \approx 0$).  
B) A componente de velocidade normal à parede ($v$) possui a mesma magnitude da velocidade livre da corrente ($V_0$).  
C) A difusão viscosa longitudinal é o termo predominante na equação da quantidade de movimento.  
D) A pressão varia intensamente entre a parede sólida e o bordo exterior da camada limite devido à rotação das partículas fluidas.  
E) Os efeitos viscosos superam totalmente as forças inerciais, permitindo eliminar os termos convectivos de aceleração.

**3.** No método integral de Von Kármán, aplica-se a conservação da quantidade de movimento linear a um volume de controle que envolve a camada limite sobre uma placa plana. Sobre o balanço de forças e as hipóteses simplificadoras desse método, é correto afirmar que:

A) A placa sólida exerce uma força retardadora sobre o fluido (sinal negativo) e, pela Terceira Lei de Newton, o fluido exerce sobre a placa uma força de arrasto de mesmo módulo no sentido positivo do escoamento ($+x$).  
B) A vazão de massa que atravessa a fronteira superior do volume de controle é estritamente nula por se tratar de uma linha de corrente impermeável.  
C) O método integral exige a resolução exata ponto a ponto da pressão e da velocidade antes de integrar os fluxos de momento.  
D) A força exercida pela placa sobre o fluido atua no sentido de acelerar as camadas fluidas adjacentes à parede.  
E) O perfil polinomial parabólico adotado é uma solução analítica exata das equações diferenciais de Navier-Stokes.

**4.** A espessura de deslocamento ($\delta^*$) e a espessura de quantidade de movimento ($\theta$) quantificam os efeitos globais do atrito viscoso na camada limite. Qual é a interpretação física correta dessas grandezas?

A) A espessura $\delta^*$ mede o afastamento das linhas de corrente externas decorrente da redução de vazão de massa, enquanto $\theta$ quantifica o déficit total no fluxo de quantidade de movimento do escoamento.  
B) A espessura $\delta^*$ mede a espessura geométrica total da camada limite, enquanto $\theta$ mede exclusivamente a subcamada viscosa.  
C) A espessura $\delta^*$ quantifica a perda de energia cinética do escoamento, enquanto $\theta$ identifica o ponto de separação da camada limite.  
D) A espessura $\theta$ é sempre maior do que a espessura de deslocamento $\delta^*$ para qualquer escoamento sobre placa plana lisa.  
E) Ambas as espessuras são propriedades geométricas fixas da placa sólida e independem da velocidade do escoamento.

**5.** No projeto naval, a previsão da resistência friccional do casco utiliza formulações clássicas como a equação de Schoenherr, a fórmula de Granville e a linha ITTC-1957. A respeito da finalidade prática dessas formulações, é correto afirmar que:

A) A linha ITTC-1957 constitui uma convenção pragmática adotada internacionalmente para a extrapolação de resistência entre modelo e navio real, enquanto a fórmula de Granville estima o coeficiente de atrito local na popa ($x = L$).  
B) A equação de Schoenherr aplica-se unicamente ao regime laminar de placas planas de pequena extensão.  
C) A fórmula de Granville foi proposta para calcular a resistência de ondas na proa do navio.  
D) A linha ITTC-1957 fornece a distribuição física pontual exata do atrito sobre qualquer casco tridimensional, dispensando correções de forma.  
E) A formulação de Schoenherr elimina a necessidade de considerar a rugosidade do casco em navios de grande porte.

---

## 2. Complete as lacunas

Complete cada frase com o termo ou valor adequado.

**6.1.** Em um fluido viscoso, a condição de contorno cinemática em que o fluido em contato com a parede possui velocidade relativa nula é a condição de ______________________________.

**6.2.** A força de atrito tangencial por unidade de área exercida pelo fluido sobre a superfície sólida, calculada pelo produto $\mu \left.\frac{\partial u}{\partial y}\right|_{y=0}$, é a ______________________________.

**6.3.** No escoamento bidimensional incompressível, a função matemática cujas derivadas fornecem as componentes de velocidade ($u = \partial\psi/\partial y$ e $v = -\partial\psi/\partial x$) e garantem o atendimento da continuidade é a ______________________________.

**6.4.** Na solução analítica de Blasius para placa plana laminar, a combinação adimensional entre as coordenadas espaciais expressa por $\eta = y\sqrt{\frac{V_0}{\nu x}}$ é denominada variável de ______________________________.

**6.5.** A confirmação em laboratório da teoria de Blasius por meio de medições diretas da força de cisalhamento na parede foi realizada em 1953 pelo pesquisador ______________________________.

**6.6.** Na prática da engenharia e da hidrodinâmica naval, o número de Reynolds crítico ($Re_{cr} = \frac{\rho V_0 x_{cr}}{\mu}$) comumente adotado para indicar o início da transição sobre superfície lisa é de ______________________________.

**6.7.** Nas equações médias de Reynolds (RANS), o termo adicional $-\rho\overline{u'v'}$, originado pelas flutuações de velocidade e responsável pelo transporte turbulento de momento, é denominado ______________________________.

**6.8.** Na camada limite turbulenta, a escala característica com dimensão de velocidade definida por $u_\tau = \sqrt{\frac{\tau_w}{\rho}}$ é denominada ______________________________.

**6.9.** Na estrutura da camada limite turbulenta sobre parede lisa, a região mais delgada imediatamente colada à superfície sólida ($y^+ < 5$), dominada pelo amortecimento viscoso com perfil linear $u^+ = y^+$, é a ______________________________.

**6.10.** Na formulação da conferência ATTC-1947, a constante aditiva $\Delta C_F = 0,0004$ é incorporada ao coeficiente de Schoenherr para compensar o efeito da ______________________________ do casco do navio em escala real.

---

## 3. Verdadeiro ou falso

Assinale **V** para verdadeiro ou **F** para falso.

**7.1.** A solução de Blasius para placa plana laminar transforma as equações diferenciais da camada limite na equação diferencial ordinária $f''' + \frac{1}{2}ff'' = 0$, governada na parede sólida pelas condições cinemáticas de impermeabilidade ($f(0) = 0$) e aderência ($f'(0) = 0$). ( )

**7.2.** Na solução de Blasius para placa plana laminar, a constante $5$ presente na expressão da espessura $\delta = \frac{5x}{\sqrt{Re_x}}$ representa a posição exata onde o perfil atinge rigorosamente 100% da velocidade da corrente livre ($u = V_0$). ( )

**7.3.** As linhas de corrente são curvas tangentes ao vetor velocidade em cada ponto do escoamento, sendo governadas no plano bidimensional $xy$ pela equação diferencial $v\,dx - u\,dy = 0$. ( )

**7.4.** Como as equações médias de Reynolds (RANS) calculam valores médios no tempo, elas são adequadas para quantificar com exatidão as forças de pico instantâneas responsáveis por cavitação e danos estruturais. ( )

**7.5.** Na camada limite turbulenta sobre parede lisa, a subcamada viscosa situa-se na faixa $y^+ < 5$, onde os efeitos viscosos moleculares predominam sobre as flutuações turbulentas e a velocidade varia linearmente ($u^+ = y^+$). ( )

**7.6.** A correlação de Prandtl obtida a partir da lei da potência $1/7$ ($\bar{u}/V_0 = (y/\delta)^{1/7}$) possui validade irrestrita, aplicando-se com grande precisão a navios reais operando em números de Reynolds na faixa de $10^8$ a $10^9$. ( )

---

## 4. Cálculo fixo

**Exercício trabalhado em sala de aula — Arrasto sobre chapa de madeira compensada:**

Uma chapa de madeira compensada, de dimensões $4 \times 8\text{ ft}$, é transportada no teto de um carro a $56\text{ km/h}$, perfeitamente alinhada com o fluxo de ar.

Considere as propriedades do ar a $20\ ^\circ\text{C}$ e $1\text{ atm}$:
- Massa específica: $\rho = 1,2\text{ kg/m}^3$
- Viscosidade dinâmica: $\mu = 1,8 \times 10^{-5}\text{ kg/(m}\cdot\text{s)}$
- Comprimento: $L = 2,44\text{ m}$ (dimensão de $8\text{ ft}$)
- Largura: $b = 1,22\text{ m}$ (dimensão de $4\text{ ft}$)

Determine:

**a)** A espessura da camada limite no final da chapa ($\delta$).

**b)** O arrasto total sobre a chapa considerando escoamento laminar em ambas as faces ($F_L$).

**c)** O arrasto total sobre a chapa considerando escoamento turbulento em ambas as faces ($F_T$), admitindo madeira lisa. Compare os resultados obtidos.

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

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
| **I. Fundamentos e Paradoxo** | • Paradoxo de d'Alembert e hipótese de Prandtl<br>• Condição de não escorregamento<br>• Tensão de cisalhamento na parede $\tau_w$ | **Questão 1**<br>**Item 6.1**<br>**Item 6.2** | Identificar a superação do paradoxo invíscido e a divisão do escoamento; definir a condição cinemática na parede ($u=0$); expressar a tensão tangencial pela lei de Newton. |
| **II. Dedução de Prandtl 2D** | • Simplificação da difusão longitudinal ($\partial^2 u/\partial x^2 \ll \partial^2 u/\partial y^2$)<br>• Pressão normal constante ($\partial p/\partial y \approx 0$) | **Questão 2** | Reconhecer o descarte da difusão viscosa longitudinal perante a transversal e a invariância da pressão através da espessura da camada limite. |
| **III. Método Integral do VC** | • Conservação de quantidade de movimento no VC<br>• Terceira Lei de Newton (arrasto no corpo vs. força no fluido) | **Questão 3** | Compreender o balanço global de forças, o sinal da ação retardadora no fluido e a reação positiva de arrasto sobre a placa. |
| **IV. Visualização e Função de Corrente** | • Função de corrente $\psi$ e continuidade 2D<br>• Equação diferencial das linhas de corrente em 2D | **Item 6.3**<br>**Item 7.3** | Nomear a função de corrente e sua relação com a continuidade; identificar a equação diferencial de linhas de corrente no plano ($v\,dx - u\,dy = 0$). |
| **V. Solução Exata de Blasius** | • Variável de similaridade $\eta$<br>• Validação experimental de Satish Dhawan (1953)<br>• EDO de Blasius e condições de contorno<br>• Convenção da espessura assintótica ($0,99 V_0$) | **Item 6.4**<br>**Item 6.5**<br>**Item 7.1**<br>**Item 7.2** | Nomear $\eta$; reconhecer a confirmação experimental direta de Dhawan; identificar a EDO $f'''+\frac{1}{2}ff''=0$ com $f(0)=f'(0)=0$; julgar que 5 corresponde a $0,99 V_0$ (e não $V_0$). |
| **VI. Transição e Reynolds Crítico** | • Definição analítica de $Re_{cr}$<br>• Valor prático de projeto na engenharia naval ($5 \times 10^5$) | **Item 6.6** | Identificar o valor comumente adotado na prática naval ($5 \times 10^5$) para o início da transição sobre placas lisas. |
| **VII. Equações RANS e Turbulência** | • Tensão de Reynolds ($-\rho\overline{u'v'}$)<br>• Limitação das médias temporais para forças de pico | **Item 6.7**<br>**Item 7.4** | Nomear a tensão de Reynolds gerada pelas flutuações; julgar a inadequação das médias RANS para fenômenos de pico instantâneo (cavitação/ruptura). |
| **VIII. Estrutura Turbulenta e Leis de Parede** | • Velocidade de atrito ($u_\tau = \sqrt{\tau_w/\rho}$)<br>• Subcamada viscosa ($y^+ < 5$) e lei linear $u^+ = y^+$ | **Item 6.8**<br>**Item 6.9**<br>**Item 7.5** | Nomear a velocidade de atrito; identificar a subcamada viscosa e validar seu domínio viscoso com perfil linear na faixa $y^+ < 5$. |
| **IX. Parâmetros Integrais e Von Kármán** | • Interpretação física da espessura de deslocamento ($\delta^*$)<br>• Interpretação física da espessura de quantidade de movimento ($\theta$) | **Questão 4** | Explicar $\delta^*$ como deflexão de linhas de corrente por perda de vazão mássica e $\theta$ como déficit de fluxo de momento linear. |
| **X. Resistência Turbulenta de Prandtl (1/7)** | • Perfil da lei da potência $1/7$<br>• Limite de validade ($Re_L < 10^7$) frente a navios reais | **Item 7.6** | Identificar que a lei da potência $1/7$ é uma aproximação restrita a escoamentos laboratoriais ($Re_L < 10^7$), sendo inválida para navios reais em grande escala. |
| **XI. Schoenherr e ATTC-1947** | • Margem aditiva de rugosidade $\Delta C_F = 0,0004$ da ATTC-1947 | **Item 6.10** | Identificar o termo "rugosidade" referente à correção da ATTC-1947 para o casco de aço em escala real. |
| **XII. ITTC-1957 e Linhas Modernas** | • Fórmula de Granville para a popa ($x=L$)<br>• Caráter pragmático da linha ITTC-1957 de extrapolação modelo-navio | **Questão 5** | Compreender a finalidade da fórmula de Granville para o atrito local na popa ($x=L$) e o papel pragmático da linha ITTC-1957 como convenção de extrapolação. |
| **Cálculo Fixo** | Arrasto laminar e turbulento sobre chapa de madeira compensada | **Questão 8** | Aplicar as fórmulas de Blasius e turbulenta para obter $\delta$, $F_L$, $F_T$ e a razão comparativa sobre chapa com duas faces molhadas. |
