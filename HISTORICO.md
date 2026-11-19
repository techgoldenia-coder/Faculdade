# Histórico

Registro cronológico do que foi feito. Serve para retomar contexto em sessões futuras.

## 19/11/2026 — AS2 de Web Analytics: relatórios estratégico e operacional

- Enunciado recebido no chat: loja on-line de **presentes personalizados** com queda na conversão; analisar 30 dias de dados (GA4, Google Ads, Meta Ads) e entregar relatório estratégico (até 3 páginas, gestores) e operacional (até 8 páginas, time de marketing), com KPIs, análise e otimização por canal, 2 testes A/B e próximos passos. Planilha movida de Downloads para `AS2 - Relatórios de performance loja de presentes/`.
- Formato igual à AS2 de Gestão de Anúncios: .pptx com gráficos nativos, gerado por script (`gerar_relatorios.py`, que lê a planilha e confere os números) e exportado para PDF pelo PowerPoint.
- **Leitura do limite:** CAC de mídia paga = investimento ÷ faturamento das vendas pagas (un. 01) → 35,6%, acima dos 28% (R$ 126 por venda). Google 24,7%, Meta 63,5%.
- **Achados:** só 28% de quem informa o pagamento compra; 35% saem depois de ver o frete; tablet com 3.800 usuários e nenhuma venda; compradores são mulheres de 25 a 44 anos no celular; Meta traz 39% do tráfego e 11% das vendas. Inconsistências da planilha apontadas nos slides (UTM do Meta, tag de compra, funil "Comprar" 3.350 × 655 vendas).
- **Proposta:** destravar o checkout, realocar R$ 14 mil sem aumentar a verba (cenário ≈ 329 vendas pagas, CAC 27,0%) e segmentar e medir certo. Testes A/B: frete na página do produto e segmentação no Meta.
- Fontes: só as unidades 01 a 07 (`PUCPR, [2024]a–g`). Nenhum dado de mercado externo. Conferido: 3 + 8 páginas, sem texto cortado, validação dos .pptx aprovada.
- **Revisão final:** a pedido do Yan, os dois relatórios foram juntados em **um PDF só** (`YanSuyama_WebAnalytics_Relatorios.pdf`, 12 páginas: capa + 3 + 8, cada relatório com numeração própria). Ajustes: título do slide de origem (orgânico não tem "pouco tráfego"), meta de leads sem "hoje 0%", "pontos percentuais", 4º ponto do slide 1 sem repetição. "Atividade Somativa 2" tirado do rodapé, porque o enunciado não diz o número. Aprovado para envio.
- **Entrega em 2 arquivos:** o Yan conferiu que são 2 relatórios separados. O PDF unificado foi mantido, e `separar_pdfs.py` gera `YanSuyama_WebAnalytics_RelatorioEstrategico.pdf` (3 p.) e `..._RelatorioOperacional.pdf` (8 p.), sem capa, para não passar do limite.
- **Pendências:** confirmar se é AS2; prazo e peso; nota.

## 19/11/2026 — AS2 de Marketing de Relacionamento: transformação cultural e omnichannel

- Enunciado recebido no chat: consultoria para uma **rede de academias** (5 unidades, 3000 alunos, alta rotatividade, baixo engajamento, comunicação descentralizada, cultura de vendas, avaliações negativas). Pede diagnóstico e cultura, estratégia omnichannel e plano de implementação. Sem links de artigos de apoio nesta atividade. Template movido de Downloads para a raiz da matéria.
- O caso é dado pelo enunciado, sem escolha de tema. MEGA-WR e Drip-Plan não se aplicam.
- O template foi **preenchido no lugar**, mantendo títulos, perguntas e tabelas. O script `preencher_template.py` coloca cada bloco `@@` do `TRABALHO.md` na sua âncora.
- Conteúdo: objetivo de 12 meses; 6 valores; 7 ações de engajamento interno; 7 canais; manual de comunicação (tom, prazos de resposta, LGPD); 12 métricas; cronograma em 3 etapas com piloto em 1 unidade; trilha de 6 treinamentos; 7 indicadores. As metas são **relativas à linha de base medida no mês 1**, porque o enunciado não dá números.
- Fontes: só as unidades 01 a 08 (`PUCPR, [2025]a–h`) e a LGPD. Nenhum dado de mercado externo. Cada afirmação atribuída a uma unidade foi conferida no texto do PDF. A citação da Zappos foi retirada porque o material não fala em autonomia.
- **Revisão final:** os 12 itens do enunciado estão cobertos; citações e referências batem (a–h + LGPD); não há texto do template sem preencher. Fonte dos quadros padronizada para "Elaborado pelo autor (2026)". Aprovado para envio.
- **Pendências:** prazo e peso; nota.

## 19/11/2026 — AS2 de Design Experimental: pré-projeto de pesquisa experimental MEGA-WR

