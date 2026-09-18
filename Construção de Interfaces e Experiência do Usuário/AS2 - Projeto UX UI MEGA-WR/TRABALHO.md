---
titulo: Repensando a solicitação de orçamento da MEGA-WR
subtitulo: projeto de UX/UI do fluxo de orçamento de uma confecção de uniformes
aluno: Yan Suyama
curso: Bacharelado em Marketing
disciplina: Construção de Interfaces e Experiência do Usuário
professor: Eduardo Alexandre Franciscon
instituicao: Pontifícia Universidade Católica do Paraná
cidade: Leme
ano: 2026
---

# 1 Entendendo o problema e o usuário

## 1.1 Contexto

A MEGA-WR Confecções é uma confecção familiar de Leme/SP, dos proprietários William e Rosangela, que atua há cerca de dez anos no segmento com três linhas: Saúde (jalecos e scrubs), Uniformes (profissional, escolar, esportivo e industrial) e Fitness (leggings, bermudas e camisetas dry-fit). O foco é o cliente empresarial, como escolas, empresas, clínicas e academias. Segundo os proprietários, três condições comerciais moldam o projeto: **pedido mínimo de 10 peças por modelo**, **prazo de 20 a 30 dias** e **ausência de tabela de preço**, já que cada orçamento depende de modelo, tecido, quantidade e personalização. O atendimento é feito na loja e pelo WhatsApp, e o site institucional fica em megawr.com.br (MEGA-WR CONFECÇÕES, 2026).

## 1.2 O problema observado

O site apresenta bem a empresa, mas falha no momento em que o visitante decide pedir orçamento. O levantamento abaixo foi feito na página publicada, em 16 de setembro de 2026.

[[QUADRO: Diagnóstico do site atual no momento da conversão]]

| Ponto verificado | Situação encontrada |
|---|---|
| Links de contato | **8 links** para o mesmo WhatsApp, com rótulos diferentes: "Solicitar orçamento" (4), o número de telefone (2), "Fale com a gente" e "Falar no WhatsApp" |
| Mensagem que o usuário envia | Idêntica nos 8: *"Olá! Vim pelo site e gostaria de solicitar um orçamento de uniformes."* |
| Formulário ou fluxo de orçamento | Não existe |
| Pedido mínimo de 10 peças | **Não aparece em nenhum texto visível**, só na descrição lida pelos buscadores |
| Prazo de produção | Informado (20 a 30 dias), na seção "Como trabalhamos" |

[[FONTE: Elaborado pelo autor com base em MEGA-WR Confecções (2026).]]

O próprio site anuncia como primeira etapa **"Você conta o que precisa"**, mas não oferece lugar para contar. Qualquer botão leva o visitante a uma conversa de WhatsApp com uma frase genérica, que ele não escreveu, e ele precisa descrever do zero, de memória, tudo o que acabou de ver. **O cliente** não sabe se a quantidade dele é aceita nem que informações passar; **a empresa** recebe sempre a mesma mensagem e precisa de várias perguntas de ida e volta antes de conseguir orçar.

[[FIG: site-atual-hero.png | Primeira tela do site atual no celular: o botão "Solicitar orçamento" leva direto ao WhatsApp | Captura de tela do autor em MEGA-WR Confecções (2026). | 4cm]]

**Recorte do projeto:** redesenhar a solicitação de orçamento do site. O WhatsApp continua sendo o canal de negociação, porque é o canal real da empresa, mas o cliente passa a chegar nele com o pedido já organizado.

## 1.3 Avaliação heurística do estado atual

Antes de ouvir os usuários, o site foi avaliado pelas 10 heurísticas de usabilidade de Jakob Nielsen (PUCPR, [2026?]a). A Unidade 06 recomenda essa ordem: a avaliação heurística corrige problemas básicos com mais rapidez e evita gastar a conversa com erros já conhecidos (PUCPR, [2026?]e).

[[QUADRO: Avaliação heurística do fluxo de orçamento no site atual]]

| # | Heurística | Situação no site atual | Gravidade |
|---|---|---|---|
| 1 | Visibilidade do *status* do sistema | Não há fluxo nem progresso visível; o clique troca o usuário de aplicativo sem aviso | Alta |
| 2 | Correspondência com o mundo real | Boa nas linhas de produto; falha em "DTF", termo técnico sem explicação | Média |
| 3 | Controle e liberdade do usuário | Depois de ir ao WhatsApp, não há como revisar ou corrigir o pedido no site | Alta |
| 4 | Consistência e padrões | Oito links com rótulos diferentes geram a mesma mensagem, qualquer que seja a seção de origem | Média |
| 5 | **Prevenção de erros** | **O pedido mínimo não aparece na página**; a restrição só surge na conversa | **Alta** |
| 6 | Reconhecimento em vez de memorização | O usuário precisa lembrar e redigir o que viu | Alta |
| 7 | Flexibilidade e eficiência de uso | Caminho único para cliente recorrente e visitante de primeira vez | Média |
| 8 | Estética e *design* minimalista | Página limpa, com boa hierarquia e fotos reais: ponto forte do site | Baixa |
| 9 | Ajuda para reconhecer e corrigir erros | Sem formulário, não há validação nem mensagem de erro | Média |
| 10 | Ajuda e documentação | Não há perguntas frequentes sobre mínimo, entrega, preço e tipos de personalização | Alta |

[[FONTE: Elaborado pelo autor com base em PUCPR ([2026?]a).]]

# 2 Pesquisa com usuários

## 2.1 Método

A pesquisa usou **entrevista semiestruturada**, com perguntas abertas, combinando os dois tipos descritos na Unidade 03: a **exploratória**, para entender o contexto e os problemas, e a **de validação**, aplicada sobre um protótipo ou conceito (PUCPR, [2026?]b). Cada conversa teve cinco partes: aquecimento e perfil; a última experiência real de orçamento sob medida, sempre sobre o que aconteceu e nunca sobre o que a pessoa faria; a tentativa de pedir orçamento no site atual, falando em voz alta e sem ajuda; a apresentação da proposta como sugestão; e o fechamento. O roteiro está no Apêndice A e o registro das conversas, no Apêndice B.

