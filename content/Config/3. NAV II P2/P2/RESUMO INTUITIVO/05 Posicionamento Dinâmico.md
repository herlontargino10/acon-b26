---
title: "Posicionamento Dinâmico (DP)"
topico: 5
disciplina: Navegação
curso: ACON-B
prova: 2
fonte: "navegação_prova_2.txt + ACON-B__NAV II 2° Prova__53_Posicionamento Dinâmico.txt"
atualizado: 2026-10-02
tags: [navegacao, acon-b, prova-2, dp, darps, artemis, fanbeam, cyscan, taut-wire]
aliases: [DP, Dynamic Positioning, DARPS, Artemis, FanBeam, CyScan, Taut Wire]
---

# Tópico 5 — Posicionamento Dinâmico (DP)

Anterior: [[04 GNSS]] · Próximo: [[06 Publicações Náuticas]] · Índice: [[00 Índice Navegação Prova 2]]

> [!note] Como ler esta versão
> Todo o conteúdo anterior foi **mantido**. O que veio do baralho atualizado `53_Posicionamento Dinâmico` está marcado com **🆕**. Itens **extra** continuam sendo os que não são do deck.

> [!info] 🆕 O que mudou no baralho
> Este baralho **cresceu**: ganhou cards novos sobre componentes, características e funcionamento do **DARPS**, aplicações e vantagens do **Artemis**, vantagens e aplicações do **CyScan**, e aplicações, vantagens e limitações do **Taut Wire**. Pequenas mudanças de texto: a definição do DP agora diz só "mantém a posição" (antes: "posição e rumo") e o DARPS agora é "posicionamento seguro e preciso entre navios". **Não aparecem mais no baralho novo** (mantidos nesta nota): o card "Por que o CyScan se diferencia do Artemis?", o card "CyScan × ARPA", a lacuna "___ e ___ são sistemas baseados em laser" (CyScan, FanBeam), a lacuna do DP ("depende de um conjunto de ___"), o card "Por que o DARPS em offloading?" e o card do Taut Wire "mede o ângulo e o comprimento do cabo".

## 1. Explicação simples e intuitiva

Imagine ficar **parado num ponto exato** do mar, sem âncora, com vento, onda e correnteza empurrando. Um navio comum derivaria; um navio com **DP** não.

> [!tip] Analogia
> É um **piloto automático de drone**: o computador corrige o tempo todo (*o vento empurrou para a direita, aplico motor para a esquerda*). O DP faz isso com **propulsores e leme**.

O DP precisa de três coisas:
1. **Saber onde está** → sistemas de referência de posição.
2. **Saber o que está empurrando** → sensores (vento, movimentos do casco, rumo).
3. **Reagir** → computador central + propulsores e leme.

**Na prática:** navios **offshore** (plataformas, apoio, offloading), onde ancorar é impossível ou arriscado.

**Fixação:** DP = **olhos** (referências) + **sentidos** (sensores) + **cérebro** (computador) + **músculos** (propulsores).

## 2. O que o conceito representa

**Definição (deck):** mantém **automaticamente a posição e o rumo**, **compensando** vento, ondas e correntes. Depende de um conjunto de **sistemas de referência de posição**.
🆕 *Texto do baralho novo:* sistema que **mantém a posição** da embarcação, composto por **sensores de referência, atuadores (propulsores e leme) e computador central**.

**Composição:** sensores de referência + atuadores (propulsores e leme) + computador central.

### Sensores básicos de entrada

| Sensor | Mede | Pense assim |
|---|---|---|
| **Giroscópica** | **Rumo** | A bússola do sistema |
| **Anemômetro** | **Vento** | De onde vem o empurrão |
| **VRU** | **Arfagem, rolagem e caturro** | Sente o "balanço" do casco |

### Sistemas de referência de posição

| Sistema | Tecnologia | Como funciona (deck) | Característica-chave |
|---|---|---|---|
| **DARPS** | **GPS/GLONASS diferencial + rádio UHF** | Posicionamento absoluto e **relativo** de alta precisão | **Offloading** |
| **Artemis** | **Micro-ondas** | Dois transceptores medem **distância e ângulo relativo** | Alcance até **10 km** |
| **FanBeam** | **Laser** | Sensor de curto alcance | **Referência primária** em operações críticas |
| **CyScan** | **Laser** | Feixes refletem em **alvos retrorrefletivos**: **alcance e rumo** | **Independe do GPS** |
| **Taut Wire** | **Mecânico** (cabo tensionado) | Guincho de tensão constante mantém cabo ligado a um **peso no fundo**; sensores de **inclinação** medem o ângulo e enviam a posição | Referência ligada ao **fundo** |

