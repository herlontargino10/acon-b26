

````markdown
# ECDIS — Passo a Passo Operacional

> [!info] Objetivo
> Reunir em uma única nota os procedimentos práticos de ECDIS para consulta durante os exercícios, organizados por função e por questão.

---

# Índice

## Planejamento e Monitoramento de Derrota
- [[#Passo 1 — Configurar dados do navio]]
- [[#Passo 2 — Traçar a rota]]
- [[#Passo 3 — Nomear os Way Points]]
- [[#Passo 4 — Verificar e nomear a rota]]
- [[#Passo 5 — Calcular ETA]]
- [[#Passo 6 — Confirmar ETA no destino]]
- [[#Passo 7 — Ajustar horário de referência]]
- [[#Passo 8 — Configurar AIS e monitorar]]
- [[#Passo 9 — Configurar Safety Frame]]
- [[#Passo 10 — Verificar maré na chegada]]
- [[#Passo 11 — Enviar mensagem AIS]]
- [[#Passo 12 — Transferir rota para monitoramento]]

## Exercício Prático — 22 Questões
- [[#Questão 1 — CUSTOM]]
- [[#Questão 2 — Spot Sounding]]
- [[#Questão 3 — Sensor primário de posição]]
- [[#Questão 4 — Criar derrota e monitorar dados]]
- [[#Questão 5 — Ativar sensores]]
- [[#Questão 6 — Habilitar sensores AIS e ARPA]]
- [[#Questão 7 — Habilitar alvos]]
- [[#Questão 8 — Visualizar alvos]]
- [[#Questão 9 — Monitorar Headline, COG e HDG]]
- [[#Questão 10 — Ship by Contour e Wind Vector]]
- [[#Questão 11 — Align by HDG]]
- [[#Questão 12 — Safety Contour e Safety Depth]]
- [[#Questão 13 — Vetor do navio]]
- [[#Questão 14 — Fuso horário]]
- [[#Questão 15 — Hora do navio]]
- [[#Questão 16 — Conning / Nav Aids]]
- [[#Questão 17 — Acionar AIS]]
- [[#Questão 18 — Mensagem AIS para todos]]
- [[#Questão 19 — Mensagem AIS para navio específico]]
- [[#Questão 20 — Derrota no Estreito de Gibraltar]]
- [[#Questão 21 — ETA do navio]]
- [[#Questão 22 — Maré no local de chegada]]

## Exercício Prático 2
- [[#EP2-1A — Comprimento do navio]]
- [[#EP2-1B — Calado e parâmetros de segurança]]
- [[#EP2-1C — Navio sem giro]]
- [[#EP2-2 — Criar derrota]]
- [[#EP2-3 — Nomear Waypoints]]
- [[#EP2-4 — Check Route]]
- [[#EP2-5 — Stay no Waypoint 5]]
- [[#EP2-6 — Pontos de referência]]
- [[#EP2-7 — Ativar vetores]]
- [[#EP2-8 — Adquirir alvos AIS/ARPA]]
- [[#EP2-9 — Habilitar Safety Frame]]
- [[#EP2-10 — Verificar maré]]
- [[#EP2-11 — Verificar horários]]

---

# PARTE 1 — PLANEJAMENTO E MONITORAMENTO DE DERROTA

> [!note] Fonte
> Procedimentos organizados no documento de apoio.

---

## Passo 1 — Configurar dados do navio

### Acesso

```text
Configurações / Settings
→ Ship Parameters
````

### Configurar os dados do navio

- Comprimento: **40 m**

> [!warning] Atenção — Turn Radius (Curva de Giro)
> O comprimento do navio deve ser considerado no **Advanced Planning**, na coluna **Turn Radius (Curva de Giro)**.
>
> Para determinar o valor a ser inserido no campo, utilizar:
>
> **Turn Radius = (Comprimento do navio × 3) ÷ 1852**
>
> **Exemplo — navio de 40 m:**
>
> `(40 × 3) ÷ 1852 = 0,0648 nm`
>
> Portanto, o valor calculado é aproximadamente **0,065 nm**.
>
> Ao inserir o valor no ECDIS, o sistema pode arredondá-lo automaticamente para **0,07 nm**, conforme a precisão permitida pelo campo.
>
> **Resultado no equipamento: 0,07 nm**

- Calado: **5 m** 

> [!warning] Atenção — Parâmetros de Segurança
> O **calado do navio indicado pelo professor é 5 m**.
>
> Esse valor será utilizado para calcular os parâmetros de segurança da carta.
>
> ### Cálculos
>
> **Shallow Contour**
>
> `1,1 × Calado`
>
> `1,1 × 5 = 5,5 m`
>
> **Resultado: 5,5 m**
>
> ---
>
> **Safety Contour**
>
> `1,2 × Calado`
>
> `1,2 × 5 = 6,0 m`
>
> **Resultado: 6,0 m**
>
> ---
>
> **Safety Depth**
>
> `1,5 × Calado`
>
> `1,5 × 5 = 7,5 m`
>
> **Resultado: 7,5 m**
>
> ---
>
> **Deep Contour**
>
> `2 × Calado`
>
> `2 × 5 = 10,0 m`
>
> **Resultado: 10,0 m**


```text
Configurações / Settings
→ Safety Settings
```

Definir:

- Profundidade Segura: **7,0 m**
    
- Contorno Seguro: **7,0 m**
    
- Zona de Segurança: **0,1 milha (100 m)**
    

Depois:

```text
→ ENTER
```

---

## Passo 2 — Traçar a rota

### Acesso

```text
Editor de Rota / Route Editor
→ Advanced Plannig -> New
```

### Primeiro ponto

Na tela do mapa:

```text
02° 21,899' S
005° 02,249' W
```

→ **Adicionar**

### Ponto de chegada

```text
00° 52,699' N
005° 02,249' W
```

→ **Adicionar**

A rota aparece ligando os dois pontos.

```text
→ Salvar
```

---

## Passo 3 — Nomear os Way Points

Na lista de pontos:

### Primeiro ponto

```text
Advanced Plannig
Selecionar WP desejado, da um duplo clique
→ Renomear / Rename
→ Exemplo: Través com Cabo Frio.
```

### Segundo ponto

```text
Selecionar WP
→ Renomear / Rename
→ WP2 — DESTINO
```

→ **OK**

---

## Passo 4 — Verificar e nomear a rota

```text
Verificar Rota / Check Route
```

Conferir se os alarmes gerados não impedem a navegação.

-  Sem áreas rasas
    
-  Sem áreas proibidas
    
-  Sem perigos
    

Depois:

```text
→ Salvar Rota
```

Nome:

```text
ROTA 001 — S N (005° W)
```

→ **Fechar**

---

## Passo 5 — Calcular ETA

Na rota salva:

```text
Propriedades / Properties
```

Preencher:

- Velocidade: **5 nós**
    
- Horário de partida: **10/04/2025 — 17:30 UTC**
    




Depois:

```text
→ Calcular / Calculate
```

Resultado indicado no documento:

- Distância: **~194,6 milhas**
    
- Tempo de viagem: **~38 h 55 min**
    
- ETA: **12/04/2025 — 08:25 UTC**
    

---

## Passo 6 — Confirmar ETA no destino

Verificar:

```text
10/04 — 17:30
+
38 h 55 min
=
12/04 — 08:25 UTC
```

Confirmar:

-  Velocidade de 5 nós
    
-  ETA registrada
    
-  Resultado anotado no relatório de navegação
    

---

## Passo 7 — Ajustar horário de referência

```text
Configurações Sistema / System
→ Time Zone
```

Selecionar:

```text
UTC (0)
```

Verificar:

-  Relógio correto
    
-  Sincronização com GPS
    

→ **OK**

---

## Passo 8 — Configurar AIS e monitorar

```text
Configurações
→ Sensores / Sources
→ AIS
```

Preencher:

- Nome
    
- MMSI
    
- Sinal de chamada
    
- Tipo de embarcação
    
- Dimensões: **40 m**
    
- Calado: **6 m**
    

Ativar:

```text
Show AIS Targets
```

Voltar para a tela principal.

Os navios deverão aparecer como triângulos.

Selecionar um alvo e verificar seus dados.


As configurações funcionam apenas se o AIS não estiver marcado em cor vermelha no menu display. 

---

## Passo 9 — Configurar Safety Frame

```text
Monitoring
→ Zona de Segurança
```

Ativar:

```text
Cross-Track Distance
```

Definir:

- XTE máximo: **0,05 milha**
    
- Alarme de aproximação: **3 milhas / 10 minutos**
    

Ativar:

```text
Alarme de Contorno Seguro
```

→ **OK**

Resultado esperado:

> O sistema deverá avisar caso o navio saia da rota ou se aproxime de perigo.

---

## Passo 10 — Verificar maré na chegada

Abrir:

```text
Tábuas de Marés
```

ou livro de referência.

Local:

```text
00°52,699'N
005°02,249'W
```

Data:

```text
12/04/2025
```

Horário:

```text
08:25 UTC
```

Anotar a altura da maré.

Verificar:

```text
Calado + altura da maré
→ profundidade disponível
```

Se adequado:

-  Prosseguir
    

Se inadequado:

-  Ajustar velocidade
    
-  Aguardar preamar
    

Registrar no Diário de Navegação.

---

## Passo 11 — Enviar mensagem AIS

Selecionar o navio próximo:

```text
Navio / Target
→ Mensagem / Text Message
```

Mensagem indicada:

> "Solicito passagem segura. Rumo 000°, velocidade 5 nós. Confirmo recepção."

→ **Send**

Aguardar confirmação.

Registrar:

- Horário
    
- Nome/MMSI
    
- Resposta recebida
    

---

## Passo 12 — Transferir rota para monitoramento

Selecionar:

```text
ROTA 001
```

Depois:

```text
Transfer to Monitoring
```

Confirmar que a rota aparece na tela com a linha de navegação.

Resultado:

-  Rota em monitoramento
    
-  Alarmes ativos
    
-  Navio seguindo a rota
    

---

# PARTE 2 — EXERCÍCIO PRÁTICO — 22 QUESTÕES

> [!important] Estrutura  
> Esta seção mantém a sequência das 22 questões do exercício prático fornecido.

---

## Questão 1 — CUSTOM

Configurar o modo de apresentação da carta como:

```text
CUSTOM
```

---

## Questão 2 — Spot Sounding

Configurar:

```text
SPOT SOUNDING
→ até 15,0 m
```

---

## Questão 3 — Sensor primário de posição

Definir:

```text
Primary Position Sensor
→ DGPS 1
```

---

## Questão 4 — Criar derrota e monitorar dados

Criar uma derrota com:

```text
5 Way Points
```

### Route Data — Monitorar dados da derrota

- **CRS**
    
- **XTD**
    
- **BTW**
    
- **DTX**

**Caminho:**

`Control Panel → Display Panel → Route Data`

**Se não aparecerem os dados da derrota:**
1. Verificar a opção atualmente selecionada no Display Panel.
2. Alterar para **Route Data**.
3. Confirmar a exibição dos dados da derrota.

![[Pasted image 20260922105448.png]]


---

## Questão 5 — Ativar sensores

Ativar:

```text
DGPS 1
GYRO 1
DLOG 1
ECHOSOUNDER 1
```

---

## Questão 6 — Habilitar sensores AIS e ARPA

Habilitar:

```text
AIS
ARPA A
ARPA B
```

---

## Questão 7 — Habilitar alvos

Na aba de Targets:

```text
Targets
→ ARPA A
→ ARPA B
→ AIS
→ Tracks
```

---

## Questão 8 — Visualizar alvos

Verificar visualmente na tela/carta do ECDIS:

-  ARPA A
    
-  ARPA B
    
-  AIS
    
-  Tracks
    

---

## Questão 9 — Monitorar Headline, COG e HDG

Acessar:

```text
Monitoring
```

Monitorar:

- **Headline**
    
- **COG Vector**
    
- **HDG Vector**
    

---

## Questão 10 — Ship by Contour e Wind Vector

Acessar:

```text
Monitoring
```

Habilitar:

- **Ship by Contour**
    
- **Wind Vector**
    

---

## Questão 11 — Align by HDG

Acessar:

```text
Monitoring
```

Habilitar:

```text
Align by HDG
```

> [!note] Heading Marker  
> O Heading Marker representa graficamente a direção do heading/proa do navio na carta.

---

## Questão 12 — Safety Contour e Safety Depth

Acessar:

```text
Monitoring
→ Safety Parameter
```

Configurar/verificar:

```text
Safety Contour
Safety Depth
```

---

## Questão 13 — Vetor do navio

No painel de controle vertical/lateral:

```text
Ship Vector
```

Configurar:

```text
mínimo: 6 min
```

---

## Questão 14 — Fuso horário

Acessar:

```text
Config
→ Time Zone
```

Inserir:

```text
0300W
```

---

## Questão 15 — Hora do navio

No painel de controle vertical/lateral:

```text
Ship's Time
```

Verificar/exibir a hora do navio.

---

## Questão 16 — Conning / Nav Aids

Acessar:

```text
Conning
→ Nav Aids
```

---

## Questão 17 — Acionar AIS

No painel de controle vertical:

```text
AIS
```

Acionar/habilitar o AIS.

---

## Questão 18 — Mensagem AIS para todos

Acessar:

```text
AIS Message
```

Criar e enviar:

```text
Safety Message
→ TO ALL
```

---

## Questão 19 — Mensagem AIS para navio específico

Acessar:

```text
AIS Message
```

Criar e enviar:

```text
Normal Message
→ TO SPECIFIC
```

---

## Questão 20 — Derrota no Estreito de Gibraltar

Criar uma derrota:

```text
→ Entrada no Estreito de Gibraltar
```

---

## Questão 21 — ETA

Determinar a:

```text
ETA do navio
```

Valor indicado no exercício:

```text
18:12
```

---

## Questão 22 — Maré

Verificar a maré no local de chegada.

Valor indicado:

```text
0,46 m
```

Verificar também:

```text
Task
→ Facilities
```

Resultado indicado no exercício:

```text
SIM — o porto possui facilidades
```

---

# PARTE 3 — EXERCÍCIO PRÁTICO 2

---

## EP2-1A — Inserir comprimento do navio

Acessar:

```text
Task List
→ Advanced Planning
→ New
→ WPT
```

Criar os pontos da derrota.

Na tabela dos Waypoints:

```text
→ coluna TURN RATIO
```

Inserir o comprimento do navio conforme:

```text
3 × comprimento do navio
-------------------------
          1.852
```

---

## EP2-1B — Inserir calado e parâmetros de segurança

### Safety Contour

```text
Task List
→ Monitoring
→ Safety Alarms
→ Route
→ Safety Parameters
```

Safety Contour:

```text
Calado × 1,2
```

Ou:

```text
Calado + 20%
```

### Safety Depth

```text
Calado × 1,5
```

Ou:

```text
Calado + 50%
```

### Shallow Contour

Acessar:

```text
Task List
→ Tasks
→ Chart
→ ENC
```

Configurar:

```text
Shallow Contour
= Calado × 1,1
```

### Deep Contour

Configurar:

```text
Deep Contour
= Calado × 2,0
```

---

## EP2-1C — Navio sem giro

Acessar:

```text
Task List
→ Navigation
→ Heading
```

Selecionar:

```text
MAGNÉTICA
```

---

## EP2-2 — Criar derrota

Acessar:

```text
Task List
→ Advanced Planning
→ New
```

Criar uma derrota com:

```text
→ Entrada no Estreito de Gibraltar
```

---

## EP2-3 — Nomear Waypoints

Depois de criar a derrota:

```text
Tabela dos Waypoints
→ coluna/linha abaixo de NAME
```

Inserir o nome de cada Waypoint.

---

## EP2-4 — Check Route

Na mesma página de criação dos Waypoints:

```text
→ Check Route
→ Play
```

Executar a verificação da derrota.

---

## EP2-5 — Stay no Waypoint 5

Na tabela dos Waypoints:

```text
→ selecionar Waypoint 5
→ campo STAY
```

Inserir:

```text
0100
```

Significado:

> O navio deverá aguardar uma hora no Waypoint 5 antes de prosseguir.

---

## EP2-6 — Pontos de referência

Acessar:

```text
→ REF PTS
```

Para criar o primeiro ponto:

```text
Clicar com botão esquerdo no Waypoint
→ segurar
→ arrastar até o ponto de terra mais próximo
→ soltar
```

Repetir para criar o segundo ponto de referência.

---

## EP2-7 — Ativar vetores

Acessar:

```text
Task List
→ Monitoring
→ Route Monitoring
```

Selecionar cada vetor desejado.

Exemplos:

-  Wind
    
-  COG
    
-  Outros vetores disponíveis
    

---

## EP2-8 — Adquirir alvos AIS / ARPA

Adquirir os alvos:

```text
AIS
ARPA
```

Verificar sua apresentação no ECDIS.

---

## EP2-9 — Habilitar Safety Frame

Acessar:

```text
Task List
→ Monitoring
→ Safety Frame
```

Habilitar:

```text
Safety Frame
```

---

## EP2-10 — Verificar maré

Para o local de chegada da derrota:

```text
Task
→ Tide
→ Table
```

Localizar o valor da maré correspondente ao horário de chegada no último Waypoint da derrota de Gibraltar.

---

## EP2-11 — Verificar horários

Para conferir os horários configurados:

```text
Task List
→ Config
→ Time Zone
```

Observar:

```text
UTC Time
Ship's Time
Time Zone
```

---

# CHECKLIST RÁPIDO — ANTES DE EXECUTAR

## Configuração

-  CUSTOM
    
-  Spot Sounding
    
-  Sensor primário
    
-  Heading
    
-  Time Zone
    
-  Ship's Time
    

## Sensores

-  DGPS 1
    
-  GYRO 1
    
-  DLOG 1
    
-  Echosounder 1
    
-  AIS
    
-  ARPA A
    
-  ARPA B
    

## Carta

-  Display Category / Custom
    
-  Spot Sounding
    
-  Layers
    
-  Safety Contour
    
-  Safety Depth
    
-  Shallow Contour
    
-  Deep Contour
    

## Rota

-  Waypoints
    
-  Nome dos Waypoints
    
-  Check Route
    
-  Nome da rota
    
-  Stay
    
-  Reference Points
    
-  Route Monitoring
    

## Monitoramento

-  CRS
    
-  XTD
    
-  BTW
    
-  DTX
    
-  Headline
    
-  COG Vector
    
-  HDG Vector
    
-  Wind Vector
    
-  Ship by Contour
    
-  Align by HDG
    

## Segurança

-  Safety Parameters
    
-  Safety Contour
    
-  Safety Depth
    
-  Safety Frame
    
-  Safety Alarms
    
-  Area Alerts
    

## AIS / ARPA

-  Alvos AIS visíveis
    
-  ARPA A
    
-  ARPA B
    
-  Aquisição de alvos
    
-  AIS Message — TO ALL
    
-  AIS Message — TO SPECIFIC
    

## Chegada

-  ETA
    
-  Maré
    
-  Facilities
    

```

### Uma observação importante

No arquivo, há **alguns valores que não coincidem com as questões que você me passou anteriormente**. Por exemplo, o documento usa **calado de 6 m** no primeiro procedimento e coordenadas diferentes no exemplo de criação da rota. :contentReference[oaicite:1]{index=1}

Por isso, para o seu material definitivo de estudo, eu manteria esta nota como **“procedimento de referência”**, mas deixaria os **valores específicos da prova/exercício** dentro de cada questão. Isso evita misturar um exemplo do manual com os dados que o professor efetivamente forneceu.
```