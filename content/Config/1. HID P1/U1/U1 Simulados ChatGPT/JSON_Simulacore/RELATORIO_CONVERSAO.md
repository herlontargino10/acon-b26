# RELATÓRIO DE CONVERSÃO DOS SIMULADOS DA UNIDADE 1 PARA JSON DO SIMULACORE

**Data de Execução:** 11/10/2026  
**Ambiente:** Simulados da Unidade I de Mecânica dos Fluidos / Hidrodinâmica  
**Pasta de Saída:** `JSON_Simulacore/`  
**JSON de Referência Estrutural:** `44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json`

---

## 1. TABELA CONSOLIDADA DE CONVERSÃO

| Capítulo | Questões na origem | Questões convertidas | Questões pendentes | JSON válido | Fidelidade conferida |
|---|---:|---:|---:|---|---|
| **Capítulo 1** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 2** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 3** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 4** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 5** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 6** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 7** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **Capítulo 8** | 40 | 39 | 1 (Buckingham–$\Pi$) | Sim (OK) | Sim (100% conferida) |
| **TOTAL** | **320** | **312** | **8** | **Sim (8/8)** | **Sim (312/312)** |

---

## 2. INVENTÁRIO DETALHADO POR CAPÍTULO

Cada arquivo simulado original é estruturado em 5 grandes blocos de avaliação:
- **Questão 1:** Múltipla escolha sobre conjunto de afirmativas (I a V), com 5 alternativas `(a)` a `(e)`.
- **Questão 2:** Preenchimento de lacunas com 15 itens independentes (`gap`).
- **Questão 3:** Verdadeiro ou falso com 15 itens conceituais (`tf`).
- **Questão 4:** Múltipla escolha analítica/conceitual com 8 subquestões (`mc`).
- **Questão 5:** Exercício discursivo de Análise Dimensional de Buckingham–$\Pi$ em 6 passos fundamentais.

### Composição das Questões Convertidas por Capítulo:
- **Múltipla Escolha (`mc`):** 9 questões (Questão 1 + 8 subquestões da Questão 4).
- **Preenchimento de Lacunas (`gap`):** 15 questões (itens 1 a 15 da Questão 2).
- **Verdadeiro ou Falso (`tf`):** 15 questões (itens 1 a 15 da Questão 3).
- **Total por capítulo convertido:** 39 questões por arquivo JSON.
- **Total geral convertido nos 8 capítulos:** **312 questões objetivas**.

---

## 3. QUESTÕES PENDENTES: TRATAMENTO DO EXERCÍCIO DE BUCKINGHAM–$\Pi$

Em estrita conformidade com a **Seção 5.4 e Seção 9** das diretrizes do projeto:
> *"Se houver questões discursivas, questões compostas, cálculos ou outros formatos sem correspondência comprovada, registre-as no relatório de pendências. Não as descarte, não invente tipos de questão e não as transforme artificialmente em múltipla escolha."*

A **5ª Questão** de todos os 8 simulados consiste em um problema discursivo completo de Análise Dimensional resolvido sistematicamente em seis passos:
1. Identificação/listagem das variáveis ($n$ variáveis).
2. Determinação das dimensões físicas fundamentais ($[M, L, T]$).
3. Contagem das dimensões fundamentais e determinação do número de grupos adimensionais ($j = n - k$).
4. Escolha das variáveis repetitivas.
5. Montagem da equação dimensional do grupo $\Pi$.
6. Determinação algébrica dos expoentes e apresentação da solução / número adimensional final (ex.: Reynolds).

### Análise de Compatibilidade Estrutural:
- O JSON de referência obrigatório (`44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json`) suporta exclusivamente os tipos `mc` (múltipla escolha), `tf` (verdadeiro/falso com opções booleanas) e `gap` (lacuna simples com string esperada).
- Embora em outros bancos do Simulacore exista o tipo `disc` com campo discursivo único, o modelo de importação de referência fornecido não contempla questões discursivas estruturadas em 6 passos.
- Portanto, para **garantir a integridade pedagógica e documental e evitar adulteração do exercício**, as 8 questões de Buckingham–$\Pi$ foram catalogadas como **pendentes de definição/suporte da plataforma**, sem serem deformadas em testes de múltipla escolha.

