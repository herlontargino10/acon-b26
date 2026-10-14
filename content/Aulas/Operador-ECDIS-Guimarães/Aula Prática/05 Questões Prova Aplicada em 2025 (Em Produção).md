## 1ª Questão — 6,0 pontos

Sabendo-se que o seu calado é de **20 metros** e o comprimento é **125 metros**, seu fuso é **08E**, configure sua estação e faça o que se pede:


> [!danger] Configuração do calado  
> Antes de prosseguirmos para a letra **A**, vamos configurar os parâmetros da embarcação. Conforme informado no enunciado, o **calado do navio é de 20 metros**.

## Adicionar parâmetros de calado (Safety Contour e Safety Deep) 

Acessar:

```text 
→ Task List → Monitoring → Aba Safety Alarms → Aba Safety Meters
```

- Calado: **20 m** 

> [!warning] Atenção — Parâmetros de Segurança
> O **calado do navio indicado pelo professor é 20 m**.
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
> `1,2 × 20 = 24 m`
>
> **Resultado: 24,0 m**
>
> ---
>
> **Safety Depth**
>
> `1,5 × Calado`
>
> `1,5 × 20 = 30 m`
>
> **Resultado: 30 m**
>
> ---

![[20261005_094824.jpg]]

## Adicionar parâmetros de calado (Shallow Contour e Deep Contour) 

Acessar:

```text 
→ Task List → Charts → Aba ENC
```


> [!warning] Atenção — Parâmetros de Segurança
> O **calado do navio indicado pelo professor é 20 m**.
>
> Esse valor será utilizado para calcular os parâmetros de segurança da carta.
>
> ### Cálculos
>
> **Shallow Contour**
>
> `1,1 × Calado`
>
> `1,1 × 20 = 22 m`
>
> **Resultado: 22 m**
>
> ---
>
> **Deep Contour**
>
> `2 × Calado`
>
> `2 × 20 = 40,0 m`
>
> **Resultado: 40,0 m**

![[20261005_094802.jpg]]

### a) Planejar a derrota, com no mínimo oito waypoints, em direção ao fundeadouro, sabendo que a região é polar e existe intensa área de pesca nas proximidades.

Acessar:

```text
→ Task List → Advanced Plannig → New
```

### Primeiro ponto

Na tela do mapa:

```text
Clicar em cima da posição do navio e ir construindo os waypoints
```

→ **Adicionar utilizando o cursor mouse.** 

### Ponto de chegada

```text
Fundeadouro
```


A rota aparece ligando todos os pontos.

```text
→ Salvar
```

___

> [!danger] Configuração do comprimento do navio e do raio de guinada
> 
> Ainda com base no enunciado da questão, devemos considerar que a embarcação possui **125 metros de comprimento**.
> 
> Como não há uma opção específica para inserir o comprimento do navio, o professor orientou que essa informação seja registrada na coluna **TURN RADIUS**.
>
> Essa configuração será realizada após a criação dos waypoints, quando as colunas correspondentes estiverem disponíveis para a inserção dos dados da rota.
> 
> Com os waypoints criados e ainda na função **Advance Planning**, vamos inserir a informação na coluna **TURN RADIUS**, seguindo a orientação do professor e o procedimento adotado para o exercício.
> 
> Para isso, o valor calculado deverá ser inserido na coluna **TURN RADIUS**. Caso a aba correspondente não esteja aberta, siga o caminho indicado abaixo para acessá-la e realizar as configurações necessárias.

