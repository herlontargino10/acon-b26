# Auditoria de Cruzamento — Capítulo 4

## 1. Fontes utilizadas
- **PDF-alvo:** 018-022_Mecanica_dos_Fluidos_Capitulo_4.pdf
- **Markdown-alvo:** 018-022_Mecanica_dos_Fluidos_Capitulo_4.md
- **Transcrições relevantes:** HidVoz 260807_094506_original.txt e HidVoz 260814_073641_original.txt
- **Inventário:** INVENTARIO_GERAL_TRANSCRIÇÕES.md

## 2. Mapa das transcrições relevantes

- **Arquivo:** HidVoz 260807_094506_original.txt
  - **Temas encontrados:** Primeira Lei da Termodinâmica, densidade mássica de energia (energia interna vs cinética), trabalhos de fronteira e aplicação prática de conservação de energia/velocidade no "Efeito Squat".
  - **Páginas/seções do capítulo relacionadas:** A lei de conservação de energia e Hipóteses fundamentais.
  - **Nível de relevância:** ALTA. Cobre todo o embasamento de conservação de energia do Capítulo 4.

- **Arquivo:** HidVoz 260814_073641_original.txt
  - **Temas encontrados:** Hipóteses fluidodinâmicas (incompressibilidade, regime invíscido, fluido newtoniano x não-newtoniano), arrasto de pressão vs arrasto de cisalhamento (shear) e condição de não-deslizamento.
  - **Páginas/seções do capítulo relacionadas:** 8 Hipóteses fundamentais.
  - **Nível de relevância:** ALTA. Destrincha e exemplifica as hipóteses apresentadas secamente no PDF.

## 3. Conteúdo já contemplado
*(PDF + transcrição + capítulo estão coerentes)*

- **Balanço básico da Primeira Lei da Termodinâmica:** A relação entre variação de energia, calor e trabalho ($E = Q - W$).
- **Componentes da Energia Específica ($e$):** A divisão em energia interna, cinética e potencial ($e = \hat{u} + \frac{1}{2}V^2 + gz$).
- **Hipótese do Calor ($\dot{Q}$):** A decisão de descartar o calor nas análises hidrodinâmicas do navio.
- **Divisão do Trabalho ($\dot{W}$):** Trabalho de máquina vs. Trabalho de pressão/cisalhamento.
- **Hipótese de Escoamento Totalmente Desenvolvido:** Ambos concordam que não existe variação espacial ao longo do fluxo e que não se aplica genericamente ao contorno externo de um navio.

## 4. Conteúdo presente, mas incompleto
- **Fluidos Newtonianos:** O conceito está no capítulo, mas a transcrição adiciona o importante contraste com **fluidos não-newtonianos** e sua aplicação prática naval.
- **Hipótese de Fluido Invíscido:** Está no capítulo, mas a explicação da aula aprofunda a sua relação com a dicotomia **Arrasto de Pressão (Drag Pressure) vs. Arrasto de Cisalhamento (Drag Shear)**.

## 5. Conteúdo explicado pelo professor e ausente do capítulo

- **Conceito:** Efeito Squat (afundamento hidrodinâmico).
  - **Trecho/ideia:** O professor usa a conservação de energia/Bernoulli para explicar por que navios reduzem a margem abaixo da quilha em canais restritos.
  - **Origem:** HidVoz 260807_094506_original.txt
  - **Relação com o PDF:** Ausente no PDF (o PDF apresenta apenas a formulação algébrica da energia).
  - **Possível localização:** Após a seção de energia ou nas hipóteses.

- **Conceito:** Componentes do Arrasto (Drag Pressure e Drag Shear) e Condição de Não-Deslizamento.
  - **Trecho/ideia:** Professor debate qual arrasto é maior e explica como a água "gruda" no casco gerando o arrasto de fricção (shear drag).
  - **Origem:** HidVoz 260814_073641_original.txt
  - **Relação com o PDF:** Ausente.
  - **Possível localização:** Na explicação da hipótese de fluido invíscido.

## 6. Conteúdo da aula ausente no PDF

- **Exemplos do Efeito Squat** e interação hidrodinâmica em canais restritos.
- **Fluidos não-newtonianos** (exemplificados com "lama" e "amido de milho").
- **Drag Pressure vs Drag Shear**.
- **Analogia do corpo humano** (comparado a um volume de controle térmico/hídrico para explicar a Primeira Lei).

## 7. Fórmulas cruzadas

