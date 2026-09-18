"""Gera YanSuyama_ProjetoUXUI.pdf a partir de TRABALHO.md.

Uso:  python Entrega/gerar_pdf.py
Etapas: diagramas SVG -> recortes das telas -> HTML (ABNT) -> PDF pelo Edge
-> leitura das páginas para numerar o sumário -> PDF final.

Marcadores aceitos em TRABALHO.md:
  [[QUADRO: título]]            título numerado acima da tabela seguinte
  [[FONTE: texto]]              fonte abaixo de quadro ou figura
  [[FIG: arquivo | título | fonte | largura]]
  [[GRADE: arq1 ; arq2 ; ... | leg1 ; leg2 ; ... | título | fonte | colunas | largura de cada tela | alinhar]]
                                ("alinhar" é opcional: põe as legendas na mesma linha)
  arquivo.png@y0-y1             recorta a imagem entre as alturas y0 e y1 (px)
"""
import html
import pathlib
import re
import shutil
import subprocess
import tempfile

import markdown
from PIL import Image

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
FIG = AQUI / "figuras"
TELAS = RAIZ / "Prototipo" / "telas-site"  # capturas da versão de teste do site
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SAIDA = AQUI / "YanSuyama_ProjetoUXUI.pdf"


# ---------------------------------------------------------------- diagramas
def _txt(cx, cy, linhas, cor="#111"):
    if isinstance(linhas, str):
        linhas = [linhas]
    n = len(linhas)
    y0 = cy - (n - 1) * 7.5 + 4
    out = []
    for i, t in enumerate(linhas):
        peso = "700" if i == 0 else "400"
        tam = 13 if i == 0 else 11
        fill = cor if i == 0 else "#444"
        out.append(f'<text x="{cx}" y="{y0 + i * 15}" text-anchor="middle" font-size="{tam}" font-weight="{peso}" fill="{fill}">{html.escape(t)}</text>')
    return "".join(out)


def caixa(cx, cy, w, h, linhas, tipo="normal"):
    estilos = {
        "normal": 'fill="#fff" stroke="#6B7280" stroke-width="1.5"',
        "novo": 'fill="#FFF5F5" stroke="#CC1F24" stroke-width="2"',
        "externo": 'fill="#EEF2FB" stroke="#1F3F9C" stroke-width="1.5" stroke-dasharray="5 4"',
        "nota": 'fill="#F9FAFB" stroke="#9CA3AF" stroke-width="1.2" stroke-dasharray="4 3"',
    }
    return f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="7" {estilos[tipo]}/>' + _txt(cx, cy, linhas)


def losango(cx, cy, w, h, linhas):
    pts = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
    return f'<polygon points="{pts}" fill="#FFFBEB" stroke="#B45309" stroke-width="1.5"/>' + _txt(cx, cy, linhas)


def elipse(cx, cy, w, h, linhas):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{w / 2}" ry="{h / 2}" fill="#16181D"/>' + _txt(cx, cy, linhas, "#fff").replace('fill="#444"', 'fill="#D1D5DB"')


def seta(pontos, rotulo=None, pos=None, tracejada=False, ponta=True):
    d = " ".join(f"{x},{y}" for x, y in pontos)
    extra = ' stroke-dasharray="5 4"' if tracejada else ""
    marca = ' marker-end="url(#seta)"' if ponta else ""
    s = f'<polyline points="{d}" fill="none" stroke="#374151" stroke-width="1.5"{extra}{marca}/>'
    if rotulo:
        x, y = pos
        s += f'<text x="{x}" y="{y}" font-size="11" font-weight="700" fill="#374151" text-anchor="middle">{html.escape(rotulo)}</text>'
    return s


def svg(w, h, corpo):
    defs = ('<defs><marker id="seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#374151"/></marker></defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="Arial, Helvetica, sans-serif">{defs}<rect width="{w}" height="{h}" fill="#fff"/>{corpo}</svg>')