Famílias úteis: **laser** (CyScan, FanBeam) · **rádio** (DARPS, Artemis) · **mecânico** (Taut Wire).

### 🆕 DARPS em detalhe (baralho novo)

- **Projetado para** operações de carregamento, como a atracação de **navios aliviadores (shuttle tankers)** ao lado de plataformas **FPSO/FSU**, com posição **absoluta e relativa** de precisão **centimétrica**.
- **Componentes de referência:** **GPS/GLONASS de alta performance, rádio UHF, unidade de processamento e HMI**.
- **Características:** posicionamento **relativo e absoluto** de alta precisão · **integração com DP** · tecnologia **TDMA** · operação em **curtas e longas distâncias**.
- **Como funciona:** **relativo**, calculando **distância e marcação** entre embarcações com alta precisão; **absoluto**, por **correções diferenciais (DGPS)**.
- Texto do baralho novo para o resumo: sistema que combina GPS/GLONASS diferencial e rádio UHF para posicionamento **seguro e preciso entre navios**.

### 🆕 Aplicações, vantagens e limitações (baralho novo)

| Sistema | Aplicações | Vantagens | Limitações |
|---|---|---|---|
| **Artemis** | Transferência de óleo (**offloading**), **navios-sonda**, **FPSOs** e **plataformas fixas** | **Alta precisão**, **resistência a interferências ambientais**, **confiabilidade em operações simultâneas** | *(não citadas no baralho)* |
| **CyScan** | **Navios de apoio**, **plataformas de petróleo**, **navios de construção** e **parques eólicos**, especialmente quando o **GPS não é confiável** | **Não depende do GPS** · **funciona bem em baixa visibilidade** · **compatível com a maioria dos sistemas de controle DP** | *(não citadas no baralho)* |
| **Taut Wire** | **Navios DP**, **embarcações de construção e mergulho**, em lâminas d'água de **até 400–500 m ou mais** | **Alta precisão** · **resistência a ruídos acústicos e interferências ambientais** · **calibração simples** | **Alcance limitado pela profundidade da água e pela geometria da embarcação** · **necessidade de fornecimento contínuo de energia** |

**O que muda quando algo muda?**
- Perde o GPS → DARPS fica comprometido; CyScan, FanBeam e Taut Wire seguem.
- Vento muda → o anemômetro avisa o computador, que reage antes da deriva.
- Mar mais agitado → a VRU registra mais movimento do casco; o sistema distingue balanço de deslocamento real.
- 🆕 Visibilidade cai → o CyScan segue funcionando bem (vantagem do baralho).
- 🆕 Água muito funda ou geometria desfavorável → o Taut Wire perde alcance. Falta energia → o Taut Wire para (necessita fornecimento contínuo).

## 3. Como identificar o tipo de questão

| Pista no enunciado | Aponta para |
|---|---|
| "manter posição e rumo automaticamente", "vento, ondas, correntes" | **DP** |
| "offloading", "posicionamento relativo", "UHF" | **DARPS** |
| 🆕 "shuttle tankers", "FPSO/FSU", "precisão centimétrica", "TDMA", "HMI", "marcação entre embarcações" | **DARPS** |
| "micro-ondas", "10 km", "distância e ângulo" | **Artemis** |
| 🆕 "navios-sonda", "operações simultâneas", "plataformas fixas" | **Artemis** |
| "laser de curto alcance", "referência primária" | **FanBeam** |
| "alvos retrorrefletivos", "independente do GPS" | **CyScan** |
| 🆕 "baixa visibilidade", "parques eólicos", "compatível com a maioria dos sistemas DP" | **CyScan** |
| "cabo", "peso no fundo", "guincho de tensão constante", "inclinação" | **Taut Wire** |
| 🆕 "400–500 m", "calibração simples", "energia contínua", "geometria da embarcação" | **Taut Wire** |
| "rumo" / "vento" / "arfagem, rolagem, caturro" | **Giro / Anemômetro / VRU** |

