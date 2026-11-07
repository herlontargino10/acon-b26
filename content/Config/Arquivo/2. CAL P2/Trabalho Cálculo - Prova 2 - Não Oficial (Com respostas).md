---
title: 2º Trabalho de Cálculo I
tags:
  - calculo1
  - matematica
  - derivadas
  - integrais
---

# 2º Trabalho de Cálculo I (NÃO OFICIAL)

---

> [!abstract] Informações e Regras
> 1. O trabalho deverá ser entregue, impreterivelmente, no dia da prova;
> 2. Este trabalho terá valor de $2{,}0$ (dois) pontos, que serão somados aos $8{,}0$ (oito) pontos referentes à primeira prova, compondo a nota final da primeira avaliação.

---

## 1ª Questão: Derivadas Elementares

Calcule a derivada de cada uma das funções abaixo:

### 1.1) $f(x) = 186{,}57$
Como $f(x)$ é uma função constante:
$$f'(x) = 0$$

---

### 1.2) $g(x) = \sqrt[4]{30}$
Como $\sqrt[4]{30}$ é um valor numérico constante independente de $x$:
$$g'(x) = 0$$

---

### 1.3) $h(u) = A u^3 + B u^2 + C u$
Aplicando a regra da potência ($\frac{d}{du}[u^n] = n u^{n-1}$) com constantes $A, B, C$:
$$h'(u) = 3A u^2 + 2B u + C$$

---

### 1.4) $y = 5 e^x + 1$ 
Aplicando a derivada da exponencial natural e da constante:

$$y' = 5e^x+0$$

---

### 1.5) $S(p) = \sqrt{p} - p$
Reescrevendo a raiz como potência fracionária:
$$S(p) = p^{1/2} - p$$
Derivando em relação a $p$:
$$S'(p) = \frac{1}{2}p^{-1/2} - 1 = \frac{1}{2\sqrt{p}} - 1$$

---

### 1.6) $y = x^{5/3} - x^{2/3}$
Aplicando a regra da potência a cada termo:
$$\frac{d}{dx}\left(x^{5/3}\right) = \frac{5}{3}x^{\frac{5}{3} - 1} = \frac{5}{3}x^{2/3}$$
$$\frac{d}{dx}\left(x^{2/3}\right) = \frac{2}{3}x^{\frac{2}{3} - 1} = \frac{2}{3}x^{-1/3}$$
Logo:
$$y' = \frac{5}{3}x^{2/3} - \frac{2}{3}x^{-1/3}$$

Ou, na forma de raízes:
$$y' = \frac{5\sqrt[3]{x^2}}{3} - \frac{2}{3\sqrt[3]{x}} = \frac{5x - 2}{3\sqrt[3]{x}}$$

---

### 1.7) $f(x) = x^{2{,}4} + x^{-3} - x^{-2/5}$
Aplicando a regra da potência termo a termo:
$$f'(x) = 2{,}4 x^{1{,}4} - 3x^{-4} - \left(-\frac{2}{5}\right)x^{-7/5}$$
$$f'(x) = 2{,}4 x^{1{,}4} - \frac{3}{x^4} + \frac{2}{5 x^{7/5}}$$

---

### 1.8) $h(x) = x^5 - x^3 + x^2 + 17x - 8$
Derivando cada termo polinomial:
$$h'(x) = 5x^4 - 3x^2 + 2x + 17$$

---

## 2ª Questão: Equação da Reta Tangente

Encontre uma equação da reta tangente a curva onde $x = a$:

### 2.1) $f(x) = x^4 + 2x^2 - x$, $a = 1$

1. **Determinar o ponto de tangência $f(1)$:**
   $$f(1) = 1^4 + 2(1)^2 - 1 = 1 + 2 - 1 = 2 \implies (1, 2)$$

2. **Determinar a derivada geral $f'(x)$:**
   $$f'(x) = 4x^3 + 4x - 1$$

3. **Calcular a inclinação $m = f'(1)$:**
   $$m = f'(1) = 4(1)^3 + 4(1) - 1 = 4 + 4 - 1 = 7$$

4. **Equação da reta tangente:**
   $$y - 2 = 7(x - 1) \implies y - 2 = 7x - 7$$
   $$y = 7x - 5$$

---

### 2.2) $y = 3x^2 - x^3$, $a = 1$

1. **Determinar o ponto de tangência $y(1)$:**
   $$y(1) = 3(1)^2 - (1)^3 = 3 - 1 = 2 \implies (1, 2)$$

2. **Determinar a derivada geral $y'$:**
   $$y' = 6x - 3x^2$$

3. **Calcular a inclinação $m = y'(1)$:**
   $$m = y'(1) = 6(1) - 3(1)^2 = 6 - 3 = 3$$

4. **Equação da reta tangente:**
   $$y - 2 = 3(x - 1) \implies y - 2 = 3x - 3$$
   $$y = 3x - 1$$

---

## 3ª Questão: Regras do Produto, Quociente e Trigonométricas

Calcule a derivada das funções abaixo:

### 3.1) $f(x) = (x^3 + 2x)e^x$
Aplicando a regra do produto $(u \cdot v)' = u'v + uv'$:
- $u = x^3 + 2x \implies u' = 3x^2 + 2$
- $v = e^x \implies v' = e^x$

$$f'(x) = (3x^2 + 2)e^x + (x^3 + 2x)e^x$$
Fatorando $e^x$:
$$f'(x) = (x^3 + 3x^2 + 2x + 2)e^x$$

---