**Participantes:** duas pessoas de Leme/SP, conhecidas do autor, com compras sob medida recentes e perfis deliberadamente diferentes, entrevistadas individualmente em 17 de setembro de 2026 e identificadas como P1 e P2 para preservar a identidade. **Cuidados na análise:** P1 trabalha em uma indústria que já é cliente da MEGA-WR, por isso a análise deu mais peso ao que ela fez e relatou do que às opiniões sobre a empresa; e a proposta foi mostrada em **versão preliminar**, um dia antes da publicação do protótipo navegável final, por isso os tempos dessa etapa são aproximados.

## 2.2 Perfil e principais respostas

[[QUADRO: Perfil dos participantes e principais respostas]]

| | P1 (compra de empresa) | P2 (academia) |
|---|---|---|
| Perfil | 33 anos, analista de RH em indústria de Leme/SP; organiza SIPAT, eventos e ações internas | 47 anos, dono de academia de bairro em Leme/SP, com cerca de 250 alunos e 4 professores |
| Como compra | Acima de certo valor, Compras exige 3 orçamentos e fornecedor com CNPJ. Compra sob medida 4 a 5 vezes por ano, pelo computador e WhatsApp Web ("na fábrica tem área em que nem pode entrar com celular") | Ele mesmo decide e paga. Compra sob medida uma vez por ano, "se muito", só pelo celular, entre uma aula e outra |
| Caso relatado | 180 camisetas da SIPAT, em agosto. Procurou fornecedores no Google, no Instagram e no grupo de RH da região | 5 camisetas dry-fit para os professores, pensando em vender aos alunos. Achou o fornecedor pelo Instagram de outra academia |
| O contato | Um fornecedor respondeu com áudio de dois minutos, com o preço no meio; outro mandou o preço sem o prazo, "e o prazo pra mim é o que mais importa". Teve preço do mesmo dia a cinco dias úteis | Perguntou "quanto fica camiseta com logo?" e recebeu, no dia seguinte, perguntas sobre quantidade, tecido, tamanho e cores: "Eu não sabia metade" |
| Onde travou | "Silk ou DTF?": respondeu "o que for melhor", "que é a pior resposta", e cada fornecedor orçou uma coisa diferente | "Tecido? Eu achei que dry-fit era o tecido." E o tamanho dos alunos: "Eu lá sei?" |
| O que descobriu tarde | Fotolito cobrado à parte e pagamento 50% adiantado, quando a empresa paga com boleto em 28 dias | Mínimo de 30 peças, taxa do "molde" do logo e frete |
| Desfecho | Descartou um fornecedor que não emitia nota no valor: "Não dá pra cadastrar" | Desistiu pelo mínimo e pelo medo de encalhar; fez 5 numa loja do centro, e "a estampa já tá rachando" |
| O que mudaria | "Receber tudo num formato só. Preço, prazo, pagamento, o que está incluso. Num PDF que eu anexo e pronto" | "Se tivesse como os alunos encomendarem direto, cada um escolhendo o tamanho e pagando o seu, eu fazia 50 camisetas amanhã" |

[[FONTE: Elaborado pelo autor com base nas entrevistas.]]

## 2.3 Padrões e problemas recorrentes

Seguindo o caminho da Unidade 03, em que os dados revelam padrões e os padrões geram *insights* (PUCPR, [2026?]b), as respostas foram agrupadas em seis padrões:

1. **A pergunta técnica trava o pedido.** Nenhum dos dois sabia responder sobre técnica ou tecido, e quem responde "o que for melhor" recebe orçamentos que não se comparam.
2. **Custos e condições aparecem tarde.** Fotolito, molde, frete, pagamento adiantado e mínimo só surgiram depois do primeiro contato.
3. **O tamanho é sempre a última informação.** P1 depende de uma planilha dos supervisores, que leva uma semana; P2 não sabe a numeração dos alunos.
4. **O formato da resposta pesa tanto quanto o preço.** P1 precisa de um documento para anexar ao pedido de compra; áudio não serve.
5. **O risco decide.** Para a empresa, o risco é o prazo e o documento; para o pequeno empresário, o estoque encalhado.
6. **Ser de Leme conta.** Os dois valorizaram poder ir até a loja, e P1 notou que "isso é um ponto forte e ninguém fala".

Com dois participantes, esses padrões são **indícios fortes, e não conclusões generalizáveis**. O que só a empresa pode responder, como nota, boleto faturado e faixa de preço, fica para uma conversa com os proprietários (seção 10).

# 3 Personas

Personas são personagens semifictícios que representam grupos de usuários com objetivos, comportamentos e dores semelhantes, criados com base em dados reais (PUCPR, [2026?]b). As duas abaixo sintetizam P1 e P2, com nomes fictícios.

[[QUADRO: Personas]]

| | Juliana, a compradora da indústria (B2B) | Marcos, o dono da academia (pequeno negócio) |
|---|---|---|
| Em uma frase | *"Receber tudo num formato só [...] Num PDF que eu anexo e pronto."* | *"O problema não é pagar, é eu ficar no meio."* |
| Perfil | 34 anos, analista de RH de uma indústria de Leme/SP. Organiza a SIPAT, as campanhas internas e a confraternização. Não decide sozinha: acima de certo valor, a compra passa pelo setor de Compras | 47 anos, dono de academia de bairro em Leme/SP há nove anos. Dá aula de manhã, cuida do caixa e da manutenção. Decide e paga sozinho |
| Contexto de uso | No computador do trabalho, com o WhatsApp Web aberto, precisa de 180 camisetas para a SIPAT, que tem data marcada, e de três orçamentos. Os tamanhos só chegam uma semana depois | Pelo celular, entre uma aula e outra, quer camisetas dry-fit pretas com o logo para os professores e pensa em vender aos alunos |
| Objetivos | Três orçamentos comparáveis; entrega antes do evento; fornecedor que Compras aceite cadastrar | Uniformizar a equipe com uma peça que aguente o uso diário; vender aos alunos sem risco de encalhar |
| Necessidades | Informar data limite, CNPJ, nota fiscal e boleto faturado; mandar os tamanhos depois; receber a proposta em PDF ou por e-mail; ver amostra antes de um pedido grande | Saber o mínimo e o preço aproximado antes de preencher tudo; receber indicação do que é melhor para academia; pausar e continuar depois; deixar cada aluno escolher e pagar a sua peça |
| Frustrações | Preço dentro de áudio; proposta sem prazo; custos cobrados à parte; pagamento adiantado, que "trava tudo no financeiro"; ter de cobrar o fornecedor | Perguntas técnicas; taxas e frete que aparecem no fim; o medo de preencher tudo "e aí é caro"; a estampa barata que racha |
| Hábitos digitais | Computador e WhatsApp Web o dia inteiro; pesquisa no Google, no Instagram e no grupo de RH da região | Só celular; descobre fornecedores pelo Instagram de outras academias e confia em quem é da cidade: "Se é daqui, eu posso passar lá e olhar" |

