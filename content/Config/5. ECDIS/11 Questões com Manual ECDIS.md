As **11 questões específicas de Planejamento e Monitoramento de Derrota**.

Referência principal o **Navi-Sailor 4000 ECDIS User Manual v. 3.02.350, September 2025**.

Onde o manual não fornece informação suficiente para determinar um valor, vou deixar isso explicitamente indicado, sem inventar o parâmetro.

# ECDIS — 11 QUESTÕES

## Planejamento e Monitoramento de Derrota

---

# 1. Configurar o ECDIS — navio 40 m, calado 5 m e gyro inoperante

### Objetivo

Configurar os dados básicos do navio e preparar o ECDIS para a situação em que o **gyro está inoperante**, mantendo uma fonte válida de posicionamento.

### Dados da questão

- Comprimento do navio: **40 m**
    
- Calado: **5 m**
    
- Gyro: **inoperante**
    

### Caminho principal

**Control Panel / Sensors / Positioning**

e, para os parâmetros de segurança:

**Tasks List → Monitoring → Safety alarms → Safety parameters**

### Procedimento

**1. Configurar o calado**

O manual utiliza o parâmetro **Draught** nos dados da rota/voyage plan. O procedimento consiste em selecionar o campo correspondente e inserir o valor do calado.

Neste exercício:

> **Draught = 5 m**

**2. Configurar o comprimento do navio**

O manual informa que o **Ship Length** é utilizado pelo sistema e que esse valor é especificado na configuração do sistema. A documentação detalhada dessa configuração está no **Installation Guide**, e não no User Manual.

Neste exercício:

> **Ship Length = 40 m**

**3. Verificar o posicionamento**

No painel dos sistemas de posicionamento, selecione a fonte disponível como **PRIM**.

O manual define:

- **PRIM** = sistema primário de posicionamento;
    
- **SEC** = sistema secundário de posicionamento.
    

Se o simulador possuir **DGPS/GPS 1**, essa é a fonte que deve ser verificada como posicionamento primário disponível.

**4. Gyro inoperante**

Não tentar selecionar o gyro como fonte válida de heading se ele está declarado inoperante.

O manual também possui modo **DR**, no qual o operador pode definir o DR como fonte primária ou secundária e inserir a posição atual.

### Resultado esperado

- Ship Length = **40 m**
    
- Draught = **5 m**
    
- Posicionamento válido selecionado como **Primary**
    
- Gyro identificado como **inoperante**, não utilizado como fonte válida de heading.
    

### Atenção

A questão **não fornece UKC** nem uma política de segurança que permita calcular numericamente um Safety Contour. Portanto, **não vou atribuir automaticamente um valor ao Safety Contour apenas porque o calado é 5 m**.

O próprio manual define Safety Contour como o limite entre água segura e insegura e Safety Depth como uma profundidade definida pelo navegador, por exemplo, calado + UKC.

### Referência

**Manual — págs. 67–75 / 142–143**

---

# 2. Traçar derrota da posição do navio até 50°32.699' N / 005°02.249' W, com no mínimo 10 Way Points

### Objetivo

Criar uma derrota iniciando na posição atual do navio e terminando nas coordenadas fornecidas, utilizando **pelo menos 10 WPTs**.

### Caminho

**Tasks List → Route Planning**

### Procedimento

1. Abrir **Route Planning**.
    
2. Selecionar **New**.
    
3. O ECDIS apresenta o cursor gráfico e a janela **Place First Point**.
    
4. Posicionar o primeiro ponto na posição atual do navio.
    
5. Clicar com o botão esquerdo.
    
6. O primeiro WPT será criado como **WPT 0**.
    
7. Posicionar o cursor no próximo ponto.
    
8. Clicar para criar o próximo WPT.
    
9. Repetir o procedimento até possuir **no mínimo 10 WPTs**.
    
10. Fazer o último WPT coincidir com:
    

> **50°32.699' N**  
> **005°02.249' W**

O manual confirma que o primeiro ponto recebe o número **0**, os pontos seguintes são numerados sequencialmente e o procedimento pode ser repetido quantas vezes forem necessárias.

### Resultado esperado

Uma rota gráfica ligando:

