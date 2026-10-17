---
title: "Gabarito comentado — Simulado U2 — Homogeneidade e Análise Dimensional"
subject: "Mecânica dos Fluidos"
tags:
  - gabarito
  - unidade-2
  - analise-dimensional
---

# Gabarito comentado — Simulado de Hidrodinâmica — Unidade II

**Fonte exclusiva:** PDF *O Princípio da Homogeneidade e Análise Dimensional*. As respostas e os comentários abaixo se limitam aos conceitos, à terminologia e aos exemplos apresentados nessa apostila.

---

## 1ª Questão — Assinale a alternativa correta

**Resposta: (b) I, II, III e IV, apenas.**

- **I — Verdadeira.** O princípio da homogeneidade dimensional exige que os termos de uma equação que são somados ou subtraídos tenham as mesmas dimensões.
- **II — Verdadeira.** A apostila chama de normalizada a equação cujos termos são adimensionais e da ordem da unidade.
- **III — Verdadeira.** O número de Euler é apresentado como a adimensionalização natural da pressão e como a relação entre forças de pressão e forças de inércia.
- **IV — Verdadeira.** O número de Reynolds indica a importância relativa entre forças de inércia e forças viscosas.
- **V — Falsa.** A apostila afirma que, na prática, não é possível satisfazer simultaneamente os requisitos de similaridade de Reynolds, Froude e Weber em testes de modelos de navios.

---

## 2ª Questão — Complete as lacunas

1. **homogeneidade**.
2. **normalizada**.
3. **restritiva**.
4. **tempo**.
5. **\(\rho u^2L^2\)**.
6. **Euler**.
7. **inércia**.
8. **viscosas**.
9. **Newton**.
10. **gravitacionais**.
11. **livres**.
12. **superficial**.
13. **experimentais**.
14. **adimensionais**.
15. **\(m\)**.

**Comentários:**

- As respostas 1–4 vêm da seção sobre homogeneidade dimensional e variáveis dimensionais/adimensionais.
- As respostas 5–12 vêm do desenvolvimento das forças de inércia, dos números de Euler, Reynolds, Froude e Weber e da lei da viscosidade de Newton.
- As respostas 13–15 vêm das seções sobre finalidades da análise dimensional e teorema π de Buckingham.

---

## 3ª Questão — Verdadeiro ou falso

**Gabarito:** V, F, V, V, V, V, V, F, V, V, V, F, V, V, F.

1. **Verdadeira.** A apostila define uma equação adimensional como aquela cujos termos não têm dimensão.
2. **Falsa.** Para ser normalizada, além de adimensional, a equação deve ter termos da ordem da unidade.
3. **Verdadeira.** A normalização é descrita como mais restritiva do que a adimensionalização.
4. **Verdadeira.** Segundo a apostila, quando o número de Euler é grande, as forças de pressão são maiores que as forças de inércia.
5. **Verdadeira.** A apostila afirma que, quando Reynolds é muito alto, as forças viscosas podem ser negligenciadas.
6. **Verdadeira.** O texto associa Reynolds à transição entre regime laminar e turbulento.
7. **Verdadeira.** O número de Froude tem efeito dominante em escoamentos com superfícies livres.
8. **Falsa.** O número de Weber relaciona forças de inércia e forças de tensão superficial.
9. **Verdadeira.** Uma das finalidades da análise dimensional é obter leis de escala para prever o desempenho do protótipo a partir do modelo.
10. **Verdadeira.** Buckingham–\(\Pi\) permite descobrir grupos adimensionais a partir de variáveis dimensionais.
11. **Verdadeira.** A primeira etapa consiste em listar as variáveis e contar o total, incluindo a variável dependente.
12. **Falsa.** A apostila orienta que as variáveis sejam independentes; dá como exemplo evitar usar simultaneamente \(u\), \(A\) e \(Q=uA\).
13. **Verdadeira.** A similaridade geométrica significa que o navio e o modelo têm a mesma forma.
14. **Verdadeira.** Na similaridade cinemática, as velocidades correspondentes são proporcionais por um fator de escala constante.
15. **Falsa.** O texto afirma que, na prática, só é possível satisfazer um dos três requisitos de similaridade discutidos; os outros devem ser sacrificados.

---

## 4ª Questão — Múltipla escolha

### 4.1 — Resposta (b): Equação normalizada

A apostila define como normalizada a equação cujos termos são adimensionais e da ordem da unidade.

### 4.2 — Resposta (c): Euler

O número de Euler é apresentado como a adimensionalização natural da pressão.

