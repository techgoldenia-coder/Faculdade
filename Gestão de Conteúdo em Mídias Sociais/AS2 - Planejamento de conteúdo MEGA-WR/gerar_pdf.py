"""Gera YanSuyama_AS2_GestaoConteudo.pdf a partir de TRABALHO.md.

Uso:  python gerar_pdf.py
Etapas: Markdown -> HTML (ABNT) -> PDF pelo Edge -> leitura das páginas para numerar o sumário
-> PDF final. A capa é impressa à parte e não entra na contagem; a numeração começa na folha
de rosto e aparece a partir da Introdução (NBR 14724).

Marcadores no TRABALHO.md: [[QUADRO:título]] e [[TABELA:título]] antes do elemento; [[FONTE:texto]] depois.
"""
import html
import pathlib
import re
import subprocess
import tempfile

import markdown
from pypdf import PdfReader, PdfWriter

AQUI = pathlib.Path(__file__).resolve().parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SAIDA = AQUI / "YanSuyama_AS2_GestaoConteudo.pdf"


# ---------------------------------------------------------------- markdown -> html
def converter(md_texto):
    cont = {"quadro": 0, "tabela": 0}
    md_texto = re.sub(r"^---\n.*?\n---\n", "", md_texto, flags=re.S)
    md_texto = re.sub(r"<!--.*?-->", "", md_texto, flags=re.S)

    def legenda(tipo, nome):
        def sub(m):
            cont[tipo] += 1
            return f'\n<p class="legenda {tipo}"><b>{nome} {cont[tipo]}</b> – {html.escape(m.group(1).strip())}</p>\n'
        return sub

    md_texto = re.sub(r"\[\[QUADRO:(.+?)\]\]", legenda("quadro", "Quadro"), md_texto)
    md_texto = re.sub(r"\[\[TABELA:(.+?)\]\]", legenda("tabela", "Tabela"), md_texto)
    md_texto = re.sub(r"\[\[FONTE:(.+?)\]\]", lambda m: f'\n<p class="fonte">Fonte: {m.group(1).strip()}</p>\n', md_texto)
    corpo = markdown.markdown(md_texto, extensions=["extra", "sane_lists"])
    # tabela numérica (padrão IBGE) × quadro textual
    corpo = re.sub(r'(<p class="legenda tabela">.*?</p>\s*)<table>', r'\1<table class="tabela">', corpo, flags=re.S)
    corpo = corpo.replace("<table>", '<table class="quadro">')
    corpo = re.sub(r'<table class="quadro">(\s*<thead>\s*<tr>\s*<th>Data</th>)', r'<table class="quadro calendario">\1', corpo)
    corpo = re.sub(r'<table class="quadro">(\s*<thead>\s*<tr>\s*<th>Tipo</th>)', r'<table class="quadro matriz">\1', corpo)
    corpo = re.sub(r'<table class="quadro">(\s*<thead>\s*<tr>\s*<th>Fase</th>)', r'<table class="quadro plano">\1', corpo)

    # legenda + quadro/tabela/modelo + fonte formam um bloco que não se separa;
    # quadros longos podem quebrar, mas a fonte fica presa à última linha
    def bloco(m):
        longo = m.group(0).count("<tr>") > 10
        return f'<div class="bloco{" longo" if longo else ""}">{m.group(0)}</div>'
    corpo = re.sub(r'<p class="legenda[^"]*">.*?</p>\s*(?:<table.*?</table>|<blockquote>.*?</blockquote>)\s*<p class="fonte">.*?</p>',
                   bloco, corpo, flags=re.S)
    # Referências: título sem número, centralizado; lista alinhada à esquerda (NBR 6023)
    corpo = re.sub(r"<h1>(REFERÊNCIAS)</h1>(.*)$", r'<h1 class="sem-num">\1</h1><div class="ref">\2</div>', corpo, flags=re.S)
    # ids para o sumário
    n = [0]

    def ident(m):
        n[0] += 1
        return f'<{m.group(1)} id="s{n[0]}"{m.group(2)}>'
    corpo = re.sub(r"<(h[123])((?: class=\"[^\"]*\")?)>", ident, corpo)
    return corpo, cont


def titulos(corpo):
    return [(int(nivel), sid, html.unescape(re.sub(r"<[^>]+>", "", t)))
            for nivel, sid, t in re.findall(r'<h([123]) id="(s\d+)"[^>]*>(.*?)</h[123]>', corpo)]


