## 1. Visão geral

Este documento compila o estudo consolidado das questões **1.1 a 1.8** de Cálculo I. O objetivo principal deste bloco de exercícios é dominar a **derivação direta de funções por meio da regra da potência (regra do tombo)** e compreender o comportamento de diferentes tipos de termos, coeficientes e constantes.

  
### Conceitos Centrais Estudados

- **Funções Constantes:** Derivada de um valor numérico fixo ou expressão sem a variável independente (seja um decimal, inteiro ou radical).
    
      
    
- **Constantes Multiplicativas e Termos Lineares:** Manutenção de coeficientes que multiplicam variáveis e comportamento da derivada de termos de primeiro grau.
    
      
    
- **Regra da Potência (Regra do Tombo):** Aplicação da fórmula $(x^n)' = n \cdot x^{n-1}$ em expoentes inteiros positivos, inteiros negativos, decimais e fracionários.
    
      
    
- **Reescrita e Conversão de Radicais:** Transformação de raízes em expoentes fracionários para viabilizar a derivação.
    
      
    
- **Ajuste de Sinais e Simplificação de Notação:** Multiplicação de sinais ao tombar expoentes negativos e omissão de coeficientes unitários explícitos (escrever $C$ em vez de $1C$).
    
      
    

## 2. Questão 1.1 — Derivada de uma constante

### Enunciado

$$f(x) = 186{,}57$$

### Conceito

Derivada de uma função constante. Como a expressão consiste em um número real puro e não possui a variável independente $x$, a função não sofre variação à medida que $x$ muda.

  

### Resolução Comentada

1. Identifica-se que $186{,}57$ é um valor constante.
    
      
    
2. Aplica-se a regra fundamental de derivação de constantes:
    
      
    
    $$f'(x) = 0$$
    

### Regra Prática

Se a expressão independe da variável em relação à qual se está derivando, ela é uma constante isolada e sua derivada é **zero**.

  

### Erros e Cuidados

- Não tentar aplicar a regra do tombo diretamente em um número sem variável.
    
      
    
- Não confundir o número decimal com um coeficiente de variável $x$.
    
      
    

## 3. Questão 1.2 — Constante escrita como radical

### Enunciado

$$g(x) = \sqrt[4]{30}$$

### Conceito

Constante representada em forma de radical. O termo possui índice e radical, porém permanece sem a presença da variável $x$.

  

### Resolução Comentada

1. Observa-se que a expressão $\sqrt[4]{30}$ não contém a variável $x$.
    
      
    
2. Por se tratar de um número real fixo, sua taxa de variação é nula:
    
      
    
    $$g'(x) = 0$$
    

### Regra Prática

Um radical sem variável é uma **constante**. O índice da raiz não deve ser confundido com um expoente de variável.

  

### Erros e Cuidados

- Não tentar reescrever $\sqrt[4]{30}$ como $30^{1/4}$ para depois descer o expoente $\frac{1}{4}$. A regra do tombo se aplica apenas a bases variáveis ($x^n$).
    
      
    

## 4. Questão 1.3 — Regra da potência e constantes multiplicativas

### Enunciado

$$h(u) = Au^3 + Bu^2 + Cu$$

### Conceito

Derivação termo a termo de uma função polinomial onde $u$ é a variável independente e $A$, $B$ e $C$ atuam como constantes multiplicativas (coeficientes genéricos).

  

### Resolução Comentada

1. **Primeiro termo ($Au^3$):** Aplica-se a regra do tombo em $u^3$, mantendo a constante $A$:
    
      
    
    $$(Au^3)' = A \cdot (3u^{3-1}) = 3Au^2$$
    
2. **Segundo termo ($Bu^2$):** Aplica-se a regra do tombo em $u^2$, mantendo a constante $B$:
    
      
    
    $$(Bu^2)' = B \cdot (2u^{2-1}) = 2Bu$$
    
3. **Terceiro termo ($Cu$):** Deriva-se o termo linear em $u$:
    
      
    
    $$(Cu)' = C \cdot (1u^{1-1}) = C \cdot u^0 = C \cdot 1 = C$$
    

### Resultado Final

$$h'(u) = 3Au^2 + 2Bu + C$$

### Regra Prática

- Quando uma constante está multiplicando a variável, **a constante se mantém** no cálculo.
    
      
    
- A derivada de qualquer termo linear do $1^\circ$ grau ($C \cdot u$) resulta apenas na própria constante ($C$).
    
      
    

## 5. Questão 1.4 — Regra da potência, simplificação e derivada da constante

### Observação sobre o Registro das Questões

