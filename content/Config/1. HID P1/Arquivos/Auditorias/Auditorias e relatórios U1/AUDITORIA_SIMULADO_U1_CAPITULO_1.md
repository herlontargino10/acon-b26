# Relatório de Auditoria Final — Simulado de Hidrodinâmica (Capítulo 1)

## 1. Fonte Utilizada e Inventário
- **Arquivos-fonte exclusivos utilizados e preservados:** 
  1. `001-006_Mecanica_dos_Fluidos_Capitulo_1.md` (Fonte exclusiva para Questões 1 a 4).
  2. `questao-5.png` (Fonte exclusiva para a Questão 5).
- Nenhuma fonte externa ou da internet foi consultada.

## 2. Auditoria Completa das Questões (Matriz de Cobertura e Fundamentação)

### Questão 1 (Afirmativas e Alternativas)
- **Afirmativa I:** Fiel à fonte (Seções 1 e 21). Verdadeira.
- **Afirmativa II:** Distrator validado. Falso, pois a vazão é taxa por unidade de *tempo*, não área (Seções 5 e 21).
- **Afirmativa III:** Fiel à fonte (Seção 13). Verdadeira.
- **Afirmativa IV:** Distrator validado. Falso, pois no caso incompressível a densidade é *constante* (Seção 14).
- **Afirmativa V:** Fiel à fonte (Seções 7 e 26). Verdadeira.
- **Unicidade da resposta:** Apenas a alternativa (b) agrupa as opções corretas (I, III, V). Nenhuma outra combinação satisfaz.
- **Status:** APROVADO

### Questão 2 (Lacunas)
1. **energia** (Seção 1). Exato.
2. **densidade** (Seção 2). Exato.
3. **volume de controle** (Seção 3). Exato.
4. **tempo** (Seção 5). Exato.
5. **saindo** ou *de saída* (Seções 4, 8, 22). Exato e equivalência testada.
6. **local** (Seções 7, 26). Exato.
7. **continuidade** (Seção 13). Exato.
8. **incompressíveis** (Seção 14). Exato.
9. **velocidade** (Seção 16). Exato.
10. **espaço** (Seções 20, 22). Exato.
- **Status:** APROVADO

### Questão 3 (Verdadeiro ou Falso)
- **Item 1:** Falso (Seção 1). Correção aplicada no gabarito: indicada para casos complicados.
- **Item 2:** Verdadeiro (Seção 2). Fiel à fonte.
- **Item 3:** Falso (Seção 3). Correção aplicada no gabarito: volume é fixo no espaço.
- **Item 4:** Verdadeiro (Seção 5). Fiel à fonte.
- **Item 5:** Verdadeiro (Seção 12). Fiel à fonte.
- **Item 6:** Verdadeiro (Seção 14). Fiel à fonte.
- **Item 7:** Falso (Seção 15). Correção aplicada no gabarito: interpretado como massa saindo.
- **Item 8:** Verdadeiro (Seções 17, 19). Fiel à fonte.
- **Item 9:** Verdadeiro (Seção 11). Fiel à fonte.
- **Item 10:** Falso (Seção 13). Correção aplicada no gabarito: a variação da densidade participa da forma geral.
- **Status:** APROVADO

### Questão 4 (Múltipla Escolha)
- **4.1:** Alternativa (e) correta (Seções 15, 16). Distratores desqualificados pelas próprias regras do texto.
- **4.2:** Alternativa (c) correta (Seções 10, 13). Demais alternativas remetem a outros conceitos listados no material.
- **4.3:** Alternativa (b) correta (Seção 3, 22). Demais alternativas são conceitualmente inconsistentes com o PDF original.
- **4.4:** Alternativa (b) correta (Seções 4, 8, 22). Demonstra a justificativa física para o sinal.
- **4.5:** Alternativa (c) correta (Seções 17, 22). Relação entre normal e velocidade.
- **Status:** APROVADO

### Questão 5 (Auditoria Matemática e Metodológica)
A questão foi elaborada rigorosamente sobre a imagem `questao-5.png`.
- **Enunciado:** Reproduzido fielmente.
- **Passo 1:** Variáveis $u, D, \mu, \rho$ ($n=4$). Correto.
- **Passo 2:** Dimensões $[u]=LT^{-1}, [D]=L, [\mu]=ML^{-1}T^{-1}, [\rho]=ML^{-3}$ ($m=3$). Correto.
- **Passo 3:** $N_\Pi = 4-3=1$. Correto.
- **Passo 4:** Repetitivas $u, \mu, \rho$. Não-repetitiva $D$. Correto.
- **Passo 5:** $\Pi_1 = D \rho^a \mu^b u^c$. Correto.
- **Passo 6 (Auditoria Algébrica):** 
  - Equação: $[M^0 L^0 T^0] = [L][ML^{-3}]^a[ML^{-1}T^{-1}]^b[LT^{-1}]^c$
  - Equações do sistema:
    - $M: a + b = 0 \Rightarrow a = -b$
    - $T: -b - c = 0 \Rightarrow c = -b$
    - $L: 1 - 3a - b + c = 0$
  - Substituição: $1 - 3(-b) - b + (-b) = 0 \Rightarrow 1 + 3b - 2b = 0 \Rightarrow 1 + b = 0 \Rightarrow b = -1$.
  - Consequência: $a = -(-1) = 1$ e $c = -(-1) = 1$.
  - Resolução dos expoentes validada: $a=1$, $b=-1$, $c=1$.
  - Equação final de $\Pi_1 = \rho^1 u^1 D^1 \mu^{-1} = \frac{\rho u D}{\mu}$ (Número de Reynolds).
  - Confirmação dimensional do grupo: $[\rho u D / \mu] = (ML^{-3} \cdot LT^{-1} \cdot L) / (ML^{-1}T^{-1}) = (ML^{-1}T^{-1}) / (ML^{-1}T^{-1}) = 1$ (Adimensional comprovado).
- **Status:** APROVADO

## 3. Qualidade Pedagógica e Redação
As cinco questões foram mantidas separadas do arquivo de gabarito e revisadas. Erros ambíguos não foram observados e nenhuma questão precisou ser suprimida na versão final do documento.

## 4. Status Final da Auditoria
- **Todas as respostas foram verificadas.**
- **A Questão 5 está matematicamente correta e comprovada.**
- O simulado está **APROVADO INTEGRALMENTE**.
