# RELATÓRIO DE CORREÇÃO DAS FÓRMULAS MATEMÁTICAS — SIMULACORE (UNIDADE 1)

**Data da Auditoria e Correção:** 11/10/2026  
**Projeto:** Mecânica dos Fluidos / Hidrodinâmica — Unidade 1 (Capítulos 1 a 8)  
**Ambiente:** Plataforma Simulacore (`Simula_Core.html`)  
**Diretório de Origem (Preservado):** `U1 Simulados ChatGPT/JSON_Simulacore/`  
**Diretório dos Arquivos Corrigidos:** `U1 Simulados ChatGPT/JSON_Simulacore_CORRIGIDOS/`

---

## 1. Causa Identificada da Falha de Exibição

Ao inspecionar a arquitetura da aplicação Simulacore no arquivo `Simula_Core.html` (`C:\Users\Herlon Targino\Documents\quartz\content\Config\0. Simulacore\App Simula Core\Simula_Core.html`), constatou-se que:

1. **Ausência de Mecanismo de Renderização LaTeX:** A aplicação web não importa nem inicializa bibliotecas de renderização dinâmica de fórmulas matemáticas, tais como **MathJax** ou **KaTeX**.
2. **Escapamento Estrito de Strings para Texto Puro:** Toda string de enunciado, alternativa, justificativa ou lacuna é tratada como texto puro e submetida à função de higienização HTML:
   ```javascript
   function esc(str) {
     return String(str)
       .replace(/&/g, '&amp;')
       .replace(/</g, '&lt;')
       .replace(/>/g, '&gt;')
       .replace(/"/g, '&quot;');
   }
   ```
3. **Exibição Literal de Delimitadores:** Consequentemente, quaisquer delimitadores LaTeX (`$...$` ou `$$...$$`) e comandos como `\rho`, `\frac{...}{...}`, `\partial` e `\dot` eram renderizados literalmente na tela (ex.: o usuário via o texto literal `$\rho$` ou `\frac{\partial u}{\partial t}=0` em vez do símbolo formatado).

---

## 2. Padrão Matemático Adotado como Referência

Para determinar a representação compatível com o Simulacore sem alterar o código-fonte da aplicação, foi realizada uma análise comparativa aprofundada com os simulados funcionais do projeto:
- **Arquivo de Referência Direta:** `44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json` (localizado em `Config/1. HID P1/U1/U1 Simulacore/`).
- **Simulados de Física P2:** Conjuntos de questões funcionais em `Config/0. Simulacore/Questões/FIS P2/`.

Nesses arquivos funcionais, as expressões matemáticas são estruturadas inteiramente com **caracteres Unicode e notação textual padronizada**:

| Categoria | Sintaxe Anterior (LaTeX não renderizado) | Padrão Simulacore (Unicode Limpo) |
| :--- | :--- | :--- |
| **Delimitadores** | `$...$` e `$$...$$` | Removidos integralmente |
| **Letras Gregas** | `\rho`, `\mu`, `\tau`, `\theta`, `\phi`, `\sigma` | `ρ`, `μ`, `τ`, `θ`, `ϕ`, `σ` |
| **Derivadas Parciais** | `\frac{\partial u}{\partial x}`, `\frac{\partial^2u}{\partial y^2}` | `∂u/∂x`, `∂²u/∂y²` |
| **Derivada Material** | `\frac{Du}{Dt}`, `\frac{D(\rho V)}{Dt}=0` | `Du/Dt`, `D(ρV)/Dt = 0` |
| **Operadores e Vetores** | `\nabla\cdot\mathbf V=0`, `V\cdot` | `∇·V = 0`, `V·` |
| **Taxas Temporais** | `\dot m=\rho uA`, `\dot{E}`, `\dot{W}` | `ṁ = ρuA`, `Ė`, `Ẇ` |
| **Subscritos** | `V_0`, `C_1`, `p_1`, `u_2`, `\tau_{yx}`, `\sigma_{ij}` | `V₀`, `C₁`, `p₁`, `u₂`, `τ_yx`, `σᵢⱼ` |
| **Sobrescritos** | `V^2`, `y^2`, `a^2`, `\Delta^2u` | `V²`, `y²`, `a²`, `Δ²u` |
| **Frações / Perfis** | `\frac{1}{2}V^2`, `\frac{V_0}{a}y` | `(1/2)V²`, `(V₀/a)y` |
| **Trigonometria** | `\sin\theta`, `g\cos\theta` | `sen θ`, `g cos θ` |
| **Relações e Comparações**| `\rho_1\ne\rho_2`, `p_1 > p_2`, `>` | `ρ₁ ≠ ρ₂`, `p₁ > p₂`, `>` |
| **Lacunas (`gap`)** | `$\rho$`, `$\rho uA$`, `$0$`, `$V_0$` | `ρ`, `ρuA`, `0`, `V₀` |

---

## 3. Quantidade de Fórmulas Examinadas por Capítulo

Foram mapeadas e catalogadas **109 expressões LaTeX únicas**, distribuídas em **502 ocorrências totais** ao longo dos 8 capítulos da Unidade 1:

