---
title: "ECDIS, ENC, S-57, RENC e ZoC"
topico: 3
disciplina: Navegação
curso: ACON-B
prova: 2
fonte: "navegação_prova_2.txt + ACON-B__NAV II 2° Prova__50_ECDIS.txt"
atualizado: 2026-10-02
tags: [navegacao, acon-b, prova-2, ecdis, enc, s-57, renc, zoc]
aliases: [ECDIS, ENC, S-57, RENC, ZoC, Zones of Confidence, Carta Eletrônica de Navegação]
---

# Tópico 3 — ECDIS, ENC, S-57, RENC e ZoC

Anterior: [[02 VTS LPS VTMIS v1]] · Próximo: [[04 GNSS]] · Índice: [[00 Índice Navegação Prova 2]]

> [!note] Como ler esta versão
> Todo o conteúdo anterior foi **mantido**. O que veio do baralho atualizado `50_ECDIS` está marcado com **🆕**. Onde o texto do baralho novo difere do antigo, os dois ficam visíveis (marcados como "antes" e "agora").

## 1. Explicação simples e intuitiva

Pense no **GPS do carro**, mas muito mais sério: o mapa é uma base de dados inteligente, você aproxima e aparecem mais detalhes, e o aparelho **apita** se você vai em direção a um perigo. O **ECDIS** é isso, aprovado oficialmente para navegar, no lugar da carta de papel.

🆕 Junto com as **ENCs**, o ECDIS é o principal meio de navegação eletrônica nos navios mercantes, e é considerado uma **alternativa às cartas náuticas em papel**.

| Peça | O que é | Analogia |
|---|---|---|
| **ECDIS** | O sistema (tela + software + sensores) | O **GPS do carro** |
| **ENC** | A carta eletrônica oficial (banco de dados) que roda no ECDIS | O **mapa oficial** carregado |
| **S-57** | O formato/padrão em que a ENC é escrita | O **idioma oficial** (como o PDF) |
| **RENC** | Centro regional que confere cada ENC e a distribui | O **cartório** que carimba e entrega |

**ZoC (Zonas de Confiança)** são a legenda de qualidade do mapa: *"esta área foi levantada com tecnologia precisa; esta outra tem dados antigos e duvidosos"*.

**Na prática:** o ECDIS recebe posição, rumo e velocidade, mostra o navio sobre a carta, sobrepõe radar e AIS e **alarma** quando você se aproxima de perigos. É uma ferramenta, não o comandante.

## 2. O que o conceito representa

- **ECDIS (deck):** Sistema de Informação Geográfica **aprovado para navegação**, conforme IMO/IHO; aceito como **equivalente às cartas de papel** pela **SOLAS V/19**.
  - 🆕 É um **método de navegação eletrônica**, considerado **alternativa às cartas náuticas em papel**.
  - 🆕 **Exibe** informações das ENCs e **integra** dados de **posição, rumo e velocidade**.
  - 🆕 **ECDIS + ENCs** são os principais meios de navegação eletrônica em navios mercantes.
  - 🆕 **Somente ENCs** podem ser usadas dentro do ECDIS para atender ao padrão de desempenho da IMO.
-  🆕 **ENC:* **banco de dados oficial** criado por um **Escritório Hidrográfico Nacional** para uso com um ECDIS.
  - 🆕 É uma representação **digital** de uma área geográfica do mundo real, para fins de navegação marítima.
- **S-57:** o **único** padrão de dados ENC exigido para atender ao requisito de transporte da SOLAS; permite ao ECDIS cumprir os padrões de desempenho da IMO.
-  🆕 RENC = **Centro Regional de Cartas de Navegação Eletrônica**; são organizações sem fins lucrativos de **países produtores de ENCs** que **verificam a conformidade** com os padrões IHO.
- **ZoC:** indicam a **qualidade e a precisão dos dados hidrográficos** de cada área. *(Extra: categorias de A1/A2, as melhores, até C/D, e "U" para não avaliada.)*
- **Vetor:** na ENC os objetos são **vetores**, então posição e tamanho relativo se ajustam à **escala de visualização**. A **RNC** é imagem escaneada (raster), sem essa flexibilidade.
  - 🆕 Os objetos da ENC podem ser representados por imagens **raster** ou, **mais comumente**, por imagens **vetoriais**.