[[FONTE: Elaborado pelo autor com base nas entrevistas.]]

Juliana representa a **compra com processo formal**, com regras, documentos e fornecedores comparados lado a lado; Marcos, a **compra de quem arrisca o próprio dinheiro**, em que pesam preço, mínimo e estoque. Em comum, os dois dependem de outras pessoas para fechar o pedido: os supervisores e os alunos.

# 4 Insights e definição do problema

## 4.1 Principais aprendizados

Além dos padrões da seção 2.3, a pesquisa trouxe quatro aprendizados que mudaram o rumo do projeto:

1. **Para empresa, as condições vêm antes do preço.** CNPJ, nota fiscal, forma de pagamento e prazo decidem se o fornecedor pode ser contratado: "Pra empresa isso vem antes do preço" (P1).
2. **O problema do mínimo é o risco, não o número.** P2 desistiu de 30 peças, mas faria 50 se cada aluno escolhesse e pagasse a sua.
3. **O fluxo organiza, mas demora.** Os dois acharam a proposta mais demorada que o botão atual; o atalho para quem só quer conversar precisa continuar existindo.
4. **Ser da cidade é argumento de venda.** A loja em Leme dá confiança e permite ver o tecido, e o site quase não fala disso.

## 4.2 Problemas identificados

O quadro cruza a pesquisa com o diagnóstico heurístico da seção 1.3. A prioridade segue o critério da Unidade 06: primeiro o que impede a tarefa, depois o que gera frustração (PUCPR, [2026?]e).

[[QUADRO: Problemas priorizados]]

| Problema | Evidência na pesquisa | Heurística | Prioridade |
|---|---|---|---|
| Condições essenciais invisíveis (mínimo, nota, prazo) | P1: "Eles emitem nota? Qual o prazo pra 15? Tem pedido mínimo?"; P2: "E faz 4?" | 5 e 10 | Crítica |
| Cliente não sabe o que informar | P1: "eu ia ficar olhando pro WhatsApp em branco"; P2: "Eu não sabia metade" | 6 | Crítica |
| Sem espaço para as condições de compra de empresa | P1: CNPJ, nota, boleto e 3 orçamentos | 7 | Crítica para B2B |
| Termos técnicos sem indicação de uso | P1: "o que for melhor"; P2: "qual é o melhor pra camiseta que vai suar todo dia?" | 2 | Alta |
| Tarefa longa sem como pausar | P1 espera uma semana pelos tamanhos; P2 responde entre uma aula e outra | 3 e 7 | Alta |
| Custos e preço desconhecidos até o fim | P2: "preenche tudo e aí é caro"; taxas de molde e tela nos dois casos | 10 | Alta, depende da empresa |
| Proposta que não se anexa nem se compara | P1: áudio com o preço no meio | — | Média |

[[FONTE: Elaborado pelo autor.]]

## 4.3 Oportunidades de melhoria

1. **Orçamento guiado em quatro passos**, que termina com uma mensagem organizada e igual para qualquer fornecedor que a cliente queira comparar.
2. **Condições visíveis antes do primeiro contato:** mínimo, prazo, "sem cadastro" e loja em Leme, junto do botão principal e nas perguntas frequentes.
3. **Bloco opcional "Compra pela empresa"**, com CNPJ, nota fiscal e forma de pagamento preferida.
4. **"Não sei, quero indicação" como primeira opção de personalização**, para que a dúvida técnica vire pedido de ajuda.
5. **Pausar sem perder nada:** informar só o total, enviar a planilha de tamanhos depois e ter o pedido salvo automaticamente.
6. **Envio por WhatsApp ou e-mail, com resumo em PDF**, no celular e no computador.
7. **Pedido em grupo**, para quem não chega sozinho ao mínimo, como equipes e alunos.
8. **Atalho "Fale direto no WhatsApp"** para quem tem pressa.

## 4.4 Declaração do problema

> **Juliana** precisa receber orçamentos completos e no mesmo formato, porque o setor de Compras só aceita propostas comparáveis, com CNPJ, nota, pagamento e prazo. **Mas hoje** manda uma mensagem genérica e recebe áudios, preços sem prazo e custos que só aparecem depois.

> **Marcos** precisa saber logo se o pedido cabe no mínimo e no bolso, porque é ele quem arrisca o dinheiro e o estoque. **Mas hoje** só descobre mínimo, taxas e preço depois de responder uma lista de perguntas técnicas.

**Pergunta que orienta a solução:** como fazer cada cliente chegar à MEGA-WR com um pedido completo e comparável, sabendo antes o que é atendido, sem tirar o atalho de quem só quer conversar?

# 5 Estruturação da solução

## 5.1 Organização do conteúdo

A Unidade 04 apresenta a organização por categorias temáticas e por tarefas (PUCPR, [2026?]c). O site atual usa só a primeira, com as linhas de produto; a proposta mantém as categorias e acrescenta uma **entrada por tarefa**, "Montar meu orçamento", rótulo que antecipa que a pessoa vai preencher algo antes da conversa, ao contrário de "Solicitar orçamento".

[[QUADRO: Onde cada informação passa a aparecer]]

| Informação | Onde aparece na proposta | Por quê |
|---|---|---|
| Mínimo, prazo e loja em Leme | Abaixo do botão principal, no passo 2 e nas perguntas frequentes | P1 e P2 procuraram no site atual e não encontraram; os dois valorizaram o fornecedor local |
| Linhas de produto | Cards da página inicial, cada um com o atalho "Orçar linha" | P2 foi direto à linha Fitness: começar com ela selecionada economiza um passo |
| Bordado, silk e DTF | Passo 3, com "Não sei, quero indicação" em primeiro, e nas perguntas frequentes | Os dois não sabiam escolher a técnica |
| Tecido | Não é perguntado; a MEGA-WR indica no orçamento | P2 "achou que dry-fit era o tecido"; é decisão técnica do fornecedor |
| CNPJ, nota e pagamento | Passo 4, só para quem marca "Compra pela empresa" | Para P1, "vem antes do preço"; para pessoa física, não aparece |
| Preço | O resumo explica como o valor é calculado | Sem tabela, o site não promete o que não pode cumprir |
| WhatsApp direto | Passo 1 ("Com pressa?"), fechamento da página e rodapé | Os dois acharam o fluxo mais demorado que um toque só (heurística 7) |