Nos registros do trabalho, os itens **1.3** e **1.4** apresentaram a mesma expressão $h(u) = Au^3 + Bu^2 + Cu$. Na tutoria, o item **1.4** foi utilizado para aprofundar os conceitos de simplificação de notação e o comportamento de termos constantes adicionais.

  

### Enunciado

$$h(u) = Au^3 + Bu^2 + Cu$$

### Resolução Comentada e Aprofundamentos

1. **Derivação de $Au^3$ e $Bu^2$:**
    
      
    
    $$(Au^3)' = 3Au^2 \quad \text{e} \quad (Bu^2)' = 2Bu$$
    
2. **Derivação de $Cu$ e Simplificação de Notação:**
    
    A aplicação da regra resulta em $1C$. Na convenção algébrica e nas exigências formais de exames, o coeficiente $1$ deve ser omitido, escrevendo-se unicamente **$C$**.
    
      
    
3. **Fundamentação da Derivada de uma Constante Isolada (Explicada durante a tutoria):**
    
      
    - **Visão Gráfica:** A derivada representa a inclinação da reta tangente. Uma função constante $y = c$ é uma reta horizontal, cuja inclinação (variação) é $0$.
        
          
        
    - **Demonstração Matemática:** Reescrevendo a constante $1$ como $1 \cdot u^0$:
        
          
        
        $$(1)' = (1 \cdot u^0)' = 0 \cdot 1 \cdot u^{0-1} = 0$$
        

### Resultado Final

$$h'(u) = 3Au^2 + 2Bu + C$$

### Erros e Cuidados

- **Não escrever $1C$ na resposta final.** A forma simplificada padronizada é $C$.
    
      
    
