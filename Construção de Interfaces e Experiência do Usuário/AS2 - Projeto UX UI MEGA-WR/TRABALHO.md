---
titulo: Repensando a solicitação de orçamento da MEGA-WR
subtitulo: projeto de UX/UI do fluxo de orçamento de uma confecção de uniformes
aluno: Yan Suyama
curso: Bacharelado em Marketing
disciplina: Construção de Interfaces e Experiência do Usuário
instituicao: Pontifícia Universidade Católica do Paraná
ano: 2026
---

<!--
FONTE DO PDF. Este arquivo gera `Entrega/YanSuyama_ProjetoUXUI.pdf`.
Para regerar depois de editar: `python Entrega/gerar_pdf.py`

Marcadores usados pelo gerador:
  [[AVISO-SIMULACAO]]           caixa vermelha de aviso
  [[TAG-SIMULACAO]]             aviso vermelho curto
  [[QUADRO: título]]            título numerado acima da tabela seguinte
  [[FONTE: texto]]              fonte abaixo de quadro ou figura
  [[FIG: arquivo | título | fonte | largura]]
  [[PAR: arq1 ; arq2 | legenda1 ; legenda2 | título | fonte]]
  [[QUEBRA]]                    quebra de página

Versão preliminar: as seções 2, 3, 4, 7.3 e 8 usam entrevistas SIMULADAS
e devem ser refeitas com as conversas reais antes da entrega definitiva.
-->

# 1 Entendendo o problema e o usuário

## 1.1 Contexto

A MEGA-WR Confecções é uma confecção familiar de Leme/SP, dos proprietários William e Rosangela, que atua há cerca de dez anos no segmento. Produz três linhas: Saúde (jalecos e scrubs), Uniformes (profissional, escolar, esportivo e industrial) e Fitness (leggings, bermudas e camisetas dry-fit). O foco é o cliente empresarial, como escolas, empresas, clínicas e academias, com atendimento secundário a quem compra para uso próprio.

Três condições comerciais moldam todo o projeto, segundo informações fornecidas pelos proprietários: **pedido mínimo de 10 peças por modelo**, **prazo de 20 a 30 dias** após a confirmação e **ausência de tabela de preço**, já que cada orçamento é montado conforme modelo, tecido, quantidade e personalização. A empresa atende presencialmente na loja e pelo WhatsApp, e mantém um site institucional em megawr.com.br (MEGA-WR CONFECÇÕES, 2026).

## 1.2 O problema observado

O site apresenta bem a empresa, mas falha no momento em que o visitante decide pedir um orçamento. O levantamento abaixo foi feito na página publicada, em 16 de setembro de 2026.

[[QUADRO: Diagnóstico do site atual no momento da conversão]]

| Ponto verificado | Situação encontrada |
|---|---|
| Estrutura | Página única (*one-page*), com as seções Linhas, Personalização, Clientes, Como trabalhamos e Sobre |
| Links de contato | **8 links**, todos para o mesmo número de WhatsApp |
| Rótulos desses links | "Solicitar orçamento" (4, incluindo o ícone do topo no celular), o número de telefone (2), "Fale com a gente" e "Falar no WhatsApp" |
| Mensagem que o usuário envia | Idêntica nos 8 links: *"Olá! Vim pelo site e gostaria de solicitar um orçamento de uniformes."* |
| Formulário ou fluxo de orçamento | Não existe |
| Pedido mínimo de 10 peças | **Não aparece em nenhum texto visível da página**. Consta apenas na descrição lida pelos buscadores |
| Prazo de produção | Informado (20 a 30 dias), na seção "Como trabalhamos" |

[[FONTE: Elaborado pelo autor com base em MEGA-WR Confecções (2026).]]

A primeira etapa do processo anunciado pelo próprio site é **"Você conta o que precisa"**, mas a interface não oferece nenhum lugar para contar. Qualquer botão tira o visitante do site e o coloca numa conversa de WhatsApp com uma frase genérica, que ele não escreveu, e ele precisa descrever do zero, de memória, tudo o que acabou de ver.

[[FIG: site-atual-hero.png | Primeira tela do site atual no celular: o botão "Solicitar orçamento" leva direto ao WhatsApp | Captura de tela do autor em MEGA-WR Confecções (2026). | 6.2cm]]

O atrito aparece nas duas pontas. **O cliente** não sabe se a quantidade dele é aceita, quanto custa nem que informações precisa passar. **A empresa** recebe sempre a mesma mensagem, sem nenhum dado do pedido, e precisa conduzir uma sequência de perguntas de ida e volta antes de conseguir orçar.

**Recorte do projeto:** redesenhar a solicitação de orçamento do site da MEGA-WR. O WhatsApp continua sendo o canal final de negociação, porque é o canal real da empresa, mas o cliente passa a chegar nele com o pedido já organizado.

## 1.3 Avaliação heurística do estado atual

Antes de ouvir os usuários, o site foi avaliado segundo as 10 heurísticas de usabilidade de Jakob Nielsen apresentadas no material da disciplina (PUCPR, [2026?]a). A Unidade 06 recomenda justamente essa ordem: a avaliação heurística antes do teste com usuários corrige problemas básicos com mais rapidez e evita gastar a conversa com erros já conhecidos (PUCPR, [2026?]e).

[[QUADRO: Avaliação heurística do fluxo de orçamento no site atual]]

