---
title: "AIS (Automatic Identification System)"
topico: 1
disciplina: Navegação
curso: ACON-B
prova: 2
fonte: "navegação_prova_2.txt + ACON-B__NAV II 2° Prova__51_AIS.txt"
atualizado: 2026-10-02
tags: [navegacao, acon-b, prova-2, ais]
aliases: [AIS, Sistema de Identificação Automática, SOTDMA]
---

# Tópico 1 — AIS

Anterior: [[00 Índice Navegação Prova 2]] · Próximo: [[02 VTS LPS VTMIS v1]]

> [!note] Como ler esta versão
> Todo o conteúdo anterior foi **mantido**. O que veio do baralho atualizado `51_AIS` está marcado com **🆕**.

> [!info] 🆕 O que mudou no baralho
> O baralho `51_AIS` é quase igual ao anterior. **Mudou:** o card de mensagens curtas (agora: alertas de segurança e informações sobre auxílio à navegação) e o card do princípio de funcionamento (texto mais curto). **Não aparecem mais no baralho novo** (mantidos nesta nota): função do SOTDMA, obrigatoriedade IMO (300/500 AB/passageiros), canais 87B/88B, SAT-AIS, "estado da navegação" nos dados dinâmicos, o card que diferencia as três categorias e os V/F de alcance e canais. O SOTDMA ainda aparece como etapa 3 do funcionamento.

## 1. Explicação simples e intuitiva

Imagine que cada navio usa um **crachá eletrônico** e fica falando em voz alta no rádio VHF: *"Sou o navio tal, estou aqui, nesta velocidade, neste rumo, indo para tal porto"*. Todo navio por perto ouve e vê o outro na tela, com nome, vetor e tudo.

**Como não vira bagunça?** Como num grupo de WhatsApp em que todos combinaram turnos: cada um fala no seu "pedacinho" de tempo, sem ninguém mandando. Isso é o **SOTDMA**: os navios dividem o tempo de transmissão **sem estação central**.

**Na prática:** o alvo AIS aparece como triângulo com vetor, no radar ou no ECDIS. Você clica e vê nome, MMSI, destino, ETA.

> [!tip] Analogia
> - **Radar** = lanterna no escuro: só vê o que a luz bate.
> - **AIS** = todo mundo com um letreiro luminoso: você lê o nome, mesmo atrás de uma ilha. Mas quem não liga o letreiro (ou não tem) fica invisível para ele.
>
> Por isso o AIS **complementa** o radar e **não substitui** nada.

🆕 No baralho, o AIS é definido como um **sistema de auxílio à navegação**, e o radar ganha dele uma **camada adicional de segurança e consciência situacional**.

## 2. O que o conceito representa

**Para que serve:** aumentar a segurança marítima, prevenindo colisões e auxiliando o monitoramento do tráfego. Também ajuda a gestão portuária e a busca e salvamento.

**Princípio:** posicionamento (GNSS) + comunicação sem fio (VHF). 🆕 Texto do baralho novo: baseia-se na **integração de tecnologias de posicionamento e comunicação sem fio**. 🆕 Definição do baralho: **sistema de auxílio à navegação** que permite às embarcações trocar automaticamente informações como **identidade, posição, curso e velocidade** (curso = rumo), por sinais de rádio VHF.

**5 etapas:**

1. Coleta de dados (sensores do navio)
2. Transmissão via VHF
3. Protocolo SOTDMA (organiza quem fala quando)
4. Recepção e exibição
5. Cálculo anticolisão

### As categorias de dados (o coração do tópico)

| Categoria | Pergunta que responde | Exemplos | Quem insere | Frequência (deck) |
|---|---|---|---|---|
| **Estáticos** (🆕 também chamados "dados fixos") | *Quem sou eu?* | Nome, MMSI, tipo, dimensões | Na instalação (permanentes) | A cada 6 min |
| **Dinâmicos** | *Como me movo?* | Posição, velocidade, rumo, estado da navegação | Automático (sensores) | Segundos a minutos |
| **De viagem** | *Para onde vou?* | Calado, tipo de carga, destino, ETA | **Manual**, pelo comandante | A cada 6 min |
| **Msgs curtas de segurança** | *Preciso avisar algo* | Alerta, boia desaparecida; 🆕 alertas de segurança e informações sobre auxílio à navegação | Texto livre | Conforme necessidade |