### Detalhamento das 8 Questões de Buckingham–$\Pi$ Pendentes:
1. **Capítulo 1 — 5ª Questão:** Duto circular ($u, D, \mu, \rho$), obtenção de $\Pi_1 = \mu / (\rho u D)$ e $Re = \rho u D / \mu$.
2. **Capítulo 2 — 5ª Questão:** Duto circular ($u, D, \mu, \rho$), obtenção de $\Pi_1 = \mu / (\rho u D)$ e $Re = \rho u D / \mu$.
3. **Capítulo 3 — 5ª Questão:** Duto circular ($u, D, \mu, \rho$), obtenção de $\Pi_1 = \mu / (\rho u D)$ e $Re = \rho u D / \mu$.
4. **Capítulo 4 — 5ª Questão:** Duto circular ($u, D, \mu, \rho$), variáveis repetitivas $u, D, \rho$, obtenção de $\Pi_1 = \mu / (\rho u D)$ e $Re = \rho u D / \mu$.
5. **Capítulo 5 — 5ª Questão:** Escoamento interno ($U, \rho, \mu, D$), sistema de equações de expoentes, obtenção de $\Pi = \rho U D / \mu$.
6. **Capítulo 6 — 5ª Questão:** Escoamento Poiseuille ($U, \Delta p, a, \mu, \rho$), 5 variáveis e 3 dimensões, formação de 2 grupos adimensionais.
7. **Capítulo 7 — 5ª Questão:** Canal inclinado ($U, g, a, \mu, \rho$), 5 variáveis e 3 dimensões, formação de 2 grupos adimensionais com gravidade.
8. **Capítulo 8 — 5ª Questão:** Escoamento de Couette ($u, D, \mu, \rho$), obtenção de $\Pi_1 = \mu / (\rho u D)$ e $Re = \rho u D / \mu$.

---

## 4. PRESERVAÇÃO INTEGRAL DAS JUSTIFICATIVAS (`explanation`)

Todas as 312 questões convertidas contam com justificativa detalhada e fundamentada:
- **Questões de Múltipla Escolha (`mc`):** As justificativas preservam os comentários item a item do gabarito original, detalhando o porquê de cada afirmativa estar correta ou incorreta, além de deduções algébricas e notas conceituais.
- **Questões de Verdadeiro ou Falso (`tf`):** Todas as justificativas associadas explicam exatamente o fundamento físico e a interpretação do resumo do capítulo correspondente.
- **Questões de Preenchimento de Lacunas (`gap`):** Todas as explicações originais (incluindo notas conceituais do gabarito, justificativas de termos compostos e sequenciamento didático do capítulo) foram integralmente preservadas.
- **Ausência de justificativas:** 0 questões (100% das questões convertidas possuem justificativas ricas e pertinentes ao seu enunciado).

---

## 5. NOTAÇÃO CIENTÍFICA, FÓRMULAS E CARACTERES ESPECIAIS

Durante a conversão, foi mantida a fidelidade às equações e notações de Mecânica dos Fluidos:
- Símbolos gregos preservados: $\rho$, $\mu$, $\tau$, $\theta$, $\nabla$, $\Pi$, etc.
- Notação de derivadas parciais e materiais: $\frac{\partial u}{\partial x}$, $\frac{\partial v}{\partial y}$, $\frac{\partial p}{\partial x}$, $\frac{Du}{Dt}$, etc.
- Caracteres especiais, aspas e barras invertidas foram devidamente escapados pelo serializador JSON UTF-8 (`ensure_ascii=False`), mantendo compatibilidade sintática estrita com o padrão JSON RFC 8259.

> **Observação para teste de renderização no Simulacore:** As fórmulas matemáticas no arquivo Markdown utilizam sintaxe LaTeX delimitada por `$...$` e `$$...$$`. O importador do Simulacore e o frontend devem ter suporte a bibliotecas de renderização MathJax ou KaTeX para que as expressões apareçam formatadas visualmente.

---

## 6. VALIDAÇÃO TÉCNICA E ESTRUTURAL

Todos os 8 arquivos JSON gerados foram submetidos a testes rigorosos por analisador sintático e validador estrutural automatizado (`validate_all.py`), conferindo:
1. **Sintaxe JSON:** 100% válidos, parseados sem erro.
2. **Raiz:** Todos os arquivos contêm uma lista JSON direta `[...]`.
3. **Campos Obrigatórios:** Todos os objetos contêm `type`, `question`, `category` e `explanation`.
4. **Múltipla Escolha (`mc`):**
   - Campo `options` presente como lista de strings (4 ou 5 opções conforme original).
   - Campo `correct` é obrigatoriamente um número inteiro (`int`), iniciando em índice zero (`0`), apontando com exatidão para a alternativa correta no gabarito oficial.
5. **Verdadeiro ou Falso (`tf`):**
   - Campo `options` padronizado como `["Verdadeiro", "Falso"]`.
   - Campo `correct` é obrigatoriamente um booleano nativo (`true` ou `false`, sem aspas).
6. **Preenchimento de Lacunas (`gap`):**
   - Campo `correct` é uma string com o termo exato esperado.
   - Campo `options` não está presente (conforme JSON de referência).
7. **Limpeza de Artefatos:** Remoção de divisores residuais de markdown (`---`) e marcadores de formatação redundantes (`**`).

---

## 7. SITUAÇÃO DO TESTE DE IMPORTAÇÃO

- **Status do Teste:** O teste de importação direta na plataforma Simulacore **NÃO** foi realizado nesta etapa, uma vez que não foram fornecidas credenciais ativas, endpoint de API ou acesso web ao painel do Simulacore no ambiente de trabalho.
- **Garantia Técnica:** Todos os arquivos passaram na validação sintática e estrutural de paridade 1:1 com o arquivo `44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json`, que representa o formato de sucesso homologado na plataforma.
