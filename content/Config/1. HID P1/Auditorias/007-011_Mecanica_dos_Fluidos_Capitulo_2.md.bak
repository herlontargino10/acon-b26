---
title: "Mecânica dos Fluidos — Capítulo 2"
subject: "Mecânica dos Fluidos"
source: "1_Leis_de_conservação-007-011.pdf"
pages: "007–011"
tags:
  - mecanica-dos-fluidos
  - hidrodinamica
  - estudo
---

# Capítulo 2 — A Lei de Conservação da Quantidade de Movimento

## 1. Conservação da Quantidade de Movimento e Segunda Lei de Newton

### Definição
A lei da conservação da quantidade de movimento pode ser expressa na forma diferencial aplicando-se diretamente a Segunda Lei de Newton a um elemento de fluido infinitesimal.

### Explicação
Newton estabeleceu que qualquer variação de quantidade de movimento de um objeto é devido à ação de alguma força externa. Sem a ação de uma força externa, a quantidade de movimento se mantém constante.

Em mecânica dos fluidos, um elemento de massa, $dm$, pode não ser constante em um dado sistema. A equação fundamental na perspectiva lagrangeana é apresentada como:

$$
\frac{D(mV)}{Dt} = F
$$

- **$\frac{D(mV)}{Dt}$**: Variação da quantidade de movimento no tempo (massa $m$ multiplicada pela velocidade $V$).
- **$F$**: Força externa aplicada.

### Atenção / Pegadinha
> [!warning] Atenção
> A equação fundamental é bem conhecida por alunos do ensino fundamental e está estruturada sob a perspectiva **lagrangeana**. Sob a ótica euleriana, como a massa fluida pode não ser constante num dado sistema e a janela de observação está fixa, a derivada deve ser interpretada de modo abrangente.

## 2. A Derivada Material (Substantiva ou Total)

### Definição
Sob a perspectiva euleriana, a derivada temporal simples é substituída pela **derivada material** (também referida como derivada substantiva ou derivada total). Ela é composta da tradicional variação da velocidade no tempo e de uma derivada convectiva.

### Explicação
Como nossa janela de observação está fixa no espaço (abordagem euleriana), torna-se necessária a inclusão da derivada convectiva. O termo principal introduzido pela fonte é:

$$
\rho \frac{Du}{Dt}
$$

- **$\rho$**: Densidade do fluido.
- **$\frac{Du}{Dt}$**: A derivada material da velocidade.
- **Aceleração local**: Representa a variação direta da velocidade com o tempo na posição fixa.
- **Derivada convectiva**: Indica que existe um gradiente espacial, ou seja, o fluido altera a sua velocidade em função da sua mudança de posição ao longo do escoamento.

## 3. Exemplo de Concepções: O Tubo Convergente

### Exemplo
Considere um tubo convergente por onde passa um escoamento de um fluido. O escoamento entra por uma abertura de maior dimensão do que na saída.

- **Parâmetros conhecidos**: Velocidades ($u_1$ e $u_2$), densidades ($\rho_1$ e $\rho_2$) e áreas da seção transversal ($A_1$ e $A_2$).
- **Condição do fluido**: Incompressível (logo, $\rho_1 = \rho_2$).

Aplicando-se a Lei da Conservação da Massa a este tubo, tem-se a relação:

$$
\rho_2 u_2 A_2 - \rho_1 u_1 A_1 = 0
$$

Simplificando (cancelando as densidades, já que $\rho_1 = \rho_2$):

$$
u_2 A_2 = u_1 A_1
$$

### Interpretação Física
A equação demonstra que, como a área da entrada é maior que a da saída ($A_1 > A_2$), a velocidade na saída tem de ser, obrigatoriamente, maior do que a velocidade na entrada ($u_2 > u_1$). Essa variação de velocidade ao longo do espaço físico representa aceleração do escoamento, e **aceleração indica o aparecimento de uma força**.

## 4. Perspectiva Lagrangeana vs. Euleriana: A Bola na Rampa

Para evidenciar o porquê de ambas as concepções exigirem compreensões matemáticas distintas, a fonte propõe a analogia de um sólido: uma bola descendo uma rampa, desprezando o atrito, e acelerando sob ação da força da gravidade.

### Abordagem Lagrangeana
Nesta concepção, acompanhamos o objeto (a bola ou a partícula fluida). Medindo as velocidades em três instantes distintos da descida, registra-se $u_1 < u_2 < u_3$, tratando-se de um MUV (movimento uniformemente variado).

Neste referencial móvel, a derivada temporal é não-nula:
$$
\frac{\partial u}{\partial t} \neq 0
$$