def sitemap():
    c = []
    c.append(caixa(380, 34, 220, 48, ["Página inicial", "megawr.com.br"]))
    c.append(seta([(380, 58), (380, 80), (180, 80), (180, 100)], ponta=False))
    c.append(seta([(380, 80), (580, 80), (580, 100)], ponta=False))
    c.append(caixa(180, 120, 300, 40, ["Seções da página inicial", "acesso por âncora"]))
    c.append(caixa(580, 120, 300, 40, ["Orçamento guiado · /orcamento", "novo"], "novo"))
    esq = [("Linhas: Saúde · Uniformes · Fitness", "normal"), ("Personalização: bordado · silk · DTF", "normal"),
           ("Clientes", "normal"), ("Como trabalhamos", "normal"), ("Dúvidas frequentes", "novo"), ("Sobre e contato", "normal")]
    dir_ = [("1. Produto", "novo"), ("2. Quantidade e tamanhos", "novo"), ("3. Personalização", "novo"),
            ("4. Entrega e contato", "novo"), ("Resumo e envio", "novo"), ("WhatsApp ou e-mail", "externo")]
    ys = [177 + i * 44 for i in range(6)]
    c.append(seta([(45, 140), (45, ys[-1])], ponta=False))
    c.append(seta([(445, 140), (445, ys[-1])], ponta=False))
    for y, (t, tipo) in zip(ys, esq):
        c.append(seta([(45, y), (60, y)], ponta=False))
        c.append(caixa(195, y, 270, 34, [t], tipo))
    for i, (y, (t, tipo)) in enumerate(zip(ys, dir_)):
        c.append(seta([(445, y), (460, y)], ponta=False))
        c.append(caixa(545, y, 170, 34, [t], tipo))
        if i < 5:
            c.append(seta([(545, y + 17), (545, y + 27)]))
    c.append(caixa(700, ys[1], 104, 48, ["Pedido em", "grupo /g/código"], "novo"))
    c.append(seta([(630, ys[1]), (647, ys[1])]))
    c.append(seta([(330, ys[0]), (458, ys[0])], tracejada=True))
    c.append('<text x="392" y="158" font-size="10" text-anchor="middle" fill="#374151">atalho: linha</text>'
             '<text x="392" y="170" font-size="10" text-anchor="middle" fill="#374151">pré-selecionada</text>')
    ly = 448
    c.append(f'<rect x="60" y="{ly}" width="28" height="16" rx="3" fill="#fff" stroke="#6B7280" stroke-width="1.5"/>'
             f'<text x="96" y="{ly + 12}" font-size="11" fill="#111">existente</text>'
             f'<rect x="190" y="{ly}" width="28" height="16" rx="3" fill="#FFF5F5" stroke="#CC1F24" stroke-width="2"/>'
             f'<text x="226" y="{ly + 12}" font-size="11" fill="#111">novo na proposta</text>'
             f'<rect x="360" y="{ly}" width="28" height="16" rx="3" fill="#EEF2FB" stroke="#1F3F9C" stroke-width="1.5" stroke-dasharray="5 4"/>'
             f'<text x="396" y="{ly + 12}" font-size="11" fill="#111">destino externo</text>'
             f'<line x1="520" y1="{ly + 8}" x2="555" y2="{ly + 8}" stroke="#374151" stroke-width="1.5" stroke-dasharray="5 4"/>'
             f'<text x="563" y="{ly + 12}" font-size="11" fill="#111">atalho</text>')
    return svg(760, 475, "".join(c))