- Repositório clonado em `Desktop/Faculdade` (máquina do trabalho). O Yan deixou o repositório **público** por decisão própria, avisado da regra do `CLAUDE.md`; voltar para privado.
- Enunciado recebido no chat: pré-projeto respondendo a 12 perguntas (problema, hipóteses, VI, VD, controle, design, ambiente, tratamento, participantes, seleção, entre × intra, análise), com o exemplo de Enns e Hackett (1990) via Creswell (2014). Template Word movido de Downloads para a raiz da matéria: é a **Atividade Somativa 2**.
- **Tema escolhido pelo Yan:** MEGA-WR, fatorial 2 × 2 entre sujeitos, em laboratório on-line: condições de compra no anúncio (mínimo de 10 peças + preço de entrada) × foto (produto × cliente real de Leme) → intenção de pedir orçamento (Likert 7, 3 itens) e pedido de contato (sim/não). Hipóteses tiradas das entrevistas reais da AS2 de Construção de Interfaces.
- Amostra: 160 (40 por condição); mínimo de 128 pela análise de poder (f = 0,25, α = 0,05, poder 0,80, conferida por cálculo). Análise: ANOVA fatorial, qui-quadrado e regressão logística.
- **Fontes externas ao material** (reais, conferir se quiser): Cohen (1988), Faul *et al.* (2007, G*Power), Cronbach (1951), Resolução CNS 466/2012 e Creswell (2014), esta do enunciado. Material da PUC citado como `(PUCPR, [2025]a–g)`, com a data de "Fonte: a autora (2025)" nas unidades.
- **Conferência final:** as 12 perguntas foram cobertas e citações e referências batem. Corrigido: a MEGA-WR **não tem tabela de preço**, então o "a partir de R$ X" passou a ser um valor a definir com os proprietários. O mínimo virou "10 peças por modelo", e os fatos vindos dos proprietários passaram a citar SUYAMA (2026), não o site. Aprovado para envio.
- **Pendências:** prazo e peso; nota.

## 16/11/2026 — Três matérias novas: Design Experimental, Marketing de relacionamento e Web Analytics

- O Yan salvou os PDFs soltos na raiz de cada pasta, com o nome da plataforma (`Materiais Online N.pdf`). Os 24 foram movidos para `Base de dados/` e renomeados para `<Matéria> - N.pdf`, no padrão das outras matérias. Os dois `Materiais Online.pdf` sem número são a unidade 01, conferido no texto.
- Texto extraído de todos com `pdftotext`, sem erro. Exceção: `Design Experimental - 2.1.pdf` é o infográfico da unidade 02, quase todo em imagem. Para usá-lo, ler as páginas como imagem.
- `INFO.md` criado nas três, com as unidades, os tópicos, os cases e a bibliografia tirada das referências. **Pendentes:** semestre (registrado como 2026/2, a confirmar), professor, ementa oficial e avaliações.
- **Web Analytics tem só 7 unidades:** falta confirmar se existe a unidade 08.
- Bibliografia registrada só no `INFO.md`. Entra no `BANCO-DE-REFERENCIAS.md` quando for usada em trabalho.
- Linhas adicionadas no `PAINEL.md` (matérias e notas) e no `ESTRUTURA.md`.
- **Atividade das três matérias respondida no chat**, com justificativa a partir dos PDFs. Questões enviadas e respostas:
  - Design Experimental: 1 D, 3 E, 6 E, V/F B (número da questão não informado), 10 D.
  - Marketing de relacionamento: 1 C, 3 B, 4 B, 6 E, 7 A.
  - Web Analytics: 1 C, 2 D, 4 E, 9 B (questão de mais risco, A é a alternativa concorrente), 10 B.
  - As demais questões não foram enviadas. Respostas ainda não salvas em arquivo nas matérias.

## 21/09/2026 — AS2 de Construção de Interfaces: entregue

- **Entregue** `Entrega/YanSuyama_ProjetoUXUI.pdf` — 24 páginas, PDF único, capa com Professor Eduardo Alexandre Franciscon. Aguardando nota.
- Conferido antes do envio: sem marcadores `[INSERIR LINK]`/`[PREENCHER]`/`[VERIFICAR]` no texto e protótipo respondendo no ar (`site-prototipo-megawr.vercel.app` e `/orcamento`, HTTP 200).
- **Prazo registrado no `PAINEL` era 18/09**; entrega feita em 21/09. Quando a nota sair, verificar se houve desconto por atraso.
- **Dois riscos foram entregues declarados, não resolvidos:** teste com 2 participantes (o enunciado pede 3), limitação assumida na seção 8.1 e como prioridade na conclusão; e o protótipo feito em código (Astro), não em Figma/XD/Sketch como o item 3.2 do enunciado nomeia.
- Continua em aberto na pasta: `AS2 - Projeto UX UI MEGA-WR (rascunho).docx`, de 14/09, desatualizado — decisão do Yan sobre apagar ou mover.

## 16/09/2026 — AS2 de Gestão de Conteúdo: planejamento estratégico de conteúdo MEGA-WR

