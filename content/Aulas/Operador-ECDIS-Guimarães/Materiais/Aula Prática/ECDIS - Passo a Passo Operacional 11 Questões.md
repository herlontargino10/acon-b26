
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

---

# PLANEJAMENTO E MONITORAMENTO DE DERROTA

---

## Passo 1 — Navio a Gyro Inoperante

Verificar os sensores e selecionar a agulha Magnética.

```text
Task List → Navigation → Heading → Magnetic
```

Selecionar:

```text
MAGNETIC
```

[[#Índice]]


## Passo 1.1 — Criar Waypoints


```text
→ Task List → Advanced Plannig -> New
```


### Primeiro ponto

Na tela do mapa:

```text
Depende da posição do navio no momento
```

→ **Adicionar utilizando o cursor mouse.** 

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

[[#Índice]]


## Passo 2 — Configurar tamanho do navio


```text
→ Task List → Advanced Plannig -> Coluna Turn Radius
````


- Comprimento: **40 m**

> [!warning] Atenção — Turn Radius (Curva de Giro)
> **Pré-requisito:** os **Waypoints precisam estar criados antes de configurar o Turn Radius.**
>
> O comprimento do navio deve ser considerado no **Advanced Planning**, na coluna **Turn Radius (Curva de Giro)** dando um duplo clique.
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

![[Pasted image 20261005172229.png]]


### Adicionar parâmetros de calado (Safety Contour e Safety Deep) 


```text 
→ Task List → Monitoring → Aba Safety Alarms → Aba Safety Meters
```

- Calado: **5 m** 

> [!warning] Atenção — Parâmetros de Segurança
> O **calado do navio indicado pelo professor é 5 m**.
>
> Esse valor será utilizado para calcular os parâmetros de segurança da carta.
>
> ### Cálculos
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

![[20261005_094824.jpg]]


### Adicionar parâmetros de calado (Shallow Contour e Deep Contour) 

```text 
→ Task List → Charts → Aba ENC
```


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
> **Deep Contour**
>
> `2 × Calado`
>
> `2 × 5 = 10,0 m`
>
> **Resultado: 10,0 m**

![[20261005_094802.jpg]]

[[#Índice]]

---

## Passo 3 — Nomear os Way Points

Na lista de pontos:

### Primeiro ponto

```text
→ Task List → Advanced Plannig -> Selecionar WP desejando
````

Selecionar WP desejado, da um duplo clique
→ Renomear 
→ Exemplo: Través Cabo Frio.
→ **ENTER**

[[#Índice]]

---

## Passo 4 — Verificar a rota

```text
→ Task List → Advanced Plannig -> Check Route
````

![[Pasted image 20261005173346.png]]

Conferir se os alarmes gerados não impedem a navegação.

-  Sem áreas rasas
    
-  Sem áreas proibidas
    
-  Sem perigos
    

Depois:

```text
→ Salvar Rota
```

[[#Índice]]

---

## Passo 5 — Calcular ETA com a ferramenta Schedule

Na rota salva:

```text
→ Task List → Advanced Plannig -> Schedule Calculation -> Create Schedule -> Schedule Calculation Botão Play
````


> [!warning] Antes de calcular o Schedule
> Antes de executar o **Schedule**, é necessário preencher as informações abaixo:
>
> **1. ETD — Horário de partida**
>
> Inserir **somente na Linha 0**:
>
> `10/04/2025 — 17:30 UTC`
>
> **2. Velocidade**
>
> Inserir a velocidade planejada na **Linha 1** e replicá-la até o último Waypoint.
>
> ### Atalho — Replicar a velocidade
>
> 1. Insira a velocidade desejada na **Linha 1**.
> 2. Clique com o **botão direito do mouse** sobre o valor inserido.
> 3. Selecione **Fill**.
> 4. O ECDIS irá replicar automaticamente a velocidade para o restante da coluna, até o último Waypoint.
>
> **3. STAY — Tempo de permanência**
>
> Após preencher a velocidade, localize a **linha do Waypoint indicado pelo professor** e, nessa mesma linha, preencha o campo **STAY**.
>
> **Neste exercício:**
>
> - **Waypoint:** WPT 5
> - **STAY:** `01:00 h`
>
> > [!important] Atenção
> > O **STAY deve ser inserido na linha do Waypoint correspondente**.
> >
> > Neste exercício, inserir **01:00 h na linha do WPT 5**.
>
> Depois de preencher o ETD, a velocidade e o STAY, o Schedule estará pronto para ser calculado.


![[Pasted image 20261005173528.png]]


[[#Índice]]

---

## Passo 6 — Inserir 2 pontos de referência

Acessar:

```text
→ → Task List → Advanced Plannig -> REF. PTS
```

Para criar uma referência:

```text
Clicar com botão esquerdo no Waypoint onde vai partir essa marcação
→ segurar
→ arrastar até o ponto de terra mais próximo (Ex: Um faról)
→ soltar
```

Repetir para criar o segundo ponto de referência.


[[#Índice]]

## Passo 7 — Ativar os vetores do navio (CONFIRMAR)




---

## Passo 8 — Adiquiri alvos no AIS e ARPA (CONFIRMAR)

```text
Configurações
→ Sensores / Sources
→ AIS
```

Preencher:


Ativar:

```text
Show AIS Targets
```

Voltar para a tela principal.

Os navios deverão aparecer como triângulos.

Selecionar um alvo e verificar seus dados.

As configurações funcionam apenas se o AIS não estiver marcado em cor vermelha no menu display. 

[[#Índice]]

---

## Passo 9 — Configurar Safety Frame

```text
Task List → Monitoring - Aba Safety Alarms → Safety Frame
```


![[Pasted image 20261005180237.png]]

[[#Índice]]

---

## Passo 10 — Verificar maré na chegada

```text
Task List -> Tasks -> Tides 
```

> [!tip] Buscar da tábua de maré
> A estação pode ser localizada:
>
> - **Por nome:** `Places`
> - **Por proximidade:** definir um **raio de distância** e buscar as estações mais próximas.


[[#Índice]]

---

## Passo 11 — Enviar mensagem AIS

Selecionar o navio próximo:

```text
Task List -> AIS -> Navio -> Aba Messaging
→ Mensagem / Text Message
```

No campo **Send Message**, escolher o tipo de mensagem:

- **Safety Text** — mensagem de segurança
- **Normal Text** — mensagem normal

### Exemplo de mensagem

`Teste de equipamento.`

Após inserir a mensagem:

`→ Send on Channel A & B`

> [!warning] Atenção
> Antes de enviar, confirme se o tipo de mensagem selecionado (**Safety Text** ou **Normal Text**) corresponde ao que foi solicitado no exercício.

[[#Índice]]

---

## Passo 12 — Registrar na carta recomendação do Comandante (Confirmar) 

Ferramenta MAPS.

Selecionar:




[[#Índice]]


## Passo 12 — Registrar na carta um aviso rádio 
Ferramenta Man Corr

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

[[#Índice]]

---

## Questão 2 — Spot Sounding

Configurar:

```text
SPOT SOUNDING
→ até 15,0 m
```

[[#Índice]]

---

## Questão 3 — Sensor primário de posição

Definir:

```text
Primary Position Sensor
→ DGPS 1
```

[[#Índice]]

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

[[#Índice]]

---

## Questão 5 — Ativar sensores

Ativar:

```text
DGPS 1
GYRO 1
DLOG 1
ECHOSOUNDER 1
```

[[#Índice]]

---

## Questão 6 — Habilitar sensores AIS e ARPA

Habilitar:

```text
AIS
ARPA A
ARPA B
```

[[#Índice]]

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

[[#Índice]]

---

## Questão 8 — Visualizar alvos

Verificar visualmente na tela/carta do ECDIS:

-  ARPA A
    
-  ARPA B
    
-  AIS
    
-  Tracks

[[#Índice]]

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

[[#Índice]]

---

## Questão 10 — Ship by Contour e Wind Vector

Acessar:

```text
Monitoring
```

Habilitar:

- **Ship by Contour**
    
- **Wind Vector**

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

---

## Questão 15 — Hora do navio

No painel de controle vertical/lateral:

```text
Ship's Time
```

Verificar/exibir a hora do navio.

[[#Índice]]

---

## Questão 16 — Conning / Nav Aids

Acessar:

```text
Conning
→ Nav Aids
```

[[#Índice]]

---

## Questão 17 — Acionar AIS

No painel de controle vertical:

```text
AIS
```

Acionar/habilitar o AIS.

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

---

## Questão 20 — Derrota no Estreito de Gibraltar

Criar uma derrota:

```text
→ Entrada no Estreito de Gibraltar
```

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

---

## EP2-3 — Nomear Waypoints

Depois de criar a derrota:

```text
Tabela dos Waypoints
→ coluna/linha abaixo de NAME
```

Inserir o nome de cada Waypoint.

[[#Índice]]

---

## EP2-4 — Check Route

Na mesma página de criação dos Waypoints:

```text
→ Check Route
→ Play
```

Executar a verificação da derrota.

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

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

[[#Índice]]

---

## EP2-8 — Adquirir alvos AIS / ARPA

Adquirir os alvos:

```text
AIS
ARPA
```

Verificar sua apresentação no ECDIS.

[[#Índice]]

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

[[#Índice]]

---

## EP2-10 — Verificar maré

Para o local de chegada da derrota:

```text
Task
→ Tide
→ Table
```

Localizar o valor da maré correspondente ao horário de chegada no último Waypoint da derrota de Gibraltar.

[[#Índice]]

---

