
### Enunciado

Uma chapa de madeira compensada, de dimensões 4 × 8 ft, é transportada no teto de um carro a 56 km/h, perfeitamente alinhada com o fluxo de ar.

Considere as propriedades do ar a 20 °C e 1 atm:

- Massa específica: $\rho=1,2\ kg/m^3$
    
- Viscosidade dinâmica: $\mu=1,8\times10^{-5}\ kg/(m\cdot s)$
    
- Comprimento: $L=2,44\ m$
    
- Largura: $b=1,22\ m$
    

Determine:

**a)** A espessura da camada limite no final da chapa.

**b)** O arrasto sobre a chapa considerando escoamento laminar.

**c)** O arrasto sobre a chapa considerando escoamento turbulento, admitindo madeira lisa. Compare os resultados.

---

## Resolução

### Dados iniciais

$$V=\frac{56}{3,6}=15,56\ m/s$$

### 1. Número de Reynolds

$$Re_L=\frac{\rho VL}{\mu}$$

$$Re_L=\frac{1,2(15,56)(2,44)}{1,8\times10^{-5}}$$

$$\boxed{Re_L=2,53\times10^6}$$

### a) Espessura da camada limite

$$\delta=\frac{5L}{\sqrt{Re_L}}$$

$$\delta=\frac{5(2,44)}{\sqrt{2,53\times10^6}}$$

$$\boxed{\delta=7,67\ mm}$$

### b) Arrasto laminar

Coeficiente de atrito:

$$C_{f,L}=\frac{1,328}{\sqrt{Re_L}}$$

$$\boxed{C_{f,L}=0,000835}$$

Área das duas faces:

$$A=2bL=2(1,22)(2,44)$$

$$A=5,9536\ m^2$$

Força de arrasto:

$$F_L=C_{f,L}\frac{\rho V^2}{2}A$$

$$F_L=0,000835\cdot\frac{1,2(15,56)^2}{2}\cdot5,9536$$

$$\boxed{F_L\approx0,72\ N}$$

### c) Arrasto turbulento

Coeficiente de atrito:

$$C_{f,T}=\frac{0,074}{Re_L^{1/5}}$$

$$C_{f,T}=\frac{0,074}{(2,53\times10^6)^{1/5}}$$

$$\boxed{C_{f,T}\approx0,00388}$$

Força de arrasto:

$$F_T=C_{f,T}\frac{\rho V^2}{2}A$$

$$F_T=0,00388\cdot\frac{1,2(15,56)^2}{2}\cdot5,9536$$

$$\boxed{F_T\approx3,36\ N}$$

### Comparação

$$\frac{F_T}{F_L}=\frac{3,36}{0,72}$$

$$\boxed{F_T\approx4,65F_L}$$

Portanto, o arrasto turbulento é aproximadamente 4,6 vezes maior que o laminar.

---

## Como calcular na calculadora científica

### 1. Potência negativa: exemplo $10^{-5}$

Na calculadora:

1. Digite `10`.
    
2. Aperte a tecla `xʸ` ou `^`.
    
3. Digite `5`.
    
4. Aperte a tecla `+/−` para colocar o expoente negativo.
    
5. Aperte `=`.
    

Resultado:

$$10^{-5}=0,00001$$

**Atenção:** a tecla `+/−` pode aparecer como `(-)` em algumas calculadoras.

### 2. Notação científica: exemplo $1,8\times10^{-5}$

O jeito mais rápido é utilizar a tecla `EXP`, `EE` ou `×10ˣ`.

Digite:

`1,8 → EXP → (-) → 5`

Resultado:

$$1,8\times10^{-5}=0,000018$$

Não digite o número 10 separadamente quando estiver usando a tecla EXP.

### 3. Raiz quadrada: exemplo $\sqrt{2,53\times10^6}$

Digite:

`√ ( 2,53 EXP 6 ) =`

Resultado aproximado:

$$\sqrt{2,53\times10^6}=1590,6$$

### 4. Potência fracionária: exemplo $(2,53\times10^6)^{1/5}$

Essa operação aparece no coeficiente turbulento.

Digite:

`( 2,53 EXP 6 ) → xʸ → 0,2 → =`

Por quê?

$$\frac{1}{5}=0,2$$

Resultado aproximado:

$$ (2,53\times10^6)^{0,2}=19,08$$

Depois:

$$C_{f,T}=\frac{0,074}{19,08}$$

$$C_{f,T}=0,00388$$

### 5. Como digitar o número de Reynolds inteiro

Para calcular:

$$Re_L=\frac{1,2(15,56)(2,44)}{1,8\times10^{-5}}$$

Digite:

`1,2 × 15,56 × 2,44 ÷ (1,8 EXP (-) 5) =`

Resultado:

$$Re_L\approx2,53\times10^6$$

---

## Macetes para a prova

|Operação|Como fazer|
|---|---|
|$10^{-5}$|`10 ^ (-) 5`|
|$1,8\times10^{-5}$|`1,8 EXP (-) 5`|
|$\sqrt{Re}$|Tecla `√`|
|$Re^{1/5}$|`Re ^ 0,2`|
|$Re^{1/2}$|`Re ^ 0,5`|
|$Re^{-1/2}$|`Re ^ (-) 0,5`|

### Sequência para memorizar

**REYNOLDS → ESPESSURA → COEFICIENTE → FORÇA → COMPARAÇÃO**

|Resultado|Valor aproximado|
|---|---|
|Reynolds|$2,53\times10^6$|
|Espessura laminar|7,67 mm|
|Arrasto laminar|0,72 N|
|Arrasto turbulento|3,36 N|
|Relação entre arrastos|4,65 vezes|

**Observação importante:** os resultados turbulentos acima utilizam diretamente a correlação $0,074/Re_L^{1/5}$. Nas anotações do professor aparece um coeficiente próximo de 0,00377 e um arrasto de aproximadamente 3,3 N. A diferença é de arredondamento ou de valor intermediário utilizado. Na prova, priorize a correlação e os arredondamentos adotados pelo professor. A hipótese de escoamento turbulento desde o início da placa também deve ser mantida conforme o método ensinado.