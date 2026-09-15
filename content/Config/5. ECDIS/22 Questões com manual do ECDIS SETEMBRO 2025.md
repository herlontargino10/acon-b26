
A base é o arquivo **“Prática - 22 Questões”** e o **Navi-Sailor 4000 ECDIS User Manual v. 3.02.350 — September 2025**. As 22 tarefas estão explicitamente listadas no material de prática.

---

# PRÁTICA — 22 QUESTÕES

## Navi-Sailor 4000 ECDIS v. 3.02.350 - SETEMBRO 2025
---

## BLOCO 1 — CONFIGURAÇÃO DO ECDIS

### 1. Modo de exibição

**Questão:**  
Selecionar o modo de exibição do display como **Custom**.

**Caminho no simulador:**

```text
TASK LIST
   ↓
CHART
   ↓
Display Category
   ↓
CUSTOM
```

**Resultado esperado:**  
O modo de apresentação passa para **Custom**.

**Manual:** **p. 114–115**.

Na p. 114 o manual manda pressionar **Display category** e selecionar **Custom**.

**Memorização:**

> **Chart → Display Category → Custom**

---

# 2. Camadas da carta

**Questão:** habilitar:

- Spot sounding to 15m
    
- Name
    
- Other Information
    

**Caminho indicado pela questão:**

```text
TASK LIST
   ↓
CHART
   ↓
LAYER
```

No manual, a configuração equivalente está na categoria **Custom**.

Na lista de objetos aparecem:

- **Other text** — inclui Names;
    
- **Spot soundings to** — mostra profundidades menores que o valor configurado;
    
- demais classes de informação da carta.
    

**Procedimento:**

```text
Display Category → Custom

☑ Spot soundings to
   → 15 m

☑ Other text / Names

☑ Other Information
   → conforme a nomenclatura apresentada no simulador
```

**Manual:** **p. 114–115**.

### Atenção

A expressão da questão **“Name / Other Information”** não aparece literalmente com a mesma redação em todo o trecho do manual. O manual utiliza **Other text**, dentro do qual inclui **Names**. Portanto, no simulador, siga os nomes que aparecem na interface.

---

# 3. Sensor primário de posição

**Questão:**  
Qual o sensor primário de posição?

**Caminho:**

```text
Painel de Controle
   ↓
Sensors / Ship Position
   ↓
PRIM
```

Na página 67 o manual explica que:

- **PRIM** seleciona a fonte como sistema primário;
    
- **SEC** seleciona a fonte secundária.
    

### Para conferir qual está selecionado

Depois de selecionar o PRIM:

```text
Display Panel
   ↓
Sensor Data/Status
   ↓
Primary Status
```

A p. 68 mostra os dados do sistema de posicionamento primário.

**Manual:** **p. 67–68**.

---

# 4. Criar e monitorar uma rota com 5 WPT

**Questão:**

> Crie uma rota com 5 WPT.  
> Monitore CRS, XTD, BTW, DTW etc.

## PARTE A — criar a rota

**Caminho:**

```text
Route Planning
   ↓
New
```

O manual inicia a criação na p. 262:

```text
New
→ posicionar WPT 0
→ botão esquerdo
→ posicionar WPT 1
→ botão esquerdo
→ repetir
```

Para 5 WPT:

```text
WPT 0
WPT 1
WPT 2
WPT 3
WPT 4
```

Depois:

```text
botão direito 2x
→ sair do modo de criação
```

### PARTE B — visualizar dados da rota

Na p. 267 o manual mostra as opções de apresentação:

- Waypoints names
    
- Turns
    
- Cross track distances
    
- Reference points
    
- Wheel over lines
    
- Remarks
    
- **CRS/DIST/SPD**
    

### PARTE C — Route Monitoring

A p. 95 mostra o grupo **Waypoints**, incluindo seleção do próximo WPT, XTL, Radius etc.

### Importante sobre BTW/DTW

A questão usa **BTW/DTW**, mas o manual desta versão emprega nomenclaturas como:

- **BWW** — Bearing Waypoint to Waypoint;
    
- **BWOL** — Bearing to Wheel Over Line;
    
- **DWOL** — Distance to Wheel Over Line;
    
- **CRS/DIST/SPD**.
    

Essas abreviações estão definidas no próprio manual.

**Manual principal:** **p. 262–267**  
**Monitoramento:** **p. 95–103**

---

# BLOCO 2 — SENSORES E ALVOS

# 5. Ativar todos os sensores disponíveis

A questão pede:

```text
DGPS 1
Gyro 1
Dlog 1
Echosounder 1
```

