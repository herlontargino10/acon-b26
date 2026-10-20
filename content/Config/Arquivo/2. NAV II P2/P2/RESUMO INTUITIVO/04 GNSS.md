---
title: "GNSS"
topico: 4
disciplina: Navegação
curso: ACON-B
prova: 2
tags: [navegacao, acon-b, prova-2, gnss, gps, trilateracao]
aliases: [GNSS, GPS, trilateração, DGPS]
---

# Tópico 4 — GNSS

Anterior: [[03 ECDIS ENC]] · Próximo: [[05 Posicionamento Dinâmico v1]] · Índice: [[00 Índice Navegação Prova 2]]

> [!note] Aviso
> O deck tem **só um card** sobre GNSS (princípio de funcionamento), além de menções no DARPS (GPS/GLONASS diferencial). O que está marcado como **extra** não é do deck.

## 1. Explicação simples e intuitiva

**GNSS** (*Global Navigation Satellite System*) é o nome genérico dos sistemas de navegação por satélite. O GPS americano é o mais conhecido; o deck cita também o GLONASS.

Os satélites funcionam como **faróis no céu**, cada um "gritando" *"estou nesta posição, falando neste exato instante"*. O receptor mede quanto tempo o sinal demorou e calcula a distância até cada satélite.

> [!tip] Analogias
> - Fixar posição com **três distâncias de radar** de pontos conhecidos: cada distância traça um círculo e o navio está onde se cruzam. O GNSS faz o mesmo em 3D, com esferas.
> - Contar os segundos entre relâmpago e trovão: o tempo vira distância.

**Na prática:** a antena GNSS no mastro entrega posição, velocidade e hora ao ECDIS, ao AIS, ao radar, ao DP e a todo o resto. É a **fonte de posição** da maior parte do passadiço.

## 2. O que o conceito representa

**Princípio (deck):** o GNSS determina a posição por **trilateração**. O receptor recebe sinais de **pelo menos quatro satélites**, mede o **tempo de propagação**, calcula as **distâncias** e obtém a **posição tridimensional** e o **tempo exato**.

**A fórmula por trás (extra):**

$$d = c \cdot \Delta t$$

| Símbolo | Significado prático |
|---|---|
| $d$ | distância até o satélite (km) |
| $c$ | velocidade do sinal (a da luz), $\approx 300\,000\ \text{km/s}$ |
| $\Delta t$ | tempo que o sinal levou para chegar (s) |

**Por que quatro satélites, e não três?** Contagem de incógnitas:
- Posição tem **3 incógnitas** (latitude, longitude, altitude) → 3 satélites.
- O relógio do receptor é impreciso; o dos satélites é atômico. O **erro do relógio** é a **4ª incógnita** → 4 satélites.
- Por isso o resultado entrega **posição + tempo exato**.

**Visualização:** 1 satélite → você está numa **esfera**; 2 → num **círculo**; 3 → em **dois pontos** (um absurdo, no espaço); o 4º elimina a dúvida e acerta o relógio.

**O que muda quando algo muda?**
- Mais satélites visíveis → mais redundância.
- Erro de tempo → erro de distância: $1\ \mu s \approx 300\ \text{m}$.
- Menos de 4 satélites → a solução 3D deixa de ser possível.

**Diferencial (extra):** uma estação de referência em posição **conhecida** compara o que o GPS diz com a posição real e transmite a **correção**. No deck: **DARPS** = GPS/GLONASS diferencial + rádio UHF, para posicionamento de alta precisão em offloading ([[05 Posicionamento Dinâmico v1]]).

## 3. Como identificar o tipo de questão

- "**trilateração**" · "tempo de propagação" · "pelo menos **quatro** satélites" · "posição tridimensional e **tempo exato**" → princípio do GNSS.
- "diferencial" · "GPS/GLONASS" · "estação de referência" → DGPS, DARPS.
- "independente do GPS" → sistemas alternativos (CyScan, [[05 Posicionamento Dinâmico v1]]).

**Padrões típicos:** "Explique o princípio do GNSS" (card do deck) · V/F com palavra trocada ("triangulação", "três satélites", "bidimensional") · lacuna "o receptor mede o tempo de ___".

**Diferenciar:**
- **Trilateração vs triangulação:** distâncias vs ângulos. O GNSS é trilateração.
- **GNSS vs GPS:** gênero vs uma constelação.
- **GNSS vs DGPS:** o diferencial adiciona correção de uma estação de referência.