A inclinação do gráfico da velocidade em função do tempo é a aceleração:
$$
a = \frac{\Delta u}{\Delta t}
$$
Verifica-se, de forma direta e visual, que existe uma força atuando na partícula (gravidade).

### Abordagem Euleriana
Aqui, observa-se o escoamento a partir de uma **janela fixa no espaço** (um ponto estacionário ao longo da rampa). Em cada janela de observação, conforme o tempo transcorre, a velocidade de cada partícula sucessiva que ali passa não varia; ou seja, o escoamento é **permanente**:

$$
\frac{\partial u}{\partial t} = 0
$$

### Interpretação Simples
> [!tip] Interpretação
> Se dermos um zoom microscópico nesta "janela", veremos que a bola, instantes antes de passar, tem velocidade um pouco menor; instantes após passar, tem velocidade um pouco maior. Porém, exatamente *quando atravessa a janela fixa*, a leitura naquele ponto será sempre idêntica (constante) a cada unidade de tempo para as sucessivas partículas.

### Atenção / Pegadinha
> [!warning] Atenção
> Como a derivada temporal dá zero na janela ($\frac{\partial u}{\partial t} = 0$), alguém menos atento poderia concluir precipitadamente que **não existe força atuando**. Esse pensamento é fundamentalmente **errado**.

Na abordagem euleriana, a derivada temporal precisa ser ajustada para incluir o termo espacial (convectivo). 

> [!important] Importante
> O texto frisa que, embora a abordagem euleriana traga muitos benefícios em fluidos complexos, "a facilidade matemática não está entre esses benefícios".

## 5. Aceleração Convectiva e Equações Totais

### Explicação
A força sobre a rampa ou num escoamento existe, ela apenas "não estava aparecendo porque estava faltando os termos de aceleração convectiva". Quando se plota a velocidade em função das posições no espaço ($x$ e $y$), a variação se torna matematicamente tangível pela inclinação das curvas.

> [!important] Observação
> No caso ilustrado pelos gráficos da fonte, a aceleração é constante, ou seja, o ângulo de inclinação da função que define a variação das velocidades em $x$ e $y$ é constante. Contudo, a fonte adverte expressamente que a inclinação **poderia não ser constante** em outras situações (a variação espacial da velocidade não precisa obrigatoriamente ser linear em todos os casos).

### Demonstração Didática (Origem dos Termos)
A forma como se introduz a aceleração convectiva no modelo euleriano pode ser analisada por unidades de medida. Estas variações traduzem as diferenças de velocidade antes de entrar na janela e logo após sair.

**Na direção $x$**:
$$
\frac{\Delta u}{\Delta t} = \frac{\Delta u \Delta x}{\Delta t \Delta x} = \frac{\Delta x \Delta u}{\Delta t \Delta x} = u \frac{\Delta u}{\Delta x}
$$

**Na direção $y$**:
$$
\frac{\Delta u}{\Delta t} = \frac{\Delta u \Delta y}{\Delta t \Delta y} = \frac{\Delta y \Delta u}{\Delta t \Delta y} = v \frac{\Delta u}{\Delta y}
$$

> **Observação:** As transformações demonstrativas baseadas na manipulação de frações infinitesimais ilustram o conceito de forma puramente funcional para que o aluno visualize de onde surge a conversão entre o diferencial temporal ($\Delta t$) para os diferenciais espaciais de posição ($\Delta x$, $\Delta y$) multiplicados pela velocidade local correspondente ($u$, $v$).

### Equações de Aceleração Total 
Ao fixar o observador no espaço $(x, y, z)$ — abordagem euleriana — e fazendo o limite do intervalo de tempo tender a zero ($\Delta \rightarrow 0$), constrói-se a aceleração total para cada eixo de translação.

**No eixo $x$:**
$$
a_x = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z}
$$

**No eixo $y$:**
### Forma apresentada na fonte
$$
a_y = \frac{\partial y}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z}
$$
### Observação
O primeiro termo temporal à direita da igualdade encontra-se digitado explicitamente como $\frac{\partial y}{\partial t}$ no material original.
### Interpretação possível
Trata-se muito provavelmente de um erro de formatação/tipografia na própria fonte. O termo fisicamente correto da aceleração local deveria referir-se à componente $v$ da velocidade ($\frac{\partial v}{\partial t}$), análogo ao $\frac{\partial u}{\partial t}$ no eixo $x$. A escrita da fonte foi fielmente reportada.

**No eixo $z$:**
$$
a_z = \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z}
$$

