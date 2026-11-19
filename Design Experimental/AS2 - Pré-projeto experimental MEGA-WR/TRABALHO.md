<!--
CONTROLE (não vai para o PDF)
- Disciplina: Design Experimental — Atividade Somativa 2. Individual. Prazo e peso: [confirmar].
- Enunciado: pré-projeto de pesquisa experimental respondendo às 12 perguntas (problema, hipóteses, VI, VD,
  controle, design, ambiente, tratamento, participantes, seleção, design dos participantes, análise estatística).
  Exemplo dado no enunciado: Enns e Hackett (1990), via Creswell (2014). Entrega em PDF a partir do template Word.
- Tema escolhido pelo Yan em 19/11/2026: MEGA-WR, fatorial 2x2 (condições de compra × tipo de foto) sobre a
  intenção de pedir orçamento. Base das hipóteses: entrevistas reais da AS2 de Construção de Interfaces (P1 e P2).
- Fonte do PDF: este arquivo → gerar_docx.py → .docx no template → PDF exportado pelo Word.
- Sintaxe: "QUADRO:" = título acima do quadro; "FONTE:" = fonte abaixo; "LARGURAS:" = largura das colunas em cm.
-->

# Transparência e prova social no anúncio de uniformes personalizados

*Pré-projeto de pesquisa experimental aplicado à MEGA-WR Confecções*

## 1 Contexto e problema do estudo

A MEGA-WR Confecções é uma confecção familiar de Leme/SP com três linhas: Saúde, Uniformes e Fitness. O foco é o cliente empresarial, como escolas, empresas, clínicas e academias, e o atendimento é feito na loja e pelo WhatsApp (MEGA-WR CONFECÇÕES, 2026). Segundo os proprietários, a empresa atua há cerca de dez anos, trabalha com pedido mínimo de 10 peças por modelo e prazo de produção de 20 a 30 dias, e não tem tabela de preço, porque cada orçamento depende de modelo, tecido, quantidade e personalização (SUYAMA, 2026).

Uma pesquisa qualitativa feita pelo autor com compradores de uniformes de Leme (SUYAMA, 2026) mostrou um padrão: as condições de compra aparecem tarde. Um dono de academia desistiu de um fornecedor "pelo mínimo e pelo medo de encalhar" e pediu uma referência de preço, "nem que seja 'a partir de R$ tanto'". O mesmo entrevistado contou que encontrou o fornecedor pelo Instagram de outra academia e que confia em quem é da cidade. Hoje, o site da MEGA-WR não mostra o mínimo nem uma referência de preço antes do primeiro contato (SUYAMA, 2026).

Essa pesquisa foi exploratória: levantou indícios com duas pessoas, sem permitir conclusão sobre causa e efeito. Para isso é preciso uma pesquisa conclusiva causal, que manipula a possível causa e mede o efeito (PUCPR, [2025]b). Daí o problema deste estudo:

**Informar as condições de compra (pedido mínimo e preço de referência) e mostrar a foto de um cliente real da região em um anúncio de Instagram aumenta a intenção de pedir orçamento à MEGA-WR entre os responsáveis pela compra de uniformes de organizações de Leme e região?**

O problema atende aos critérios do material: é observável e operacionalizável, porque cada elemento do anúncio pode ser ligado ou desligado e a intenção pode ser medida em escala; é pertinente, porque a resposta define o que a empresa mostra nos anúncios e no site; e é delimitado, porque trata de um público, uma região e um período (PUCPR, [2025]f).

**Objetivo do experimento:** avaliar o efeito das condições de compra no anúncio e do tipo de foto, e da interação entre os dois, sobre a intenção de pedir orçamento, mantendo constantes todos os outros elementos do anúncio.

A estrutura a seguir segue os componentes do exemplo de Enns e Hackett (1990 apud CRESWELL, 2014): participantes, planejamento experimental, manipulação, instrumentos com verificação da manipulação e procedimento. O Quadro 1 resume as respostas às perguntas da atividade, detalhadas nas seções seguintes.