## DGPS 1

```text
Navigation / Sensors
→ Ship Position
→ DGPS 1
→ PRIM ou seleção correspondente
```

**p. 67–68.**

## Gyro 1

```text
Sensors
→ Heading
→ GYRO 1
```

**p. 85.**

## Dlog 1

```text
Sensors
→ Speed
→ DLOG 1
```

**p. 86.**

## Echosounder 1

```text
Sensors
→ Echosounder
→ ECHOSOUNDER 1
```

Na p. 88 o manual diz explicitamente que **ECHOSOUNDER 1** pode ser selecionado como fonte de profundidade e que sua leitura passa a ser utilizada nos cálculos do sistema.

### Resumo

|Sensor|Página|
|---|--:|
|DGPS 1|**67**|
|Gyro 1|**85**|
|Dlog 1|**86**|
|Echosounder 1|**88**|

---

# 6. Habilitar sensores

**Questão:**

- AIS
    
- ARPA A
    
- ARPA B
    

## AIS

No Control Panel:

```text
Sensors Window
→ AIS
```

A janela Sensors possui explicitamente o controle **AIS** para ligar a apresentação dos alvos AIS.

**p. 25.**

## ARPA

```text
Sensors Window
→ ARPA
→ selecionar fonte
```

O manual também permite selecionar **ARPA A(B)** no Target panel.

**p. 310.**

### Resumo

```text
AIS       → p. 25 / 319
ARPA A/B  → p. 310
```

---

# 7. Habilitar alvos

**Questão:**

```text
Targets
→ Show Targets
→ ARPA A
→ ARPA B
→ AIS Tracks
```

## ARPA A/B

```text
Targets
→ Target Table
→ Show Target
→ ARPA A(B)
```

O manual confirma o procedimento na seção ARPA.

**p. 310–311.**

## AIS

```text
Targets
→ Target Table
→ Show Target
→ AIS
```

**p. 319.**

## AIS Tracks

```text
Show Target
→ Tracks
```

O manual especifica que o botão **Tracks** liga a apresentação dos rastros dos alvos na carta.

**p. 321.**

### Resultado esperado

Os alvos aparecem no **Chart panel**, e os parâmetros de movimento são apresentados na tabela de alvos.

---

# 8. Monitorar a área

**Questão:**

> Monitore a área visualmente. Observe os alvos habilitados acima.

Aqui não há uma nova configuração específica.

Depois das questões 6 e 7, a tarefa é **observar o Chart panel**.

Verifique visualmente:

```text
Own ship
+
ARPA A
+
ARPA B
+
AIS targets
+
AIS Tracks
```

A p. 16 descreve o Chart Area como a área onde são apresentados, entre outros, o navio próprio e os objetos AIS.

**Manual:** **p. 16 + 310–321.**

### Resultado esperado

Não é necessário abrir outra configuração. É uma questão de **monitoramento visual dos alvos já habilitados**.

---

# BLOCO 3 — MONITORAMENTO DO NAVIO

# 9. Monitorar o navio

**Questão:**

Habilitar:

- Headline
    
- COG vector
    
- HDG vector
    

**Caminho:**

```text
TASK LIST
→ Monitoring
→ Route Monitoring
→ Ship
```

Marcar:

```text
☑ Headline
☑ COG vector
☑ HDG vector
```

O manual confirma exatamente esses três controles na p. 47.

### Significado

- **Headline** = linha do heading do navio;
    
- **COG vector** = vetor de movimento sobre o fundo;
    
- **HDG vector** = vetor relativo à água.
    

**Manual:** **p. 47–48.**

---

# 10. Exibição do navio e vento

**Questão:**

> Exibir o navio como contorno, e não como símbolo.  
> Habilitar Wind vector.

**Caminho:**

```text
TASK LIST
→ Monitoring
→ Route Monitoring
```

### Navio

```text
Ship by...
→ Contour
```

### Vento

```text
Wind vector
→ selecionar modo necessário
```

O manual confirma que **Ship by…** permite selecionar:

- symbol;
    
- contour.
    

E também possui **Wind vector**.

**Manual:** **p. 48.**

---

# 11. Alinhamento do contorno

**Questão:**

> Alinhar o contorno do navio ao HDG vector.

**Caminho:**

```text
TASK LIST
→ Monitoring
→ Route Monitoring
→ Align by...
→ HDG
```

O manual confirma:

- **HDG** = orientação conforme o heading detector/gyro;
    
- **COG** = orientação conforme o vetor COG.
    

### Resultado esperado

O contorno do navio fica orientado pelo **HDG**.