[[FONTE: Elaborado pelo autor.]]

## 5.2 Mapa de navegação (sitemap)

A página inicial continua sendo uma página única, com seções acessadas por âncora. A novidade é o ramo **/orcamento**, com quatro passos e resumo, e a página de **pedido em grupo**, aberta a partir do passo 2. O WhatsApp e o e-mail da MEGA-WR passam a ser o fim do fluxo, e não mais o começo.

[[FIG: sitemap.svg | Mapa do site proposto | Elaborado pelo autor. | 15cm]]

## 5.3 Como a estrutura facilita a navegação

- **Um passo, um assunto.** Produto, quantidade, personalização e entrega em passos separados reduzem a carga de memória, oitava regra de ouro de Shneiderman (PUCPR, [2026?]a), e deixam claro o que falta.
- **Profundidade curta.** Todo o conteúdo institucional continua a um toque da página inicial, e "Orçar linha" elimina um passo para quem já escolheu (PUCPR, [2026?]c).
- **O erro é evitado antes de acontecer.** O pedido mínimo é verificado no passo 2, enquanto a pessoa escolhe as quantidades, e não depois do envio.
- **Diálogo com fechamento e um caminho para cada ritmo.** Resumo, mensagem visível e tela de próximos passos dão início, meio e fim à tarefa, quarta regra de ouro de Shneiderman (PUCPR, [2026?]a); o atalho para o WhatsApp atende quem só quer conversar (heurística 7).

## 5.4 Fluxo de uso

[[FIG: fluxo.svg | Fluxo de solicitação de orçamento, com pontos de decisão e tratamento de erro | Elaborado pelo autor. | 12.5cm]]

# 6 Wireframes

## 6.1 Telas

As telas foram desenhadas em **alta fidelidade** (PUCPR, [2026?]c) **dentro de uma cópia do próprio site da MEGA-WR**, com cabeçalho, fontes, cores e componentes reais, para que a proposta fosse avaliada com a cara da marca. Foram projetadas primeiro para o celular, aparelho de P2; no computador, como P1 precisava, o mesmo fluxo se ajusta à tela. As figuras mostram a versão revisada após a pesquisa.

[[QUADRO: Telas do projeto e heurística que cada uma endereça]]

| Tela | O que resolve | Heurística principal |
|---|---|---|
| Página inicial | Botão principal com mínimo, prazo, "sem cadastro" e loja em Leme; atalho por linha | 5, prevenção de erros |
| Perguntas frequentes | Respostas às dúvidas que hoje chegam pelo WhatsApp | 10, ajuda e documentação |
| Passo 1: produto | Escolha visual da linha e do modelo; atalho para o WhatsApp | 6, reconhecimento |
| Passo 2: quantidade | Medidor do pedido mínimo em tempo real e opção "Ainda não tenho os tamanhos" | 5, prevenção de erros |
| Passo 3: personalização | Indicação em primeiro lugar, técnica explicada pela descrição e posição opcional | 2, linguagem do usuário |
| Passo 4: entrega e contato | Dados mínimos, bloco opcional para empresa e erro indicado no próprio campo | 9, mensagens de erro claras |
| Resumo | "Editar" em cada item, prévia da mensagem, PDF e envio por WhatsApp ou e-mail | 3, controle e liberdade |
| Abaixo do mínimo e pedido em grupo | Explica a regra e oferece saídas, como juntar equipe ou alunos | 9 e 7 |
| Confirmação | Código do pedido e próximos passos | 1, visibilidade do *status* |

[[FONTE: Elaborado pelo autor.]]

[[GRADE: 01-home-v2.png@0-1640 ; 03-passo1-produto.png@0-1590 ; 04-passo2-ok.png@0-1640 | Página inicial ; Passo 1: produto ; Passo 2: quantidade | Página inicial e passos 1 e 2 do orçamento | Elaborado pelo autor. | 3 | 4.6cm | alinhar]]

[[GRADE: 07-passo3-personalizacao-v2.png@0-1640 ; 08-passo4-entrega-v2.png@0-1610 ; 09-resumo-v2.png@0-1585 | Passo 3: personalização ; Passo 4: entrega e contato ; Resumo | Passos 3 e 4 e resumo do pedido | Elaborado pelo autor. | 3 | 4.6cm | alinhar]]

[[GRADE: 02-faq.png ; 05-passo2-abaixo-minimo.png@0-1980 ; 11-pedido-em-grupo.png@0-1980 ; 10-confirmacao.png@0-2000 | Perguntas frequentes ; Abaixo do mínimo ; Pedido em grupo ; Confirmação | Ajuda, caminhos alternativos e confirmação | Elaborado pelo autor. | 4 | 3.7cm | alinhar]]

## 6.2 Padrões de interface

**Cores.** A paleta usa as cores institucionais da MEGA-WR, e todas as combinações de texto passam no contraste mínimo de 4,5:1 do nível AA da WCAG 2.2 (W3C, 2024).

[[QUADRO: Paleta e contraste]]

| Cor | Uso | Contraste sobre branco |
|---|---|---|
| Azul `#1F3F9C` | Botão principal (um por tela), item selecionado, links e mínimo atingido | 9,3:1 |
| Vermelho `#CC1F24` | Acento da marca: etapa atual e linhas finas de destaque | 5,5:1 |
| Grafite `#16181D` | Texto principal | 17,8:1 |
| Cinza `#5F6672` | Texto de apoio | 5,8:1 |

[[FONTE: Elaborado pelo autor, com contraste calculado pela fórmula da WCAG 2.2 (W3C, 2024).]]