**posição do navio → WPT 1 → WPT 2 → ... → WPT 10 ou superior → destino**

com o último WPT nas coordenadas determinadas.

### Atenção

A questão estabelece **mínimo de 10 WPTs**, portanto não basta colocar apenas 10 pontos contando ou não o WPT 0 sem verificar a convenção usada pelo simulador.

No manual, o primeiro ponto é explicitamente **WPT 0**.

### Referência

**Manual — págs. 262–264**

---

# 3. Nomear os principais WPT

### Objetivo

Atribuir nomes aos WPTs considerados principais e permitir sua identificação durante o planejamento e monitoramento.

### Caminho

**Tasks List → Route Planning → Waypoints table**

### Procedimento

1. Abrir a tabela de WPTs.
    
2. Localizar a coluna **Name**.
    
3. Selecionar o WPT desejado.
    
4. Dar duplo clique no campo **Name**.
    
5. Digitar o nome.
    
6. Pressionar **ENTER**.
    
7. Repetir para os WPTs principais.
    

O manual confirma que a tabela possui as colunas **WPT, Name, Position, Leg Type, Leg, Total Distance, X PORT/X STBD e Turn Radius**.

Para inserir o nome:

> selecionar **Name → duplo clique → digitar → ENTER**.

### Resultado esperado

Os WPTs principais passam a apresentar seus respectivos nomes na tabela.

Também é possível mostrar os nomes na carta por meio de:

**Show → Waypoints names**

O manual indica que essa opção permite mostrar os nomes dos WPTs na carta.

### Atenção

A questão não especifica **quais** WPTs são considerados principais nem quais nomes devem ser utilizados. Portanto, no exercício, use os WPTs designados pelo instrutor/simulador.

### Referência

**Manual — págs. 264–267**

---

# 4. Checar a derrota e nomeá-la

### Objetivo

Executar a verificação de segurança da derrota e posteriormente salvar a rota com um nome identificável.

### Caminho

**Tasks List → Route Planning → Check route**

### Procedimento

**1. Carregar/selecionar a rota**

Certifique-se de que a rota criada está carregada no Route Planning.

**2. Abrir Check route**

Selecionar:

> **Check route**

**3. Escolher o critério de carta**

No grupo **Safety options**, selecionar:

- **Best scale**, ou
    
- **All scales**
    

conforme o exercício.

**4. Executar a verificação**

Acionar **Check route**.

O ECDIS verifica a rota procurando perigos à navegação.

**5. Analisar o resultado**

O sistema informa se foram encontrados perigos.

Caso encontre um perigo:

1. Selecionar o perigo;
    
2. Visualizá-lo na carta;
    
3. Se necessário, utilizar **WPT Editor**;
    
4. Alterar a rota;
    
5. Fazer nova verificação.
    

O manual informa que, após alteração de um WPT, os trechos próximos são automaticamente verificados novamente.

**6. Nomear a derrota**

Depois de concluir a verificação, retornar à área de salvamento da rota.

Inserir o nome desejado no campo de nome e pressionar:

> **Save**

O manual especifica que o nome da rota é inserido no campo de nome antes de pressionar **Save**.

### Resultado esperado

- Rota verificada;
    
- Resultado da checagem analisado;
    
- Rota salva;
    
- Rota identificada pelo nome escolhido.
    

### Atenção

**Checar a rota não significa apenas apertar Check Route e ignorar o resultado.** Os perigos encontrados devem ser analisados.

Além disso, o manual permite escolher entre **Best scale** e **All scales** para a verificação.

### Referência

**Manual — págs. 285–289**

---

# 5. Configurar o Schedule: suspender em 10/04/2025 às 1730 UTC, velocidade de 8 nós, aguardar 1 h no WPT 5 e determinar a ETA no destino

### Objetivo

Criar um Schedule para a rota, considerando:

- Data: **10/04/2025**
    
- Hora: **1730 UTC**
    
- Velocidade: **8 kn**
    
- Permanência no WPT 5: **1 hora**
    
- Determinar ETA no destino.
    

### Caminho

**Route Planning → Schedule calculation → Create Schedule**

### Procedimento

1. Carregar a rota.
    