As mensagens curtas podem ir para **uma embarcação específica ou para todas** na área. 🆕 Definição do baralho: mensagens de **texto em formato livre**, relacionadas à **segurança da navegação**.

### Parâmetros-chave

- Canais VHF **87B (161,975 MHz)** e **88B (162,025 MHz)**, dedicados ao AIS.
- Alcance navio-navio: **15 a 20 milhas náuticas** (maior com antena alta ou via satélite).
- **SAT-AIS**: satélites em órbita baixa captam o sinal e retransmitem a estações em terra (monitoramento global em mar aberto).

### Obrigatoriedade (IMO)

1. Navios **≥ 300 AB** em viagem **internacional**
2. Navios de **carga ≥ 500 AB** **não** engajados em viagem internacional
3. **Todos** os navios de passageiros

Esporte e recreio: geralmente só recomendado, podendo ser obrigatório em navegação oceânica.

> [!info] Detalhe do deck
> Quem é obrigado deve manter o AIS **sempre em funcionamento**. 🆕 *"Embarcações obrigadas a usar o **AIS**, devem mantê-lo sempre em **funcionamento**, a menos que a **segurança da navegação** exija o contrário para proteção de informações."*

**O que muda quando algo muda?** Dado dinâmico muda sozinho conforme o navio se move. Dado de viagem só muda se alguém digitar, por isso o destino pode ficar desatualizado.

## 3. Como identificar o tipo de questão

**Palavras-chave que gritam "AIS":** troca automática de informações · VHF · MMSI · SOTDMA · ETA · calado · SAT-AIS · "complementa o radar" · canais 87B/88B. 🆕 "sistema de auxílio à navegação" · "identidade, posição, curso e velocidade" · "consciência situacional" · "formato livre".

**Padrões típicos:**
- **Classificação:** "dado inserido manualmente pelo comandante" → viagem.
- **Lacuna:** "três categorias: ___, ___ e ___".
- **V/F com número trocado:** alcance 3–5 mi (falso), obrigatoriedade, canais.
- **"Cite quatro...":** vantagens, limitações, dados estáticos, dados de viagem.
- 🆕 **Definição-relâmpago**: "dados permanentes inseridos na instalação" → estáticos/fixos · "mudam com o movimento" → dinâmicos · "percurso atual, inseridos manualmente pelo comandante" → viagem · "texto livre relacionado à segurança" → mensagens curtas · "complementa o radar, camada adicional" → AIS · "direcionadas a embarcações específicas ou a todas" → mensagens curtas.

**Diferenciar parecidos:**
- **AIS vs ARPA:** AIS é *comunicação* entre navios; ARPA é *processamento do eco do radar*.
- **AIS vs VTS:** AIS é o equipamento; VTS é o *serviço* que o usa como sensor ([[02 VTS LPS VTMIS v1]]).
- **AIS vs SAT-AIS:** VHF 15–20 mi vs cobertura global.

## 4. Macetes, bizus e atalhos

> [!tip] Bizus
> - **Estáticos = "N-M-T-D":** **N**ome, **M**MSI, **T**ipo, **D**imensões. O RG do navio.
> - **Viagem = "C-C-D-E":** **C**alado, **C**arga, **D**estino, **E**TA. A passagem da viagem.
> - **Dinâmicos = o velocímetro:** posição, velocidade, rumo (e estado da navegação).
> - **"6-6":** estáticos e viagem a cada **6 min**; dinâmicos rápidos; mensagens só se necessário.
> - **Obrigatoriedade:** internacional = limite **menor (300)**; doméstica = só **carga ≥ 500**; **passageiros: todos**.
> - **Alcance:** VHF é linha de visada → **15–20 mi**. "3 a 5" é falso.
> - 🆕 **Estáticos = fixos:** se a pergunta diz "dados fixos", é o mesmo que estáticos.
> - 🆕 **Mensagens curtas = "texto livre + segurança + pode ser para todos".**