| # | Heurística | Situação no site atual | Gravidade |
|---|---|---|---|
| 1 | Visibilidade do *status* do sistema | Não existe fluxo, logo não há progresso visível. O clique troca o usuário de aplicativo sem aviso | Alta |
| 2 | Correspondência com o mundo real | Boa nas linhas de produto. Falha em "DTF", termo técnico que exige leitura da descrição para ser entendido | Média |
| 3 | Controle e liberdade do usuário | Depois de ir ao WhatsApp não há como revisar ou corrigir o pedido dentro do site | Alta |
| 4 | Consistência e padrões | Oito links com rótulos diferentes geram a mesma mensagem, qualquer que seja a seção de origem. Quem clica em Saúde envia o mesmo texto de quem clica em Fitness | Média |
| 5 | **Prevenção de erros** | **O pedido mínimo não aparece na página.** O usuário só descobre a restrição depois de iniciar a conversa | **Alta** |
| 6 | Reconhecimento em vez de memorização | O usuário precisa lembrar e redigir o que viu. Nenhuma informação é levada para a etapa seguinte | Alta |
| 7 | Flexibilidade e eficiência de uso | Caminho único: cliente recorrente e visitante de primeira vez percorrem exatamente o mesmo trajeto | Média |
| 8 | Estética e *design* minimalista | Página limpa, com boa hierarquia e fotos reais. Ponto forte do site | Baixa |
| 9 | Ajuda para reconhecer e corrigir erros | Sem formulário, não há validação nem mensagem de erro | Média |
| 10 | Ajuda e documentação | Não há perguntas frequentes. Dúvidas previsíveis (mínimo, entrega, preço, tipos de personalização) não têm resposta organizada | Alta |

[[FONTE: Elaborado pelo autor com base em PUCPR ([2026?]a).]]

[[QUEBRA]]

# 2 Pesquisa com usuários

[[AVISO-SIMULACAO]]

## 2.1 Método

A pesquisa usou **entrevista semiestruturada**, com perguntas abertas, em duas partes que correspondem aos dois tipos de entrevista descritos na Unidade 03 (PUCPR, [2026?]b):

- **Parte exploratória:** conversa sobre a última vez que a pessoa pediu orçamento de algo feito sob medida. A pergunta é sempre sobre o que já aconteceu, nunca sobre o que a pessoa faria, para evitar respostas induzidas.
- **Parte de validação:** a pessoa usa o protótipo da solução com uma tarefa concreta e comenta em voz alta o que entende, o que estranha e o que mudaria.

**Participantes:** duas pessoas com perfis opostos, uma que compra para um grupo (B2B) e outra que compra para si (B2C). **Critério de recrutamento:** ter pedido orçamento de algum produto sob medida nos últimos 12 meses. Os participantes são identificados como P1 e P2, para preservar a identidade. O roteiro completo está no Apêndice A e o registro das conversas, no Apêndice B.

## 2.2 Perfil dos participantes

[[QUADRO: Perfil dos participantes]]

| | P1 | P2 |
|---|---|---|
| Idade | 42 anos | 26 anos |
| Ocupação | Coordenadora administrativa de clínica odontológica (Leme/SP) | Técnico de enfermagem em hospital (Pirassununga/SP), plantão 12x36 |
| Perfil de compra | B2B: compra para a equipe e leva a decisão ao sócio | B2C: compra para uso próprio |
| Frequência de compra sob medida | Duas a três vezes por ano | Primeira vez com personalização |
| Uso do celular | Pesquisa no celular; consolida no computador | Só celular ("nem tenho computador em casa") |
| Caso relatado | Uniforme bordado para 14 pessoas, em andamento | Dois scrubs com nome e COREN bordados, há quatro meses |

[[FONTE: Elaborado pelo autor com base nas entrevistas simuladas.]]

## 2.3 Principais respostas

[[QUADRO: Principais respostas por tema]]

| Tema | P1 (B2B) | P2 (B2C) |
|---|---|---|
| Como começou | Indicação no grupo de WhatsApp de clínicas e busca no Google. Abriu três ou quatro sites para "ter uma noção de preço antes de falar com alguém" | Post patrocinado no Instagram, perfil, site pelo link da bio. "Era de noite, depois do plantão, deitado já" |
| O contato | O botão levou a uma mensagem pronta. A resposta veio duas horas depois, com perguntas sobre modelo, tecido, bordado ou silk e tamanhos: "Eu não sabia metade" | Escreveu o pedido completo abaixo da mensagem pronta. No dia seguinte, soube que o mínimo era 10 peças |
| Tempo até ter preço | Cerca de cinco dias, "muito por minha causa", porque precisou coletar os tamanhos da equipe | "Nunca tive" |
| O que descobriu tarde | Prazo de 30 dias úteis em um fornecedor e uma taxa separada pela arte do bordado | O pedido mínimo: "Se estivesse escrito no site, eu nem tinha perdido tempo" |
| Comparação | Três orçamentos em formatos diferentes (PDF, áudio e texto), que precisou passar para uma tabela, "e mesmo assim não batia" | Comprou numa loja on-line que mostra o preço do bordado na hora |
| Desistência | "Já deixei conversa morrer. Depois de uma semana fica chato voltar" | Tentou juntar colegas do plantão, mas "fica difícil organizar tamanho, pagamento" |
| O que mudaria | "Saber antes o que vão me perguntar" e receber o orçamento "num formato que eu pudesse repassar direto" | "Colocar o mínimo logo de cara. Nem que seja pequenininho embaixo do botão" |

[[FONTE: Elaborado pelo autor com base nas entrevistas simuladas.]]

## 2.4 Padrões e problemas recorrentes

Seguindo o caminho proposto pela Unidade 03, em que os dados revelam padrões e os padrões geram *insights* (PUCPR, [2026?]b), as respostas foram agrupadas em cinco padrões:

1. **A conversa começa no escuro.** P1 não sabia o que precisaria informar; P2 não sabia se seria atendido. Nos dois casos, o WhatsApp foi aberto sem a informação que decide o resto do processo.
2. **Informação crítica chega tarde.** Pedido mínimo, prazo e taxa de arte só apareceram depois do primeiro contato e custaram dias, dos dois lados.
3. **Pedir para um grupo não cabe numa sessão só.** Os dois dependeram de outras pessoas, seja para coletar tamanhos (P1), seja para somar peças (P2), e a tarefa foi interrompida.
4. **O abandono é silencioso.** Ninguém recusa o orçamento: a pessoa "deixa a conversa morrer" ou "deixa pra lá", e o fornecedor não fica sabendo por quê.
5. **O celular é o canal de pesquisa**, mas quem decide em grupo precisa de um resumo que possa repassar.

Com duas pessoas, esses padrões são **indícios a confirmar**, não conclusões generalizáveis.

## 2.5 Pesquisa complementar com o negócio

Uma conversa com William e Rosangela completa o diagnóstico com dados do atendimento: quantas mensagens são trocadas até fechar um orçamento, quais perguntas se repetem, com que frequência chegam pedidos abaixo de 10 peças e se é viável informar uma faixa de preço inicial. Essa conversa não conta como participante da pesquisa e fica registrada como próxima etapa (seção 10).

[[QUEBRA]]

# 3 Personas

[[TAG-SIMULACAO]]

As personas são personagens semifictícios que representam grupos de usuários com objetivos, comportamentos e dores semelhantes (PUCPR, [2026?]b). As duas abaixo sintetizam os perfis de P1 e P2, e cada uma vem com um cenário de uso, que descreve como a pessoa interage com o serviço numa situação real.

## 3.1 Patrícia, a compradora da equipe (B2B)

> "Se eu soubesse que precisava de tamanho, cor e onde vai o logo, eu já juntava tudo antes de chamar."

**Perfil:** 42 anos, coordenadora administrativa de uma clínica odontológica em Leme/SP. Cuida de compras, fornecedores e pagamentos. Não decide sozinha: leva as opções ao sócio.

**Cenário de uso:** a clínica quer padronizar o uniforme de 14 pessoas, com logo bordado. Entre um paciente e outro, na recepção, Patrícia pesquisa fornecedores pelo celular. À noite, passa as opções para uma planilha no computador para apresentar ao sócio.

**Objetivos:**

- Conseguir orçamentos comparáveis, no mesmo formato, para levar a quem decide.
- Pedir do jeito certo na primeira vez, sem parecer despreparada diante do vendedor.

**Necessidades:** saber de antemão o que será perguntado; poder pausar enquanto coleta os tamanhos da equipe; conhecer prazo e custos extras antes de fechar.

**Frustrações:** perguntas técnicas que não sabe responder ("Qual gramatura?"); a sensação de "estar atrasando a pessoa"; custos que só aparecem no final; orçamentos que não batem entre si.

**Hábitos digitais:** confortável com celular e WhatsApp. Pesquisa no Google e em grupos de indicação. Abandona cadastro que peça CNPJ logo no começo.

## 3.2 Rafael, o profissional que compra para si (B2C)

> "Colocar o mínimo logo de cara. Nem que seja pequenininho embaixo do botão."

**Perfil:** 26 anos, técnico de enfermagem em hospital de Pirassununga/SP, em plantão 12x36. Compra com o próprio dinheiro. Só usa celular.

**Cenário de uso:** depois do plantão, deitado, vê no Instagram um post patrocinado de scrub bordado. Entra no perfil, depois no site, escolhe cor e modelo e pede orçamento de dois scrubs com nome e COREN. Só no dia seguinte descobre que o pedido mínimo é de 10 peças.

**Objetivos:**

- Ter uma peça personalizada que passe uma imagem profissional no trabalho.
- Resolver tudo pelo celular, sem ir até a loja.

**Necessidades:** saber logo no início se o pedido dele é atendido; ver preço sem precisar conversar; ter uma saída se a quantidade não for suficiente.

**Frustrações:** perder tempo com um fornecedor que "parecia que era pra qualquer um"; não conseguir organizar uma compra coletiva com colegas.

**Hábitos digitais:** nativo de celular e de Instagram. Compara em segundos e troca de loja sem culpa, mas guarda o perfil de quem o tratou bem para uma compra futura.

## 3.3 Por que duas personas opostas

Patrícia é a cliente ideal do negócio; Rafael é quem o negócio precisa recusar, ao menos na forma em que ele chega hoje. Projetar para os dois obriga a interface a resolver o caminho feliz e também o momento de dizer "não", que é exatamente onde o site atual falha. A pesquisa mostrou ainda um ponto em comum: os dois dependem de outras pessoas para completar o pedido.

[[QUEBRA]]

# 4 Insights e definição do problema

[[TAG-SIMULACAO]]

## 4.1 Principais aprendizados

1. **O botão de orçamento resolve a vontade de falar, não a de pedir.** O cliente chega ao WhatsApp sem saber o que informar, e o orçamento vira um interrogatório.
2. **Dizer "não" cedo é um serviço.** Para quem está fora do pedido mínimo, a melhor experiência é saber disso em segundos, e não no dia seguinte.
3. **O pedido coletivo é uma tarefa em etapas.** Tanto a compradora B2B quanto o comprador B2C precisaram parar para falar com outras pessoas.
4. **Quem compra para uma empresa precisa comparar e repassar.** O formato da resposta pesa tanto quanto o preço.

## 4.2 Problemas identificados

O quadro cruza os achados da pesquisa com o diagnóstico heurístico da seção 1.3. A prioridade segue o critério da Unidade 06: primeiro o que impede a tarefa, depois o que gera frustração (PUCPR, [2026?]e).

[[QUADRO: Problemas priorizados]]