### Escoamento Permanente
Caso o escoamento seja classificado como "permanente", as variações parciais exclusivas de tempo na janela de observação assumem valor igual a zero:
$$
\frac{\partial u}{\partial t} = 0, \quad \frac{\partial v}{\partial t} = 0 \quad \text{e} \quad \frac{\partial w}{\partial t} = 0
$$
*(Nota: as parcelas convectivas permanecerão intactas).*

---

## 6. Observação Restrita — Trecho Removido pelo Autor

### Forma apresentada na fonte
$$
\frac{D(\frac{m}{Vol}V)}{Dt} = \frac{F}{Vol}
$$
$$
\frac{D(\rho V)}{Dt} = \frac{F}{Vol}
$$
$$
\rho \frac{D(V)}{Dt} = \frac{F}{Vol}
$$

Apesar desta equação ser aparentemente simples, existe uma série de complexidades do lado direito. De onde as forças externas podem vir? Considerando um objeto sólido, por exemplo, um cubo, como é possível fazer este cubo se mover?

### Observação
Todo o texto discursivo listado acima e as respectivas fórmulas, contidos na subseção "Forças atuantes em um elemento fluido" da página 11, constam **completamente riscados em vermelho** no PDF original. 

### Interpretação possível
A formatação (risco sobreposto contínuo) denota descarte, cancelamento formal ou revisão metodológica realizada pelo próprio professor. As equações e o texto complementar demonstravam uma passagem didática convertendo a lei de Newton pela unidade de volume usando a densidade e questionando a origem das forças externas (usando o exemplo de um cubo sólido).

---

## Resumo Ultra-Rápido
- **2ª Lei (Fluidos):** Variação de quantidade de movimento é força externa. A massa no sistema varia. 
- **Concepção Lagrangeana:** O referencial move-se acompanhando o fluido (é fácil e intuitivo enxergar variação e força, mas inviável de se modelar massas fluidas complexas).
- **Concepção Euleriana:** O referencial é uma "janela" cravada fixa no espaço.
- **Derivada Material / Total:** Ferramenta euleriana para registrar forças corretamente. É constituída da aceleração **local** (mudança temporal num ponto) mais a aceleração **convectiva** (efeito dos gradientes espaciais). 
- **Escoamento Permanente:** Somente os termos da aceleração temporal ($\partial / \partial t$) serão igualados a zero; as parcelas convectivas ($u\frac{\partial}{\partial x}$, etc.) respondem pela aceleração espacial (ex: funil e convergentes).

## Prováveis Assuntos de Prova
1. Explicação teórica ou qualitativa diferenciando a abordagem lagrangeana (acompanhando partícula fluida) da euleriana (janela fixa).
2. Compreensão da perigosa pegadinha na abordagem euleriana, justificando por que a ausência de aceleração local ($\frac{\partial u}{\partial t} = 0$) **não implica** em inexistência de força atuante no objeto (comprovar pelos gradientes espaciais/convectivos do tubo convergente).
3. Interpretação física e expansão dos termos tridimensionais das equações da aceleração total ($a_x, a_y, a_z$).

## Pontos Confusos ou Incompletos
- Na conversão da aceleração convectiva ($\frac{\Delta u}{\Delta t} = \dots = u \frac{\Delta u}{\Delta x}$), a simplificação dos termos das frações não respeita a formalidade pura do Cálculo Diferencial, servindo apenas de manobra didática visual.
- A presença confirmada do erro tipográfico no termo $a_y$ (substituindo a velocidade parcial $\partial v$ pela variável de posição $\partial y$).
- Seção cortada ("Forças atuantes...") sobre a divisão da força pelo volume e a indagação do cubo sólido.

## Perguntas para Verificar a Compreensão
1. Por que, ao aplicar a Segunda Lei de Newton aos fluidos, há um desprendimento do formato clássico escolar?
2. Em escoamento permanente sob a janela euleriana, a velocidade de cada gota pode ser variável no espaço, mas constante para aquela coordenada $x, y, z$ ao longo dos segundos. Verdadeiro ou Falso? Justifique.
3. Se houvesse uma passagem do fluido de forma constante num diâmetro também constante, haveria aceleração convectiva?
4. A adoção da concepção Euleriana simplifica o desenvolvimento matemático? 

