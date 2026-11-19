"""Gera o .docx da AS2 de Design Experimental a partir do TRABALHO.md, dentro do template da PUC-PR.

Uso:  python gerar_docx.py <TRABALHO.md> <template.docx> <saida.docx>

Sintaxe aceita no TRABALHO.md:
  <!-- ... -->          bloco de controle, ignorado
  # / ## / ###          título do trabalho / seção / subseção
  *texto*               linha inteira em itálico logo após o título = subtítulo
  - item                lista com marcador (estilo Lista_Bullet do template)
  QUADRO: título        legenda acima do quadro
  LARGURAS: a;b;c       largura das colunas do próximo quadro, em cm
  | a | b |             quadro (a primeira linha é o cabeçalho; a linha |---| é ignorada)
  FONTE: texto          fonte abaixo do quadro
  **negrito**, *itálico*, \\* = asterisco literal
"""
import re
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

MD, TEMPLATE, SAIDA = sys.argv[1], sys.argv[2], sys.argv[3]

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s](?:[^*]*[^*\s])?\*)")


def add_runs(par, texto):
    texto = texto.replace("\\*", "\x00")
    for parte in INLINE.split(texto):
        if not parte:
            continue
        if parte.startswith("**") and parte.endswith("**"):
            run = par.add_run(parte[2:-2].replace("\x00", "*"))
            run.bold = True
        elif parte.startswith("*") and parte.endswith("*") and len(parte) > 2:
            run = par.add_run(parte[1:-1].replace("\x00", "*"))
            run.italic = True
        else:
            par.add_run(parte.replace("\x00", "*"))


doc = docx.Document(TEMPLATE)
pars = doc.paragraphs

# Nome do estudante: o primeiro "[Escreva aqui]"
pars[3].runs[0].text = "Yan Suyama"

# Âncora: o "[Escreva aqui]" da resposta. Tudo é inserido antes dela.
ancora = pars[6]
assert ancora.text == "[Escreva aqui]", ancora.text
# Bloco repetido do template (título vazio, sumário, quebra, segundo "sua resposta"): sai.
for p in pars[7:14]:
    p._p.getparent().remove(p._p)


def par(texto="", estilo="Normal", alinhar=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = ancora.insert_paragraph_before("", style=estilo)
    if alinhar is not None:
        p.alignment = alinhar
    add_runs(p, texto)
    return p


def quadro(linhas, larguras):
    linhas = [l for l in linhas if not re.match(r"^\|\s*-", l)]
    celulas = [[c.strip() for c in l.strip().strip("|").split("|")] for l in linhas]
    ncol = len(celulas[0])
    t = doc.add_table(rows=len(celulas), cols=ncol)
    t.style = doc.styles["Estilo Berry"]
    t.autofit = False
    for i, linha in enumerate(celulas):
        for j, txt in enumerate(linha):
            cel = t.cell(i, j)
            if larguras:
                cel.width = Cm(larguras[j])
            p = cel.paragraphs[0]
            p.style = doc.styles["Conteudo_tabela"]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, txt)
            if i == 0:
                for r in p.runs:
                    r.bold = True
    # Cabeçalho repete se o quadro quebrar de página
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    trPr = t.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement("w:tblHeader")
    h.set(qn("w:val"), "true")
    trPr.append(h)
    # Nenhuma linha se parte entre duas páginas
    for row in t.rows:
        cs = OxmlElement("w:cantSplit")
        cs.set(qn("w:val"), "true")
        row._tr.get_or_add_trPr().insert(0, cs)
    ancora._p.addprevious(t._tbl)


texto = open(MD, encoding="utf-8").read()
texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
linhas = texto.splitlines()

i = 0
em_referencias = False
larguras = None
depois_do_titulo = False
while i < len(linhas):
    l = linhas[i].rstrip()
    if not l.strip():
        i += 1
        continue
    if l.startswith("# "):
        par(l[2:], "Heading 1", None)
        depois_do_titulo = True
    elif l.startswith("## "):
        p = par(l[3:], "Heading 2", None)
        p.paragraph_format.keep_with_next = True
        em_referencias = l[3:].strip().lower() == "referências"
    elif l.startswith("### "):
        p = par(l[4:], "Heading 3", None)
        p.paragraph_format.keep_with_next = True
    elif depois_do_titulo and l.startswith("*") and l.endswith("*"):
        p = par(l, "Normal", None)
        p.paragraph_format.space_after = Pt(14)
    elif l.startswith("QUADRO:"):
        p = par(l[7:].strip(), "Caption", WD_ALIGN_PARAGRAPH.LEFT)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(6)
    elif l.startswith("LARGURAS:"):
        larguras = [float(x.replace(",", ".")) for x in l[9:].strip().split(";")]
    elif l.startswith("|"):
        bloco = []
        while i < len(linhas) and linhas[i].startswith("|"):
            bloco.append(linhas[i])
            i += 1
        quadro(bloco, larguras)
        larguras = None
        continue
    elif l.startswith("FONTE:"):
        p = par("Fonte: " + l[6:].strip(), "Caption", WD_ALIGN_PARAGRAPH.LEFT)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(12)
    elif l.startswith("- "):
        par(l[2:], "Lista_Bullet")
    elif re.match(r"^\d+\. ", l):
        par(re.sub(r"^\d+\. ", "", l), "Lista_Numerado")
    elif em_referencias:
        p = par(l, "Normal", WD_ALIGN_PARAGRAPH.LEFT)
        p.paragraph_format.space_after = Pt(9)
    else:
        par(l)
    if not l.startswith("# "):
        depois_do_titulo = depois_do_titulo and l.startswith("# ")
    i += 1

ancora._p.getparent().remove(ancora._p)

cp = doc.core_properties
cp.author = "Yan Suyama"
cp.last_modified_by = "Yan Suyama"
cp.title = "Design Experimental – Atividade Somativa 2 – Pré-projeto de pesquisa experimental"
cp.comments = ""

doc.save(SAIDA)
print("ok:", SAIDA)
