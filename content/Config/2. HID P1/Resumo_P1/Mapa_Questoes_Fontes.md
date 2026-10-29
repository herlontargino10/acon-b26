# Auditoria e Mapa de Rastreabilidade de Questões e Fontes — Hidrodinâmica P1

> **Status da Auditoria Técnica:** Concluída e Auditada  
> **Escopo:** Verificação individual das 40 questões do `Questionário P1.pdf` contra as fontes originais locais (Apostilas U1 e U2, Transcrições de Aula, Exercícios e Simulados).

---

## 1. Inventário de Fontes Auditadas no Workspace

| Identificador | Nome do Arquivo | Tipo / Origem | Páginas / Seções Analisadas | Tópicos Principais Cobertos |
| :--- | :--- | :--- | :--- | :--- |
| **DOC-00** | `Questionário P1.pdf` | Roteiro Oficial do Professor | 6 páginas (40 Q&A) | 7 blocos estruturantes da avaliação teórica P1. |
| **DOC-01** | `1_Leis_de_conservação-001-006.pdf` | Apostila Teórica U1 | Páginas 1–6 | Conservação da massa, VC diferencial cúbico, continuidade 3D compressível e incompressível ($\nabla \cdot \mathbf{V} = 0$). |
| **DOC-02** | `1_Leis_de_conservação-007-011.pdf` | Apostila Teórica U1 | Páginas 7–11 | Momento linear, 2ª Lei, Lagrangeano vs. Euleriano, Derivada Material, aceleração local e convectiva, bocais. |
| **DOC-03** | `1_Leis_de_conservação-011-018.pdf` | Apostila Teórica U1 | Páginas 11–18 | Forças superficiais e de corpo, dedução de $-\partial p/\partial x$, tensões cisalhantes ($\tau = \mu \partial u/\partial y$) e analogia dos trens. |
| **DOC-04** | `1_Leis_de_conservação-018-022.pdf` | Apostila Teórica U1 | Páginas 18–22 | Navier–Stokes vetorial completa, 1ª Lei da Termodinâmica, calor e trabalho. |
| **DOC-05** | `1_Leis_de_conservação-022-024.pdf` | Apostila Teórica U1 | Páginas 22–24 | Metodologia dos 6 passos gerais para escoamentos analíticos laminares internos. |
| **DOC-06** | `1_Leis_de_conservação-024-027.pdf` | Apostila Teórica U1 | Páginas 24–27 | Escoamento plano de Poiseuille (placas fixas sob $\partial p/\partial x$), não-escorregamento e impenetrabilidade. |
| **DOC-07** | `1_Leis_de_conservação-027-031.pdf` | Apostila Teórica U1 | Páginas 27–31 | Escoamento em canal inclinado dominado pela gravidade (*gravity-driven film flow*). |
| **DOC-08** | `1_Leis_de_conservação-031-034.pdf` | Apostila Teórica U1 | Páginas 31–34 | Escoamento plano de Couette (placa móvel sob cisalhamento puro com $\partial p/\partial x = 0$), perfil linear. |
| **DOC-09** | `2_O_Princípio_da_Homogeneidade_e_Análise_Dimensional.pdf` | Apostila Teórica U2 (Prof. Edson Mesquita) | Páginas 1–17 | Sistemas $MLT/FLT$, homogeneidade dimensional, força de inércia, $Eu, Re, Fr, We$, Teorema de Buckingham, similaridades e dilema de escala. |
| **DOC-10** | `Resolução Q.5 - Passo 6.md` | Exercício Resolvido | Passo 6 (Buckingham) | Resolução de sistema de expoentes para determinação de $Re = \frac{\rho u D}{\mu}$ com variáveis repetidas $(\rho, \mu, u)$. |
| **DOC-11** | `U1\U1 Resumos\*.md` | Resumos Estruturados U1 | Capítulos 1 a 8 | Revisão conceitual detalhada, notas de lousa e ênfases de prova de U1. |
| **DOC-12** | `U2\U2 Resumos\Mecanica_dos_Fluidos_Capitulo_2.md` | Resumo Estruturado U2 | Seções 1 a 11 | Revisão conceitual e dedutiva completa de U2 com anotações de prova. |
| **DOC-13** | `44_QUESTÕES_P1_SEM_CÁLCULO.json` | Banco Conceitual | 44 questões de fixação | Armadilhas conceituais, testes de verdadeiro/falso e justificativas físicas. |
| **DOC-14** | `Arquivos\Transcrições\*.txt` | Gravações de Sala de Aula | Vários arquivos | Esclarecimentos orais do professor sobre critérios de correção, jargões e ênfases de prova. |

