GERADOR DE QUESTÕES — SIMULACORE (JSON IMPORTÁVEL)

```txt
Vou enviar um ou mais materiais:

- PDF
    
- Slides
    
- Resumo
    
- Transcrição de aula
    
- Prova antiga
    
- Áudio transcrito
    
- Anotações
    

Sua tarefa é gerar um banco de questões PRONTO PARA IMPORTAÇÃO na minha plataforma SIMULACORE.

REGRAS IMPORTANTES:

NÃO explicar teoria.  
NÃO resumir conteúdo.  
NÃO criar texto de aula.

Objetivo:  
Criar questões para treino e prova.

━━━━━━━━━━━━━━━━━━

FORMATO DE SAÍDA

Retornar APENAS JSON válido.

Estrutura obrigatória:

[  
{  
"type":"mc|tf|gap|disc|assoc",  
"question":"texto",  
"category":"categoria",  
"options":[],  
"correct":"",  
"explanation":"explicação"  
}  
]

Campos:

type:  
mc = múltipla escolha  
tf = verdadeiro/falso  
gap = completar lacuna  
disc = discursiva  
assoc = associação

question:  
texto completo.

category:  
matéria ou subtópico.

options:  
mc → array alternativas  
tf → ["Verdadeiro","Falso"]  
gap → []  
disc → []  
assoc → pares ou opções

correct:  
mc → índice correto (0–3)  
tf → true ou false  
gap → resposta  
disc → resposta modelo resumida  
assoc → pares corretos

explanation:  
explicação curta.

━━━━━━━━━━━━━━━━━━

DISTRIBUIÇÃO

Gerar automaticamente:

30% múltipla escolha  
20% verdadeiro/falso  
20% completar lacuna  
20% discursiva  
10% associação

Se o material for pequeno:  
mínimo 20 questões.

Se grande:  
gerar 50–150.

━━━━━━━━━━━━━━━━━━

DIFICULDADE

Misturar:

30% fácil  
50% média  
20% difícil

NÃO escrever dificuldade no JSON.

━━━━━━━━━━━━━━━━━━

PEGADINHAS (OBRIGATÓRIO)

Criar questões com:

- inversão de conceitos
    
- exceções
    
- números próximos
    
- alternativas quase iguais
    
- conceitos confundíveis
    
- negativos ("EXCETO")
    
- detalhes regulatórios
    
- interpretação
    
- caso prático
    

Mas:  
NUNCA inventar fatos.

━━━━━━━━━━━━━━━━━━

TIPO ESPECÍFICO

MC:

- 4 alternativas
    
- apenas 1 correta
    
- evitar óbvias
    

TF:

- afirmações completas
    
- evitar frases curtas
    

GAP:

- exigir recuperação ativa
    
- evitar copiar texto
    

DISC:

- resposta em tópicos
    
- pronta para correção
    

ASSOC:  
Formato:

"options":[  
["Item A","Item 1"],  
["Item B","Item 2"]  
]

correct:  
[  
0,  
1,  
2  
]

━━━━━━━━━━━━━━━━━━

QUALIDADE

Priorizar:

1. assuntos repetidos
    
2. títulos
    
3. exemplos do professor
    
4. tabelas
    
5. pegadinhas
    
6. questões anunciadas
    

Ignorar:

- introdução
    
- agradecimentos
    
- exemplos irrelevantes
    

━━━━━━━━━━━━━━━━━━

SE HOUVER BIZU DE PROVA

Transformar cada bizu em:

- 1 discursiva
    
- 2 objetivas
    
- 1 pegadinha
    

━━━━━━━━━━━━━━━━━━

ANTES DE FINALIZAR

Validar:

✔ JSON válido  
✔ sem vírgula sobrando  
✔ importável  
✔ sem duplicadas  
✔ respostas corretas  
✔ categories preenchidas  
✔ sem campos extras

Entregar somente JSON.


REGRA DE UX DA SIMULACORE

Gerar questões pensando no menor esforço de digitação.

Distribuição:

45% MC  
25% TF  
15% GAP  
10% ASSOC  
5% DISC

TF:  
Usar:  
"type":"tf"

Salvar:  
"correct": true  
ou  
"correct": false

NÃO pedir para digitar:  
"Verdadeiro"  
ou  
"Falso"

MC:  
Sempre usar options.

DISC:  
Somente caso prático.

GAP:  
Resposta curta (1–3 palavras).

Objetivo:  
Máximo aprendizado com mínimo teclado.