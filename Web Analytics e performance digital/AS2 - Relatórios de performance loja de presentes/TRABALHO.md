# AS2 — Relatórios de performance digital: loja de presentes personalizados — Web Analytics e Performance Digital

- **Prazo:** `[PREENCHER]`
- **Peso na nota:** `[PREENCHER]`
- **Formato exigido:** dois relatórios em slides ou PDF — estratégico (até 3 páginas) e operacional (até 8 páginas). Entregue em **2 PDFs**, um por relatório (sem capa, dentro do limite). Também existe a versão unificada com capa.
- **Número da atividade:** a pasta diz AS2, mas o enunciado não diz `[VERIFICAR]`; por isso o PDF não traz "Atividade Somativa".
- **Individual:** Yan Suyama

## Arquivos

| Arquivo | O que é |
|---|---|
| `YanSuyama_WebAnalytics_RelatorioEstrategico.pdf` | **Entrega 1** — relatório estratégico, 3 páginas. |
| `YanSuyama_WebAnalytics_RelatorioOperacional.pdf` | **Entrega 2** — relatório operacional, 8 páginas. |
| `YanSuyama_WebAnalytics_Relatorios.pdf` | Versão unificada (não é a entrega) — 12 páginas: capa + relatório estratégico (3, numerado 1/3 a 3/3) + relatório operacional (8, numerado 1/8 a 8/8). |
| `Relatórios de performance - Web Analytics.pptx` | Versão editável, com gráficos nativos. |
| `Planilha web analytics.xlsx` | Dados recebidos com o enunciado (movida de Downloads). |
| `separar_pdfs.py` | Corta o PDF unificado nos dois PDFs de entrega (páginas 2–4 e 5–12). |
| `gerar_relatorios.py` | Lê a planilha, calcula os indicadores, confere os valores-chave e monta o .pptx (capa + os dois relatórios). |

Para regerar: `python -P gerar_relatorios.py "Planilha web analytics.xlsx" .` e exportar o .pptx para PDF pelo PowerPoint (**Arquivo → Exportar → Criar PDF/XPS**), com o mesmo nome do PDF unificado; depois `python -P separar_pdfs.py YanSuyama_WebAnalytics_Relatorios.pdf`. Se editar direto no PowerPoint, o script sobrescreve as edições.

## O que o enunciado pede

Empresa de presentes personalizados, só venda on-line, com queda na conversão. Consultor de performance digital avalia os últimos 30 dias, identifica problemas e oportunidades no site e nas campanhas e propõe otimizações e testes. Premissas: leads = cadastros ou primeira etapa do formulário sem compra; ticket médio R$ 450; CAC específico de mídia paga até 28% do faturamento.

| Item do enunciado | Onde está |
|---|---|
| Estratégico: KPIs mais importantes | Estratégico, p. 1 (PDF p. 2) (5 indicadores + tabela de CAC por canal) |
| Estratégico: insights sobre o desempenho | Estratégico, p. 2 (funil do checkout + 4 insights) |
| Estratégico: soluções estratégicas | Estratégico, p. 3 (3 frentes, impacto e metas de 60 dias) |
| Operacional: KPIs de todas as frentes | Operacional, p. 1 (PDF p. 5) (negócio, site, Google, Meta + CAC por campanha) |
| Operacional: análise e otimizações do site | Operacional, p. 2 (origem), 3 (funil e checkout), 4 (perfil) |
| Operacional: análise e otimizações do Google Ads | Operacional, p. 5 |
| Operacional: análise e otimizações do Meta Ads | Operacional, p. 6 |
| Operacional: 2 testes A/B (site e mídia paga) | Operacional, p. 7 |
| Operacional: próximos passos | Operacional, p. 8 (verba, cronograma de 8 semanas, metas) |

## Decisões

- **CAC de 28%:** lido como investimento em mídia ÷ faturamento das vendas atribuídas à mídia paga (un. 01: CAC em % = investimento ÷ faturamento). Equivale a até R$ 126 por venda. Sobre o faturamento total daria 13,6%, mas 58% das vendas vêm de orgânico e direto, sem custo de mídia; isso está explicado no estratégico, p. 1.
- **Estrutura dos relatórios** segue a un. 07: introdução (objetivo e período), métricas, insights e recomendações. O estratégico foca em resultado e recomendação, sem citações acadêmicas; o operacional detalha métricas e cita as unidades.
- **Testes A/B:** site = calculadora de frete e prazo na página do produto (35% saem depois de ver o frete); mídia = segmentação no Meta (público atual × mulheres de 25 a 44 anos com interesse em moda e beleza, viagens e entretenimento). Uma variável por teste (un. 06).
- **Cenário de verba:** mantém R$ 40 mil. Premissa conservadora: a verba nova rende no máximo o limite (R$ 126 por venda); o que já existe mantém o CAC atual. **É estimativa, não previsão.**
- **Sem dado de mercado externo.** Pix, parcelamento e checkout sem cadastro são recomendações de prática, não números.

## Números-chave (calculados pelo script a partir da planilha)

| Indicador | Valor |
|---|---|
| Faturamento | R$ 294.750 (655 vendas × R$ 450) |
| Conversão do site | 1,72% (655 ÷ 38.000) |
| Conclusão do checkout | 13,7% (655 ÷ 4.785); pagamento → compra 28,1% (655 ÷ 2.334) |
| Mídia paga | R$ 40.000; 250 vendas; CAC R$ 160 = 35,6% do ticket; ROAS 2,81 |
| Google Ads | CAC R$ 111 (24,7%); Search R$ 125 (27,8%); PMax R$ 83 (18,5%) |
| Meta Ads | CAC R$ 286 (63,5%); Camp. 1 R$ 1.600; Conjunto 1 R$ 111; Conjunto 2 R$ 500 |
| Cenário proposto | ≈ 329 vendas pagas, CAC R$ 122 (27,0%) |

## Inconsistências da planilha (apontadas nos relatórios, não corrigidas)

- O GA4 atribui 15.000 usuários e 300 leads ao Meta; a plataforma registra 2.800 cliques e 100 leads.
- A Search registra 110 conversões para 120 vendas.
- A jornada chama de "Comprar" uma etapa com 3.350 usuários, mas as vendas são 655. O checkout indica 85% na última etapa, mas 655 ÷ 2.334 = 28%.
- Os conjuntos da Campanha 2 do Meta somam 30 conversões; a campanha registra 35.
- O gênero dos compradores soma 90%.
- O CTR da planilha é calculado sobre o alcance, não sobre impressões.

## Fontes

Unidades 01 a 07 da matéria, citadas como `(PUCPR, [2024]a–g)`. O PDF não traz data; o ano vem do crédito "Fonte: Autora, 2024" e dos acessos de 2024 citados nas unidades.