QUADRO: Quadro 1 – Síntese do pré-projeto
LARGURAS: 5.2;11.8
| Pergunta da atividade | Resposta neste pré-projeto |
|---|---|
| Problema do estudo | Se mostrar o pedido mínimo e o preço de referência, e a foto de um cliente real, aumenta a intenção de pedir orçamento à MEGA-WR |
| Hipóteses | H1: as condições de compra aumentam a intenção; H2: a foto de cliente real aumenta a intenção; H3: há interação entre os dois fatores |
| Variáveis independentes | Condições de compra no anúncio (ausentes × presentes) e tipo de foto (produto em estúdio × cliente real da região) |
| Variáveis dependentes | Intenção de pedir orçamento (escala de 7 pontos, 3 itens) e pedido de contato ao final (sim/não) |
| Variáveis de controle | Formato e texto do anúncio, produto, prazo informado, tempo de exposição, ordem das perguntas, período de coleta; medidas: tipo e porte da organização, quantidade por pedido, familiaridade com a marca e aparelho |
| Tipo de design | Experimento verdadeiro, com delineamento fatorial 2 × 2 (4 condições) |
| Ambiente | Laboratório: ambiente on-line simulado, com o anúncio em uma tela de feed do Instagram |
| Tratamento | Quatro versões do mesmo anúncio, que mudam apenas a faixa de condições e a foto |
| Participantes | 160 responsáveis pela compra de uniformes (40 por condição); mínimo de 128 válidos |
| Seleção | Amostra não probabilística por conveniência e indicação, com filtro de elegibilidade; distribuição aleatória entre as condições |
| Design dos participantes | Entre participantes (entre sujeitos): cada pessoa vê uma única versão |
| Análise estatística | ANOVA fatorial 2 × 2 para a intenção; qui-quadrado e regressão logística para o pedido de contato |
FONTE: Elaborado pelo autor (2026).

## 2 Hipóteses

As hipóteses partem de evidência anterior, como recomenda o material (PUCPR, [2025]f), e não de suposição. As duas primeiras vêm das entrevistas: o comprador que desconhece o mínimo e o preço tem medo de "preencher tudo e aí é caro", e o pequeno comprador confia em fornecedor que outro cliente da cidade já usa (SUYAMA, 2026). A terceira é de interação: a foto de um cliente real pode tornar as condições mais críveis, porque mostra que outra organização da região já comprou nessas condições.

QUADRO: Quadro 2 – Hipóteses nula (H₀) e alternativa (H₁)
LARGURAS: 3.2;6.9;6.9
| Hipótese | H₀ (sem efeito) | H₁ (com efeito) |
|---|---|---|
| H1: condições de compra | A intenção média de pedir orçamento é igual com ou sem as condições no anúncio | A intenção média é maior quando o anúncio informa o pedido mínimo e o preço de referência |
| H2: tipo de foto | A intenção média é igual com a foto de produto e com a foto de cliente real | A intenção média é maior com a foto de um cliente real da região |
| H3: interação | O efeito das condições de compra é o mesmo para os dois tipos de foto | O efeito das condições de compra é diferente conforme o tipo de foto (esperado: maior com a foto de cliente real) |
FONTE: Elaborado pelo autor (2026).

As mesmas três hipóteses valem para a segunda variável dependente, o pedido de contato. Nesse caso, a comparação é entre as proporções de pessoas que pedem orçamento em cada condição. O nível de significância adotado é α = 0,05.

## 3 Variáveis do estudo

### 3.1 Variáveis independentes

São os dois fatores manipulados pelo pesquisador, cada um com dois níveis (PUCPR, [2025]c):

- **Fator A, condições de compra no anúncio.** Nível A1, ausentes: o anúncio não informa mínimo nem preço, como acontece hoje. Nível A2, presentes: uma faixa no rodapé da imagem informa "Pedido a partir de 10 peças por modelo" e "Camiseta personalizada a partir de R$ X". Como a empresa não tem tabela de preço, X será definido com os proprietários antes da coleta: o menor valor que eles conseguem cumprir para uma camiseta personalizada simples.
- **Fator B, tipo de foto.** Nível B1, produto: a camiseta personalizada fotografada em estúdio, sem pessoas. Nível B2, cliente real: a equipe de uma organização de Leme, cliente da MEGA-WR, usando a mesma camiseta, com uma legenda que identifica a organização e a cidade. A foto só é usada com autorização por escrito do cliente.