- Enunciado recebido no chat: relatório estruturado em 3 partes (marca + calendário 70-20-10; métricas + cenário alto alcance × baixa conversão; community management + crise). **Individual, sem template.** Prazo e peso não informados.
- **Decisão do Yan:** usar a **MEGA-WR** (marca real) mesmo com o enunciado pedindo "marca fictícia". Risco de desconto avisado; mitigação: premissa declarada na introdução — dados institucionais reais, calendário/metas/números/crise fictícios, nenhuma escola ou empresa associada à crise.
- Recorte: MEGA-WR inteira (nicho uniformes personalizados, B2B local), não só a linha Fitness — coerente com o posicionamento real "especialistas em uniformes, não loja de moda".
- Calendário de **outubro/2026**: 20 posts (14 E / 4 T-I / 2 P) em Instagram + Facebook, WhatsApp como conversão. Datas conferidas na web: Professor 15/10, Médico 18/10, Dentista 25/10, Comerciário 30/10 (Lei 12.790/2013).
- **Divergência no material:** a un. 05 chama os 20% de "tendências"; a un. 08, de "inspiracional". A definição oficial está numa imagem da un. 05 que não sai na extração — texto usa "tendências e inspiração" e cita as duas. Print pedido ao Yan (opcional).
- Métricas: alcance qualificado (% na região), taxa de engajamento com peso em salvamentos/compartilhamentos, taxa de conversão (conversas de WhatsApp ÷ cliques, com etiqueta de origem). Crise hipotética: estampa de uniforme escolar descascando, exposta em grupo de Facebook da cidade.
- Citação do material da PUC alinhada à convenção do banco: `(PUCPR, [2025]a–h)` — data tirada de "Fonte: o autor, 2025" nas imagens. 8 unidades + documento institucional da MEGA-WR registrados no `BANCO-DE-REFERENCIAS.md`.
- Rascunho completo salvo; aguarda revisão do Yan. Formato final (docx/PDF em ABNT) ainda não gerado.
- **18/09 — versão de entrega:** introdução passa a dizer que a MEGA-WR é a **empresa dos pais do Yan** e que o trabalho serve para ajudá-los (pedido do Yan). Revisão completa: 19 quadros e 1 tabela numerados, com título e fonte (NBR 14724); calendário sem a coluna repetida de canal; citação longa encurtada para ficar abaixo de 3 linhas; aspas diretas com "não paginado"; siglas soltas removidas (B2B); novo Quadro 12 com exemplo de legenda no tom da marca; conclusão amarra o plano como proposta real para a empresa.
- Trabalho movido para pasta própria `AS2 - Planejamento de conteúdo MEGA-WR/` (`TRABALHO.md` + `gerar_pdf.py` + PDF). Gerador adaptado do da AS2 de UX, com duas melhorias: **capa fora da contagem** (numeração começa na folha de rosto e aparece a partir da Introdução, NBR 14724) e **folha de rosto** com natureza do trabalho. Sumário com 3 níveis, conferido; nenhuma página órfã além de fim de seção.
- `YanSuyama_AS2_GestaoConteudo.pdf` — 29 páginas, revisado página a página. Capa e folha de rosto com **Leme** (cidade do Yan) e, na folha de rosto, **Tutoria: Talita Leuçz** — ambos informados pelo Yan em 18/09; tutoria também registrada no `PAINEL` e no `INFO.md`.
- **18/09 — versão condensada (29 → 18 páginas),** a pedido do Yan (meta de 15 a 20). Todos os itens do enunciado e todas as unidades citadas foram mantidos. Cortes: subseções 2.1.1–2.1.3 viraram parágrafos; persona, públicos e valores saíram dos quadros e foram para o texto; a justificativa (antiga 2.5) entrou na 2.3; distribuição semanal e fluxo de produção viraram texto; as três métricas foram para um quadro só; o diagnóstico da 3.2 virou parágrafo; as rotinas de relacionamento viraram lista; a matriz de respostas passou para 6 casos; os níveis de crise viraram texto e as fases, um quadro (a primeira resposta entra dentro dele); "o que não fazer" virou parágrafo. Resultado: 10 quadros e 1 tabela (antes, 19 quadros e 1 tabela). A versão de 29 páginas não foi versionada.

## 16/09/2026 — AS2 de Gestão de Anúncios: análise de resultados e otimização do plano de mídia