---

## 2. Matriz Completa de Rastreabilidade e Auditoria Individual (Q1 a Q40)

### Estrutura de Classificação da Auditoria:
- **Dimensão A — Classificação Principal Exclusiva (Partição 1-para-1, soma = 40):**
  - **`[SUPORTE DIRETO]`** (34 questões): Teoria, hipóteses, equações e gabarito confirmados diretamente nas apostilas e no questionário, sem divergência documental.
  - **`[DIVERGÊNCIA DOCUMENTAL]`** (2 questões): Fundamentação teórica existente nas apostilas, porém com discrepância notacional ou conceitual registrada entre a apostila e o questionário.
  - **`[DEDUÇÃO COMPLEMENTAR]`** (4 questões): Gabarito oficial e fórmulas presentes no `Questionário P1.pdf`, com dedução analítica formal em coordenadas cilíndricas complementada no resumo para suprir a lacuna da apostila de U1 (que deduziu apenas o caso de placas planas).
- **Dimensão B — Etiquetas Complementares de Auditoria (Metadados transversais não excludentes):**
  - `[DIV]`: Existência de divergência nas fontes.
  - `[COMP]`: Presença de dedução analítica complementar.
  - `[CONF]`: Necessidade de confirmação/alinhamento de critério com o professor.
  - `[LIM]`: Limitação de verificação documental no material local.