CSS = """
@page { size: A4; margin: 3cm 2cm 2cm 3cm;
  @top-right { content: counter(page); font-family: Arial, sans-serif; font-size: 10pt; } }
@page pre { @top-right { content: none; } }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 12pt; line-height: 1.5; color: #000; margin: 0; }
.capa, .rosto, .sumario { page: pre; }
.capa, .rosto { height: 24.6cm; display: flex; flex-direction: column; justify-content: space-between;
  text-align: center; break-after: page; }
.capa .topo, .capa .autor, .rosto .autor { font-weight: bold; text-transform: uppercase; }
.capa .titulo, .rosto .titulo { font-size: 12pt; }
.capa .titulo b, .rosto .titulo b { text-transform: uppercase; }
.capa .base, .rosto .base { font-weight: bold; text-transform: uppercase; }
.rosto .natureza { margin-left: 8cm; text-align: justify; font-size: 11pt; line-height: 1.15; }
.sumario { break-after: page; }
.sumario h1 { text-align: center; break-before: auto; }
.toc { list-style: none; padding: 0; margin: 0; }
.toc li { display: flex; align-items: baseline; gap: 6px; line-height: 1.5; }
.toc li .t { white-space: nowrap; overflow: hidden; }
.toc li .dots { flex: 1; border-bottom: 1px dotted #000; transform: translateY(-4px); }
.toc li.n1 { font-weight: bold; text-transform: uppercase; }
.toc li.n2 { text-transform: uppercase; }
.toc li.n3 { font-weight: bold; }
.conteudo p { text-align: justify; text-indent: 1.25cm; margin: 0 0 6pt; orphans: 3; widows: 3; }
.conteudo li p, .conteudo td p, .conteudo blockquote p { text-indent: 0; }
h1 { font-size: 12pt; font-weight: bold; text-transform: uppercase; margin: 0 0 18pt; break-before: page; break-after: avoid; }
h1.sem-num { text-align: center; }
h2 { font-size: 12pt; font-weight: normal; text-transform: uppercase; margin: 18pt 0 6pt; break-after: avoid; }
h3 { font-size: 12pt; font-weight: bold; margin: 14pt 0 6pt; break-after: avoid; }
ul, ol { margin: 0 0 8pt; padding-left: 1.25cm; text-align: justify; }
li { margin-bottom: 3pt; }
.legenda { text-indent: 0 !important; font-size: 10pt; line-height: 1.3; margin: 12pt 0 3pt !important; text-align: left !important;
  break-after: avoid; }
.fonte { text-indent: 0 !important; font-size: 10pt; line-height: 1.3; margin: 3pt 0 12pt !important; text-align: left !important; }
table { width: 100%; border-collapse: collapse; font-size: 10pt; line-height: 1.3; margin: 0; break-inside: auto; }
table tr { break-inside: avoid; }
table.quadro th, table.quadro td { border: 1px solid #000; padding: 4pt 5pt; text-align: left; vertical-align: top; }
table.quadro th { background: #EDEDED; }
.bloco:not(.longo) { break-inside: avoid; }
.bloco.longo .fonte { break-before: avoid; }
table.calendario th:nth-child(1) { width: 2.2cm; }
table.calendario th:nth-child(2), table.calendario th:nth-child(5) { width: 1cm; }
table.calendario th:nth-child(4) { width: 2.5cm; }
table.calendario th:nth-child(6) { width: 3cm; }
table.matriz th:nth-child(1) { width: 3.6cm; }
table.matriz th:nth-child(2) { width: 2.8cm; }
table.plano th:nth-child(1), table.plano th:nth-child(2) { width: 2.6cm; }
table.calendario td:nth-child(1) { white-space: nowrap; }
table.calendario td:nth-child(2), table.calendario td:nth-child(5),
table.calendario th:nth-child(2), table.calendario th:nth-child(5) { text-align: center; }
table.tabela { border-top: 1.5px solid #000; border-bottom: 1.5px solid #000; }
table.tabela th { border-bottom: 1px solid #000; padding: 4pt 5pt; text-align: center; }
table.tabela td { padding: 3pt 5pt; text-align: center; }
table.tabela th:first-child, table.tabela td:first-child { text-align: left; }
blockquote { margin: 0; padding: 8pt 12pt; border: 1px solid #000; font-size: 11pt; line-height: 1.4; break-inside: avoid; }
blockquote p { text-align: left !important; margin: 0 0 6pt !important; }
blockquote p:last-child { margin-bottom: 0 !important; }
.ref p { text-align: left !important; text-indent: 0 !important; line-height: 1.15; margin: 0 0 12pt !important; }
"""