- Diferenciar constante isolada de constante multiplicativa:
    
      
    - Constante multiplicando variável: se mantém ($(5u)' = 5$).
        
          
        
    - Constante isolada: vira zero ($(5)' = 0$).
        
          
        

## 6. Questão 1.5 — Raiz quadrada e termo linear negativo

### Enunciado

$$S(p) = \sqrt{p} - p$$

### Conceito

Derivação de função com radical simples e termo linear com sinal negativo.

  

### Resolução Comentada

1. **Derivada da primeira parte ($\sqrt{p}$):**
    
      
    - Escreve-se a raiz quadrada em forma de potência: $\sqrt{p} = p^{1/2}$.
        
          
        
    - Aplica-se a regra do tombo:
        
          
        
        $$\left(p^{1/2}\right)' = \frac{1}{2} \cdot p^{\frac{1}{2} - 1} = \frac{1}{2} \cdot p^{-1/2}$$
        
    - Reescreve-se o expoente negativo no denominador como raiz:
        
          
        
        $$\frac{1}{2p^{1/2}} = \frac{1}{2\sqrt{p}}$$
        
2. **Derivada da segunda parte ($-p$):**
    
      
    - Escreve-se $-p$ na forma explicita $-1 \cdot p^1$.
        
          
        
    - Aplicando o tombo:
        
          
        
        $$(-1 \cdot p^1)' = 1 \cdot (-1) \cdot p^{1-1} = -1 \cdot p^0 = -1$$
        

### Resultado Final

$$S'(p) = \frac{1}{2\sqrt{p}} - 1$$

### Regras Práticas

- **Regra da Raiz Quadrada:** $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$ ($1$ sobre o dobro da raiz).
    
      
    
- **Variável de $1^\circ$ Grau Negativa:** A derivada de $-x$ ou $-p$ é sempre **$-1$**.
    
      
    

## 7. Questão 1.6 — Expoentes fracionários

### Enunciado

$$y = x^{5/3} - x^{2/3}$$

### Conceito

Aplicação da regra da potência em expoentes fracionários positivos.

  

### Resolução Comentada

1. **Derivada do primeiro termo ($x^{5/3}$):**
    
      
    - Desce o expoente $\frac{5}{3}$.
        
          
        
    - Subtrai $1$ do expoente:
        
          
        
        $$\frac{5}{3} - 1 = \frac{5}{3} - \frac{3}{3} = \frac{2}{3}$$
        
    - Termo derivado: $\frac{5}{3} x^{2/3}$
        
          
        
2. **Derivada do segundo termo ($-x^{2/3}$):**
    
      
    - Desce o expoente $\frac{2}{3}$ preservando o sinal negativo.
        
          
        
    - Subtrai $1$ do expoente:
        
          
        
        $$\frac{2}{3} - 1 = \frac{2}{3} - \frac{3}{3} = -\frac{1}{3}$$
        
    - Termo derivado: $-\frac{2}{3} x^{-1/3}$
        
          
        

### Formas de Apresentação da Resposta Final

- **Forma Exponencial Direta:**
    
      
    
    $$y' = \frac{5}{3} x^{2/3} - \frac{2}{3} x^{-1/3}$$
    
- **Forma Convertida em Radicais:**
    
    Transformando $x^{2/3} = \sqrt[3]{x^2}$ e $x^{-1/3} = \frac{1}{\sqrt[3]{x}}$:
    
      
    
    $$y' = \frac{5\sqrt[3]{x^2}}{3} - \frac{2}{3\sqrt[3]{x}}$$
    

### Regra Prática

Para subtrair $1$ de uma fração $\frac{a}{b}$, faz-se a operação rápida no numerador mantendo o denominador:

  

$$\frac{a}{b} - 1 = \frac{a - b}{b}$$

## 8. Questão 1.7 — Expoentes decimais, negativos e fracionários

### Enunciado

$$f(x) = x^{2{,}4} + x^{-3} - x^{-2/5}$$

### Conceito

Derivação de múltiplos termos com expoentes decimais, inteiros negativos e fracionários negativos.

  

### Resolução Comentada

1. **Primeiro termo ($x^{2,4}$):**
    
      
    
    $$2{,}4 \cdot x^{2{,}4 - 1} = 2{,}4 x^{1{,}4}$$
    
2. **Segundo termo ($+x^{-3}$):**
    
      
    - Tombando o expoente $-3$ com parênteses para preservação de sinal:
        
          
        
        $$+\left(-3\right) \cdot x^{-3 - 1} = -3 x^{-4}$$
        
3. **Terceiro termo ($-x^{-2/5}$):**
    
      
    - Tombando o expoente $-\frac{2}{5}$ sobre o sinal de menos que antecede a variável:
        
          
        
        $$-\left(-\frac{2}{5}\right) \cdot x^{-\frac{2}{5} - 1} = +\frac{2}{5} x^{-\frac{2}{5} - \frac{5}{5}} = +\frac{2}{5} x^{-7/5}$$
        

### Resultado Final

$$f'(x) = 2{,}4 x^{1{,}4} - 3 x^{-4} + \frac{2}{5} x^{-7/5}$$

### Regras Práticas

- **Subtração em Expoentes Negativos:** Ao subtrair $1$ de um número negativo, aumenta-se o valor absoluto do expoente negativo (ex.: $-3 - 1 = -4$; $-\frac{2}{5} - 1 = -\frac{7}{5}$).
    
      
    
- **Confronto de Sinais:**
    
      
    - $+ (-n) \implies -$
        
          
        
    - $- (-n) \implies +$
        
          
        

## 9. Questão 1.8 — Derivação termo a termo de um polinômio

### Enunciado

$$h(x) = x^5 - x^3 + x^2 + 17x - 8$$

### Conceito

Derivação direta de um polinômio de grau 5 aplicando as regras básicas termo a termo.

  

### Resolução Comentada

- Termo $x^5$: $5 \cdot x^{5-1} = 5x^4$
    
      
    
- Termo $-x^3$: $-3 \cdot x^{3-1} = -3x^2$
    
      
    
- Termo $+x^2$: $+2 \cdot x^{2-1} = +2x$
    
      
    
- Termo $+17x$: $+17$
    
      
    
- Termo $-8$: $0$
    
      
    

### Resultado Final

$$h'(x) = 5x^4 - 3x^2 + 2x + 17$$

## 10. Resumo prático para consulta rápida

### Guia de Regras por Tipo de Termo

|**Estrutura do Termo**|**Função f(x)**|**Derivada f′(x)**|**Exemplo Prático**|
|---|---|---|---|
|**Constante isolada**|$c$|$0$|$(186{,}57)' = 0$, $(\sqrt[4]{30})' = 0$, $(-8)' = 0$|
|**Termo linear**|$c \cdot x$|$c$|$(17x)' = 17$, $(Cu)' = C$, $(-p)' = -1$|
|**Potência inteira positiva**|$x^n$|$n \cdot x^{n-1}$|$(x^5)' = 5x^4$|
|**Potência inteira negativa**|$x^{-n}$|$-n \cdot x^{-n-1}$|$(x^{-3})' = -3x^{-4}$|
|**Raiz quadrada simples**|$\sqrt{x}$|$\frac{1}{2\sqrt{x}}$|$(\sqrt{p})' = \frac{1}{2\sqrt{p}}$|
|**Expoente fracionário**|$x^{a/b}$|$\frac{a}{b} \cdot x^{\frac{a-b}{b}}$|$(x^{5/3})' = \frac{5}{3}x^{2/3}$|
|**Expoente decimal**|$x^{d}$|$d \cdot x^{d-1}$|$(x^{2,4})' = 2,4x^{1,4}$|

## 11. Erros e cuidados importantes

1. **Confundir constante isolada com coeficiente:**
    
      
    - Incorreto: A derivada de $17x$ ser $0$.
        
          
        
    - Correto: O coeficiente se mantém no termo linear: $(17x)' = 17$.
        
          
        
2. **Subtração incorreta em expoentes negativos:**
    
      
    - Incorreto: $-3 - 1 = -2$.
        
          
        
    - Correto: $-3 - 1 = -4$.
        
          
        
3. **Não multiplicar os sinais ao tombar expoentes negativos:**
    
      
    - Incorreto: Derivar $-x^{-2/5}$ resultando em $-\frac{2}{5}x^{-7/5}$.
        
          
        
    - Correto: O sinal do expoente multiplica o sinal da frente: $-\left(-\frac{2}{5}\right)x^{-7/5} = +\frac{2}{5}x^{-7/5}$.
        
          
        
4. **Manter coeficientes unitários explícitos:**
    
      
    - Incorreto: Escrever $1C$ na resposta da derivada de $Cu$.
        
          
        
    - Correto: Escrever apenas $C$.
        
          
        
5. **Derivar constantes sob radicais como se fossem variáveis:**
    
      
    - Incorreto: Tratar $\sqrt[4]{30}$ descendo o expoente $\frac{1}{4}$.
        
          
        
    - Correto: Como não há variável $x$, a expressão é uma constante e sua derivada é $0$.
        
          
        

## 12. Checklist de resolução

Ao resolver um exercício de derivação de termos somados ou subtraídos, verifique os seguintes passos:

  

- [ ] Identifiquei a variável independente da função (ex.: $x$, $u$, $p$).
    
      
    
- [ ] Verifiquei se existem termos constantes isolados (que devem resultar em $0$).
    
      
    
- [ ] Reescrevi os radicais em formato de potência fracionária ($x^{m/n}$).
    
      
    
- [ ] Apliquei a regra do tombo descendo o expoente multiplicando o coeficiente existente.
    
      
    
- [ ] Utilizei parênteses ao descer expoentes negativos para garantir a multiplicação de sinais correta.
    
      
    
- [ ] Subtraí $1$ do expoente com atenção aos sinais e às frações ($\frac{a-b}{b}$).
    
      
    
- [ ] Mantive apenas os coeficientes nos termos de primeiro grau ($cx \to c$).
    
      
    
- [ ] Omita o coeficiente $1$ das respostas finais.
    
      
    

## 13. Revisão ativa

### Perguntas

1. Qual é a derivada de $f(x) = \sqrt[5]{12}$ e qual a justificativa para esse resultado?
    
      
    
2. Qual é o resultado da derivada do termo linear $-x$?
    
      
    
3. Ao derivar $x^{-5}$, qual deve ser o novo expoente e o coeficiente resultante?
    
      
    
4. Qual é a regra prática direta para a derivada de $\sqrt{x}$?
    
      
    
5. Como fica o sinal e o novo expoente ao derivar o termo $-x^{-3/4}$?
    
      
    
6. Por que o resultado final da derivada de $Cu$ é escrito como $C$ e não como $1C$?
    
      
    

### Gabarito da revisão ativa

1. **Resposta:** $f'(x) = 0$. Justificativa: $\sqrt[5]{12}$ é uma constante, pois não depende da variável $x$. A taxa de variação de qualquer constante é zero.
    
      
    
2. **Resposta:** $-1$. O termo $-x$ pode ser lido como $-1 \cdot x^1$, cuja derivada resulta no coeficiente $-1$.
    
      
    
3. **Resposta:** Resposta: $-5x^{-6}$. O expoente $-5$ desce multiplicando e a subtração fica $-5 - 1 = -6$.
    
      
    
4. **Resposta:** $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$ ($1$ dividido pelo dobro da raiz).
    
      
    
5. **Resposta:** $+\frac{3}{4}x^{-7/4}$. A multiplicação de sinais leva a $-\left(-\frac{3}{4}\right) = +\frac{3}{4}$, e o novo expoente é $-\frac{3}{4} - 1 = -\frac{7}{4}$.
    
      
    
6. **Resposta:** Porque na convenção algébrica o coeficiente $1$ fica implícito ($1 \cdot C = C$), sendo essa a forma simplificada exigida em Cálculo I.