> [!warning] Pegadinhas
> - "Canais dedicados **exclusivamente**..." parece exagero, mas é **verdadeiro**. Não "corrija" o que está certo.
> - "SOTDMA usa **estação central**" → falso.
> - "AIS **substitui** o radar" → falso, sempre.
> - 🆕 Trocar **"curso"** por outra coisa: curso = **rumo**, não é outro dado.
> - 🆕 Esquecer que o complemento ao radar é **camada adicional de segurança e consciência situacional**, e não substituição.

**Quando NÃO confiar no AIS:** como único meio de detectar tráfego. Ele depende da **cooperação** do outro navio.

## 5. Raciocínio inverso (partir da resposta)

- **"Quem digita?"** Manual = viagem · instalação = estático · sensor = dinâmico.
- **"Qual a frequência?"** 6 min e **não** manual → estático · 6 min e manual → viagem · segundos → dinâmico.
- **"É obrigado?"** Passageiro? (sim) → senão, viagem internacional? (≥ 300 AB) → senão, carga? (≥ 500 AB).
- **"Aparece no radar, mas não no AIS?"** Não tem AIS, está desligado ou fora de alcance: limitação "dependência de cooperação".
- 🆕 **"Mensagem de texto livre, de segurança?"** → mensagens curtas. Se **vai para todos na área** ou para **uma embarcação específica**, é a mesma categoria.
- 🆕 **"Dados permanentes, inseridos na instalação?"** → estáticos/fixos. **"Mudam com o movimento?"** → dinâmicos.

## 6. Mapa mental da questão

1. **Qual é a pergunta?** Definição, classificação, número, V/F ou lista?
2. **Qual categoria de dado?** Quem, como, para onde ou aviso?
3. **Tem número?** Confira: 15–20 mi · 6 min · 300/500 AB · 87B/88B.
4. **É V/F?** Procure a **palavra trocada**: número, "estação central", "substitui", "satélite".
5. 🆕 **É lacuna ou definição-relâmpago?** Procure a pista: "instalação", "movimento", "manualmente", "formato livre", "camada adicional".

## 7. Resolução passo a passo

**Q1. (V/F) "O alcance típico navio-navio do AIS é de 3 a 5 milhas, sendo o SAT-AIS para distâncias superiores."**
1. AIS = VHF → o alcance vem da linha de visada.
2. Memória: 15–20 mi.
3. **Falso**: o erro está no número.

**Q2. "Dado relativo ao percurso atual, inserido manualmente pelo comandante."**
Pistas: *percurso atual* + *manual* → **dados de viagem**.

**Q3. "Principal função do SOTDMA."**
Alocar automaticamente os tempos de transmissão VHF para evitar interferência, **sem estação central**.

**Q4. "Cinco etapas do AIS."**
Coleta → transmissão VHF → SOTDMA → recepção/exibição → cálculo anticolisão.

**Q5. "Quatro vantagens e quatro limitações."**
- **Vantagens:** prevenção de colisão · gestão de tráfego e portuária · busca e salvamento · complementa o radar.
- **Limitações:** dependência da cooperação · alcance limitado (VHF) · risco de sobrecarga de informação · não substitui outros equipamentos.

🆕 **Q6. "O que é um AIS?"** Sistema de auxílio à navegação que permite às embarcações trocar automaticamente informações (identidade, posição, curso e velocidade) por sinais de rádio VHF. *Por que assim?* Estrutura: o que é + o que troca + por qual meio.

🆕 **Q7. "Meio de comunicação e alcance típico."** Rádio **VHF**, **15 a 20 milhas náuticas**.

🆕 **Q8. "Exemplos de mensagens curtas."** **Alertas de segurança** e **informações sobre auxílio à navegação** (por exemplo, uma boia desaparecida).

🆕 **Q9. (lacuna) "Para embarcações de ____, a obrigatoriedade do AIS varia."** **Esporte e recreio** (geralmente recomendado, podendo ser obrigatório em navegação oceânica).

🆕 **Q10. (lacuna) "O ____ opera por rádio VHF, alcance típico de 15 a 20 mi para comunicação ____."** **Sistema de Identificação Automática (AIS)**; **navio-navio**.

🆕 **Q11. "Frequência de transmissão."** Fixo: a cada 6 min · Dinâmicos: frequentemente, de segundos a minutos · De viagem: a cada 6 min · Mensagens curtas: conforme necessidade.