| Questão | Bloco | Tema Central | Seção no Resumo | Fontes Primárias Pertinentes | Classificação Principal (Exclusiva) | Etiquetas Complementares e Notas Documentais |
| :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| **Q1** | Bloco 1 | Caracterização formal do regime permanente | Seção 1.1 | DOC-00 (p. 1), DOC-02 (pp. 8-10), DOC-11 (Cap. 2) | **`[SUPORTE DIRETO]`** | Condição $\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$. Propriedades invariantes no ponto fixo. |
| **Q2** | Bloco 1 | Aceleração em bocal convergente com $\partial u/\partial t = 0$ | Seção 1.2 | DOC-00 (p. 1), DOC-02 (pp. 7-8), DOC-11 (Cap. 2) | **`[SUPORTE DIRETO]`** | Inércia convectiva $u \frac{\partial u}{\partial x} > 0$ devido à redução da área ($A_2 < A_1$). |
| **Q3** | Bloco 1 | Derivada material 1D e termo de inércia puramente espacial | Seção 1.3 | DOC-00 (p. 1), DOC-02 (pp. 8-10), DOC-11 (Cap. 2) | **`[SUPORTE DIRETO]`** | Expressão $\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x}$. Termo espacial: $u \frac{\partial u}{\partial x}$. |
| **Q4** | Bloco 1 | Aceleração convectiva em duto divergente permanente | Seção 1.4 | DOC-00 (p. 1), DOC-02 (pp. 7-9), DOC-11 (Cap. 2) | **`[SUPORTE DIRETO]`** | $u > 0$ e $\frac{\partial u}{\partial x} < 0 \implies u \frac{\partial u}{\partial x} < 0$ (desaceleração física). |
| **Q5** | Bloco 1 | Erro clássico: confundir aceleração local com material | Seção 1.5 | DOC-00 (p. 1), DOC-02 (pp. 8-10), DOC-13 (Q9) | **`[SUPORTE DIRETO]`** | Confundir $\frac{\partial \mathbf{V}}{\partial t} = \mathbf{0}$ na janela fixa com $\frac{D\mathbf{V}}{Dt} \neq \mathbf{0}$ na partícula móvel. |
| **Q6** | Bloco 2 | Equação da continuidade 3D compressível | Seção 2.1 | DOC-00 (p. 1), DOC-01 (pp. 4-6), DOC-11 (Cap. 1) | **`[SUPORTE DIRETO]`** | $\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$ deduzida no VC cúbico $\Delta x\Delta y\Delta z$. |
| **Q7** | Bloco 2 | Redução para escoamentos incompressíveis ($\nabla \cdot \mathbf{V} = 0$) | Seção 2.2 | DOC-00 (p. 2), DOC-01 (p. 6), DOC-13 (Q2, Q8) | **`[SUPORTE DIRETO]`** | Água: $\rho = \text{cte} \implies \frac{\partial \rho}{\partial t} = 0$, fatoração e cancelamento de $\rho$. |
| **Q8** | Bloco 2 | Significado físico de divergente nulo ($\nabla \cdot \mathbf{V} = 0$) | Seção 2.3 | DOC-00 (p. 2), DOC-01 (p. 6), DOC-13 (Q6) | **`[SUPORTE DIRETO]`** | Taxa de dilatação volumétrica nula ($\frac{1}{\delta V}\frac{D(\delta V)}{Dt} = 0$); volume rigorosamente constante. |
| **Q9** | Bloco 2 | Cálculo de $\partial v/\partial y$ em canal 2D ($u = C_1 + C_2 x$) | Seção 2.4 | DOC-00 (p. 2), DOC-01 (pp. 5-6), DOC-13 (Q7) | **`[SUPORTE DIRETO]`** | Continuidade 2D $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0 \implies C_2 + \frac{\partial v}{\partial y} = 0 \implies \frac{\partial v}{\partial y} = -C_2$. |
| **Q10** | Bloco 2 | Interpretação física de $\frac{\partial v}{\partial y} = -C_2 < 0$ | Seção 2.5 | DOC-00 (p. 2), DOC-01 (pp. 5-6), DOC-13 (Q7) | **`[SUPORTE DIRETO]`** | Convergência transversal das camadas para compensar o estiramento horizontal e manter o volume constante. |
| **Q11** | Bloco 3 | Força líquida de pressão em elemento diferencial $dx\,dy\,dz$ | Seção 3.1 | DOC-00 (p. 2), DOC-03 (pp. 12-14), DOC-11 (Cap. 3) | **`[SUPORTE DIRETO]`** | Força líquida: $-\frac{\partial p}{\partial x}dx\,dy\,dz$. Por unidade de volume: $-\frac{\partial p}{\partial x}$. |
| **Q12** | Bloco 3 | Justificativa do sinal de menos ($-\frac{\partial p}{\partial x}$) em Navier–Stokes | Seção 3.2 | DOC-00 (p. 2), DOC-03 (p. 13), DOC-13 (Q15) | **`[SUPORTE DIRETO]`** | Pressão é tensão normal compressiva (de fora para dentro). Aceleração $+x$ exige $p_1 > p_2 \implies \frac{\partial p}{\partial x} < 0$. |
| **Q13** | Bloco 3 | Consequência se a força de pressão fosse $+\frac{\partial p}{\partial x}$ | Seção 3.3 | DOC-00 (p. 2-3), DOC-03 (pp. 13-14), DOC-13 | **`[SUPORTE DIRETO]`** | Aceleração espontânea para zonas de maior pressão, violando o equilíbrio mecânico compressivo. |
| **Q14** | Bloco 3 | Duas grandes classes de forças em fluidos | Seção 3.4 | DOC-00 (p. 3), DOC-03 (pp. 11-12), DOC-11 (Cap. 3) | **`[SUPORTE DIRETO]`** | Forças de superfície (contato: pressão e atrito viscoso) e forças de corpo/campo (à distância: gravidade). |
| **Q15** | Bloco 4 | Condição de não-escorregamento (*no-slip*) no casco | Seção 4.1 | DOC-00 (p. 3), DOC-06 (p. 25), DOC-08 (p. 32) | **`[SUPORTE DIRETO]`** | Aderência molecular: fluido na parede sólida adquire a velocidade do sólido ($u_{\text{rel}} = 0$). |
| **Q16** | Bloco 4 | Condição de impenetrabilidade em fronteira impermeável | Seção 4.2 | DOC-00 (p. 3), DOC-06 (p. 25), DOC-08 (p. 32) | **`[SUPORTE DIRETO]`** | Impossibilidade de fluxo através da parede rígida: velocidade normal $v_n = \mathbf{V} \cdot \mathbf{n} = 0$. |
| **Q17** | Bloco 4 | Por que o fluxo no casco não é "totalmente desenvolvido" | Seção 4.3 | DOC-00 (p. 3), DOC-05 (p. 23), DOC-06 (p. 24) | **`[SUPORTE DIRETO]`** | Camada limite cresce da proa à popa, formas do casco variam geometricamente e $\frac{\partial u}{\partial x} \neq 0$. |
| **Q18** | Bloco 4 | Incapacidade do fluido invíscido de calcular atrito | Seção 4.4 | DOC-00 (p. 3), DOC-03 (pp. 15-16), DOC-06 (p. 25) | **`[SUPORTE DIRETO]`** | Fluido invíscido desliza na parede ($u_{\text{parede}} \neq 0$) e $\mu = 0 \implies \tau_w = \mu \frac{\partial u}{\partial y} = 0$. |
| **Q19** | Bloco 5 | Três princípios clássicos de conservação | Seção 5.1 | DOC-00 (p. 3), DOC-01 (p. 1), DOC-04 (pp. 18-20) | **`[SUPORTE DIRETO]`** | Conservação da massa, da quantidade de movimento (momento linear) e da energia. |
| **Q20** | Bloco 5 | Diferença direta: Lagrangeana vs. Euleriana | Seção 5.2 | DOC-00 (p. 4), DOC-02 (pp. 8-10), DOC-13 (Q10) | **`[SUPORTE DIRETO]`** | Lagrangeano persegue partículas individuais no tempo; Euleriano observa coordenadas fixas no espaço. |
| **Q21** | Bloco 5 | Duas parcelas da derivada material euleriana | Seção 5.3 | DOC-00 (p. 4), DOC-02 (pp. 8-10), DOC-11 (Cap. 2) | **`[SUPORTE DIRETO]`** | Parcela local ($\frac{\partial}{\partial t}$) e parcela convectiva ($(\mathbf{V} \cdot \nabla)$). |
| **Q22** | Bloco 5 | Classificação das forças quanto à interação mecânica | Seção 5.4 | DOC-00 (p. 4), DOC-03 (pp. 11-12), DOC-11 (Cap. 3) | **`[SUPORTE DIRETO]`** | Forças de superfície (contato através das fronteiras) e forças de corpo (ação à distância volumétrica). |
| **Q23** | Bloco 5 | Distinção entre aderência e impenetrabilidade | Seção 5.5 | DOC-00 (p. 4), DOC-06 (p. 25), DOC-08 (p. 32) | **`[SUPORTE DIRETO]`** | Não-escorregamento zera velocidade tangencial relativa; impenetrabilidade zera velocidade normal. |
| **Q24** | Bloco 5 | Escoamento plano de Poiseuille (placas fixas sob pressão) | Seção 5.6 | DOC-00 (p. 4), DOC-06 (pp. 24-27), DOC-11 (Cap. 6) | **`[SUPORTE DIRETO]`** | Perfil parabólico simétrico induzido puramente por desnível de pressão entre placas paralelas fixas. |
| **Q25** | Bloco 5 | Escoamento de Couette (placa móvel sob arraste) | Seção 5.7 | DOC-00 (p. 4), DOC-08 (pp. 31-34), DOC-11 (Cap. 8) | **`[SUPORTE DIRETO]`** | Perfil linear $u(y) = \frac{V_0}{a}y$ e tensão cisalhante constante $\tau = \mu \frac{V_0}{a}$ arrastado por placa móvel. |
| **Q26** | Bloco 5 | Número de Reynolds ($Re$): inércia vs. viscosidade | Seção 5.8 | DOC-00 (p. 4), DOC-09 (pp. 3-4), DOC-12 (Seção 5.2) | **`[SUPORTE DIRETO]`** | $Re = \frac{\rho U L}{\mu}$. Razão inércia/viscosidade, comanda a transição laminar-turbulenta. |
| **Q27** | Bloco 5 | Número de Froude ($Fr$): inércia vs. gravidade | Seção 5.9 | DOC-00 (p. 4), DOC-09 (pp. 4-5), DOC-12 (Seção 5.3) | **`[SUPORTE DIRETO]`** | $Fr = \frac{U}{\sqrt{gL}}$. Compara inércia à gravidade, governa o sistema de ondas de proa do navio. |
| **Q28** | Bloco 5 | Três similaridades físicas (tanque vs. navio) | Seção 5.10 | DOC-00 (p. 4), DOC-09 (pp. 13-17), DOC-12 (Seção 10) | **`[SUPORTE DIRETO]`** | Similaridade geométrica (proporções lineares $\alpha$), cinemática ($\mathbf{V}_m/\mathbf{V}_p$ cte) e dinâmica (forças homólogas ctes). |
| **Q29** | Bloco 6 | Regra da Homogeneidade Dimensional | Seção 6.1 | DOC-00 (p. 5), DOC-09 (p. 2), DOC-12 (Seção 3) | **`[SUPORTE DIRETO]`** | Todos os membros aditivos de uma equação física devem possuir rigorosamente a mesma dimensão primária ($M, L, T$). |
| **Q30** | Bloco 6 | Procedimento de adimensionalização | Seção 6.2 | DOC-00 (p. 5), DOC-09 (p. 2), DOC-12 (Seção 3) | **`[SUPORTE DIRETO]`** | Dividir cada termo aditivo por uma mesma combinação algébrica de variáveis que possua a mesma dimensão. |
| **Q31** | Bloco 6 | Teorema $\Pi$ de Buckingham: número de grupos ($k=n-m$) | Seção 6.3 | DOC-00 (p. 5), DOC-09 (pp. 6-7), DOC-12 (Seção 6) | **`[SUPORTE DIRETO]`** | Se há $n$ variáveis e $m$ dimensões básicas, obtêm-se exatamente $k = n - m$ monômios adimensionais. |
| **Q32** | Bloco 6 | Independência dimensional das variáveis repetidas | Seção 6.4 | DOC-00 (p. 5), DOC-09 (p. 7), DOC-12 (Seção 6) | **`[SUPORTE DIRETO]`** | Devem ser dimensionalmente independentes; proibido que qualquer combinação entre elas forme um adimensional isolado. |
| **Q33** | Bloco 6 | Quantidade e requisito cumulativo das variáveis repetidas | Seção 6.5 | DOC-00 (p. 5), DOC-09 (p. 7), DOC-12 (Seção 6) | **`[SUPORTE DIRETO]`** | Devem ser exatamente $m$ variáveis repetidas e devem, juntas, conter todas as dimensões básicas do problema. |
| **Q34** | Bloco 6 | Grupos na resistência do casco ($R, \rho, U, L, \mu, g, \sigma$) | Seção 6.6 | DOC-00 (p. 5), DOC-09 (pp. 9-12), DOC-12 | **`[DIVERGÊNCIA DOCUMENTAL]`** | `[DIV]`, `[CONF]`, `[LIM]`. $n=7, m=3 \implies k=4$: $C_T, Re, Fr, We$. Divergência: a apostila usa $Rn, Fn, Wn$ e $\Pi_1 = R_{\text{forma}} / (\rho L^2 U^2)$. Limitação: fórmula explícita de $C_T$ não consta em Q34. |
| **Q35** | Bloco 7 | Definição de $Re_D$ em duto e faixas críticas | Seção 7.1 | DOC-00 (p. 5-6), DOC-09 (p. 4), DOC-12 | **`[DIVERGÊNCIA DOCUMENTAL]`** | `[DIV]`, `[CONF]`. $Re_D = \frac{\rho U D}{\mu}$. Faixas: Laminar ($<2300$), Transição ($2300$ a $4000$), Turbulento ($>4000$). Divergência: apostila cita apenas $(Re_D)_{cr} \cong 2,3\times 10^3$. |
| **Q36** | Bloco 7 | Perfil radial parabólico $u(r) = u_{\max}[1-(r/R)^2]$ | Seção 7.2 | DOC-00 (p. 6), dedução analítica canônica cilíndrica | **`[DEDUÇÃO COMPLEMENTAR]`** | `[COMP]`, `[CONF]`, `[LIM]`. Equação e resposta confirmadas no Questionário. Dedução em casca coaxial cilíndrica complementada no resumo para suprir lacuna de U1. |
| **Q37** | Bloco 7 | Relação velocidade máxima e média ($u_{\max} = 2U$) | Seção 7.3 | DOC-00 (p. 6), integração radial de vazão | **`[DEDUÇÃO COMPLEMENTAR]`** | `[COMP]`. Resposta confirmada no Questionário. Dedução analítica por integração $dA = 2\pi r dr$ complementada no resumo. |
| **Q38** | Bloco 7 | Perfil linear da tensão cisalhante $\tau(r)$ no duto | Seção 7.4 | DOC-00 (p. 6), balanço diferencial de forças | **`[DEDUÇÃO COMPLEMENTAR]`** | `[COMP]`. $\tau(r) = \frac{r}{2}\frac{\Delta p}{L}$. Nula no centro ($r=0$) e máxima na parede ($r=R=D/2$). Confirmado no Questionário. |
| **Q39** | Bloco 7 | Equação de Hagen–Poiseuille ($\Delta p = \frac{128\mu LQ}{\pi D^4}$) | Seção 7.5 | DOC-00 (p. 6), dedução analítica clássica | **`[DEDUÇÃO COMPLEMENTAR]`** | `[COMP]`. Fórmula e proporcionalidades confirmadas no Questionário. Dedução por substituição de $u_{\max}$ e $Q$ complementada. |
| **Q40** | Bloco 7 | Sensibilidade de $\Delta p$ à redução do diâmetro pela metade | Seção 7.6 | DOC-00 (p. 6), DOC-13 | **`[SUPORTE DIRETO]`** | $\Delta p \propto D^{-4} \implies (1/2)^{-4} = 16$ vezes de aumento. Confirmado no Questionário e no banco conceitual. |

