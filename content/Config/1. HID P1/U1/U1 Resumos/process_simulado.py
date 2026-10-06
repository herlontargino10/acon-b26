import os

source_file = "2_Simulado_Hidrodinamica_Capitulo_1.md"
target_file = "2_Simulado_Hidrodinamica_Capitulo_1_COMENTADO.md"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

gabarito = """
<GABARITO COMENTADO>
## Questão 1

### 1.1
**Resposta correta:** C

**Por que está correta:**
A Seção 3 define o volume de controle como uma região onde "o fluido pode entrar ou sair", e a Seção 4 apresenta o balanço de massa que equaciona essas entradas e saídas.

**Análise das alternativas:**
- **A)** Errada — O fluido pode entrar e sair do volume de controle e a massa é conservada localmente (Seção 7).
- **B)** Errada — A conservação aplica-se a uma região fixa por onde o fluido passa, não exigindo que a massa fique parada no mesmo local (Seção 3).
- **D)** Errada — A conservação da massa estabelece que a massa não pode ser criada ou desaparecer (Seção 1).
- **E)** Errada — O volume de controle é usado justamente para analisar o fluido quando este atravessa suas superfícies (Seções 1 e 3).

**Conceito cobrado:** Conservação da massa e volume de controle.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 1.2
**Resposta correta:** B

**Por que está correta:**
A Seção 3 define explicitamente o volume de controle como "um volume fixo no espaço, de forma arbitrária... O fluido pode entrar ou sair dele."

**Análise das alternativas:**
- **A)** Errada — É uma região fixa no espaço, não acompanha partículas individuais de fluido (Seção 3).
- **C)** Errada — É uma região de forma arbitrária escolhida para a análise, não necessariamente uma caixa física (Seção 3).
- **D)** Errada — O material da Unidade I não fornece informação suficiente para justificar esta alternativa de forma segura.
- **E)** Errada — Representa uma região espacial para análise, não exclusivamente a massa armazenada (Seção 22).

**Conceito cobrado:** Volume de controle.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 1.3
**Resposta correta:** B

**Por que está correta:**
Pela fórmula da vazão mássica $\dot m = \rho u A$ (Seção 5) e considerando densidade constante para fluido incompressível (Seção 14), se a área diminui, a velocidade deve necessariamente aumentar para manter o balanço de massa e a mesma vazão mássica.

**Análise das alternativas:**
- **A)** Errada — Uma diminuição na velocidade reduziria a vazão mássica, violando o balanço de massa.
- **C)** Errada — A massa não pode ser criada ou desaparecer (Seção 1).
- **D)** Errada — O termo incompressível indica que a densidade é constante, logo ela não aumenta (Seção 14).
- **E)** Errada — A vazão não desaparece, pois a massa não pode desaparecer (Seção 1).

**Conceito cobrado:** Vazão e continuidade.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 1.4
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão e suas alternativas de forma segura.
**Conceito cobrado:** Regime permanente.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 1.5
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão e suas alternativas de forma segura.
**Conceito cobrado:** Perfil de Couette.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 2

### 2.1
**Resposta correta:** C

**Por que está correta:**
A análise da variação de área e velocidade deve considerar a conservação da massa através das seções, cujo balanço é explicitamente equacionado no material por meio da vazão mássica $\dot m = \rho u A$ (Seções 4 e 5).

**Análise das alternativas:**
- **A), B), D), E)** Erradas — O material da Unidade I não fornece informação suficiente para justificar essas alternativas de forma segura como sendo fatores exclusivos ("somente"), pois o foco principal da relação velocidade/área no resumo é a conservação de massa/vazão.

**Conceito cobrado:** Balanço de massa em tubulações.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 2.2
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão e suas alternativas de forma segura.
**Conceito cobrado:** Descrição Euleriana e Lagrangiana.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 2.3
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão e suas alternativas de forma segura.
**Conceito cobrado:** Relação de pressão, velocidade e energia.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 2.4
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão e suas alternativas de forma segura.
**Conceito cobrado:** Efeito Squat.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 2.5
**Resposta correta:** C

**Por que está correta:**
A equação da continuidade é a própria lei de conservação da massa (Seção 13), e o material mostra que ela consiste no balanço entre as taxas de entrada, saída e variação interna para satisfazer a conservação local (Seções 4 e 7).

**Análise das alternativas:**
- **A)** Errada — Tratando-se de fluido incompressível, a densidade é constante (Seção 14).
- **B)** Errada — O material foca explicitamente nas variações espaciais da velocidade, não exigindo que ela seja igual em todos os pontos (Seção 20).
- **D)** Errada — A continuidade é aplicada a um volume de controle pelo qual o fluido livremente escoa/se move (Seção 3).
- **E)** Errada — Se o escoamento é constante e incompressível (1D), o que entra deve ser exatamente o que sai (Seção 16).

**Conceito cobrado:** Equação da continuidade e interpretação física.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 3

### 3.1
**Resposta correta:** Vazão mássica.
**Por que está correta:** A Seção 5 define a vazão mássica como "a taxa de quantidade de fluido por unidade de tempo que passa por uma face".
**Conceito cobrado:** Definição de vazão mássica.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 3.2
**Resposta correta:** Volume de controle.
**Por que está correta:** A Seção 3 define o volume de controle como "um volume fixo no espaço, de forma arbitrária, que contém fluido" usado para a análise do escoamento.
**Conceito cobrado:** Definição de volume de controle.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 3.3
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão de forma segura.
**Conceito cobrado:** Descrição do movimento de fluidos.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 3.4
**Resposta correta:** Equação da continuidade.
**Por que está correta:** A Seção 13 afirma que a lei de conservação da massa também é conhecida como "equação da continuidade".
**Conceito cobrado:** Equação de conservação da massa.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 3.5
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão de forma segura.
**Conceito cobrado:** Perfil de velocidade de Couette.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 4

### 4.1
**Resposta correta:** Falso.
**Por que está correta / Análise das alternativas:** A Seção 3 afirma que o volume de controle é uma região arbitrária através da qual o fluido pode entrar e sair livremente, não implicando que deva permanecer parado.
**Conceito cobrado:** Escoamento no volume de controle.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 4.2
**Resposta correta:** Verdadeiro.
**Por que está correta / Análise das alternativas:** De acordo com o balanço de massa (Seções 8 e 28), se a entrada de massa supera a saída, existe aumento (acúmulo) da massa interna armazenada.
**Conceito cobrado:** Balanço de massa e armazenamento.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 4.3
**Resposta correta:** Falso.
**Por que está correta / Análise das alternativas:** A Seção 3 define o volume de controle como um volume de forma arbitrária no espaço escolhido para a análise, e não necessariamente uma caixa física construída em volta do fluido (Seção 22).
**Conceito cobrado:** Definição do volume de controle.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 4.4
**Resposta correta:** Falso.
**Por que está correta / Análise das alternativas:** A Seção 20 e as Pegadinhas (Seção 22) ressaltam fortemente que o balanço se dá pelas variações espaciais da velocidade (suas derivadas espaciais, como $\frac{\partial u}{\partial x}$), e não pelo balanço das velocidades propriamente ditas.
**Conceito cobrado:** Equação da continuidade (Forma Diferencial Incompressível).
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 4.5
**Resposta correta:** N/A
**Por que está correta / Análise das alternativas:** O material da Unidade I não fornece informação suficiente para justificar esta questão de forma segura.
**Conceito cobrado:** Escoamento de Couette.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

## Questão 5

### 5.1
**Respostas corretas e explicação:**
- **a)** O material da Unidade I não fornece informação suficiente para calcular ou justificar o conceito de "vazão volumétrica" de forma segura.
- **b)** O material indica que para o caso incompressível 1D (Seção 16), o que entra deve ser exatamente o que sai, mantendo o balanço de massa. Usando a vazão mássica $\dot m = \rho u A$ (Seção 5) com densidade constante (Seção 14), tem-se: $u_A A_A = u_B A_B \Rightarrow 2 \cdot 0,04 = u_B \cdot 0,01 \Rightarrow u_B = 8 \, m/s$.
- **c)** Fisicamente (Seções 1 e 5), para conservar a massa que atravessa o volume, a redução na área de passagem exige que o fluido escoe a uma velocidade maior para compensar e manter constante a quantidade de massa transportada por unidade de tempo.
**Conceito cobrado:** Conservação da massa (continuidade) com mudança de área.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md

### 5.2
**Respostas corretas e explicação:**
- **a)** Pelo balanço de massa (Seções 4, 6 e 8), a taxa de variação é a diferença entre a massa que entra e a massa que sai: $\frac{\Delta m}{\Delta t} = \dot m_{in} - \dot m_{out} = 12 - 8 = 4 \, kg/s$.
- **b)** A massa armazenada aumenta.
- **c)** Explicando fisicamente, o material enfatiza (Seção 8 e Pegadinhas da Seção 22) que, como há mais massa entrando do que saindo, o saldo positivo se acumula no interior do volume de controle, aumentando a massa armazenada.
**Conceito cobrado:** Balanço de massa e taxa de variação.
**Fonte principal:** 001-006_Mecanica_dos_Fluidos_Capitulo_1.md
</GABARITO COMENTADO>
"""

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content + "\n" + gabarito)

print("Done")