**Tipografia e componentes.** Saira nos títulos e Inter no texto, as mesmas fontes do site atual, o que mantém a consistência com a marca (heurística 4). O botão principal, em formato de pílula, fica sempre na base da tela, ao alcance do polegar; o item selecionado ganha borda azul e sinal de confirmação; alertas de orientação são âmbar e erros, vermelhos. Todos os alvos de toque têm pelo menos 40 px, acima do mínimo de 24 px da WCAG 2.2 (W3C, 2024).

**Princípios visuais de Robin Williams** (PUCPR, [2026?]a): **contraste**, com um único botão de destaque por tela; **proximidade**, com rótulo, campo e erro juntos e cada item do resumo ao lado do seu "Editar"; **alinhamento**, em coluna única à esquerda; e **repetição**, com cabeçalho, indicador de etapas e botão na mesma posição em todos os passos.

## 6.3 Ajustes após feedback

O principal ajuste pedido nas conversas foi um lugar para as condições de compra de empresa, que virou o bloco "Compra pela empresa" no passo 4. Todos os ajustes estão na seção 8.3, com imagens de antes e depois.

# 7 Protótipo navegável

## 7.1 Descrição e link

O protótipo é uma **versão de teste do site da MEGA-WR**: uma cópia do código do site oficial, feito em Astro, com o orçamento guiado e as demais mudanças da proposta; o site oficial não foi alterado. É um protótipo de alta fidelidade, com interações realistas e quase idêntico ao produto final (PUCPR, [2026?]d).

- **Link do protótipo:** https://site-prototipo-megawr.vercel.app (orçamento guiado em https://site-prototipo-megawr.vercel.app/orcamento)
- **Versões:** acrescentar `?v=1` ao endereço abre a versão apresentada nas conversas; sem o parâmetro, abre a versão revisada após o feedback.

Nenhuma mensagem é enviada: a tela final mostra o texto que a MEGA-WR receberia. Uma faixa no topo identifica a página como protótipo acadêmico, e a versão de teste está bloqueada para buscadores.

## 7.2 Interações implementadas

Todos os controles das telas da seção 6 funcionam: o início pelo botão principal ou pelo card de uma linha, que já vem selecionada; os contadores por tamanho, com o medidor que muda de cor ao chegar a 10 peças; o aviso abaixo do mínimo, que leva ao pedido em grupo; "Ainda não tenho os tamanhos", com envio de planilha; o salvamento automático, com a opção "Começar de novo"; o bloco "Compra pela empresa"; a validação com erro indicado no campo; o "Editar" de cada item do resumo; e o envio por WhatsApp ou e-mail, que leva à confirmação.

## 7.3 Observações dos usuários na exploração

- **P1** aprovou o resumo: "É exatamente o que eu queria ter mandado pros três fornecedores: todo mundo recebendo a mesma coisa, aí dá pra comparar." Travou nos tamanhos ("Eu não sei os tamanhos agora") e sentiu falta das condições de empresa: "Condição de pagamento. Se faz boleto faturado. E se emite nota."
- **P2** foi direto a "Ainda não tenho os tamanhos": "Isso aqui me salvou." Hesitou na técnica ("qual é o melhor pra camiseta que vai suar todo dia?") e achou o fluxo comprido para fazer entre uma aula e outra: "Se salvasse onde eu parei, beleza."

# 8 Testes de usabilidade e melhorias

## 8.1 Método e resultados

O teste seguiu o modelo de **teste com usuários** da Unidade 06: observar o que a pessoa faz ao executar uma tarefa real (PUCPR, [2026?]e). Cada participante pediu um orçamento ligado ao seu perfil (15 camisas polo bordadas, para P1; 4 camisetas dry-fit com o logo da academia, para P2), primeiro no site atual e depois na proposta. Foram observados tempo, facilidade de aprendizado, erros e satisfação (confiança de 1 a 5). Com dois participantes, os resultados indicam tendências, mas não permitem generalizar; ampliar a amostra é a primeira prioridade da próxima iteração (seção 10).

[[QUADRO: Resultados do teste]]

| Participante | Site atual: tempo até tocar no botão | Proposta: tempo até o resumo | Concluiu a proposta | Confiança (1 a 5) |
|---|---|---|---|---|
| P1 | Cerca de 9 s | Cerca de 2 min 40 s | Sim | 4 |
| P2 | Cerca de 25 s | Cerca de 3 min 30 s, com pausas para ler | Sim | 3 |

[[FONTE: Elaborado pelo autor com base nos testes.]]

Os tempos **não medem a mesma coisa**, e essa diferença é o principal resultado. No site atual, a tarefa "termina" em segundos porque o site apenas transfere a pessoa para o WhatsApp, sem nenhuma informação do pedido: P1 achou o botão em 9 segundos, mas perguntou "Eles emitem nota? Qual o prazo pra 15? Tem pedido mínimo?", e P2, "Mas quanto custa, mais ou menos? E faz 4?". Na proposta, os dois levaram cerca de três minutos, mas terminaram com o pedido completo. P1 resumiu a troca: "Melhor: eu sei o que mandar. [...] Pior: é mais demorado." A confiança não chegou a 5 pelos motivos que a pesquisa já apontava: P1 não sabia quando teria resposta ("Se tivesse 'respondemos em até 1 dia útil', eu daria 5"), e P2 não sabia se o preço caberia no bolso ("Eu já passei por isso: preenche tudo e aí é caro").

## 8.2 Dificuldades, sugestões e pontos positivos

Os dois problemas críticos foram a falta de lugar para as condições de compra de empresa (P1) e a falta de uma referência de preço, que faz o pequeno comprador desconfiar de preencher tudo (P2).

[[QUADRO: Dificuldades, sugestões e pontos positivos registrados no teste]]

| | P1 (compra de empresa) | P2 (academia) |
|---|---|---|
| Dificuldades encontradas | Sem lugar para CNPJ, nota fiscal e forma de pagamento; os tamanhos chegam numa planilha, não peça a peça; trabalha no computador e precisa de um documento, não só de uma conversa | Sem referência de preço; fluxo longo para fazer no celular entre uma tarefa e outra; ainda depende de saber a diferença entre bordado, silk e DTF |
| Sugestões recebidas | Pagamento, boleto faturado e nota visíveis; resumo em PDF ou por e-mail, pelo computador; envio da planilha de tamanhos; informar "respondemos em até 1 dia útil"; pedir amostra ou ver o tecido na loja | Faixa de preço, "nem que seja 'a partir de R$ tanto'"; uma opção "pra academia", "já com o tecido certo"; pedido em grupo como pré-venda, com cada aluno pagando o seu |
| Pontos positivos | O resumo que deixa todos os fornecedores recebendo "a mesma coisa"; saber o que mandar, em vez de "ficar olhando pro WhatsApp em branco"; "Ainda não tenho os tamanhos": "É a minha vida, o tamanho vem por último" | Saber do mínimo antes de mandar mensagem: "não passei vergonha"; "Ainda não tenho os tamanhos": "Isso aqui me salvou"; o pedido em grupo; "Enviaria, porque é aqui de Leme" |