- 🆕 **Profundidades mapeadas:** podem ser usadas em cálculos de **folga sob a quilha**, para garantir que o navio navegue em águas seguras.
- **Sensores que interagem:** posição, rumo, velocidade, radar, AIS, NAVTEX e ecobatímetro → **monitoramento contínuo e alarmes de perigo**.
- **Sobreposição radar/ARPA:** a sobreposição dos **ecos fixos de terra** na carta serve para **confirmar a precisão da posição** e **identificar erros no GPS ou na carta**.
- **Atualizações (SOLAS V/27):** arquivos digitais (Avisos aos Navegantes) por **mídia ou sem fio**, **aplicados automaticamente pelo ECDIS**.

> [!warning] 🆕 Ponto para confirmar com o instrutor
> O card de atualização fala em "ENC/RNC", mas o baralho novo diz que **somente ENCs** podem ser usadas dentro do ECDIS para atender ao padrão de desempenho da IMO. O baralho não define RNC; vale confirmar como tratar isso na prova.

**O que muda quando algo muda?**
- Sensor falha → o ECDIS perde informação ou mostra posição errada.
- Atualização não aplicada → carta desatualizada, risco real.
- Escala muda → o vetor se redimensiona.
- 🆕 Profundidade da carta muda → muda a folga sob a quilha calculada.

## 3. Como identificar o tipo de questão

| Pista no enunciado | Aponta para |
|---|---|
| "equivalente à carta de papel", "SOLAS V/19", "sistema aprovado" | **ECDIS** |
| 🆕 "alternativa às cartas em papel", "método de navegação eletrônica", "exibe e integra posição, rumo e velocidade" | **ECDIS** |
| "banco de dados padronizado", "emitido sob autoridade de serviço hidrográfico" | **ENC** |
| 🆕 "banco de dados oficial", "Escritório Hidrográfico Nacional", "representação digital" | **ENC** |
| "único padrão", "requisitos de transporte da SOLAS" | **S-57** |
| "sem fins lucrativos", "validam e distribuem", "revendedores" | **RENC** |
| 🆕 "Centro Regional de Cartas de Navegação Eletrônica", "países produtores de ENCs" | **RENC** |
| "qualidade/precisão dos dados hidrográficos" | **ZoC** |
| "ecos fixos de terra", "erro do GPS ou da carta" | **Sobreposição radar/ECDIS** |
| "atualização", "Avisos aos Navegantes", "automaticamente" | **Atualização de ENC** |
| "único meio de navegação", "falha" | **Limitações do ECDIS** |
| 🆕 "folga sob a quilha", "águas seguras", "profundidades mapeadas" | **Profundidades da carta** |
| 🆕 "raster", "mais comumente vetoriais" | **Representação dos objetos da ENC** |

**Padrões típicos:** lacuna "distribuídas por meio dos ___" (RENCs) · V/F de atualização ("aplicação pelo usuário" = falso) · V/F do piloto automático ("elimina monitoramento" = falso) · "dois motivos para não ser único meio".
🆕 O baralho novo é dominado por **lacunas**: "O ___ e as ___ são os principais meios...", "Somente ___ podem ser usados dentro do ECDIS", "Os centros regionais... são chamados de ___", "O ___ é alternativa às ___".

**Diferenciar:** ECDIS (sistema) vs ENC (dados) · ENC vs S-57 (carta vs formato) · RENC (valida/distribui) vs Serviço Hidrográfico (emite) · ENC (vetor) vs RNC (imagem).
🆕 Escritório Hidrográfico Nacional **cria** a ENC · RENC **verifica a conformidade** com a IHO.