def local_ano(meta):
    return "<br>".join(x for x in (meta.get("local", "").strip(), meta["ano"]) if x)


def pagina_capa(meta):
    capa = f"""<section class="capa">
      <div class="topo">{meta['instituicao']}<br><span style="font-weight:normal">{meta['curso']}</span></div>
      <div class="autor">{meta['aluno']}</div>
      <div class="titulo"><b>{meta['titulo']}</b>: {meta['subtitulo']}</div>
      <div class="base">{local_ano(meta)}</div></section>"""
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{meta['titulo']}</title>
      <style>{CSS}</style></head><body>{capa}</body></html>"""


def pagina_corpo(meta, corpo, paginas=None):
    itens = []
    for nivel, sid, t in titulos(corpo):
        pg = (paginas or {}).get(sid, "")
        itens.append(f'<li class="n{nivel}"><span class="t">{html.escape(t)}</span><span class="dots"></span><span>{pg}</span></li>')
    rosto = f"""<section class="rosto">
      <div class="autor">{meta['aluno']}</div>
      <div class="titulo"><b>{meta['titulo']}</b>: {meta['subtitulo']}</div>
      <div class="natureza">{meta['natureza']}{f"<br><br>Tutoria: {meta['tutoria']}" if meta.get('tutoria') else ""}</div>
      <div class="base">{local_ano(meta)}</div></section>"""
    sumario = f'<section class="sumario"><h1>Sumário</h1><ul class="toc">{"".join(itens)}</ul></section>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{meta['titulo']}</title>
      <style>{CSS}</style></head><body>{rosto}{sumario}<main class="conteudo">{corpo}</main></body></html>"""


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
    # o sumário repete os títulos: a busca começa depois da página que traz o último item dele
    ultimo = norm(lista[-1][2])[:28]
    inicio = next(i for i, p in enumerate(pags) if any(norm(l).startswith(ultimo) for l in p.splitlines())) + 1
    res = {}
    for nivel, sid, t in lista:
        alvo = norm(t)[:28]
        for i in range(inicio, len(pags)):
            if any(norm(l).startswith(alvo) for l in pags[i].splitlines()):
                res[sid] = i + 1  # a folha de rosto é a página 1 do corpo
                inicio = i
                break
    return res


def conferir_remissivas(md_texto, cont):
    texto = re.sub(r"<!--.*?-->", "", md_texto, flags=re.S)
    erros = []
    for tipo, nome in (("quadro", "Quadro"), ("tabela", "Tabela")):
        for num in re.findall(rf"\({nome} (\d+)\)|\b{nome} (\d+)\b", texto):
            n = int(next(x for x in num if x))
            if n > cont[tipo]:
                erros.append(f"{nome} {n}")
    return sorted(set(erros))


def main():
    md_texto = (AQUI / "TRABALHO.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    meta = dict(re.findall(r"^(\w+):[ ]?(.*)$", re.search(r"^---\n(.*?)\n---", md_texto, re.S).group(1), re.M))
    corpo, cont = converter(md_texto)

    capa_pdf, corpo_pdf = AQUI / "_capa.pdf", AQUI / "_corpo.pdf"
    imprimir(pagina_capa(meta), capa_pdf)
    imprimir(pagina_corpo(meta, corpo), corpo_pdf)
    paginas = paginas_dos_titulos(corpo_pdf, corpo)
    imprimir(pagina_corpo(meta, corpo, paginas), corpo_pdf)

    saida = PdfWriter()
    for arq in (capa_pdf, corpo_pdf):
        for pagina in PdfReader(arq).pages:
            saida.add_page(pagina)
    saida.add_metadata({"/Title": f"{meta['titulo']}: {meta['subtitulo']}", "/Author": meta["aluno"]})
    with open(SAIDA, "wb") as f:
        saida.write(f)
    capa_pdf.unlink()
    corpo_pdf.unlink()

    faltando = [t for _, sid, t in titulos(corpo) if sid not in paginas]
    print("PDF:", SAIDA, "-", len(PdfReader(SAIDA).pages), "páginas")
    print("quadros:", cont["quadro"], "| tabelas:", cont["tabela"])
    print("títulos sem página no sumário:", faltando or "nenhum")
    print("remissivas para quadro/tabela inexistente:", conferir_remissivas(md_texto, cont) or "nenhuma")


if __name__ == "__main__":
    main()
