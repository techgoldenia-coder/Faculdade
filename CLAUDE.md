# CLAUDE.md — Faculdade

## Sobre mim

- **Nome:** Yan Suyama
- **Curso:** Bacharelado em Marketing — PUC-PR
- **Trabalho:** Analista de marketing na Drip-Plan; objetivo de atuar como consultor de marketing.
- **Outro workspace:** `Desktop/0-Claude` — consultoria, clientes e estudos (método La Torre). Esta pasta aqui é **só faculdade**.
- **Sistema:** Windows 11 — shell PowerShell.
- **Repositório:** esta pasta é versionada em `techgoldenia-coder/Faculdade` (GitHub, **privado**).

## Para que serve esta pasta

Guardar o conteúdo das matérias e me apoiar em dois modos:

1. **Estudar** — resumir aula, explicar conceito, montar simulado e material de prova.
2. **Produzir trabalhos** — interpretar enunciado, estruturar, pesquisar, redigir e revisar em ABNT.

## Estrutura

**Organização por matéria, não por semestre.** Cada matéria é uma pasta na raiz, com o nome dela. O semestre é registrado dentro do `INFO.md` e no `PAINEL.md`, não na hierarquia de pastas.

- `PAINEL.md` — índice de todas as matérias, prazos em aberto e notas. **Primeiro arquivo a consultar.**
- `0 - Institucional/` — o que vale para o curso inteiro: normas ABNT, grade curricular, banco de referências.
- `1 - Modelos/` — modelos para copiar, incluindo `_MODELO-MATERIA/` para abrir matéria nova.
- `<Nome da matéria>/` — uma pasta por matéria.

Dentro de cada matéria:

- `INFO.md` — semestre, professor, ementa, avaliações, notas.
- `Base de dados/` — tudo que é material de consulta: slides e PDFs do professor, livros, artigos, links salvos.
- **Os trabalhos, anotações e resumos ficam soltos na raiz da matéria**, sem subpasta.

## Nome dos arquivos soltos na matéria

Como ficam todos no mesmo nível, o prefixo é o que mantém tudo ordenado e localizável:

- Trabalho: `AS1 - <tema>.md`
- Anotação de aula: `Aula 03 - <tema>.md`
- Resumo de prova: `Resumo prova - <tema>.md`

Trabalho que gere muitos arquivos (anexos, planilhas, versões) pode ganhar pasta própria: `AS1 - <tema>/`.

## Como me ajudar

### Sempre

- Responder em **português**, direto ao ponto, sem enrolação.
- Antes de falar de uma matéria, **ler o `INFO.md` dela e o material em `Base de dados/`**. Não responder de memória genérica sobre marketing quando existe material do professor.
- Dizer de onde veio cada informação: `Gestão de marcas 3.pdf` ou autor/obra. Se for conhecimento externo ao material da aula, deixar isso explícito.
- Nunca inventar autor, ano, página ou dado de mercado. Sem fonte confirmada, marcar `[VERIFICAR]`.

### Nos trabalhos

- Começar pelo enunciado: o que é pedido, critérios de correção, formato e prazo. Se o enunciado não estiver na pasta, pedir antes de escrever.
- Apresentar a **estrutura proposta antes** do texto corrido, para eu aprovar.
- Escrever no meu tom: objetivo e concreto, sem palavra difícil só para impressionar.
- **Usar meus casos reais quando couber** — Drip-Plan, MEGA-WR e o que estiver em `0-Claude/Clientes/`. É o que diferencia meu trabalho de um genérico.
- Seguir `0 - Institucional/Normas-ABNT.md`. Toda fonte usada entra também em `0 - Institucional/BANCO-DE-REFERENCIAS.md`.
- Entregar rascunho para eu revisar e ajustar — o texto final é meu, não é para colar sem leitura.

### Nos estudos

- Ao resumir uma aula, salvar na raiz da matéria como `Aula NN - <tema>.md`, no formato de `1 - Modelos/MODELO-Anotacao-de-Aula.md`.
- Preferir explicação com exemplo de marca real a definição de dicionário.
- Em revisão para prova: gerar as questões primeiro; o gabarito comentado só depois que eu responder.

## Regras do projeto

- **Lembrar de commits em checkpoints:** o repositório é privado no GitHub (`techgoldenia-coder/Faculdade`), para acesso em casa e no trabalho. Sempre que fecharmos um passo importante — matéria nova, trabalho entregue, nota lançada — me lembrar de commitar e sugerir a mensagem.
- **O repositório não pode virar público.** Contém material didático da PUC-PR protegido por direito autoral e dados reais de cliente usados nos trabalhos.

- **Resumo antes de salvar conteúdo:** antes de gravar anotação, resumo ou trabalho, mostrar um resumo curto do que vai entrar e esperar meu ok. Não vale para `ESTRUTURA.md` e `HISTORICO.md`.
- **Manter `PAINEL.md`, `ESTRUTURA.md` e `HISTORICO.md` atualizados** automaticamente, sem eu pedir, sempre que a estrutura mudar ou fecharmos um passo importante. Curtos: uma linha por item.
- **Matéria nova:** copiar `1 - Modelos/_MODELO-MATERIA/` para a raiz, renomear com o nome da matéria, preencher o `INFO.md` e adicionar a linha no `PAINEL.md`.
- **Não apagar material de aula.** Matéria concluída continua na raiz; só o status no `INFO.md` e no `PAINEL.md` muda.