[[FONTE: Elaborado pelo autor com base nos testes.]]

## 8.3 Melhorias implementadas

[[QUADRO: Feedback recebido e decisão tomada]]

| Feedback | O que mudou | Situação |
|---|---|---|
| "Condição de pagamento. Se faz boleto faturado. E se emite nota" (P1) | Bloco opcional **"Compra pela empresa"**, com CNPJ, "preciso de nota fiscal" e forma de pagamento, que entram na mensagem | Implementado |
| "Poder baixar o resumo em PDF ou receber por e-mail" (P1) | **"Enviar por e-mail"** ao lado do WhatsApp, **"Baixar PDF"** e aviso de que, no computador, o WhatsApp abre no WhatsApp Web | Implementado |
| "Se eu pudesse subir minha planilha de tamanhos" (P1) | **Envio de planilha** em "Ainda não tenho os tamanhos" | Implementado |
| "Se salvasse onde eu parei, beleza" (P2) | **Salvamento automático** no aparelho, com o aviso "Continuamos de onde você parou" | Implementado |
| "Qual é o melhor pra camiseta que vai suar todo dia?" (P2) | **"Não sei, quero indicação" em primeiro**, com o selo "Recomendado se estiver em dúvida" | Implementado |
| Posição do logo desnecessária (P2) | Posição **opcional**, com "Combinar depois" | Implementado |
| "Pior: é mais demorado" (P1 e P2) | Atalho **"Fale direto no WhatsApp"** no passo 1 | Implementado |
| Amostra e loja em Leme (P1 e P2) | **"Quero ver tecido e modelo antes de fechar"** no passo 4, **"Loja em Leme para ver o tecido"** junto do botão principal e nova pergunta frequente | Implementado |
| Pré-venda com cada aluno pagando o seu (P2) | O pedido em grupo passa a citar equipes e alunos; o pagamento individual depende da empresa | Parcial; recomendação à MEGA-WR |
| Faixa de preço (P2) e prazo de resposta (P1) | Não implementados: dependem de dado e de compromisso que só a empresa pode assumir | Recomendação à MEGA-WR |

[[FONTE: Elaborado pelo autor.]]

[[GRADE: 08-passo4-entrega-v1.png@1938-2588 ; 08-passo4-entrega-v2.png@1938-3958 ; 09-resumo-v1.png@1598-2844 ; 09-resumo-v2.png@2028-3678 | Passo 4, antes ; Passo 4, depois: compra pela empresa, e-mail e ver o tecido ; Resumo, antes ; Resumo, depois: e-mail e PDF | Antes e depois das duas principais melhorias | Elaborado pelo autor. | 4 | 3.7cm]]

As demais mudanças aparecem nas telas da seção 6 e podem ser comparadas no protótipo navegável, abrindo o mesmo endereço com e sem `?v=1`.

# 9 Reflexão crítica e ética

A solução aplica UX com **empatia**, ao partir do que as pessoas viveram, e UI ao traduzir isso em hierarquia, contraste e um caminho claro por tela, sem tirar o atalho de quem prefere conversar. Mostrar mínimo, prazo e condições antes do contato é **transparência** (PUCPR, [2026?]f): evita que alguém perca tempo com uma conversa que não vai virar venda. O fluxo só pede CNPJ a quem compra pela empresa e deixa o e-mail opcional, seguindo o princípio da **necessidade** da LGPD (BRASIL, 2018), e o pedido salvo fica apenas no aparelho da pessoa. Não usa *dark patterns*, respeita contraste e tamanho de toque e, por funcionar no celular e no computador, é **inclusivo**.

# 10 Conclusão

O principal aprendizado foi que o problema não estava no canal. O WhatsApp é o canal certo para a MEGA-WR; o erro era chegar até ele sem nada nas mãos. A avaliação heurística apontou onde olhar, e a pesquisa confirmou os dois problemas centrais que ela previa: as condições invisíveis e o cliente que não sabe o que mandar. Mas as conversas mostraram o que a análise sozinha não mostrava: a compra de empresa tem regras próprias, como CNPJ, nota, boleto, três orçamentos e um documento para anexar, e o pequeno empresário não teme o mínimo, e sim o risco de estoque. As principais mudanças da versão revisada nasceram desses dois achados.

Numa próxima iteração, as prioridades são:

1. **Ampliar o teste**, com pelo menos um terceiro participante, e medir de novo o tempo no protótipo final, que já incorpora as melhorias.
2. **Conversar com William e Rosangela** sobre nota fiscal e boleto faturado, prazo de resposta, faixa de preço inicial, cobrança de matriz ou tela, amostra e pré-venda com pagamento individual.
3. **Explorar a oportunidade comercial** que P2 trouxe no fechamento: legging personalizada com o nome da academia, da linha Fitness, que "ninguém da academia sabe" que a MEGA-WR faz.
4. **Medir depois de publicar:** quantas conversas iniciadas pelo site viram orçamento, comparando o botão atual com o novo fluxo por meio de um teste A/B (PUCPR, [2026?]e).

# Referências

BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Acesso em: 16 set. 2026.

MEGA-WR CONFECÇÕES. **MEGA-WR Confecções**: uniformes profissionais, escolares e da saúde. Leme, 2026. Disponível em: https://megawr.com.br. Acesso em: 16 set. 2026.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 02: usabilidade e design visual na experiência do usuário. Curitiba: PUCPR, [2026?]a. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 03: pesquisa com usuários e criação de personas. Curitiba: PUCPR, [2026?]b. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 04: arquitetura da informação e navegação digital. Curitiba: PUCPR, [2026?]c. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 05: prototipagem de interfaces digitais. Curitiba: PUCPR, [2026?]d. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 06: testes de usabilidade e iteração contínua. Curitiba: PUCPR, [2026?]e. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Construção de interfaces e experiência do usuário**: unidade 07: tendências e ética no design de experiências. Curitiba: PUCPR, [2026?]f. Material didático.