def fluxo():
    CX, RX, LX = 330, 590, 100
    c = []
    c.append(elipse(CX, 32, 250, 46, ["Início", "acessa o site pelo celular"]))
    c.append(seta([(CX, 55), (CX, 80)]))
    c.append(caixa(CX, 102, 250, 42, ["Página inicial", "mínimo, prazo e dúvidas frequentes"]))
    c.append(seta([(CX, 123), (CX, 149)]))
    c.append(losango(CX, 185, 230, 70, ["Entrou pelo card", "de uma linha?"]))
    c.append(seta([(CX + 115, 185), (RX - 102, 185)], "Sim", ((CX + 115 + RX - 100) / 2, 178)))
    c.append(caixa(RX, 185, 200, 42, ["Linha já vem", "pré-selecionada"]))
    c.append(seta([(RX, 206), (RX, 268), (CX + 127, 268)]))
    c.append(seta([(CX, 220), (CX, 246)], "Não", (CX + 22, 238)))
    c.append(caixa(CX, 268, 250, 42, ["Passo 1 · Produto"], "novo"))
    c.append(seta([(CX, 289), (CX, 316)]))
    c.append(caixa(CX, 338, 250, 42, ["Passo 2 · Quantidade e tamanhos"], "novo"))
    c.append(seta([(CX + 125, 338), (RX - 100, 338)], tracejada=True, ponta=False))
    c.append(caixa(RX, 338, 200, 42, ["Sem os tamanhos?", "total, planilha e salvo"], "nota"))
    c.append(seta([(CX, 359), (CX, 389)]))
    c.append(losango(CX, 425, 230, 70, ["Total ≥ 10 peças?"]))
    c.append(seta([(CX + 115, 425), (RX - 102, 425)], "Não", ((CX + 115 + RX - 100) / 2, 418)))
    c.append(caixa(RX, 425, 200, 42, ["Aviso com opções", "grupo · aumentar · seguir"]))
    c.append(seta([(RX, 446), (RX, 488)], "grupo", (RX + 24, 472)))
    c.append(caixa(RX, 510, 200, 42, ["Pedido em grupo", "ao somar 10 peças, segue"], "novo"))
    c.append(seta([(RX - 100, 510), (CX + 127, 510)]))
    c.append(seta([(CX, 460), (CX, 488)], "Sim", (CX + 22, 478)))
    c.append(caixa(CX, 510, 250, 42, ["Passo 3 · Personalização"], "novo"))
    c.append(seta([(CX, 531), (CX, 558)]))
    c.append(caixa(CX, 580, 250, 42, ["Passo 4 · Entrega e contato"], "novo"))
    c.append(seta([(CX + 125, 580), (RX - 100, 580)], tracejada=True, ponta=False))
    c.append(caixa(RX, 580, 200, 42, ["Compra pela empresa?", "CNPJ, nota e pagamento"], "nota"))
    c.append(seta([(CX, 601), (CX, 629)]))
    c.append(losango(CX, 665, 230, 70, ["Nome, WhatsApp e", "cidade preenchidos?"]))
    c.append(seta([(CX - 115, 665), (LX + 72, 665)], "Não", ((CX - 115 + LX + 70) / 2, 658)))
    c.append(caixa(LX, 665, 140, 42, ["Erro indicado", "no próprio campo"]))
    c.append(seta([(LX, 644), (LX, 580), (CX - 127, 580)]))
    c.append(seta([(CX, 700), (CX, 728)], "Sim", (CX + 22, 718)))
    c.append(caixa(CX, 750, 250, 42, ["Resumo", "revisa pedido e mensagem"], "novo"))
    c.append(seta([(CX, 771), (CX, 799)]))
    c.append(losango(CX, 835, 230, 70, ["Precisa corrigir?"]))
    c.append(seta([(CX - 115, 835), (LX + 72, 835)], "Sim", ((CX - 115 + LX + 70) / 2, 828)))
    c.append(caixa(LX, 835, 140, 42, ["Editar a etapa"]))
    c.append(seta([(LX - 70, 835), (14, 835), (14, 268), (CX - 127, 268)], tracejada=True))
    c.append('<text x="26" y="560" font-size="10" fill="#374151" transform="rotate(-90 26 560)" text-anchor="middle">volta à etapa escolhida</text>')
    c.append(seta([(CX, 870), (CX, 894)], "Não", (CX + 22, 886)))
    c.append(caixa(CX, 918, 250, 46, ["WhatsApp ou e-mail recebe", "o pedido estruturado"], "externo"))
    c.append(seta([(CX, 941), (CX, 962)]))
    c.append(elipse(CX, 986, 290, 46, ["Fim", "MEGA-WR responde com o orçamento"]))
    return svg(720, 1015, "".join(c))


def preparar_figuras():
    FIG.mkdir(exist_ok=True)
    (FIG / "sitemap.svg").write_text(sitemap(), encoding="utf-8")
    (FIG / "fluxo.svg").write_text(fluxo(), encoding="utf-8")