- Enunciado recebido no chat: apresentação em grupo (PDF) com 4 itens — recapitulação do cliente/objetivo, dados e métricas hipotéticos por mídia, plano de otimização (push, mídia tradicional, pull) e plano de ação interno.
- Base: AS1 (plano de mídia MEGA-WR, linha Fitness, Leme/SP, 01/11/2026–31/01/2027, R$ 12.000, Meta Ads + Google Ads + mídia exterior). Material de apoio lido: unidades 03 a 08.
- **Ponto do material a tratar com cuidado:** a unidade 05 lista leilão de palavras-chave/Google Ads como push/outbound; a unidade 06 diz que o anúncio que responde a uma busca é canal pull. A unidade 05 também chama push de "estratégia de mídia tradicional".
- **Decisões do Yan:** estrutura e cenário hipotético aprovados; Google Ads tratado como **pull**, sem slide sobre a divergência do material; trabalho **individual**; formato **.pptx**.
- **Cenário:** leitura em 30/11/2026 (fim da Fase 1, 33% do período). Diagnóstico: Meta saturado (frequência 8,5), Reels a R$ 10,81 por conversa contra R$ 23,68 do feed, Google B2C com 38% da verba em termos irrelevantes, Google B2B no teto (91% de parcela de impressões), outdoor sem rastreio, 59% das perdas B2C por causa interna. ROAS digital 2,55; B2B com ROAS 10,9.
- **Otimização:** verba restante de R$ 6.510 redistribuída sem aumentar o total; prospecção ativa em 60 academias; busdoor com QR code e cupom; outdoor não renovado; novos KPIs de venda, ROAS, tempo de resposta e origem do lead.
- **Produzido** em `Gestão de Anúncios em Canais Sociais/AS2 - Otimização do Plano de Mídia MEGA-WR/`: `TRABALHO.md`, `(rascunho).pptx` com 24 slides e gráficos nativos, e planilha de dados com fórmulas conferidas no Excel. Renderização revisada slide a slide pelo PowerPoint; exportação para PDF testada.
- **Dados reais usados:** prazo de 20 a 30 dias e horário de atendimento, conferidos em megawr.com.br em 16/09/2026. Preço e ticket médio são **premissas hipotéticas**.
- **Citações:** unidades 03 a 08 como `PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ, 2026a–f`, no padrão da AS1 da matéria. As outras matérias usam `[2026?]`/`[2025]`; ver nota no banco de referências.
- **Pendências:** prazo, peso e rubrica; revisão do Yan; exportar PDF.
- **18/09 — versão de entrega:** Yan aprovou ticket médio e formato de citação e preencheu a professora (Cláudia Osna Geber). Arquivo limpo para entrega: sem "(rascunho)" no nome, capa com "Professora", nota repetida do slide 2 removida e metadado "generated using python-pptx" apagado (autor e título agora são do Yan). PDF `YanSuyama_AS2_GestaoAnuncios.pdf` exportado e conferido. Falta só a leitura final e o envio.

## 18/09/2026 — AS2 Construção de Interfaces: versão condensada (45 → 24 páginas)

- A pedido do Yan (meta de 20 a 25 páginas). Todos os itens do enunciado, dados, falas, citações e os dois apêndices foram mantidos; apêndices idênticos.
- Cortes: perfil e principais respostas num quadro só; personas lado a lado num quadro; 8.3 a 8.5 viraram um quadro (dificuldades, sugestões, pontos positivos); 7.2 virou parágrafo; seções 5.3 e 5.4 trocaram de ordem (explicação antes do fluxo).
- Figuras: telas em grades de 3 e 4 (marcador `[[GRADE]]` no gerador); saíram as figuras de "depois" que repetiam telas da seção 6 e a tela do erro; antes e depois ficou numa figura só (passo 4 e resumo). 14 → 7 figuras.
- Diagramação: seções sem quebra de página (só apêndices em página nova), sumário em 1 página, quadros em espaçamento simples, Apêndice A em duas colunas e apêndices em 10 pt.
- Capa com **Professor: Eduardo Alexandre Franciscon** (também no `INFO.md`). Versão de 45 páginas guardada fora do repositório, na pasta temporária da sessão.

## 18/09/2026 — AS2 Construção de Interfaces: versão de entrega

- Yan aprovou o conteúdo. Limpeza para entrega: saiu o bloco de notas internas do topo do `TRABALHO.md` (a documentação dos marcadores foi para o `gerar_pdf.py`) e o código morto do aviso de pesquisa simulada.
- Frases com tom de recado ao professor reescritas sem mudar o conteúdo: "Dois cuidados declarados" virou "Cuidados na análise"; na 8.1, a limitação de 2 participantes continua explícita, sem "o enunciado pede três" e "por causa do prazo".
- Figuras sem a faixa "Protótipo acadêmico": escondida só no modo de captura (`?shot`); no site publicado ela continua. Recortes deslocados em 52 px.
- Corrigida a numeração das figuras (a do erro no campo saía como Figura 4 na página 26); agora 1 a 14 na ordem do texto.
- Capa com cidade (Leme), como nas outras AS2. Professor(a) não consta: `INFO.md` ainda sem o nome.

## 18/09/2026 — AS2: trabalho reescrito com as entrevistas reais; revisão do protótipo aguarda publicação

