"""Preenche o template da AS2 de Marketing de Relacionamento com o conteúdo do TRABALHO.md.

Uso:  python preencher_template.py <TRABALHO.md> <template.docx> <saida.docx>

O template já traz títulos, perguntas e tabelas. O TRABALHO.md é dividido em blocos "@@ ÂNCORA";
cada âncora diz onde o bloco entra (ver ANCORAS abaixo). Dentro dos blocos:
  ## título             título no padrão do template (negrito, vinho)
  - item / 1. item      lista com marcador / numerada (estilos do template)
  QUADRO: / LARGURAS: a | b / | tabela | / FONTE:   quadro novo no "Estilo Berry"
  a | b | c             nos blocos T0..T7: linhas de dados das tabelas do próprio template
  **negrito**, *itálico*
"""
import copy
import re
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

MD, TEMPLATE, SAIDA = sys.argv[1], sys.argv[2], sys.argv[3]
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s](?:[^*]*[^*\s])?\*)")
VINHO = RGBColor(0x99, 0x00, 0x33)


CINZA = RGBColor(0x33, 0x33, 0x33)


def add_runs(par, texto, tamanho=None, cor=None):
    for parte in INLINE.split(texto):
        if not parte:
            continue
        if parte.startswith("**") and parte.endswith("**"):
            r = par.add_run(parte[2:-2])
            r.bold = True
        elif parte.startswith("*") and parte.endswith("*") and len(parte) > 2:
            r = par.add_run(parte[1:-1])
            r.italic = True
        else:
            r = par.add_run(parte)
        if tamanho:
            r.font.size = Pt(tamanho)
        if cor:
            r.font.color.rgb = cor


doc = docx.Document(TEMPLATE)
P = list(doc.paragraphs)
T = list(doc.tables)

# Conferência: o template é o esperado
assert P[11].text.startswith("(completar"), P[11].text
assert P[43].text.startswith("4.1"), P[43].text
assert P[52].text.startswith("Descreva brevemente"), P[52].text

# Capa
P[4].add_run(" Yan Suyama").bold = False
P[5].runs[0].text = "Projeto Prático:"


def novo_par(estilo="Normal"):
    p = doc.add_paragraph(style=estilo)
    p._p.getparent().remove(p._p)
    return p


def larguras_tabela(t, cms):
    t.autofit = False
    grid = t._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), cms):
        gc.set(qn("w:w"), str(int(w * 567)))
    for row in t.rows:
        for c, w in zip(row.cells, cms):
            c.width = Cm(w)


def proteger_linhas(t, cabecalho=1):
    for k, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement("w:cantSplit")
        cs.set(qn("w:val"), "true")
        trPr.insert(0, cs)
        if k < cabecalho:
            h = OxmlElement("w:tblHeader")
            h.set(qn("w:val"), "true")
            trPr.append(h)


def quadro_novo(linhas, larguras):
    linhas = [l for l in linhas if not re.match(r"^\|\s*-", l)]
    cel = [[c.strip() for c in l.strip().strip("|").split("|")] for l in linhas]
    t = doc.add_table(rows=len(cel), cols=len(cel[0]))
    t.style = doc.styles["Estilo Berry"]
    for i, linha in enumerate(cel):
        for j, txt in enumerate(linha):
            p = t.cell(i, j).paragraphs[0]
            p.style = doc.styles["Normal"]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.0
            add_runs(p, txt, 10, CINZA)
            if i == 0:
                for r in p.runs:
                    r.bold = True
    if larguras:
        larguras_tabela(t, larguras)
    proteger_linhas(t)
    if len(cel) <= 5:  # quadro curto não se divide entre páginas
        for row in t.rows[:-1]:
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.keep_with_next = True
    t._tbl.getparent().remove(t._tbl)
    return t._tbl


def blocos_de(linhas):
    """Converte as linhas de um bloco em elementos XML (parágrafos e quadros), em ordem."""
    out = []
    i, larg, em_ref = 0, None, False
    while i < len(linhas):
        l = linhas[i].rstrip()
        if not l.strip():
            i += 1
            continue
        if l.startswith("## "):
            p = novo_par()
            r = p.add_run(l[3:])
            r.bold = True
            r.font.color.rgb = VINHO
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(12)
            em_ref = l[3:].strip().lower() == "referências"
        elif l.startswith("QUADRO:"):
            p = novo_par("Caption")
            add_runs(p, l[7:].strip())
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(6)
        elif l.startswith("LARGURAS:"):
            larg = [float(x.strip().replace(",", ".")) for x in re.split(r"[|;]", l[9:])]
            i += 1
            continue
        elif l.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].startswith("|"):
                bloco.append(linhas[i])
                i += 1
            out.append(quadro_novo(bloco, larg))
            larg = None
            continue
        elif l.startswith("FONTE:"):
            p = novo_par("Caption")
            add_runs(p, "Fonte: " + l[6:].strip())
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(12)
        elif l.startswith("- "):
            p = novo_par("Lista_Bullet")
            add_runs(p, l[2:])
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        elif re.match(r"^\d+\. ", l):
            p = novo_par("Lista_Numerado")
            add_runs(p, re.sub(r"^\d+\. ", "", l))
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        else:
            p = novo_par()
            add_runs(p, l)
            if em_ref:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.space_after = Pt(9)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        out.append(p._p)
        i += 1
    return out


