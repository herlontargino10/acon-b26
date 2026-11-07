---
title: 2º Trabalho de Cálculo I
tags:
  - calculo1
  - matematica
  - derivadas
  - integrais
---

# 2º Trabalho de Cálculo I

**Código:** ACOM-B-01/2026  
**Data:** ____/____/2026  
**Nome:** ___________________________________________________  

> [!abstract] Informações e Regras
> 1. O trabalho deverá ser entregue, impreterivelmente, no dia da prova; e
> 2. Este trabalho terá valor de $2{,}0$ (dois) pontos, que serão somados aos $8{,}0$ (oito) pontos referentes à primeira prova, compondo a nota final da primeira avaliação.

---

## 1ª Questão: Derivadas Elementares

Calcule a derivada de cada uma das funções abaixo:

### 1.1) $f(x) = 186{,}57$
Como $f(x)$ é uma função constante:
$$f'(x) = 0$$

### 1.2) $g(x) = \sqrt[4]{30}$
Como $\sqrt[4]{30}$ é uma constante real independente de $x$:
$$g'(x) = 0$$

### 1.3) $h(u) = Au^3 + Bu^2 + Cu$
Aplicando a regra do tombo / potência ($\frac{d}{du}[u^n] = n u^{n-1}$):
$$h'(u) = 3A u^2 + 2B u + C$$

### 1.4) $y = 5e^x + 1$
Aplicando a derivada da exponencial natural e da constante:
$$y' = 5\frac{d}{dx}(e^x) + \frac{d}{dx}(1)$$
$$y' = 5e^x$$

### 1.5) $S(p) = \sqrt{p} - p$
Escrevendo na forma potencial:
$$S(p) = p^{1/2} - p$$
Derivando em relação a $p$:
$$S'(p) = \frac{1}{2}p^{-1/2} - 1 = \frac{1}{2\sqrt{p}} - 1$$

### 1.6) $y = x^{5/3} - x^{2/3}$
Aplicando a regra da potência a cada termo:
$$\frac{d}{dx}\left(x^{5/3}\right) = \frac{5}{3}x^{\frac{5}{3} - 1} = \frac{5}{3}x^{2/3}$$
$$\frac{d}{dx}\left(x^{2/3}\right) = \frac{2}{3}x^{\frac{2}{3} - 1} = \frac{2}{3}x^{-1/3}$$

Logo:
$$y' = \frac{5}{3}x^{2/3} - \frac{2}{3}x^{-1/3}$$
Ou, na forma de raízes:
$$y' = \frac{5\sqrt[3]{x^2}}{3} - \frac{2}{3\sqrt[3]{x}} = \frac{5x - 2}{3\sqrt[3]{x}}$$

### 1.7) $f(x) = x^{2{,}4} + x^{-3} - x^{-2/5}$
Derivando termo a termo pela regra da potência:
$$f'(x) = 2{,}4 x^{1{,}4} - 3x^{-4} - \left(-\frac{2}{5}\right)x^{-\frac{7}{5}}$$
$$f'(x) = 2{,}4 x^{1{,}4} - \frac{3}{x^4} + \frac{2}{5x^{7/5}}$$

### 1.8) $h(x) = x^5 - x^3 + x^2 + 17x - 8$
Derivando o polinômio:
$$h'(x) = 5x^4 - 3x^2 + 2x + 17$$

---

## 2ª Questão: Equação da Reta Tangente

A equação da reta tangente a uma curva no ponto de abscissa $x = a$ é dada por:
$$y - f(a) = f'(a)(x - a)$$

### 2.1) $f(x) = x^4 + 2x^2 - x$, no ponto $a = 1$
1. **Ponto de tangência:**
   $$f(1) = 1^4 + 2(1)^2 - 1 = 1 + 2 - 1 = 2 \implies (1, 2)$$
2. **Derivada da função:**
   $$f'(x) = 4x^3 + 4x - 1$$
3. **Coeficiente angular ($m$):**
   $$m = f'(1) = 4(1)^3 + 4(1) - 1 = 7$$
4. **Equação da reta:**
   $$y - 2 = 7(x - 1) \implies y = 7x - 5$$

### 2.2) $y = 3x^2 - x^3$, no ponto $a = 1$
1. **Ponto de tangência:**
   $$y(1) = 3(1)^2 - (1)^3 = 3 - 1 = 2 \implies (1, 2)$$
2. **Derivada da função:**
   $$y' = 6x - 3x^2$$
3. **Coeficiente angular ($m$):**
   $$m = y'(1) = 6(1) - 3(1)^2 = 3$$
4. **Equação da reta:**
   $$y - 2 = 3(x - 1) \implies y = 3x - 1$$

---

## 3ª Questão: Regras do Produto, Quociente e Funções Trigonométricas

### 3.1) $f(x) = (x^3 + 2x)e^x$
Pela regra do produto $[u \cdot v]' = u'v + uv'$:
* $u = x^3 + 2x \implies u' = 3x^2 + 2$
* $v = e^x \implies v' = e^x$

$$f'(x) = (3x^2 + 2)e^x + (x^3 + 2x)e^x = (x^3 + 3x^2 + 2x + 2)e^x$$

### 3.2) $g(x) = (5x^4 - 3x^3 + 5x - 8)\cos(x)$
Pela regra do produto:
$$g'(x) = (20x^3 - 9x^2 + 5)\cos(x) + (5x^4 - 3x^3 + 5x - 8)(-\sin(x))$$
$$g'(x) = (20x^3 - 9x^2 + 5)\cos(x) - (5x^4 - 3x^3 + 5x - 8)\sin(x)$$