## 4. Macetes, bizus e atalhos

> [!tip] Bizus
> - **Vida de uma ENC:** Serviço Hidrográfico **produz** → RENC **valida e distribui** → revendedor **vende** → você **instala** → ECDIS **atualiza sozinho**.
> - **V/19 = carta/equivalência** · **V/27 = atualização**.
> - **S-57 = "o único"**, afirmação **verdadeira** (como o "exclusivamente" dos canais do AIS).
> - **ECDIS nunca anda sozinho. Dois motivos:** falha de equipamento/sensores + erro humano de configuração.
> - 🆕 **Cadeia curta (baralho novo):** Escritório Hidrográfico Nacional **cria** → RENC **verifica** → ECDIS **exibe**.
> - 🆕 **Sensores "P-R-V + R-A-N-E":** **P**osição, **R**umo, **V**elocidade + **R**adar, **A**IS, **N**AVTEX, **E**cobatímetro.
> - 🆕 **Lacunas decoráveis:** ECDIS + ENCs · folga sob a quilha · raster · digital · banco de dados · ENCs · RENC · cartas náuticas em papel.

> [!warning] Pegadinhas
> - "A atualização exige que o usuário **aplique** o arquivo" → **falso**: o ECDIS aplica.
> - "ECDIS + piloto automático dispensa vigilância" → **falso**.
> - Confundir **ZoC** (qualidade) com **RENC** (distribuição).
> - Dizer que o RENC **emite** a ENC.
> - 🆕 Trocar **ENC** (dado) por **ECDIS** (sistema) nas lacunas.
> - 🆕 Trocar "folga sob a quilha" por outro termo: é o cálculo que usa as **profundidades mapeadas**.
> - 🆕 Esquecer que o vetor é "**mais comumente**" usado e que o raster é a alternativa.

**Quando NÃO usar o ECDIS isoladamente:** dúvida sobre sensores, configuração ou qualidade da carta (ZoC ruim). Cruze com radar, ecobatímetro e observação visual.

## 5. Raciocínio inverso

**Diagnóstico por sobreposição radar** *(interpretação; o deck só pede "GPS ou carta")*:
- Ecos de terra **batem** com a costa da carta → posição e carta coerentes.
- Ecos **deslocados em todo o mapa, na mesma direção e distância** → provável erro de **posição** (GPS).
- Ecos **deslocados só num trecho** → provável erro da **carta** ali (possível ZoC ruim).

**Deduzindo a origem:**
- "Quem fiscaliza a conformidade da ENC?" → RENC. "Quem emite?" → Serviço Hidrográfico.
- "Por que o ECDIS substitui o papel?" → conformidade IMO/IHO + SOLAS V/19.
- Carta desatualizada → o que falhou na **cadeia de atualização**?

🆕 **Da pergunta para o ator/peça (baralho novo):**
- "Quem **cria** a ENC?" → **Escritório Hidrográfico Nacional**.
- "Quem **verifica a conformidade** com a IHO?" → **RENC**.
- "O que **exibe** a ENC e integra posição, rumo e velocidade?" → **ECDIS**.
- Lacuna com "águas seguras" e "cálculos" → **folga sob a quilha** (depende das profundidades da carta).
- Lacuna com "alternativa" → par **ECDIS** ↔ **cartas náuticas em papel**.
- Lacuna comparando formas de imagem → **raster** e **vetoriais** ("mais comumente" aponta para o vetor).

## 6. Mapa mental da questão

1. **Sistema, dado ou formato?** (ECDIS · ENC · S-57)
2. **Quem faz o quê?** (emite → Serviço Hidrográfico · valida/distribui → RENC)
3. **Palavra absoluta?** ("único", "elimina", "exclusivamente"): teste contra o que você sabe.
4. **Qualidade ou atualização?** (ZoC ou V/27)
5. 🆕 **É lacuna?** Procure a pista vizinha: "banco de dados", "digital", "raster", "folga sob a quilha", "papel".