---

## 3. Síntese Quantitativa e Estrutura Lógica da Auditoria

### 3.1. Dimensão A: Classificação Principal Exclusiva por Questão (Total = 40)

Cada uma das 40 questões pertence a uma e apenas uma categoria principal, formando uma partição matemática rigorosa:

| Categoria Principal Exclusiva | Questões Abrangidas | Quantidade | Percentual |
| :--- | :--- | :---: | :---: |
| **1. Suporte Direto sem Divergência** | Q1 a Q33 e Q40 | **34** | 85,0% |
| **2. Divergência Documental Identificada** | Q34 e Q35 | **2** | 5,0% |
| **3. Gabarito no Questionário com Dedução Complementada** | Q36, Q37, Q38 e Q39 | **4** | 10,0% |
| **Total Geral da Partição** | **Q1 a Q40** | **40** | **100,0%** |

$$\text{Soma da Classificação Principal}: 34 + 2 + 4 = 40 \text{ questões (100\% do universo auditado)}$$

---

### 3.2. Dimensão B: Etiquetas Complementares de Auditoria (Metadados Transversais Não Excludentes)

Diferentemente da Classificação Principal (que é estritamente disjunta), as **Etiquetas Complementares** operam como atributos de auditoria independentes e não somatórios, podendo incidir isolada ou conjuntamente sobre qualquer questão sem comprometer a contagem de 40 questões:

