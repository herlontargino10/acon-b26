# REVISÃO DAS PROPOSTAS — ETAPA 4.1A

## 1. CARDS PROPOSTOS PARA REMOÇÃO

### Card 1
**Capítulo:** 1
**Card:** Vazão de saída
**Frente:** Como é expressa a vazão de saída?
**Verso:** $\dot m_{out}=\rho_2u_2A_2$.
**Motivo da remoção:** Card puramente mecânico fragmentando a definição-base de vazão mássica sem testar um conceito físico distinto.
**Existe outro card cobrindo o mesmo conceito?** Sim.
**Qual?** "Qual é a expressão da vazão mássica? ($\dot m=\rho uA$)."
**O conceito continua adequadamente coberto após a remoção?** Sim. O índice *out/in* é intuitivo.
**Fonte que sustenta a decisão:** PDF 1, onde a equação geral já cobre os subcasos.

### Card 2
**Capítulo:** 1
**Card:** Vazão de entrada
**Frente:** Como é expressa a vazão de entrada?
**Verso:** $\dot m_{in}=\rho_1u_1A_1$.
**Motivo da remoção:** Idêntico ao Card 1. Redundância artificial (fragmentação excessiva).
**Existe outro card cobrindo o mesmo conceito?** Sim.
**Qual?** O card mestre de vazão mássica.
**O conceito continua adequadamente coberto após a remoção?** Sim.
**Fonte que sustenta a decisão:** PDF 1.

### Card 3
**Capítulo:** 1
**Card:** Área da face
**Frente:** Qual é a área da face considerada?
**Verso:** $A=\Delta y\Delta z$.
**Motivo da remoção:** Foca na matemática trivial/geométrica isolada em vez da física do volume de controle.
**Existe outro card cobrindo o mesmo conceito?** Não no formato geométrico, mas a dimensionalidade (1D, 2D, 3D) é coberta.
**Qual?** N/A.
**O conceito continua adequadamente coberto após a remoção?** Sim, o conceito do cubo elementar é abordado pela malha computacional (CFD) e demais definições.
**Fonte que sustenta a decisão:** Markdown do Capítulo 1.

