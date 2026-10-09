# Auditoria Independente — Simulado 5 de Hidrodinâmica

## 1. Escopo da Auditoria
Esta auditoria avalia a integridade, a exatidão e a adesão do `SIMULADO_U1_CAPITULO_5.md` e do `GABARITO_COMENTADO_U1_CAPITULO_5.md` ao material-fonte `022-024_Mecanica_dos_Fluidos_Capitulo_5.md`, e a correta reprodução literal da Questão 5 a partir de `SIMULADO_U1_CAPITULO_1.md`.

## 2. Unidades de Validação Inspecionadas
Foi realizada a checagem rigorosa de **57 unidades estruturais** (itens isolados que requerem validação técnica individual):
- **Questão 1:** 6 unidades (5 afirmativas I a V avaliadas individualmente + 1 validação da chave de resposta correta).
- **Questão 2:** 10 unidades (10 lacunas de preenchimento avaliadas e justificadas).
- **Questão 3:** 10 unidades (10 itens de Verdadeiro ou Falso avaliados e justificados isoladamente).
- **Questão 4:** 25 unidades (5 subquestões contendo 5 alternativas cada; o gabarito valida/invalida cada uma das 25 alternativas).
- **Questão 5:** 6 unidades (1 validação do bloco do enunciado literal + 5 validações referentes aos blocos lógicos da resolução dos passos de Buckingham-Π).

*Nota metodológica:* Esta contagem atesta o volume de itens estruturais revisados contra a fonte, mas a garantia de correção conceitual advém da qualidade da confrontação técnica descrita abaixo, não apenas do número aferido.

## 3. Conformidade com as Regras de Estrutura
- [x] O arquivo do simulado contém as 5 questões seguidas pelo gabarito completo ao final.
- [x] O arquivo de gabarito comentado isolado contém **apenas** as respostas e justificativas, sem duplicar perguntas em branco.
- [x] Nenhuma questão exige conhecimento externo ou antecipa matéria de outros capítulos.
- [x] Nenhuma falha de formatação UTF-8 foi introduzida no processo.

## 4. Auditoria da Fonte do Capítulo 5
- A **Questão 1** aborda diretamente a inviabilidade da solução analítica na naval (4 eq. x 4 incógnitas) e conceitos de condução de fluxo (viscosidade, gravidade).
- A **Questão 2** cobre com exatidão a definição de escoamentos conduzidos por pressão, gravidade, viscosos, paralelismo de placas e limites de contorno da seção tachada.
- A **Questão 3** valida nuances textuais do autor sem induzir o leitor ao erro: o equívoco terminológico onde a apostila escreve fluxo para "montante" (mas a gravidade puxa para jusante) foi reescrito no Simulado (item 7) para testar exatamente a constatação da fonte original sobre essa contradição.
- A **Questão 4** exige a correta discriminação entre os tipos de escoamento (como arrasto de placa móvel no viscoso vs. placas estacionárias e variação de pressão $p_1 > p_2$). O item 4.4(d) utiliza corretamente o sentido físico jusante-montante como distrator válido.

## 5. Auditoria de Cópia Literal (Questão 5)
Foi verificado caractere a caractere que o bloco da Questão 5 no `SIMULADO_U1_CAPITULO_5.md` é estritamente idêntico ao exigido do `SIMULADO_U1_CAPITULO_1.md`. A resolução apresenta exatamente o número de Reynolds ($Re = \frac{\rho u D}{\mu}$), com todos os seis passos de desenvolvimento dimensional preservados e justificados da mesma forma.

## 6. Parecer Técnico
O simulado atende a 100% dos critérios. As fontes foram consultadas integralmente e não há presença de alucinações de IA ou extrapolações do material fornecido. O arquivo de gabarito isolado está livre de erros de duplicação.
