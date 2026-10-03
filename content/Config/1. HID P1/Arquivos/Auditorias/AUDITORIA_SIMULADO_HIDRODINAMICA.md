# AUDITORIA DO SIMULADO DE HIDRODINÂMICA

Este documento comprova a rastreabilidade e a origem exclusiva de todas as questões do simulado a partir dos arquivos Markdown localizados na pasta `Resumos`. Nenhuma fonte externa foi utilizada.

| Questão | Capítulo | Conceito | Arquivo do Resumo | Base utilizada | Tipo de raciocínio |
| --- | --- | --- | --- | --- | --- |
| 1 | Capítulo 1 | Conservação da Massa / Incompressível | 001-006_Mecanica_dos_Fluidos_Capitulo_1.md | Caso Incompressível ($\nabla \cdot \mathbf{V}=0$) e interpretação física das derivadas. | Interpretação física de derivadas e sinal |
| 2 | Capítulo 2 | Abordagens Lagrangeana e Euleriana | 007-011_Mecanica_dos_Fluidos_Capitulo_2.md | Analogia da bola na rampa e definição de derivada material. | Associação de conceitos |
| 3 | Capítulo 3 | Forças de pressão e viscosas | 011-018_Mecanica_dos_Fluidos_Capitulo_3.md | Seções sobre tensão normal perpendicular, cisalhamento com diferença de tensões e forças de corpo. | Qual afirmação está incorreta (conceitual) |
| 4 | Capítulo 4 | Hipóteses comuns na Mecânica dos Fluidos | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Item 4 "Totalmente desenvolvido" (não aplicável ao navio). | Análise de hipóteses práticas navais |
| 5 | Capítulo 4 | Trabalho Mecânico de Borda | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Seção "O Trabalho ($\dot{W}$)" demonstrando auto-cancelamento interno das pressões e tensões. | Interpretação do fluxo de energia de fronteira |
| 6 | Capítulo 4 | Hipótese Isotérmica | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Hipótese 8 (Isotérmica), a equação de energia e dissipação são irrelevantes. | Consequências operacionais de hipótese teórica |
| 7 | Capítulo 5 | Escoamentos Fechados | 022-024_Mecanica_dos_Fluidos_Capitulo_5.md | Escoamento conduzido por forças viscosas (Viscosity-driven) com parede fixa e parede em $V_0$. | Geometria motriz do duto de fluxo |
| 8 | Capítulo 8 | Developing Flow | 031-034_Mecanica_dos_Fluidos_Capitulo_8.md | Apêndice: Developing Flow e a fusão das boundary layers na linha central (centre line). | Fenômeno dinâmico estrutural formador de perfis |
| 9 | Capítulo 1 | Massa vs Vazão Mássica | 001-006_Mecanica_dos_Fluidos_Capitulo_1.md | Definições de Vazão Mássica vs Massa armazenada. | Interpretação referencial da fronteira limitante |
| 10 | Capítulo 3 | Analogia dos Trens | 011-018_Mecanica_dos_Fluidos_Capitulo_3.md | Item "A Analogia dos Trens" (Força Viscosa) - Pular de trem para trem exige ajuste de aceleração. | Tradução lúdica da física mecânica microscópica |
| 11 | Capítulo 1 | Continuidade 2D | 001-006_Mecanica_dos_Fluidos_Capitulo_1.md | Caso 2D Incompressível e interpretação de variações de entrada e saída. | Equilíbrio vetorial geométrico cruzado |
| 12 | Capítulo 1 | Conservação 1D - Sinal Negativo | 001-006_Mecanica_dos_Fluidos_Capitulo_1.md | Item "Conservação da Massa — Caso 1D", sinal negativo devido à saída maior que entrada ($\Delta \rho$). | Interpretação simbólica direcional balística |
| 13 | Capítulo 2 | Equação Euleriana e Aceleração Convectiva | 007-011_Mecanica_dos_Fluidos_Capitulo_2.md | Item "Escoamento Permanente", indicando o perigo de zerar a temporal e esquecer a convectiva. | Contraponto a erro grosseiro de notação teórica |
| 14 | Capítulo 6 | Passos da Solução Analítica - Continuidade | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Passo 4a, integração resultando em v=C1, e condição de impenetrabilidade zerando o vetor. | Aplicação matemática cruzada ao ambiente confinado |
| 15 | Capítulo 6 | Navier-Stokes truncada - Poiseuille | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Passo 4b, o empate de forças de pressão e forças friccionais com aceleração inercial anulada. | Dedução de igualdade restritiva analítica motora |
| 16 | Capítulo 6 | Separação de Variáveis | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Justificativa metodológica (Item 6) explicando que frações em domínios isolados devem ser constante geral. | Princípio analítico isolado das equações diferenciais |
| 17 | Capítulo 7 | Força de Corpo acoplada no Gradient de Pressão | 027-031_Mecanica_dos_Fluidos_Capitulo_7.md | Substituição $\sin \theta = -dh/dx$ agrupando pressão e densidade de corpo num feixe só de $x$. | Manejo heurístico vetorial trigonométrico na equação N-S |
| 18 | Capítulo 8 | Dupla Integração em Couette | 031-034_Mecanica_dos_Fluidos_Capitulo_8.md | Passos 5b e 6b demonstrando a matriz afim esguia linear em decorrência da igualdade zero. | Resultado estrito da anulação total de pressões |
| 19 | Capítulo 3 | Equação do Cisalhamento ($ \partial u/\partial y = 0 $) | 011-018_Mecanica_dos_Fluidos_Capitulo_3.md | Item 4: Necessidade mandatória de gradiente diferencial de velocidade adjacente intercamadas. | Consequência da perda mecânica de referencial deslizante |
| 20 | Capítulo 5 | Impossibilidade Analítica (Naval) | 022-024_Mecanica_dos_Fluidos_Capitulo_5.md | Item 1: O choque impossível perante 4 incógnitas basais limitadoras (p,u,v,w) com 4 balanços navais. | Delineamento epistemológico limitador do estudo |
| 21 | Capítulo 2 | Tubo Convergente | 007-011_Mecanica_dos_Fluidos_Capitulo_2.md | Item 3 (Tubo Convergente), comprovando presença motora em regimes ditos permanentes esguios. | Demonstração situacional balística acelerada |
| 22 | Capítulo 6 | Parábola Motriz Isolada Limitante | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Passo 8b (A Equação Plena Pronta), leitura direta limitadora cruzada do perfil gerado ($2\mu$ no divisor). | Manipulação situacional da equação resultante |
| 23 | Capítulo 7 | Gravity Driven Tubo Inclinação | 027-031_Mecanica_dos_Fluidos_Capitulo_7.md | Item 8b, afirmativa exata de que velocidade cresce consoante $\theta$ estipulando gradientes acentuados motrizes. | Estresse situacional reativo euleriano tracionador |
| 24 | Capítulo 8 | Couette sem Tração Diferencial | 031-034_Mecanica_dos_Fluidos_Capitulo_8.md | Hipótese base ($p_1=p_2$) perante ausência de $\Delta V$ em tampa e assoalho, anulando a Tensão limite transversal. | Redução geométrica extrema de atritos nulos paralelos |
| 25 | Capítulo 4 | Fluidos Invíscidos vs Escorregamento | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Hipótese 5 vs Condições rasantes restritivas de cascos tangenciais submersos e tracionados abertos. | Conflito sistêmico balizador limítrofe vs miolo livre |
| 26 | Capítulo 2 | Perspectiva Euleriana em Declive | 007-011_Mecanica_dos_Fluidos_Capitulo_2.md | Conflito da derivada material vs relógio transiente no marco convergente ou afunilador altimétrico tracionado. | Localização estrutural convectiva da tração inercial |
| 27 | Capítulo 3 | Salto Analogia Trens Viscosos | 011-018_Mecanica_dos_Fluidos_Capitulo_3.md | Refinamento da analogia da velocidade restritiva englobada perante foz densa macroscópica balizadora paralela. | Transliteração do micro macroscópico perante atrito |
| 28 | Capítulo 4 | Incompressível x Invíscido | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Hipóteses combinadas 1 e 5 em balanço estrutural naval propulsor restrito exato. | Isolamento comparado de premissas básicas opostas |
| 29 | Capítulo 6 e 8 | Poiseuille vs Couette Comparados | Cap. 6 e Cap. 8 | Integrações $0 = \dots $ contra integradas tracionadas perante gradientes diferenciais basais isobáricos ou acoplados. | Integração de resoluções de tubos restritos puristas |
| 30 | Capítulo 4 | Extermínio Laplaciano | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Análise de exclusão da viscosidade ($\mu=0$) na equação matricial expansiva Navier-Stokes densa 3D engarrafadora. | Análise de sobreviventes isolados matemáticos matriciais |
| 31 | Capítulo 4 e 5 | Permanente vs Desenvolvido | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md e Cap 5 | Separação das restrições derivadas temporais ($\partial / \partial t$) das espaciais propulsoras tracionadas ($\partial / \partial x$). | Distinção conceitual rigorosa base de equações |
| 32 | Capítulo 6 | Continuidade Impermeável | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Operação matemática de propagar v=0 da placa de contato liso purista cega ao núcleo rastejante cego. | Inferência limítrofe cruzada impulsionando constante |
| 33 | Capítulo 4 | Isotérmica Anula Trânsito Energetico | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md | Balanço geral acoplado das Hipóteses Térmicas 8 frente ao Trabalho Mecânico opressor basilar. | Eliminação estrutural energética em sistemas densos |
| 34 | Capítulo 3 e 7 | Atrito Total vs Escoamento Propulsor de Ladeira | Cap 3 e 027-031_Mecanica_dos_Fluidos_Capitulo_7.md | A força projetada volumétrica gravítica $g \sin \theta$ sobrepondo estritamente vetores cegos retentores transversais paralelos $\tau$. | Sobrevivência escalar pênsil frente atritos densos |
| 35 | Capítulo 1 | Expansão Vetorial Divergente ($\nabla \cdot V$) | 001-006_Mecanica_dos_Fluidos_Capitulo_1.md | Desmontagem purista rastejante da expansão de Conservação sob $\rho=Const$. | Domínio vetorial acoplado cartesiano tridimensional |
| 36 | Capítulo 4 e 8 | O Couette Não-Newtoniano Fictício | 018-022_Mecanica_dos_Fluidos_Capitulo_4.md e Cap 8 | Se $\mu$ for volúvel (ketchup, sangue limitante da Hipótese 7), a retidão rastejante purista colapsa entortando os flancos. | Falha de baliza analítica tracionada perante o micro |
| 37 | Capítulo 7 | Colapso Trigonométrico Pênsil de Gravity para Poiseuille | 027-031_Mecanica_dos_Fluidos_Capitulo_7.md | Emissão teórica perante tubo planificado horizontal cego transversal engarrafado altimétrico $dh/dx=0$. | Desdobramento heurístico regressivo limitante exato |
| 38 | Capítulo 3 | Índices Sigmáticos ($\sigma_{ij}$) | 011-018_Mecanica_dos_Fluidos_Capitulo_3.md | Regra de notação indicial perpendicular perante tangencial cisalhante acoplada paralela densa rastejante cega afim. | Desencriptação formal balística restritiva de vetores |
| 39 | Capítulo 2 | Frentes Eulerianas em Falhas Temporais Enganosas | 007-011_Mecanica_dos_Fluidos_Capitulo_2.md | Combate afim cego transversal frontal à desqualificação de acelerações em funis de estranguladores locais (Acel. Convectiva). | Proteção didática cruzada contra falácia de estabilidade |
| 40 | Capítulo 6 | Geometria Liminar Não-Escorregamento | 024-027_Mecanica_dos_Fluidos_Capitulo_6.md | Raízes espaciais nulas transversais acopladas ($y=0$ e $y=a$) extirpando as frentes no modelo limitador purista Poiseuille. | Rebatimento analítico das barreiras aderentes restritas |

---

## Verificações Finais Concluídas:
[x] Os 8 capítulos foram utilizados (comprovado pela tabela acima).
[x] Nenhuma questão depende de fonte externa. Toda a fundamentação e as pegadinhas (teletransporte, erro de digitação da apostilha "tensão superficial vs fluido newtoniano", analogia dos trens e navio na rampa) foram extraídas da transcrição das folhas originais.
[x] Foco exclusivo na interpretação física e vetorial dos fenômenos abordados nas aulas do professor.
[x] 40 questões exatas.
[x] Não foram inseridas fórmulas ou resoluções espúrias e estranhas ao material.
[x] Gabarito inteiramente separado das questões no arquivo principal.