As duas variáveis são qualitativas nominais e entram na análise codificadas (0 = ausente ou produto; 1 = presente ou cliente real).

### 3.2 Variáveis dependentes

- **VD1, intenção de pedir orçamento.** Definição conceitual: disposição declarada de procurar a MEGA-WR para cotar uniformes. Definição operacional: média de três afirmações em escala de 7 pontos, de "discordo totalmente" (1) a "concordo totalmente" (7): "Eu pediria um orçamento à MEGA-WR"; "Se precisasse de uniformes agora, eu clicaria em 'Pedir orçamento'"; e "Eu incluiria a MEGA-WR entre os fornecedores que consultaria". É uma variável quantitativa intervalar.
- **VD2, pedido de contato.** Definição operacional: resposta à pergunta final "Quer que a MEGA-WR entre em contato com um orçamento para a sua organização?", com resposta sim ou não. É uma variável qualitativa, mas mede uma decisão real: quem responde "sim" recebe o contato. Por isso, aproxima a intenção do comportamento.

### 3.3 Variáveis de controle

Variáveis de controle não fazem parte do teste, mas podem interferir no resultado e devem ser mantidas constantes ou neutralizadas (PUCPR, [2025]c). Neste estudo, a maioria é mantida constante pelo próprio desenho do anúncio e do questionário; as características dos participantes, que não podem ser fixadas, são medidas e conferidas na análise (Quadro 3).

QUADRO: Quadro 3 – Variáveis de controle e forma de controle
LARGURAS: 5.2;11.8
| Variável | Como é controlada |
|---|---|
| Formato e texto do anúncio | Mesmo modelo de post do Instagram (1080 × 1350 px), mesmo título ("Uniformes personalizados para a sua equipe"), mesma legenda e mesmo botão "Pedir orçamento" nas quatro versões |
| Produto mostrado | Mesmo modelo e mesma cor de camiseta nas duas fotos |
| Prazo informado | "Produção em 20 a 30 dias" aparece nas quatro versões, para que só o mínimo e o preço variem |
| Tempo de exposição | O botão "Avançar" só aparece após 15 segundos de anúncio na tela |
| Instrumento e ordem das perguntas | Mesmo questionário, na mesma ordem, para todos |
| Período de coleta | Uma única janela de quatro semanas, fora da Black Friday e da volta às aulas, que mudam a procura por uniformes |
| Tipo e porte da organização, quantidade por pedido, familiaridade com a MEGA-WR, cidade e aparelho usado | Medidos no questionário; a aleatorização tende a distribuí-los igualmente entre os grupos, o que é conferido na análise |
FONTE: Elaborado pelo autor (2026).

## 4 Design experimental

### 4.1 Tipo de experimento e delineamento estatístico

O estudo é um **experimento verdadeiro**: os participantes são distribuídos aleatoriamente entre as condições, e existe um grupo de controle bem definido (PUCPR, [2025]d). O grupo de controle é a condição A1B1, sem condições de compra e com foto de produto, que serve de referência para medir o efeito de cada mudança (PUCPR, [2025]a).

O delineamento é o **fatorial simples 2 × 2** (2²): dois fatores manipulados ao mesmo tempo, cada um com dois níveis, o que permite medir os efeitos principais e a interação (PUCPR, [2025]e). Ele foi escolhido porque o problema tem dois fatores e uma hipótese de interação (H3). Um delineamento inteiramente casualizado com um fator só obrigaria a fazer dois experimentos separados e não mostraria a interação. O delineamento em blocos não foi usado porque não há uma fonte de variação conhecida que justifique blocos; as diferenças entre organizações são tratadas como variáveis de controle medidas.

QUADRO: Quadro 4 – Condições experimentais do fatorial 2 × 2
LARGURAS: 4.6;6.2;6.2
| | B1: foto de produto | B2: foto de cliente real |
|---|---|---|
| A1: sem condições de compra | Condição 1, grupo de controle (n = 40) | Condição 2 (n = 40) |
| A2: com mínimo e preço de referência | Condição 3 (n = 40) | Condição 4 (n = 40) |
FONTE: Elaborado pelo autor (2026).

### 4.2 Ambiente: laboratório

