---
tags: [calculo-1, limites, continuidade, graficos, ACON-B]
data: 2026-07-24
disciplina: Cálculo I
tema: Interpretação de gráficos — valor, limite lateral, limite e continuidade
---

# Cálculo I — Lendo gráficos: valor, limite e continuidade

> [!abstract] Ideia central
> Três conceitos que **parecem** iguais mas respondem perguntas diferentes:
> - **Valor da função** → *o ponto que está desenhado*
> - **Limite** → *pra onde a curva aponta ao se aproximar*
> - **Continuidade** → *o limite e o valor batem?*
>
> A maior parte dos erros vem de **misturar esses três**. O resto desta nota é sobre mantê-los separados.

---

## 1. As bolinhas: a regra que destrava tudo

Em cada valor de $x$, a função só pode ter **uma** altura. Quando o gráfico mostra bolinhas concorrendo, a regra é:

| Bolinha | Significado |
|---|---|
| ⚫ **Cheia** (fechada) | "O ponto é AQUI." Está **incluído**. |
| ⚪ **Vazia** (aberta) | "O ponto NÃO é aqui." Está **excluído** — é só um lugar que a curva *quase* toca. |

> [!tip] Regra de ouro
> Se há uma cheia e uma vazia na mesma vertical, **a cheia vence** para o valor da função. A vazia é só "de passagem".

---

## 2. Valor da função — $f(a)$

**Pergunta que responde:** "Qual ponto está *desenhado* exatamente em $x = a$?"

- Olhe a vertical de $x = a$ e procure a **bolinha cheia**.
- Se não há bolinha cheia desenhada → **$f(a)$ não existe**.

> [!example] Exemplos da aula
> - **Q1, $x=3$:** nada desenhado sobre o 3 → $f(3)$ **não existe**.
> - **Q2, $x=-2$:** bolinha cheia em $y=2$ → $g(-2) = 2$. (A vazia em $y=4$ é ignorada.)

---

## 3. Limite lateral

**Pergunta que responde:** "Andando pela curva em direção a $x = a$, pra qual altura eu estou mirando?"

> [!important] O limite lateral IGNORA a bolinha
> Não importa se a bolinha é aberta ou fechada. O limite olha **só pra onde a curva aponta**, não pro que está incluído.

### Como ler cada lado

- **Limite pela esquerda** $\displaystyle\lim_{x \to a^-} f(x)$
  Venha de valores **menores** que $a$ (ex: $a-1,\ a-0.5,\ a-0.1$). Pare no instante em que chega em $a$. **Não siga viagem.**

- **Limite pela direita** $\displaystyle\lim_{x \to a^+} f(x)$
  Venha de valores **maiores** que $a$ (ex: $a+1,\ a+0.5,\ a+0.1$). Pare ao chegar em $a$.

> [!warning] Armadilha comum
> Não confunda a altura *onde a curva termina lá na frente* com a altura *logo ao lado de $a$*. O limite lateral só olha o pedacinho **coladinho** em $a$ — faça um "zoom mental" bem perto do ponto.

### Quando a curva dispara

Se a curva sobe/desce **sem parar** perto de $a$ (não existe número onde ela estacione), escrevemos $+\infty$ ou $-\infty$.

> [!note] Infinito = "não existe", com sabor
> Dizer que o limite é $+\infty$ é dizer que ele **não existe**. O símbolo só descreve *como* ele falha (dispara pra cima sem parar).

---

## 4. Limite (bilateral) — $\displaystyle\lim_{x \to a} f(x)$

**Pergunta que responde:** "Os dois lados apontam pro *mesmo* número?"

$$
\lim_{x \to a} f(x) = L
\quad\Longleftrightarrow\quad
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L
$$

- **Concordam** (mesmo número) → o limite existe e vale esse número.
- **Discordam** (números diferentes, ou um $+\infty$ e outro $-\infty$) → o limite **não existe**.

> [!tip] A intuição do "furinho"
> Se a curva chega no $L$ pela esquerda e **continua** a partir do $L$ pela direita, é como uma linha que passa reta por ali com só um furinho no meio (a bolinha vazia). **O limite não enxerga o furo** → o limite é $L$, mesmo que a bolinha cheia esteja em outro lugar.

> [!example] Exemplos da aula
> - **Q1, $x=3$:** esquerda → $-\infty$, direita → $+\infty$. Vão pro infinito em **extremos opostos** → **não concordam** → limite **não existe**.
> - **Q2, $x=-2$:** esquerda → $4$, direita → $4$. **Concordam** → $\displaystyle\lim_{x\to-2} g(x) = 4$. (Não importa que $g(-2)=2$; o limite ignora a bolinha.)

---

## 5. Continuidade em $x = a$

**Pergunta que responde:** "O ponto desenhado está *no lugar certo*, exatamente onde a curva aponta?"

Para $f$ ser contínua em $a$, **as três condições** precisam valer:

1. $f(a)$ **existe** (há bolinha cheia)
2. $\displaystyle\lim_{x \to a} f(x)$ **existe** (os dois lados concordam)
3. $\displaystyle\lim_{x \to a} f(x) = f(a)$ (limite **e** valor são **iguais**)

> [!fail] Basta UMA falhar
> Se qualquer uma das três não vale, a função é **descontínua** em $a$. Você pode justificar pela mais direta.

### Tipos de descontinuidade vistos

| Situação | Nome | Exemplo da aula |
|---|---|---|
| Limite é $\pm\infty$ (curva dispara) | **Descontinuidade infinita** | **Q1, $x=3$** |
| Limite existe, mas $\neq f(a)$ (ponto fora do lugar) | **Descontinuidade removível** | **Q2, $x=-2$**: $\lim = 4 \neq 2 = g(-2)$ |

> [!example] Justificativas formais da aula
> - **Q1:** $f(3)$ não existe $\Rightarrow$ $f$ é descontínua em $x=3$ (descontinuidade infinita).
> - **Q2:** $\displaystyle\lim_{x\to-2} g(x) = 4 \neq 2 = g(-2)$ $\Rightarrow$ $g$ é descontínua em $x=-2$ (removível).

---

## 6. Roteiro rápido para qualquer gráfico

> [!question] Para cada $x = a$ pedido, pergunte nesta ordem:
> 1. **Onde está o $a$?** Suba uma linha vertical imaginária.
> 2. **O que está desenhado ali?** Bolinha cheia? Vazia? Nada? → responde $f(a)$.
> 3. **Vindo da esquerda**, pra qual altura a curva aponta? (zoom coladinho em $a$)
> 4. **Vindo da direita**, pra qual altura a curva aponta?
> 5. **Os dois lados concordam?** → responde o limite bilateral.
> 6. **Limite $=$ valor?** → responde a continuidade.

---

## 7. Erros que eu preciso evitar

- [ ] Deixar a bolinha vazia "roubar" o valor da função → só a **cheia** conta.
- [ ] Deixar a bolinha influenciar o **limite** → o limite **ignora** a bolinha.
- [ ] Seguir viagem pela curva além de $a$ ao calcular o limite lateral → pare **em** $a$.
- [ ] Confundir a altura final da curva (lá na frente) com a altura **coladinha** em $a$.
- [ ] Achar que "os dois vão pro infinito" garante o limite → precisam ir pro **mesmo** infinito.
- [ ] Concluir "contínua" sem checar se limite **e** valor são **iguais**.

---

## Links relacionados
- [[Cal1-Limites-Contas]] *(próxima aula: fatoração, racionalização — Questões 3 e 4)*
- [[Cal1-Limites-Laterais-Funcoes-Definidas]] *(Questão 5: funções por partes)*
