# Gabarito Comentado e Auditoria — Simulado Simples P1

> **Documento de Referência:** Simulado P1 de Hidrodinâmica I — Versão de Estudo  
> **Fontes Auditadas:** `SIMULADO_P1_DIRECIONAMENTO_PROFESSOR.md`, `SIMULADO_P1_DIRECIONAMENTO_PROFESSOR_GABARITO_COMENTADO.md`, transcrição de áudio `Bizu hidroVoz 261030_104750_original.txt` e anotações do aluno `direcionamento_do_professor_prova_1.txt`.  
> **Diretriz de Elaboração:** Resoluções objetivas, fórmulas essenciais, justificativas breves e registro transparente de ambiguidades e pendências.

---

## 1. Grade Resumo do Gabarito

| Questão | Tipo | Assunto Principal | Gabarito Oficial |
| :---: | :--- | :--- | :---: |
| **Q1** | Múltipla Escolha | Escoamento permanente em duto divergente incompressível | **[B]** |
| **Q2** | Múltipla Escolha | Continuidade 3D e cancelamento da densidade absoluta | **[C]** |
| **Q3** | Múltipla Escolha | Orientação do professor em sala de aula | *EXCLUÍDA / NÃO COBRADA* |
| **Q4** | Múltipla Escolha | 2ª Lei de Newton em VC infinitesimal e força de pressão | **[A]** |
| **Q5** | Múltipla Escolha | Condições de contorno cinemáticas (impenetrabilidade e aderência) | **[C]** |
| **Q6** | Completar Lacunas | 10 conceitos estruturantes de Hidrodinâmica I | *10 subitens (com 2 ambiguidades)* |
| **Q7** | Verdadeiro ou Falso | Princípio da Homogeneidade e Teorema $\Pi$ de Buckingham | **V – V – F – V – F – V** |
| **Q8** | Cálculo Fixo | Método dos Seis Passos de Buckingham–$\Pi$ | *Vaga Reservada* |

---

## 2. Resolução Comentada por Questão

---

### Questão 1 — Escoamento Incompressível em Duto Divergente

* **Gabarito Oficial:** **Alternativa [B]**
* **Justificativa Breve:**  
  1. Pela conservação da massa para fluido incompressível, a vazão volumétrica é constante ao longo do duto:
     $$Q = A(x) \cdot u(x) = \text{constante} \implies u(x) = \frac{Q}{A(x)}$$
  2. Como a seção é divergente ($\frac{dA}{dx} > 0$), derivando a velocidade obtém-se:
     $$\frac{\partial u}{\partial x} = -\frac{Q}{[A(x)]^2}\frac{dA}{dx} < 0$$
  3. No regime permanente, a aceleração local é nula ($\frac{\partial u}{\partial t} = 0$). Logo, a aceleração total da partícula fluida reduz-se à parcela convectiva:
     $$a_x = \frac{Du}{Dt} = \underbrace{\frac{\partial u}{\partial t}}_{=0} + u\frac{\partial u}{\partial x} = a_{\text{conv}}$$
  4. Sendo $u > 0$ e $\frac{\partial u}{\partial x} < 0$, o produto resulta em aceleração negativa ($a_{\text{conv}} < 0$). Como velocidade e aceleração têm sentidos opostos, ocorre a **desaceleração da partícula fluida**.
* **Distratores em Síntese:**  
  * [A] Incorreta: confunde regime permanente ($\frac{\partial u}{\partial t} = 0$, ponto fixo) com aceleração total nula ($\frac{Du}{Dt} = 0$).  
  * [C] Incorreta: violaria a conservação da massa ($A$ aumenta $\implies u$ diminui).  
  * [D] Incorreta: o termo convectivo $u\frac{\partial u}{\partial x}$ atua plenamente em escoamentos unidimensionais de área variável.  
  * [E] Incorreta: incompressibilidade significa $\rho = \text{constante}$, e não velocidade constante.

---

### Questão 2 — Equação da Continuidade e Densidade Absoluta