| Capítulo | Arquivo | Total Questões | Fórmulas Inline (`$...$`) | Fórmulas Display (`$$...$$`) | Total de Fórmulas Corrigidas |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | `SIMULADO_U1_CAPITULO_1_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 98 | 4 | **102** |
| **2** | `SIMULADO_U1_CAPITULO_2_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 46 | 3 | **49** |
| **3** | `SIMULADO_U1_CAPITULO_3_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 45 | 4 | **49** |
| **4** | `SIMULADO_U1_CAPITULO_4_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 37 | 3 | **40** |
| **5** | `SIMULADO_U1_CAPITULO_5_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 43 | 0 | **43** |
| **6** | `SIMULADO_U1_CAPITULO_6_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 52 | 0 | **52** |
| **7** | `SIMULADO_U1_CAPITULO_7_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 60 | 0 | **60** |
| **8** | `SIMULADO_U1_CAPITULO_8_NIVEL_FACIL_AMPLIADO_AUDITADO.json` | 39 | 107 | 0 | **107** |
| **TOTAL**| — | **312** | **488** | **14** | **502** |

---

## 4. Correções Realizadas

1. **Substituição Integral das Expressões:** Todas as 502 ocorrências de delimitadores LaTeX (`$` e `$$`) foram substituídas pela notação Unicode correspondente nos campos `question`, `options`, `correct` e `explanation`.
2. **Preservação e Limpeza das Lacunas (`gap`):**
   - Nas questões de preenchimento de lacunas, o campo `correct` continha comandos como `$\rho$` ou `$0$`. Esses valores foram convertidos para texto limpo (`ρ`, `0`), permitindo que a digitação do usuário ou a validação automática funcionem perfeitamente.
   - Enunciados com sublinhados (ex.: `$\dot m=$ __________` e `$y=$ ____`) foram convertidos para `ṁ = __________` e `y = ____`, garantindo legibilidade imediata sem fragmentação visual.
3. **Tratamento de Expressões com Quebras de Linha:**
   - Equações extensas multilinhas (como a equação diferencial da conservação da massa e os componentes da aceleração convectiva) foram unificadas em linhas contínuas legíveis:
     - `∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z + ∂ρ/∂t = 0`
     - `a_x = ∂u/∂t + u(∂u/∂x) + v(∂u/∂y) + w(∂u/∂z)`

---

## 5. Resultado da Validação dos Arquivos JSON

A validação foi realizada via rotina automatizada (`validate_corrections.py`), verificando os seguintes critérios:

1. **Sintaxe JSON:** Todos os 8 arquivos em `JSON_Simulacore_CORRIGIDOS` possuem sintaxe JSON válida e foram formatados com recuo de 2 espaços e codificação UTF-8 sem BOM.
2. **Total de Questões e Tipologia:**
   - 39 questões por arquivo (312 questões no total, 100% preservadas).
   - Tipos de questão: **9 de Múltipla Escolha (`mc`)**, **15 de Verdadeiro ou Falso (`tf`)** e **15 de Lacunas (`gap`)** em cada capítulo.
3. **Preservação de Gabaritos e Opções:**
   - Em questões de múltipla escolha (`mc`), os índices numéricos inteiros (0 a 3) e o vetor de 4 alternativas mantiveram rigorosamente a mesma ordem e significado.
   - Em questões de verdadeiro ou falso (`tf`), os booleanos nativos (`true` e `false`) não sofreram qualquer alteração.
   - Em questões de lacuna (`gap`), as respostas mantiveram a exata correspondência conceitual com o gabarito original.
4. **Preservação de Justificativas:** Todas as 312 questões possuem o campo `explanation` completo, sem perda de texto explicativo.
5. **Varredura de Caracteres Residuais:**
   - Total de delimitadores `$` restantes nos 8 arquivos: **0**.
   - Total de comandos LaTeX com barra invertida (`\`) não processados: **0**.

---

## 6. Arquivos Corrigidos e Caminhos

Os arquivos originais foram mantidos intactos em `JSON_Simulacore/`. As versões corrigidas e prontas para importação no Simulacore estão localizadas em:

1. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_1_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
2. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_2_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
3. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_3_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
4. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_4_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
5. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_5_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
6. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_6_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
7. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_7_NIVEL_FACIL_AMPLIADO_AUDITADO.json`
8. `C:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulados ChatGPT\JSON_Simulacore_CORRIGIDOS\SIMULADO_U1_CAPITULO_8_NIVEL_FACIL_AMPLIADO_AUDITADO.json`

---

## 7. Verificação Visual Recomendada no Navegador

Embora todas as 502 expressões tenham sido convertidas rigorosamente de acordo com o padrão comprovado do arquivo funcional `44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json`, recomenda-se que o usuário realize um teste visual abrindo o `Simula_Core.html` e carregando um dos simulados (por exemplo, os Capítulos 1 e 8, que possuem maior densidade de fórmulas) para checar:
1. Renderização das fontes do sistema para subscritos e sobrescritos (ex.: `V₀`, `∂²u/∂y²`).
2. Digitação e conferência nas questões de lacuna (`gap`), garantindo conforto na inserção de símbolos como letras gregas ou texto equivalente.
