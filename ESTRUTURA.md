# Estrutura de Pastas — Faculdade

Mapa objetivo. Atualizado automaticamente quando a estrutura muda.

**Organização por matéria, não por semestre.** Cada matéria é uma pasta na raiz. O semestre fica registrado no `INFO.md` da matéria e no `PAINEL.md`.

- `/` — raiz: arquivos de controle (`CLAUDE.md`, `PAINEL.md`, `ESTRUTURA.md`, `HISTORICO.md`), `README.md` (capa do repositório no GitHub) e `.gitignore` + uma pasta por matéria. Versionado em `techgoldenia-coder/Faculdade` (privado).
- `PAINEL.md` — índice de todas as matérias (semestre, status, professor), prazos em aberto, datas do semestre e notas. Primeiro arquivo a consultar.
- `0 - Institucional/` — o que vale para o curso inteiro. `Normas-ABNT.md` (formatação, citações NBR 10520, referências NBR 6023; template do professor sempre prevalece); `Grade-Curricular.md` (grade oficial e situação de cada matéria, a preencher); `BANCO-DE-REFERENCIAS.md` (toda fonte já usada em trabalho, em ABNT, com onde foi usada — transversal às matérias, por isso fica aqui).
- `1 - Modelos/` — modelos para copiar. `MODELO-INFO-Materia.md`, `MODELO-Anotacao-de-Aula.md`, `MODELO-Trabalho.md` (enunciado, critérios de correção, estrutura, checklist de entrega), `MODELO-Resumo-para-Prova.md` (mapa de conteúdo, comparações, simulado, erros). `_MODELO-MATERIA/` — pasta pronta para clonar ao abrir matéria nova.

## Matérias

- `Gestão de Anúncios em Canais Sociais/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs + transcrições das videoaulas 2 a 8. Contém `AS1 - Plano de Mídia MEGA-WR/` (.docx, planilha operacional e `Imagens/` com as peças) e `AS2 - Otimização do Plano de Mídia MEGA-WR/` — `TRABALHO.md` (enunciado, decisões, premissas e roteiro), `AS2 - Otimização do Plano de Mídia MEGA-WR (rascunho).pptx` (24 slides, o entregável) e `AS2 - Dados hipotéticos MEGA-WR.xlsx` (números com fórmulas + modelo de controle de leads). Na raiz, `Layout trabalho.docx` (template da AS1).
- `Gestão de Conteúdo em Mídias Sociais/` — 2026/2, **cursando**. Disciplina completa em 8 PDFs (presença on-line → social listening → personas e posicionamento (case Sallve) → identidade e tom de voz → influência e estratégia de conteúdo → métricas → multiplataforma → fechamento). Contém `AS2 - Planejamento de conteúdo MEGA-WR.md` — relatório individual (marca, calendário 70-20-10 de outubro/2026, métricas, community management e crise), com notas de revisão e checklist no fim do arquivo.
- `Gestão de marcas/` — 2026/1, concluída. 6 PDFs na base (inclui `Branding.pdf`, 3 MB, aparentemente material de referência e não slide de aula).
- `Marketing de conteúdo/` — 2026/1, concluída. 11 PDFs na base.
- `Processos de decisão e tipos de segmentação/` — 2026/1, concluída. 6 PDFs na base.

- `Construção de Interfaces e Experiência do Usuário/` — 2026/2, **cursando**. disciplina completa em 8 PDFs de unidade (UX/UI → usabilidade e design visual → pesquisa e personas → arquitetura da informação → prototipagem → testes de usabilidade → tendências e ética → fechamento) + transcrição das 10 heurísticas de Nielsen e das 8 regras de Shneiderman, que não saem no texto do PDF. Contém `AS2 - Projeto UX UI MEGA-WR/` — trabalho com pasta própria por gerar muitos arquivos: `TRABALHO.md` (fonte do PDF), `Entrega/` (`YanSuyama_ProjetoUXUI.pdf`, `gerar_pdf.py` e `figuras/`), `Prototipo/` (`index.html` navegável, `img/`, `telas/` e `gerar_telas.py`) e `Pesquisa/` (roteiro de entrevista e questionário, em .md e .docx).

## Padrão de cada matéria

`INFO.md` (semestre, professor, ementa, avaliações, notas) + `Base de dados/` (todo material de consulta: slides e PDFs do professor, livros, artigos) + trabalhos, anotações e resumos **soltos na raiz da matéria**, sem subpasta.

Prefixo no nome mantém a ordem: `AS1 - <tema>.md`, `Aula 03 - <tema>.md`, `Resumo prova - <tema>.md`. Trabalho com muitos anexos pode virar pasta própria.