- **Pesquisa real:** o Yan conversou com 2 pessoas de Leme em 17/09 — P1, analista de RH de uma indústria que já é cliente da MEGA-WR (compra com processo de Compras: 3 orçamentos, CNPJ, nota, boleto faturado), e P2, dono de academia de bairro (decide e paga, só celular, desistiu pelo mínimo e pelo medo de encalhar). O registro foi estruturado por IA; entraram no trabalho só falas e observações. Trechos marcados como "[suposição]" e a reação no condicional de P2 ficaram de fora.
- **A simulação saiu por completo do PDF** (avisos vermelhos, P1/P2 simulados, Patrícia e Rafael). Novas personas: **Juliana**, a compradora da indústria, e **Marcos**, o dono da academia.
- **Declarado no método:** P1 trabalha numa empresa que já é cliente (viés); a parte da proposta foi feita com a versão preliminar, então os tempos são aproximados; o teste teve **2 participantes**, e o enunciado pede 3 (limitação registrada na seção 8.1).
- **Protótipo revisado com o feedback real** (`?v=1` = versão apresentada; sem parâmetro = revisada): bloco "Compra pela empresa" (CNPJ opcional, nota, forma de pagamento), envio por e-mail e "Baixar PDF", planilha de tamanhos, salvamento automático no aparelho, "Não sei, quero indicação" em primeiro, posição do logo opcional ("Combinar depois"), atalho "Fale direto no WhatsApp", "Quero ver tecido e modelo antes de fechar" e "Loja em Leme" junto do botão. Fluxo testado de ponta a ponta no Node.
- **Ficaram como recomendação à MEGA-WR** (dependem da empresa): faixa de preço, prazo de resposta, pré-venda com pagamento individual e legging personalizada para academias.
- **PDF:** 45 páginas, com as figuras refeitas (pares antes e depois) e recortes via `arquivo.png@y0-y1` no `gerar_pdf.py`.
- **Bloqueio na Vercel resolvido:** as publicações feitas de dentro da pasta ficavam `BLOCKED` porque a CLI anexava o commit do repositório da faculdade, e o e-mail do autor (`techgoldenia@gmail.com`) não bate com nenhuma conta do GitHub ligada à Vercel. **Solução:** fazer `vercel build --prod` na pasta e publicar com `vercel deploy --prebuilt --prod` a partir de uma cópia de `.vercel/project.json` + `.vercel/output` **fora do git** (passo a passo no `README.md` da cópia). A configuração do git não foi alterada. Revisão publicada e conferida no ar; o site oficial continua igual.

## 18/09/2026 — AS2: protótipo refeito como versão de teste do site real da MEGA-WR

- **Pedido do Yan:** criar o protótipo dentro de uma cópia do site da MEGA-WR, com toda a identidade visual, e publicar na Vercel. Regra: **não alterar o site no ar**.
- **Cópia em `AS2 - Projeto UX UI MEGA-WR/site-prototipo-megawr/`** (Astro), feita a partir de `0-Claude/Clientes/MEGA WR/Site`, que não foi tocado. Ficaram fora da cópia: `node_modules`, `dist`, `.vercel` (aponta para o projeto antigo `mega-wr`), `.env.local`, `wrangler.jsonc` (deploy do site oficial) e as notas internas.
- **O site oficial está no Cloudflare, não na Vercel** (`LANCAMENTO.md`). A versão de teste vai para um **projeto novo e separado** na Vercel, e nunca para o `mega-wr`.
- **Proteções da versão de teste:** `noindex` em todas as páginas, `robots.txt` com `Disallow: /`, sem sitemap e faixa "Protótipo acadêmico · PUCPR · versão de teste" no topo. A tela final não envia nada ao WhatsApp real, para as pessoas testando não mandarem mensagem à empresa.
- **O que foi acrescentado à cópia:** página `/orcamento` (4 passos, resumo, confirmação e pedido em grupo, com `?v=1`, `?p=` e `?linha=`); "Montar meu orçamento" no topo, no hero e no fechamento; condições abaixo do botão; "Orçar linha" nos cards; seção de dúvidas frequentes; passo 01 de "Como trabalhamos" reescrito.
- **PDF atualizado** com as telas da versão do site (`Prototipo/telas-site/`, geradas por `gerar_telas_site.py`) e com o texto das seções 5.1, 6.1, 6.2 e 7.1 ajustado. As telas do protótipo avulso (`Prototipo/index.html`, `telas/`) ficam como histórico.
- **Publicado na Vercel:** https://site-prototipo-megawr.vercel.app (conta `yansuyama-1701`, projeto novo `site-prototipo-megawr`, separado do `mega-wr`). Público, com `noindex`. O link entrou na seção 7.1 do PDF. O site oficial (megawr.com.br) foi conferido depois e está igual. Para republicar: `npx vercel deploy --prod` dentro de `site-prototipo-megawr/`, que agora está ligado ao projeto novo.

## 16/09/2026 — AS2 de Construção de Interfaces: versão preliminar completa, com pesquisa simulada