**Manual:** **p. 48.**

---

# 12. Monitorar alarmes

**Questão:**

> Monitorar os alarmes durante a navegação:
> 
> - Safety Contour
>     
> - Safety Depth
>     

**Caminho:**

```text
TASK LIST
→ Monitoring
→ Safety Alerts
→ Safety Parameters
```

A p. 141 confirma a abertura da página **Safety Alerts**.

Na p. 143:

```text
Safety contour
→ inserir valor

Safety depth
→ inserir valor
```

e confirmar as alterações.

### Ponto crítico

O manual diz explicitamente:

> o alerta é gerado pelo **Safety contour**, não pelo valor de Shallow contour.

### Antigrounding

Na p. 144 existem os controles:

```text
☑ Safety contour
☑ Nav. hazard
☑ Highlight Danger
```

**Manual:** **p. 141–144.**

---

# 13. Configurar vetor do navio

**Questão:**

> Painel de controle / ... / min

**Caminho confirmado no manual:**

```text
Control Panel
→ Vectors
→ botão que mostra o comprimento atual
→ selecionar comprimento
```

A p. 48 explica que o botão **Vectors** abre a lista de comprimentos disponíveis e que o operador deve selecionar o comprimento necessário.

### Atenção

A questão que você recebeu **não especifica quantos minutos devem ser selecionados**.

Portanto, não vou inventar um valor. O manual confirma o procedimento, mas o valor específico precisa vir do exercício/simulador.

**Manual:** **p. 48.**

---

# 14. Alterar fuso horário para 3W

**Caminho:**

```text
TASK LIST
→ Config
→ Time Zone
→ Time zone
→ 3W
→ ENTER
```

O manual confirma que a página Time Zone contém:

- UTC time;
    
- Ship's time;
    
- Time zone.
    

E permite inserir o fuso na linha **Time zone**.

### Resultado

O horário do navio é recalculado de acordo com o novo fuso.

**Manual:** **p. 49.**

---

# 15. Exibir hora do navio

**Caminho:**

```text
Painel de Controle
→ Time Window
→ clicar no botão do relógio
```

A janela Time mostra:

```text
UTC
ou
Ship's time
```

O manual confirma que o botão do relógio alterna entre os dois modos.

### Portanto

**Questão 15 → p. 26.**

A seção geral de monitoramento de tempo começa na **p. 157**, mas para executar a troca no display a referência direta é a **p. 26**.

---

# BLOCO 4 — AIS E MENSAGENS

# 16. AIS no Conning

**Questão:**

> Ligue o AIS no Conning.  
> Botão UP / Nav. Aids.

Aqui precisamos separar o que está **confirmado neste manual** do que não está.

O manual confirma que o Conning Panel possui três vistas:

```text
Instruments
Route
Docking
```

e que ele é aberto pelo controle do Conning Panel.

Também diz explicitamente que a descrição das janelas do Conning está em:

> **Multifunctional Display. Navi-Sailor 4000 ECDIS (v. 3.02.350). Additional Functions, Chapter 3.**

### Portanto, para a prova:

```text
Conning
→ UP
→ Nav. Aids
→ AIS
```

é a sequência fornecida **na sua folha de prática**, mas **o manual User Manual que estamos analisando não documenta essa sequência específica**.

**Referência neste manual:** p. 39–40.  
**Referência necessária para confirmar o botão UP/Nav. Aids:** _Additional Functions_, Chapter 3.

Essa é uma das poucas questões em que não devemos misturar os dois manuais.

---

# 17. AIS no display da carta

**Caminho rápido:**

```text
Control Panel
→ Sensors
→ AIS
```

A janela Sensors possui o botão AIS para apresentar os alvos AIS.

### Procedimento detalhado

```text
TASK LIST
→ Targets
→ Target Table
→ Show Target
→ AIS
```

A p. 319 confirma esse procedimento e que os alvos passam a aparecer no Chart panel.

**Manual:** **p. 25 + 319.**

---

# 18. Mensagem de segurança para todos

**Questão:**

> Envie uma mensagem de segurança para todos.

**Caminho:**

```text
TASK LIST
→ AIS
→ Messaging
→ Create Message
→ Safety Text
```

O manual confirma exatamente essa sequência.

Depois:

```text
Safety Text
→ To All
```

A opção **To All** envia a mensagem para todos os navios na cobertura de rádio.

Depois:

```text
Text
→ escrever mensagem

Send
→ Auto
→ Close
```

### Resumo para decorar

```text
AIS
→ Messaging
→ Create Message
→ Safety Text
→ To All
→ escrever
→ Send
→ Auto
→ Close
```