2. Abrir a tabela do Schedule.
    
3. Selecionar **Schedule calculation**.
    
4. Pressionar **Create Schedule**.
    
5. Inserir os parâmetros nos WPTs.
    

O manual descreve o procedimento de criação do Schedule e permite inserir **ETA, Stay, Time zone, ETD e Speed** para os WPTs.

### Configuração do exercício

No ponto inicial:

> **10/04/2025 — 1730 UTC**

Na velocidade:

> **8 kn**

No:

> **WPT 5 → Stay = 1:00 h**

O ECDIS utiliza os dados da rota e do Schedule para calcular os tempos seguintes.

### ETA no destino

Depois de inserir os dados, verificar a ETA calculada para o último WPT.

Durante o monitoramento, o Route Data / Schedule apresenta informações como ETA, TTG e PTA.

### Resultado esperado

O ECDIS deverá apresentar:

> **ETA do último WPT = valor calculado pelo Schedule**

### Atenção importante

**Não é possível determinar numericamente a ETA apenas com os dados escritos na questão**, porque a ETA depende das distâncias dos WPTs que serão efetivamente traçados.

Portanto, a resposta operacional correta é **configurar o Schedule e ler a ETA calculada pelo ECDIS**.

### Referência

**Manual — págs. 292–294**

---

# 6. Inserir 2 pontos de referência

### Objetivo

Adicionar dois **Reference Points** associados à derrota.

### Caminho

**Tasks List → Route Planning → Ref. points**

### Procedimento

1. Abrir **Route Planning**.
    
2. Selecionar **Ref. points**.
    
3. Selecionar o WPT ao qual o ponto de referência será associado.
    
4. O marcador aparece na carta.
    
5. Posicionar o marcador no ponto de referência desejado.
    
6. Confirmar com o botão esquerdo.
    
7. Repetir para o segundo ponto.
    

O manual especifica que, ao utilizar **Ref. points**, o marcador aparece na carta associado ao WPT selecionado; depois pode ser deslocado para o novo ponto de referência.

Quando criado, o ponto aparece na carta como **dois círculos azuis**, ligados ao WOL por uma linha tracejada, com bearing/distance indicados.

### Resultado esperado

Dois pontos de referência configurados e associados aos respectivos WPTs.

### Atenção

O manual permite também o uso de **Snap to object**, que pode associar automaticamente o ponto a um objeto quando este estiver suficientemente próximo.

### Referência

**Manual — págs. 299–303**

---

# 7. Ativar os vetores do navio

### Objetivo

Exibir graficamente os principais vetores relacionados ao movimento do próprio navio.

### Caminho

**Tasks List → Monitoring → Route Monitoring**

### Procedimento

Na área **Ship**, habilitar:

- **Headline**
    
- **COG vector**
    
- **HDG vector**
    

O manual descreve exatamente esses três controles:

- **Headline** → linha do aproamento;
    
- **COG vector** → vetor de movimento sobre o fundo;
    
- **HDG vector** → vetor relativo à água, baseado em log speed e heading.
    

### Configuração complementar

Para configurar o comprimento dos vetores:

**Control Panel → Vectors**

Selecionar o comprimento desejado.

O manual informa que o comprimento pode ser definido por tempo, em minutos, ou como **Fixed**.

### Resultado esperado

Na carta deverão aparecer os vetores configurados do próprio navio.

### Atenção — importante nesta questão

Como a Questão 1 estabelece **gyro inoperante**, o **HDG vector pode não estar disponível de forma válida**, dependendo da configuração/simulação.

Não devemos fingir que um gyro inoperante fornece heading válido.

O **COG vector**, por outro lado, é relacionado ao movimento sobre o fundo.

### Referência

**Manual — págs. 47–48**

---

# 8. Adquirir alvos no AIS e ARPA e monitorá-los no ECDIS

### Objetivo

Apresentar e acompanhar alvos provenientes de **AIS** e **ARPA** no ECDIS.

### Caminho

**Control Panel → Sensors**

e depois:

**Tasks List → Targets**

### Procedimento

**1. Ativar AIS**

Verificar/ativar AIS na área de sensores.

**2. Ativar ARPA**