## 4. Macetes, bizus e atalhos

> [!tip] Bizus
> - Frase-resumo: *"Trilateração: 4 satélites, tempo de propagação → distâncias → posição 3D + tempo."*
> - Por que 4? **3 posições + 1 relógio = 4**.
> - Trilateração = distâncias = círculos de radar.

> [!warning] Pegadinhas
> - Trocar **trilateração por triangulação** (a mais provável).
> - "Três satélites bastam": o deck pede **pelo menos quatro**.
> - Dizer que o GNSS mede **ângulos**: ele mede **tempo**.
> - Esquecer o **tempo exato** como produto do cálculo.

**Quando NÃO confiar só no GNSS:** em operações críticas (DP), ele é **um** entre vários sistemas de referência; CyScan e FanBeam funcionam **sem depender do GPS**.

## 5. Raciocínio inverso (isolando variáveis)

$d = c \cdot \Delta t$ reorganizada:

| Quero achar | Fórmula | Pergunta típica |
|---|---|---|
| $d$ | $d = c \cdot \Delta t$ | "O sinal levou 0,07 s. Qual a distância?" |
| $\Delta t$ | $\Delta t = d / c$ | "O satélite está a 21 000 km. Quanto tempo levou?" |
| $c$ | $c = d / \Delta t$ | Raro, mesma conta |

**Quando falta dado:**
- Dá **erro de tempo** e quer **erro de posição**: $d = c \cdot \Delta t$ com $\Delta t$ sendo o erro. 1 µs → ≈ 300 m; 1 ns → ≈ 0,3 m.
- Dá **erro de distância** e quer o de tempo: $\Delta t = d / c$.

**Raciocínio conceitual (extra):** no oceano você já conhece a altitude (≈ nível do mar), o que elimina uma incógnita; mas, pela lógica do deck, a solução 3D completa com tempo exato exige **quatro**.

Conte as **incógnitas**. Cada satélite entrega uma equação.

## 6. Mapa mental da questão

1. **O que a questão pede?** Princípio, número de satélites, tempo/distância ou erro?
2. **Tem conta?** Use $d = c \cdot \Delta t$ e converta unidades (km/s, ms, µs).
3. **Palavra trocada?** (triangulação, três, ângulo)
4. **GNSS puro ou diferencial?** (estação de referência, UHF, DARPS)

Distraem: nomes de constelações e altitude orbital. Em questão de princípio, decide: **trilateração + 4 satélites + tempo**.

## 7. Resolução passo a passo

**Q1. "Explique o princípio de funcionamento do GNSS."** (card do deck)
1. **Método:** trilateração (calcula posição a partir de **distâncias**, não de ângulos).
2. **Entrada:** sinais de **pelo menos 4 satélites** (3 para posição, 1 para o relógio).
3. **Medida:** **tempo de propagação**.
4. **Cálculo:** distâncias até os satélites.
5. **Saída:** **posição 3D** e **tempo exato**.

**Q2 (extra). Sinal levou 0,070 s. Qual a distância?**
$d = 300\,000\ \text{km/s} \times 0{,}070\ \text{s} = 21\,000\ \text{km}$. Confere: satélites GPS orbitam a cerca de 20 000 km.

**Q3 (extra). Relógio do receptor adianta 2 µs. Erro de distância?**
$d = 300\,000\ \text{km/s} \times 2\times10^{-6}\ \text{s} = 0{,}6\ \text{km} = 600\ \text{m}$. Um erro minúsculo de tempo vira centenas de metros: por isso o quarto satélite.

**Q4. (V/F) "O GNSS determina a posição por triangulação com três satélites."**
**Falso**: é **trilateração**, com **pelo menos quatro**. Dois erros na mesma frase.

## 8. Como pensar sozinho

1. **O que o satélite me entrega?** Um **tempo**. Nada de ângulo.
2. **O que faço com ele?** Converto em **distância** ($d = c \cdot \Delta t$).
3. **Quantas distâncias preciso?** Quantas **incógnitas**: posição (3) + relógio (1) = 4.

## 9. Treinamento de raciocínio

**Fáceis**
- **F1.** Complete: "O GNSS determina a posição por ___, recebendo sinais de pelo menos ___ satélites."
- **F2.** O que o receptor mede para calcular a distância até cada satélite?
- **F3.** V/F: "O GNSS fornece, além da posição, o tempo exato." Justifique.