def inserir_depois(ref_el, elementos):
    for el in elementos:
        ref_el.addnext(el)
        ref_el = el
    return ref_el


def substituir(par, elementos):
    inserir_depois(par._p, elementos)
    par._p.getparent().remove(par._p)


def preencher_tabela(t, linhas, inicio, larguras=None, tamanho=None):
    dados = [[c.strip() for c in l.split("|")] for l in linhas if l.strip()]
    modelo = t.rows[-1]._tr
    while len(t.rows) - inicio < len(dados):
        t._tbl.append(copy.deepcopy(modelo))
    while len(t.rows) - inicio > len(dados):
        t._tbl.remove(t.rows[-1]._tr)
    for k, linha in enumerate(dados):
        row = t.rows[inicio + k]
        for c, txt in zip(row.cells, linha):
            tcPr = c._tc.get_or_add_tcPr()
            for v in tcPr.findall(qn("w:vAlign")):
                tcPr.remove(v)
            va = OxmlElement("w:vAlign")
            va.set(qn("w:val"), "center")
            tcPr.append(va)
            for extra in c.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
            p = c.paragraphs[0]
            for r in list(p.runs):
                r._r.getparent().remove(r._r)
            p.style = doc.styles["Normal"]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.0
            add_runs(p, txt, tamanho or 10, CINZA)
    if larguras:
        larguras_tabela(t, larguras)
    proteger_linhas(t, cabecalho=inicio)


# Lê os blocos
texto = re.sub(r"<!--.*?-->", "", open(MD, encoding="utf-8").read(), flags=re.S)
blocos, atual = {}, None
for l in texto.splitlines():
    m = re.match(r"^@@\s+(\S+)", l)
    if m:
        atual = m.group(1)
        blocos[atual] = []
    elif atual:
        blocos[atual].append(l)

usados = set()


def B(nome):
    usados.add(nome)
    return blocos[nome]


# Texto corrido
inserir_depois(P[9]._p, blocos_de(B("INTRO")))
substituir(P[11], blocos_de(B("OBJETIVO")))
inserir_depois(P[16]._p, blocos_de(B("2.1a")))
inserir_depois(P[17]._p, blocos_de(B("2.1b")))
inserir_depois(P[18]._p, blocos_de(B("2.1c")))
inserir_depois(P[21]._p, blocos_de(B("2.2a")))
inserir_depois(P[22]._p, blocos_de(B("2.2b")))
inserir_depois(P[31]._p, blocos_de(B("3.1")))
inserir_depois(P[37]._p, blocos_de(B("3.3")))
inserir_depois(P[43]._p, blocos_de(B("PAPEIS")))
substituir(P[45], blocos_de(B("T4NOTA")))
substituir(P[47], blocos_de(B("T5NOTA")))
substituir(P[49], blocos_de(B("T6NOTA")))
inserir_depois(P[52]._p, blocos_de(B("4.2")))
P[54]._p.getparent().remove(P[54]._p)
inserir_depois(T[7]._tbl, blocos_de(B("4.3NOTA")))
inserir_depois(P[57]._p, blocos_de(B("FINAL")))
P[58]._p.getparent().remove(P[58]._p)

# Etapas: título da etapa fica junto da tabela
for k in (44, 46, 48):
    P[k].paragraph_format.keep_with_next = True

# Tabelas do template
preencher_tabela(T[0], B("T0"), 1, [3.6, 13.3])
preencher_tabela(T[1], B("T1"), 1, [3.6, 13.3])
preencher_tabela(T[2], B("T2"), 1, [3.6, 4.6, 8.7])
preencher_tabela(T[3], B("T3"), 1, [2.9, 4.0, 10.0])
for t, nome in ((T[4], "T4"), (T[5], "T5"), (T[6], "T6")):
    preencher_tabela(t, B(nome), 1, [5.6, 2.6, 5.0, 3.7], tamanho=9.5)
    for c in t.rows[0].cells:
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
# Tabela 7: linha 0 = objetivo, linha 1 = cabeçalho, dados a partir da linha 2
cel = T[7].rows[0].cells[1]
p = cel.paragraphs[0]
for r in list(p.runs):
    r._r.getparent().remove(r._r)
add_runs(p, " ".join(l.strip() for l in B("T7OBJ") if l.strip()), 10, CINZA)
preencher_tabela(T[7], B("T7"), 2, [5.6, 11.3])
# Quadro de indicadores fica inteiro em uma página, junto do título 4.3
for row in T[7].rows[:-1]:
    for c in row.cells:
        for p in c.paragraphs:
            p.paragraph_format.keep_with_next = True
for k in (55, 56):
    P[k].paragraph_format.keep_with_next = True

faltando = set(blocos) - usados
assert not faltando, f"blocos sem âncora: {faltando}"

cp = doc.core_properties
cp.author = "Yan Suyama"
cp.last_modified_by = "Yan Suyama"
cp.title = "Marketing de Relacionamento – Atividade Somativa 2 – Transformação cultural e comunicação integrada"
cp.comments = ""
doc.save(SAIDA)
print("ok:", SAIDA)