**Padrões típicos:** CyScan × Artemis (laser × micro-ondas) · CyScan × ARPA (referência de posição × processamento de alvos de radar) · lacuna "___ e ___ são baseados em laser" (CyScan, FanBeam) · "Explique o Taut Wire" · "Por que o DARPS em offloading?"
🆕 O baralho novo traz perguntas de **aplicações, vantagens e limitações** de cada sistema e a lacuna "O sistema de posicionamento por micro-ondas para medição precisa de distância e direção entre embarcações é o ____" (**Artemis**).

**Diferenciar:**
- **CyScan vs FanBeam:** ambos laser; CyScan: alcance e rumo, **sem GPS**; FanBeam: **curto alcance**, referência primária.
- **CyScan vs Artemis:** laser vs micro-ondas.
- **CyScan vs ARPA:** referência de posição do DP vs rastreamento de alvos do radar.
- **Artemis vs DARPS:** distância e ângulo entre transceptores vs DGPS + UHF.

## 4. Macetes, bizus e atalhos

> [!tip] Bizus
> - **Laser** → **C**yScan e **F**anBeam ("**L**ápis **C**om **F**ita").
> - **Micro-ondas** → **A**rtemis · **U**HF + GPS → **D**ARPS (D de Diferencial) · **Cabo** → **T**aut Wire.
> - **Palavra → sistema:** offloading → DARPS · 10 km → Artemis · retrorrefletivo → CyScan · peso no fundo → Taut Wire · curto alcance + primária → FanBeam.
> - **Sensores "G-A-V":** **G**iro (rumo) · **A**nemômetro (vento) · **V**RU (arfagem, rolagem, caturro).
> - 🆕 **Vantagens do CyScan "N-B-C":** **N**ão depende do GPS · **B**aixa visibilidade (funciona bem) · **C**ompatível com os sistemas DP.
> - 🆕 **Componentes do DARPS "G-U-P-H":** **G**PS/GLONASS · **U**HF · **P**rocessamento · **H**MI.
> - 🆕 **Características do DARPS:** relativo + absoluto · integra com DP · **TDMA** · curta e longa distância.
> - 🆕 **Taut Wire, limitações "P-E":** **P**rofundidade/geometria limitam o alcance · **E**nergia contínua.
> - 🆕 **Quem faz offloading:** DARPS (shuttle tankers com FPSO/FSU) e também Artemis (transferência de óleo).

> [!warning] Pegadinhas
> - Dizer que o CyScan usa **micro-ondas** (é o Artemis).
> - Dizer que o Artemis tem alcance curto: até **10 km**; curto alcance é o FanBeam.
> - Taut Wire mede **ângulo** (e comprimento) do cabo, **não** vento ou velocidade.
> - Confundir **VRU** (balanço) com **giroscópica** (rumo).
> - Dizer que o DP depende de **um único** sistema: depende de um **conjunto**.
> - 🆕 Atribuir ao **Taut Wire** a vantagem de "independente do GPS" ou "baixa visibilidade": essas são do **CyScan** no baralho.
> - 🆕 Esquecer que o Taut Wire tem **limitações** (profundidade, geometria, energia contínua) e tratá-lo como solução universal.
> - 🆕 Achar que offloading é exclusivo do DARPS: o baralho cita **offloading** também nas aplicações do **Artemis**.

**Quando NÃO usar:** detecção de alvos de tráfego não é CyScan (é radar/ARPA).

## 5. Raciocínio inverso (da necessidade para o sistema)

- **"Perdi o satélite. O que me mantém?"** → algo sem GPS: CyScan, FanBeam ou Taut Wire.
- **"Preciso da posição em relação a outra embarcação."** → relativo: DARPS ou Artemis.
- **"Precisão máxima a curta distância, operação crítica."** → FanBeam.
- **"Referência ligada ao fundo."** → Taut Wire.