- **Decisão do Yan:** montar o trabalho inteiro com entrevistas simuladas, com aviso em vermelho antes da pesquisa, para mostrar a proposta ao professor. Depois, fazer as conversas reais apresentando a solução como sugestão e refazer as seções que dependem de usuário.
- **Por que "simulada":** as respostas enviadas batiam com as proto-personas escritas em 14/09 (nome, idade, cargo, cidade, 14 pessoas, COREN) e comentavam um protótipo que ainda não existia. Não usar esse conteúdo como pesquisa real.
- **Aviso no PDF:** caixa vermelha no início da seção 2 e aviso curto nas seções 3, 4, 7.3, 8 e no Apêndice B. Nas tabelas de teste, só entrou o que a simulação trazia: tempo "não medido" e P3 "a realizar".
- **Diagnóstico corrigido no ar:** são 8 links de WhatsApp com a mesma mensagem (4 "Solicitar orçamento", 2 no telefone, "Fale com a gente", "Falar no WhatsApp"), e não 8 botões iguais. O mínimo de 10 peças aparece só na descrição lida pelo Google. O botão do site é azul, e o protótipo seguiu essa cor.
- **Solução:** orçamento guiado em 4 passos que termina no WhatsApp com a mensagem pronta. A versão 2, revisada após o feedback, trouxe pedido em grupo, "ainda não tenho os tamanhos" com Salvar, mínimo e prazo junto do botão, e baixar ou copiar o resumo. Faixa de preço e preço para poucas peças ficaram como recomendação à MEGA-WR.
- **Produzido:** `Prototipo/index.html` (navegável, `?v=1` e `?v=2`), 15 telas em `Prototipo/telas/`, `Entrega/YanSuyama_ProjetoUXUI.pdf` (38 páginas, ABNT, sumário numerado), sitemap e fluxograma em SVG. Para regerar: `gerar_telas.py` e depois `gerar_pdf.py`. O `TRABALHO.md` é a fonte do PDF.
- **Citações:** só unidades da disciplina (PUCPR, [2026?]a–f), o site da MEGA-WR, WCAG 2.2 (versão de 12/12/2024, conferida) e LGPD, art. 6º, III (conferida no Planalto). Os livros da bibliografia não foram citados porque não foram lidos.
- **Roteiro reescrito** para a sessão real com 3 pessoas: parte exploratória → site atual cronometrado → proposta como sugestão ("o que você mudaria?"). Questionário corrigido: diz "8 perguntas".
- **Protótipo sem link público:** usa a marca de um cliente real, então a forma de hospedar fica a critério do Yan. No PDF, o link está como `[INSERIR LINK]`.
- **Inconsistência em `0-Claude/Clientes/MEGA WR/DOCUMENTO-INSTITUCIONAL.md`:** o resumo executivo diz mínimo de 12 peças e a seção 6 diz 10. Usei 10, que é o valor confirmado.
- **Pendências:** 3 conversas reais; conversa com William e Rosangela (volume abaixo de 10 peças, faixa de preço, taxa de arte, pedido em grupo); link do protótipo; enunciado e prazo não salvos na pasta; `AS2 - Projeto UX UI MEGA-WR (rascunho).docx` está desatualizado.

## 14/09/2026 — AS2 de Construção de Interfaces: Projeto UX/UI da MEGA-WR

- Trabalho: processo de design completo documentado em PDF único (`YanSuyama_ProjetoUXUI.pdf`). Pasta própria em `Construção de Interfaces e Experiência do Usuário/AS2 - Projeto UX UI MEGA-WR/`.
- **Tema escolhido:** o fluxo de solicitação de orçamento do site da MEGA-WR. Decisão do Yan entre três opções (a outra forte era a aprovação de conteúdo agência-cliente na Drip-Plan).
- **Descoberta que mudou o recorte:** a MEGA-WR **já tem site** (`megawr.com.br`) — o `DOCUMENTO-INSTITUCIONAL.md` em `0-Claude` está desatualizado nesse ponto (registrava "não possui (a criar)", 04/08/2026). Como existe site no ar, o trabalho ganhou avaliação heurística do estado atual e base comparativa antes/depois, em vez de projeto do zero.
- **Diagnóstico levantado na página (verificado, não suposto):** one-page em Astro com as âncoras `#topo`, `#linhas`, `#personalizacao`, `#clientes`, `#sobre`; **8 botões "Solicitar orçamento", todos para o mesmo link** `wa.me/5519991336523` com mensagem pré-preenchida idêntica; sem formulário; **pedido mínimo de 10 peças não informado em lugar nenhum**; prazo de 20 a 30 dias informado. O site anuncia "Você conta o que precisa" como etapa 1 do processo mas não oferece onde contar.
- **Contradições no enunciado** (ele traz duas listas de requisitos que divergem): wireframes "média ou alta" × "alta" fidelidade; teste com "duas" × "três" pessoas. Regra adotada: seguir sempre o mais exigente — alta fidelidade e 3 participantes. A segunda lista ainda exige resultado quantitativo (tempo de tarefa e satisfação), o que a primeira não pede.
- **Decisão de ferramenta do Yan:** produzir wireframes e protótipo aqui, sem Figma. Risco registrado com ele — o item 3.2 nomeia Figma/XD/Sketch explicitamente. Mitigação disponível se quiser depois: plugin html.to.design para importar as telas prontas ao Figma.
- Criados `TRABALHO.md` (11 seções, com contexto e avaliação heurística já em rascunho e marcadores `[AGUARDA PESQUISA]` no que depende de gente real) e `Pesquisa/ROTEIRO-entrevista.md` (recrutamento, entrevista em 4 blocos, tarefa de observação no site atual e ficha de registro).
- **Caminho crítico é do Yan:** 2 entrevistas e 3 testes de protótipo com pessoas reais (família e amigos). Nada de persona ou resultado de teste inventado — além de fraude acadêmica, é o que denuncia trabalho genérico.