W3C – WORLD WIDE WEB CONSORTIUM. **Web Content Accessibility Guidelines (WCAG) 2.2**. [*S. l.*]: W3C, 2024. Disponível em: https://www.w3.org/TR/WCAG22/. Acesso em: 16 set. 2026.

# Apêndice A – Roteiro da entrevista

**Bloco 1 – Aquecimento**

1. Me conta rapidinho o que você faz.
2. Quando precisa resolver alguma coisa, você usa mais o celular ou o computador?
3. Com que frequência você compra ou contrata algo feito sob medida?

**Bloco 2 – A experiência real**

4. Me conta da última vez que você pediu orçamento de algo sob medida. O que era?
5. Como você começou? Qual foi o primeiro lugar que você olhou?
6. Como foi o contato? Me conta o passo a passo.
7. Quanto tempo levou da primeira mensagem até ter um preço na mão?
8. Teve alguma hora em que você ficou sem saber o que responder ou perguntar?
9. Teve alguma informação que você só descobriu depois e queria ter sabido no começo?
10. Você pediu orçamento em mais de um lugar? Como escolheu?
11. Já desistiu de um orçamento no meio do caminho? O que fez você desistir?
12. Se pudesse mudar uma coisa nesse processo, o que seria?

**Bloco 3 – Site atual**

Tarefa no celular, em megawr.com.br, falando em voz alta e sem ajuda, cronometrada até o toque no botão de orçamento.

**Bloco 4 – A proposta, como sugestão**

13. O que você achou?
14. Ficou faltando alguma informação para você se sentir seguro de enviar?
15. De 1 a 5, quanto você confiou que ia conseguir o que precisava? Por quê?
16. Se fosse de verdade, você enviaria ou procuraria outro lugar?
17. O que você mudaria nessa proposta?
18. Tem alguma parte que você não usaria ou achou desnecessária?
19. Comparando com o site que você usou antes: o que ficou melhor e o que ficou pior?

**Bloco 5 – Fechamento**

20. Tem alguma coisa que eu não perguntei e que você acha importante?

# Apêndice B – Registro das entrevistas

Falas registradas entre aspas; observações do entrevistador em itálico. Conversas realizadas em 17 de setembro de 2026.

### P1 – analista de RH em indústria, 33 anos

*Perfil: organiza a SIPAT, a festa de fim de ano e as ações internas. Compras acima de certo valor passam pelo setor de Compras, que exige 3 orçamentos e fornecedor cadastrado com CNPJ. A indústria em que trabalha já é cliente da MEGA-WR.*

**1.** "Sou do RH. Faço um pouco de tudo: treinamento, integração, e os eventos internos acabam caindo comigo. SIPAT, Outubro Rosa, confraternização."

**2.** "No trabalho, computador. WhatsApp Web o dia inteiro. Na fábrica tem área em que nem pode entrar com celular. Então se é coisa da empresa, é no computador."

**3.** "Umas 4 ou 5 vezes por ano. Camiseta de SIPAT todo ano, colete da brigada, às vezes caneca ou squeeze de brinde."

**4.** "Camiseta da SIPAT, agora em agosto. Umas 180 peças, com a arte da campanha na frente e o logo atrás."

**5.** "Primeiro liguei pro fornecedor do ano passado. Mas Compras pede 3 orçamentos, então fui no Google e no Instagram procurar mais dois. E perguntei no grupo de RH da região quem o pessoal usava."

**6.** "Mandei mensagem no WhatsApp. Um me respondeu com áudio de dois minutos, com o preço no meio do áudio. Aí eu tive que pedir: 'consegue me mandar isso por escrito, em PDF, com CNPJ e validade?' Porque eu não consigo anexar áudio no pedido de compra." *(silêncio)* "O outro me mandou o preço certinho, mas sem o prazo. E o prazo pra mim é o que mais importa, porque a SIPAT tem data. Se chega um dia depois, não serve pra nada."

**7.** "O mais rápido, no mesmo dia. O mais demorado, uns cinco dias úteis. E nesse eu tive que cobrar duas vezes."

**8.** "Quando perguntaram se era silk ou DTF. Eu não sabia a diferença. E a arte tinha degradê, então parece que muda o preço. Eu falei 'o que for melhor', que é a pior resposta, né? Porque aí cada um me orçou uma coisa diferente e eu não conseguia comparar."

**9.** "Que um deles cobrava à parte o 'fotolito' ou 'tela', não lembro o nome. E que o pagamento era 50% adiantado. Aqui a empresa paga com boleto em 28 dias, no mínimo. Adiantado já trava tudo no financeiro."

**10.** "Três, obrigatório. No fim, quem decide é Compras, pelo menor preço, desde que cumpra o prazo. Mas eu influencio: se o fornecedor me dá trabalho, eu aviso."

**11.** "Desisti de um que não emitia nota com CNPJ, era MEI e não tinha como emitir no valor. Não dá pra cadastrar."

**12.** "Receber tudo num formato só. Preço, prazo, pagamento, o que está incluso. Num PDF que eu anexo e pronto."

**Site atual** (tarefa: 15 camisas polo bordadas com o logo da empresa). *Tempo até tocar no botão: cerca de 9 segundos.* "Tá, 'Solicitar orçamento' tá bem aqui em cima." *Rolou a página antes de tocar.* "Deixa eu ver se tem polo... tem, na linha Uniformes. 'Bordado', ok. Indústria, eles atendem indústria. Tem SESI de cliente, isso conta." *Ao tocar:* "Ah, abriu o WhatsApp do celular. Eu faria isso no computador, na verdade." *Entendeu rápido onde pedir, mas não o que mandar. Perguntou:* "Eles emitem nota? Qual o prazo pra 15? Tem pedido mínimo?" *Nenhuma dessas respostas está visível; o prazo aparece na seção "Como trabalhamos", à qual ela não chegou.*

**Proposta.** *Tempo até o resumo: cerca de 2 min 40 s, na versão preliminar. Hesitou nos tamanhos:* "Eu não sei os tamanhos agora. Eu mando uma planilha pros supervisores e demora uma semana pra voltar."

