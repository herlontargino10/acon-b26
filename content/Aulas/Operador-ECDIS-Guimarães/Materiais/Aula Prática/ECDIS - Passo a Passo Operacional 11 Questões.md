
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

## 1. Configurar ECDIS sabendo que o comprimento do navio é de 40 metros, calado 5m e sua gyro está inoperante.


Verificar os sensores e selecionar a agulha Magnética.

```text
Task List → Navigation → Heading → Magnetic
```

Selecionar:

```text
MAGNETIC
```

[[#Índice]]

## 1.1 Adicionar comprimento do navio 40 metros


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


## 1.2 Adicionar parâmetros de calado (Safety Contour e Safety Deep) 


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

## 1.3 Adicionar parâmetros de calado (Shallow Contour e Deep Contour) 

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

## 2. — Traçar derrota da posição do navio até 50°32.699' N / 005°02.249' W, com no mínimo 10 Way Points.


```text
→ Task List → Advanced Plannig -> New
```

### Primeiro ponto

Na tela do mapa:

```text
A partir da posição do navio no momento
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


___

## Passo 3 — Nomear os principais Way Points

Na lista de pontos:

### Primeiro ponto

```text
→ Task List → Advanced Plannig -> Selecionar WP desejando
````

Selecionar WP desejado, da um duplo clique
→ Renomear 
→ Exemplo: Través Cabo Frio.
→ **ENTER**
→ **SALVAR**

[[#Índice]]

---

## 4. Checar a derrota e nomeá-la


## 4.1 Checar a derrota 


```text
→ Task List → Advanced Plannig -> Check Route -> Play Check Route
````

![[Pasted image 20261005173346.png]]

Conferir se os alarmes gerados não impedem a navegação.

-  Sem áreas rasas
    
-  Sem áreas proibidas
    
-  Sem perigos
    

## 4.1 Nomear a derrota 

Após checar toda rota, nomear no campo determinado e da **ENTER**.

Depois:

```text
→ Clicar em SALVE
```

[[#Índice]]

---

## 5. Suspender em 10/04/2025 às 1730 UTC, velocidade de 8 nós, aguardar 1 h no WPT 5 e determinar a ETA no destino

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
> 3. Selecione **Clears Fill**.
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

## 6. Inserir 2 pontos de referência

Acessar:

```text
→ Task List → Advanced Plannig -> REF. PTS
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

____

## Passo 7 — Ativar os vetores do navio (CONFIRMAR)






---

## 8. Adiquiri alvos no AIS e ARPA  e monitorá-los no ECDIS (CONFIRMAR)

```text
Configurações
→ Sensores
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

## 9. Configurar Safety Frame

```text
Task List → Monitoring - Aba Safety Alarms → Safety Frame
```


![[Pasted image 20261005180237.png]]

[[# Índice]]

---

## 10. Verificar altura da maré na chegada

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

## 11. Enviar mensagem AIS para um navio próximo, a fim de realizar uma experiência com o equipamento

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

## 12. Registrar na carta a recomendação do comandante para atenção a navegação na zona de separação de tráfego (Confirmar) 

- Ferramenta MAPS.





[[#Índice]]


____

## 13. Inserir um aviso de exercício de tiro da Royal Navy, com área circular de 5 NM com centro em 50°21.274' N  / 006°33.831' W (Confirmar) 

- Ferramenta Man Corr



[[#Índice]]