### 3.3) $y = \frac{x^3}{1 - x^2}$
Pela regra do quociente $\left[\frac{u}{v}\right]' = \frac{u'v - uv'}{v^2}$:
$$y' = \frac{3x^2(1 - x^2) - x^3(-2x)}{(1 - x^2)^2} = \frac{3x^2 - 3x^4 + 2x^4}{(1 - x^2)^2}$$
$$y' = \frac{3x^2 - x^4}{(1 - x^2)^2} = \frac{x^2(3 - x^2)}{(1 - x^2)^2}$$

### 3.4) $s(t) = \frac{t}{(t - 1)^2}$
Aplicando a regra do quociente:
$$s'(t) = \frac{1 \cdot (t - 1)^2 - t \cdot 2(t - 1)}{(t - 1)^4}$$
Fatorando $(t - 1)$ no numerador:
$$s'(t) = \frac{(t - 1)[(t - 1) - 2t]}{(t - 1)^4} = \frac{-t - 1}{(t - 1)^3} = -\frac{t + 1}{(t - 1)^3}$$

### 3.5) $f(x) = 3x^2 - 2\cos(x)$
$$f'(x) = 6x - 2(-\sin(x)) = 6x + 2\sin(x)$$

### 3.6) $g(x) = \frac{1}{2}\sin(x) - \frac{7}{4}\cos(x) + 7$
$$g'(x) = \frac{1}{2}\cos(x) - \frac{7}{4}(-\sin(x)) + 0 = \frac{1}{2}\cos(x) + \frac{7}{4}\sin(x)$$

---

## 4ª Questão: Integrais Indefinidas

### 4.1) $\int \left(\frac{1}{x^2} - 8\right) dx$
$$\int (x^{-2} - 8) dx = \frac{x^{-1}}{-1} - 8x + C = -\frac{1}{x} - 8x + C$$

### 4.2) $\int (x^3 - 6x) dx$
$$\int (x^3 - 6x) dx = \frac{x^4}{4} - 6 \cdot \frac{x^2}{2} + C = \frac{x^4}{4} - 3x^2 + C$$

### 4.3) $\int \left(x^{-3} + \frac{2}{3}x^{3/2} - 6e^x + 4\right) dx$
Integrando termo a termo:
1. $\int x^{-3} dx = \frac{x^{-2}}{-2} = -\frac{1}{2x^2}$
2. $\int \frac{2}{3}x^{3/2} dx = \frac{2}{3} \cdot \frac{x^{5/2}}{5/2} = \frac{2}{3} \cdot \frac{2}{5} x^{5/2} = \frac{4}{15}x^{5/2}$
3. $\int -6e^x dx = -6e^x$
4. $\int 4 dx = 4x$

$$\int \left(x^{-3} + \frac{2}{3}x^{3/2} - 6e^x + 4\right) dx = -\frac{1}{2x^2} + \frac{4}{15}x^{5/2} - 6e^x + 4x + C$$

### 4.4) $\int -\frac{2}{3}e^x dx$
$$\int -\frac{2}{3}e^x dx = -\frac{2}{3}e^x + C$$

### 4.5) $\int \left(5\sin(x) + \frac{1}{4}\cos(x)\right) dx$
$$-5\cos(x) + \frac{1}{4}\sin(x) + C$$

---

## 5ª Questão: Análise Gráfica de Funções

Observando a imagem nítida fornecida:

> [!note] Leitura das referências do gráfico
> - No eixo $y$, as marcas principais mostram o nível tracejado superior em $y = \frac{9}{4}$ (dois picos atingem este valor).
> - Em $x = 1$, há uma descontinuidade pontual (círculo aberto / "bola aberta") exatamente na altura tracejada $y = 2$.
> - A reta tracejada vertical em $x = \frac{3}{2}$ cruza a curva na altura $y = 2$.

### 5.1) $f(3/2) = ?$
Seguindo a linha tracejada vertical em $x = \frac{3}{2}$, o ponto pertence à curva no cruzamento com a reta horizontal de ordenada $2$:
$$f\left(\frac{3}{2}\right) = 2$$

### 5.2) $f(1) = ?$
Olhando atentamente para $x = 1$, há um **ponto aberto** (círculo não preenchido) em $(1, 2)$ sem nenhum outro ponto fechado definido para essa abscissa:
* **Não existe / Não está definido** (ou seja, $1 \notin \text{Dom}(f)$).
*(Nota: caso o professor considere o limite ou a curva sem descontinuidade formal, o valor correspondente à altura é $2$).*

### 5.3) Identifique um ponto de mínimo relativo
São os vales (pontos mais baixos locais) da curva. Pela escala do eixo $x$:
* Ponto de mínimo em $x = 0$ com altura aproximada $(0; 1{,}4)$.
* Ponto de mínimo no vale em $x = 2$ com altura aproximada $(2; 1{,}3)$.
* Pontos de mínimo intermediários nos vales em torno de $x \approx 0{,}8$ e $x \approx 1{,}2$.

> **Exemplo de resposta:** O ponto de mínimo local no intervalo visível pode ser identificado em $(2; 1{,}3)$ ou no vale inicial $(0; 1{,}4)$.

### 5.4) Identifique um ponto de máximo relativo
São os picos locais da curva:
* Ponto de máximo local em $x = \frac{1}{2}$: $\left(\frac{1}{2}, \frac{9}{4}\right)$.
* Outro pico local de altura máxima correspondente em $x \approx 1{,}6$: $\left(1{,}6; \frac{9}{4}\right)$.
*(Observação: o pico central em $x = 1$ possui círculo aberto na ordenada $2$, portanto os máximos relativos bem definidos são os picos em que $y = \frac{9}{4}$).*