**Manual:** **p. 324–327.**

---

# 19. Mensagem normal para um navio

**Caminho:**

```text
TASK LIST
→ AIS
→ Messaging
→ Create Message
→ Normal Text
```

Depois:

```text
To target with MMSI
→ inserir MMSI
```

O manual também permite selecionar o alvo diretamente na carta para obter o MMSI.

Depois:

```text
escrever mensagem
→ Send
→ Auto
→ Close
```

### Diferença fundamental

**Questão 18:**

```text
Safety Text
→ To All
```

**Questão 19:**

```text
Normal Text
→ To target with MMSI
```

**Manual:** **p. 324–327.**

---

# BLOCO 5 — NAVEGAÇÃO E PLANEJAMENTO

# 20. Orientação do comandante

**Questão:**

> Você recebeu a orientação do comandante para chamá-lo na entrada do canal. Insira essa informação na carta.

Para esta questão, a forma mais direta é inserir um **Text Object**.

### Caminho

```text
Manual Update
→ Add objects
→ Text
```

Depois:

```text
Text
→ escrever a orientação
```

A seção de objetos de texto permite colocar a informação que será apresentada na carta.

### Outra possibilidade: Remark da rota

Se a intenção do instrutor for associar a informação à perna da rota:

```text
Route Planning
→ Extra Data
→ Remarks
```

A p. 266 confirma que **Remarks** podem ser inseridas para a perna da rota.

E a p. 267 confirma que **Remarks** podem ser exibidas na carta.

### Minha orientação para a prova

Se a instrução for simplesmente:

> **“Insira essa informação na carta.”**

use:

```text
Manual Update
→ Add objects
→ Text
```

**Referência principal:** **p. 222–225** para User Chart Text Object.  
**Alternativa vinculada à rota:** **p. 266–267**.

---

# 21. Preencher o Schedule

Esta é uma das questões que exige mais atenção.

A questão fornece:

```text
Velocidade normal: 10 kn
Saída WP0: 1200Z
Fuso: 3W
Dentro do canal: máximo 4 kn
```

## Passo 1 — criar a rota

Primeiro a rota de 5 WPT precisa existir.

```text
Route Planning
→ Load route
```

## Passo 2 — Schedule

```text
Route Planning
→ Schedule calculation
→ Create Schedule
```

O manual confirma exatamente essa sequência.

## Passo 3 — preencher os dados

A tabela possui:

- ETA;
    
- Stay;
    
- Time zone;
    
- ETD;
    
- Speed.
    

### Para o exercício

No WP0:

```text
ETD = 1200Z
```

Nos trechos fora do canal:

```text
Speed = 10 kn
```

No(s) trecho(s) dentro do canal:

```text
Speed = 4 kn
```

O fuso:

```text
Time zone = 3W
```

### Depois

```text
Schedule Calculation
→ Calculate
```

O ECDIS calcula as células vazias.

### Ponto importante

A questão pede:

> “Determine a hora de chegada ao último WP.”

**Não é possível fornecer a hora numericamente apenas com os dados da folha**, porque a distância entre os 5 WPT e qual trecho está dentro do canal não estão especificados no texto da questão.

O procedimento correto é deixar o **ECDIS calcular o ETA** depois que a rota real de 5 WPT estiver criada.

**Manual:** **p. 292–294.**

---

# 22. Maré — Porto de Seattle

Esta questão possui **duas operações diferentes**:

1. determinar a altura da maré;
    
2. verificar as facilidades do porto.
    

A questão pede que a maré seja determinada **quando o navio estiver no último WP**, portanto a ETA calculada na questão 21 é necessária.

---

## 22A — Altura da maré

**Caminho:**

```text
TASKS
→ Tides
→ Place
```

Depois selecionar o ponto de referência.

O manual oferece três maneiras:

### Por nome

```text
By name
→ nome do reference point
→ ENTER
```

### Lista

```text
All Places
→ selecionar reference point
→ duplo clique
```

### Pelo cursor

```text
By cursor
→ Distance
→ Find
→ selecionar ponto
```

Depois:

```text
Diagram
→ selecionar Date
```

O sistema apresenta a **tidal curve** do ponto selecionado.

### Para a questão

Você precisa:

```text
Porto de Seattle
        ↓
selecionar referência de maré apropriada
        ↓
data da chegada ao WP final
        ↓
horário da chegada
        ↓
ler a altura da maré
```

### Atenção

O manual descreve **como obter a altura da maré**, mas o valor numérico de Seattle depende:

- do reference point selecionado;
    
