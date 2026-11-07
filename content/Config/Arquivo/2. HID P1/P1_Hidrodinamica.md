---
aliases:
- Simulado P1 Hidrodinâmica I
tags:
- hidrodinamica
- engenharia
- estudo
- prova
title: P1 Hidrodinâmica I --- Resumo completo
---


------------------------------------------------------------------------

## 2. Questões de múltipla escolha

### Questão 1 --- Escoamento permanente e incompressível em duto divergente

Em um escoamento permanente e incompressível de água através de um duto
divergente:

-   **Permanente:** as propriedades do escoamento em um ponto não variam
    com o tempo.
-   **Incompressível:** a massa específica permanece constante.
-   **Duto divergente:** a área da seção transversal aumenta.
-   Com o aumento da área, a velocidade diminui.
-   A aceleração convectiva longitudinal é negativa.

A aceleração convectiva longitudinal é:

$$
a_c = u\\frac{\\partial u}{\\partial x}
$$

**Alternativas do simulado:**

  -----------------------------------------------------------------------
  Alternativa                         Afirmação
  ----------------------------------- -----------------------------------
  A                                   A massa específica aumenta e a
                                      velocidade aumenta.

  B                                   A aceleração local é
                                      necessariamente positiva.

  C                                   A velocidade diminui e a aceleração
                                      convectiva longitudinal é negativa.

  D                                   A velocidade permanece constante em
                                      qualquer seção.

  E                                   A aceleração convectiva é sempre
                                      nula em regime permanente.
  -----------------------------------------------------------------------

> \[!success\] Gabarito: C Em duto divergente, a velocidade diminui e a
> aceleração convectiva longitudinal é negativa.

### Questão 2 --- Equação da continuidade

A equação da continuidade expressa a **conservação da massa**.

Para um escoamento tridimensional incompressível:

$$
\\frac{\\partial u}{\\partial x}
+\\frac{\\partial v}{\\partial y}
+\\frac{\\partial w}{\\partial z}=0
$$

Onde:

-   $u$: velocidade na direção $x$.
-   $v$: velocidade na direção $y$.
-   $w$: velocidade na direção $z$.
-   $\\rho$: massa específica.

**Por que a massa específica não aparece?**

Como a massa específica é constante no escoamento incompressível, ela
pode ser fatorada e cancelada na equação.

**Alternativas do simulado:**

  ------------------------------------------------------------------------------------------------------------------
  Alternativa                         Afirmação
  ----------------------------------- ------------------------------------------------------------------------------
  A                                   $\\partial u/\\partial x+\\partial v/\\partial y+\\partial w/\\partial z=0$;
                                      $\\rho$ é constante e pode ser fatorada e cancelada.

  B                                   A soma das derivadas é igual a $\\rho$; a densidade cresce no tempo.

  C                                   $\\partial\\rho/\\partial t=0$; isso, isoladamente, garante continuidade.

  D                                   $\\nabla\\cdot V=\\rho$; a massa específica é a divergência.

  E                                   $\\nabla\\cdot V=1$; a água tem volume constante.
  ------------------------------------------------------------------------------------------------------------------

> \[!success\] Gabarito: A Para $\\rho$ constante, a continuidade
> reduz-se a $\\nabla\\cdot V=0$.

### Questão 3 --- Aceleração de uma partícula fluida na descrição euleriana

A descrição euleriana analisa o comportamento do fluido em pontos do
espaço.

A aceleração material é formada pela soma de duas parcelas:

**Aceleração local**

Representa a variação da velocidade em relação ao tempo em determinado
ponto:

$$
a_l=\\frac{\\partial u}{\\partial t}
$$

**Aceleração convectiva**

Representa a variação da velocidade em relação à posição:

$$
a_c=u\\frac{\\partial u}{\\partial x}
$$

**Derivada material unidimensional:**

$$
\\boxed{
\\frac{Du}{Dt}
=
\\frac{\\partial u}{\\partial t}
+u\\frac{\\partial u}{\\partial x}
}
$$

Em regime permanente, a aceleração local é nula, mas a aceleração
convectiva ainda pode existir.

**Alternativas do simulado:**

  Alternativa   Afirmação
  ------------- -----------------------------------------------------------
  A             Em regime permanente, toda aceleração é nula.
  B             A aceleração local depende apenas da posição.
  C             $Du/Dt=\\partial u/\\partial t-u\\partial u/\\partial x$.
  D             $Du/Dt=\\partial u/\\partial t+u\\partial u/\\partial x$.
  E             A aceleração convectiva é $\\partial u/\\partial t$.

> \[!success\] Gabarito: D **Observação do documento:** esta questão
> está identificada como provável.

### Questão 4 --- Segunda lei de Newton aplicada a um volume infinitesimal

Ao aplicar a segunda lei de Newton a um elemento infinitesimal de
fluido, é necessário considerar as forças que atuam nele.

As forças são divididas em:

-   **Forças de superfície:** atuam nas superfícies do elemento, como as
    forças de pressão.
-   **Forças de corpo:** atuam no volume do elemento.

A força resultante de pressão na direção $x$ é:

$$
\\boxed{
F_x=-\\frac{\\partial p}{\\partial x}dV
}
$$

Onde:

-   $p$: pressão.
-   $dV$: volume infinitesimal.
-   $\\partial p/\\partial x$: variação da pressão na direção $x$.

O sinal negativo indica que a força aponta no sentido de pressão
decrescente, isto é, da maior para a menor pressão.

