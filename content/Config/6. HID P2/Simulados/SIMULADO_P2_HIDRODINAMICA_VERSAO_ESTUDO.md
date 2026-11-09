# Simulado P2 de Hidrodinâmica I — Versão de estudo

**Nível:** Fácil a Médio  
**Orientação:** responda às questões sem consultar o gabarito.  
**Formato:** múltipla escolha, completar lacunas, verdadeiro ou falso e cálculo.

---

## Questões de múltipla escolha

### Questão 1 — Paradoxo de d'Alembert e hipótese de Prandtl

Em 1904, Ludwig Prandtl propôs a teoria da camada limite, superando o Paradoxo de d'Alembert (que previa força de arrasto nula sobre corpos imersos em fluidos ideais). De acordo com a hipótese fundamental de Prandtl, como o escoamento ao redor de um corpo real imerso deve ser dividido?

- [ ] **A)** Em uma região única e homogênea, onde a viscosidade molecular atua com a mesma intensidade em todo o campo fluido.
- [ ] **B)** Em duas regiões: um escoamento potencial externo, onde os efeitos viscosos são desprezíveis, e uma fina camada limite junto ao corpo, onde as forças viscosas e inerciais possuem a mesma ordem de grandeza.
- [ ] **C)** Em uma camada externa puramente turbulenta e uma camada interna invíscida sem resistência ao avanço.
- [ ] **D)** Em uma região onde a pressão é nula sobre toda a superfície e uma região onde a velocidade é constante.
- [ ] **E)** Em um escoamento laminar na face superior e um escoamento potencial exclusivamente na face inferior do corpo.

### Questão 2 — Simplificações de Navier-Stokes na camada limite

Ao aplicar uma análise de ordem de grandeza às equações de Navier-Stokes para o escoamento permanente sobre uma placa plana delgada ($\delta \ll L$), Prandtl introduziu simplificações fundamentais. Qual dessas simplificações físicas está correta?

- [ ] **A)** A difusão viscosa longitudinal ($\partial^2 u/\partial x^2$) é desprezível em comparação com a difusão transversal ($\partial^2 u/\partial y^2$), e a variação de pressão através da espessura da camada limite é aproximadamente nula ($\partial p/\partial y \approx 0$).
- [ ] **B)** A componente de velocidade normal à parede ($v$) possui a mesma magnitude da velocidade livre da corrente ($V_0$).
- [ ] **C)** A difusão viscosa longitudinal é o termo predominante na equação da quantidade de movimento.
- [ ] **D)** A pressão varia intensamente entre a parede sólida e o bordo exterior da camada limite devido à rotação das partículas fluidas.
- [ ] **E)** Os efeitos viscosos superam totalmente as forças inerciais, permitindo eliminar os termos convectivos de aceleração.

### Questão 3 — Método integral e volume de controle

No método integral de Von Kármán, aplica-se a conservação da quantidade de movimento linear a um volume de controle que envolve a camada limite sobre uma placa plana. Sobre o balanço de forças e as hipóteses simplificadoras desse método, é correto afirmar que:

- [ ] **A)** A placa sólida exerce uma força retardadora sobre o fluido (sinal negativo) e, pela Terceira Lei de Newton, o fluido exerce sobre a placa uma força de arrasto de mesmo módulo no sentido positivo do escoamento ($+x$).
- [ ] **B)** A vazão de massa que atravessa a fronteira superior do volume de controle é estritamente nula por se tratar de uma linha de corrente impermeável.
- [ ] **C)** O método integral exige a resolução exata ponto a ponto da pressão e da velocidade antes de integrar os fluxos de momento.
- [ ] **D)** A força exercida pela placa sobre o fluido atua no sentido de acelerar as camadas fluidas adjacentes à parede.
- [ ] **E)** O perfil polinomial parabólico adotado é uma solução analítica exata das equações diferenciais de Navier-Stokes.

### Questão 4 — Espessuras integrais e Equação de Von Kármán

A espessura de deslocamento ($\delta^*$) e a espessura de quantidade de movimento ($\theta$) quantificam os efeitos globais do atrito viscoso na camada limite. Qual é a interpretação física correta dessas grandezas?