🆕 **Do baralho novo:**
- "GPS ruim **e** visibilidade baixa" → **CyScan** (não depende do GPS e funciona bem em baixa visibilidade).
- "Precisão **centimétrica** na atracação de navio aliviador a FPSO/FSU" → **DARPS**.
- "Ruído acústico e interferência ambiental atrapalham; quero calibração simples" → **Taut Wire**.
- "Profundidade muito grande, posso usar Taut Wire?" → o **alcance é limitado pela profundidade da água e pela geometria da embarcação** (o baralho cita 400–500 m ou mais como aplicação).
- "Falta de energia a bordo" → o Taut Wire exige **fornecimento contínuo de energia**.
- "Quais componentes tem o DARPS?" → GPS/GLONASS de alta performance, UHF, unidade de processamento, HMI.
- "Como o DARPS acha a posição **absoluta**?" → por **correções diferenciais (DGPS)**; **relativa** → distância e marcação entre embarcações.

**Quantitativo (extra, simplificado):** Taut Wire com cabo de comprimento $L$ e ângulo $\theta$ em relação à vertical:

$$\text{deslocamento} \approx L \cdot \sin\theta$$

| Variável | Significado prático |
|---|---|
| $L$ | comprimento do cabo (≈ profundidade, se vertical) |
| $\theta$ | inclinação do cabo (quanto o navio saiu de cima do peso) |
| deslocamento | quanto o navio se afastou |

Invertendo: $\theta = \arcsin(\text{desloc}/L)$ e $L = \text{desloc}/\sin\theta$. Maior ângulo, mais deriva.

**CyScan/Artemis:** se mede distância $d$ e ângulo $\theta$, a posição relativa decompõe em $d\cos\theta$ e $d\sin\theta$.

Pergunte qual grandeza o sensor **realmente mede** (ângulo, distância, tempo) e transforme em posição.

## 6. Mapa mental da questão

1. **Qual o problema?** Manter posição? Posição relativa? Falta de GPS?
2. **Que tecnologia aparece?** Laser, micro-ondas, UHF/GPS ou cabo?
3. **Alcance e uso:** curto, 10 km, offloading, operação crítica?
4. **Sensor de entrada ou referência de posição?** (Giro/anemômetro/VRU **vs** DARPS/Artemis/FanBeam/CyScan/Taut Wire)
5. 🆕 **A pergunta é de aplicação, vantagem ou limitação?** Consulte a tabela de aplicações/vantagens/limitações da seção 2.

Nomes comerciais parecidos distraem; tecnologia e uso decidem.

## 7. Resolução passo a passo

**Q1. "O que é e como é composto o DP?"**
Função: manter posição e rumo automaticamente. Composição: sensores + atuadores (propulsores e leme) + computador central: precisa **sentir, decidir e agir**.

**Q2. "Por que o CyScan se diferencia do Artemis?"** Tecnologia: CyScan = **laser** (alcance e rumo); Artemis = **micro-ondas** (distância e ângulo).

**Q3. "O CyScan se diferencia do ARPA por quê?"** CyScan = referência de posição baseada em laser; ARPA = processamento e rastreamento automático de alvos do radar. Não competem.

**Q4. "Funcionamento do Taut Wire."**
1. Peso no fundo + cabo ligado ao navio.
2. **Guincho de tensão constante** mantém o cabo esticado (uma "régua reta").
3. **Sensores de inclinação** medem o ângulo (e comprimento).
4. Dados vão ao DP, que calcula a posição.

**Q5. "Por que o DARPS em offloading?"** Offloading exige saber a **posição relativa** entre embarcações com alta precisão; DARPS = DGPS + UHF.

**Q6. "Sensores básicos de entrada."** Rumo → giroscópica · vento → anemômetro · arfagem/rolagem/caturro → VRU.

🆕 **Q7. "Qual sistema é projetado para operações de carregamento, como atracação de shuttle tankers ao lado de FPSO/FSU, com posição absoluta e relativa de precisão centimétrica?"** **DARPS.**

🆕 **Q8. "Principais componentes de referência do DARPS."** GPS/GLONASS de alta performance, rádio UHF, unidade de processamento e HMI.

🆕 **Q9. "Características do DARPS."** Posicionamento relativo e absoluto de alta precisão; integração com DP; tecnologia TDMA; operação em curtas e longas distâncias.

🆕 **Q10. "Como funciona o DARPS?"** Relativo: calcula **distância e marcação** entre embarcações com alta precisão. Absoluto: por **correções diferenciais (DGPS)**.