## Respostas Esperadas
1. Porque, diferentemente de blocos sólidos fechados, um elemento de escoamento fluido varia sua massa agregada, e a janela fixa no espaço exige compensar as porções que entram e saem de cena usando termos diferenciais convectivos em adição aos temporais puros.
2. Verdadeiro. Em qualquer segundo escolhido, a partícula que cruzar o ponto (2,2) terá, por exemplo, 10 m/s. No ponto adiante (3,3) terá sempre 12 m/s. A velocidade ali não muda ao longo do relógio (escoamento permanente).
3. Não. Havendo diâmetro constante (sem variação de área) e escoamento permanente, não haveria incremento das velocidades espaciais para conservar a massa, anulando as parcelas do gradiente convectivo (não há força externa induzindo acelerações espaciais).
4. Falso. Como dito formalmente, a visão euleriana não traz facilidade ou simplificação matemática — na verdade, expande a simples derivada numa série de parcelas complexas envolvendo derivadas parciais espaciais combinadas.

# Flashcards para Anki

## Essenciais
Q: O que compõe a expressão da **Derivada Material** na perspectiva euleriana?
A: A aceleração local (variação tradicional da velocidade no tempo num dado ponto) somada à derivada convectiva (gradiente do fluxo através das variáveis espaciais).

Q: Se a aceleração local $\left(\frac{\partial u}{\partial t}\right)$ num ponto for nula, isso prova que a força que rege o escoamento ali é zero?
A: Errado. O zero na local prova apenas que o escoamento é **permanente**. A aceleração (e as forças) continuam sendo validadas pela parcela de **aceleração convectiva**.

Q: Qual premissa rege as áreas e velocidades num tubo que afunila contendo um fluido incompressível?
A: Como $A_1 > A_2$ (a área diminui), a velocidade de saída deverá ser maior ($u_2 > u_1$) para preservar a massa (vazão), gerando uma aceleração convectiva detectável pela janela euleriana.

## Importantes
Q: Como é possível traduzir a condição de escoamento **permanente** no cálculo numérico da referida abordagem euleriana?
A: As derivadas que respondem apenas à ação contínua do tempo zeram. Portanto: $\frac{\partial u}{\partial t} = 0$, $\frac{\partial v}{\partial t} = 0$ e $\frac{\partial w}{\partial t} = 0$.

Q: A abordagem euleriana foca na facilidade e simplificação das matemáticas?
A: Não. Pelo contrário, as equações se desdobram em derivadas parciais complexas. O ganho da Euleriana repousa na organização prática da leitura e controles através de referências espaciais físicas fixas.

## Práticos
Q: Transcreva a equação formal para a aceleração total de fluidos em relação ao eixo de abscissas ($x$).
A: $a_x = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z}$

Q: Na dedução algébrica exposta na fonte para a aceleração espacial no eixo $y$, como se isola a componente "$v$"?
A: A substituição demonstra que $\frac{\Delta y}{\Delta t}$ perfaz o desdobramento da unidade de velocidade de modo a associá-lo, resultando em: $v \frac{\Delta u}{\Delta y}$.

## CSV para Anki
```csv
O que compõe a expressão da **Derivada Material** na perspectiva euleriana?;"A aceleração local (variação tradicional da velocidade no tempo num dado ponto) somada à derivada convectiva (gradiente do fluxo através das variáveis espaciais)."
Se a aceleração local $\left(\frac{\partial u}{\partial t}\right)$ num ponto for nula, isso prova que a força que rege o escoamento ali é zero?;"Errado. O zero na local prova apenas que o escoamento é **permanente**. A aceleração (e as forças) continuam sendo validadas pela parcela de **aceleração convectiva**."
Qual premissa rege as áreas e velocidades num tubo que afunila contendo um fluido incompressível?;"Como $A_1 > A_2$ (a área diminui), a velocidade de saída deverá ser maior ($u_2 > u_1$) para preservar a massa (vazão), gerando uma aceleração convectiva detectável pela janela euleriana."
Como é possível traduzir a condição de escoamento **permanente** no cálculo numérico da referida abordagem euleriana?;"As derivadas que respondem apenas à ação contínua do tempo zeram. Portanto: $\frac{\partial u}{\partial t} = 0$, $\frac{\partial v}{\partial t} = 0$ e $\frac{\partial w}{\partial t} = 0$."
A abordagem euleriana foca na facilidade e simplificação das matemáticas?;"Não. Pelo contrário, as equações se desdobram em derivadas parciais complexas. O ganho da Euleriana repousa na organização prática da leitura e controles através de referências espaciais físicas fixas."
Transcreva a equação formal para a aceleração total de fluidos em relação ao eixo de abscissas ($x$).;"$a_x = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z}$"
Na dedução algébrica exposta na fonte para a aceleração espacial no eixo $y$, como se isola a componente "$v$"?;"A substituição demonstra que $\frac{\Delta y}{\Delta t}$ perfaz o desdobramento da unidade de velocidade de modo a associá-lo, resultando em: $v \frac{\Delta u}{\Delta y}$."
```
