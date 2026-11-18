# RELATÓRIO ETAPA 2 — 02 MARÉ

## 1. Fonte utilizada

02_Maré.pdf

## 2. Inventário utilizado

INVENTARIO_02_MARE.md

## 3. Estrutura construída

A construção seguiu fielmente a divisão observada na fonte, ramificada nos seguintes 5 grandes blocos temáticos:
1. **Teoria das Marés**
   - O que é Maré
   - Fatores Causadores das Marés (e o domínio da Lua)
   - Ciclos Lunares e Amplitudes (Sizígia e Quadratura)
   - Tipos de Maré
   - Principais Componentes de Maré (Courtier)
   - Classificação por Altura
   - Importância e Riscos à Navegação (Maré Meteorológica)
2. **Elementos e Características das Curvas de Marés**
   - Curvas de Maré
   - Elementos Formadores (PM, BM, A, NM, h, NR)
   - Relação Barco x Fundo do Mar (Sondagem)
3. **Tábua de Marés (TM)**
   - O que é a Tábua de Marés
   - Equação da Previsão da Maré
   - Interpretação da Tábua
4. **Determinação da Altura da Maré em um Dado Instante**
   - Ideia Principal (Intervalo e Variação)
   - Exemplo / Estudo de Caso Resolvido
   - Método 1: Regra dos Doze Avos
   - Método 2: Interpolação Gráfica
5. **Método Expedito de Previsão e Estabelecimento do Porto (EP)**
   - Culminação da Lua
   - O Almanaque Náutico
   - O Estabelecimento do Porto (EP)

## 4. Fórmulas preservadas

Quantidade identificada e preservada: 9 fórmulas/equações.
1. Atração Gravitacional: $F = G \frac{(Mm)}{r^2}$
2. Relação Conceitual (Força Geradora de Maré = Atração Gravitacional + Força Centrífuga)
3. Critério de Courtier: $F = \frac{K_1 + O_1}{M_2 + S_2}$
4. Amplitude da Maré: $A = PM - BM$
5. Nível Médio: $NM = \frac{PM + BM}{2}$
6. Altura da Maré: $h = \text{nível instantâneo} - NR$
7. Profundidade Real: Profundidade real = Sondagem + Altura da maré
8. Equação da Previsão da Maré: $\eta(t) = Z_0 + \sum_j H_j \cos(\sigma_j t + g_j)$
9. Estabelecimento do Porto: $EP = PM - \text{Culminação da Lua}$

*(A variação $\Delta H = H_{PM} - H_{BM}$ listada no inventário está englobada no desdobramento de amplitude).*

## 5. Figuras e gráficos tratados

- 6 gráficos de marés (sendo gráficos de onda periódica, fases, tipos de maré, e curva gráfica de interpolação da enchente/vazante).
- 11 diagramas/infográficos/mapas (incluindo atração gravitacional, sistemas Sol-Terra-Lua, fluxograma de Tábuas, recortes de tábuas de marés, mapas meteorológicos e diagrama do Movimento da Lua).

## 6. Tabelas tratadas

Foram mantidas as 7 tabelas e descrições tabulares relevantes da fonte:
1. Comparação entre parâmetros e força da Lua e do Sol.
2. Tabela do Critério de Courtier.
3. Classificação de altura (Micro, Meso, Macro, Hipermarés).
4. Componentes Harmônicos principais adaptados de Pugh 2004.
5. Regra dos 12 Avos (frações/horas).
6. Almanaque Náutico de 2025 focado na coluna "Passagem Meridiana".
7. Tabela referencial de Estabelecimento do Porto (EP) para o Brasil.

## 7. Exemplos e exercícios

Foram preservados os 2 exemplos identificados na Etapa 1:
- Exemplo introdutório contendo as variáveis $PM = 10m$ e $BM = 5m$.
- Estudo de caso guiado utilizando a "saída do porto de SL às 10 h", calculando $\Delta H$ por meio da Regra dos Doze Avos e conferindo os $4,30m$ resultantes através da Interpolação Gráfica.

## 8. Inconsistências preservadas

As 2 inconsistências listadas no inventário foram transportadas com bloco `[!warning] Inconsistência da fonte`:
1. Ambiguidade devido a legendas faltantes para os itens "HS" e "FC" nas cartas de Maré Meteorológica.
2. Divergência metodológica explícita onde o "Porto de SL" citado no passo a passo da TM não possui ligação clara com as amostras de tábuas de Julho utilizadas para instruir o exercício.

## 9. Uso de fontes externas

Nenhuma fonte externa foi utilizada.

## 10. Fidelidade à fonte

Todo o material foi construído exclusivamente a partir dos textos, slides e representações do PDF autoral `02_Maré.pdf`, utilizando o mapa fornecido pelo inventário. Todo o trabalho limitou-se ao escopo da Unidade 2 de Oceanografia Física sem misturas ou vazamentos de conteúdo da Unidade 1.

## 11. Veredito

**APROVADO**

- O material atende a todos os critérios.
- Garantiu cobertura temática total dos 5 blocos do inventário.
- Preservou as 9 equações exigidas.
- Contextualizou didaticamente sem recorrer a saberes externos, mantendo tabelas e o exercício prático passo-a-passo e a exposição das duas inconsistências.
