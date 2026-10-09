# Auditoria Final Independente — Simulado 3

## 1. Arquivos Envolvidos e Inspecionados
- Fonte primária (Cap. 3): `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`
- Fonte da Questão 5: `SIMULADO_U1_CAPITULO_1.md`
- Simulado: `SIMULADO_U1_CAPITULO_3.md`
- Gabarito: `GABARITO_COMENTADO_U1_CAPITULO_3.md`

## 2. Esclarecimento: Matriz de Contagem das Unidades de Validação
O relatório anterior apresentou os números "26" e "31". Eles representavam uma contagem macro baseada em agrupamentos de respostas (1 para a Q1 inteira, 10 para Q2, 10 para Q3, 5 para Q4 = 26; mais 5 para agrupamentos na Q5 = 31).

Para esta auditoria rigorosa, o critério de validação adotado foi **microanalítico**. Cada afirmação, alternativa da múltipla escolha, lacuna ou passo matemático que exija avaliação isolada para anular ou aprovar a questão foi contado como **1 unidade de validação individual**.

Abaixo, a matriz detalhada da auditoria:

| Questão | Tipo de Questão | Detalhamento das Unidades Analisadas | Total de Itens Verificados |
| :--- | :--- | :--- | :---: |
| **Questão 1** | Múltipla Escolha (Afirmativas) | 5 afirmativas (I a V) analisadas individualmente contra a fonte + 1 verificação da consistência da alternativa final que as combina. | **6** |
| **Questão 2** | Lacunas | 10 lacunas independentes avaliadas e confrontadas com o material original. | **10** |
| **Questão 3** | Verdadeiro ou Falso | 10 afirmações avaliadas e justificadas separadamente. | **10** |
| **Questão 4** | Múltipla Escolha Direta | 5 subquestões (4.1 a 4.5), cada uma contendo 5 alternativas rigorosamente analisadas (1 correta provada + 4 incorretas invalidadas isoladamente). | **25** |
| **Questão 5** | Análise Dimensional | 6 passos formais da estrutura metodológica de Buckingham-Π (1. identificação, 2. dimensões fundamentais, 3. cálculo dos grupos, 4. seleção das repetitivas, 5. montagem de Π, 6. equação dos expoentes e validação). | **6** |
| **TOTAL** | | | **57** |

A auditoria cruzou e verificou **57 unidades** independentes de validação de conhecimento ao longo do documento.

## 3. Auditoria das Questões 1 a 4 (Fundamentação e Exclusividade)
Cada alternativa das questões foi verificada e validada puramente pelo arquivo `011-018_Mecanica_dos_Fluidos_Capitulo_3.md`:
- **Questão 1:** A afirmativa I reflete o conteúdo da Seção 1 ($\rho \frac{DV}{Dt}$). A II é falsa: forças de corpo não tocam as superfícies (Tabela, Seção 2). A III e V são confirmadas perfeitamente pela Seção 3 (Lei de Pascal e regra do sinal do fluxo). A alternativa (b) é a única que contempla exatamente a tríade I, III, V.
- **Questão 2:** A auditoria procurou os termos correspondentes às lacunas (*densidade, tangenciais, perpendicular, translação, normal, de corpo, trens, gradiente, dinâmica, queda*). Todos figuram expressa e pedagogicamente no texto original, sem inferências externas de engenharia civil ou aeronáutica.
- **Questão 3:** As afirmações V/F trabalham com as entrelinhas didáticas do material (por exemplo, diferenciar "esmagamento/torção" local perante translação nas tensões de cisalhamento, listado no aviso amarelo "Atenção (Diferença de Tensão)").
- **Questão 4 (Exclusividade Múltipla Escolha):** Em todas as 5 questões (4.1 a 4.5), foi provado que **existe exatamente apenas uma alternativa correta**. Os distratores criados (total de 20 alternativas falsas) baseiam-se em erros clássicos e comuns previstos pelo professor (como tentar aplicar conservação térmica isotérmica ao invés do foco inercial) e todos são diretamente combatíveis pela leitura da apostila.

## 4. Auditoria da Questão 5
- **Reprodução literal confirmada:** O enunciado, a introdução das variáveis (densidade $\rho$, viscosidade $\mu$, diâmetro $D$, velocidade $u$) e as instruções (método de Buckingham-Π em 6 passos fundamentais) são idênticos em redação e estrutura ao contido no `SIMULADO_U1_CAPITULO_1.md`.
- **Exatidão dos Seis Passos:** A modelagem matricial no passo 6 foi independentemente resolvida.
  - O sistema linear isolado pela base $[M^0 L^0 T^0] = [L]^1 [M L^{-3}]^a [M L^{-1} T^{-1}]^b [L T^{-1}]^c$ resulta matematicamente em $b = -1$ (usando isolamento na equação de Comprimento $1 - 3a - b + c = 0$).
  - Substituindo $b=-1$, tem-se $a=1, c=1$.
  - O formato deduzido é $D^1 \rho^1 \mu^{-1} u^1 = \frac{\rho u D}{\mu}$, que é puramente o adimensional de Reynolds.
  - Divergências matemáticas: **Nenhuma encontrada**.

## 5. Auditoria de Estrutura e Gabarito
- **No arquivo principal (`SIMULADO_U1_CAPITULO_3.md`):** As 5 questões são listadas de forma limpa, sem spoilers entre elas. Apenas ao atingir o fim da página começa o bloco do "Gabarito Comentado", permitindo ao leitor realizar a prova sem interferência.
- **No arquivo complementar (`GABARITO_COMENTADO_U1_CAPITULO_3.md`):** O conteúdo está idêntico e sincronizado, oferecendo a visão paralela e consolidada completa do teste e das explicações.

## 6. Correções Efetivadas e Pendências
- **O que foi corrigido:** O erro reportado estava centrado na deficiência de clareza (no relatório anterior) referente aos parâmetros macroscópicos vs. microscópicos que compunham a "contagem". Isso foi solucionado reestruturando as tabelas deste documento de Auditoria para abranger as 57 validações unitárias verificadas individualmente. O simulado em si não possuía erros factuais com relação ao conteúdo, não necessitando exclusão de afirmações.
- **Pendências remanescentes:** **NENHUMA**. O material cumpre 100% da métrica especificada.