**Alternativas do simulado:**

  -------------------------------------------------------------------------
  Alternativa                         Afirmação
  ----------------------------------- -------------------------------------
  A                                   $F_x=+(\\partial p/\\partial x)dV$,
                                      sempre na direção de maior pressão.

  B                                   $F_x=-(\\partial p/\\partial x)dV$,
                                      apontando da maior para a menor
                                      pressão.

  C                                   $F_x=\\rho dV$, independentemente da
                                      pressão.

  D                                   $F_x=-p/dV$.

  E                                   $F_x=0$ para qualquer gradiente de
                                      pressão.
  -------------------------------------------------------------------------

> \[!success\] Gabarito: B O sinal negativo indica força no sentido de
> pressão decrescente.

### Questão 5 --- Condições de contorno em paredes sólidas

Em uma parede sólida, fixa e impermeável, aplicam-se duas condições
cinemáticas ao fluido viscoso.

**1. Não escorregamento**

A velocidade tangencial do fluido junto à parede é igual a zero:

$$
V_t=0
$$

**2. Impenetrabilidade**

A velocidade normal à parede também é igual a zero:

$$
V_n=0
$$

Portanto, o fluido não escorrega sobre a parede nem atravessa sua
superfície.

**Alternativas do simulado:**

  -----------------------------------------------------------------------
  Alternativa                         Afirmação
  ----------------------------------- -----------------------------------
  A                                   Velocidade normal diferente de zero
                                      e tangencial livre.

  B                                   Pressão e massa específica
                                      necessariamente nulas.

  C                                   Velocidade tangencial máxima e
                                      normal máxima.

  D                                   Apenas a condição de pressão
                                      constante.

  E                                   Não escorregamento e
                                      impenetrabilidade: velocidades
                                      tangencial e normal nulas na
                                      parede.
  -----------------------------------------------------------------------

> \[!success\] Gabarito: E Parede fixa e impermeável: velocidades normal
> e tangencial iguais a zero.

------------------------------------------------------------------------

## 3. Questão 6 --- Complete as lacunas

A questão reúne definições e conceitos fundamentais de Hidrodinâmica.

### 6a. Propriedades físicas fundamentais

Duas propriedades físicas fundamentais do fluido:

-   **Massa específica**
-   **Viscosidade**

### 6b. Equação da continuidade

A equação da continuidade expressa a conservação da:

-   **Massa**

### 6c. Aceleração material

Na descrição euleriana, a aceleração material resulta da soma das
acelerações:

-   **Local**
-   **Convectiva**

### 6d. Forças em um elemento fluido

As forças que atuam em um elemento fluido dividem-se em:

-   **Superfície**
-   **Corpo**

### 6e. Escoamentos de Couette e Poiseuille

-   **Couette:** escoamento laminar entre placas devido ao movimento de
    uma placa.
-   **Poiseuille:** escoamento impulsionado por gradiente de pressão.

### 6f. Número de Reynolds

O número de Reynolds representa a razão entre efeitos de:

-   **Inércia**
-   **Viscosidade**

$$
Re=\\frac{\\text{efeitos de inércia}}
{\\text{efeitos de viscosidade}}
$$

------------------------------------------------------------------------

## 4. Questão 7 --- Verdadeiro ou falso

**Tema:** análise dimensional e teorema de Buckingham.

### Afirmação I

Em uma equação dimensionalmente homogênea, os termos somados possuem as
mesmas dimensões.

> \[!success\] VERDADEIRO Os termos somados precisam apresentar as
> mesmas dimensões.

### Afirmação II

O teorema $\\Pi$ de Buckingham estabelece que $k=n-m$ grupos
adimensionais.

> \[!success\] VERDADEIRO

Fórmula:

$$
\\boxed{k=n-m}
$$

Onde:

-   $k$: quantidade de grupos adimensionais.
-   $n$: número total de variáveis.
-   $m$: número de dimensões fundamentais independentes.

### Afirmação III

As variáveis repetidas podem ser dimensionalmente dependentes.

> \[!danger\] FALSO De acordo com o gabarito do documento, as variáveis
> repetidas não podem ser dimensionalmente dependentes.

### Afirmação IV

Para 7 variáveis e 3 dimensões fundamentais independentes, formam-se 4
grupos adimensionais.

> \[!success\] VERDADEIRO

Aplicação:

$$
k=7-3=4
$$

Resultado: **4 grupos adimensionais**.

------------------------------------------------------------------------

## 5. Questão 8 --- Aplicação de cálculo

O documento informa que essa questão será baseada em um exercício
fornecido separadamente pelo professor.

O enunciado não foi reproduzido no arquivo.

Informações disponíveis:

-   É uma questão de cálculo.
-   O exercício já foi fornecido separadamente.
-   O tema não foi revelado no áudio.
-   A questão está reservada para o cálculo passado em aula.

> \[!warning\] Atenção É necessário revisar o exercício específico
> fornecido pelo professor. O documento não contém dados suficientes
> para reconstruir o cálculo.

------------------------------------------------------------------------

## 6. Gabarito geral

  Questão   Resposta
  --------- ---------------------------------
  1         C
  2         A
  3         D
  4         B
  5         E
  6a        Massa específica e viscosidade
  6b        Massa
  6c        Local e convectiva
  6d        Superfície e corpo
  6e        Couette e Poiseuille
  6f        Inércia e viscosidade
  7-I       Verdadeiro
  7-II      Verdadeiro
  7-III     Falso
  7-IV      Verdadeiro
  8         Cálculo fornecido separadamente

------------------------------------------------------------------------