Ativar **ARPA A** e/ou **ARPA B**, conforme o simulador.

**3. Abrir Targets**

Selecionar:

> **Targets**

**4. Mostrar os alvos**

Na página **Target Table**, o ECDIS permite ligar a apresentação das fontes:

- ARPA A/B
    
- AIS
    
- Own
    

O manual confirma esses controles.

**5. Monitorar**

Na carta, observar os alvos.

É possível também selecionar um alvo na tabela para localizá-lo visualmente na carta; o alvo selecionado é destacado no Chart Panel.

### Informações que podem ser acompanhadas

A Target Table apresenta, entre outras:

- Name
    
- CPA
    
- TCPA
    
- COG
    
- SOG
    
- Range
    
- Bearing.
    

### Resultado esperado

Alvos AIS e ARPA visíveis e acompanhados no ECDIS.

### Atenção

**Aquisição/ativação do alvo não é a mesma coisa que simplesmente receber AIS.** O manual diferencia o sleeping AIS target do target ativado; o target ativado permite apresentação gráfica adicional.

### Referência

**Manual — págs. 309–321 e 335–348**

---

# 9. Configurar o Safety Contour

### Objetivo

Configurar o limite de profundidade utilizado pelo ECDIS para distinguir águas seguras de águas inseguras.

### Caminho

**Tasks List → Monitoring → Safety alarms → Safety parameters**

### Procedimento

1. Abrir **Safety parameters**.
    
2. Localizar o grupo **Safety Parameters**.
    
3. Selecionar **Safety Contour**.
    
4. Inserir o valor determinado para o exercício.
    
5. Confirmar.
    

O manual define Safety Contour como o contorno escolhido pelo navegador para distinguir visualmente água segura e insegura.

### Relação com o calado

Para esta prova:

> **Calado = 5 m**

Mas o valor final do Safety Contour **não pode ser calculado somente a partir desse dado**.

O manual define:

> Safety Contour = limite entre águas seguras e inseguras.

e:

> Safety Depth = profundidade definida pelo navegador, podendo ser, por exemplo, calado + UKC.

### Resultado esperado

O Safety Contour escolhido aparece configurado nos parâmetros de segurança e passa a ser utilizado pelo ECDIS na apresentação/monitoramento de segurança.

### Atenção

A questão não fornece:

- UKC;
    
- política da empresa;
    
- valor solicitado pelo instrutor;
    
- contorno disponível na ENC.
    

Portanto, **não vou inventar “Safety Contour = X m”**.

Se o simulador/professor fornecer o valor, esse é o valor que deve ser inserido.

### Referência

**Manual — págs. 142–144**

---

# 10. Verificar a altura da maré local para a hora de chegada

### Objetivo

Determinar a altura da maré no local de destino no horário previsto de chegada.

### Dados

Destino da questão:

> **50°32.699' N / 005°02.249' W**

O horário de chegada deve ser obtido no **Schedule da Questão 5**.

### Caminho

**Tasks → Tides → Place → Diagram**

### Procedimento

**1. Abrir Tides**

Selecionar:

> **Tasks → Tides**

**2. Selecionar Place**

Abrir a aba **Place**.

**3. Selecionar o ponto de referência de maré**

O manual oferece três métodos:

- **By name**
    
- **All Places**
    
- **By cursor**
    

Para este exercício, como temos as coordenadas do destino, o método mais interessante é **By cursor**, procurando o ponto de referência próximo ao destino.

**4. Abrir Diagram**

Após selecionar o ponto de referência, o ECDIS apresenta a curva de maré.

**5. Inserir a data**

Na aba **Diagram**, selecionar a data.

**6. Localizar a hora da ETA**

Ativar:

> **Cursor Data**

Posicionar o cursor sobre a curva na hora correspondente à ETA.

O sistema apresenta o valor da altura da maré na janela de informações.

### Resultado esperado

Obter:

> **Hora da ETA → altura da maré correspondente**

### Atenção

A altura **não pode ser determinada agora apenas com as coordenadas do destino**, porque depende de:

1. rota criada;
    
2. Schedule;
    
3. ETA calculada;
    
4. ponto de referência de maré selecionado;
    
5. dados de maré disponíveis na base do ECDIS.
    