### Card 4
**Capítulo:** 1
**Card:** Entrada maior que saída
**Frente:** Se entra mais massa do que sai, o que acontece à massa interna?
**Verso:** A massa interna aumenta.
**Motivo da remoção:** O raciocínio é redundante com o card mestre do regime transiente, gerando cartões avulsos muito elementares que inflam o baralho (Anki) sem agregar valor de revisão.
**Existe outro card cobrindo o mesmo conceito?** Sim.
**Qual?** O novo card proposto sobre Regime Transiente (Caixa d'água).
**O conceito continua adequadamente coberto após a remoção?** Perfeitamente coberto e com ganho pedagógico.
**Fonte que sustenta a decisão:** Transcrições das aulas.

### Card 5
**Capítulo:** 1
**Card:** Saída maior que entrada
**Frente:** Se sai mais massa do que entra, o que acontece à massa interna?
**Verso:** A massa interna diminui.
**Motivo da remoção:** Mesmo motivo do Card 4.
**Existe outro card cobrindo o mesmo conceito?** Sim.
**Qual?** O novo card proposto sobre Regime Transiente.
**O conceito continua adequadamente coberto após a remoção?** Sim.
**Fonte que sustenta a decisão:** Transcrições das aulas.

### Card 6
**Capítulo:** 1
**Card:** Entrada igual à saída
**Frente:** Se entrada e saída são iguais, o que ocorre?
**Verso:** Não há acúmulo de massa.
**Motivo da remoção:** Fragmentação desnecessária do princípio básico de regime permanente.
**Existe outro card cobrindo o mesmo conceito?** Sim.
**Qual?** O novo card sobre Regime Permanente e Transiente.
**O conceito continua adequadamente coberto após a remoção?** Sim, de forma mais consolidada e física.
**Fonte que sustenta a decisão:** Transcrições das aulas.

---

## 2. CARD PROPOSTO PARA REFORMULAÇÃO

**Card atual**
**Frente:** O que significa $\partial u/\partial x>0$ segundo o material?
**Verso:** Existe massa saindo na direção x.

**Problema identificado:** Demasiadamente mecânico/matemático. A notação exata do sinal da derivada pode ser um falso foco, enquanto o aluno deveria memorizar o significado físico (gradiente gerando vazão).

**Card proposto**
**Frente:** O que significa fisicamente a desigualdade parcial positiva ($\partial u/\partial x > 0$) na continuidade 1D?
**Verso:** Significa que há mais massa saindo do que entrando na direção analisada.

**O que foi alterado e por quê:** Foi inserido o termo "continuidade 1D" para dar lastro teórico à pergunta e focado na palavra "fisicamente" para exigir a compreensão de acúmulo ao invés de mera memorização do sinal.
**Fonte:** Capítulo 1 Markdown enriquecido e PDF 1.

---

## 3. OS 8 NOVOS CARDS PROPOSTOS

### Novo Card 1
**Capítulo:** 1
**Conceito:** Regime Permanente vs Regime Transiente (Caixa d'água)
**Por que esse conceito merece um card:** Aglutina três cards mecânicos (removidos) numa explicação unificada que ilustra a taxa temporal da equação da massa.
**Frente proposta:** Qual a diferença conceitual e de acúmulo de massa entre Regime Permanente e Regime Transiente na visão do balanço?
**Verso proposto:** No Regime Permanente não há acúmulo (a massa que entra é igual à que sai). No Transiente, há variação da massa interna no tempo (como uma caixa d'água enchendo/esvaziando).
**Fonte no capítulo/PDF:** PDF 1 (Balanço Inicial).
**Fonte nas transcrições:** `HidVoz 260728_085323_original.txt`.
**Explicação do professor que justifica o card:** A didática da caixa d'água associada ao ladrão é o elemento cognitivo principal para o aluno discernir $\partial \rho / \partial t$.

### Novo Card 2
**Capítulo:** 2
**Conceito:** Visão Euleriana vs Lagrangeana
**Por que esse conceito merece um card:** Define o pilar de referencial da aceleração convectiva.
**Frente proposta:** Como se diferenciam a visão Euleriana e a visão Lagrangeana na hidrodinâmica?
**Verso proposto:** A Euleriana observa o fluxo passando por uma seção fixa (como alguém na margem do rio). A Lagrangeana acompanha a partícula ao longo do tempo (como descer o rio dentro de um barco).
**Fonte no capítulo/PDF:** PDF 2.
**Fonte nas transcrições:** `HidVoz 260728_102746_original.txt`.
**Explicação do professor que justifica o card:** O professor insistiu na diferenciação utilizando explicitamente exemplos práticos navais e automobilísticos, cobrindo o hiato abstrato do PDF.

### Novo Card 3
**Capítulo:** 3
**Conceito:** Analogia dos Trens e Atrito Viscoso
**Por que esse conceito merece um card:** Materializa o funcionamento da tensão de cisalhamento, um dos tópicos mais contraintuitivos da engenharia.
**Frente proposta:** Qual é a analogia usada pelo professor para descrever a geração de atrito viscoso tangencial entre camadas de fluido?
**Verso proposto:** A analogia do salto entre dois trens em velocidades diferentes: a massa precisa ser acelerada/freada ao trocar de camada, gerando o atrito viscoso.
**Fonte no capítulo/PDF:** Markdown Capítulo 3 (Adicionado na Etapa 3).
**Fonte nas transcrições:** `Hid260807_080417_original.txt`.
**Explicação do professor que justifica o card:** O professor conectou a aceleração das partículas no eixo y ao "choque/esforço" da mudança de trilhos.

### Novo Card 4
**Capítulo:** 4
**Conceito:** Efeito Squat
**Por que esse conceito merece um card:** Traduz as consequências extremas do termo cinético (velocidade $\times$ pressão) de Navier-Stokes/Bernoulli para navios reais, o ápice da disciplina.
**Frente proposta:** Qual efeito hidrodinâmico naval é causado pelo aumento da energia cinética (e queda de pressão) quando o navio passa por águas restritas?
**Verso proposto:** O Efeito Squat (afundamento dinâmico e sucção de borda).
**Fonte no capítulo/PDF:** Extracurricular à apostila, adicionado organicamente na aula (Markdown Cap 4).
**Fonte nas transcrições:** `HidroVoz 260724_131733_original.txt`.
**Explicação do professor que justifica o card:** O professor descarta a equação térmica (calor isolado) e mostra que o impacto da mecânica é o Efeito Squat na proa do navio.

### Novo Card 5
**Capítulo:** 5
**Conceito:** Força Motriz Gravitacional Projetada ($g \sin \theta$)
**Por que esse conceito merece um card:** O PDF apresenta o ângulo sem distinção da direção da gravidade, podendo causar erro em prova. O card isola o vetor correto.
**Frente proposta:** No escoamento inclinado (Gravity-driven), qual é a verdadeira força motriz e que tipo de perfil ela gera?
**Verso proposto:** A componente projetada da gravidade ($g \sin \theta$). Ela gera um perfil parabólico de velocidades.
**Fonte no capítulo/PDF:** PDF 5.
**Fonte nas transcrições:** `HidVoz 260814_091758_original.txt`.
**Explicação do professor que justifica o card:** Explicou repetidamente para desconsiderar a normal clássica e decompor a gravidade pelo seno impulsionando o líquido rampa abaixo.

### Novo Card 6
**Capítulo:** 6
**Conceito:** Equilíbrio estático / Cabo de Guerra
**Por que esse conceito merece um card:** Fixa a razão analítica da equação de Poiseuille: inércia nula (equilíbrio total entre a força motriz de pressão e o atrito).
**Frente proposta:** O que representa fisicamente o equilíbrio de um perfil de velocidades (Poiseuille) totalmente desenvolvido em tubo fechado?
**Verso proposto:** Um "cabo de guerra" entre a pressão que empurra o fluido e o cisalhamento (viscosidade) que o freia, com inércia nula ao longo do fluxo.
**Fonte no capítulo/PDF:** Markdown Cap 6.
**Fonte nas transcrições:** Diversas transcrições, incluindo o resumo pedagógico.
**Explicação do professor que justifica o card:** A analogia simplifica a densa integração de Navier-Stokes.

### Novo Card 7
**Capítulo:** 7
**Conceito:** Observação sobre Avaliação (Escoamento inclinado)
**Por que esse conceito merece um card:** Orienta o aluno no Anki a não gastar horas decorando passagens algébricas gigantes que foram explicitamente descartadas em sala.
**Frente proposta:** [DICA DE PROVA] O professor costuma cobrar a dedução analítica do escoamento inclinado (Gravity-driven)?
**Verso proposto:** Não. O professor declarou em sala que NÃO vai cobrar o desenvolvimento do modelo inclinado por gravidade (foco em Poiseuille e Couette).
**Fonte no capítulo/PDF:** Markdown Cap 7.
**Fonte nas transcrições:** `HidVoz 260814_091758_original.txt`.
**Explicação do professor que justifica o card:** "Isto aqui é algebricamente mais difícil, não colocarei em avaliação."

### Novo Card 8
**Capítulo:** 8
**Conceito:** Aplicação do Escoamento de Couette (Navios PSV)
**Por que esse conceito merece um card:** Dá vida útil ao modelo de "tampa superior móvel", aproximando-o da Engenharia Naval e Marítima.
**Frente proposta:** Qual é a aplicação prática naval do modelo analítico bidimensional de Couette ensinado em sala?
**Verso proposto:** Situações de confinamento fluido e perturbação viscosa em manobras reais (ex: navio PSV atracando rente a uma plataforma offshore).
**Fonte no capítulo/PDF:** Markdown Cap 8.
**Fonte nas transcrições:** `HidVoz 260814_081707_original.txt`.
**Explicação do professor que justifica o card:** O professor troca a lousa estéril (placa se movendo) pelo maquinário costeiro prático da área de óleo e gás, vital para fixação conceitual do Engenheiro.

---

## 4. TESTE DE NECESSIDADE DOS NOVOS CARDS

| Novo Card | No PDF? | No MD? | Na Aula? | Analogia/Aplicação? | Já coberto? | Classificação |
|---|---|---|---|---|---|---|
| 1 (Reg. Permanente / Caixa d'água) | Sim | Sim | Sim | Sim (Caixa D'água) | Indiretamente | **NECESSÁRIO** (substitui os 3 removidos com ganho superior). |
| 2 (Euleriana vs Lagrangeana) | Não claro | Sim | Sim | Sim (Rio/Barco) | Não | **NECESSÁRIO** |
| 3 (Analogia dos Trens) | Não | Sim | Sim | Sim (Trens) | Não | **ÚTIL, MAS OPCIONAL** (boa intuição, mas sem reflexo direto em fórmula). |
| 4 (Efeito Squat) | Não | Sim | Sim | Sim (Navio afundando) | Não | **NECESSÁRIO** |
| 5 (Força g sen theta) | Sim | Sim | Sim | Não | Não | **NECESSÁRIO** |
| 6 (Cabo de Guerra / Poiseuille) | Não | Sim | Sim | Sim (Cabo de Guerra) | Parcialmente | **ÚTIL, MAS OPCIONAL** (excelente viés físico sobre inércia nula). |
| 7 (Dica de Prova - Inclinado) | Não | Sim | Sim | Não | Não | **ÚTIL, MAS OPCIONAL** (otimização de estudo). |
| 8 (Couette PSV Offshore) | Não | Sim | Sim | Sim (PSV atracando) | Não | **NECESSÁRIO** |

---

## 5. PRINCIPAL VERIFICAÇÃO (CRITÉRIOS ESPECIAIS)

Os novos cards obedecem fielmente à orientação de ancorar a retenção técnica com a memória visual/contextual (Couette $\to$ Offshore PSV; Energia $\to$ Efeito Squat; Tensão $\to$ Salto entre trens). Essas analogias foram amplamente atestadas pelas transcrições auditadas nas Etapas 2 e 3 e foram transpostas como perguntas formais aqui de maneira responsável.
A dica de prova (Card 7) também está explicitamente marcada como `[DICA DE PROVA]` para não se confundir com lei da física, evitando o engessamento dogmático e mantendo o aluno ciente dos atalhos de aprovação declarados pelo docente.

---

## 6. RESULTADO FINAL

| Tipo | Quantidade | Observação |
|---|---:|---|
| Remoções propostas | 6 | Remoção por hiperfragmentação no Cap 1. |
| Reformulações propostas | 1 | Ajuste da parcial 1D no Cap 1 para exigir viés físico. |
| Novos cards | 8 | Resgate valioso da Etapa 3. |
| Novos realmente necessários | 5 | Efeito Squat, Eulerian/Lagrangian, Couette PSV, Caixa d'água, $g \sin \theta$. |
| Novos opcionais | 3 | Cabo de guerra, Trens em atrito, Dica de prova. |
| Novos redundantes | 0 | Nenhum dos propostos padece de redundância. |
| Novos não sustentados | 0 | Todos rastreados a uma fala precisa do professor. |

 *(Nenhuma alteração física efetuada. Fico no aguardo de sua avaliação.)*