🆕 **Q11. (lacuna) "O sistema de posicionamento dinâmico por micro-ondas para medição de distância e direção entre embarcações é o ____."** **Artemis.**

🆕 **Q12. "Aplicações e vantagens do Artemis."** Aplicações: offloading, navios-sonda, FPSOs e plataformas fixas. Vantagens: alta precisão, resistência a interferências ambientais e confiabilidade em operações simultâneas.

🆕 **Q13. "Três vantagens do CyScan."** Não depende do GPS · funciona bem em baixa visibilidade · compatível com a maioria dos sistemas de controle DP.

🆕 **Q14. "Aplicações do CyScan."** Navios de apoio, plataformas de petróleo, navios de construção e parques eólicos, especialmente quando o GPS não é confiável.

🆕 **Q15. "Aplicações, vantagens e limitações do Taut Wire."** Aplicações: navios DP, embarcações de construção e mergulho, lâminas d'água de até 400–500 m ou mais. Vantagens: alta precisão; resistência a ruídos acústicos e interferências ambientais; calibração simples. Limitações: alcance limitado pela profundidade da água e pela geometria da embarcação; necessidade de fornecimento contínuo de energia.

## 8. Como pensar sozinho

1. **O que ele mede?** Distância e ângulo? Alcance e rumo? Ângulo de cabo? Posição por satélite?
2. **Com que "material"?** Laser, micro-ondas, rádio UHF/GPS ou cabo?
3. **Em que situação brilha?** Offloading (DARPS), curto alcance (FanBeam), sem GPS (CyScan), 10 km (Artemis), ligado ao fundo (Taut Wire).
4. 🆕 **Onde ele falha?** Taut Wire: profundidade, geometria, energia. DARPS: depende de GPS/GLONASS. CyScan: depende de alvos retrorrefletivos. Artemis: alcance até 10 km. *(Só as limitações do Taut Wire são citadas no baralho; as demais são dedução a partir de como cada sistema funciona.)*

## 9. Treinamento de raciocínio

**Fáceis**
- **F1.** Complete: "O ___ e o ___ são sistemas de referência baseados em tecnologia laser."
- **F2.** Qual sensor mede arfagem, rolagem e caturro?
- **F3.** Qual sistema de referência tem alcance de até 10 km?

**Médias**
- **M1.** O GPS foi interrompido. Cite dois sistemas que continuam funcionando e justifique.
- **M2.** Por que o guincho do Taut Wire precisa de **tensão constante**?
- **M3.** Navio e FPSO fazem offloading. Qual sistema e por quê? O que seria insuficiente?

**Difíceis**
- **D1.** Taut Wire com cabo de 100 m a 5° da vertical. Estime o deslocamento horizontal e o que o DP faz. ($\sin 5° \approx 0{,}087$)
- **D2.** Um colega propõe só GPS diferencial "por ser o mais preciso". Argumente por que o DP depende de um **conjunto**.
- **D3.** Compare CyScan e FanBeam: o que têm em comum, o que diferencia e quando escolher cada um?

**🆕 Complemento do baralho novo**
- **F4.** Cite os quatro componentes de referência do DARPS.
- **F5.** Cite as três vantagens do CyScan.
- **M4.** Uma operação de offloading ocorre com baixa visibilidade e GPS pouco confiável. Qual sistema de referência escolher e por quê? Cite duas vantagens do baralho.
- **M5.** Diferencie as aplicações do Artemis e as do CyScan, usando dois exemplos de cada.
- **D4.** Um navio de construção opera em lâmina d'água de 450 m. O Taut Wire serve? Use aplicações, limitações e a ideia de geometria da embarcação.
- **D5.** Explique como o DARPS obtém, ao mesmo tempo, posição **absoluta** e **relativa**.

> [!question] Modo treinador
> Responda por escrito antes de olhar qualquer gabarito.

## 10. Questões com dados escondidos