O experimento é de **laboratório**, em ambiente on-line simulado: o participante vê o anúncio dentro de uma imagem do feed do Instagram, como na simulação de site de e-commerce citada no material (PUCPR, [2025]d). A escolha prioriza a validade interna. No laboratório, todos veem o mesmo anúncio pelo mesmo tempo e respondem às mesmas perguntas. Em um teste de campo no Meta Ads, o algoritmo entregaria cada versão a públicos diferentes, e a intenção não poderia ser medida em escala.

O custo é a validade externa, porque o ambiente é artificial e o participante sabe que está em uma pesquisa (PUCPR, [2025]d). Por isso, o estudo prevê uma **replicação em campo** (PUCPR, [2025]a): a combinação vencedora será testada contra o anúncio atual em um teste A/B no Meta Ads, com público de Leme e região, medindo conversas iniciadas no WhatsApp.

### 4.3 Design dos participantes: entre sujeitos

O design é **entre participantes (entre sujeitos)**: cada pessoa vê apenas uma das quatro versões. No design intraparticipantes, quem visse a versão com o preço e depois a versão sem o preço já saberia o preço, e a segunda resposta ficaria contaminada pela primeira. O design entre sujeitos evita esse efeito de aprendizagem e de ordem, com o custo de exigir mais participantes (PUCPR, [2025]d).

## 5 Tratamento: manipulação da variável independente

As quatro versões do anúncio serão produzidas a partir de um único arquivo, pelo mesmo designer, com a identidade visual da MEGA-WR. Só dois elementos mudam:

- **Condições de compra (fator A):** nas versões A2, entra uma faixa no rodapé da imagem, nas cores da marca, com "Pedido a partir de 10 peças por modelo · Camiseta personalizada a partir de R$ X". Nas versões A1, o mesmo espaço mostra só o logo, para que a área ocupada pelo texto seja parecida.
- **Tipo de foto (fator B):** as duas fotos têm o mesmo enquadramento aproximado, a mesma luz e a mesma camiseta. A diferença é a presença das pessoas de uma organização real da cidade, identificada na legenda.

O participante recebe a instrução: "Imagine que você está procurando um fornecedor de uniformes personalizados para a sua organização e encontra este anúncio no Instagram". Em seguida, vê o anúncio por pelo menos 15 segundos. A manipulação é conferida depois (seção 7) com duas perguntas, uma para cada fator, como Enns e Hackett fizeram (1990 apud CRESWELL, 2014).

## 6 Participantes

### 6.1 Quem e quantos

Os participantes são **160 responsáveis pela compra de uniformes**, ou pessoas que participam dessa decisão, em organizações de Leme e de cidades vizinhas, como Araras e Pirassununga. São donos e gestores de academias, escolas, clínicas e comércios, e profissionais de RH e compras de empresas e indústrias. Eles correspondem às duas personas da pesquisa anterior: a compradora de empresa e o dono de pequeno negócio (SUYAMA, 2026).

O tamanho da amostra deve ser grande o bastante para detectar o efeito dos fatores, sem encarecer o estudo além do necessário (PUCPR, [2025]b). Uma análise de poder estatístico para a ANOVA fatorial, com efeito médio (f = 0,25), α = 0,05, poder de 0,80 e quatro grupos, indica um **mínimo de 128 participantes válidos** (COHEN, 1988; FAUL *et al.*, 2007). O estudo planeja **160 (40 por condição)**, uma margem de 20% para as exclusões descritas abaixo. Os 40 por condição coincidem com o exemplo de fatorial do material, que usou 40 participantes por combinação (PUCPR, [2025]g).

### 6.2 Como os participantes são selecionados

A amostragem é **não probabilística, por conveniência e por indicação**, porque não existe uma lista de todos os compradores de uniformes da região. O convite é feito por três caminhos: grupos de WhatsApp de profissionais de RH e de empresários da região; contato direto do autor com academias, escolas e clínicas; e indicação dos próprios participantes. O convite fala em "pesquisa acadêmica da PUCPR sobre compra de uniformes" e **não cita a MEGA-WR**, para não atrair só quem já gosta da marca.