| Problema | Evidência na pesquisa | Heurística | Prioridade |
|---|---|---|---|
| Pedido mínimo invisível | P2 descobriu o mínimo no dia seguinte | 5 | Crítica |
| Cliente não sabe o que informar | P1: "Eu não sabia metade" | 6 | Crítica |
| Sem saída para quem fica abaixo do mínimo | P2 desistiu e comprou em outra loja | 9 | Alta |
| Tarefa longa sem como pausar | P1 levou dois dias para voltar com os tamanhos | 3 e 7 | Alta |
| Troca de aplicativo sem aviso, com mensagem genérica | P1 enviou a frase pronta e recebeu uma lista de perguntas | 1 | Alta |
| Termos técnicos sem tradução | P1: "Qual gramatura? Não sei" | 2 | Média |
| Orçamento em formato que não se compara nem se repassa | P1 precisou montar uma tabela para o sócio | 10 | Média |
| Custos e prazos descobertos no final | P1: taxa de arte e prazo em dias úteis | 10 | Média, depende de dado da empresa |

[[FONTE: Elaborado pelo autor.]]

## 4.3 Oportunidades de melhoria

1. Substituir a ida direta ao WhatsApp por um **orçamento guiado em quatro passos** dentro do site.
2. Mostrar **pedido mínimo e prazo junto do botão principal** e validar a quantidade em tempo real.
3. Oferecer uma **saída para quem não chega a 10 peças**: montar pedido em grupo por link.
4. Permitir **informar só o total** e **salvar para continuar depois**.
5. Explicar bordado, silk e DTF pela descrição de uso, com foto, sem exigir o termo técnico.
6. Gerar ao final uma **mensagem estruturada e um resumo para baixar**, que o cliente revisa antes de enviar.
7. Criar **perguntas frequentes** com as dúvidas que hoje consomem o atendimento.

## 4.4 Declaração do problema

> **Patrícia**, que compra uniformes para a equipe de uma clínica, precisa enviar um pedido de orçamento completo e comparável na primeira tentativa, porque cada ida e volta atrasa a decisão do sócio. **Mas hoje** o site a leva para uma conversa em branco, sem dizer o que ela precisa informar.

> **Rafael**, profissional de saúde que compra para si, precisa saber logo no início se o pedido dele pode ser atendido, porque não quer perder tempo com um fornecedor que não serve. **Mas hoje** o pedido mínimo só aparece depois que ele já abriu a conversa.

**Pergunta que orienta a solução:** como fazer o cliente chegar ao WhatsApp da MEGA-WR com o pedido já organizado, sabendo desde o início se ele é atendido?

[[QUEBRA]]

# 5 Estruturação da solução

## 5.1 Organização do conteúdo

A Unidade 04 apresenta modelos de organização do conteúdo, entre eles por categorias temáticas e por tarefas (PUCPR, [2026?]c). O site atual usa só o primeiro, com as linhas de produto. A proposta mantém as categorias, que funcionam bem para quem está conhecendo a empresa, e acrescenta uma **entrada por tarefa**: "Montar meu orçamento".

[[QUADRO: Onde cada informação passa a aparecer]]

| Informação | Onde aparece na proposta | Por quê |
|---|---|---|
| Pedido mínimo e prazo | Logo abaixo do botão principal, no passo 2 e nas perguntas frequentes | É a informação que decide se vale a pena continuar |
| Linhas de produto | Cards da página inicial, cada um com atalho "Orçar linha" | Quem já escolheu a linha começa o orçamento com ela pré-selecionada |
| Bordado, silk e DTF | Passo 3, no momento da escolha, e nas perguntas frequentes | A explicação aparece quando a decisão é tomada |
| Tecido | Não é perguntado. A MEGA-WR indica no orçamento | P1 não sabia responder; é decisão técnica do fornecedor |
| Preço | Resumo explica como o valor é calculado | A empresa não tem tabela; o site não promete o que não pode cumprir |
| WhatsApp direto | Ícone no topo da página | Cliente recorrente continua podendo falar direto (heurística 7) |

[[FONTE: Elaborado pelo autor.]]

A **rotulação** também muda. "Solicitar orçamento" sugeria um contato imediato; "Montar meu orçamento" antecipa que a pessoa vai preencher algo no próprio site antes da conversa.

## 5.2 Mapa de navegação (sitemap)

[[FIG: sitemap.svg | Mapa do site proposto | Elaborado pelo autor. | 16cm]]

A página inicial continua sendo uma página única, com seções acessadas por âncora. A novidade é o ramo **/orcamento**, com quatro passos e resumo, e a página de **pedido em grupo**, aberta a partir do passo 2. O WhatsApp aparece como destino externo: é o fim do fluxo, e não mais o começo.

## 5.3 Fluxo de uso

[[FIG: fluxo.svg | Fluxo de solicitação de orçamento, com pontos de decisão e tratamento de erro | Elaborado pelo autor. | 15.2cm]]

## 5.4 Justificativa da estrutura

- **Um passo, um assunto.** Dividir o pedido em produto, quantidade, personalização e entrega reduz a carga de memória, que é a oitava regra de ouro de Shneiderman (PUCPR, [2026?]a), e deixa claro o que falta em cada momento.
- **Profundidade curta.** Todo conteúdo institucional continua a um toque da página inicial, e o atalho "Orçar linha" elimina um passo para quem já escolheu, seguindo a recomendação de evitar níveis de profundidade excessivos (PUCPR, [2026?]c).
- **O erro é evitado antes de acontecer.** A regra do pedido mínimo é verificada no passo 2, enquanto a pessoa escolhe as quantidades, e não depois do envio.
- **Diálogo com fechamento.** Resumo, mensagem visível e tela de próximos passos dão início, meio e fim à tarefa, a quarta regra de ouro de Shneiderman (PUCPR, [2026?]a).