**Q-A.** "Um sensor emite feixes de laser que refletem em alvos específicos e mede alcance e rumo. Em que é superior ao DGPS?"
**Q-B.** "Posição de um navio **em relação a outro**, com GPS/GLONASS diferencial e rádio UHF. Que sistema?"
**Q-C.** "Cabo do Taut Wire com 80 m, inclinado 3° da vertical. Quanto o navio derivou?" ($\sin 3° \approx 0{,}052$)
**Q-D.** "Um navio em DP perde o GPS, mas mantém posição por dois sensores, um laser e um cabo. Quais?"
🆕 **Q-E.** "Parque eólico, GPS pouco confiável, neblina. Qual sistema de referência o baralho indica?"
🆕 **Q-F.** "Um sistema que usa tecnologia TDMA e integra-se ao DP, com GPS/GLONASS, UHF, unidade de processamento e HMI." Qual?
🆕 **Q-G.** "Sistema que mantém um cabo ligado a um peso no fundo, mas que pode perder alcance em águas muito fundas e precisa de energia contínua." Qual, e qual dessas duas informações vem do baralho como limitação?

> [!success]- Gabarito comentado
> - **Q-A:** *laser + alvos refletores* → **CyScan**; superior porque **independe do GPS**.
> - **Q-B:** *GPS/GLONASS diferencial + UHF + relativo* → **DARPS**.
> - **Q-C:** $80 \times 0{,}052 \approx 4{,}2\ \text{m}$ (simplificação).
> - **Q-D:** laser (CyScan ou FanBeam) e cabo (**Taut Wire**): nenhum depende do satélite.
> - 🆕 **Q-E:** **CyScan**: parques eólicos aparecem nas aplicações, "especialmente quando o GPS não é confiável", e ele funciona bem em baixa visibilidade.
> - 🆕 **Q-F:** **DARPS** (TDMA, integração com DP e os quatro componentes).
> - 🆕 **Q-G:** **Taut Wire**. As **duas** informações aparecem nas limitações do baralho: alcance limitado pela **profundidade da água e geometria da embarcação**, e **fornecimento contínuo de energia**.

## 11. Erros mais comuns

| Erro | Como evitar |
|---|---|
| Laser × micro-ondas (CyScan × Artemis) | CyScan = laser · Artemis = micro-ondas |
| Esquecer que o CyScan independe do GPS | É a sua principal vantagem |
| Artemis de curto alcance | Artemis: **até 10 km** · FanBeam: curto alcance |
| Confundir CyScan com ARPA | Referência de posição × rastreamento de alvos |
| Trocar VRU e giroscópica | VRU = movimentos do casco · Giro = rumo |
| Taut Wire mede vento/velocidade | Mede **ângulo** (e comprimento) do cabo |
| DP depende de um só sensor | Depende de um **conjunto** de referências |
| Esquecer o "relativo" do DARPS | Dá posição **absoluta e relativa** |
| 🆕 Trocar as vantagens de CyScan, Artemis e Taut Wire | CyScan: sem GPS, baixa visibilidade, compatível com DP · Artemis: precisão, resistência a interferências, operações simultâneas · Taut Wire: precisão, resistência a ruído acústico, calibração simples |
| 🆕 Esquecer as limitações do Taut Wire | Profundidade/geometria e energia contínua |
| 🆕 Esquecer os componentes do DARPS | GPS/GLONASS, UHF, processamento, HMI |
| 🆕 Confundir "absoluto" e "relativo" no DARPS | Absoluto = DGPS · relativo = distância e marcação entre embarcações |

## 12. Conexão entre os assuntos

- [[04 GNSS]]: DARPS é GNSS diferencial com UHF; o CyScan dá alternativa **independente do GPS**.
- [[03 ECDIS ENC]]: compartilham sensores (posição, rumo); posição errada contamina os dois.
- [[01 AIS]]: informa a outros navios a posição e o estado da navegação.
- [[02 VTS LPS VTMIS]]: operações de DP perto de porto exigem comunicação com o VTS.
- **Hidrodinâmica** (outra matéria do curso): vento, ondas e correntes são **forças sobre o casco**, a mesma física que o DP compensa.
- Radar/ARPA: aparece na comparação com o CyScan.

O DP é onde **posicionamento (GNSS), sensores (giro, vento, VRU) e física das forças (Hidrodinâmica)** se encontram. Se uma peça falha, outras compensam: **redundância**.

## 13. Resumo final de memorização rápida