# ---------------------------------------------------------------- markdown -> html
def caminho(nome):
    """Localiza a imagem; "arquivo.png@y0-y1" gera um recorte entre as alturas y0 e y1 (px)."""
    if "@" in nome:
        base, faixa = nome.split("@")
        y0, y1 = (int(v) for v in faixa.split("-"))
        destino = FIG / f"{pathlib.Path(base).stem}_{y0}-{y1}.png"
        im = Image.open(caminho(base))
        im.crop((0, y0, im.width, min(y1, im.height))).save(destino, optimize=True)
        return destino
    for pasta in (FIG, TELAS):
        if (pasta / nome).exists():
            return pasta / nome
    raise FileNotFoundError(nome)


def achar(nome):
    return caminho(nome).as_uri()


def converter(md_texto):
    cont = {"fig": 0, "quadro": 0}
    md_texto = re.sub(r"^---\n.*?\n---\n", "", md_texto, flags=re.S)
    md_texto = re.sub(r"<!--.*?-->", "", md_texto, flags=re.S)

    def fig(m):
        arq, titulo, fonte, larg = [p.strip() for p in m.group(2).split("|")]
        cont["fig"] += 1
        return (f'\n<figure class="fig"><figcaption><b>Figura {cont["fig"]}</b> – {html.escape(titulo)}</figcaption>'
                f'<img src="{achar(arq)}" style="width:{larg}"><p class="fonte">Fonte: {fonte}</p></figure>\n')

    def grade(m):
        arqs, legs, titulo, fonte, cols, larg, *opc = [p.strip() for p in m.group(2).split("|")]
        cont["fig"] += 1
        itens = ""
        for letra, a, l in zip("abcdefghij", arqs.split(";"), legs.split(";")):
            itens += (f'<div><img src="{achar(a.strip())}" style="width:{larg}">'
                      f'<p class="sub">({letra}) {html.escape(l.strip())}</p></div>')
        # "alinhar": legendas na mesma linha, para telas de alturas parecidas
        classe = "fig grade alinhada" if "alinhar" in opc else "fig grade"
        return (f'\n<figure class="{classe}"><figcaption><b>Figura {cont["fig"]}</b> – {html.escape(titulo)}</figcaption>'
                f'<div class="itens" style="grid-template-columns:repeat({cols},{larg})">{itens}</div>'
                f'<p class="fonte">Fonte: {fonte}</p></figure>\n')

    def quadro(m):
        cont["quadro"] += 1
        return f'\n<p class="quadro-titulo"><b>Quadro {cont["quadro"]}</b> – {html.escape(m.group(1).strip())}</p>\n'

    # figuras simples e pares numeradas juntas, na ordem em que aparecem no texto
    md_texto = re.sub(r"\[\[(FIG|GRADE):(.+?)\]\]", lambda m: (fig if m.group(1) == "FIG" else grade)(m), md_texto)
    md_texto = re.sub(r"\[\[QUADRO:(.+?)\]\]", quadro, md_texto)
    md_texto = re.sub(r"\[\[FONTE:(.+?)\]\]", lambda m: f'\n<p class="fonte">Fonte: {m.group(1).strip()}</p>\n', md_texto)
    corpo = markdown.markdown(md_texto, extensions=["extra", "sane_lists"])
    # tabelas: marca como quadro
    corpo = corpo.replace("<table>", '<table class="quadro">')
    # títulos sem número (Referências, Apêndices) ficam centralizados
    corpo = re.sub(r"<h1>((?:Referências|Apêndice)[^<]*)</h1>", r'<h1 class="sem-num">\1</h1>', corpo)
    corpo = corpo.replace('<h1 class="sem-num">Referências', '<h1 class="sem-num ref-titulo">Referências')
    # referências: alinhadas à esquerda, sem recuo (NBR 6023)
    corpo = re.sub(r'(<h1 class="sem-num ref-titulo">Referências</h1>)(.*?)(?=<h1)',
                   lambda m: m.group(1) + '<div class="ref">' + m.group(2) + '</div>', corpo, flags=re.S)
    corpo = corpo.replace('<h1 class="sem-num">Apêndice B', '<h1 class="sem-num segue">Apêndice B')
    corpo = re.sub(r'(<h1 class="sem-num">Apêndice A[^<]*</h1>)(.*?)(?=<h1)',
                   lambda m: m.group(1) + '<div class="colunas">' + m.group(2) + '</div>', corpo, flags=re.S)
    # apêndices em espaçamento simples, como material de apoio
    k = corpo.find('<h1 class="sem-num">Apêndice')
    if k >= 0:
        corpo = corpo[:k] + '<div class="apendice">' + corpo[k:] + '</div>'
    # ids para o sumário
    n = [0]

    def ident(m):
        n[0] += 1
        return f'<{m.group(1)} id="s{n[0]}"{m.group(2)}>'
    corpo = re.sub(r"<(h[12])((?: class=\"[^\"]*\")?)>", ident, corpo)
    return corpo