- **Equação da Primeira Lei:**
  - PDF: $\frac{dE}{dt} = \frac{\delta Q}{dt} - \frac{\delta W}{dt}$
  - Aula: Professor fala $E = Q - W$.
  - Capítulo: Traz as duas notações e a explicação integral.
  - Situação: CONSISTENTE.
  
- **Densidade Mássica de Energia ($e$):**
  - PDF: $e = \hat{u} + \frac{1}{2}V^2 + gz$
  - Aula: Discutida verbalmente.
  - Capítulo: $e = \hat{u} + \frac{1}{2}V^2 + gz$
  - Situação: CONSISTENTE.

## 8. Divergências entre PDF × Transcrição × Capítulo

### Divergência 1
- **PDF:** "viscosidade do fluido é constante independente da tensão superficial aplicada..." (pág. 021)
- **Transcrição:** Os alunos leem o termo errado "tensão superficial" em voz alta [ERRO/TERMO APARENTEMENTE INCOMUM NA FALA], mas o professor continua a explicação sob o conceito real de "tensão de cisalhamento".
- **Capítulo:** O capítulo sinaliza magistralmente na seção "Pontos Confusos ou Incompletos: Inconsistência de Terminologia", denunciando o lapso do autor no PDF.
- **Tipo de divergência:** Erro conceitual claro no PDF original.
- **Observação:** O capítulo procedeu corretamente ao registrar o erro da fonte primária sem mascará-lo.

## 9. Explicações didáticas importantes do professor

### 9.1 Analogias
- **Corpo humano como Sistema Termodinâmico:** O professor usa a temperatura corporal, suor e ingestão de água para ilustrar fisicamente a conservação de energia e massa em um Volume de Controle (HidVoz 260807_094506).

### 9.2 Exemplos de vida real
- **Navegação em lodo/lama:** Usado para ilustrar o comportamento bizarro de fluidos não-newtonianos sob tensão de cisalhamento quando propulsores de rebocadores os atingem (HidVoz 260814_073641).
- **Barcos menores na margem do rio:** Usado para explicar a condição de aderência/não-deslizamento, onde a água é mais lenta nas bordas por fricção (HidVoz 260814_073641).

### 9.3 Intuições físicas
- **Diferença entre Drag Pressure e Drag Shear:** Intuição vital sobre por que cascos longos sofrem predominantemente com atrito, justificando quando se deve ou não adotar a hipótese "invíscida".

### 9.4 Alertas para prova
- O professor alerta que as deduções analíticas massivas de Navier-Stokes não serão cobradas de forma decorada, focando no entendimento dos termos (presente sutilmente na aula, ratificando a "Incerteza Pedagógica" já citada no capítulo).

### 9.5 Perguntas feitas em aula
- "Qual é a diferença, o que que é o fluido newtoniano, fluido não newtoniano, alguém sabe?"
- "E quem é maior? O drag pressure ou drag shear?"
- "O que que é o velho efeito squat, se vocês fossem falar agora?"

## 10. Conteúdo potencialmente útil para integração futura

- **Definição estendida de Fluidos Não-Newtonianos (Lama marinha):** AVALIAR
- **Efeito Squat como exemplo de Conservação de Energia:** INTEGRAR FUTURAMENTE
- **Arrasto de Pressão x Cisalhamento e Condição de Aderência:** INTEGRAR FUTURAMENTE
- **Analogia do Corpo Humano para balanço $E = Q - W$:** AVALIAR
- **Erro de Tensão Superficial (já pontuado):** JÁ INTEGRADO (Não alterar)

## 11. Pontos que exigem verificação
- As passagens transcritas onde o professor (ou o microfone) engole termos, gerando falas como "tensão superficial" ou "hotel da densidade" [DÚVIDA DE TRANSCRIÇÃO]. O capítulo atual lidou bem ignorando os ruídos.
- A "Ambiguidade Algébrica: $-(p - V.n)dA$" pontuada no Markdown não foi mencionada pelo professor nas aulas, o que sugere que foi um detalhe tipográfico do PDF que não foi escrito no quadro-negro. Não requer mudança.

## 12. Conclusão diagnóstica
- **Quantidade de conceitos cruzados:** 11
- **Quantidade já contemplada:** 5
- **Quantidade incompleta:** 2
- **Quantidade ausente:** 2
- **Quantidade de divergências:** 1 (Erro do PDF capturado pelo Capítulo)
- **Quantidade de pontos duvidosos:** 1 (Ambiguidade algébrica não citada na aula)
- **Quantidade de conteúdos didáticos potencialmente úteis:** 5

*Nenhuma alteração foi realizada nos arquivos nesta etapa.*