🆕 **Q12. "É usado para complementar o radar, oferecendo camada adicional de segurança e consciência situacional."** → **AIS**.

## 8. Como pensar sozinho

1. **Quem fala?** O navio, por VHF, sem central.
2. **O que ele fala?** Quem é, como se move, para onde vai e avisos.
3. **Para quê?** Evitar colisão, gerir tráfego, ajudar no salvamento.

Se o dado muda no enunciado (ex.: "mudou de destino"), pergunte: *é manual? É de viagem? Alguém precisa atualizar?*

🆕 Para as definições-relâmpago, faça a pergunta **"quem insere e quando muda?"**: instalação/permanente → estático · movimento → dinâmico · comandante/percurso → viagem · texto livre → mensagem curta.

## 9. Treinamento de raciocínio

**Fáceis**
- **F1.** O oficial digita "Santos, ETA 14h30, calado 9,8 m". Que categoria e quem insere?
- **F2.** V/F: "O SOTDMA depende de uma estação-base que distribui os horários." Se falso, corrija.
- **F3.** Complete: o AIS opera nos canais VHF ___ e ___.

**Médias**
- **M1.** Carga de 420 AB faz só cabotagem. Está obrigado ao AIS? E em viagem internacional?
- **M2.** Um iate aparece no radar, mas não no AIS. Dê três explicações possíveis.
- **M3.** Como diferenciar "boia X desaparecida" de um dado de viagem (formato, frequência, finalidade)?

**Difíceis**
- **D1.** No ECDIS, o triângulo AIS e o eco de radar do mesmo navio aparecem deslocados. O que isso sugere? Como descobrir quem está errado?
- **D2.** Explique por que o AIS *complementa* e não *substitui* o radar (duas limitações + uma vantagem do radar).
- **D3.** O que perde um VTS sem AIS? E o que continua útil num AIS sem VTS?

**🆕 Complemento do baralho novo**
- **F4.** Complete: "O AIS é um sistema de ____ à navegação que permite às embarcações trocar automaticamente identidade, posição, curso e velocidade por rádio ____."
- **M4.** Dê dois exemplos de mensagens curtas do AIS e diga por que não são dados de viagem.
- **D4.** Explique, com suas palavras, o que significa o AIS oferecer "camada adicional de segurança e consciência situacional" ao radar, sem substituí-lo.

> [!question] Modo treinador
> Responda por escrito antes de olhar qualquer gabarito. Depois confira com sua professora/tutor ou peça correção.

## 10. Questões com dados escondidos

**Q-A.** Carga de 600 AB, só entre portos brasileiros, desliga o AIS no porto "porque não precisa". Ele tem razão?
**Q-B.** Navio de passageiros de 250 AB em viagem doméstica. É obrigado?
**Q-C.** No VTS, o AIS de um navio mostra destino de três dias atrás. Categoria, responsável e risco?
**Q-D.** Um dado é enviado a cada 6 min e **não** é digitado por ninguém. Qual categoria?
🆕 **Q-E.** "Mensagem de texto livre, ligada à segurança, que pode ser enviada a um navio específico ou a todos na área." Qual categoria?
🆕 **Q-F.** "Dados permanentes da embarcação, inseridos na instalação." Como o baralho chama essa categoria?

> [!success]- Gabarito comentado
> - **Q-A:** carga **não internacional ≥ 500 AB** → é obrigado e deve manter o AIS **sempre ligado**. Ele está errado.
> - **Q-B:** passageiros: **sem corte de tamanho** → obrigado.
> - **Q-C:** dado de **viagem**, manual; responsabilidade da própria embarcação; risco: informação errada no VTS (limitação: depende de cooperação).
> - **Q-D:** 6 min e sem digitação → **estático**.
> - 🆕 **Q-E:** **mensagens curtas de segurança**.
> - 🆕 **Q-F:** **dados fixos (estáticos)**.

## 11. Erros mais comuns