def titulos(corpo):
    return [(nivel, sid, html.unescape(re.sub(r"<[^>]+>", "", t)))
            for nivel, sid, t in re.findall(r'<h([12]) id="(s\d+)"[^>]*>(.*?)</h[12]>', corpo)]


CSS = """
@page { size: A4; margin: 3cm 2cm 2cm 3cm;
  @top-right { content: counter(page); font-family: Arial, sans-serif; font-size: 10pt; } }
@page pre { @top-right { content: none; } }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 12pt; line-height: 1.5; color: #000; margin: 0; }
.capa, .sumario { page: pre; }
.capa { height: 24.6cm; display: flex; flex-direction: column; justify-content: space-between; text-align: center;
  text-transform: uppercase; font-weight: bold; break-after: page; }
.capa .meio { font-size: 14pt; }
.capa .meio span { display: block; text-transform: none; font-weight: normal; font-size: 12pt; margin-top: 8pt; }
.sumario { break-after: page; }
.sumario h1 { text-align: center; }
.toc { list-style: none; padding: 0; margin: 0; }
.toc li { display: flex; align-items: baseline; gap: 6px; line-height: 1.2; }
.toc li .t { white-space: nowrap; overflow: hidden; }
.toc li .dots { flex: 1; border-bottom: 1px dotted #000; transform: translateY(-4px); }
.toc li.n1 { font-weight: bold; text-transform: uppercase; }
.toc li.n2 { padding-left: 0; }
.conteudo p { text-align: justify; text-indent: 1.25cm; margin: 0 0 6pt; orphans: 3; widows: 3; }
.conteudo li p, .conteudo td p, .conteudo blockquote p { text-indent: 0; }
h1 { font-size: 12pt; font-weight: bold; text-transform: uppercase; margin: 24pt 0 12pt; break-after: avoid; }
h1.sem-num { text-align: center; break-before: page; margin-top: 0; }
h1.sem-num.ref-titulo { break-before: auto; margin-top: 24pt; }
h1.sem-num.segue { break-before: auto; margin-top: 18pt; }
h3 { font-size: 11pt; font-weight: bold; margin: 12pt 0 4pt; break-after: avoid; }
h2 { font-size: 12pt; font-weight: bold; margin: 18pt 0 6pt; break-after: avoid; }
ul, ol { margin: 0 0 8pt; padding-left: 1.25cm; text-align: justify; }
li { margin-bottom: 3pt; }
blockquote { margin: 8pt 0 10pt 1.25cm; padding: 2pt 0 2pt 10pt; border-left: 3px solid #888; font-size: 11pt; line-height: 1.4; }
code { font-family: Consolas, monospace; font-size: 10.5pt; background: #f1f1f1; padding: 0 3px; }
table.quadro { width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.15; margin: 0 0 2pt; break-inside: auto; }
table.quadro th, table.quadro td { border: 1px solid #000; padding: 3pt 4pt; text-align: left; vertical-align: top; }
table.quadro th { background: #EDEDED; }
table.quadro tr { break-inside: avoid; }
.quadro-titulo { text-indent: 0 !important; font-size: 10pt; margin: 12pt 0 3pt !important; text-align: left !important; break-after: avoid; }
.fonte { text-indent: 0 !important; font-size: 10pt; margin: 2pt 0 12pt !important; text-align: left !important; }
.fig { margin: 12pt 0; text-align: center; break-inside: avoid; }
.fig figcaption { font-size: 10pt; text-align: left; margin-bottom: 4pt; }
.fig img { max-width: 100%; border: 1px solid #ccc; }
.fig img[src$=".svg"] { border: 0; }
.fig .fonte { text-align: left !important; }
.grade .itens { display: grid; gap: 6pt 0.35cm; justify-content: center; align-items: start; }
.grade img { display: block; }
.grade.alinhada .itens { align-items: stretch; }
.grade.alinhada .itens > div { display: flex; flex-direction: column; justify-content: space-between; }
.grade .sub { text-indent: 0 !important; font-size: 10pt; text-align: center !important; margin: 3pt 0 0 !important; line-height: 1.25; }
.ref p { text-align: left !important; text-indent: 0 !important; line-height: 1.15; margin: 0 0 12pt !important; }
.apendice p, .apendice li { font-size: 10pt; line-height: 1.2; }
.apendice .colunas { column-count: 2; column-gap: 0.8cm; }
.apendice .colunas p { break-after: avoid; }
.apendice p { margin-bottom: 4pt !important; }
.apendice ol { margin-bottom: 4pt; }
.apendice li { margin-bottom: 1pt; }
"""