Portanto, nesta questão, a sequência correta é:

**Route → Schedule → ETA → Tides → referência local → hora da ETA → altura.**

### Referência

**Manual — págs. 353–357**

---

# 11. Enviar uma mensagem AIS para um navio próximo, a fim de realizar experiência com o equipamento

### Objetivo

Selecionar um navio AIS próximo e enviar uma mensagem de teste/experiência utilizando o sistema AIS.

### Caminho

**Tasks List → AIS → Messaging**

### Procedimento

**1. Verificar que os alvos AIS estão sendo apresentados**

O manual exige que a apresentação dos alvos AIS esteja ligada antes da transmissão da mensagem.

**2. Abrir Messaging**

Selecionar:

> **AIS → Messaging**

**3. Criar mensagem**

Pressionar:

> **Create Message**

O manual apresenta as opções de mensagem **Safety Text** e **Normal Text**.

Como a questão diz apenas:

> “enviar uma mensagem AIS para um navio próximo, a fim de realizar experiência com o equipamento”

a opção mais coerente é uma **Normal Text**, salvo instrução diferente do instrutor.

**4. Selecionar o navio**

Utilizar:

> **To target with MMSI**

e selecionar o alvo desejado.

O manual permite inserir diretamente o MMSI ou selecionar o alvo na carta para que o MMSI seja preenchido automaticamente.

**5. Digitar a mensagem**

Exemplo para exercício:

> **TEST MESSAGE — ECDIS AIS TEST**

**6. Enviar**

Pressionar:

> **Send**

**7. Canal**

Selecionar:

> **Auto**

O manual indica **Auto** como opção geralmente recomendada.

**8. Fechar**

Pressionar:

> **Close**

### Resultado esperado

A mensagem deve aparecer na tabela de mensagens enviadas com um dos estados possíveis, como:

- **Waiting**
    
- **Sent**
    
- **Delivered**
    
- **Failed**.
    

### Atenção

A questão exige enviar **para um navio próximo**, portanto não usar **To All**.

O procedimento correto é selecionar **To target with MMSI** e direcionar a mensagem ao alvo específico.

### Referência

**Manual — págs. 324–327**

---

# RESUMO OPERACIONAL — 11 QUESTÕES

|Nº|Tarefa|Caminho principal|Manual|
|--:|---|---|--:|
|**1**|Configurar navio 40 m / calado 5 m / gyro inoperante|Sensors / Safety Parameters|**67–75 / 142–143**|
|**2**|Criar derrota ≥10 WPT até coordenadas|Route Planning → New|**262–264**|
|**3**|Nomear WPTs|Route Planning → Waypoints|**264–267**|
|**4**|Checar e nomear derrota|Route Planning → Check route → Save|**285–289**|
|**5**|Schedule / 1730 UTC / 8 kn / 1 h WPT5 / ETA|Schedule calculation|**292–294**|
|**6**|2 Reference Points|Route Planning → Ref. points|**299–303**|
|**7**|Vetores do navio|Monitoring → Route Monitoring|**47–48**|
|**8**|AIS + ARPA / monitorar alvos|Targets|**309–321 / 335–348**|
|**9**|Safety Contour|Monitoring → Safety alarms → Safety parameters|**142–144**|
|**10**|Maré na hora da chegada|Tasks → Tides → Place → Diagram|**353–357**|
|**11**|Mensagem AIS para navio próximo|AIS → Messaging|**324–327**|

## Sequência que eu usaria no simulador

A ordem mais lógica para executar as 11 é:

**1 → 2 → 3 → 4 → 6 → 5 → 7 → 8 → 9 → 10 → 11**

Porque existe uma dependência importante:

**Questão 2 cria a rota → Questão 3 identifica os WPT → Questão 4 verifica → Questão 6 adiciona referências → Questão 5 calcula a ETA → Questão 10 usa essa ETA para determinar a maré.**

E há três pontos que eu deixaria especialmente marcados para estudo:

> **Q4 — Check Route**  
> **Q5 — Schedule / ETA**  
> **Q10 — Tide na hora da ETA**

Essas três questões dependem diretamente da rota que você efetivamente construir no simulador.