**Médias**
- **M1.** Por que o quarto satélite não é "só um reforço"? Explique em incógnitas.
- **M2.** Um sinal leva 0,075 s. Calcule a distância em km ($c = 300\,000$ km/s).
- **M3.** Diferencie trilateração de triangulação com um exemplo do passadiço (marcações × distâncias de radar).

**Difíceis**
- **D1.** Erro de relógio de 1 µs desloca o navio 300 m. Por que o erro aparece em **distância** e não em ângulo?
- **D2.** Em DP, o GNSS cai por interferência. Que tipo de referência continua funcionando e por quê? (pense no CyScan)
- **D3.** Como uma estação diferencial melhora a posição? Em que operação do deck isso é usado?

> [!question] Modo treinador
> Responda por escrito antes de olhar qualquer gabarito.

## 10. Questões com dados escondidos

**Q-A.** O sinal de um satélite chegou 0,068 s depois de enviado. "A que distância ele está?" (a velocidade do sinal não foi dada)
**Q-B.** Um receptor só capta 3 satélites. Consegue posição 3D com tempo exato?
**Q-C.** Um colega diz: "O GNSS descobre a posição medindo os ângulos entre os satélites." Qual o erro conceitual?
**Q-D.** Erro de posição de 150 m causado só por erro de relógio. Qual o erro de tempo aproximado?

> [!success]- Gabarito comentado
> - **Q-A:** dado escondido: velocidade da luz. $d = 300\,000 \times 0{,}068 = 20\,400\ \text{km}$.
> - **Q-B:** **não**: são 4 incógnitas (3 de posição + tempo); com 3 satélites falta uma equação.
> - **Q-C:** descreveu **triangulação**. O GNSS mede **tempo → distância**: **trilateração**.
> - **Q-D:** $\Delta t = d/c = 0{,}150 / 300\,000 = 5\times10^{-7}\ \text{s} = 0{,}5\ \mu s$.

## 11. Erros mais comuns

| Erro | Como evitar |
|---|---|
| Trilateração × triangulação | Trilateração = **distâncias**; triangulação = ângulos |
| "3 satélites bastam" | 3 posições + 1 relógio = **4** |
| Esquecer o "tempo exato" | O GNSS entrega posição **e** tempo |
| Confundir GNSS com GPS | GNSS é o gênero; GPS é uma constelação |
| Errar unidades (µs, ms, km/s) | Converta tudo para s e km (ou m) antes |
| Achar o GNSS infalível | Pode falhar: por isso há referências alternativas |
| Esquecer a estação de referência no diferencial | DGPS/DARPS corrigem com apoio de rádio |

## 12. Conexão entre os assuntos

- [[01 AIS v1]]: a posição transmitida vem do GNSS. Se erra, o erro viaja pelo VHF.
- [[03 ECDIS ENC]]: posiciona seu navio na carta; a sobreposição de ecos de radar **checa** essa posição.
- [[02 VTS LPS VTMIS v1]]: usa posições recebidas via AIS.
- [[05 Posicionamento Dinâmico v1]]: GNSS (inclusive diferencial, no DARPS) é um sistema de referência; CyScan e FanBeam dão independência do GPS.
- [[06 Publicações Náuticas]]: a posição é plotada em cartas mantidas atualizadas pelos Avisos.

O GNSS é a **fonte** de posição de quase tudo no passadiço; por isso nunca é verdade absoluta.

## 13. Resumo final de memorização rápida

- **GNSS** = navegação por satélite. Método: **trilateração**.
- **Receptor:** ≥ **4 satélites** → **tempo de propagação** → **distâncias** → **posição 3D + tempo exato**.
- **Fórmula (extra):** $d = c \cdot \Delta t$ · $c \approx 300\,000$ km/s · 1 µs ≈ 300 m.
- **Por que 4:** 3 de posição + 1 do relógio.
- **Diferencial (GPS/GLONASS + UHF):** **DARPS**, offloading.
- **Pegadinhas:** triangulação, "3 satélites", ângulos.
- **10 segundos:** *tempo de propagação, quatro satélites, trilateração* → GNSS; *independente do GPS* → laser ([[05 Posicionamento Dinâmico v1]]).

## 14. Modo treinador

> [!question] Responda sem olhar
> 1. Por que três satélites não bastam pela lógica do deck? Conte incógnitas.
> 2. Se o relógio do receptor adianta 1 µs, o que acontece com a posição e por quê?
> 3. Um sinal GNSS levou 0,072 s. Qual a distância? Mostre a conta com unidades.