### 3.2) $g(x) = (5x^4 - 3x^3 + 5x - 8)\cos(x)$
Pela regra do produto:
- $u = 5x^4 - 3x^3 + 5x - 8 \implies u' = 20x^3 - 9x^2 + 5$
- $v = \cos(x) \implies v' = -\sin(x)$

$$g'(x) = (20x^3 - 9x^2 + 5)\cos(x) - (5x^4 - 3x^3 + 5x - 8)\sin(x)$$

---

### 3.3) $y = \frac{x^3}{1 - x^2}$
Aplicando a regra do quociente $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
- $u = x^3 \implies u' = 3x^2$
- $v = 1 - x^2 \implies v' = -2x$

$$y' = \frac{3x^2(1 - x^2) - x^3(-2x)}{(1 - x^2)^2} = \frac{3x^2 - 3x^4 + 2x^4}{(1 - x^2)^2}$$
$$y' = \frac{3x^2 - x^4}{(1 - x^2)^2} = \frac{x^2(3 - x^2)}{(1 - x^2)^2}$$

---

### 3.4) $s(t) = \frac{t}{(t - 1)^2}$
Aplicando a regra do quociente:
- $u = t \implies u' = 1$
- $v = (t - 1)^2 \implies v' = 2(t - 1)$

$$s'(t) = \frac{1 \cdot (t - 1)^2 - t \cdot 2(t - 1)}{(t - 1)^4}$$
Colocando o fator $(t - 1)$ em evidência no numerador:
$$s'(t) = \frac{(t - 1)[(t - 1) - 2t]}{(t - 1)^4} = \frac{(t - 1 - 2t)}{(t - 1)^3} = \frac{-t - 1}{(t - 1)^3} = -\frac{t + 1}{(t - 1)^3}$$

---

### 3.5) $f(x) = 3x^2 - 2\cos(x)$
Sabendo que $\frac{d}{dx}[\cos(x)] = -\sin(x)$:
$$f'(x) = 6x - 2(-\sin(x)) = 6x + 2\sin(x)$$

---

### 3.6) $g(x) = \frac{1}{2}\sin(x) - \frac{7}{4}\cos(x) + 7$
Derivando termo a termo:
$$g'(x) = \frac{1}{2}\cos(x) - \frac{7}{4}(-\sin(x)) + 0$$
$$g'(x) = \frac{1}{2}\cos(x) + \frac{7}{4}\sin(x)$$

---

## 4ª Questão: Integrais Indefinidas

Encontre a integral das funções abaixo:

### 4.1) $\int \left(\frac{1}{x^2} - 8\right) dx$
Reescrevendo a fração como expoente negativo:
$$\int (x^{-2} - 8) dx = \frac{x^{-1}}{-1} - 8x + C = -\frac{1}{x} - 8x + C$$

---

### 4.2) $\int (x^3 - 6x) dx$
Integrando termo a termo:
$$\int (x^3 - 6x) dx = \frac{x^4}{4} - 6 \cdot \frac{x^2}{2} + C = \frac{x^4}{4} - 3x^2 + C$$

---

### 4.3) $\int \left(x^{-3} + \frac{2}{3}x^{3/2} - 6e^x + 4\right) dx$
Integrando termo a termo:
$$\int x^{-3} dx = \frac{x^{-2}}{-2} = -\frac{1}{2x^2}$$
$$\int \frac{2}{3}x^{3/2} dx = \frac{2}{3} \cdot \frac{x^{5/2}}{\frac{5}{2}} = \frac{2}{3} \cdot \frac{2}{5} x^{5/2} = \frac{4}{15}x^{5/2}$$
$$\int -6e^x dx = -6e^x$$
$$\int 4 dx = 4x$$

**Resultado final:**
$$-\frac{1}{2x^2} + \frac{4}{15}x^{5/2} - 6e^x + 4x + C$$

---

### 4.4) $\int -\frac{2}{3}e^x dx$
$$\int -\frac{2}{3}e^x dx = -\frac{2}{3}e^x + C$$

---

## 5ª Questão: Análise Gráfica de Funções

Observe o gráfico e encontre o que é pedido:


![[Pasted image 20261012130751.png]]

### 5.1) $f(3/2) = ?$
Olhando a linha tracejada vertical em $x = \frac{3}{2}$, ela atinge a curva no valor correspondente do eixo $y$:
$$f\left(\frac{3}{2}\right) = 2$$

---

### 5.2) $f(1) = ?$
Olhando a linha tracejada vertical em $x = 1$, ela sobe até o topo local com altura $y = 2$:
$$f(1) = 2$$

---

### 5.3) Identifique um ponto de mínimo relativo
Observando os vales (pontos mais baixos locais):
- No trecho inicial, há um mínimo em $x = 0$ com $y \approx 1{,}4$ (ou ponto $(0; 1{,}4)$).
- Há também outros mínimos locais nos vales entre $x = \frac{1}{2}$ e $x = 1$ e entre $x = 1$ e $x = \frac{3}{2}$.
- **Exemplo de ponto:** $(0; f(0))$ ou aproximadamente $(0; 1{,}4)$.

---

### 5.4) Identifique um ponto de máximo relativo
Observando as cristas/picos da curva:
- Existe um máximo relativo local em $x = 1$, correspondente ao ponto $(1, 2)$.
- Existem cristas mais altas em $x = \frac{1}{2}$ e aproximadamente em $x \approx 1{,}6$, onde $y = \frac{5}{2}$ (ou valor assinalado entre $2$ e $3$, como $\frac{9}{4}$ / $2{,}25$).
- **Resposta direta:** O ponto **$(1, 2)$** é um ponto de máximo relativo claro assinalado no gráfico.