* **Gabarito Oficial:** **Alternativa [C]**
* **Justificativa Breve:**  
  1. A forma geral da conservação da massa tridimensional é:
     $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$$
  2. Para fluido incompressível ($\rho = \text{constante}$ no espaço e no tempo), a derivada temporal é nula ($\frac{\partial \rho}{\partial t} = 0$) e a densidade é fatorada para fora das derivadas espaciais:
     $$\rho (\nabla \cdot \mathbf{V}) = \rho \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \right) = 0$$
  3. Sendo a massa específica da água líquida não nula ($\rho \neq 0$), divide-se ambos os membros por $\rho$, cancelando-a algebricamente por divisão:
     $$\nabla \cdot \mathbf{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$
  4. O cancelamento é uma simplificação algébrica exata, não sendo um desprezo numérico nem uma substituição por peso específico.
* **Distratores em Síntese:**  
  * [A] Incorreta: a conservação da massa continua sendo a lei regente.  
  * [B] Incorreta: o cancelamento decorre de $\rho = \text{constante} \neq 0$, e não de aproximação por ser pequena.  
  * [D] Incorreta: o peso específico ($\gamma = \rho g$) atua na Equação da Quantidade de Movimento (força de corpo).  
  * [E] Incorreta: o cancelamento é perfeitamente válido no caso tridimensional geral.

---

### Questão 3 — NÃO SERÁ COBRADA (Posição Oficial do Professor)

* **Posição Oficial:** O professor declarou expressamente no áudio: "*E o terceiro, não vou falar*". A questão está formalmente excluída da avaliação. A posição foi preservada para manter a numeração das questões subsequentes.

---

### Questão 4 — Segunda Lei de Newton e Força de Pressão

* **Gabarito Oficial:** **Alternativa [A]**
* **Justificativa Breve:**  
  1. A pressão atua sempre empurrando a superfície para o interior do volume (caráter compressivo):
     * Face de entrada em $x$: empurra no sentido positivo $+x$ $\implies F_{\text{in}} = + p\,dy\,dz$.
     * Face de saída em $x + dx$: empurra no sentido negativo $-x$ $\implies F_{\text{out}} = - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz$.
  2. Somando as forças compressivas atuantes nas duas faces opostas:
     $$dF_{p,x} = F_{\text{in}} + F_{\text{out}} = p\,dy\,dz - \left(p + \frac{\partial p}{\partial x}dx\right)dy\,dz = -\frac{\partial p}{\partial x}dx\,dy\,dz$$
  3. Dividindo pelo volume diferencial do elemento ($dVol = dx\,dy\,dz$), obtém-se a força por unidade de volume:
     $$f_{p,x} = \frac{dF_{p,x}}{dx\,dy\,dz} = -\frac{\partial p}{\partial x}$$
  4. O sinal negativo decorre diretamente do balanço direcional das forças compressivas na face de saída (sentido $-x$).
* **Distratores em Síntese:**  
  * [B] Incorreta: erra o sinal algébrico resultante ($+ \frac{\partial p}{\partial x}$).  
  * [C] Incorreta: havendo gradiente de pressão, a resultante não é nula.  
  * [D] Incorreta: inverte as dimensões de força líquida e força volumétrica.  
  * [E] Incorreta: o gradiente de pressão atua tanto em fluidos compressíveis quanto incompressíveis.

---

### Questão 5 — Condições de Contorno Cinemáticas em Fronteiras Sólidas

* **Gabarito Oficial:** **Alternativa [C]**
* **Justificativa Breve:**  
  1. **Condição de Impenetrabilidade:** A parede é sólida e impermeável, impedindo o fluxo através dela. Logo, a componente de velocidade normal relativa na parede é nula:
     $$\mathbf{V}_{\text{rel}} \cdot \mathbf{n} = 0 \quad (\text{para parede em repouso: } v_n = 0)$$
  2. **Condição de Aderência (Não-Escorregamento):** O atrito viscoso e as forças intermoleculares impedem o deslizamento do fluido viscoso na superfície. Logo, a componente de velocidade tangencial relativa na parede é nula:
     $$\mathbf{V}_{\text{rel}} \times \mathbf{n} = \mathbf{0} \quad (\text{para parede em repouso: } u_{\text{tangencial}} = 0)$$
  3. Ambas incidem diretamente sobre o campo de velocidades $\mathbf{V}$, sendo classificadas como **condições cinemáticas**.
* **Distratores em Síntese:**  
  * [A] Incorreta: inverte as componentes (normal na impenetrabilidade; tangencial na aderência).  
  * [B] Incorreta: fluidos invíscidos ($\mu = 0$) não satisfazem aderência (deslizam sobre a parede sólida).  
  * [D] Incorreta: são cinemáticas (velocidades), e não dinâmicas (tensões).  
  * [E] Incorreta: aderência decorre da viscosidade, não da gravidade, e não se aplica a fluidos invíscidos.

---

### Questão 6 — Conceitos Estruturantes de Hidrodinâmica I

1. **tensão superficial**  
   *Justificativa:* Identificada pelo símbolo $\sigma$ e pela dimensão primária $[MT^{-2}]$ no sistema $MLT$. As demais citadas no enunciado são $\rho$ $[ML^{-3}]$, $\mu$ $[ML^{-1}T^{-1}]$ e $p$ $[ML^{-1}T^{-2}]$.
2. **Continuidade**  
   *Justificativa:* A aplicação da conservação da massa a um volume infinitesimal fixo resulta formalmente na Equação da Continuidade.
3. **euleriana**  
   *Justificativa:* Perspectiva em que se fixam coordenadas espaciais estáticas $(x, y, z)$ no espaço para observar o escoamento ao longo do tempo.
4. **lagrangeana**  
   *Justificativa:* Perspectiva que acompanha a trajetória de partículas fluidas individuais ao longo do tempo.
5. **local** ; **convectiva** *(nesta ordem estrita)*  
   *Justificativa:* A derivada material da velocidade decompõe-se na taxa de variação temporal local ($\frac{\partial \mathbf{V}}{\partial t}$) e na taxa de variação espacial convectiva ($(\mathbf{V}\cdot\nabla)\mathbf{V}$).
6. **superfície** ; **corpo**  
   *Justificativa:* Forças de superfície atuam nas fronteiras por contato mecânico (pressão e viscosidade); forças de corpo atuam na massa do elemento à distância (peso gravitacional). *(Não se adota o termo "campo" por ausência na fonte oficial).*
7. **ITEM COM AMBIGUIDADE DOCUMENTAL NAS FONTES (Placas Planas Paralelas):**  
   *Justificativa e Distinção das Possibilidades:* O professor não especificou no áudio a condição condutora do escoamento. Existem duas possibilidades documentadas oficialmente:  
   * **Possibilidade 1 (gradiente de pressão entre placas fixas):** conduzido por **gradiente de pressão** $\implies$ escoamento plano de **Poiseuille**.  
   * **Possibilidade 2 (placa móvel sob arraste viscoso com gradiente nulo):** conduzido por **arraste de placa móvel** $\implies$ escoamento plano de **Couette**.  
   *Não há base documental para eleger uma única alternativa sem que o professor defina a condição condutora.*
8. **ITEM COM AMBIGUIDADE DOCUMENTAL NAS FONTES (Número Adimensional de Inércia):**  
   *Justificativa e Distinção das Possibilidades:* O professor não especificou no áudio qual força é comparada à inércia. Existem duas possibilidades documentadas oficialmente:  
   * **Possibilidade 1 (inércia versus forças viscosas):** Número de **Reynolds** ... forças **viscosas** ($Re = \frac{\rho U L}{\mu}$).  
   * **Possibilidade 2 (inércia versus forças gravitacionais):** Número de **Froude** ... forças **gravitacionais** ($Fr = \frac{U}{\sqrt{gL}}$).  
   *Ambas as possibilidades possuem respaldo idêntico nas fontes oficiais.*
9. **modelo** ; **protótipo**  
   *Justificativa:* O modelo é a embarcação em escala geométrica reduzida testada no tanque; o protótipo é o navio real em escala natural (1:1).
10. **constante** ; **pontos homólogos**  
    *Justificativa:* Na similaridade cinemática, as trajetórias são semelhantes e a razão de velocidades em posições correspondentes é rigorosamente **constante** ($\frac{V_m}{V_p} = \text{constante}$). O termo técnico oficial para essas posições é **pontos homólogos** *(a expressão "partícula homóloga" constitui jargão oral de sala de aula)*.

---

### Questão 7 — Princípio da Homogeneidade e Teorema $\Pi$ de Buckingham (Teoria Pura)

* **Item 7.1: VERDADEIRO (V)**  
  *Justificativa:* O Princípio da Homogeneidade Dimensional exige que todos os termos somados algebricamente em uma equação física válida tenham as mesmas dimensões primárias fundamentais ($MLT$ ou $FLT$).
* **Item 7.2: VERDADEIRO (V)**  
  *Justificativa:* A adimensionalização formal consiste em dividir cada termo da equação por uma combinação de variáveis que possua a mesma dimensão desses termos.
* **Item 7.3: FALSO (F)**  
  *Justificativa:* O Teorema $\Pi$ de Buckingham estabelece que o número de grupos adimensionais independentes é dado pela **diferença** $k = n - m$, e não pela soma $n + m$.
* **Item 7.4: VERDADEIRO (V)**  
  *Justificativa:* Na hidrodinâmica naval, o sistema padrão adotado é o $MLT$, composto por $m = 3$ dimensões primárias: Massa ($M$), Comprimento ($L$) e Tempo ($T$).
* **Item 7.5: FALSO (F)**  
  *Justificativa:* É expressamente proibido selecionar variáveis repetidas puramente geométricas (como comprimento, largura e raio), pois compartilham apenas a dimensão Comprimento ($L$), violando o requisito de conter todas as dimensões primárias do problema ($M, L, T$).
* **Item 7.6: VERDADEIRO (V)**  
  *Justificativa:* Na Etapa 6, como o produto de cada grupo $\Pi$ deve ser estritamente adimensional, as potências das dimensões fundamentais são igualadas a zero ($M^0 L^0 T^0$) para a resolução dos expoentes algébricos.

---

### Questão 8 — CÁLCULO FIXO — SEIS PASSOS

* **Status:** Vaga fixa reservada para a aplicação do procedimento canônico em seis etapas de Buckingham–$\Pi$ trabalhado em sala de aula.

---

## 3. Matriz de Cruzamento: Áudio vs. Anotações vs. Fontes Oficiais

| Posição | Conteúdo no Áudio do Professor | Anotação do Aluno | Fonte Oficial / Status | Classificação de Certeza |
| :---: | :--- | :--- | :--- | :---: |
| **Q1** | Duto divergente incompressível permanente | Duto divergente incompressível permanente | Q4 Questionário / Leis de Conservação | **Confirmado** |
| **Q2** | Continuidade 3D e densidade absoluta | Continuidade 3D e densidade absoluta | Q7 Questionário / Leis de Conservação | **Confirmado** |
| **Q3** | *"E o terceiro, não vou falar"* | *"Ele não vai falar"* | Omitido formalmente pelo docente | **Excluído (Não Cobrado)** |
| **Q4** | 2ª Lei de Newton infinitesimal, pressão e sinal negativo | Volume infinitesimal, força de pressão e sinal negativo | Q11–13 Questionário / Balanço $dF_{p,x}$ | **Confirmado** |
| **Q5** | Condições de contorno cinemáticas | Condições de contorno cinemáticas | Q15–16 Questionário / Impenetrabilidade e Aderência | **Confirmado** |
| **Q6.1** | Propriedades físicas fundamentais | Propriedades físicas fundamentais | Tensão superficial $\sigma$ $[MT^{-2}]$ | **Confirmado** |
| **Q6.2** | Conservação de massa aplicada ao volume | Conservação de massa no volume | Equação da Continuidade | **Confirmado** |
| **Q6.3/4** | Perspectivas euleriana e lagrangeana | Perspectivas euleriana e lagrangeana | Descrições cinemáticas do escoamento | **Confirmado** |
| **Q6.5** | Concepção euleriana com 2 acelerações | Concepção euleriana com 2 acelerações | Acelerações local e convectiva | **Confirmado** |
| **Q6.6** | Forças que atuam sobre elemento fluido | Divisão das forças no elemento fluido | Forças de superfície e forças de corpo | **Confirmado** |
| **Q6.7** | Escoamento laminar entre 2 placas planas | Escoamento laminar entre placas | Poiseuille (pressão) ou Couette (placa móvel) | **Ambiguidade Documentada** |
| **Q6.8** | Razão entre forças de inércia e outra força | Razão entre forças de inércia e força | Reynolds (viscosa) ou Froude (gravidade) | **Ambiguidade Documentada** |
| **Q6.9** | Ensaios de modelos de tanque e similaridade | Ensaio de modelo de tanques e similaridade | Modelo e Protótipo | **Confirmado** |
| **Q6.10** | Constante velocidade partícula homóloga | Constante, velocidade, partícula homólogo | Razão de velocidades constante / Pontos homólogos | **Confirmado** |
| **Q7** | Homogeneidade e 6 princípios de Buckingham | Homogeneidade dimensional e 6 passos de Pi-Buckingham | Teoria de Análise Dimensional (V ou F) | **Confirmado** |
| **Q8** | Cálculo dos 6 passos feito em sala | Cálculo 6 passos (fixa) | Buckingham–$\Pi$ Canônico | **Confirmado (Reservado)** |

---

## 4. Lista Consolidada de Pendências e Incertezas

1. **Quinta Questão de Múltipla Escolha (Posição Q3):**
   * *Incerteza:* O professor declarou: *"São 5 múltiplas escolhas aí tá ah?"*, mas logo em seguida afirmou expressamente: *"E o terceiro, não vou falar"*.
   * *Decisão Adotada:* Apenas 4 conteúdos foram fornecidos (Q1, Q2, Q4 e Q5). A posição Q3 foi formalmente mantida como *não cobrada*, sem invenção de questões substitutas.
2. **Condição Condutora nas Placas Planas (Subitem 6.7):**
   * *Incerteza:* O áudio omitiu o mecanismo condutor do escoamento.
   * *Decisão Adotada:* Não escolher arbitrariamente entre Poiseuille e Couette. Registrar no gabarito as duas hipóteses técnicas: Poiseuille plano (gradiente de pressão entre placas fixas) e Couette plano (arraste de placa móvel).
3. **Força Confrontada no Número Adimensional de Inércia (Subitem 6.8):**
   * *Incerteza:* O áudio citou forças de inércia, mas omitiu a força de confronto.
   * *Decisão Adotada:* Não escolher arbitrariamente entre Reynolds e Froude. Registrar no gabarito as duas hipóteses técnicas: Reynolds (inércia vs. forças viscosas) e Froude (inércia vs. forças gravitacionais).
4. **Terminologia "Partícula Homóloga" vs. "Pontos Homólogos" (Subitem 6.10):**
   * *Incerteza:* O professor utilizou oralmente a expressão informal *"partícula homóloga"*.
   * *Decisão Adotada:* Aceitar o termo oficial da disciplina (**pontos homólogos**) e registrar que "partícula homóloga" corresponde ao jargão de sala de aula.
5. **Ressalva Pedagógica de Correção dos Itens 6.7 e 6.8:**
   * Os itens 7 e 8 da Questão 6 **não devem ser pontuados como respostas únicas** enquanto não houver esclarecimento expresso pelo professor das condições de contorno omitidas.