def montar_html(meta, corpo, paginas=None):
    itens = []
    for nivel, sid, t in titulos(corpo):
        pg = (paginas or {}).get(sid, "")
        itens.append(f'<li class="n{nivel}"><span class="t">{html.escape(t)}</span><span class="dots"></span><span>{pg}</span></li>')
    capa = f"""<section class="capa">
      <div>{meta['instituicao']}<br>{meta['curso']}</div>
      <div>{meta['aluno']}</div>
      <div class="meio">{meta['titulo']}<span>{meta['subtitulo']}</span>
        <span style="margin-top:28pt">Projeto de UX/UI apresentado à disciplina {meta['disciplina']}.</span>
        <span>Professor: {meta['professor']}</span></div>
      <div>{meta['cidade']}<br>{meta['ano']}</div></section>"""
    sumario = f'<section class="sumario"><h1 style="break-before:auto">Sumário</h1><ul class="toc">{"".join(itens)}</ul></section>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{meta['titulo']}</title>
      <style>{CSS}</style></head><body>{capa}{sumario}<main class="conteudo">{corpo}</main></body></html>"""


def imprimir(html_texto, pdf):
    tmp = AQUI / "_tmp_trabalho.html"
    tmp.write_text(html_texto, encoding="utf-8")
    perfil = pathlib.Path(tempfile.gettempdir()) / "edge-pdf-prof"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={perfil}",
                    "--virtual-time-budget=8000", "--allow-file-access-from-files", f"--print-to-pdf={pdf}", tmp.as_uri()],
                   capture_output=True, timeout=180)
    tmp.unlink()


def paginas_dos_titulos(pdf, corpo):
    texto = subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", str(pdf), "-"], capture_output=True).stdout.decode("utf-8")
    pags = texto.split("\f")
    norm = lambda s: re.sub(r"\s+", " ", s).strip().upper()
    lista = titulos(corpo)
    # o sumário repete os títulos: começa a busca depois da página que traz o último item dele
    ultimo = norm(lista[-1][2])[:28]
    inicio = next(i for i, p in enumerate(pags) if any(norm(l).startswith(ultimo) for l in p.splitlines())) + 1
    res = {}
    for nivel, sid, t in lista:
        alvo = norm(t)[:28]
        for i in range(inicio, len(pags)):
            linhas = [norm(l) for l in pags[i].splitlines()]
            if any(l.startswith(alvo) for l in linhas):
                res[sid] = i + 1
                inicio = i
                break
    return res


def main():
    preparar_figuras()
    md_texto = (RAIZ / "TRABALHO.md").read_text(encoding="utf-8")
    meta = dict(re.findall(r"^(\w+): (.+)$", re.search(r"^---\n(.*?)\n---", md_texto, re.S).group(1), re.M))
    corpo = converter(md_texto)
    rascunho = AQUI / "_rascunho.pdf"
    imprimir(montar_html(meta, corpo), rascunho)
    paginas = paginas_dos_titulos(rascunho, corpo)
    rascunho.unlink()
    imprimir(montar_html(meta, corpo, paginas), SAIDA)
    faltando = [t for _, sid, t in titulos(corpo) if sid not in paginas]
    print("PDF:", SAIDA)
    print("títulos sem página no sumário:", faltando or "nenhum")


if __name__ == "__main__":
    main()
