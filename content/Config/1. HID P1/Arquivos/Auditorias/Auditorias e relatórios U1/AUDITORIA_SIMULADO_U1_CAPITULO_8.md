# Auditoria do Simulado 8 (Capítulo 8)

## 1. Escopo e Metodologia
Auditoria realizada sobre os arquivos `SIMULADO_U1_CAPITULO_8.md` e o seu par independente `GABARITO_COMENTADO_U1_CAPITULO_8.md`. O referencial técnico basilar é o documento `031-034_Mecanica_dos_Fluidos_Capitulo_8.md` atrelado ao `SIMULADO_U1_CAPITULO_1.md` (fonte da Questão 5).

Os testes de integridade foram segregados em conferência teórica manual rigorosa e medições de string lógicas via PowerShell para garantir que falsos-positivos não inflassem o resultado final.

## 2. Inspeção Automatizada de Integridade e Estrutura
Foi executado script extraindo isoladamente blocos pelo método lógico `Substring` ao invés de padrões puramente literais vagos.

**Resultados do Log de Execução (PowerShell):**
- **Enunciado da Questão 5:** Extraídos os caracteres entre o título e a tag final. O tamanho registrado no arquivo de origem (Sim 1) foi exatos **489** bytes, coincidindo assimetricamente com os **489** de destino no Simulado 8. *Conclusão: 100% Idêntico.*
- **Resolução da Questão 5 (Gabarito):** Recorte efetuado entre o subtítulo final e o fim do documento (EOF). O registro marcou **2262** caracteres para a fonte e destino. *Conclusão: 100% Idêntico.*
- **Sincronia do Gabarito:** O rodapé do Simulado detém **15446** caracteres que foram perfeitamente emparelhados ao clone solitário standalone sem detecção de desvios, ausências ou erros de conversão no UTF-8.
- **Estruturação Funcional (Regex Matches):**
  - Questão 1 apontou 5 afirmativas formatadas (I a V). (1 resposta)
  - Questão 2 apontou 10 traços restritivos formatando lacunas.
  - Questão 3 apontou 10 aberturas condicionais de "Verdadeiro ou Falso".
  - Questão 4 apontou 5 subquestões base portando as exatas 25 alternativas "A–E".
  - Questão 5 marcou os 6 passos fixos (1 a 6).
  - Total de validação estática: **57 unidades.**

## 3. Avaliação Conceitual (Questões 1 a 4)

Com as métricas asseguradas, procedeu-se a revisão humana contra a teoria da mecânica friccional plana:

- **Fidelidade da Equação de Couette:** O material fonte destaca amplamente o declínio de Navier-Stokes. A cobrança foi exata ao ressaltar a abolição das pressões diferenciais isobáricas ($p_1 = p_2$) e do empuxo ($\rho g_x = 0$) focando no cisalhamento $0=\mu (\partial^2 u/\partial y^2)$.
- **Escoamento Linear:** Foi bem diferenciado nas questões a distinção vital do perfil gerado, que em Couette é retilíneo/linear, em oposição frontal à barriga parabólica de Poiseuille. Não há pegadinhas e os enunciados são blindados.
- **Entrance Region x Desenvolvido:** Exigiu-se a distinção do termo $\partial u / \partial x = 0$ restritivamente apenas quando as boundary layers se fundem na linha central da modelagem tridimensional elástica descrita. 
- **Sem inserção externa:** A imagem aditiva "Developing Flow" foi citada, mas a cobrança e o jargão foram circunscritos ao que o autor expressou didaticamente ("viscous drag", "boundary layers", "centre line"). Nenhuma propriedade termodinâmica alienígena ou fórmulas exóticas foram validadas sem suporte expresso.

## 4. Conclusão Final
O Simulado 8 encontra-se chancelado sob alto nível de restrição, cobrindo o tema sem viciar os algoritmos de conferência. Não foram omitidas falhas e o material encontra-se apto, sincronizado e sem ambiguidades residuais.
