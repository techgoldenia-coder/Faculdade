# Histórico

Registro cronológico do que foi feito. Serve para retomar contexto em sessões futuras.

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