"Pode", "necessária", "elimina" e "automaticamente" mudam o sentido da frase. Leia devagar.

## 7. Resolução passo a passo

**Q1. "Por que o ECDIS não deve ser único meio? Dois motivos."**
O ECDIS depende de entradas externas: falhas de equipamento/sensores **e** erros humanos de configuração.

**Q2. "O que são ZoC?"** *Zones of Confidence* → confiança nos **dados hidrográficos** → qualidade e precisão de cada área.

**Q3. (V/F) "O S-57 é o único formato de ENC aceito pela SOLAS."** **Verdadeiro**. Palavra forte não torna falsa a frase; o fato é que decide.

**Q4. (V/F) "Atualização por mídia removível, sendo necessária a aplicação pelo usuário."** Parte 1 correta, parte 2 é a pegadinha → **Falso**: o ECDIS aplica automaticamente.

**Q5. (V/F) "ECDIS + piloto automático elimina a necessidade de monitoramento humano."** **Falso**: alerta, mas o oficial supervisiona.

**Q6. "Utilidade da sobreposição de ecos de terra."** Confirmar a posição e identificar erros no GPS ou na carta: se o eco não cai sobre a costa da carta, alguém está errado.

🆕 **Q7. "O que é o ECDIS?"** Sistema de informação geográfica para navegação, conforme IMO e IHO, usado como método de navegação eletrônica. *Por que assim?* Três pedaços: o que é, a conformidade e o uso.

🆕 **Q8. "O que é uma ENC?" (versão do baralho novo)** Banco de dados **oficial**, criado por um **Escritório Hidrográfico Nacional**, para uso com um **ECDIS**. *Por que assim?* "Oficial" + "quem cria" + "para quê".

🆕 **Q9. "O que são os RENCs e qual a função?" (versão do baralho novo)** Organizações **sem fins lucrativos** de países **produtores de ENCs** que **verificam a conformidade** das ENCs com os padrões **IHO**.

🆕 **Q10. (lacuna) "As profundidades mapeadas podem ser usadas em cálculos de ____ para garantir águas seguras."** **Folga sob a quilha.**

🆕 **Q11. (lacuna) "O ____ é considerado uma alternativa às ____ para navegação."** **ECDIS**; **cartas náuticas em papel.**

🆕 **Q12. "O que o ECDIS exibe e integra?"** **Exibe** informações das ENCs e **integra** dados de **posição, rumo e velocidade**.

🆕 **Q13. (lacunas rápidas)** "O ____ e as ____ são os principais meios de navegação eletrônica" → **ECDIS; ENCs** · "Objetos da ENC por imagens ____ ou, mais comumente, vetoriais" → **raster** · "ENC é uma representação ____ de uma área" → **digital** · "ENC é um ____ oficial" → **banco de dados** · "Somente ____ podem ser usados dentro do ECDIS" → **ENCs** · "Centros regionais são chamados de ____" → **RENC**.

## 8. Como pensar sozinho

1. **Sistema, dado ou formato?**
2. **Quem é o ator?** (Serviço Hidrográfico, RENC, revendedor, usuário, o próprio ECDIS)
3. **O que pode dar errado?** Sensor, humano, atualização, qualidade da carta.
4. 🆕 **Qual é o verbo?** *Criar* (Escritório), *verificar* (RENC), *exibir/integrar* (ECDIS), *exigir* (S-57/SOLAS), *atualizar* (arquivos digitais).

Se a frase tira o ator da jogada ("o usuário aplica") ou promete demais ("elimina vigilância"), desconfie.

## 9. Treinamento de raciocínio

**Fáceis**
- **F1.** Complete: "As ENCs são distribuídas para revendedores por meio dos ___."
- **F2.** Qual o único padrão ENC que atende ao requisito de transporte da SOLAS?
- **F3.** Cite dois sensores que interagem com o ECDIS.