1. **`[DIV]` — Existência de Divergência nas Fontes (2 questões: Q34, Q35):**  
   Identifica onde o texto da Apostila de U2 discrepa do gabarito oficial do `Questionário P1.pdf` (notação $Rn, Fn, Wn$ vs. $Re, Fr, We$ e faixas de transição de Reynolds).
2. **`[COMP]` — Presença de Dedução Analítica Complementar (4 questões: Q36 a Q39):**  
   Sinaliza questões cujas respostas e fórmulas constam no questionário, mas cuja dedução passo a passo em coordenadas radiais cilíndricas foi suprida pelo resumo de estudos.
3. **`[CONF]` — Necessidade de Confirmação com o Professor (7 questões: Q34, Q35, Q36–Q39 e premissa de $R_{\text{forma}}$):**  
   Mapeia tópicos em que se recomenda que o estudante consulte o docente quanto a critérios de correção e profundidade discursiva exigida na folha de avaliação.
4. **`[LIM]` — Limitações de Verificação Documental (5 questões: Q34, Q36–Q39):**  
   Registra pontos onde as fontes documentais locais do professor omitiram etapas dedutivas ou definições formais fechadas (ex.: ausência da fórmula explícita de normalização de $C_T$ em Q34 e ausência de dedução de tubos cilíndricos na Apostila de U1).

