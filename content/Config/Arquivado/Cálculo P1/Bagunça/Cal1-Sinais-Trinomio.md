---
tags: [calculo-1, fatoracao, trinomio, sinais, ACON-B]
disciplina: Cálculo I
tema: Regra de sinais na fatoração de trinômios
---

# Fatorar Trinômio — a Regra dos Sinais

> [!abstract] A ideia
> Trinômio: **x² + (meio)x + (último)**. Para fatorar, acho **dois números** que:
> - **multiplicam** o último termo
> - **somam** o do meio
>
> O que trava a maioria é o **sinal** desses dois números. Esta nota resolve isso com um mapa de decisão.

---

## O mapa de decisão (olhe DOIS sinais)

Você olha o sinal do **último termo** primeiro, depois o do **meio**.

> [!important] Passo 1 — olhe o ÚLTIMO termo
> - **ÚLTIMO POSITIVO** → os dois números têm o **MESMO sinal**. Aí o meio decide qual:
>     - meio **+** → os dois **POSITIVOS**
>     - meio **−** → os dois **NEGATIVOS**
> - **ÚLTIMO NEGATIVO** → os dois números têm **SINAIS DIFERENTES** (um + e um −).
>     - o número **MAIOR** leva o sinal do **MEIO**.

### Em tabela

| Último termo | Meio | Sinais dos dois números |
|---|---|---|
| **positivo** | **+** | os dois **+** |
| **positivo** | **−** | os dois **−** |
| **negativo** | **+** | diferentes — o **maior é +** |
| **negativo** | **−** | diferentes — o **maior é −** |

---

## Os quatro casos, com exemplo

> [!example] Caso 1 — último +, meio +  →  os dois positivos
> **x² + 6x + 8**
> Números que multiplicam 8 e somam 6: **2 e 4** (ambos +).
> → **(x + 2)(x + 4)**

> [!example] Caso 2 — último +, meio −  →  os dois negativos
> **x² − 6x + 8**
> Multiplicam 8, somam −6: **−2 e −4**.
> Confere: (−2)(−4) = +8 ✓   (−2)+(−4) = −6 ✓
> → **(x − 2)(x − 4)**

> [!example] Caso 3 — último −, meio +  →  diferentes, maior é +
> **x² + 3x − 10**
> Multiplicam −10 (sinais diferentes), somam +3. Pares de 10: 2 e 5.
> Meio é **+**, então o maior (5) é **+**: **+5 e −2**.
> Confere: (+5)(−2) = −10 ✓   (+5)+(−2) = +3 ✓
> → **(x + 5)(x − 2)**

> [!example] Caso 4 — último −, meio −  →  diferentes, maior é −
> **x² − 3x − 10**
> Mesmos pares (2 e 5), multiplicam −10.
> Meio é **−**, então o maior (5) é **−**: **−5 e +2**.
> Confere: (−5)(+2) = −10 ✓   (−5)+(+2) = −3 ✓
> → **(x − 5)(x + 2)**

> [!tip] Casos 3 e 4 são "gêmeos"
> Mesmos números (2 e 5), só muda **qual leva o menos** — e quem decide é o sinal do meio.

---

## Regras de sinais de apoio

> [!note] Multiplicação
> - sinais **iguais** → **positivo**   ( (+)(+)=+ ;  (−)(−)=+ )
> - sinais **diferentes** → **negativo**   ( (+)(−)=− )

> [!note] Soma / subtração
> - sinais **iguais** → **junta** e mantém o sinal   ( (−5)+(−3) = −8 )
> - sinais **diferentes** → **subtrai** e fica com o sinal do **maior**   ( (+7)+(−3) = +4 )

---

## Passo a passo completo

> [!question] Para fatorar qualquer x² + bx + c:
> 1. **Liste os pares** que MULTIPLICAM o último termo (lista curta).
> 2. **Teste a soma** em cada par → ache o que dá o do meio.
> 3. **Decida o sinal** pelo mapa acima (olhe último, depois meio).
> 4. **Escreva** (x + n1)(x + n2), cada número com seu sinal.
> 5. (Opcional) **Confira**: multiplique de volta e veja se dá o trinômio original.

> [!info] Ordem não importa
> (x − 4)(x − 5) é o mesmo que (x − 5)(x − 4). O que NÃO pode mudar é o sinal de cada número.

---

## Checklist rápido (na prova)

- [ ] Olhei o sinal do ÚLTIMO termo?
- [ ] Último +? → mesmos sinais (meio decide + ou −)
- [ ] Último −? → sinais diferentes (maior leva o sinal do meio)
- [ ] Conferi multiplicando de volta?

## Links
- [[Cal1-Limites-Fatoracao]]  *(receita 0/0: substitui → fatora → cancela → substitui)*
- [[Cal1-Limites-Graficos-Aula]]  *(leitura de gráficos)*