- **Critérios de inclusão:** ter 18 anos ou mais e decidir ou participar da compra de uniformes em uma organização de Leme ou região, conferido por uma pergunta-filtro no início do questionário.
- **Critérios de exclusão:** ser cliente atual, funcionário ou parente dos proprietários da MEGA-WR; ter participado do pré-teste; errar a pergunta de atenção; ou responder em menos de um terço do tempo mediano do pré-teste.

Depois do filtro, a **plataforma do questionário sorteia a condição** de cada participante, com distribuição equilibrada entre os quatro grupos (por exemplo, o recurso de randomização do Qualtrics ou do LimeSurvey). A aleatorização garante que as diferenças entre os grupos venham do anúncio, e não do perfil de quem caiu em cada um (PUCPR, [2025]a). Se as exclusões deixarem alguma condição com menos de 32 respostas válidas, a coleta continua até completar esse número.

## 7 Procedimento e instrumento de coleta

O instrumento é um **questionário estruturado** on-line, com perguntas fechadas e escalas, aplicado igualmente a todos (PUCPR, [2025]g). Antes da coleta, um **pré-teste com 10 pessoas** do público, que não entram na amostra, verifica se as perguntas são claras, se as duas manipulações são percebidas e quanto tempo o questionário leva (previsão: cerca de 6 minutos). A sequência é:

1. **Termo de consentimento:** objetivo da pesquisa, participação voluntária, anonimato e direito de desistir, conforme as normas de pesquisa com seres humanos (BRASIL, 2012).
2. **Pergunta-filtro e perfil:** função na compra de uniformes, tipo e porte da organização, cidade e quantidade de peças em um pedido típico.
3. **Sorteio da condição e exposição:** instrução do cenário e anúncio na tela por pelo menos 15 segundos.
4. **Variável dependente 1:** as três afirmações de intenção, em ordem fixa.
5. **Verificação da manipulação:** "O anúncio informava a quantidade mínima de peças?" e "A foto mostrava a equipe de uma organização real?", com as respostas sim, não e não lembro.
6. **Controles finais:** pergunta de atenção ("para mostrar que está lendo, marque 'concordo totalmente'"), se já conhecia a MEGA-WR e o aparelho usado.
7. **Variável dependente 2:** a pergunta do pedido de contato. Só quem responde "sim" informa nome e WhatsApp. Esses dados ficam separados das respostas e são usados apenas para o contato autorizado.
8. **Encerramento:** explicação de que existiam quatro versões do anúncio e agradecimento.

As respostas ficam registradas na própria plataforma, com a condição sorteada, a data e o tempo de resposta. São exportadas em planilha para a análise, sem identificação dos participantes.

## 8 Análise estatística

A análise segue o delineamento e o tipo de cada variável dependente, como orienta o material (PUCPR, [2025]g). O software previsto é o JASP, gratuito, ou o SPSS.

- **Preparação dos dados:** exclusão pelos critérios da seção 6.2. Em seguida, verificação da manipulação: o teste qui-quadrado deve mostrar que quem viu a faixa de condições respondeu "sim" na pergunta correspondente em proporção maior do que quem não viu, e o mesmo para a foto.
- **Confiabilidade da escala:** consistência interna dos três itens de intenção pelo alfa de Cronbach (CRONBACH, 1951), como Enns e Hackett relataram para as suas escalas (1990 apud CRESWELL, 2014). Com alfa de 0,70 ou mais, os itens viram um índice único pela média.
- **Equivalência dos grupos:** qui-quadrado para conferir se tipo de organização, porte, quantidade por pedido e familiaridade com a marca ficaram distribuídos de forma parecida nas quatro condições.
- **Teste das hipóteses na VD1:** **ANOVA fatorial 2 × 2** (dois fatores), que testa o efeito principal das condições de compra (H1), o efeito principal do tipo de foto (H2) e a interação (H3). H₀ é rejeitada quando p < 0,05 (PUCPR, [2025]g). Se a interação for significativa, as quatro médias são comparadas duas a duas pelo teste de Tukey. Os resultados são apresentados com o tamanho do efeito (eta² parcial) e intervalos de confiança de 95%.
- **Pressupostos da ANOVA:** análise dos resíduos quanto à normalidade (teste de Shapiro-Wilk) e à homogeneidade das variâncias (teste de Levene). A independência é garantida pelo design entre sujeitos (PUCPR, [2025]g). Se algum grupo ficar desequilibrado em uma variável de controle, a análise é repetida incluindo essa variável como covariável (ANCOVA).
- **Teste das hipóteses na VD2:** como o pedido de contato é sim ou não, usa-se o qui-quadrado de independência entre as quatro condições e uma regressão logística com os dois fatores e a interação. Foi o mesmo tipo de modelo que a Buzzware usou para estimar taxas de resposta (PUCPR, [2025]b).
- **Análise exploratória:** a interação entre as condições de compra e a quantidade típica por pedido. O mínimo de 10 peças pode atrair quem compra mais e afastar quem compra menos. Para a MEGA-WR, isso também é resultado útil, porque filtra contatos que não virariam pedido.

