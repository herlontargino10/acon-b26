import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Q2.10 in SIMULADO
    q2_old = r"10\. O material documentado grafou equivocadamente que no fluido Newtoniano a viscosidade \w+ constante em rela\w+ \w+ tens\w+ _________ aplicada, quando no rigor f\w+sico o termo correto seria tens\w+ de cisalhamento\."
    q2_new = "10. Na listagem de simplificações de projeto, um fluido classificado como newtoniano é caracterizado por possuir a sua _________ mantida constante independentemente da tensão aplicada."
    content = re.sub(q2_old, q2_new, content)
    
    # 2. Update Q4.4 in SIMULADO
    q4_old = r"\*\*Questão 4\.4\.\*\* Na leitura atenta da formulação.*?nos cálculos infinitesimais\."
    q4_new = '''**Questão 4.4.** Segundo o texto-base, o equacionamento associado ao trabalho da pressão na modelagem de energia apresenta uma particularidade fundamental em relação ao volume de controle. Assinale a alternativa que a descreve corretamente:
(a) O trabalho de pressão acumula energia estática integralmente no interior do volume, pois cada elemento de fluido contrai-se volumetricamente sob ação da barreira externa impermeável sem transição espacial.
(b) Ação da pressão restringe-se puramente às variações tridimensionais rotacionais no centro do volume de controle, não surtindo efeitos dinâmicos nas fronteiras marginais.
(c) As forças de pressão internas realizam saldos contínuos de energia que multiplicam a viscosidade ao longo de toda a massa, exigindo correções isotérmicas absolutas.
(d) O trabalho da pressão realiza saldo apenas ao cruzar a barreira da superfície de controle, não gerando saldo no núcleo do volume de controle devido à ação de forças opostas entre elementos adjacentes.
(e) Trata-se de uma força de natureza puramente inercial constante que age como trabalho de máquina, dissipando-se de forma isolada pelas pás diretrizes do navio.'''
    content = re.sub(q4_old, q4_new, content, flags=re.DOTALL)
    
    # 3. Update Gabarito Q2.10
    g2_old = r"10\. \*\*superficial\*\*: Preservada a grafia do desvio material didático.*?alerta\w+\."
    g2_new = "10. **viscosidade**: A hipótese 7 da Seção 7 define textualmente que o fluido newtoniano é aquele no qual a viscosidade se mantém constante perante a tensão."
    content = re.sub(g2_old, g2_new, content, flags=re.DOTALL)
    
    # 4. Update Gabarito Q4.4
    g4_old = r"\*\*Questão 4\.4\.\*\* Alternativa correta: \*\*\(b\)\*\*.*?\*\*Questão 4\.5\.\*\*"
    g4_new = '''**Questão 4.4.** Alternativa correta: **(d)**
- **(a) Incorreta:** O trabalho de pressão não armazena energia de forma isolada no volume.
- **(b) Incorreta:** É o contrário, ele atua nas fronteiras da superfície de controle e não no núcleo.
- **(c) Incorreta:** Não há saldo interno no núcleo do volume, as forças internas se cancelam.
- **(d) Correta:** Conforme descrito na Seção 5.3, no núcleo do volume as forças de pressão adjacentes se cancelam. O saldo real acontece apenas ao cruzar a superfície de controle.
- **(e) Incorreta:** O trabalho de máquina é uma modalidade separada, referindo-se a eixos mecânicos cruzando a fronteira, e não ao trabalho de pressão do fluido.

**Questão 4.5.**'''
    content = re.sub(g4_old, g4_new, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")

update_file('SIMULADO_U1_CAPITULO_4.md')
