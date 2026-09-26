```txt

Você receberá um ou mais materiais relacionados ao meu curso de **Oficiais da Marinha Mercante**, podendo ser:

- PDF
    
- Slides
    
- Resumo
    
- Transcrição de aula
    
- Prova antiga
    
- Áudio transcrito
    
- Anotações
    
- Material complementar fornecido pelo professor
    

Sua tarefa é transformar o conteúdo recebido em um **banco de questões pronto para importação na plataforma SIMULACORE**.

O objetivo é criar questões para **treino, revisão e simulação de prova**, priorizando recuperação ativa, interpretação e aplicação prática.

---

# 1. REGRA FUNDAMENTAL

**NÃO explique teoria.**

**NÃO faça resumo.**

**NÃO crie texto de aula.**

**NÃO acrescente conteúdo que não esteja sustentado pelos materiais fornecidos.**

Sua saída deve ser exclusivamente o banco de questões em JSON.

Quando houver informação insuficiente no material para elaborar uma questão com resposta inequívoca, **não crie a questão**.

Conhecimento externo somente poderá ser utilizado para interpretar uma informação do material quando isso não alterar, complementar ou contradizer o conteúdo fornecido.

Em caso de conflito entre fontes:

1. Prova antiga / questão oficial fornecida
    
2. Material oficial da disciplina
    
3. Slides ou material do professor
    
4. Resumo/anotações
    
5. Outras fontes fornecidas
    

Se houver conflito relevante entre materiais, **não invente uma solução**. Evite transformar o ponto conflitante em questão, salvo quando a própria divergência for explicitamente apresentada como objeto de estudo.

---

# 2. OBJETIVO DAS QUESTÕES

As questões devem simular o tipo de raciocínio exigido em provas de **Oficiais da Marinha Mercante**.

Priorize, quando presentes no material:

- conceitos técnicos;
    
- procedimentos;
    
- normas e regulamentos;
    
- responsabilidades;
    
- condições e exceções;
    
- sequência de procedimentos;
    
- interpretação;
    
- aplicação prática;
    
- cálculos;
    
- unidades e valores;
    
- tabelas;
    
- limites;
    
- classificações;
    
- equipamentos;
    
- situações operacionais;
    
- causas e consequências;
    
- diferenças entre conceitos semelhantes;
    
- situações em que uma pequena alteração muda a resposta.
    

A questão deve testar **conhecimento**, não apenas reconhecimento visual do texto.

---

# 3. QUANTIDADE

Determine automaticamente a quantidade com base no volume e na densidade do conteúdo.

### Material pequeno

Gerar no mínimo **20 questões**.

### Material médio

Gerar aproximadamente **30–60 questões**.

### Material grande

Gerar aproximadamente **50–150 questões**.

Não gerar questões artificiais apenas para atingir uma quantidade.

Se o conteúdo não sustentar uma determinada quantidade de questões de qualidade, gerar menos questões em vez de inventar conteúdo.

---

# 4. DISTRIBUIÇÃO DOS TIPOS

A distribuição obrigatória é:

- **45% MC — múltipla escolha**
    
- **25% TF — verdadeiro/falso**
    
- **15% GAP — completar lacuna**
    
- **10% ASSOC — associação**
    
- **5% DISC — discursiva**
    

Para pequenas quantidades, arredondar de maneira razoável mantendo a distribuição o mais próxima possível.

A prioridade é:

**qualidade e fidelidade ao material > precisão matemática da distribuição.**

---

# 5. DIFICULDADE

Gerar somente questões de nível:

- **60% média**
    
- **40% difícil**
    

Não criar questões classificadas como fáceis.

A dificuldade deve vir principalmente de:

- necessidade de discriminar conceitos semelhantes;
    
- interpretação;
    
- aplicação;
    
- exceções;
    
- detalhes importantes;
    
- combinação de informações;
    
- análise de situação;
    
- valores ou condições próximos;
    
- alternativas plausíveis;
    
- consequências de uma decisão;
    
- leitura cuidadosa do enunciado.
    

**Não aumentar a dificuldade inventando informações.**

---

# 6. PEGADINHAS

As pegadinhas são obrigatórias quando o conteúdo permitir.

Utilizar:

- inversão de conceitos;
    
- troca de causa e consequência;
    
- condições semelhantes;
    
- exceções;
    
- números próximos;
    
- unidades semelhantes;
    
- alternativas quase iguais;
    
- conceitos facilmente confundíveis;
    
- troca de sequência de procedimentos;
    
- alteração de uma condição operacional;
    
- palavras como **EXCETO**, **INCORRETO**, **NÃO**, **SOMENTE**, **SEMPRE** e **NUNCA**;
    
- interpretação de tabelas;
    
- interpretação de regras;
    
- casos práticos.
    

A pegadinha deve ser **tecnicamente defensável**.

Nunca criar uma alternativa enganosa apenas por diferença semântica irrelevante.

Nunca utilizar ambiguidade como forma de aumentar a dificuldade.

---

# 7. PRIORIZAÇÃO DO CONTEÚDO

Ao analisar os materiais, dê prioridade nesta ordem:

1. questões de provas antigas;
    
2. assuntos repetidos;
    
3. assuntos enfatizados pelo professor;
    
4. títulos e subtítulos;
    
5. conceitos destacados;
    
6. tabelas;
    
7. números, limites e unidades;
    
8. procedimentos;
    
9. exceções;
    
10. exemplos relevantes;
    
11. observações e alertas do professor;
    
12. detalhes com potencial de cobrança.
    

Ignore ou reduza:

- introduções genéricas;
    
- agradecimentos;
    
- apresentações pessoais;
    
- conteúdo administrativo irrelevante;
    
- exemplos claramente fora do objetivo da disciplina;
    
- repetições que não acrescentem informação.
    

---

# 8. PROVAS ANTIGAS

Se houver prova antiga, utilize-a como referência prioritária para identificar:

- estilo das perguntas;
    
- nível de dificuldade;
    
- assuntos cobrados;
    
- forma de elaboração das alternativas;
    
- conceitos recorrentes;
    
- tipo de raciocínio exigido;
    
- detalhes que costumam ser cobrados.
    

**Não copie simplesmente as questões antigas.**

Use-as para criar novas questões sobre o mesmo conhecimento.

Se uma questão antiga apresentar um conceito importante, explore-o por ângulos diferentes.

---

# 9. BIZUS DE PROVA

Se o professor indicar explicitamente que determinado assunto, conceito, número, regra ou tópico "vai cair", "é importante para a prova", "decorar", "atenção", "cai muito" ou equivalente:

Transforme o conteúdo relevante em:

- **1 questão discursiva**
    
- **2 questões objetivas**
    
- **1 questão com pegadinha**
    

Somente faça isso quando houver informação suficiente no material.

Não criar discursivas apenas para cumprir a regra se o conteúdo não permitir uma resposta objetiva.

---

# 10. TIPOS DE QUESTÃO

## MC — Múltipla escolha

Formato:

"type":"mc"

Regras:

- exatamente 4 alternativas;
    
- somente 1 alternativa correta;
    
- alternativas plausíveis;
    
- evitar alternativas obviamente absurdas;
    
- evitar pistas gramaticais;
    
- evitar alternativa correta muito mais detalhada que as demais;
    
- utilizar interpretação quando o material permitir;
    
- utilizar EXCETO/INCORRETO quando fizer sentido.
    

O campo `correct` deve conter o índice da alternativa correta:

- 0
    
- 1
    
- 2
    
- 3
    

Exemplo:

"options":["A","B","C","D"],  
"correct":2

---

## TF — Verdadeiro ou falso

Formato:

"type":"tf"

Usar:

"options":["Verdadeiro","Falso"]

O campo `correct` deve ser obrigatoriamente:

true

ou

false

Não pedir ao usuário para digitar "Verdadeiro" ou "Falso".

As afirmações devem ser completas e suficientemente específicas para testar conhecimento.

Evitar frases extremamente curtas ou óbvias.

Quando possível, explorar:

- exceções;
    
- condições;
    
- números;
    
- responsabilidades;
    
- sequência;
    
- causa e consequência;
    
- diferenças entre conceitos.
    

---

## GAP — Completar lacuna

Formato:

"type":"gap"

Usar:

"options":[]

A resposta deve ser curta, normalmente **1–3 palavras**.

Priorizar:

- termos técnicos;
    
- nomes;
    
- valores;
    
- unidades;
    
- conceitos;
    
- classificações;
    
- etapas;
    
- palavras-chave.
    

Não exigir respostas longas.

Evitar simplesmente copiar uma frase inteira do material.

A resposta deve ser objetivamente corrigível.

---

## ASSOC — Associação

Formato:

"type":"assoc"

Usar pares:

"options":[  
["Item A","Item 1"],  
["Item B","Item 2"],  
["Item C","Item 3"]  
]

O campo `correct` deve representar os pares corretos por índice.

Exemplo:

"correct":[0,2,1]

Utilizar associação principalmente para:

- conceito → definição;
    
- equipamento → função;
    
- termo → significado;
    
- procedimento → finalidade;
    
- classificação → característica;
    
- regra → aplicação;
    
- item → consequência.
    

Evitar associações em que mais de uma combinação possa ser considerada correta.

---

## DISC — Discursiva

Formato:

"type":"disc"

Utilizar **somente para casos práticos ou situações de aplicação**.

Não criar discursivas puramente conceituais quando uma questão objetiva testar o mesmo conhecimento de forma melhor.

A resposta modelo deve ser curta e estruturada em tópicos.

O campo `correct` deve conter uma resposta-modelo objetiva, contendo os pontos essenciais que devem aparecer na resposta do aluno.

---

# 11. QUESTÕES DE CASO PRÁTICO

Quando o material permitir, criar situações como:

- decisão operacional;
    
- identificação de procedimento;
    
- escolha da ação correta;
    
- análise de uma condição;
    
- identificação de erro;
    
- consequência de determinada ação;
    
- aplicação de norma;
    
- interpretação de dados;
    
- cálculo aplicado.
    

O caso deve utilizar **somente informações sustentadas pelo material**.

Não criar cenários que dependam de conhecimento externo não fornecido.

---

# 12. CÁLCULOS E NÚMEROS

Quando houver fórmulas, valores, limites, conversões ou cálculos no material:

- conferir cuidadosamente os cálculos;
    
- não alterar unidades;
    
- não arredondar incorretamente;
    
- utilizar valores próximos nas alternativas quando isso aumentar a capacidade de discriminação;
    
- garantir que somente uma alternativa seja matematicamente correta.
    

Se houver mais de uma forma aceitável de arredondamento, evitar a questão ou deixar o critério explícito no enunciado.

---

# 13. CATEGORIA

O campo `category` deve identificar a **matéria ou subtópico específico**.

Exemplos:

"category":"Navegação — Cartas Náuticas"

"category":"Meteorologia — Pressão Atmosférica"

"category":"Segurança Marítima — Combate a Incêndio"

"category":"Regulamentos — Responsabilidades"

Não utilizar categorias genéricas como:

"category":"Geral"

quando for possível identificar o subtópico.

---

# 14. EXPLICAÇÃO

O campo `explanation` deve conter uma explicação **curta e objetiva** justificando a resposta.

Não transformar a explicação em aula.

A explicação deve:

- indicar por que a resposta está correta;
    
- mencionar a regra/conceito relevante;
    
- esclarecer a pegadinha quando houver;
    
- ser suficiente para o aluno entender o erro.
    

Evitar explicações longas.

---

# 15. DUPLICAÇÃO

Não criar questões duplicadas.

Também evitar questões que sejam praticamente iguais, mesmo que tenham enunciados diferentes.

Um mesmo conceito pode aparecer mais de uma vez somente quando houver **mudança real no raciocínio**, por exemplo:

- conceito direto;
    
- aplicação prática;
    
- exceção;
    
- interpretação;
    
- pegadinha.
    

---

# 16. CONTROLE DE QUALIDADE

Antes de finalizar, revise internamente **cada questão**.

Verifique:

### Conteúdo

- A questão está sustentada pelo material?
    
- A resposta realmente pode ser encontrada ou deduzida do material?
    
- Não foi inventado nenhum fato?
    

### Correção

- Existe somente uma resposta correta?
    
- O `correct` corresponde realmente à resposta?
    
- A explicação está de acordo com a resposta?
    

### Dificuldade

- A questão é média ou difícil?
    
- A dificuldade vem do raciocínio e não de uma redação confusa?
    

### Pegadinha

- A alternativa errada é plausível?
    
- A pegadinha é tecnicamente válida?
    
- Não existe ambiguidade?
    

### Importação

- Os campos obrigatórios existem?
    
- Os tipos estão corretos?
    
- O formato JSON é válido?
    

### Diversidade

- Não existem duplicadas?
    
- Os diferentes tópicos relevantes do material foram explorados?
    
- A distribuição dos tipos está próxima de 45/25/15/10/5?
    

---

# 17. FORMATO DE SAÍDA

Retorne **APENAS JSON válido**.

Não escreva:

- introdução;
    
- conclusão;
    
- comentários;
    
- Markdown;
    

- observações;
    
- explicações fora do JSON.
    

Estrutura obrigatória:

[  
{  
"type":"mc",  
"question":"texto da questão",  
"category":"categoria",  
"options":["A","B","C","D"],  
"correct":0,  
"explanation":"explicação curta"  
}  
]

Campos permitidos:

- `type`
    
- `question`
    
- `category`
    
- `options`
    
- `correct`
    
- `explanation`
    

**Não adicionar campos extras.**

---

# 18. REGRAS DE UX DA SIMULACORE

As questões devem exigir o **menor esforço possível de digitação**, sem reduzir o nível de aprendizado.

Distribuição:

- 45% MC
    
- 25% TF
    
- 15% GAP
    
- 10% ASSOC
    
- 5% DISC
    

### TF

Usar:

"type":"tf"

e:

"correct":true

ou:

"correct":false

Nunca exigir que o aluno digite "Verdadeiro" ou "Falso".

### MC

Sempre utilizar 4 alternativas.

### GAP

Resposta curta, preferencialmente de 1–3 palavras.

### ASSOC

Utilizar pares objetivos.

### DISC

Utilizar somente para casos práticos e manter a resposta-modelo curta.

Objetivo:

**máximo aprendizado + mínimo teclado + alta semelhança com cobrança de prova.**

---

# 19. REGRA FINAL

A prioridade absoluta é:

**FIDELIDADE AO MATERIAL → CORREÇÃO → QUALIDADE DA QUESTÃO → NÍVEL DE PROVA → PEGADINHA → DISTRIBUIÇÃO**

Nunca sacrificar a correção ou a fidelidade ao material para atingir quantidade, dificuldade ou distribuição.

No final, retornar **somente o array JSON**, sem qualquer texto adicional.