# Versão de teste do site da MEGA-WR — AS2 PUCPR

Cópia do site oficial (`0-Claude/Clientes/MEGA WR/Site`) usada como protótipo do projeto de UX/UI
"Repensando a solicitação de orçamento da MEGA-WR". **Não é o site oficial** e não publica nele:
o oficial está no Cloudflare; esta cópia vai para um projeto separado na Vercel.

## O que muda em relação ao site oficial

- Página nova `/orcamento`: orçamento guiado em 4 passos, resumo, confirmação e pedido em grupo.
  Nada é enviado ao WhatsApp real; a tela final só mostra a mensagem.
- Revisão após as entrevistas: compra pela empresa (CNPJ, nota, pagamento), envio por e-mail e PDF,
  planilha de tamanhos, salvamento automático (localStorage), indicação de técnica em primeiro,
  posição opcional, atalho para o WhatsApp e "ver tecido antes de fechar".
- "Montar meu orçamento" no topo, no hero e no fechamento; condições (mínimo, prazo, sem cadastro)
  abaixo do botão; "Orçar linha" nos cards; seção de dúvidas frequentes.
- Proteções: `noindex`, `robots.txt` com `Disallow: /`, sem sitemap, faixa "Protótipo acadêmico" no topo.

## Parâmetros de endereço

| Parâmetro | Efeito |
|---|---|
| `?v=1` | Versão apresentada nas conversas com os participantes (17/09/2026) |
| `?linha=saude` (ou `uniformes`, `fitness`) | Começa o orçamento com a linha escolhida |
| `?p=p2-baixo` (e outros) | Abre um estado pronto — usado para gerar as figuras do PDF |
| `?shot` | Modo de captura (hero com altura fixa, sem rodapé e sem a faixa de protótipo) |

## Comandos

```sh
npm ci
npm run dev                       # http://localhost:4321
npm run build                     # gera dist/
npx vercel build --prod           # gera .vercel/output (exige vercel login)
```

**Publicar:** não rode `vercel deploy` direto desta pasta. Ela fica dentro do repositório da faculdade, e a
Vercel bloqueia a publicação porque o e-mail do commit não bate com uma conta do GitHub. Copie
`.vercel/project.json` e `.vercel/output/` para uma pasta fora do git e, nela, rode
`npx vercel deploy --prebuilt --prod`. O destino continua sendo o projeto `site-prototipo-megawr`.

Depois de mudar a interface: `python ../Prototipo/gerar_telas_site.py` e `python ../Entrega/gerar_pdf.py`.