**Médias**
- **M1.** Um colega diz que o RENC *produz* a ENC. Corrija e explique o papel de cada ator.
- **M2.** V/F: "O ECDIS é equivalente ao papel apenas se estiver conectado a todos os sensores." Analise.
- **M3.** Por que a representação **vetorial** é vantagem sobre uma imagem?

**Difíceis**
- **D1.** Ecos de terra todos deslocados 0,3' para leste em relação à carta, inclusive de ilhas distantes. Hipótese mais provável e como confirmar?
- **D2.** A atualização chegou por sem fio, mas a carta ainda mostra um perigo antigo. Liste três pontos da cadeia de atualização para investigar.
- **D3.** Explique por que "ECDIS com piloto automático ligado" não permite relaxar a vigilância (falha de sensor, erro de configuração e uma manobra real).

**🆕 Complemento do baralho novo**
- **F4.** Complete: "Somente ____ podem ser usados dentro do ECDIS para atender ao padrão de desempenho da IMO."
- **M4.** Explique ECDIS × ENC com a analogia do GPS do carro.
- **D4.** Relacione as profundidades mapeadas da ENC com a segurança da navegação: que cálculo alimentam e por que isso depende de a carta estar correta e atualizada?

> [!question] Modo treinador
> Responda por escrito antes de olhar qualquer gabarito.

## 10. Questões com dados escondidos

**Q-A.** Atualização das ENCs chegou em um pen drive. O oficial diz: "Agora tenho que aplicar manualmente cada arquivo." Está certo?
**Q-B.** Área marcada na carta como de baixa qualidade. Que recurso informa isso e por que importa?
**Q-C.** "Qual organização sem fins lucrativos valida de forma independente as ENCs e as distribui?" Que informação não dita elimina "Serviço Hidrográfico"?
**Q-D.** Posição GPS perfeita, mas o eco de uma ponta de terra aparece **dentro** da água na carta. Em que ordem investiga?
🆕 **Q-E.** "Organização sem fins lucrativos, de país produtor de ENCs, que verifica se as ENCs seguem os padrões IHO." Qual a sigla e o nome por extenso?
🆕 **Q-F.** "O ECDIS mostra o navio sobre a carta com posição, rumo e velocidade." De onde vêm esses dados e o que o ECDIS faz com eles?

> [!success]- Gabarito comentado
> - **Q-A:** Não. Mídia ou sem fio entregam o arquivo; a **aplicação é automática**.
> - **Q-B:** **ZoC**: mostra qualidade e precisão da área, logo a margem de segurança necessária.
> - **Q-C:** **RENC**. "Sem fins lucrativos + valida + distribui" afasta o Serviço Hidrográfico, que **emite**.
> - **Q-D:** Erro **geral** (posição) ou **local** (carta/ZoC)? Cruze com ecobatímetro e observação visual; a sobreposição serve exatamente para identificar erros no GPS ou na carta.
> - 🆕 **Q-E:** **RENC** (Centro Regional de Cartas de Navegação Eletrônica).
> - 🆕 **Q-F:** Vêm dos **sensores**; o ECDIS os **integra** às informações das ENCs que **exibe**.

## 11. Erros mais comuns

| Erro | Como evitar |
|---|---|
| Achar que o usuário aplica a atualização | O **ECDIS** aplica |
| ECDIS elimina o monitoramento humano | Alerta, mas o oficial supervisiona |
| Trocar RENC por Serviço Hidrográfico | RENC valida/distribui · Serviço emite |
| "Corrigir" o S-57 como único | O deck diz **verdadeiro** |
| Confundir ENC com ECDIS | ENC = dados · ECDIS = sistema |
| Confundir ZoC com escala | ZoC é qualidade/precisão dos dados |
| Esquecer que sensor errado contamina o ECDIS | Tão bom quanto sensores e configuração |
| Trocar V/19 por V/27 | 19 = equivalência ao papel · 27 = atualização |
| 🆕 Esquecer o nome por extenso do RENC | **Centro Regional de Cartas de Navegação Eletrônica** |
| 🆕 Responder outro termo em "cálculos de ____" | **Folga sob a quilha** |
| 🆕 Trocar "raster" por "vetorial" na lacuna | "Raster" vem antes de "mais comumente vetoriais" |
| 🆕 Esquecer "alternativa às cartas em papel" | ECDIS ↔ cartas náuticas em papel |