---

## 4. Mapeamento Final das 40 Questões para o Simulado P1 e Gabarito Comentado

| Questão | Bloco | Item no Simulado P1 (`SIMULADO_P1_HIDRODINAMICA.md`) | Localização no Gabarito Comentado | Tipo de Cobertura | Status |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **Q1** | Bloco 1 | 1ª Questão (Afirmativa I) e 2ª Questão (Lacuna 2) | Gabarito 1ª Q (I) e 2ª Q (2) | Direta e Suficiente | Aprovado |
| **Q2** | Bloco 1 | 1ª Questão (Afirmativa II) e 3ª Questão (Item 1) | Gabarito 1ª Q (II) e 3ª Q (1) | Direta e Suficiente | Aprovado |
| **Q3** | Bloco 1 | 1ª Questão (Afirmativa III) e 2ª Questão (Lacuna 1) | Gabarito 1ª Q (III) e 2ª Q (1) | Direta e Suficiente | Aprovado |
| **Q4** | Bloco 1 | 1ª Questão (Afirmativa IV) | Gabarito 1ª Q (IV) | Direta e Suficiente | Aprovado |
| **Q5** | Bloco 1 | 1ª Questão (Afirmativa V) e 3ª Questão (Item 2) | Gabarito 1ª Q (V) e 3ª Q (2) | Direta e Suficiente | Aprovado |
| **Q6** | Bloco 2 | 2ª Questão (Lacuna 3) e Questão 4.1 | Gabarito 2ª Q (3) e 4ª Q (4.1) | Direta e Suficiente | Aprovado |
| **Q7** | Bloco 2 | 2ª Questão (Lacuna 4) e 3ª Questão (Item 3) | Gabarito 2ª Q (4) e 3ª Q (3) | Direta e Suficiente | Aprovado |
| **Q8** | Bloco 2 | 3ª Questão (Item 4) e Questão 4.1 | Gabarito 3ª Q (4) e 4ª Q (4.1) | Direta e Suficiente | Aprovado |
| **Q9** | Bloco 2 | Questão 4.2 | Gabarito 4ª Q (4.2) | Direta e Suficiente | Aprovado |
| **Q10** | Bloco 2 | 3ª Questão (Item 5) e Questão 4.2 | Gabarito 3ª Q (5) e 4ª Q (4.2) | Direta e Suficiente | Aprovado |
| **Q11** | Bloco 3 | 2ª Questão (Lacuna 5) e Questão 4.3 | Gabarito 2ª Q (5) e 4ª Q (4.3) | Direta e Suficiente | Aprovado |
| **Q12** | Bloco 3 | 3ª Questão (Item 6) e Questão 4.3 | Gabarito 3ª Q (6) e 4ª Q (4.3) | Direta e Suficiente | Aprovado |
| **Q13** | Bloco 3 | 3ª Questão (Item 7) | Gabarito 3ª Q (7) | Direta e Suficiente | Aprovado |
| **Q14** | Bloco 3 | 2ª Questão (Lacuna 6) | Gabarito 2ª Q (6) | Direta e Suficiente | Aprovado |
| **Q15** | Bloco 4 | 2ª Questão (Lacuna 7) e 3ª Questão (Item 8) | Gabarito 2ª Q (7) e 3ª Q (8) | Direta e Suficiente | Aprovado |
| **Q16** | Bloco 4 | 2ª Questão (Lacuna 8) e 3ª Questão (Item 9) | Gabarito 2ª Q (8) e 3ª Q (9) | Direta e Suficiente | Aprovado |
| **Q17** | Bloco 4 | 3ª Questão (Item 10) e Questão 4.4 | Gabarito 3ª Q (10) e 4ª Q (4.4) | Direta e Suficiente | Aprovado |
| **Q18** | Bloco 4 | 3ª Questão (Item 11) | Gabarito 3ª Q (11) | Direta e Suficiente | Aprovado |
| **Q19** | Bloco 5 | 2ª Questão (Lacuna 9) | Gabarito 2ª Q (9) | Direta e Suficiente | Aprovado |
| **Q20** | Bloco 5 | 2ª Questão (Lacuna 10) e 3ª Questão (Item 12) | Gabarito 2ª Q (10) e 3ª Q (12) | Direta e Suficiente | Aprovado |
| **Q21** | Bloco 5 | 2ª Questão (Lacuna 11) | Gabarito 2ª Q (11) | Direta e Suficiente | Aprovado |
| **Q22** | Bloco 5 | 3ª Questão (Item 13) | Gabarito 3ª Q (13) | Direta e Suficiente | Aprovado |
| **Q23** | Bloco 5 | 3ª Questão (Item 14) e Questão 4.4 | Gabarito 3ª Q (14) e 4ª Q (4.4) | Direta e Suficiente | Aprovado |
| **Q24** | Bloco 5 | 2ª Questão (Lacuna 12) e Questão 4.5 | Gabarito 2ª Q (12) e 4ª Q (4.5) | Direta e Suficiente | Aprovado |
| **Q25** | Bloco 5 | 2ª Questão (Lacuna 13) e Questão 4.5 | Gabarito 2ª Q (13) e 4ª Q (4.5) | Direta e Suficiente | Aprovado |
| **Q26** | Bloco 5 | 2ª Questão (Lacuna 14) e Questão 4.6 | Gabarito 2ª Q (14) e 4ª Q (4.6) | Direta e Suficiente | Aprovado |
| **Q27** | Bloco 5 | 2ª Questão (Lacuna 15) e Questão 4.6 | Gabarito 2ª Q (15) e 4ª Q (4.6) | Direta e Suficiente | Aprovado |
| **Q28** | Bloco 5 | 2ª Questão (Lacuna 16) e 3ª Questão (Item 15) | Gabarito 2ª Q (16) e 3ª Q (15) | Direta e Suficiente | Aprovado |
| **Q29** | Bloco 6 | 2ª Questão (Lacuna 17) e 3ª Questão (Item 16) | Gabarito 2ª Q (17) e 3ª Q (16) | Direta e Suficiente | Aprovado |
| **Q30** | Bloco 6 | 3ª Questão (Item 17) | Gabarito 3ª Q (17) | Direta e Suficiente | Aprovado |
| **Q31** | Bloco 6 | 2ª Questão (Lacuna 18) e 5ª Questão (Passo 3) | Gabarito 2ª Q (18) e 5ª Q (Passo 3) | Direta e Suficiente | Aprovado |
| **Q32** | Bloco 6 | 3ª Questão (Item 18) | Gabarito 3ª Q (18) | Direta e Suficiente | Aprovado |
| **Q33** | Bloco 6 | 2ª Questão (Lacuna 19) e 5ª Questão (Passo 4) | Gabarito 2ª Q (19) e 5ª Q (Passo 4) | Direta e Suficiente | Aprovado |
| **Q34** | Bloco 6 | Questão 4.7 | Gabarito 4ª Q (4.7) | Direta e Suficiente | Aprovado |
| **Q35** | Bloco 7 | 2ª Questão (Lacuna 20) e Questão 4.8 | Gabarito 2ª Q (20) e 4ª Q (4.8) | Direta e Suficiente | Aprovado |
| **Q36** | Bloco 7 | 3ª Questão (Item 19) e 6ª Questão (Item b) | Gabarito 3ª Q (19) e 6ª Q (Item b) | Direta e Suficiente | Aprovado |
| **Q37** | Bloco 7 | 3ª Questão (Item 20) e 6ª Questão (Item c) | Gabarito 3ª Q (20) e 6ª Q (Item c) | Direta e Suficiente | Aprovado |
| **Q38** | Bloco 7 | Questão 4.9 e 6ª Questão (Item a) | Gabarito 4ª Q (4.9) e 6ª Q (Item a) | Direta e Suficiente | Aprovado |
| **Q39** | Bloco 7 | Questão 4.10 e 6ª Questão (Item d) | Gabarito 4ª Q (4.10) e 6ª Q (Item d) | Direta e Suficiente | Aprovado |
| **Q40** | Bloco 7 | Questão 4.10 e 6ª Questão (Item d) | Gabarito 4ª Q (4.10) e 6ª Q (Item d) | Direta e Suficiente | Aprovado |