[[QUEBRA]]

# 6 Wireframes

## 6.1 Telas

As telas foram desenhadas em **alta fidelidade**, próximas da aparência final, com tipografia, cores, ícones e espaçamentos definidos (PUCPR, [2026?]c). Foram projetadas primeiro para o celular, que é o aparelho de pesquisa dos dois participantes. O projeto tem 11 telas e estados.

[[QUADRO: Telas do projeto e heurísticas que cada uma endereça]]

| Tela | Função | Heurística principal |
|---|---|---|
| Página inicial | Botão principal com mínimo, prazo e "sem cadastro"; atalho por linha | 5, prevenção de erros |
| Perguntas frequentes | Respostas às dúvidas que hoje chegam pelo WhatsApp | 10, ajuda e documentação |
| Passo 1: produto | Escolha visual da linha e do modelo | 6, reconhecimento |
| Passo 2: quantidade | Medidor de pedido mínimo em tempo real | 5, prevenção de erros |
| Passo 2: abaixo do mínimo | Explica a regra e oferece saídas | 9, recuperação de erros |
| Passo 2: sem os tamanhos | Informa só o total e salva o pedido | 3, controle e liberdade |
| Passo 3: personalização | Técnica pela descrição, posição no desenho da peça e envio do logo | 2, linguagem do usuário |
| Passo 4: entrega e contato | Dados mínimos, sem CNPJ, com erro indicado no campo | 9, mensagens de erro claras |
| Resumo | Revisão com "Editar" em cada item e prévia da mensagem | 3, controle e liberdade |
| Confirmação | Mensagem enviada, código do pedido e próximos passos | 1, visibilidade do *status* |
| Pedido em grupo | Link para colegas e contador até 10 peças | 7, flexibilidade |

[[FONTE: Elaborado pelo autor.]]

[[PAR: 01-home-v2-topo.png ; 02-faq.png | Página inicial ; Perguntas frequentes | Página inicial e perguntas frequentes | Elaborado pelo autor.]]

[[PAR: 03-passo1-produto.png ; 04-passo2-ok.png | Passo 1: produto ; Passo 2: quantidade | Passos 1 e 2 do orçamento | Elaborado pelo autor.]]

[[PAR: 07-passo3-personalizacao.png ; 08-passo4-entrega.png | Passo 3: personalização ; Passo 4: entrega e contato | Passos 3 e 4 do orçamento | Elaborado pelo autor.]]

[[PAR: 09-resumo-v2.png ; 10-confirmacao.png | Resumo ; Confirmação | Resumo e confirmação | Elaborado pelo autor.]]

[[PAR: 08-passo4-erro.png ; 06-passo2-sem-tamanhos.png | Erro indicado no campo ; Pedido salvo sem os tamanhos | Tratamento de erro e pausa do pedido | Elaborado pelo autor.]]

## 6.2 Padrões de interface

**Cores.** A paleta usa as cores institucionais da MEGA-WR. Todas as combinações de texto passam no contraste mínimo de 4,5:1 exigido pelo nível AA da WCAG 2.2 (W3C, 2024).

[[QUADRO: Paleta e contraste]]

| Cor | Uso | Contraste sobre branco |
|---|---|---|
| Azul `#1F3F9C` | Botão principal (um por tela) e links | 9,3:1 |
| Vermelho `#CC1F24` | Destaques da marca, etapa atual e item selecionado | 5,5:1 |
| Grafite `#16181D` | Texto principal | 17,8:1 |
| Cinza `#5F6672` | Texto de apoio | 5,8:1 |
| Verde `#166534` | Confirmação e mínimo atingido | Acima de 7:1 |

[[FONTE: Elaborado pelo autor, com contraste calculado pela fórmula da WCAG 2.2 (W3C, 2024).]]

**Tipografia.** Saira nos títulos e Inter no texto, as mesmas fontes do site atual, o que mantém a consistência com a marca (heurística 4).

**Componentes.** Botão principal azul, sempre na base da tela e ao alcance do polegar; item selecionado com borda vermelha e sinal de confirmação; indicador de etapas no topo; alerta âmbar para orientação e vermelho para erro. Todos os alvos de toque têm pelo menos 40 px, acima do mínimo de 24 px da WCAG 2.2 (W3C, 2024).

**Princípios visuais de Robin Williams**, conforme a Unidade 02 (PUCPR, [2026?]a):

- **Contraste:** um único botão de destaque por tela, para que a próxima ação seja óbvia.
- **Proximidade:** rótulo, campo e mensagem de erro ficam juntos; cada item do resumo fica ao lado do seu "Editar".
- **Alinhamento:** coluna única alinhada à esquerda, que se lê de cima para baixo no celular.
- **Repetição:** cabeçalho, indicador de etapas e botão na mesma posição em todos os passos.

## 6.3 Ajustes após feedback

Os ajustes feitos nas telas depois da exploração do protótipo pelos participantes estão documentados, com imagens de antes e depois, na seção 8.6.

[[QUEBRA]]

# 7 Protótipo navegável

## 7.1 Descrição e link

O protótipo foi construído em HTML, CSS e JavaScript e funciona no navegador do celular ou do computador. Segundo a Unidade 05, o protótipo de alta fidelidade tem interações realistas e é quase idêntico ao produto final (PUCPR, [2026?]d). Construí-lo em código permitiu que os controles funcionassem de verdade, com soma de quantidades, validação e montagem da mensagem, em vez de apenas simular a troca de telas.

- **Link do protótipo:** `[INSERIR LINK]`
- **Arquivo:** `Prototipo/index.html`
- **Versões:** `?v=1` abre a versão inicial e `?v=2` (padrão) abre a versão revisada após o feedback.