## 12. Conexão entre os assuntos

- [[01 AIS v1]]: alimenta o ECDIS com alvos; erro de GNSS do outro navio vira erro na sua tela.
- [[02 VTS LPS VTMIS v1]]: informação em tempo real que você cruza com a carta.
- [[04 GNSS]]: fonte da posição do ECDIS.
- [[05 Posicionamento Dinâmico v1]]: sensores de referência dependem de posicionamento confiável.
- [[06 Publicações Náuticas]]: os **Avisos aos Navegantes** digitais atualizam a ENC.
- Radar/ARPA: a sobreposição de ecos funciona como auditoria do ECDIS.

## 13. Resumo final de memorização rápida

- **ECDIS** = sistema aprovado (IMO/IHO), equivalente ao papel (**SOLAS V/19**). **Não** é único meio: falha de sensor + erro humano.
  - 🆕 Método de **navegação eletrônica**, **alternativa às cartas em papel**; **exibe** ENCs e **integra** posição, rumo e velocidade. **ECDIS + ENCs** = principais meios de navegação eletrônica. **Somente ENCs** atendem ao padrão IMO dentro do ECDIS.
- **ENC** = banco de dados padronizado, emitido sob autoridade de Serviço Hidrográfico. Formato **S-57** (único exigido). Vetorial.
  - 🆕 **Banco de dados oficial** criado por **Escritório Hidrográfico Nacional**; representação **digital**; objetos **raster** ou, mais comumente, **vetoriais**.
  - 🆕 **Profundidades** → cálculo de **folga sob a quilha**.
- **RENC** = sem fins lucrativos, **valida e distribui**. 🆕 **Centro Regional de Cartas de Navegação Eletrônica**; países produtores de ENCs; verifica conformidade IHO.
- **ZoC** = qualidade e precisão dos dados hidrográficos.
- **Sensores:** posição, rumo, velocidade, radar, AIS, NAVTEX, ecobatímetro.
- **Radar sobreposto:** ecos de terra conferem posição e carta.
- **Atualização (V/27):** arquivos digitais, mídia ou sem fio, **aplicados automaticamente**.
- **Piloto automático:** não elimina o monitoramento humano.
- **10 segundos:** *sistema* → ECDIS · *dados/banco* → ENC · *formato único* → S-57 · *valida/distribui* → RENC · *qualidade da área* → ZoC · *atualiza* → automático.

### 🆕 Lacunas do baralho novo (revisão rápida)

| Lacuna | Resposta |
|---|---|
| O ____ e as ____ são os principais meios de navegação eletrônica | ECDIS; ENCs |
| Cálculos de ____ em águas seguras | folga sob a quilha |
| Imagens ____ ou, mais comumente, vetoriais | raster |
| ENC é uma representação ____ de uma área geográfica | digital |
| ENC é um ____ oficial criado por Escritório Hidrográfico Nacional | banco de dados |
| Somente ____ podem ser usados dentro do ECDIS | ENCs |
| Centros regionais de cartas de navegação eletrônica | RENC |
| O ____ é alternativa às ____ | ECDIS; cartas náuticas em papel |

## 14. Modo treinador

> [!question] Responda sem olhar
> 1. Por que o ECDIS "equivalente ao papel" **ainda** exige vigilância humana?
> 2. Se o sensor de posição estiver errado, o que o ECDIS mostra? Como você perceberia o erro usando o radar?
> 3. Em uma frase, a diferença entre **ENC**, **S-57** e **RENC**.
> 4. 🆕 Quem **cria** a ENC e o que o RENC faz com ela, segundo o baralho novo?
