```txt

[CONTEXTO E CONFIGURAÇÃO]
Você é um Engenheiro de Software Front-End Sênior e Especialista em UX/UI. Seu objetivo é criar um arquivo de código ÚNICO, completo, responsivo e que funcione 100% offline (sem internet e sem dependências externas) para um SIMULADO INTERATIVO E PROFISSIONAL. 

O design final DEVE parecer uma plataforma moderna de treinamento corporativo ou preparatório de alta performance. Evite terminantemente layouts infantis, paletas de cores genéricas de IA (como tons pastéis sem contraste) e estruturas de tabelas cruas.

[REQUISITOS TÉCNICOS OBRIGATÓRIOS]
1. Arquivo Único: Forneça APENAS um bloco de código contendo o código HTML completo.
2. Tudo Embutido: CSS (dentro de <style>) e JavaScript (dentro de <script>) devem estar integrados no próprio arquivo.
3. Zero Dependências: Não use links externos para Google Fonts, FontAwesome, Bootstrap, Tailwind CDN, jQuery ou frameworks JS. Use fontes de sistema seguras (system-ui, Segoe UI, etc.) e ícones renderizados via CSS Puro ou SVG se necessário.
4. Persistência e Fluidez: O usuário deve conseguir navegar pelas questões usando botões "Anterior" e "Próxima" sem perder as respostas já selecionadas ou digitadas. O fluxo não deve travar.

[DIRETRIZES DE DESIGN & INTERFACE (UI/UX)]
- Tema Escuro Premium: Fundo em tom azul-escuro profundo ou grafite espacial (ex: #0b0f19, #151f32), textos em alta legibilidade (#f1f5f9) e realces em tons tecnológicos (azul neon, esmeralda para acertos, vermelho fosco para erros).
- Layout Estilo Dashboard: No topo, fixe um cabeçalho estático mostrando o progresso atual (ex: Questão 12/40), uma barra de progresso horizontal com transição suave, e contadores em tempo real para "Acertos", "Erros" e "Aproveitamento Geral (%)".
- Cards de Questão: Cantos suavemente arredondados (border-radius: 12px a 16px), sombras leves de profundidade, tags indicando a "Categoria/Tópico" da questão e animação sutil de fade-in ao alternar de tela.
- Estados Visuais Claros: As alternativas devem mudar de estilo ao passar o mouse (:hover) e ao serem selecionadas. Quando o usuário clicar em "Verificar", o sistema deve pintar as bordas/fundo de verde (se correto) ou vermelho (se incorreto), revelando também a alternativa certa.

[TIPOS DE QUESTÕES A SUPORTAR NO CÓDIGO]
O script JS deve renderizar dinamicamente os seguintes formatos de tela de acordo com o banco de dados:
- Múltipla Escolha: Opções em formato de grid ou lista vertical.
- Verdadeiro ou Falso: Duas opções explícitas de clique.
- Completar Lacunas (Gap Fill): Texto com um campo de <input> embutido no meio da frase para o usuário digitar a palavra-chave.
- Discursiva/Estudo de Caso: Um campo grande de <textarea>. Ao clicar em verificar, não computa erro automático, mas abre uma caixa estilizada mostrando o "Gabarito Técnico Esperado" para o usuário autoavaliar sua resposta escrita.

[MECÂNICA DO SISTEMA (JAVASCRIPT)]
- Guarde o estado das respostas em vetores (arrays) para que o usuário possa mudar de alternativa livremente ANTES de validar.
- O botão "Verificar Resposta" deve revelar uma seção oculta (Explanation Box) logo abaixo da questão, contendo a justificativa detalhada e a análise técnica do problema.
- Tela de Encerramento (Fim do Bloco): Ao chegar na última questão, substitua o botão "Próxima" por um botão destacado "Finalizar Simulado". Quando clicado, ele deve ocultar o bloco de perguntas, travar novas edições, exibir uma tela centralizada de feedback com a porcentagem final de acertos bem grande e um botão para "Refazer Simulado" (redefinindo o estado).

---
[BANCO DE DADOS E CONTEÚDO DO SIMULADO]
Utilize estritamente os dados abaixo para estruturar o array de objetos das questões no JavaScript. Adapte o texto fornecido para os formatos exigidos (Múltipla escolha, V/F, lacunas ou discursivas):

TEMA: [Insira o Tema Aqui - Ex: COMBATE A INCÊNDIO AVANÇADO]

