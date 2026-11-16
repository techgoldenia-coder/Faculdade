# Estrutura de Pastas — Faculdade

Mapa objetivo. Atualizado automaticamente quando a estrutura muda.

**Organização por matéria, não por semestre.** Cada matéria é uma pasta na raiz. O semestre fica registrado no `INFO.md` da matéria e no `PAINEL.md`.

- `/` — raiz: arquivos de controle (`CLAUDE.md`, `PAINEL.md`, `ESTRUTURA.md`, `HISTORICO.md`), `README.md` (capa do repositório no GitHub) e `.gitignore` + uma pasta por matéria. Versionado em `techgoldenia-coder/Faculdade` (privado).
- `PAINEL.md` — índice de todas as matérias (semestre, status, professor), prazos em aberto, datas do semestre e notas. Primeiro arquivo a consultar.
- `0 - Institucional/` — o que vale para o curso inteiro. `Normas-ABNT.md` (formatação, citações NBR 10520, referências NBR 6023; template do professor sempre prevalece); `Grade-Curricular.md` (grade oficial e situação de cada matéria, a preencher); `BANCO-DE-REFERENCIAS.md` (toda fonte já usada em trabalho, em ABNT, com onde foi usada — transversal às matérias, por isso fica aqui).
- `1 - Modelos/` — modelos para copiar. `MODELO-INFO-Materia.md`, `MODELO-Anotacao-de-Aula.md`, `MODELO-Trabalho.md` (enunciado, critérios de correção, estrutura, checklist de entrega), `MODELO-Resumo-para-Prova.md` (mapa de conteúdo, comparações, simulado, erros). `_MODELO-MATERIA/` — pasta pronta para clonar ao abrir matéria nova.

## Matérias

- `Gestão de Anúncios em Canais Sociais/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs + transcrições das videoaulas 2 a 8. Contém `AS1 - Plano de Mídia MEGA-WR/` (.docx, planilha operacional e `Imagens/` com as peças) e `AS2 - Otimização do Plano de Mídia MEGA-WR/` — `TRABALHO.md` (enunciado, decisões, premissas e roteiro), `YanSuyama_AS2_GestaoAnuncios.pdf` (entrega, 24 páginas), `AS2 - Otimização do Plano de Mídia MEGA-WR.pptx` (versão editável) e `AS2 - Dados hipotéticos MEGA-WR.xlsx` (números com fórmulas + modelo de controle de leads). Na raiz, `Layout trabalho.docx` (template da AS1).
- `Gestão de Conteúdo em Mídias Sociais/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs (presença on-line → social listening → personas e posicionamento (case Sallve) → identidade e tom de voz → influência e estratégia de conteúdo → métricas → multiplataforma → fechamento). Contém `AS2 - Planejamento de conteúdo MEGA-WR/` — relatório individual (marca, calendário 70-20-10 de outubro/2026, métricas, community management e crise): `TRABALHO.md` (fonte do PDF; notas de controle em comentário no topo), `YanSuyama_AS2_GestaoConteudo.pdf` (entrega, 18 páginas, ABNT) e `gerar_pdf.py` (regenera o PDF).
- `Gestão de marcas/` — 2026/1, concluída. 6 PDFs na base (inclui `Branding.pdf`, 3 MB, aparentemente material de referência e não slide de aula).
- `Marketing de conteúdo/` — 2026/1, concluída. 11 PDFs na base.
- `Processos de decisão e tipos de segmentação/` — 2026/1, concluída. 6 PDFs na base.

- `Construção de Interfaces e Experiência do Usuário/` — 2026/2, **cursando**. disciplina completa em 8 PDFs de unidade (UX/UI → usabilidade e design visual → pesquisa e personas → arquitetura da informação → prototipagem → testes de usabilidade → tendências e ética → fechamento) + transcrição das 10 heurísticas de Nielsen e das 8 regras de Shneiderman, que não saem no texto do PDF. Contém `AS2 - Projeto UX UI MEGA-WR/` — trabalho com pasta própria por gerar muitos arquivos: `TRABALHO.md` (fonte do PDF), `Entrega/` (`YanSuyama_ProjetoUXUI.pdf`, `gerar_pdf.py` e `figuras/`), `site-prototipo-megawr/` (cópia de teste do site da MEGA-WR em Astro, com a página `/orcamento`; é o protótipo oficial do trabalho), `Prototipo/` (`telas-site/` + `gerar_telas_site.py`, que geram as figuras do PDF; `index.html`, `telas/` e `gerar_telas.py` são o protótipo avulso anterior, mantido como histórico) e `Pesquisa/` (roteiro de entrevista e questionário, em .md e .docx).

- `Design Experimental/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs (experimentos e design experimental → causalidade → variáveis → tipos de experimento → delineamentos estatísticos → passo a passo, partes 1 e 2 → fechamento) + `Design Experimental - 2.1.pdf`, infográfico da unidade 02 (concepções de pesquisa), quase todo em imagem.
- `Marketing de relacionamento/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs (conceitos e evolução → consumidor e neuromarketing → CX → customer success → jornada do cliente → CRM → cultura centrada no cliente → fechamento).
- `Web Analytics e performance digital/` — 2026/2, **cursando**. 7 PDFs (métricas e KPIs → sites e landing pages → GA4 → Google Ads → Meta Ads → experimentação e growth → relatórios e dashboards); unidade 08 a confirmar.

## Padrão de cada matéria

`INFO.md` (semestre, professor, ementa, avaliações, notas) + `Base de dados/` (todo material de consulta: slides e PDFs do professor, livros, artigos) + trabalhos, anotações e resumos **soltos na raiz da matéria**, sem subpasta.

Prefixo no nome mantém a ordem: `AS1 - <tema>.md`, `Aula 03 - <tema>.md`, `Resumo prova - <tema>.md`. Trabalho com muitos anexos pode virar pasta própria.