### 4.3 — Resposta (b): Reynolds

O número de Reynolds relaciona forças de inércia e forças viscosas.

### 4.4 — Resposta (d): Froude

A apostila destaca o efeito dominante de Froude em escoamentos com superfícies livres, como resistência de navios, ondas de superfície e canais abertos.

### 4.5 — Resposta (a): forças de inércia e de tensão superficial

Essa é a relação física atribuída ao número de Weber no material.

### 4.6 — Resposta (c): \(n-m\)

A apostila usa a diferença entre o número de variáveis dimensionais \(n\) e o número de dimensões fundamentais independentes \(m\) para contar os grupos π nos exemplos apresentados.

### 4.7 — Resposta (b): forças correspondentes proporcionais pelo mesmo fator

A similaridade dinâmica exige que as forças existentes no escoamento sejam escaladas por um mesmo fator.

### 4.8 — Resposta (c): incompatibilidade dos ajustes de velocidade

A apostila explica que a igualdade de Froude exige uma condição de velocidade diferente daquela exigida para igualar Reynolds e Weber quando o modelo é menor e se utiliza o mesmo fluido.

---

## 5ª Questão — Cálculo de Análise Dimensional

**Objetivo:** obter um grupo adimensional com as variáveis \(\Delta p\), \(u\), \(\rho\) e \(L\), conforme o exemplo de Euler apresentado na apostila.

### Passo 1 — Listar as variáveis e contá-las

As variáveis são:

- diferença de pressão: \(\Delta p\);
- velocidade característica: \(u\);
- massa específica: \(\rho\);
- comprimento característico: \(L\).

Logo, \(n=4\).

### Passo 2 — Identificar as dimensões primárias

Usam-se as dimensões fundamentais massa (\(M\)), comprimento (\(L\)) e tempo (\(T\)); portanto, \(m=3\).

As dimensões das variáveis são:

\[
[\Delta p]=ML^{-1}T^{-2}
\]

\[
[u]=LT^{-1}
\]

\[
[\rho]=ML^{-3}
\]

\[
[L]=L
\]

### Passo 3 — Calcular o número de grupos \(\pi\)

\[
n-m=4-3=1
\]

Portanto, há um grupo adimensional independente.

### Passo 4 — Escolher as variáveis repetidas

Seguindo o exemplo da apostila, escolhem-se \(u\), \(\rho\) e \(L\) como variáveis repetidas. A variável que não se repete é \(\Delta p\).

### Passo 5 — Formar o grupo \(\pi\)

Escreve-se:

\[
\pi_1=\Delta p\,u^a\rho^bL^c
\]

### Passo 6 — Determinar os expoentes e verificar a adimensionalidade

Substituindo as dimensões:

\[
1=(ML^{-1}T^{-2})(LT^{-1})^a(ML^{-3})^b(L)^c
\]

Igualando os expoentes das dimensões fundamentais:

\[
M:\quad 0=1+b \quad\Rightarrow\quad b=-1
\]

\[
T:\quad 0=-2-a \quad\Rightarrow\quad a=-2
\]

\[
L:\quad 0=-1+a-3b+c
\]

Substituindo \(a=-2\) e \(b=-1\):

\[
0=-1-2+3+c \quad\Rightarrow\quad c=0
\]

Logo:

\[
\pi_1=\Delta p\,u^{-2}\rho^{-1}
\]

ou

\[
\boxed{\pi_1=\frac{\Delta p}{\rho u^2}}
\]

Esse grupo corresponde ao número de Euler apresentado na apostila:

\[
\boxed{Eu=\frac{\Delta p}{\rho u^2}}
\]

**Verificação:** as dimensões se cancelam, portanto o grupo é adimensional.

---

## Auditoria de cobertura

- Homogeneidade dimensional, adimensionalização e normalização.
- Dimensões fundamentais \(M\), \(L\) e \(T\).
- Força de inércia e normalização das forças.
- Números de Euler, Reynolds, Froude e Weber.
- Lei da viscosidade de Newton.
- Finalidades da análise dimensional.
- Teorema π de Buckingham e suas seis etapas.
- Similaridade geométrica, cinemática e dinâmica.
- Dilema da similaridade em modelos de navios.
- Exemplo de Buckingham–\(\Pi\) aplicado ao número de Euler.

**Limite da fonte:** o gabarito usa apenas as definições, relações, exemplos e conclusões registrados no PDF fornecido; não acrescenta justificativas externas para substituir as explicações da apostila.