```text
→ Task List → Advanced Plannig → Schedule Calculation → Create Schedule → Schedule Calculation Botão Play
````


> [!question] Como determinar o valor que devo inserir no campo Turn Radius?
> 
> Para determinar o valor a ser inserido no campo **TURN RADIUS**, utilize a seguinte fórmula:
> 
> **Turn Radius = (Comprimento do navio × 3) ÷ 1852**
> 
> **Exemplo — navio de 125 m:**
> 
> `(125 × 3) ÷ 1852 = 0,20 nm`
> 
> Portanto, para uma embarcação com **125 metros de comprimento**, o valor calculado é aproximadamente **0,20 milhas náuticas (MN)**.
>

### Vídeo de apoio — Configuração do Turn Radius

<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/Hsdd9uL6gHU?si=2wpTYRx979HIDfMX"
  title="Demonstração prática do ECDIS"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>

___

4. **Configuração do fuso horário**

Ainda na função **Advance Planning**, vamos configurar o fuso horário solicitado no enunciado da questão. Para isso, inseriremos o valor **08E** na coluna **Time Zone**.


### Vídeo de apoio — Adicionar Fuso Horário no Schedule

<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/vT0E5EUg658?si=MKYQmAt-Xf6iVNQL"
  title="Demonstração prática do ECDIS"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>

### b) Schedule

Construir e preencher o schedule, sabendo que o suspender está previsto para hoje às **15:00Z**. A duração da viagem será de **5 horas**.

### Vídeo de apoio — Configurar Schedule

<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/Ki6rcvLMj8E?si=R0hCyyw1_CZm1kjH"
  title="Demonstração prática do ECDIS"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>


### c) Checagem e monitoramento da derrota

Checar e monitorar uma derrota, utilizando a carta em **Head up** e movimento **verdadeiro**.

Acessar: 

```text
→ Task List → Advanced Plannig → Check Route → Play Check Route
````

![[Pasted image 20261005173346.png]]

Conferir se os alarmes gerados não impedem a navegação.
![[20261007_100726.jpg]]

Com a derrota planejada, verificada e os alarmes do **Check Route** devidamente conferidos, podemos prosseguir para a etapa de monitoramento. Essa função está disponível na mesma janela do **Advance Planning**.

Para iniciar o monitoramento da derrota, basta clicar em **Monitoring**.

![[Pasted image 20261014163023.png]]

Após ativar essa função, a rota planejada será exibida em **vermelho** na carta náutica.

### Vídeo de apoio — Configurar carta para Head Up e Movimento Verdadeiro

<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/NdCnq2KeyIA?si=2josj0X9GKIq7JBC"
  title="Demonstração prática do ECDIS"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>


_____

### d) Verificar e ajustar os alarmes para esta derrota.

```text
→ Task List → Advanced Plannig → Check Route → Play Check Route
````

![[20261007_100726.jpg]]
 

### e) Praticagem em São Luís

Informar a característica da praticagem em **“SÃO LUIS”** e se há serviços disponíveis nesse porto.




### f) Altura da maré no último waypoint

Quando estiver no último waypoint, qual será a altura da maré?

**Resposta:**

- Último waypoint:
- Data e hora consideradas:
- Altura da maré:
- Fonte / informação consultada:

> 

---

## 2ª Questão — 0,5 ponto

Determinar a distância entre dois pontos de terra, informar os pontos considerados.

**Resposta:**

- Ponto de terra 1:
- Ponto de terra 2:
- Distância determinada:
- Unidade:
- Procedimento / observações:


---

## 3ª Questão — 0,5 ponto

Enviar uma mensagem de segurança pelo AIS para estação com MMSI **25102024**.

**Registro da execução:**



---

## 4ª Questão — 2,0 pontos

O Comandante solicitou inserir na carta um aviso para chamá-lo quando o navio estiver no waypoint 3 e informou que recebeu um aviso rádio sobre um exercício de minagem a ser realizado pela Marinha do Brasil com área circular cujo centro é no waypoint 5 com raio de **0,8 MN**.

### a) Aviso para chamar o Comandante no waypoint 3

**Resposta / procedimento:**

- Tipo de aviso inserido:
- Waypoint associado:
- Configuração / mensagem do aviso:
- Resultado / observações:

> 

### b) Área de exercício de minagem

**Resposta / procedimento:**

- Centro da área: WP5
- Raio: 0,8 MN
- Objeto / área inserida na carta:
- Como a área foi representada:
- Resultado / observações:

> 

---

## 5ª Questão — 1,0 ponto

Faça o que se pede:

### a) Divisão da carta

Dividir a carta em duas, utilizando uma em **North up** e outra em **Course up**.

**Resposta / procedimento:**

- Configuração da primeira carta:
- Configuração da segunda carta:
- Resultado / observações:

> 

### b) Display noturno

Colocar a carta no display noturno.

**Resposta / procedimento:**

- Configuração selecionada:
- Resultado / observações:

---