Por fim, o resultado é lido também pela **significância gerencial**, e não só pela estatística (PUCPR, [2025]g). Antes da coleta, fica combinado com os proprietários um critério de decisão: uma diferença de pelo menos 0,5 ponto na escala de intenção, ou de 5 pontos percentuais no pedido de contato, é suficiente para recomendar que a MEGA-WR mostre o mínimo e o preço de referência nos anúncios e no site. O passo seguinte é a replicação em campo prevista na seção 4.2.

## 9 Limitações e cuidados éticos

- **Validade externa:** o ambiente simulado e a amostra regional por conveniência limitam a generalização. O resultado vale para compradores de uniformes de Leme e região, e não para qualquer público. A replicação em campo reduz essa limitação.
- **Intenção não é compra:** a VD2 aproxima a intenção do comportamento, mas a conversão em pedido só pode ser medida em campo.
- **O valor do preço influencia o resultado:** o efeito encontrado vale para o preço de referência testado. Um valor diferente poderia mudar a reação, e a empresa só deve anunciar um "a partir de" que consiga cumprir em qualquer orçamento.
- **Ética:** consentimento livre e esclarecido, anonimato das respostas (BRASIL, 2012), autorização de uso de imagem do cliente da foto e uso dos contatos apenas por quem pediu o orçamento.

## Referências

BRASIL. Conselho Nacional de Saúde. **Resolução nº 466, de 12 de dezembro de 2012**. Aprova as diretrizes e normas regulamentadoras de pesquisas envolvendo seres humanos. Brasília, DF: Ministério da Saúde, 2012.

COHEN, J. **Statistical power analysis for the behavioral sciences**. 2. ed. Hillsdale: Lawrence Erlbaum Associates, 1988.

CRESWELL, J. W. **Research design**: qualitative, quantitative, and mixed methods approaches. 4. ed. Thousand Oaks: SAGE Publications, 2014.

CRONBACH, L. J. Coefficient alpha and the internal structure of tests. **Psychometrika**, v. 16, n. 3, p. 297-334, 1951.

FAUL, F. *et al.* G\*Power 3: a flexible statistical power analysis program for the social, behavioral, and biomedical sciences. **Behavior Research Methods**, v. 39, n. 2, p. 175-191, 2007.

MEGA-WR CONFECÇÕES. **MEGA-WR Confecções**: uniformes profissionais, escolares e da saúde. Leme, 2026. Disponível em: https://megawr.com.br. Acesso em: 19 nov. 2026.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 01: desvendando o mundo dos experimentos: uma jornada na introdução do design experimental. Curitiba: PUCPR, [2025]a. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 02: a causalidade e os experimentos. Curitiba: PUCPR, [2025]b. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 03: conheça as variáveis utilizadas na pesquisa experimental. Curitiba: PUCPR, [2025]c. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 04: tipos de experimentos. Curitiba: PUCPR, [2025]d. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 05: design experimental estatístico. Curitiba: PUCPR, [2025]e. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 06: passo a passo de um experimento – parte 1. Curitiba: PUCPR, [2025]f. Material didático.

PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Design experimental**: unidade 07: passo a passo de um experimento – parte 2. Curitiba: PUCPR, [2025]g. Material didático.

SUYAMA, Y. **Repensando a solicitação de orçamento da MEGA-WR**: projeto de UX/UI do fluxo de orçamento de uma confecção de uniformes. 2026. Trabalho acadêmico (Construção de Interfaces e Experiência do Usuário) – Pontifícia Universidade Católica do Paraná, Leme, 2026.
