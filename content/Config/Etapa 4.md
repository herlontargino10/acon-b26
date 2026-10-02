
```txt
MECÂNICA DOS FLUIDOS — ETAPA 4
Auditoria técnica, matemática, Markdown e Obsidian

==================================================
CONFIGURAÇÃO DESTA EXECUÇÃO
==================================================

FONTE DESTA EXECUÇÃO:
[1_Leis_de_conservação-031-034]

NÚMERO DO CAPÍTULO:
[Não informado pelo usuário.]

ARQUIVO DO CAPÍTULO:
Mecanica_dos_Fluidos_Capitulo_[NÚMERO]_Obsidian_RASCUNHO.md

==================================================
OBJETIVO
==================================================

Executar uma auditoria técnica completa do arquivo produzido.

Verificar:

1. matemática;
2. LaTeX;
3. Markdown;
4. Obsidian;
5. tabelas;
6. CSV;
7. consistência de nomenclatura;
8. integridade estrutural;
9. formatação.

NÃO corrigir o arquivo ainda.

Produzir primeiro um relatório detalhado.

==================================================
AUDITORIA MATEMÁTICA
==================================================

Compare todas as expressões matemáticas do arquivo com a fonte.

Verifique:

- símbolos;
- índices;
- subscritos;
- sobrescritos;
- sinais;
- frações;
- parênteses;
- derivadas;
- diferenciais;
- letras gregas;
- vetores;
- operadores;
- limites;
- igualdade;
- aproximações;
- unidades.

NÃO corrija a matemática da fonte.

O objetivo é verificar fidelidade.

Se a fonte contiver uma expressão aparentemente incorreta e o arquivo
a reproduzir fielmente:

classifique como:

"Fiel à fonte — expressão aparentemente incomum preservada."


==================================================
REGRA ESPECIAL — DIVERGÊNCIA ENTRE RASCUNHO E FONTE
==================================================

Quando uma fórmula do RASCUNHO for diferente da fórmula da FONTE:

NÃO decidir qual fórmula é matematicamente mais correta.

Apenas registrar a divergência.

Classificar como:

"DIVULGÊNCIA DE TRANSCRIÇÃO"

e apresentar:

- fórmula exatamente como aparece na fonte;
- fórmula exatamente como aparece no rascunho;
- página da fonte;
- localização no arquivo;
- diferença encontrada.

Somente na ETAPA 5 a divergência poderá ser corrigida,
e exclusivamente para restaurar a fidelidade à fonte.

A justificativa da correção deve ser:

"Correção realizada para reproduzir a fonte autorizada."

NUNCA:

"Correção realizada porque a fórmula correta deveria ser..."

==================================================

==================================================
AUDITORIA LATEX
==================================================

Verifique:

- delimitadores `$`;
- delimitadores `$$`;
- chaves `{}`;
- comandos LaTeX;
- `\frac`;
- `\partial`;
- `\Delta`;
- letras gregas;
- subscritos;
- sobrescritos;
- `\text{}`;
- equações multilinha.

Procure comandos quebrados ou incompletos.

Exemplos de problemas:

- `\rac`;
- `ho`;
- `ight`;
- chaves não fechadas;
- delimitadores não fechados;
- fórmulas interrompidas.

==================================================
AUDITORIA MARKDOWN
==================================================

Verifique:

- títulos;
- subtítulos;
- listas;
- tabelas;
- negrito;
- itálico;
- blocos de código;
- callouts;
- separadores;
- indentação.

Verifique também se variáveis matemáticas aparecem corretamente como
matemática inline.

Exemplo:

Na direção $x$

e não:

Na direção x

quando $x$ representar uma variável ou eixo matemático.

==================================================
AUDITORIA OBSIDIAN
==================================================

Verifique:

- frontmatter YAML;
- delimitadores `---`;
- callouts;
- fórmulas MathJax;
- tabelas;
- compatibilidade com Markdown do Obsidian.

Callouts devem utilizar sintaxe válida, por exemplo:

> [!important]

> [!warning]

> [!tip]

Não invente sintaxes proprietárias.

==================================================
AUDITORIA DE TABELAS
==================================================

Verifique:

- número de colunas;
- separadores;
- cabeçalhos;
- alinhamento;
- conteúdo quebrado;
- fórmulas dentro das células.

==================================================
AUDITORIA DO CSV PARA ANKI
==================================================

Se o capítulo possuir seção CSV para Anki:

verifique:

- número correto de colunas;
- ausência de colunas extras;
- separador consistente;
- aspas;
- caracteres especiais;
- fórmulas;
- delimitadores;
- ausência de linhas vazias.

Procure especialmente por problemas como:

""$v$""

quando deveria ser:

"$v$"

Não alterar o conteúdo conceitual dos cards.

Apenas verificar a integridade estrutural.

==================================================
AUDITORIA DE CONSISTÊNCIA
==================================================

Verifique se a mesma variável, conceito ou termo aparece com grafias
diferentes ao longo do documento.

Examine:

- nomenclatura;
- símbolos;
- variáveis;
- títulos;
- subtítulos;
- abreviações.

Não altere automaticamente a terminologia da fonte.

==================================================
VERIFICAÇÃO DE FIDELIDADE TEXTUAL E TERMINOLÓGICA
==================================================

Verifique se o RASCUNHO alterou silenciosamente:

- palavras utilizadas pelo professor;
- terminologia;
- expressões técnicas;
- frases com significado específico;
- qualificadores;
- condições;
- exceções.

Não considere uma substituição válida apenas porque o termo utilizado
no rascunho parece tecnicamente mais correto.

Se a fonte disser uma coisa e o rascunho disser outra:

registrar como:

"DIVERGÊNCIA DE TRANSCRIÇÃO / TERMINOLOGIA"

Não corrigir nesta etapa.

A correção será realizada somente na Etapa 5.

==================================================

==================================================
RELATÓRIO FINAL
==================================================

Entregue:

# Auditoria Técnica — Capítulo [NÚMERO]

## 1. Problemas de fórmula

## 2. Problemas de LaTeX

## 3. Problemas de Markdown

## 4. Problemas de Obsidian

## 5. Problemas de tabelas

## 6. Problemas no CSV para Anki

## 7. Problemas de consistência

## 8. Correções necessárias

## 9. Checklist final

Classifique cada problema como:

- Crítico
- Importante
- Menor
- Sem problema

==================================================
REGRA FINAL
==================================================

NÃO alterar o arquivo nesta etapa.

Produzir apenas o relatório de auditoria.

As correções serão realizadas na Etapa 5.

==================================================
FIM DA ETAPA 4
==================================================