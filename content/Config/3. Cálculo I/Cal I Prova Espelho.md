---
tags: [calculo-1, prova, simulado, limites, continuidade, ACON-B]
disciplina: Cálculo I
tema: Prova-Espelho P1 (5 questões, mesma estrutura da prova)
---

# Cálculo I — Prova-Espelho (P1)

> [!info] Como usar
> Mesma estrutura da prova real (5 questões), só com números diferentes. Resolva tudo **sozinho**, sem abrir o gabarito. Confira só no final. O gabarito está no callout colapsável lá embaixo.

---

## 1ª Questão — gráfico de g(x), determine o que se pede em **x = 1**

> [!note] O gráfico
> Parábola para baixo com **bolinha aberta em (1, 5)** (topo) e **bolinha cheia em (1, 2)**. A curva sobe pelos dois lados mirando o 5. (Mesmo tipo da Q1 da prova — descontinuidade removível.)

**1.1)** O valor de $g(x)$, caso exista.

**1.2)** O limite lateral direito: $\displaystyle\lim_{x \to 1^+} g(x)$

**1.3)** O limite lateral esquerdo: $\displaystyle\lim_{x \to 1^-} g(x)$

**1.4)** O limite da função, apresentando a devida justificativa: $\displaystyle\lim_{x \to 1} g(x)$

**1.5)** A continuidade da função, demonstrando matematicamente.

---

## 2ª Questão — Calcule os limites abaixo:

**2.1)** $\displaystyle\lim_{x \to 3} \sqrt[4]{16\,x^8}$

**2.2)** $\displaystyle\lim_{x \to -2} \frac{5x^3}{15x}$

**2.3)** $\displaystyle\lim_{x \to -1} \left( x^5 + x^4 - x^3 + x^2 - x - 20 \right)$

Falta 1 questão parecida com a 3.1 do trabalho.

falta 1 questão parecida com a 5.2 do trabalho. 

---

## 3ª Questão — Encontre os limites abaixo:

**3.1)** $\displaystyle\lim_{x \to 3} \frac{x^3 - 4x^2 + x + 6}{x - 3}$

**3.2)** $\displaystyle\lim_{x \to 3} \frac{x^2 - 7x + 12}{x^2 - 9}$

a 3.1 não está parecida com a 4.1 do trabalho.
---

## 4ª Questão — limites laterais da função por partes, em **x = 2**

$$f(x) = \begin{cases} 3 + x, & \text{se } x < 2 \\ x^2, & \text{se } 2 \le x < 4 \\ 10 - x, & \text{se } x \ge 4 \end{cases}$$

Calcule $\displaystyle\lim_{x \to 2^-} f(x)$, $\displaystyle\lim_{x \to 2^+} f(x)$, e diga se $\displaystyle\lim_{x \to 2} f(x)$ existe.

---

## 5ª Questão — verifique a continuidade em **x = 4**, justificando

$$h(x) = \begin{cases} 3x - 2, & \text{se } x < 4 \\ 6 + x, & \text{se } x \ge 4 \end{cases}$$

---

> [!success]- GABARITO (abra só depois de tentar tudo!)
> ### 1ª Questão (x = 1)
> - **1.1)** $g(1) = 2$ (bolinha cheia)
> - **1.2)** $\lim_{x\to 1^+} g(x) = 5$ (a curva aponta para o 5)
> - **1.3)** $\lim_{x\to 1^-} g(x) = 5$
> - **1.4)** $\lim_{x\to 1} g(x) = 5$ (laterais iguais: $5 = 5$)
> - **1.5)** $\lim_{x\to 1} g(x) = 5 \neq 2 = g(1)$ → **não é contínua** (removível)
>
> ### 2ª Questão
> - **2.1)** $\sqrt[4]{16 \cdot 3^8} = \sqrt[4]{16}\cdot\sqrt[4]{3^8} = 2 \cdot 3^2 = 2\cdot 9 = \mathbf{18}$
> - **2.2)** $\frac{5x^3}{15x} = \frac{x^2}{3} \to \frac{(-2)^2}{3} = \frac{4}{3}$
> - **2.3)** substitui $x=-1$: $-1+1+1+1+1-20 = \mathbf{-17}$
>   (lembre: $(-1)$ par $=+1$, ímpar $=-1$; e $-x^3 = -(-1)=+1$; $-x=-(-1)=+1$)
>
> ### 3ª Questão
> - **3.1)** substitui $x=3$ → $0/0$. Briot-Ruffini de $x^3-4x^2+x+6$ por $(x-3)$: coef. $1,-4,1,6$, raiz $3$ → quociente $x^2-x-2$, resto $0$. Cancela $(x-3)$: $\lim_{x\to3}(x^2-x-2) = 9-3-2 = \mathbf{4}$
> - **3.2)** substitui $x=3$ → $0/0$. Cima $x^2-7x+12=(x-3)(x-4)$; baixo $x^2-9=(x-3)(x+3)$. Cancela $(x-3)$: $\lim_{x\to3}\frac{x-4}{x+3} = \frac{-1}{6} = \mathbf{-\frac{1}{6}}$
>
> ### 4ª Questão (por partes, x = 2)
> - esquerda ($x<2$ → usa $3+x$): $\lim_{x\to2^-} = 3+2 = 5$
> - direita ($2\le x<4$ → usa $x^2$): $\lim_{x\to2^+} = 2^2 = 4$
> - $5 \neq 4$ → $\lim_{x\to2} f(x)$ **não existe** (laterais diferentes)
>
> ### 5ª Questão (por partes, x = 4)
> - **1º** $h(4)$: usa $x\ge4$ → $6+x = 6+4 = 10$
> - **2º** laterais: esq. ($x<4$ → $3x-2$) $= 3\cdot4-2 = 10$; dir. ($x\ge4$ → $6+x$) $= 10$ → limite $= 10$
> - **3º** $\lim_{x\to4} h(x) = 10 = h(4)$ → **logo h é contínua em x = 4**

---

## Links
- [[Cal1-Gabarito-Q1]] — gabarito da Q1 do trabalho (formato do professor)
- [[Cal1-Sinais-Trinomio]] — regra de sinais na fatoração
- [[Cal1-Limites-Fatoracao]] — receita do 0/0
- [[Cal1-Cronograma-Trabalho]] — cronograma de estudo