| Erro | Como evitar |
|---|---|
| Trocar 15–20 mi por outro número | Ligue o alcance ao **VHF** (linha de visada) |
| SOTDMA com estação central | Imagem do grupo de WhatsApp sem administrador |
| Confundir estático com viagem | Estático = RG (permanente) · Viagem = manual, muda por viagem |
| Achar que AIS substitui radar | Ele só vê quem transmite |
| Errar o corte 300/500 AB | Internacional = 300 · doméstico = só carga ≥ 500 · passageiros = todos |
| "Corrigir" um "exclusivamente" verdadeiro (87B/88B) | Confira o fato antes de suspeitar da palavra |
| Esquecer que destino/ETA são manuais | Pergunte: "quem digitou?" |
| 🆕 Não reconhecer "dados fixos" como estáticos | São o mesmo: permanentes, inseridos na instalação |
| 🆕 Citar só "alertas" nas mensagens curtas | Dois exemplos: **alertas de segurança** e **informações sobre auxílio à navegação** |
| 🆕 Trocar "esporte e recreio" na lacuna da obrigatoriedade | Para esporte e recreio, varia: geralmente só recomendado |

## 12. Conexão entre os assuntos

- [[02 VTS LPS VTMIS v1]]: o AIS é sensor obrigatório do VTS; dados de viagem alimentam o VTMIS.
- [[03 ECDIS ENC]]: recebe o alvo AIS e mostra o triângulo sobre a carta.
- [[04 GNSS]]: fornece a posição que o AIS transmite. Se o GNSS erra, o AIS espalha o erro.
- Radar/ARPA: o AIS complementa o radar.
- [[07 CIS Bandeira Luzes e Marcas]]: o AIS ajuda, mas não dispensa a vigilância visual.

## 13. Resumo final de memorização rápida

- **AIS** = troca automática de identidade, posição, rumo e velocidade por **VHF**. Objetivo: segurança, prevenção de colisão. 🆕 **Sistema de auxílio à navegação**; princípio: integração de **posicionamento + comunicação sem fio**.
- **Canais:** 87B e 88B · **Alcance:** 15–20 mi · **Protocolo:** SOTDMA (sem central).
- **Categorias:** Estáticos (🆕 "fixos"; N-M-T-D, 6 min) · Dinâmicos (posição, velocidade, rumo, estado) · Viagem (C-C-D-E, manual, 6 min) · Msgs curtas (livre; 🆕 alertas de segurança e informações sobre auxílio à navegação).
- **5 etapas:** coleta → VHF → SOTDMA → exibição → anticolisão.
- **Obrigatório:** ≥300 AB internacional · carga ≥500 AB doméstica · todos os passageiros.
- **Vantagens:** colisão, tráfego/porto, SAR, complementa radar. **Limitações:** cooperação, alcance, sobrecarga, não substitui.
- **10 segundos:** *VHF · MMSI · ETA · SOTDMA · "troca automática"* → AIS. Se tiver número: 15–20, 6, 300/500.

### 🆕 Lacunas e definições do baralho novo (revisão rápida)

| Pergunta / lacuna | Resposta |
|---|---|
| Embarcações obrigadas a usar o ___, mantê-lo sempre em ___, a menos que a ___ exija o contrário | AIS · funcionamento · segurança da navegação |
| Para embarcações de ___, a obrigatoriedade varia | esporte e recreio |
| O ___ opera por VHF, 15–20 mi para comunicação ___ | Sistema de Identificação Automática (AIS) · navio-navio |
| Dados permanentes, inseridos na instalação | Dados fixos (estáticos) |
| Dados que mudam com o movimento | Dados dinâmicos |
| Dados do percurso atual, inseridos manualmente pelo comandante | Dados de viagem |
| Texto livre, relacionado à segurança da navegação | Mensagens curtas de segurança |
| Complementa o radar, camada adicional de segurança e consciência situacional | AIS |
| Mensagens que podem ir a embarcações específicas ou a todas na área | Mensagens curtas de segurança |

## 14. Modo treinador

> [!question] Responda sem olhar
> 1. Por que o AIS **não** substitui o radar? Use a analogia do letreiro.
> 2. Um dado muda de valor sozinho enquanto o navio navega. Qual categoria, e por que não é viagem?
> 3. Navio de 500 AB, carga, só no Brasil: por que precisa de AIS, mas um de 400 AB, também carga e só no Brasil, não?
> 4. 🆕 Quais são os dois exemplos de mensagens curtas do baralho e o que as diferencia dos dados de viagem?
