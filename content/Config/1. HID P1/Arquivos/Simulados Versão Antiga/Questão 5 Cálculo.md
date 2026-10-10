---

title: Buckingham-Pi — Resolução em 6 Passos  
tags:

- mecanica-dos-fluidos
    
- analise-dimensional
    
- prova
    

---

# Método de Buckingham–Π

## Passo 1 — Identificar as variáveis

As variáveis do problema são:

- $u$: velocidade;
    
- $D$: diâmetro;
    
- $\mu$: viscosidade dinâmica;
    
- $\rho$: massa específica.
    

Logo, o número de variáveis é:

$$  
\boxed{n=4}  
$$

---

## Passo 2 — Determinar as dimensões

As dimensões de cada variável são:

$$  
[u]=LT^{-1}  
$$

$$  
[D]=L  
$$

$$  
[\mu]=ML^{-1}T^{-1}  
$$

$$  
[\rho]=ML^{-3}  
$$

As dimensões primárias são massa ($M$), comprimento ($L$) e tempo ($T$).

Portanto:

$$  
\boxed{m=3}  
$$

---

## Passo 3 — Calcular o número de grupos adimensionais

Aplicando o teorema de Buckingham–Π:

$$  
N_{\Pi}=n-m  
$$

Substituindo os valores:

$$  
N_{\Pi}=4-3=1  
$$

Portanto, existe **um grupo adimensional**:

$$  
\boxed{N_{\Pi}=1}  
$$

---

## Passo 4 — Escolher as variáveis repetitivas

**Variáveis repetitivas:**

$$  
u,\ \mu,\ \rho  
$$

**Variável não repetitiva:**

$$  
D  
$$

---

## Passo 5 — Formar o grupo adimensional

Multiplicamos a variável não repetitiva pelas variáveis repetitivas elevadas a expoentes desconhecidos:

$$  
\boxed{\Pi_1=D\rho^a\mu^bu^c}  
$$

Os expoentes $a$, $b$ e $c$ serão determinados para que o grupo seja adimensional.

---

## Passo 6 — Determinar os expoentes

Como $\Pi_1$ é adimensional:

$$  
[L][ML^{-3}]^a[ML^{-1}T^{-1}]^b[LT^{-1}]^c  
$$

Agrupando as dimensões:

$$  
M^{a+b}L^{1-3a-b+c}T^{-b-c}=M^0L^0T^0  
$$

Igualando os expoentes a zero:

$$  
\begin{cases}  
a+b=0\  
1-3a-b+c=0\  
-b-c=0  
\end{cases}  
$$

Resolvendo:

$$  
\boxed{a=1,\quad b=-1,\quad c=1}  
$$

Substituindo em $\Pi_1=D\rho^a\mu^bu^c$:

$$  
\boxed{\Pi_1=Re=\frac{\rho uD}{\mu}}  
$$

____

# Roteiro para memorizar os 6 passos

|Passo|O que fazer|Resultado principal|
|---|---|---|
|1|Identificar as variáveis|$n=4$|
|2|Determinar as dimensões|$m=3$|
|3|Calcular os grupos|$N_{\Pi}=4-3=1$|
|4|Escolher as repetitivas|$u,\mu,\rho$; não repetitiva: $D$|
|5|Montar o grupo|$\Pi_1=D\rho^a\mu^bu^c$|
|6|Resolver os expoentes|$Re=\dfrac{\rho uD}{\mu}$|