Nenhuma mensagem é enviada e nenhum dado sai do aparelho. Uma faixa no topo identifica a página como protótipo acadêmico.

## 7.2 Interações implementadas

- Início do orçamento pelo botão principal ou pelo card de uma linha, que já vem pré-selecionada.
- Escolha de linha e modelo, com tamanhos e tecido de cada peça conforme o catálogo da empresa.
- Contadores de quantidade por tamanho e medidor do pedido mínimo, que muda de cor ao chegar a 10 peças.
- Aviso abaixo do mínimo, com acesso à página de pedido em grupo.
- Opção "Ainda não tenho os tamanhos", com total aproximado e botão Salvar.
- Seleção de técnica e de uma ou mais posições, com marcação no desenho da peça.
- Validação dos campos obrigatórios, com mensagem no próprio campo.
- Resumo com "Editar" em cada item e prévia da mensagem montada a partir das escolhas.
- Tela de confirmação com código do pedido e próximos passos.

## 7.3 Observações dos usuários na exploração

[[TAG-SIMULACAO]]

- **P1** gostou do passo de personalização: "Eu não preciso saber o nome técnico, só escolher". Valorizou ver a mensagem antes de mandar e o fato de não pedir CNPJ. Perguntou: "Dá pra salvar e voltar depois?"
- **P2** achou "bem mais organizado" e aprovou saber do mínimo na hora, "sem precisar mandar mensagem". Mas travou no aviso: "E agora? Parou ali pra mim".

[[QUEBRA]]

# 8 Testes de usabilidade e melhorias

[[TAG-SIMULACAO]]

## 8.1 Método do teste

O teste seguiu o modelo de **teste com usuários** da Unidade 06: observar o que a pessoa faz ao executar uma tarefa real, mais do que perguntar o que ela acha (PUCPR, [2026?]e).

- **Tarefas:** "Você precisa de 15 camisas polo bordadas com o logo da sua empresa. Peça um orçamento" (perfil B2B) e "Você quer 2 scrubs com o seu nome bordado. Peça um orçamento" (perfil B2C).
- **Aspectos avaliados**, conforme a Unidade 06: eficiência (tempo), facilidade de aprendizado, erro e recuperação, e satisfação.
- **Registro:** conclusão sem ajuda, dúvidas ditas em voz alta, confiança de 1 a 5 e comentários espontâneos.
- **Participantes previstos:** três. Nesta versão, P1 e P2.

## 8.2 Resultados

[[QUADRO: Resultados do teste]]

| Participante | Tarefa | Concluiu sem ajuda | Confiança (1 a 5) | Tempo |
|---|---|---|---|---|
| P1 | 15 camisas polo | Sim, chegou ao resumo | 4 | Não medido |
| P2 | 2 scrubs | Não. Interrompido no passo 2 pela regra do mínimo | 2 para compra própria; 4 se fosse para a equipe | Não medido |
| P3 | A realizar | — | — | — |

[[FONTE: Elaborado pelo autor com base na simulação.]]

A interrupção de P2 não é falha de usabilidade: a interface cumpriu seu papel ao informar a regra no momento certo. A falha estava em não oferecer um próximo passo, e é isso que a melhoria 1 corrige.

## 8.3 Dificuldades encontradas

- **Problema crítico:** abaixo do mínimo, a tela não oferecia nenhuma alternativa (P2).
- **Problema crítico:** quem compra para um grupo não tinha como pausar para coletar tamanhos (P1).
- **Melhoria desejável:** faltaram, na entrada, uma faixa de preço e o prazo médio (P1).
- **Melhoria desejável:** o orçamento precisava de um formato fácil de repassar a quem decide (P1).

## 8.4 Sugestões recebidas

- "Dá pra salvar e voltar depois?" (P1)
- Mostrar uma faixa de preço, "mesmo que aproximada, tipo 'a partir de'" (P1).
- Mostrar o mínimo de 10 peças já no começo (P1 e P2).
- Oferecer algo como "junte com colegas" ou um valor diferente para poucas peças (P2).

## 8.5 Pontos positivos observados

- Escolher a personalização por opções, sem conhecer o termo técnico.
- Ver a mensagem antes de enviar: "a pessoa do outro lado já entendeu o que eu quero, então não vou passar vergonha" (P1).
- Não pedir CNPJ nem cadastro.
- Saber do pedido mínimo na hora, dentro do site.

## 8.6 Melhorias implementadas: antes e depois

[[QUADRO: Feedback recebido e decisão tomada]]

| Feedback | O que mudou | Situação |
|---|---|---|
| "E agora? Parou ali pra mim" (P2) | O aviso abaixo do mínimo passou a oferecer **pedido em grupo**, **aumentar a quantidade** ou seguir a marca para depois | Implementado |
| "Dá pra salvar e voltar depois?" (P1) | Opção **"Ainda não tenho os tamanhos"**, com total aproximado, e botão **Salvar** em todos os passos | Implementado |
| Mínimo visível no começo (P1 e P2) | Pedido mínimo, prazo e "4 passos, sem cadastro" **logo abaixo do botão principal** | Implementado |
| Formato para repassar (P1) | Botões **Baixar resumo** e **Copiar texto** no resumo | Implementado |
| Faixa de preço "a partir de" (P1) | Não implementado: depende de dado que a empresa não divulga | Recomendação à MEGA-WR |
| Valor diferente para poucas peças (P2) | Não implementado: é decisão comercial, não de interface | Recomendação à MEGA-WR |

[[FONTE: Elaborado pelo autor.]]