- **DP:** mantém **posição e rumo** automaticamente, compensando vento, ondas e correntes; depende de **sistemas de referência de posição**. 🆕 Composto por sensores de referência, atuadores (propulsores e leme) e computador central.
- **Composição:** sensores + atuadores (propulsores e leme) + computador central.
- **Sensores:** giro (rumo) · anemômetro (vento) · VRU (arfagem, rolagem, caturro).
- **DARPS:** GPS/GLONASS diferencial + UHF · absoluto e **relativo** · **offloading**. 🆕 Shuttle tankers + FPSO/FSU, precisão centimétrica; componentes: GPS/GLONASS, UHF, processamento, HMI; TDMA; integra com DP.
- **Artemis:** **micro-ondas**, dois transceptores, **distância e ângulo**, até **10 km**. 🆕 Offloading, navios-sonda, FPSOs, plataformas fixas; alta precisão, resistência a interferências, operações simultâneas.
- **FanBeam:** **laser**, **curto alcance**, **referência primária** em operações críticas.
- **CyScan:** **laser**, alvos retrorrefletivos, **alcance e rumo**, **independe do GPS**. 🆕 Baixa visibilidade; compatível com DP; navios de apoio, plataformas, construção, parques eólicos.
- **Taut Wire:** cabo + peso no fundo, **guincho de tensão constante**, sensores de **inclinação**. 🆕 400–500 m ou mais; alta precisão, resistência a ruído acústico, calibração simples; limitações: profundidade/geometria e energia contínua.
- **10 segundos:** *offloading* → DARPS · *10 km* → Artemis · *curto alcance* → FanBeam · *retrorrefletivo/sem GPS* → CyScan · *cabo e peso no fundo* → Taut Wire.

### 🆕 Perguntas do baralho novo (revisão rápida)

| Pergunta | Resposta |
|---|---|
| O que é e como é composto o DP? | Mantém a posição; sensores de referência + atuadores (propulsores e leme) + computador central |
| Sensores de entrada básicos | Giroscópica (rumo) · anemômetro (vento) · VRU (arfagem, rolagem, caturro) |
| DARPS (aplicação) | GPS/GLONASS diferencial + UHF; posicionamento seguro e preciso entre navios |
| Artemis | Micro-ondas entre dois transceptores; distância e ângulo relativo; até 10 km |
| FanBeam | Laser de curto alcance; referência primária em operações críticas |
| CyScan | Feixes de laser em alvos retrorrefletivos; alcance e rumo |
| Taut Wire | Guincho de tensão constante + cabo + peso no fundo; sensores de inclinação |
| Qual sistema para shuttle tankers ao lado de FPSO/FSU, precisão centimétrica? | DARPS |
| Componentes do DARPS | GPS/GLONASS de alta performance, UHF, unidade de processamento, HMI |
| Características do DARPS | Relativo e absoluto de alta precisão · integração com DP · TDMA · curtas e longas distâncias |
| Funcionamento do DARPS | Relativo: distância e marcação · absoluto: correções diferenciais (DGPS) |
| Sistema por micro-ondas para distância e direção entre embarcações | Artemis |
| Aplicações do Artemis | Offloading, navios-sonda, FPSOs, plataformas fixas |
| Vantagens do Artemis | Alta precisão, resistência a interferências ambientais, confiabilidade em operações simultâneas |
| 3 vantagens do CyScan | Não depende do GPS · baixa visibilidade · compatível com DP |
| Aplicações do CyScan | Navios de apoio, plataformas, construção, parques eólicos (GPS não confiável) |
| Aplicações do Taut Wire | Navios DP, construção e mergulho, até 400–500 m ou mais |
| Vantagens do Taut Wire | Alta precisão · resistência a ruído acústico e interferências · calibração simples |
| Limitações do Taut Wire | Alcance limitado por profundidade e geometria · energia contínua |

## 14. Modo treinador

> [!question] Responda sem olhar
> 1. Por que o CyScan é importante para o DP quando o GPS falha? Uma frase.
> 2. Diferença entre **CyScan** e **ARPA**. Competem?
> 3. Num offloading, por que o DP precisa da posição **relativa** entre as duas embarcações, e não só da absoluta?
> 4. 🆕 Cite uma vantagem exclusiva de cada um: Artemis, CyScan e Taut Wire, e uma limitação do Taut Wire.
