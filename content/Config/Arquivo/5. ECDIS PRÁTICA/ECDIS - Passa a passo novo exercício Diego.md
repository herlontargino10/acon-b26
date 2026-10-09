Sim. Abaixo está o **material completo atualizado**, já corrigido para o Obsidian. O principal ajuste é que os `>` aparecem **somente nas linhas que realmente pertencem aos Callouts**. O restante fica como Markdown normal.

Copie o bloco inteiro abaixo e cole no Obsidian.

# GUIA DE ESTUDO — SIMULADO PRÁTICO ECDIS

## TRANSAS / NAVI-SAILOR 4000

> [!info] Objetivo
> Guia operacional para execução do simulado prático no ECDIS Transas Navi-Sailor 4000.
>
> **Formato:** clique → selecione → configure → confirme o resultado.

---

# ⚠️ REGRA DE OURO

> [!warning] Regra de Ouro do Transas
> **A CADA PASSO QUE ALTERAR NA ROTA, SALVE!**
>
> Não colocar a rota em **Route Monitoring / Loaded** antes de finalizar todas as alterações.

### Sequência recomendada

`Criar → Editar → Salvar → Check Route → Corrigir perigos → Salvar novamente → Route Monitoring`

> [!danger] IMPORTANTE
> **Route Monitoring / Loaded deve ser a última etapa.**
>
> Antes disso:
> - [ ] Rota criada
> - [ ] Waypoints conferidos
> - [ ] Waypoints nomeados
> - [ ] Turn Radius configurado
> - [ ] Stay configurado
> - [ ] ETA calculada
> - [ ] Reference Points inseridos
> - [ ] Check Route executado
> - [ ] Perigos verificados
> - [ ] Rota salva
> - [ ] User Maps salvos
> - [ ] Demais configurações concluídas

---

# 📋 ÍNDICE

## Configuração inicial