[[PAR: 05-passo2-abaixo-minimo-v1.png ; 05-passo2-abaixo-minimo-v2.png | Antes: sem saída ; Depois: com alternativas | Melhoria 1: pedido abaixo do mínimo | Elaborado pelo autor.]]

[[PAR: 01-home-v1-topo.png ; 01-home-v2-topo.png | Antes ; Depois: mínimo, prazo e "sem cadastro" | Melhoria 3: condições junto do botão principal | Elaborado pelo autor.]]

[[PAR: 09-resumo-v1.png ; 11-pedido-em-grupo.png | Resumo antes, sem baixar nem copiar ; Nova tela de pedido em grupo | Melhorias 1 e 4: pedido em grupo e resumo repassável | Elaborado pelo autor.]]

[[QUEBRA]]

# 9 Reflexão crítica e ética

A solução aplica UX ao partir do que as pessoas viveram, e UI ao traduzir isso em hierarquia, contraste e um único caminho claro por tela. Ela devolve ao usuário o controle do pedido: saber o que será perguntado, pausar, revisar e corrigir. Mostrar o pedido mínimo antes é uma questão de **transparência** (PUCPR, [2026?]f), porque evita que alguém perca tempo com uma conversa que não vai virar venda. O fluxo pede só nome, WhatsApp e cidade, sem CNPJ, seguindo o princípio da **necessidade** da LGPD (BRASIL, 2018). Não usa *dark patterns*, respeita contraste e tamanho de toque e, por ser projetado para quem só tem celular, é **inclusivo**.

# 10 Conclusão

O principal aprendizado do processo foi que o problema não estava no canal. O WhatsApp é o canal certo para a MEGA-WR; o erro era chegar até ele sem nada nas mãos. A avaliação heurística apontou onde olhar, mas foram as conversas que mostraram o que as heurísticas sozinhas não mostram: que tanto a compradora da empresa quanto o comprador individual dependem de outras pessoas para concluir o pedido. As duas funções mais valorizadas do protótipo revisado, o pedido em grupo e o salvar para continuar, nasceram desse achado, e não do diagnóstico inicial.

Numa próxima iteração, as prioridades são:

1. **Refazer a pesquisa e os testes com pessoas reais**: duas entrevistas e três testes, com tempo medido no site atual e no protótipo, para ter comparação de antes e depois.
2. **Conversar com William e Rosangela** sobre o volume de pedidos abaixo do mínimo, a viabilidade de uma faixa de preço inicial e de um preço para poucas peças, a existência de taxa de arte e a operação do pedido em grupo.
3. **Medir depois de publicar**: quantas conversas iniciadas pelo site viram orçamento, comparando o botão atual com o novo fluxo por meio de um teste A/B (PUCPR, [2026?]e).

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

[[QUEBRA]]

# Apêndice A – Roteiro da entrevista

**Parte exploratória**

1. Me conta rapidinho o que você faz.
2. Quando precisa resolver alguma coisa, você usa mais o celular ou o computador?
3. Com que frequência você compra ou contrata algo feito sob medida?
4. Me conta da última vez que você pediu orçamento de algo sob medida. O que era?
5. Como você começou? Qual foi o primeiro lugar que você olhou?
6. Como foi o contato? Me conta o passo a passo.
7. Quanto tempo levou da primeira mensagem até ter um preço na mão?
8. Teve alguma hora em que você ficou sem saber o que responder ou perguntar?
9. Teve alguma informação que você só descobriu depois e queria ter sabido no começo?
10. Você pediu orçamento em mais de um lugar? Como escolheu?
11. Já desistiu de um orçamento no meio do caminho? O que fez você desistir?
12. Se pudesse mudar uma coisa nesse processo, o que seria?

**Parte de validação (com o protótipo)**

13. O que você achou?
14. Ficou faltando alguma informação para você se sentir seguro de enviar?
15. De 1 a 5, quanto você confiou que ia conseguir o que precisava? Por quê?
16. Se fosse de verdade, você enviaria ou procuraria outro lugar?

# Apêndice B – Registro das entrevistas

[[TAG-SIMULACAO]]

## P1 – compradora B2B, 42 anos

**1.** "Sou coordenadora administrativa numa clínica odontológica aqui em Leme. Cuido de tudo que não é dente: compras, escala, fornecedor, pagamento, RH básico. Se quebrou alguma coisa ou falta alguma coisa, é comigo."

**2.** "Pra pesquisar, celular, porque é no intervalo, entre um paciente e outro na recepção. Mas quando vou montar alguma coisa pro sócio, eu passo pro computador, faço uma planilhinha ou junto tudo num e-mail."

**3.** "Pra clínica, umas duas ou três vezes por ano. Uniforme, jaleco, às vezes brinde pra paciente em data comemorativa, fachada teve uma vez. Pra mim mesma, quase nunca."

**4.** "Tá acontecendo agora, na verdade. Uniforme pra equipe toda: 14 pessoas, entre recepção, auxiliar e ASB. O sócio quer tudo padronizado, com logo bordado. Antes disso foi jaleco, faz uns oito meses."

**5.** "Pedi indicação no grupo de WhatsApp de outras clínicas e joguei no Google 'uniforme personalizado Leme'. Abri uns três ou quatro sites. Queria ver se trabalhavam com área da saúde e ter uma noção de preço antes de falar com alguém."

**6.** "Num deles cliquei em 'orçamento' e caiu no WhatsApp com aquela mensagem pronta, tipo 'olá, gostaria de um orçamento'. Mandei. A moça respondeu umas duas horas depois perguntando qual modelo, quantas peças, qual tecido, se era bordado ou silk, os tamanhos... Eu não sabia metade. Tecido, por exemplo, eu não faço ideia. Falei que ia ver e voltava. Levei dois dias pra voltar."