- [ ] **A)** A espessura $\delta^*$ mede o afastamento das linhas de corrente externas decorrente da redução de vazão de massa, enquanto $\theta$ quantifica o déficit total no fluxo de quantidade de movimento do escoamento.
- [ ] **B)** A espessura $\delta^*$ mede a espessura geométrica total da camada limite, enquanto $\theta$ mede exclusivamente a subcamada viscosa.
- [ ] **C)** A espessura $\delta^*$ quantifica a perda de energia cinética do escoamento, enquanto $\theta$ identifica o ponto de separação da camada limite.
- [ ] **D)** A espessura $\theta$ é sempre maior do que a espessura de deslocamento $\delta^*$ para qualquer escoamento sobre placa plana lisa.
- [ ] **E)** Ambas as espessuras são propriedades geométricas fixas da placa sólida e independem da velocidade do escoamento.

### Questão 5 — Formulações práticas de resistência friccional

No projeto naval, a previsão da resistência friccional do casco utiliza formulações clássicas como a equação de Schoenherr, a fórmula de Granville e a linha ITTC-1957. A respeito da finalidade prática dessas formulações, é correto afirmar que:

- [ ] **A)** A linha ITTC-1957 constitui uma convenção pragmática adotada internacionalmente para a extrapolação de resistência entre modelo e navio real, enquanto a fórmula de Granville estima o coeficiente de atrito local na popa ($x = L$).
- [ ] **B)** A equação de Schoenherr aplica-se unicamente ao regime laminar de placas planas de pequena extensão.
- [ ] **C)** A fórmula de Granville foi proposta para calcular a resistência de ondas na proa do navio.
- [ ] **D)** A linha ITTC-1957 fornece a distribuição física pontual exata do atrito sobre qualquer casco tridimensional, dispensando correções de forma.
- [ ] **E)** A formulação de Schoenherr elimina a necessidade de considerar a rugosidade do casco em navios de grande porte.

---

## Questão 6 — Complete as lacunas

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

## Questão 7 — Verdadeiro ou falso

Assinale **V** para verdadeiro ou **F** para falso.

**7.1.** A solução de Blasius para placa plana laminar transforma as equações diferenciais da camada limite na equação diferencial ordinária $f''' + \frac{1}{2}ff'' = 0$, governada na parede sólida pelas condições cinemáticas de impermeabilidade ($f(0) = 0$) e aderência ($f'(0) = 0$).

- [ ] V
- [ ] F

**7.2.** Na solução de Blasius para placa plana laminar, a constante $5$ presente na expressão da espessura $\delta = \frac{5x}{\sqrt{Re_x}}$ representa a posição exata onde o perfil atinge rigorosamente 100% da velocidade da corrente livre ($u = V_0$).

- [ ] V
- [ ] F

**7.3.** As linhas de corrente são curvas tangentes ao vetor velocidade em cada ponto do escoamento, sendo governadas no plano bidimensional $xy$ pela equação diferencial $v\,dx - u\,dy = 0$.

- [ ] V
- [ ] F

**7.4.** Como as equações médias de Reynolds (RANS) calculam valores médios no tempo, elas são adequadas para quantificar com exatidão as forças de pico instantâneas responsáveis por cavitação e danos estruturais.

- [ ] V
- [ ] F

**7.5.** Na camada limite turbulenta sobre parede lisa, a subcamada viscosa situa-se na faixa $y^+ < 5$, onde os efeitos viscosos moleculares predominam sobre as flutuações turbulentas e a velocidade varia linearmente ($u^+ = y^+$).

- [ ] V
- [ ] F

**7.6.** A correlação de Prandtl obtida a partir da lei da potência $1/7$ ($\bar{u}/V_0 = (y/\delta)^{1/7}$) possui validade irrestrita, aplicando-se com grande precisão a navios reais operando em números de Reynolds na faixa de $10^8$ a $10^9$.

- [ ] V
- [ ] F

---

## Questão 8 — Cálculo: arrasto sobre chapa de madeira compensada

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
