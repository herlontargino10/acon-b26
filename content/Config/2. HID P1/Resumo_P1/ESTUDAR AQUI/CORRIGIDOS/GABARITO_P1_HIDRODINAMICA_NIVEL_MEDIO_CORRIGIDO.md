# Gabarito comentado — P1 de Hidrodinâmica I

**Nível médio**  
Respostas e fundamentações objetivas.

---

## 1. Múltipla escolha

| Questão | Resposta |
|:---:|:---:|
| 1 | **B** |
| 2 | **C** |
| 3 | **Excluída** |
| 4 | **B** |
| 5 | **C** |

### Questão 1 — B

Em um duto divergente, a área aumenta. Como o escoamento é incompressível e permanente, a vazão se conserva. Assim, a velocidade diminui.

A aceleração local é nula em regime permanente:

$$
\frac{\partial u}{\partial t} = 0
$$

Entretanto, a aceleração convectiva pode ser diferente de zero:

$$
a_{\mathrm{conv}} = u \frac{\partial u}{\partial x}
$$

Como a velocidade diminui no sentido positivo do escoamento, $\frac{\partial u}{\partial x} < 0$, resultando em aceleração convectiva negativa.

### Questão 2 — C

Para um fluido incompressível, a massa específica $\rho$ é constante. Ela pode ser colocada em evidência na equação da continuidade e cancelada, pois $\rho \neq 0$.

A forma tridimensional resultante é:

$$
\nabla \cdot \mathbf{V} = 0
$$

Em coordenadas cartesianas:

$$
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0
$$

### Questão 3 — Excluída

O professor informou que não apresentaria o conteúdo dessa posição. Nenhuma questão substituta foi criada.

### Questão 4 — B

A força de pressão por unidade de volume na direção $x$ é:

$$
f_{p,x} = -\frac{\partial p}{\partial x}
$$

O sinal negativo decorre do balanço das forças compressivas de pressão nas faces opostas do elemento diferencial.

Para o volume diferencial $dV = dx\,dy\,dz$, a força resultante na direção $x$ é:

$$
dF_{p,x} = -\frac{\partial p}{\partial x}\,dV
$$

### Questão 5 — C

A condição de impenetrabilidade impede que o fluido atravesse a parede. Portanto, a componente normal da velocidade relativa é nula:

$$
\mathbf{V}_{\mathrm{rel}} \cdot \mathbf{n} = 0
$$

A condição de aderência (não escorregamento), para fluido viscoso, determina que a componente tangencial da velocidade relativa também seja nula:

$$
\mathbf{V}_{\mathrm{rel}} \times \mathbf{n} = \mathbf{0}
$$

---

## 2. Completar as lacunas

| Item | Resposta |
|:---:|---|
| 6.1 | **Tensão superficial** |
| 6.2 | **Continuidade** |
| 6.3 | **Euleriana** |
| 6.4 | **Lagrangeana** |
| 6.5 | **Local; convectiva** |
| 6.6 | **Superfície; corpo** |
| 6.7 | **Poiseuille** |
| 6.8 | **Reynolds; viscosas** |
| 6.9 | **Protótipo** |
| 6.10 | **Constante; homólogos** |

### Fundamentação breve

- **6.1 — Tensão superficial:** propriedade representada por $\sigma$.
- **6.2 — Continuidade:** a aplicação da conservação da massa conduz à equação da continuidade.
- **6.3 — Euleriana:** descrição do escoamento em posições fixas no espaço.
- **6.4 — Lagrangeana:** descrição que acompanha partículas fluidas.
- **6.5 — Local e convectiva:** são as duas parcelas da aceleração na descrição euleriana.
- **6.6 — Superfície e corpo:** classificação das forças que atuam sobre um elemento de fluido.
- **6.7 — Poiseuille:** nesta versão, o enunciado especifica placas fixas e escoamento conduzido por gradiente de pressão.
- **6.8 — Reynolds e viscosas:** nesta versão, o enunciado especifica a comparação entre forças de inércia e viscosas.
- **6.9 — Protótipo:** o modelo em escala reduzida representa o protótipo.
- **6.10 — Constante e homólogos:** na similaridade cinemática, a razão de velocidades em pontos homólogos permanece constante.

> **Atenção:** os itens 6.7 e 6.8 foram especificados para terem respostas únicas nesta versão de estudo. O áudio original não identifica de modo suficiente essas condições. Se o professor pretendia Couette (placa móvel) ou Froude (inércia em relação à gravidade), será necessário ajustar o enunciado e o gabarito.

---

## 3. Verdadeiro ou falso

| Item | Resposta |
|:---:|:---:|
| 7.1 | **V** |
| 7.2 | **V** |
| 7.3 | **F** |
| 7.4 | **V** |
| 7.5 | **V** |
| 7.6 | **F** |

**Sequência:** V – V – F – V – V – F.

### Fundamentação breve

**7.1 — Verdadeiro.** Em uma equação dimensionalmente homogênea, os termos somados devem apresentar as mesmas dimensões.

**7.2 — Verdadeiro.** O Teorema de Pi de Buckingham estabelece:

$$
k = n - m
$$

**7.3 — Falso.** A escolha das variáveis repetidas deve respeitar os requisitos do método e representar as dimensões fundamentais independentes do problema.

**7.4 — Verdadeiro.** O sistema $MLT$ utiliza massa, comprimento e tempo como dimensões fundamentais.

**7.5 — Verdadeiro.** Para que cada grupo $\Pi$ seja adimensional, os expoentes resultantes de $M$, $L$ e $T$ devem ser iguais a zero.

**7.6 — Falso.** A homogeneidade dimensional é necessária, mas não suficiente para garantir a validade física de uma equação.

---

## 4. Cálculo fixo — seis passos

Sem resolução nesta versão. O enunciado específico do exercício realizado em sala não foi fornecido junto aos materiais utilizados para elaborar este simulado.