**7.** "Nesse, uns cinco dias, mas muito por minha causa, porque eu tive que ir atrás dos tamanhos de todo mundo. Em outro lugar mandaram uma tabela em PDF no mesmo dia. Ajudou, mas não tinha o bordado incluso, então não dava pra comparar."

**8.** "Várias vezes. 'Qual gramatura?' Não sei. 'Quer o logo em quantas posições?' Nem tinha pensado. E aí fica aquela sensação de que você tá atrasando a pessoa, sabe? Ou de que vai responder qualquer coisa e depois o preço vem errado."

**9.** "O prazo. Um deles era 30 dias úteis, e a gente queria pra antes de uma reunião com um convênio. E que a arte do bordado tinha uma taxa separada, que só apareceu no final."

**10.** "Pedi em três. Ainda não escolhi, quem escolhe é o sócio. Mas o meu problema é que cada um me mandou de um jeito: um por PDF, um por áudio, um digitado no WhatsApp. Pra levar pra ele eu tive que passar tudo pra uma tabela, e mesmo assim não batia, porque cada um orçou uma coisa diferente."

**11.** "Desistir mesmo, não. Mas já deixei conversa morrer. Abri, a pessoa perguntou um monte de coisa, eu fiquei de responder e não respondi. Depois de uma semana fica chato voltar. Aí acabo indo em outro."

**12.** "Saber antes o que vão me perguntar. Se eu soubesse que precisava de tamanho, cor e onde vai o logo, eu já juntava tudo antes de chamar. E que o orçamento viesse num formato que eu pudesse repassar direto."

**13.** "Gostei bastante do passo de personalização, porque me mostra as opções. Eu não preciso saber o nome técnico, só escolher 'bordado no peito' ou coisa assim. E gostei que no final eu vejo a mensagem antes de mandar. Uma dúvida: dá pra salvar e voltar depois? Porque no meio eu vou ter que perguntar os tamanhos pro pessoal."

**14.** "Uma faixa de preço, mesmo que aproximada, tipo 'a partir de'. E o prazo médio de produção. Se aparecesse que o mínimo é 10 peças, também já me tranquilizava, porque eu sei que 14 passa. E gostei que não pediu CNPJ. Se pedisse logo no começo, eu provavelmente fechava."

**15.** "Um 4. Eu mandaria sabendo que a pessoa do outro lado já entendeu o que eu quero, então não vou passar vergonha. Não dou 5 porque ainda não sei o preço, e é isso que o sócio vai perguntar primeiro."

**16.** "Mandaria. Provavelmente mandaria primeiro pra eles, porque foi o jeito mais fácil. Mas ia continuar com os outros orçamentos pra comparar, isso eu faço de qualquer jeito."

## P2 – comprador B2C, 26 anos

**1.** "Sou técnico de enfermagem, trabalho num hospital em Pirassununga, plantão 12x36. Às vezes pego extra em outro lugar."

**2.** "Celular, 100%. Nem tenho computador em casa, na verdade."

**3.** "Quase nunca. Scrub eu compro uma vez por ano, às vezes duas. Normalmente pronto, em loja online. Personalizado foi a primeira vez que fui atrás."

**4.** "Foi uns quatro meses atrás. Queria dois scrubs com meu nome e o COREN bordados. No hospital o pessoal tá usando e fica bonito, profissional."

**5.** "Vi no Instagram. Apareceu um post de uma confecção, acho que era patrocinado, com um scrub bordado. Entrei no perfil, depois no site pelo link da bio. Era de noite, depois do plantão, deitado já."

**6.** "Olhei os modelos no site, escolhi a cor, vi que fazia bordado. Cliquei em orçamento, abriu o WhatsApp. Mandei a mensagem e ainda escrevi embaixo 'quero 2 scrubs azul marinho tamanho M com nome e COREN'. No outro dia de manhã me responderam que o pedido mínimo era 10 peças."

**7.** "Nunca tive. Não chegou nem a ter preço, porque eu não fechava 10."

**8.** "Não, eu sabia bem o que queria. O problema não foi esse."

**9.** "O mínimo, óbvio. Se estivesse escrito no site, eu nem tinha perdido tempo. Fiquei meio chateado, sinceramente. Parecia que era pra qualquer um."

**10.** "Depois disso, sim. Achei uma loja online que vende o scrub e você digita o nome na hora de comprar, já tem o preço do bordado ali. Comprei lá. Saiu um pouco mais caro que eu imaginava, mas foi rápido."

**11.** "Essa foi uma. Desisti porque não tinha como. Até pensei em juntar com o pessoal do plantão, perguntei no grupo, duas meninas se interessaram, mas aí fica difícil organizar tamanho, pagamento, e acabei deixando pra lá."

**12.** "Colocar o mínimo logo de cara. Nem que seja pequenininho embaixo do botão."

**13.** "Achei bem mais organizado. No passo da quantidade, quando eu coloquei 2 e apareceu que o mínimo é 10, pelo menos eu soube na hora, sem precisar mandar mensagem. Mas aí eu fico meio... e agora? Parou ali pra mim."

**14.** "Faltou falar o que eu faço se quiser menos que 10. Se tivesse algo tipo 'junte com colegas' ou 'indique sua equipe', talvez eu tentasse de novo com o pessoal do hospital. Ou se tivesse um valor diferente pra pouca peça, eu até pagava mais."

**15.** "Pro meu caso, um 2. O site é bom e parece sério, mas não é pra mim. Se eu fosse comprar pra equipe, dava um 4."

**16.** "Procuraria outro lugar. Mas eu salvaria o perfil deles, porque se um dia o hospital ou o pessoal do setor quiser fazer junto, eu lembro deles."