**13.** "Gostei do resumo no final. É exatamente o que eu queria ter mandado pros três fornecedores: todo mundo recebendo a mesma coisa, aí dá pra comparar."

**14.** "Condição de pagamento. Se faz boleto faturado. E se emite nota. Pra empresa isso vem antes do preço."

**15.** "4. Porque parece organizado, mas eu ainda não sei quando vou ter a resposta. Se tivesse 'respondemos em até 1 dia útil', eu daria 5."

**16.** "Enviaria. Mas também procuraria outros dois, não tem jeito, é regra."

**17.** "Poder baixar o resumo em PDF ou receber por e-mail. E poder fazer pelo computador sem cair no WhatsApp do celular."

**18.** "Pra mim não. Talvez escolher cor no detalhe, isso eu resolvo depois com a amostra."

**19.** "Melhor: eu sei o que mandar. No outro eu ia ficar olhando pro WhatsApp em branco. Pior: é mais demorado. Se eu estiver com pressa, só quero mandar um 'oi, preciso de polo'."

*Sobre "Ainda não tenho os tamanhos" e "Pedido em grupo":* "'Ainda não tenho os tamanhos' faz muito sentido. É a minha vida, o tamanho vem por último. 'Pedido em grupo' aqui não, porque quem compra é a empresa, ninguém paga individual. Mas se eu pudesse subir minha planilha de tamanhos, isso seria ótimo."

**20.** "Uma coisa: amostra. Pra 180 peças eu quero ver a peça antes. Se pudesse pedir amostra pelo site, ou passar na loja pra ver o tecido... vocês falaram que tem loja aqui em Leme? Isso é um ponto forte e ninguém fala."

### P2 – dono de academia de bairro, 47 anos

*Perfil: academia pequena em Leme, com cerca de 250 alunos e 4 professores. Ele mesmo decide e paga. Usa só o celular.*

**1.** "Tenho a academia há nove anos. Eu dou aula de manhã, cuido do caixa, da manutenção, de tudo. Academia pequena é assim."

**2.** "Celular. Computador só o da recepção, pra catraca."

**3.** "Pouco. Uma vez por ano, se muito. Camiseta dos professores, às vezes um banner."

**4.** "Começo do ano. Queria camiseta dry-fit preta com o logo pros professores. Eram 5. E pensei: já que vou fazer, faço umas pra vender pros alunos."

**5.** "Vi no Instagram de uma academia de Araras uma camiseta bonita e perguntei quem fez. Me passaram o contato."

**6.** "Mandei 'boa tarde, quanto fica camiseta com logo?'. O rapaz respondeu no outro dia perguntando quantas, que tecido, que tamanho, se o logo era em quantas cores... Eu não sabia metade. Tecido? Eu achei que dry-fit era o tecido." *(silêncio)* "Aí ele falou que o mínimo era 30. Eu tinha 5. Aí eu fiquei pensando se pegava 30 e vendia 25 pros alunos. Mas e se ninguém comprar? Fica encalhado lá no meu depósito."

**7.** "Uns quatro dias, porque eu também demorei pra responder. Eu respondo entre uma aula e outra."

**8.** "Tamanho pra aluno. Quanto P, quanto M, quanto G? Eu lá sei? Mulher usa baby look, homem não. Virou uma confusão."

**9.** "Que tinha uma taxa pra fazer o 'molde' do logo, uma vez só. Ninguém falou no começo. E o frete de Araras."

**10.** "Pedi em dois. Escolhi... na verdade não escolhi. Desisti."

**11.** "O mínimo, e o medo de encalhar. Mandei fazer 5 numa lojinha de estampa aqui do centro, na hora. Ficou meia boca, a estampa já tá rachando."

**12.** "Se tivesse como os alunos encomendarem direto, cada um escolhendo o tamanho e pagando o seu, eu fazia 50 camisetas amanhã. O problema não é pagar, é eu ficar no meio."

**Site atual** (tarefa: 4 camisetas dry-fit com o logo da academia, para você e seus professores). *Tempo até tocar no botão: cerca de 25 segundos.* "Olha, tem linha Fitness! Legging, camiseta dry-fit... isso é comigo." *Ao rolar:* "Silk, DTF... não sei o que é DTF." "Tá, Solicitar orçamento." *Tocou.* "Mas quanto custa, mais ou menos? E faz 4?"

**Proposta.** *Tempo até o resumo: cerca de 3 min 30 s, com pausas para ler, na versão preliminar. Na técnica:* "Silk, DTF, bordado... qual é o melhor pra camiseta que vai suar todo dia? Precisava de uma foto ou um 'recomendado pra academia'." *Nos tamanhos, foi direto em "Ainda não tenho os tamanhos":* "Isso aqui me salvou."

**13.** "Achei bom, mas é comprido. No celular, entre uma aula e outra, eu talvez parasse no meio. Se salvasse onde eu parei, beleza."

**14.** "Preço. Nem que seja 'a partir de R$ tanto'. Eu preciso saber se é R$ 40 ou R$ 90 pra saber se vale vender pros alunos."

**15.** "3. Eu entendi o que tava fazendo, mas não sei se no fim vai dar um preço que eu consigo pagar. Eu já passei por isso: preenche tudo e aí é caro."

**16.** "Enviaria, porque é aqui de Leme. Se é daqui, eu posso passar lá e olhar. Isso pesa."

**17.** "Faixa de preço. E uma parte 'pra academia': já com o tecido certo, sem eu ter que escolher."

**18.** "A parte de detalhe da posição do logo. Eu ia deixar pra conversar com a pessoa."

**19.** "Melhor: eu fiquei sabendo do mínimo antes de mandar mensagem, e não passei vergonha. Pior: no outro é um toque e pronto."

*Sobre "Pedido em grupo" (demonstrou interesse imediato):* "Como funciona? Eu mando um link e cada aluno escolhe o tamanho? E paga? Se for isso, é exatamente o que eu falei. Se os alunos pagam cada um, eu não corro risco nenhum." *Entendeu o pedido em grupo como pré-venda com pagamento individual, o que vai além da proposta atual.*

**20.** "Só uma coisa: eu tenho aluna que vive pedindo legging com o nome da academia. Vocês fazem legging. Ninguém da academia sabe disso. Se tivesse um jeito de eu vender isso, o pedido sai bem maior que 10."
