---
title: "Posicionamento Dinâmico (DP)"
topico: 5
disciplina: Navegação
curso: ACON-B
prova: 2
tags: [navegacao, acon-b, prova-2, dp, darps, artemis, fanbeam, cyscan, taut-wire]
aliases: [DP, Dynamic Positioning, DARPS, Artemis, FanBeam, CyScan, Taut Wire]
---

# Tópico 5 — Posicionamento Dinâmico (DP)

Anterior: [[04 GNSS]] · Próximo: [[06 Publicações Náuticas]] · Índice: [[00 Índice Navegação Prova 2]]

> [!note] Aviso
> Tópico mais denso do deck. Cobrança típica: **comparação entre os sistemas de referência**. Itens **extra** não são do deck.

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

**O que muda quando algo muda?**
- Perde o GPS → DARPS fica comprometido; CyScan, FanBeam e Taut Wire seguem.
- Vento muda → o anemômetro avisa o computador, que reage antes da deriva.
- Mar mais agitado → a VRU registra mais movimento do casco; o sistema distingue balanço de deslocamento real.

## 3. Como identificar o tipo de questão

| Pista no enunciado | Aponta para |
|---|---|
| "manter posição e rumo automaticamente", "vento, ondas, correntes" | **DP** |
| "offloading", "posicionamento relativo", "UHF" | **DARPS** |
| "micro-ondas", "10 km", "distância e ângulo" | **Artemis** |
| "laser de curto alcance", "referência primária" | **FanBeam** |
| "alvos retrorrefletivos", "independente do GPS" | **CyScan** |
| "cabo", "peso no fundo", "guincho de tensão constante", "inclinação" | **Taut Wire** |
| "rumo" / "vento" / "arfagem, rolagem, caturro" | **Giro / Anemômetro / VRU** |

**Padrões típicos:** CyScan × Artemis (laser × micro-ondas) · CyScan × ARPA (referência de posição × processamento de alvos de radar) · lacuna "___ e ___ são baseados em laser" (CyScan, FanBeam) · "Explique o Taut Wire" · "Por que o DARPS em offloading?"

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

> [!warning] Pegadinhas
> - Dizer que o CyScan usa **micro-ondas** (é o Artemis).
> - Dizer que o Artemis tem alcance curto: até **10 km**; curto alcance é o FanBeam.
> - Taut Wire mede **ângulo** (e comprimento) do cabo, **não** vento ou velocidade.
> - Confundir **VRU** (balanço) com **giroscópica** (rumo).
> - Dizer que o DP depende de **um único** sistema: depende de um **conjunto**.

**Quando NÃO usar:** detecção de alvos de tráfego não é CyScan (é radar/ARPA).

## 5. Raciocínio inverso (da necessidade para o sistema)

- **"Perdi o satélite. O que me mantém?"** → algo sem GPS: CyScan, FanBeam ou Taut Wire.
- **"Preciso da posição em relação a outra embarcação."** → relativo: DARPS ou Artemis.
- **"Precisão máxima a curta distância, operação crítica."** → FanBeam.
- **"Referência ligada ao fundo."** → Taut Wire.

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

## 8. Como pensar sozinho

1. **O que ele mede?** Distância e ângulo? Alcance e rumo? Ângulo de cabo? Posição por satélite?
2. **Com que "material"?** Laser, micro-ondas, rádio UHF/GPS ou cabo?
3. **Em que situação brilha?** Offloading (DARPS), curto alcance (FanBeam), sem GPS (CyScan), 10 km (Artemis), ligado ao fundo (Taut Wire).

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

> [!question] Modo treinador
> Responda por escrito antes de olhar qualquer gabarito.

## 10. Questões com dados escondidos

**Q-A.** "Um sensor emite feixes de laser que refletem em alvos específicos e mede alcance e rumo. Em que é superior ao DGPS?"
**Q-B.** "Posição de um navio **em relação a outro**, com GPS/GLONASS diferencial e rádio UHF. Que sistema?"
**Q-C.** "Cabo do Taut Wire com 80 m, inclinado 3° da vertical. Quanto o navio derivou?" ($\sin 3° \approx 0{,}052$)
**Q-D.** "Um navio em DP perde o GPS, mas mantém posição por dois sensores, um laser e um cabo. Quais?"

> [!success]- Gabarito comentado
> - **Q-A:** *laser + alvos refletores* → **CyScan**; superior porque **independe do GPS**.
> - **Q-B:** *GPS/GLONASS diferencial + UHF + relativo* → **DARPS**.
> - **Q-C:** $80 \times 0{,}052 \approx 4{,}2\ \text{m}$ (simplificação).
> - **Q-D:** laser (CyScan ou FanBeam) e cabo (**Taut Wire**): nenhum depende do satélite.

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

## 12. Conexão entre os assuntos

- [[04 GNSS]]: DARPS é GNSS diferencial com UHF; o CyScan dá alternativa **independente do GPS**.
- [[03 ECDIS ENC]]: compartilham sensores (posição, rumo); posição errada contamina os dois.
- [[01 AIS v1]]: informa a outros navios a posição e o estado da navegação.
- [[02 VTS LPS VTMIS v1]]: operações de DP perto de porto exigem comunicação com o VTS.
- **Hidrodinâmica** (outra matéria do curso): vento, ondas e correntes são **forças sobre o casco**, a mesma física que o DP compensa.
- Radar/ARPA: aparece na comparação com o CyScan.

O DP é onde **posicionamento (GNSS), sensores (giro, vento, VRU) e física das forças (Hidrodinâmica)** se encontram. Se uma peça falha, outras compensam: **redundância**.

## 13. Resumo final de memorização rápida

- **DP:** mantém **posição e rumo** automaticamente, compensando vento, ondas e correntes; depende de **sistemas de referência de posição**.
- **Composição:** sensores + atuadores (propulsores e leme) + computador central.
- **Sensores:** giro (rumo) · anemômetro (vento) · VRU (arfagem, rolagem, caturro).
- **DARPS:** GPS/GLONASS diferencial + UHF · absoluto e **relativo** · **offloading**.
- **Artemis:** **micro-ondas**, dois transceptores, **distância e ângulo**, até **10 km**.
- **FanBeam:** **laser**, **curto alcance**, **referência primária** em operações críticas.
- **CyScan:** **laser**, alvos retrorrefletivos, **alcance e rumo**, **independe do GPS**.
- **Taut Wire:** cabo + peso no fundo, **guincho de tensão constante**, sensores de **inclinação**.
- **10 segundos:** *offloading* → DARPS · *10 km* → Artemis · *curto alcance* → FanBeam · *retrorrefletivo/sem GPS* → CyScan · *cabo e peso no fundo* → Taut Wire.

## 14. Modo treinador

> [!question] Responda sem olhar
> 1. Por que o CyScan é importante para o DP quando o GPS falha? Uma frase.
> 2. Diferença entre **CyScan** e **ARPA**. Competem?
> 3. Num offloading, por que o DP precisa da posição **relativa** entre as duas embarcações, e não só da absoluta?