## 09/09/2026 — Pasta versionada no GitHub

- `git init` na raiz e push para **`techgoldenia-coder/Faculdade`** — repositório **privado** (confirmado: a API do GitHub responde 404 sem autenticação). O repo estava vazio; este é o commit inicial.
- 77 arquivos versionados, 94 MB. Maior arquivo: `Gestão de marcas 5.pdf` (16,1 MB) — abaixo do limite de 100 MB do GitHub, sem necessidade de Git LFS.
- Criados `README.md` (capa do repositório, aponta para PAINEL/ESTRUTURA/HISTORICO) e `.gitignore` (lixo do Windows, arquivos de bloqueio `~$` do Office).
- **A visibilidade privada é requisito, não preferência:** o repositório contém os PDFs das unidades da PUC-PR (© PUCPR — Todos os direitos reservados) e dados institucionais reais da MEGA-WR usados na AS1 de plano de mídia. Registrado como regra no `CLAUDE.md`.

## 08/09/2026 — AS1 de Gestão de Anúncios: Plano de Mídia MEGA-WR

- Trabalho em grupo da semana 4. Cliente escolhido: **MEGA-WR Confecções** (Leme/SP), linha Fitness — camiseta dry fit e calça legging.
- **Premissa do exercício definida pelo Yan:** campanha fictícia, com estoque a pronta-entrega atendendo consumidor final e empresas com personalização. Isso flexibiliza o pedido mínimo de 10 peças da operação real. A premissa está declarada no corpo do documento.
- Estrutura: híbrido B2C (varejo pronta-entrega) + B2B (personalização para academias), objetivo macro único. Período 01/11/2026 a 31/01/2027 (Black Friday + Natal + pico de matrículas de janeiro). Conceito: "Feito aqui, para treinar aqui".
- 3 mídias: Meta Ads (R$ 5.400), mídia exterior outdoor/busdoor (R$ 3.300), Google Ads pesquisa (R$ 2.400) + produção (R$ 900). Total R$ 12.000 — **verba arbitrada e declarada como premissa**, não cotação.
- Entregues dois arquivos em `AS1 - Plano de Mídia MEGA-WR/`: o template oficial da PUC preenchido (.docx) e a planilha operacional (.xlsx, abas Verba / Cronograma / Indicadores com fórmulas).
- **Peças ilustrativas produzidas** (o template exige imagens em cada mídia): 3 mockups em `Imagens/` gerados com PIL a partir dos ativos reais do cliente (logo oficial e foto `Fitness.jpg`) — anúncio Meta feed+stories, simulação de resultado de busca do Google e aplicação de outdoor+busdoor. Inseridas no .docx com legenda acima e fonte abaixo, conforme NBR 14724.
- Base do plano: dados institucionais reais da MEGA-WR (`0-Claude/Clientes/MEGA WR/DOCUMENTO-INSTITUCIONAL.md`) + etapas do plano de mídia da Unidade 02 + modelo da videoaula da semana 2.

## 08/09/2026 — AS1 de duas matérias: nota 10 nas duas

- **Construção de Interfaces e Experiência do Usuário** — AS1 nota 10. Questões conferidas aqui: 2 (hierarquia da informação), 3 (mapa de site), 5 (métodos de pesquisa), 8 (heurísticas de Nielsen), 9 (princípios visuais de Robin Williams).
- **Gestão de Conteúdo em Mídias Sociais** — AS1 nota 10. Questões conferidas aqui: 1 (marketing de conteúdo), 4 (social listening), 8 (territórios de conteúdo), 9 (arquétipos), 10 (guia de identidade).
- Justificativas e citações do material em `AS1 - Respostas e justificativas.md` na raiz de cada matéria.
- **Método que funcionou:** localizar o trecho exato no PDF da unidade antes de responder, em vez de responder por conhecimento geral de marketing. Em quase toda questão a alternativa correta reproduzia a definição do professor quase literalmente. Repetir isso nas próximas AS.

## 08/09/2026 — Matéria Gestão de Conteúdo em Mídias Sociais (2026/2)

- Terceira matéria de 2026/2, também já com os 8 PDFs soltos na pasta; movidos para `Base de dados/`.
- `INFO.md` preenchido com ementa, as 8 unidades e a bibliografia (9 livros completos + 2 truncados + 9 artigos/vídeos com URL cortada na extração).
- Sem videoaula transcrita ainda.