- da data;
    
- do horário de chegada;
    
- dos dados de maré disponíveis no sistema.
    

Portanto, **não há um valor numérico que possa ser deduzido somente da folha das 22 questões**.

**Manual:** **p. 353–357.**

---

# 22B — Facilidades do Porto de Seattle

**Caminho:**

```text
TASKS
→ Ports
→ Port
```

Depois:

```text
Port
→ digitar Seattle
→ ENTER
```

O manual manda digitar as primeiras letras do nome ou selecionar o porto da lista.

Depois:

```text
Read information
```

A página apresenta as informações disponíveis sobre o porto.

**Manual:** **p. 368–369.**

---

# RESUMO OPERACIONAL DAS 22

Esta é a versão que eu recomendo ter aberta ao lado do simulador:

|#|Executar|Caminho|Página|
|---|---|---|--:|
|**1**|Custom|Chart → Display Category → Custom|**114**|
|**2**|Spot sounding 15m / Name / Other Information|Chart → Layer / Custom|**114–115**|
|**3**|Primary position sensor|Sensors → Ship Position → PRIM|**67–68**|
|**4**|Criar 5 WPT + monitorar|Route Planning → New|**262–267**|
|**5**|DGPS/Gyro/Dlog/Echo|Sensors → respectivas páginas|**67/85/86/88**|
|**6**|AIS/ARPA A/B|Sensors → AIS / ARPA|**25/310/319**|
|**7**|ARPA A/B + AIS Tracks|Targets → Show Target|**310–321**|
|**8**|Observar área|Chart panel|**16 + 310–321**|
|**9**|Headline/COG/HDG|Monitoring → Route Monitoring|**47–48**|
|**10**|Contour + Wind|Monitoring → Route Monitoring|**48**|
|**11**|Align by HDG|Monitoring → Route Monitoring|**48**|
|**12**|Safety Contour/Depth|Monitoring → Safety Alerts|**141–144**|
|**13**|Vector do navio|Control Panel → Vectors|**48**|
|**14**|Time Zone 3W|Config → Time Zone|**49**|
|**15**|Ship's time|Time Window → relógio|**26**|
|**16**|AIS Conning|UP → Nav. Aids → AIS*|**39–40***|
|**17**|AIS carta|Sensors → AIS|**25/319**|
|**18**|Safety message all|AIS → Messaging → Safety Text → To All|**324–327**|
|**19**|Normal message|AIS → Messaging → Normal Text → MMSI|**324–327**|
|**20**|Orientação comandante|Manual Update → Add objects → Text|**222–225**|
|**21**|Schedule|Schedule Calculation → Create Schedule|**292–294**|
|**22**|Maré + Seattle port|Tasks → Tides / Ports|**353–357 / 368–369**|

* **Questão 16:** a sequência **UP → Nav. Aids** está na folha de prática, mas não está documentada no User Manual que analisamos; o próprio manual remete o detalhamento do Conning para **Additional Functions, Chapter 3**.

---

# A sequência ideal para executar a prova

Eu faria as 22 **nesta ordem**, porque algumas dependem das anteriores:

```text
01  Custom
 ↓
02  Layers
 ↓
03  Primary sensor
 ↓
05  Sensors
 ↓
06  AIS / ARPA
 ↓
07  Targets
 ↓
08  Visual monitoring
 ↓
09  Ship vectors
 ↓
10  Contour + Wind
 ↓
11  Align HDG
 ↓
12  Safety alarms
 ↓
13  Vector length
 ↓
14  Time Zone 3W
 ↓
15  Ship's Time
 ↓
16  Conning AIS
 ↓
17  AIS on chart
 ↓
18  Safety message
 ↓
19  Normal message
 ↓
04  Create 5-WPT route
 ↓
20  Commander instruction
 ↓
21  Schedule
 ↓
22  Tide + Seattle Port
```

**Mas há uma alteração prática que eu faria:** colocar a **questão 4 (rota)** antes da 9–15, porque a rota passa a ser necessária para o monitoramento e para o Schedule.

A ordem operacional mais limpa fica:

```text
CONFIGURAÇÃO
1 → 2 → 3 → 5 → 6 → 7 → 8

ROTA / MONITORAMENTO
4 → 9 → 10 → 11 → 12 → 13 → 14 → 15

AIS
16 → 17 → 18 → 19

PLANEJAMENTO
20 → 21 → 22
```

Esse é o roteiro que eu usaria no simulador. A parte mais importante para decorar não são as páginas isoladamente, mas os **caminhos de menu**. As páginas servem como confirmação rápida quando você estiver estudando.