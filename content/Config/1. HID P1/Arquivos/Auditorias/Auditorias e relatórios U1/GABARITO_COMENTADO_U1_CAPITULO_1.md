# Gabarito Comentado — Simulado de Hidrodinâmica (Capítulo 1)

## Questão 1 — Marque X

**Resposta correta:** (b) I, III e V.

**Justificativas:**
- **I. Verdadeira:** A seção 1 do material indica expressamente que na Hidrodinâmica do Navio os princípios tipicamente empregados são a conservação da massa e a conservação da quantidade de movimento.
- **II. Falsa:** A seção 5 define a vazão mássica como a taxa de quantidade de fluido por unidade de *tempo* (e não por unidade de área) que passa por uma face.
- **III. Verdadeira:** A seção 13 afirma de maneira direta que a lei de conservação da massa também é conhecida como equação da continuidade e que se aplica a qualquer fluido.
- **IV. Falsa:** A seção 14 especifica que, no caso de água e ar serem tratados como incompressíveis, a densidade absoluta é considerada *constante* ($\frac{\partial \rho}{\partial t} = 0$), portanto não varia significativamente no tempo.
- **V. Verdadeira:** As seções 7 e 26 detalham que a conservação da massa é uma lei local, significando que uma quantidade de massa não pode ir de um ponto A para um ponto B sem passar pelo espaço intermediário (não pode "teletransportar").

---

## Questão 2 — Complete as Lacunas

1. **energia** (Seção 1: As três leis citadas são massa, quantidade de movimento e energia).
2. **densidade** (Seção 2: Refere-se à densidade absoluta ou massa específica).
3. **volume de controle** (Seção 3: Definido como um volume fixo no espaço de forma arbitrária).
4. **tempo** (Seção 5: Parte integrante da definição formal de vazão mássica).
5. **saindo** (Seção 4 e 8: O sinal negativo representa a redução da massa interna quando há mais massa saindo do que entrando. Resposta equivalente aceita: *de saída*).
6. **local** (Seções 7 e 26: Lei de conservação local).
7. **continuidade** (Seção 13: Sinônimo direto da conservação da massa).
8. **incompressíveis** (Seção 14: Hipótese tratada para a água e ar, considerando densidade absoluta constante).
9. **velocidade** (Seção 16: No 1D incompressível, a igualdade indica que o que entra sai igualmente e não pode existir variação de velocidade entre entrada e saída).
10. **espaço** (Seção 20: O material destaca que o foco para aplicar a conservação está nas variações espaciais da velocidade).

---

## Questão 3 — Verdadeiro ou Falso

1. **Falso.** *Correção:* A conservação da energia é indicada para casos mais *complicados*, nos quais a temperatura é geralmente uma variável importante. (Seção 1)
2. **Verdadeiro.** A relação decorre do volume geométrico do pequeno elemento cubo $V = \Delta x \Delta y \Delta z$ aplicado na fórmula da massa $m = \rho V$. (Seção 2)
3. **Falso.** *Correção:* O volume de controle é um volume *fixo no espaço* (não se move com o fluido). O fluido é que atravessa suas superfícies. (Seção 3)
4. **Verdadeiro.** Trata-se da expressão exata apresentada no PDF para calcular a vazão mássica de uma face. (Seção 5)
5. **Verdadeiro.** É a interpretação direta fornecida para a forma integral formulada no documento. (Seção 12)
6. **Verdadeiro.** A relação vetorial compacta para fluido incompressível é expressa exatamente como $\nabla \cdot \mathbf{V} = 0$. (Seção 14)
7. **Falso.** *Correção:* A derivada $\frac{\partial u}{\partial x} > 0$ é interpretada pelo material como massa *saindo* na direção $x$, não entrando. (Seção 15)
8. **Verdadeiro.** No balanço em 2D apresentado, $-\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$, o que evidencia que a variação na componente de uma direção é equilibrada pela variação na outra. (Seção 17 e 19)
9. **Verdadeiro.** É a definição expressa para compor o vetor velocidade em coordenadas cartesianas no documento. (Seção 11)
10. **Falso.** *Correção:* A forma geral da equação da continuidade (para qualquer fluido) contém explicitamente a variação da densidade no tempo através do termo $\frac{\partial \rho}{\partial t}$. A densidade apenas não varia no caso *incompressível*. (Seções 13 e 14)