## 08/09/2026 — Matéria Gestão de Anúncios em Canais Sociais (2026/2)

- Segunda matéria de 2026/2. Pasta já criada pelo Yan com os 8 PDFs; movidos para `Base de dados/`.
- Nome oficial é **Canais Sociais**, não "redes sociais" — registrado no `INFO.md` para uso em capa de trabalho.
- Salvas as transcrições das videoaulas 02 a 08 em `Base de dados/Transcrições das videoaulas (bruta).md`. Timestamps removidos por regex (234 linhas), **nenhuma palavra alterada**.
- **A transcrição é ASR de qualidade muito ruim** e erra termos técnicos centrais. No cabeçalho do arquivo separei o que foi **verificado contra o texto dos slides** (outbound, inbound, push, pull, dados contextuais) do que é **inferência minha ainda não conferida** (first party data, testes A/B, Casey Neistat, Coca-Cola Journey, SEO, relatório da Meta), estes marcados `[VERIFICAR]`. Arquivo marcado como não citável em trabalho.
- `INFO.md` preenchido: ementa, tabela das 8 unidades cruzando título do PDF com tema da videoaula, e 15 referências da bibliografia.
- Ao banco de referências entraram só as 3 referências completas (Centa/Junior, Turchi, Oliver). As truncadas ficaram no `INFO.md` da matéria, marcadas com o que falta.

## 08/09/2026 — Matéria Construção de Interfaces e Experiência do Usuário (2026/2)

- Primeira matéria de 2026/2. O Yan foi soltando os PDFs durante a sessão; chegaram as 8 unidades (disciplina completa), todas movidas para `Base de dados/`.
- **Descoberta importante:** `pdftotext` está disponível no ambiente — dá para ler o texto dos PDFs direto, sem print. Mas **componentes interativos da plataforma PUC-PR não saem na extração** (foi o caso das 10 heurísticas e das 8 regras de ouro). Para esses, o print continua sendo necessário.
- Salva a transcrição das listas enviadas por print em `Base de dados/Unidade 02 - Heurísticas de Nielsen e Regras de Shneiderman.md` — única cópia desse conteúdo.
- `INFO.md` preenchido com ementa, as 3 unidades e seus tópicos, e a bibliografia extraída das referências dos PDFs.
- 8 referências ABNT da matéria adicionadas ao `BANCO-DE-REFERENCIAS.md`, já com a unidade de origem.

## 08/09/2026 — Estrutura inicial da pasta

Pasta `3 - Faculdade` estava vazia. Montada do zero.

- **Material migrado:** 23 PDFs (46 MB) de `Desktop/Yan - Marketing/PUC` para as pastas de matéria. Contagem e tamanho conferidos na origem e no destino antes de remover as pastas vazias; a pasta `Yan - Marketing/PUC` deixou de existir.
- **Organização por matéria** (não por semestre — decisão do Yan: matéria é a unidade que ele procura). Três matérias na raiz, cada uma com `INFO.md` + `Base de dados/`. Trabalhos e anotações ficam soltos na raiz da matéria, com prefixo no nome para ordenar.
- Criado `CLAUDE.md` com contexto do curso (Bacharelado em Marketing, PUC-PR) e as regras de como ajudar nos dois modos: estudar e produzir trabalhos.
- Criado `PAINEL.md` na raiz — índice de matérias, prazos, datas e notas em um lugar só.
- `0 - Institucional/`: `Normas-ABNT.md` escrito com conteúdo real (formatação, NBR 10520, NBR 6023); `Grade-Curricular.md` e `BANCO-DE-REFERENCIAS.md` como esqueleto.
- `1 - Modelos/`: modelos de INFO, anotação de aula, trabalho e resumo de prova + `_MODELO-MATERIA/` para clonar.

> Nota: a primeira versão da estrutura era por semestre (`1 - Semestres/2026-1/...`) com `2 - Biblioteca/` global. Descartada no mesmo dia a pedido do Yan. Se aparecer referência a esses caminhos em algum arquivo, está obsoleta.

### Pendências

- Cadastrar as **demais** matérias de 2026/2 (copiar `1 - Modelos/_MODELO-MATERIA/`, renomear, preencher `INFO.md`, adicionar linha no `PAINEL.md`).
- Preencher `Grade-Curricular.md` (período atual e grade oficial) e as datas do semestre no `PAINEL.md`.
- Preencher professor, ementa e notas nos `INFO.md` das três matérias de 2026/1.
- `Gestão de marcas/Base de dados/Branding.pdf` — confirmar se é livro/apostila de referência.
- Definir destino do material de faculdade solto na Desktop: `Trabalho pensamento criativo.pdf` (2024, 345 KB) e `Mapa pensamento criativo.pptx` / `Template de Entrega e Orientações AS 2_Ambiente Macroeconômico.docx` (ambos com 0 byte — provavelmente placeholders de nuvem ou arquivos corrompidos).