- [[#1 — Configurar o ECDIS]]
- [[#1.1 — Giro inoperante]]
- [[#1.2 — Calado e parâmetros de segurança]]
- [[#1.3 — Dimensões e Turn Radius]]

## Planejamento da derrota

- [[#2 — Traçar a derrota]]
- [[#3 — Nomear os principais Waypoints]]
- [[#4 — Check Route e salvar]]
- [[#5 — Configurar horário, velocidade, Stay e ETA]]
- [[#6 — Inserir pontos de referência]]

## Monitoramento

- [[#7 — Ativar vetores e Safety Frame]]
- [[#8 — Adquirir e monitorar alvos AIS/ARPA]]
- [[#9 — Verificar maré na chegada]]

## Comunicação e anotações

- [[#10 — Enviar mensagem AIS]]
- [[#11 — Registrar recomendação do Comandante]]
- [[#12 — Criar zona de exercício militar]]

## Finalização

- [[#13 — Colocar a rota em Route Monitoring]]

## Consulta rápida

- [[#Resumo — Telas principais]]
- [[#Checklist final antes do Route Monitoring]]

---

# 1 — CONFIGURAR O ECDIS

### Dados do exercício

| Parâmetro | Valor |
|---|---:|
| Comprimento | **40 m** |
| Calado | **5 m** |
| Giro | **Inoperante** |

---

## 1.1 — Giro inoperante

Quando o giro estiver inoperante, utilizar a **agulha magnética** como fonte de heading.

### Caminho

`Task List → Navigation → Heading → Magnetic`

### Conferir

- [ ] Heading configurado para **Magnetic**
- [ ] Gyro não está selecionado como fonte de heading

> [!note] Resultado esperado
> O ECDIS passa a utilizar a fonte magnética de heading selecionada.

---

## 1.2 — Calado e parâmetros de segurança

### Calado do navio

**5 m**

Os parâmetros de segurança devem ser calculados a partir do calado indicado para o exercício.

### Cálculos

| Parâmetro | Fórmula | Resultado |
|---|---:|---:|
| Shallow Contour | `1,1 × 5` | **5,5 m** |
| Safety Contour | `1,2 × 5` | **6,0 m** |
| Safety Depth | `1,5 × 5` | **7,5 m** |
| Deep Contour | `2 × 5` | **10,0 m** |

### Acessar os parâmetros

`Task List → Monitoring → Safety Alarms → Route → Safety Parameters`

Configurar:

- [ ] **Safety Contour = 6,0 m**
- [ ] **Safety Depth = 7,5 m**

Depois, na configuração da carta:

`Task List → Tasks → Chart → ENC`

Configurar:

- [ ] **Shallow Contour = 5,5 m**
- [ ] **Deep Contour = 10,0 m**

> [!warning] Atenção
> Os valores acima seguem os cálculos definidos para o exercício com **calado de 5 m**.
>
> Não substituir os valores por aqueles de outro exercício ou exemplo.

---

## 1.3 — Dimensões e Turn Radius

### Comprimento do navio

**40 m**

### Acesso

`Task List → Advanced Planning → New → WPT`

Na tabela dos Waypoints, localizar:

`Turn Radius`

### Cálculo

`Turn Radius = Comprimento do navio × 3 ÷ 1852`

Para um navio de 40 m:

`40 × 3 ÷ 1852 = 0,0648 NM`

`≈ 0,065 NM`

> [!important] Valor no ECDIS
> Se o sistema transformar **0,065 NM** em **0,07 NM**, utilizar o valor apresentado pelo sistema.

### Conferir

- [ ] Comprimento = 40 m
- [ ] Turn Radius calculado
- [ ] Turn Radius inserido nos Waypoints necessários
- [ ] Rota salva após alteração

---

# 2 — TRAÇAR A DERROTA

### Destino

`50° 32.699' N`

`005° 02.249' W`

### Objetivo

Criar uma derrota com **no mínimo 10 Waypoints**.

### Acesso

`Task List → Advanced Planning → Route Editor → New`

### Procedimento

1. Criar uma nova rota.
2. Inserir a posição inicial.
3. Adicionar os Waypoints necessários.
4. Continuar inserindo pontos até atingir o mínimo exigido.
5. No último Waypoint, inserir as coordenadas exatas do destino.

### Destino — WPT final

```text
Latitude:
50° 32.699' N

Longitude:
005° 02.249' W
````

### Conferir

- [ ] Mínimo de 10 Waypoints
- [ ] Coordenadas do destino corretas
- [ ] Rota visualizada na carta
- [ ] Rota salva

> [!warning] Atenção  
> Não colocar a rota em **Route Monitoring** neste momento.

---

# 3 — NOMEAR OS PRINCIPAIS WAYPOINTS

Na tabela dos Waypoints, localizar a coluna:

`Name`

Nomear os principais pontos conforme a intenção de navegação.

### Nomes do exercício

| WPT    | Nome                                   |
| ------ | -------------------------------------- |
| WPT 1  | **Início da Navegação**                |
| WPT 3  | **Marcação de Alvo em Terra**          |
| WPT 5  | **Aguardar Prático (1h)**              |
| WPT 6  | **Pico de São do Val / Ponto de Giro** |
| WPT 10 | **Chegada no Porto**                   |

### Conferir

- [ ] WPT 1 nomeado
- [ ] WPT 3 nomeado
- [ ] WPT 5 nomeado
- [ ] WPT 6 nomeado
- [ ] WPT 10 nomeado
- [ ] Alterações salvas

---

# 4 — CHECK ROUTE E SALVAR

Depois de terminar a construção da derrota:

`Route Editor → Check Route`

### Verificar o resultado

Procurar possíveis:

- [ ] Perigos de navegação
- [ ] Áreas rasas
- [ ] Áreas proibidas
- [ ] Outros perigos identificados pelo ECDIS

> [!danger] Se houver perigo  
> Não ignorar o resultado.
> 
> Analisar o perigo indicado pelo ECDIS e corrigir a rota quando necessário.

Depois da correção:

`→ Salvar → Check Route novamente`

### Se estiver tudo correto

`Save → Save As → PROVA_PRATICA → Save`

---

# 5 — CONFIGURAR HORÁRIO, VELOCIDADE, STAY E ETA

### Dados do exercício

|Parâmetro|Valor|
|---|---|
|Data de partida|**10/04/2025**|
|Hora|**17:30 UTC**|
|Velocidade|**8,0 kn**|
|Stay no WPT 5|**1 hora**|

---

## 5.1 — Horário de partida

Com a rota aberta:

`Route Editor → Schedule`

Inserir:

```
ETD:
10/04/2025
17:30 UTC
```

---

## 5.2 — Velocidade

No campo de velocidade planejada:

`Speed = 8,0 kn`

---

## 5.3 — Stay no WPT 5

Na tabela dos Waypoints:

`WPT 5 → Stay`

Inserir:

`01:00`

> [!note] Significado  
> O navio deverá permanecer **1 hora no WPT 5** antes de prosseguir.

---

## 5.4 — Turn Radius

Conferir novamente:

`Route Editor → WPT → Turn Radius`

Valor calculado:

`40 × 3 ÷ 1852 = 0,0648 NM`

`≈ 0,065 NM`

---

## 5.5 — Calcular ETA

Executar o cálculo do Schedule.

O ECDIS deverá recalcular:

- Tempo de navegação
- Tempo de permanência no WPT 5
- ETA dos Waypoints
- ETA final no destino

### Conferir

- [ ] ETD correto
- [ ] 8,0 kn
- [ ] Stay = 01:00 no WPT 5
- [ ] Turn Radius correto
- [ ] ETA final registrada

---

# 6 — INSERIR 2 PONTOS DE REFERÊNCIA

> [!warning] Não confundir  
> **Reference Points** da rota não são a mesma coisa que objetos de **User Map**.

### Acesso

`Route Planning → Ref. Points`

### Primeiro ponto

1. Selecionar o Waypoint desejado.
2. Clicar com o botão esquerdo.
3. Posicionar o marcador no ponto de referência.
4. Confirmar.

### Segundo ponto

Repetir o procedimento em outro Waypoint.

### Resultado esperado

O ECDIS deverá mostrar:

- [ ] Ponto de referência
- [ ] Linha tracejada
- [ ] Bearing
- [ ] Distance

### Conferir

- [ ] Reference Point 1
- [ ] Reference Point 2
- [ ] Rota salva

---

# 7 — ATIVAR VETORES E CONFIGURAR SAFETY FRAME

## 7.1 — Vetores do navio

Acessar:

`Task List → Monitoring → Route Monitoring`

Selecionar os vetores necessários.

Exemplos:

- [ ] Headline
- [ ] COG Vector
- [ ] HDG Vector
- [ ] Wind Vector
- [ ] Outros vetores solicitados

### Tempo do vetor

Configurar conforme o exercício.

Exemplo:

`Vector Time = 6 min`

ou

`Vector Time = 12 min`

---

## 7.2 — Safety Frame

Acessar:

`Task List → Monitoring → Safety Frame`

Configurar os parâmetros solicitados pelo exercício.

Exemplo indicado no roteiro:

```
Forward Time = 10 min
Width = 0,5 NM
```

> [!warning] Atenção  
> Utilizar os valores efetivamente exigidos pelo exercício/professor. Os valores acima são os indicados neste roteiro.

---

# 8 — ADQUIRIR E MONITORAR ALVOS AIS / ARPA

### Antes de adquirir

Verificar:

- [ ] AIS habilitado
- [ ] ARPA A habilitado
- [ ] ARPA B habilitado
- [ ] Integração Radar/AIS disponível

### Acesso

`Task List → Targets`

Habilitar:

- [ ] ARPA A
- [ ] ARPA B
- [ ] AIS
- [ ] Tracks

### Monitoramento

Na tela da carta:

1. Localizar os alvos.
2. Selecionar os alvos desejados.
3. Conferir suas informações.
4. Acompanhar os respectivos tracks.

### Conferir

- [ ] AIS visível
- [ ] ARPA A visível
- [ ] ARPA B visível
- [ ] Tracks visíveis
- [ ] Alvos selecionados

---

# 9 — VERIFICAR A ALTURA DA MARÉ NA CHEGADA

Primeiro, obter a **ETA final** no Passo 5.

Depois:

`Task List → Tide / Tides → Table`

### Procedimento

1. Localizar a estação de maré mais próxima do destino.
2. Selecionar a data correspondente à chegada.
3. Selecionar/consultar o horário da ETA.
4. Localizar a altura da maré.
5. Registrar o resultado.

### Conferir

- [ ] Estação correta
- [ ] Data correta
- [ ] Horário baseado na ETA
- [ ] Altura da maré registrada

---

# 10 — ENVIAR MENSAGEM AIS DE SEGURANÇA

### Navio destinatário

```
MMSI:
123456789
```

### Acesso

`Task List → AIS → AIS Messaging`

Selecionar:

`Addressed Safety Message`

### Destinatário

`Destination / MMSI → 123456789`

### Mensagem de teste

```
EXPERIENCIA COM O EQUIPAMENTO
```

ou

```
TEST MESSAGE
```

Depois:

`→ Send`

### Conferir

- [ ] MMSI correto
- [ ] Tipo = Addressed Safety Message
- [ ] Texto inserido
- [ ] Send executado
- [ ] Status/resultado da transmissão verificado

---

# 11 — REGISTRAR RECOMENDAÇÃO DO COMANDANTE NA TSS

### Acesso

`Task List → User Maps → Editor`

Selecionar:

`Text`

### Procedimento

1. Localizar a área da **Traffic Separation Scheme — TSS**.
2. Inserir o objeto de texto.
3. Posicionar na área desejada.
4. Inserir a recomendação.

### Texto de exemplo

```
ATENÇÃO: MANTER VIGIA ATENTA E SEGUIR AS REGRAS DA TSS — ORDEM DO COMANDANTE.
```

### Finalizar

`→ Save User Map`

### Conferir

- [ ] Texto inserido
- [ ] Texto posicionado corretamente
- [ ] User Map salvo

---

# 12 — CRIAR ZONA DE EXERCÍCIO MILITAR

### Centro da área

```
Latitude:
50° 21.274' N

Longitude:
006° 33.831' W
```

### Raio

`5 NM`

### Acesso

`Task List → User Maps → New / Editor → Area / Circle`

### Configurar

```
Centro:
50° 21.274' N
006° 33.831' W

Radius:
5 NM
```

### Tipo / estilo

```
Military
/
Exercise Area
/
Danger Area
```

Conforme a opção disponível no equipamento/exercício.

### Finalizar

`→ Save User Map`

### Conferir

- [ ] Centro correto
- [ ] Raio = 5 NM
- [ ] Área criada
- [ ] Área visível na carta
- [ ] User Map salvo

---

# 13 — COLOCAR A ROTA EM ROUTE MONITORING

> [!danger] ÚLTIMA ETAPA  
> Só executar este passo depois de concluir e salvar todas as alterações.

## Checklist antes de carregar

- [ ] Navio configurado
- [ ] Giro/Magnetic configurado
- [ ] Safety Parameters configurados
- [ ] Rota criada
- [ ] Mínimo de 10 Waypoints
- [ ] Waypoints nomeados
- [ ] Turn Radius configurado
- [ ] Stay no WPT 5 = 1 h
- [ ] ETA calculada
- [ ] Reference Points inseridos
- [ ] Vetores configurados
- [ ] AIS/ARPA configurados
- [ ] Mensagem AIS enviada
- [ ] User Maps salvos
- [ ] Zona militar criada
- [ ] Check Route executado
- [ ] Perigos verificados
- [ ] Rota salva

---

## Carregar a rota

`Task List → Route Monitoring → Select Route / Load Route`

Selecionar:

`PROVA_PRATICA`

Confirmar.

> [!success] Resultado esperado  
> A rota deverá aparecer na tela de monitoramento e o navio estará pronto para acompanhar a derrota.

---

# ⚡ RESUMO RÁPIDO — TELAS PRINCIPAIS

| Função            | Caminho                                                              |
| ----------------- | -------------------------------------------------------------------- |
| Heading / Giro    | `Task List → Navigation → Heading`                                   |
| Safety Parameters | `Task List → Monitoring → Safety Alarms → Route → Safety Parameters` |
| Criar rota        | `Task List → Advanced Planning → New`                                |
| Waypoints         | `Advanced Planning → WPT`                                            |
| Check Route       | `Route Planning → Check Route`                                       |
| Schedule / ETA    | `Route Planning → Schedule`                                          |
| Reference Points  | `Route Planning → Ref. Points`                                       |
| Vetores           | `Task List → Monitoring → Route Monitoring`                          |
| Safety Frame      | `Task List → Monitoring → Safety Frame`                              |
| AIS / ARPA        | `Task List → Targets`                                                |
| Maré              | `Task List → Tide → Table`                                           |
| AIS Messaging     | `Task List → AIS → Messaging`                                        |
| User Maps         | `Task List → User Maps`                                              |
| Route Monitoring  | `Task List → Route Monitoring`                                       |

---

# ✅ CHECKLIST FINAL DA PROVA

## 1. NAVIO

- [ ] Comprimento = **40 m**
- [ ] Calado = **5 m**
- [ ] Giro inoperante → **Magnetic**
- [ ] Turn Radius calculado

## 2. SEGURANÇA

- [ ] Shallow Contour = **5,5 m**
- [ ] Safety Contour = **6,0 m**
- [ ] Safety Depth = **7,5 m**
- [ ] Deep Contour = **10,0 m**
- [ ] Safety Frame

## 3. ROTA

- [ ] Mínimo 10 WPT
- [ ] Destino = **50°32.699'N / 005°02.249'W**
- [ ] WPTs nomeados
- [ ] Turn Radius
- [ ] Stay WPT 5 = **01:00**
- [ ] ETD = **10/04/2025 17:30 UTC**
- [ ] Speed = **8 kn**
- [ ] ETA calculada
- [ ] Check Route
- [ ] Rota salva

## 4. REFERÊNCIAS

- [ ] 2 Reference Points

## 5. MONITORAMENTO

- [ ] Headline
- [ ] COG Vector
- [ ] HDG Vector
- [ ] Wind Vector
- [ ] AIS
- [ ] ARPA A
- [ ] ARPA B
- [ ] Tracks

## 6. MARÉ

- [ ] ETA final obtida
- [ ] Estação de maré selecionada
- [ ] Data correta
- [ ] Horário da ETA
- [ ] Altura registrada

## 7. COMUNICAÇÃO

- [ ] AIS Safety Message
- [ ] MMSI = **123456789**
- [ ] Mensagem enviada

## 8. USER MAPS

- [ ] Nota do Comandante na TSS
- [ ] Zona militar
- [ ] Centro correto
- [ ] Raio = **5 NM**
- [ ] Mapas salvos

## 9. FINAL

> [!danger] Só agora  
> `Route Monitoring → Select Route / Load Route → PROVA_PRATICA`
> 
> **Rota carregada somente após todas as verificações anteriores.**