---

## Questão 4 — Múltipla Escolha

- **Questão 4.1 — Alternativa (e)**
  - *Justificativa:* A seção 15 afirma que, para o caso incompressível, a densidade não aparece nos termos finais e a lei passa a ser expressa apenas pelo balanceamento das derivadas espaciais das velocidades locais.
- **Questão 4.2 — Alternativa (c)**
  - *Justificativa:* A alternativa (c) reproduz a forma diferencial completa e geral. A (b) é para incompressível, (e) é a forma integral e (d) a vazão mássica.
- **Questão 4.3 — Alternativa (b)**
  - *Justificativa:* O volume de controle é expressamente definido na seção 3 como "um volume fixo no espaço, de forma arbitrária, que contém fluido".
- **Questão 4.4 — Alternativa (b)**
  - *Justificativa:* As seções 4 e 8 elucidam que o sinal negativo foi explicitamente introduzido para representar matematicamente a diminuição da massa interna no volume quando sai mais do que entra.
- **Questão 4.5 — Alternativa (c)**
  - *Justificativa:* A seção 17 ressalta que a velocidade associada à direção $x$ aparece com sinal negativo porque a orientação da normal da respectiva superfície de entrada aponta em sentido oposto ao do vetor da velocidade $u$.

---

## Questão 5 — Análise Dimensional

**Resolução estruturada em seis passos:**

**Passo 1 — Identificar as variáveis dimensionais**
As variáveis dimensionais do problema são $u$, $D$, $\mu$, $\rho$.
Logo, o número total de variáveis dimensionais é $n = 4$.

**Passo 2 — Determinar as dimensões das variáveis**
As dimensões base das quatro variáveis supracitadas são:
- $u: [L T^{-1}]$
- $D: [L]$
- $\mu: [M L^{-1} T^{-1}]$
- $\rho: [M L^{-3}]$

Ou seja, as dimensões primárias são M, L, T, implicando que $m = 3$.

**Passo 3 — Calcular o número de grupos adimensionais**
O número de grupos $\pi$ (adimensionais) é dado por:
$N_{\pi} = n - m = 4 - 3 = 1$
Só existe a possibilidade de apenas um número adimensional neste grupo.

**Passo 4 — Escolher as variáveis repetitivas**
O número de variáveis repetidas é 3 (correspondente a $m$). Foram escolhidas as variáveis $u$, $\mu$ e $\rho$ como variáveis repetidas, sendo $D$ a variável que não se repete.

**Passo 5 — Montar o grupo adimensional Π**
Deve-se gerar o $\pi$ agrupando os parâmetros repetidos juntamente à variável não-repetida:
$\pi_1 = D \rho^a \mu^b u^c$

**Passo 6 — Determinar os expoentes**
Substituindo a equação dimensional, tem-se:
$[M^0 L^0 T^0] = [L] [M L^{-3}]^a [M L^{-1} T^{-1}]^b [L T^{-1}]^c$

Agrupando as dimensões primárias, a expressão torna-se:
$[M^0 L^0 T^0] = [M]^{a+b} [L]^{1 - 3a - b + c} [T]^{-b - c}$

Resultando em um sistema linear de equações (igualando os expoentes a zero):
**M:** $0 = a + b \rightarrow a = -b$
**L:** $0 = 1 - 3a - b + c$
**T:** $0 = -b - c \rightarrow c = -b$

Substituindo $a = -b$ e $c = -b$ na equação da dimensão L:
$0 = 1 - 3(-b) - b + (-b)$
$0 = 1 + 3b - b - b$
$1 + b = 0 \rightarrow b = -1$

Como $a = -b$ e $c = -b$:
$a = -(-1) = 1$
$c = -(-1) = 1$

Então $a = 1$, $b = -1$ e $c = 1$.
Substituindo os expoentes na fórmula de $\pi_1$:
$\pi_1 = D \rho^1 \mu^{-1} u^1$

Ou seja, $\pi_1$ corresponde, no exemplo, ao número de Reynolds, $Re$:
$$
\boxed{Re = \frac{\rho u D}{\mu}}
$$
