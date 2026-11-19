"""Gera os dois relatórios da AS2 de Web Analytics (estratégico e operacional) em .pptx.

Uso:  python -P gerar_relatorios.py "Planilha web analytics.xlsx" <pasta_saida>

Todos os números saem da planilha da empresa (GA4, Google Ads e Meta Ads, últimos 30 dias):
o script lê os dados, calcula os indicadores e confere os valores-chave com assert antes de
montar os slides. Depois, exportar para PDF pelo PowerPoint (ver TRABALHO.md).
"""
import os
import re
import sys
from decimal import ROUND_HALF_UP, Decimal

import openpyxl
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION, XL_TICK_MARK
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

PLANILHA, SAIDA = sys.argv[1], sys.argv[2]

# ----------------------------------------------------------------------------- dados
wb = openpyxl.load_workbook(PLANILHA, data_only=True)
ws_origem, ws_jornada, ws_perfil, ws_google, ws_meta = wb.worksheets[:5]

ORIGEM = {}
for r in range(4, 9):
    nome = ws_origem.cell(r, 1).value
    ORIGEM[nome] = dict(usu=ws_origem.cell(r, 2).value, novos=ws_origem.cell(r, 3).value,
                        eng=ws_origem.cell(r, 4).value, leads=ws_origem.cell(r, 5).value,
                        vendas=ws_origem.cell(r, 6).value)
JORNADA = [(ws_jornada.cell(r, 1).value, ws_jornada.cell(r, 2).value) for r in range(3, 8)]
CHECKOUT = [(ws_jornada.cell(r, 1).value, ws_jornada.cell(r, 2).value) for r in range(11, 15)]
PERFIL = {}
for r in range(5, 23):
    a, u, b = ws_perfil.cell(r, 1).value, ws_perfil.cell(r, 2).value, ws_perfil.cell(r, 5).value
    if u is not None:
        PERFIL[a] = (u, b)
GOOGLE = {}
for r in (4, 5):
    GOOGLE[ws_google.cell(r, 2).value] = dict(
        obj=ws_google.cell(r, 3).value, alc=ws_google.cell(r, 4).value, cliq=ws_google.cell(r, 5).value,
        conv=ws_google.cell(r, 7).value, gasto=ws_google.cell(r, 9).value, vendas=ws_google.cell(r, 10).value)
META = {}
for r in (2, 3, 4):
    META[ws_meta.cell(r, 1).value] = dict(
        obj=ws_meta.cell(r, 2).value, alc=ws_meta.cell(r, 3).value, cliq=ws_meta.cell(r, 4).value,
        conv=ws_meta.cell(r, 6).value, gasto=ws_meta.cell(r, 8).value, vendas=ws_meta.cell(r, 9).value)
CONJ = {}
for r in (8, 9, 10):
    CONJ[ws_meta.cell(r, 1).value] = dict(
        alc=ws_meta.cell(r, 3).value, cliq=ws_meta.cell(r, 4).value,
        conv=ws_meta.cell(r, 5).value, gasto=ws_meta.cell(r, 7).value)

TICKET = 450
LIMITE_PCT = 0.28
LIMITE = TICKET * LIMITE_PCT  # R$ 126 por venda

USU = sum(o["usu"] for o in ORIGEM.values())
NOVOS = sum(o["novos"] for o in ORIGEM.values())
LEADS = sum(o["leads"] for o in ORIGEM.values())
VENDAS = sum(o["vendas"] for o in ORIGEM.values())
FAT = VENDAS * TICKET
G_GASTO = sum(c["gasto"] for c in GOOGLE.values())
M_GASTO = sum(c["gasto"] for c in META.values())
G_VENDAS = sum(c["vendas"] for c in GOOGLE.values())
M_VENDAS = sum(c["vendas"] for c in META.values())
INV = G_GASTO + M_GASTO
PAGAS = G_VENDAS + M_VENDAS
CAC = INV / PAGAS
ROAS = PAGAS * TICKET / INV
ROI = (PAGAS * TICKET - INV) / INV
CHK_INI, CHK_FIM = CHECKOUT[0][1], CHECKOUT[-1][1]
PAG = CHECKOUT[2][1]  # adicionaram forma de pagamento
PAG_TAXA = CHK_FIM / PAG

# conferências com a planilha
assert (USU, NOVOS, LEADS, VENDAS) == (38000, 21550, 1750, 655)
assert (G_GASTO, M_GASTO, G_VENDAS, M_VENDAS) == (20000, 20000, 180, 70)
assert ORIGEM["Google Ads"]["vendas"] == G_VENDAS and ORIGEM["Meta Ads"]["vendas"] == M_VENDAS
assert CHK_FIM == VENDAS and abs(CAC - 160) < 1e-9
assert round(PAG_TAXA, 3) == 0.281

# cenário de verba (mesmos R$ 40 mil): verba nova rende no máximo o limite de R$ 126 por venda
S, P = GOOGLE["Search"], GOOGLE["Pmax"]
C1, C2, C3 = META["Campanha 1"], META["Campanha 2"], META["Campanha 3"]
K1, K2, K3 = CONJ["Conjunto 1"], CONJ["Conjunto 2"], CONJ["Conjunto 3"]
CAC_S, CAC_P = S["gasto"] / S["vendas"], P["gasto"] / P["vendas"]
CAC_K1, CAC_C3 = K1["gasto"] / K1["conv"], C3["gasto"] / C3["vendas"]
CEN = [  # linha, hoje, proposto, premissa, vendas estimadas
    ("Google · Search (vendas)", S["gasto"], 15000, f"CAC atual (R$ {CAC_S:.0f})", 15000 / CAC_S),
    ("Google · PMax → meta de compra", P["gasto"], 10000, "R$ 5 mil a R$ 83 + R$ 5 mil a R$ 126",
     5000 / CAC_P + 5000 / LIMITE),
    ("Meta · Camp. 1 (leads)", C1["gasto"], 0, "pausar", 0),
    ("Meta · Camp. 2 · Conjunto 1", K1["gasto"], 5000, "R$ 2 mil a R$ 111 + R$ 3 mil a R$ 126",
     2000 / CAC_K1 + 3000 / LIMITE),
    ("Meta · Camp. 2 · Conjuntos 2 e 3", K2["gasto"] + K3["gasto"], 0, "pausar", 0),
    ("Meta · Camp. 3 (novos criativos)", C3["gasto"], 4000, f"CAC atual (R$ {CAC_C3:.0f})", 4000 / CAC_C3),
    ("Meta · Remarketing (nova)", 0, 6000, "limite (R$ 126)", 6000 / LIMITE),
]
CEN_INV = sum(c[2] for c in CEN)
CEN_VENDAS = sum(c[4] for c in CEN)
CEN_CAC = CEN_INV / CEN_VENDAS
assert CEN_INV == INV and CEN_CAC <= LIMITE


# ----------------------------------------------------------------------------- formatação
def num(x, d=0):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    s = f"{q:,.{d}f}"
    return s.replace(",", "#").replace(".", ",").replace("#", ".")


def pct(x, d=1):
    return num(x * 100, d) + "%"


def rs(x, d=0):
    return "R$ " + num(x, d)


def hexrgb(h):
    return RGBColor.from_string(h)


INK, MUTED, BERRY, BERRY2 = "1F2430", "5F6470", "7A1F4B", "A8336A"
TINT, GRAYT, LINE = "F7EEF2", "F2F3F5", "D9DCE1"
OK_T, OK_F, BAD_T, BAD_F, WARN_T, WARN_F = "1F6F43", "E6F4EC", "B42318", "FDECEA", "8A5300", "FFF4E0"
C_DENTRO, C_FORA, C_USU, C_COMP = "1F8FC4", "C2410C", "3A86C8", "A8336A"  # validados (dataviz)
FONT = "Calibri"
W, H = 13.333, 7.5


# ----------------------------------------------------------------------------- helpers
def _runs(p, texto, size, color, bold=False, italic=False):
    for i, parte in enumerate(re.split(r"\*\*", texto)):
        if not parte:
            continue
        r = p.add_run()
        r.text = parte
        f = r.font
        f.name, f.size, f.color.rgb = FONT, Pt(size), hexrgb(color)
        f.bold = bold or (i % 2 == 1)
        f.italic = italic


def _bullet(p, cor=BERRY2):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Emu(Inches(0.17))))
    pPr.set("indent", str(-Emu(Inches(0.17))))
    clr = pPr.makeelement(qn("a:buClr"), {})
    srgb = clr.makeelement(qn("a:srgbClr"), {"val": cor})
    clr.append(srgb)
    pPr.append(clr)
    pPr.append(pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"}))
    pPr.append(pPr.makeelement(qn("a:buChar"), {"char": "•"}))


def texto(s, x, y, w, h, paras, size=12, color=INK, bold=False, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.TOP, after=4, margin=0.0, italic=False):
    """paras: str ou lista de str / dict(t=..., bullet=bool, size, color, bold, after)."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = anchor
    m = Inches(margin)
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = m
    if isinstance(paras, str):
        paras = [paras]
    for i, item in enumerate(paras):
        if isinstance(item, str):
            item = dict(t=item)
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = item.get("align", align)
        p.space_after = Pt(item.get("after", after))
        p.line_spacing = 1.0
        _runs(p, item["t"], item.get("size", size), item.get("color", color),
              item.get("bold", bold), item.get("italic", italic))
        if item.get("bullet"):
            _bullet(p)
    return tb


def caixa(s, x, y, w, h, fill=TINT, raio=0.05, line=None):
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = raio
    shp.fill.solid()
    shp.fill.fore_color.rgb = hexrgb(fill)
    if line:
        shp.line.color.rgb = hexrgb(line)
        shp.line.width = Pt(0.75)
    else:
        shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def bolinha(s, x, y, n, d=0.36, fill=BERRY):
    c = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    c.fill.solid()
    c.fill.fore_color.rgb = hexrgb(fill)
    c.line.fill.background()
    c.shadow.inherit = False
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    _runs(p, str(n), 12 if d < 0.4 else 14, "FFFFFF", bold=True)


def cartao(s, x, y, w, h, titulo, paras, size=11, fill=TINT, n=None, after=4, tsize=13):
    caixa(s, x, y, w, h, fill)
    tx = x + 0.2
    if n is not None:
        bolinha(s, x + 0.18, y + 0.17, n)
        tx = x + 0.66
    texto(s, tx, y + 0.17, x + w - 0.2 - tx, 0.4, titulo, size=tsize, color=BERRY, bold=True,
          anchor=MSO_ANCHOR.MIDDLE)
    texto(s, x + 0.2, y + 0.66, w - 0.4, h - 0.8, paras, size=size, after=after)


def tabela(s, x, y, colw, linhas, size=10.5, row_h=0.3, hdr_fill=BERRY, fills=None, cores=None,
           negrito=(), aligns=None, zebra=True):
    """linhas[0] é o cabeçalho. fills/cores: dict {(r, c): hex}."""
    fills, cores = fills or {}, cores or {}
    nr, nc = len(linhas), len(colw)
    gf = s.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(sum(colw)), Inches(row_h * nr))
    t = gf.table
    tblPr = t._tbl.tblPr
    for at in ("bandRow", "firstRow"):
        tblPr.set(at, "0")
    for j, w in enumerate(colw):
        t.columns[j].width = Inches(w)
    for i in range(nr):
        t.rows[i].height = Inches(row_h)
        for j in range(nc):
            c = t.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.07)
            c.margin_top = c.margin_bottom = Inches(0.03)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            if i == 0:
                fill, cor, b = hdr_fill, "FFFFFF", True
            else:
                fill = fills.get((i, j), (GRAYT if (zebra and i % 2 == 0) else "FFFFFF"))
                cor, b = cores.get((i, j), INK), i in negrito
            c.fill.solid()
            c.fill.fore_color.rgb = hexrgb(fill)
            tf = c.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = (aligns[j] if aligns else (PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER))
            _runs(p, str(linhas[i][j]), size, cor, bold=b)
    return t


def status_cel(ok):
    return ("✓ dentro", OK_F, OK_T) if ok else ("✕ acima", BAD_F, BAD_T)


def grafico_barras(s, x, y, w, h, cats, series, rotulos, cores_pontos=None, legenda=False,
                   fsize=10, gap=45, vmax=None):
    """series: [(nome, valores, cor)]; rotulos: lista (por série) de listas de texto."""
    cd = CategoryChartData()
    cd.categories = cats
    for nome, vals, _ in series:
        cd.add_series(nome, vals)
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    ch = gf.chart
    ch.has_title = False
    ch.font.name, ch.font.size = FONT, Pt(fsize)
    ch.font.color.rgb = hexrgb(MUTED)
    ch.has_legend = legenda
    if legenda:
        ch.legend.position = XL_LEGEND_POSITION.TOP
        ch.legend.include_in_layout = False
        ch.legend.font.size = Pt(fsize)
        ch.legend.font.color.rgb = hexrgb(INK)
    va, ca = ch.value_axis, ch.category_axis
    va.has_major_gridlines = False
    va.visible = False
    va.minimum_scale = 0
    top = max(max(v) for _, v, _ in series)
    va.maximum_scale = vmax or top * 1.32
    ca.reverse_order = True
    ca.major_tick_mark = XL_TICK_MARK.NONE
    ca.format.line.color.rgb = hexrgb(LINE)
    ca.tick_labels.font.size = Pt(fsize)
    ca.tick_labels.font.color.rgb = hexrgb(INK)
    plot = ch.plots[0]
    plot.gap_width = gap
    plot.overlap = -8 if len(series) > 1 else 0
    for k, (ser, (_, vals, cor)) in enumerate(zip(plot.series, series)):
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = hexrgb(cor)
        ser.invert_if_negative = False
        for i, lbl in enumerate(rotulos[k]):
            pt = ser.points[i]
            if cores_pontos and k == 0 and cores_pontos[i]:
                pt.format.fill.solid()
                pt.format.fill.fore_color.rgb = hexrgb(cores_pontos[i])
            dl = pt.data_label
            dl.position = XL_LABEL_POSITION.OUTSIDE_END
            tf = dl.text_frame
            tf.text = lbl
            for r in tf.paragraphs[0].runs:
                r.font.size, r.font.name = Pt(fsize), FONT
                r.font.color.rgb = hexrgb(INK)
                r.font.bold = True
    return ch


class Deck:
    def __init__(self, prs, nome_rel, total):
        self.prs = prs
        self.nome_rel, self.total, self.n = nome_rel, total, 0

    def slide(self, tag, titulo, fonte):
        self.n += 1
        s = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        texto(s, 0.5, 0.32, 12.3, 0.3, tag.upper(), size=10.5, color=BERRY2, bold=True)
        texto(s, 0.5, 0.58, 12.33, 0.6, titulo, size=22, color=INK, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        texto(s, 0.5, 6.78, 12.33, 0.24, fonte, size=8.5, color=MUTED)
        texto(s, 0.5, 7.08, 10, 0.24,
              f"Yan Suyama  ·  Web Analytics e Performance Digital  ·  {self.nome_rel}",
              size=8.5, color=MUTED)
        texto(s, 11.33, 7.08, 1.5, 0.24, f"{self.n} / {self.total}", size=8.5, color=MUTED,
              align=PP_ALIGN.RIGHT)
        return s



FONTE_DADOS = ("Fonte: planilha de dados da empresa (GA4, Google Ads e Meta Ads, últimos 30 dias). "
               "Cálculos: elaborado pelo autor (2026).")

# valores derivados usados nos textos
O = ORIGEM
CONV_SITE = VENDAS / USU
CHK_CONC = CHK_FIM / CHK_INI
ORG_DIR = (O["Orgânico"]["vendas"] + O["Direto"]["vendas"]) / VENDAS
GANHO_10PP = PAG * 0.10
LEADS_5 = LEADS * 0.05


def conv_seg(attr):
    u, b = PERFIL[attr]
    return (b * VENDAS) / (u * USU) if u else 0


# ============================================================================ CAPA
PRS = Presentation()
PRS.slide_width, PRS.slide_height = Inches(W), Inches(H)
s = PRS.slides.add_slide(PRS.slide_layouts[6])
s.background.fill.solid()
s.background.fill.fore_color.rgb = hexrgb(BERRY)
texto(s, 0.9, 0.8, 11.5, 0.35, "PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ  ·  BACHARELADO EM MARKETING", size=12,
      color="F3D9E5", bold=True)
texto(s, 0.9, 1.25, 11.5, 0.35, "Web Analytics e Performance Digital", size=14, color="F3D9E5")
texto(s, 0.9, 2.35, 11.5, 1.6, "Performance digital de uma loja on-line de presentes personalizados", size=38,
      color="FFFFFF", bold=True, anchor=MSO_ANCHOR.BOTTOM)
texto(s, 0.9, 4.05, 11.5, 0.5, "Análise dos últimos 30 dias, otimizações e testes A/B", size=18, color="F3D9E5")
for i, (tit, desc) in enumerate((("Relatório estratégico", "para a gestão  ·  3 páginas"),
                                 ("Relatório operacional", "para o time de marketing  ·  8 páginas"))):
    x = 0.9 + i * 4.1
    caixa(s, x, 4.85, 3.8, 0.95, "8E2D5B")
    texto(s, x + 0.2, 4.92, 3.4, 0.4, tit, size=15, color="FFFFFF", bold=True)
    texto(s, x + 0.2, 5.3, 3.4, 0.4, desc, size=12, color="F3D9E5")
texto(s, 0.9, 6.45, 8, 0.4, "Yan Suyama", size=16, color="FFFFFF", bold=True)
texto(s, 8.43, 6.45, 4.0, 0.4, "2026", size=16, color="FFFFFF", bold=True, align=PP_ALIGN.RIGHT)

# ============================================================================ ESTRATÉGICO
E = Deck(PRS, "Relatório estratégico", 3)

# --- E1: KPIs
s = E.slide("Relatório estratégico  ·  para a gestão  ·  últimos 30 dias",
            "As vendas se perdem no pagamento, e metade da verba de mídia está acima do limite de CAC",
            FONTE_DADOS + " CAC de mídia paga = investimento ÷ faturamento das vendas atribuídas à mídia paga.")
texto(s, 0.5, 1.2, 12.33, 0.35,
      "**Objetivo:** mostrar onde a loja perde vendas e o que fazer para recuperar a conversão dentro do limite "
      f"de CAC. **Período:** últimos 30 dias. **Ticket médio:** {rs(TICKET)}. **Limite:** CAC de mídia paga até 28% "
      f"do faturamento ({rs(LIMITE)} por venda).", size=12, color=MUTED)
tiles = [
    ("Faturamento", rs(FAT), f"{num(VENDAS)} vendas × {rs(TICKET)}", INK, GRAYT),
    ("Conversão do site", pct(CONV_SITE, 2), f"{num(VENDAS)} vendas ÷ {num(USU)} usuários", INK, GRAYT),
    ("Conclusão do checkout", pct(CHK_CONC), f"{num(CHK_INI)} iniciaram, {num(CHK_FIM)} compraram", BAD_T, BAD_F),
    ("CAC de mídia paga", pct(CAC / TICKET), f"✕ limite 28%: {rs(CAC)} por venda contra {rs(LIMITE)}", BAD_T, BAD_F),
    ("ROAS da mídia paga", num(ROAS, 2), f"precisa de {num(1 / LIMITE_PCT, 2)} ou mais para caber nos 28%", BAD_T,
     BAD_F),
]
tw = (12.33 - 4 * 0.22) / 5
for i, (rot, val, sub, cor, fill) in enumerate(tiles):
    x = 0.5 + i * (tw + 0.22)
    caixa(s, x, 1.75, tw, 1.45, fill)
    texto(s, x + 0.18, 1.86, tw - 0.36, 0.3, rot, size=11, color=MUTED, bold=True)
    texto(s, x + 0.18, 2.14, tw - 0.36, 0.55, val, size=28, color=cor, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    texto(s, x + 0.18, 2.72, tw - 0.36, 0.42, sub, size=9.5, color=MUTED)

texto(s, 0.5, 3.45, 7.1, 0.3, f"Mídia paga por canal × limite de CAC ({rs(LIMITE)} por venda)", size=12.5,
      color=BERRY, bold=True)
g_cac, m_cac = G_GASTO / G_VENDAS, M_GASTO / M_VENDAS
lin = [["Canal", "Investimento", "Vendas", "CAC", "% do ticket", "Situação"],
       ["Google Ads", rs(G_GASTO), num(G_VENDAS), rs(g_cac), pct(g_cac / TICKET), "✓ dentro"],
       ["Meta Ads", rs(M_GASTO), num(M_VENDAS), rs(m_cac), pct(m_cac / TICKET),
        f"✕ {num(m_cac / LIMITE, 1)}× o limite"],
       ["Total mídia paga", rs(INV), num(PAGAS), rs(CAC), pct(CAC / TICKET), "✕ acima"]]
tabela(s, 0.5, 3.82, [1.75, 1.2, 0.85, 0.95, 1.05, 1.3], lin, size=12, row_h=0.42,
       fills={(1, 5): OK_F, (2, 5): BAD_F, (3, 5): BAD_F},
       cores={(1, 5): OK_T, (2, 5): BAD_T, (3, 5): BAD_T}, negrito=(3,))
texto(s, 0.5, 5.6, 7.1, 1.0,
      f"Sobre o faturamento total, a mídia custa {pct(INV / FAT)}. Mas {num(ORG_DIR * 100, 0)}% das vendas vêm de "
      f"orgânico e direto, sem mídia; por isso o limite vale para o CAC da mídia paga: {rs(INV)} para "
      f"{rs(PAGAS * TICKET)} em vendas atribuídas = {pct(CAC / TICKET)}.", size=11, color=MUTED)
cartao(s, 7.95, 3.45, 4.88, 3.18, "O que os números dizem", [
    dict(t=f"**O site gera interesse, mas perde a venda no fim.** {num(JORNADA[2][1])} pessoas puseram produto "
           f"no carrinho; {num(100 - CHK_CONC * 100, 0)}% de quem inicia o checkout não compra.", bullet=True,
         after=8),
    dict(t=f"**O Google Ads se paga** (CAC de {pct(g_cac / TICKET)} do ticket). **O Meta Ads** leva metade da "
           f"verba e traz {pct(M_VENDAS / PAGAS, 0)} das vendas pagas.", bullet=True, after=8),
    dict(t=f"**Quem compra é mulher, de 25 a 44 anos, no celular**, mas o tráfego tem muitos homens e "
           f"interessados em tecnologia, que quase não compram.", bullet=True, after=8),
    dict(t=f"**{num(LEADS)} leads não compraram:** base pronta para recuperar com e-mail e WhatsApp.",
         bullet=True),
], size=12.5)

# --- E2: insights
s = E.slide("Insights", "Quatro pontos explicam a queda na conversão", FONTE_DADOS)
texto(s, 0.5, 1.4, 5.7, 0.3, "Finalização da compra: usuários em cada etapa", size=12.5, color=BERRY, bold=True)
cats = ["Iniciou o checkout", "Informou o frete", "Informou o pagamento", "Comprou"]
vals = [v for _, v in CHECKOUT]
rot = [num(vals[0])] + [f"{num(vals[i])}  ·  {pct(vals[i] / vals[i - 1], 0)}" for i in range(1, 4)]
grafico_barras(s, 0.4, 1.75, 5.9, 3.55, cats, [("Usuários", vals, C_COMP)], [rot],
               cores_pontos=[None, None, None, C_FORA], fsize=11.5)
caixa(s, 0.5, 5.45, 5.7, 1.15, BAD_F)
texto(s, 0.7, 5.53, 5.3, 1.0, [
    dict(t=f"De cada 100 pessoas que iniciam o checkout, **{num(CHK_CONC * 100, 0)} compram**.", after=3),
    dict(t=f"A maior perda é a última: {num(PAG - CHK_FIM)} pessoas informaram a forma de pagamento e não "
           f"concluíram a compra.")], size=12, color=BAD_T, anchor=MSO_ANCHOR.MIDDLE)
cw, chh = 3.1, 2.5
pos = [(6.55, 1.4), (6.55 + cw + 0.18, 1.4), (6.55, 1.4 + chh + 0.2), (6.55 + cw + 0.18, 1.4 + chh + 0.2)]
cards = [
    ("O pagamento é o maior vazamento",
     f"Só {pct(PAG_TAXA, 0)} de quem informa o pagamento compra. É um sinal típico de recusa de cartão, erro "
     f"técnico ou falta da opção que o cliente quer. No tablet, {num(PERFIL['Tablet'][0] * USU)} usuários e "
     f"nenhuma venda."),
    ("O frete pega o cliente de surpresa",
     f"{pct(1 - CHECKOUT[2][1] / CHECKOUT[1][1], 0)} desistem logo depois de ver o frete. Num presente "
     f"personalizado, com prazo de produção, custo e prazo precisam aparecer antes do checkout."),
    ("A mídia atrai quem não compra",
     f"O Meta Ads trouxe {pct(O['Meta Ads']['usu'] / USU, 0)} dos usuários e converte "
     f"{pct(O['Meta Ads']['vendas'] / O['Meta Ads']['usu'], 2)}. Os compradores são 75% mulheres e 80% de "
     f"25 a 44 anos; homens e interessados em tecnologia são {pct(PERFIL['Masculino'][0], 0)} e "
     f"{pct(PERFIL['Tecnologia'][0], 0)} do tráfego."),
    ("Os dados não batem entre si",
     f"O GA4 atribui {num(O['Meta Ads']['usu'])} usuários ao Meta, que registra só "
     f"{num(sum(c['cliq'] for c in META.values()))} cliques. O funil conta {num(JORNADA[-1][1])} "
     f"“compras” contra {num(VENDAS)} vendas. Sem corrigir UTMs e tags, a verba é decidida com número errado."),
]
for i, ((x, y), (tit, corpo)) in enumerate(zip(pos, cards)):
    cartao(s, x, y, cw, chh, tit, corpo, size=12.5, n=i + 1, tsize=12.5)

# --- E3: soluções
s = E.slide("Soluções estratégicas",
            "Três frentes para voltar ao CAC de 28% e vender mais sem aumentar a verba",
            FONTE_DADOS + " Impactos são estimativas com as taxas atuais; o cenário de verba está no relatório "
                          "operacional.")
fw = (12.33 - 2 * 0.25) / 3
frentes = [
    ("Destravar o checkout", "Site · 30 dias", [
        "Auditar a etapa de pagamento: recusas, erros por aparelho e compra de teste no celular, desktop e tablet.",
        "Mostrar frete e prazo de entrega na página do produto (teste A/B).",
        f"Recuperar carrinhos: e-mail e WhatsApp para os {num(LEADS)} leads que não compraram."],
     f"Cada 10 pontos percentuais a mais na etapa de pagamento = **+{num(GANHO_10PP)} vendas/mês "
     f"(≈ {rs(GANHO_10PP * TICKET / 1000)} mil)**, sem custo de mídia."),
    ("Realocar a verba de mídia", f"Mídia paga · mesmos {rs(INV / 1000)} mil", [
        f"Tirar {rs(sum(c[1] - c[2] for c in CEN if c[1] > c[2]) / 1000)} mil do que vende acima do limite: "
        f"campanha de leads do Meta, dois conjuntos ruins e parte da Campanha 3.",
        "Levar para a PMax com meta de compra, o melhor conjunto do Meta e remarketing de quem quase comprou.",
        "Regra fixa: campanha acima de R$ 126 por venda por duas semanas perde verba."],
     f"Estimativa: **{num(PAGAS)} → {num(CEN_VENDAS)} vendas pagas** e CAC de "
     f"**{pct(CAC / TICKET)} → {pct(CEN_CAC / TICKET)}**."),
    ("Mirar quem compra e medir certo", "Mídia + dados · 2 semanas", [
        "Segmentar mulheres de 25 a 44 anos (moda e beleza, viagens, entretenimento), com criativos para celular.",
        "Corrigir UTMs do Meta, a tag de compra do Google e os eventos do funil no GA4 antes de escalar verba.",
        "Validar a segmentação com teste A/B no Meta antes de mudar todas as campanhas."],
     "**Decisões com dados confiáveis** e menos verba em público que não compra."),
]
for i, (tit, sub, itens, impacto) in enumerate(frentes):
    x = 0.5 + i * (fw + 0.25)
    caixa(s, x, 1.4, fw, 3.75, TINT)
    bolinha(s, x + 0.2, 1.58, i + 1, d=0.42)
    texto(s, x + 0.75, 1.52, fw - 0.9, 0.32, tit, size=14, color=BERRY, bold=True)
    texto(s, x + 0.75, 1.84, fw - 0.9, 0.26, sub, size=10.5, color=MUTED, bold=True)
    texto(s, x + 0.22, 2.28, fw - 0.44, 1.95, [dict(t=t, bullet=True) for t in itens], size=11.5, after=5)
    caixa(s, x + 0.15, 4.2, fw - 0.3, 0.82, "FFFFFF")
    texto(s, x + 0.3, 4.24, fw - 0.6, 0.74, impacto, size=11, anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.5, 5.3, 6, 0.3, "Metas para os próximos 60 dias", size=12.5, color=BERRY, bold=True)
metas = [("CAC de mídia paga", pct(CAC / TICKET), "≤ 28%"),
         ("Pagamento → compra", pct(PAG_TAXA, 0), "≥ 40%"),
         ("Conversão do site", pct(CONV_SITE, 2), "≥ 2,3%"),
         (f"Leads recuperados (≈ {num(LEADS_5)} vendas)", "sem dado", "≥ 5%")]
mw = (12.33 - 3 * 0.2) / 4
for i, (rot, hoje, meta) in enumerate(metas):
    x = 0.5 + i * (mw + 0.2)
    caixa(s, x, 5.65, mw, 0.95, GRAYT)
    texto(s, x + 0.18, 5.71, mw - 0.36, 0.3, rot, size=11, color=MUTED, bold=True)
    texto(s, x + 0.18, 6.02, mw - 0.36, 0.5, [dict(t=f"hoje {hoje}  →  **{meta}**")], size=15, color=INK,
          anchor=MSO_ANCHOR.MIDDLE)


# ============================================================================ OPERACIONAL
OP = Deck(PRS, "Relatório operacional", 8)
REF = "(PUCPR, [2024]{})"

# --- O1: KPIs de todas as frentes
s = OP.slide("Relatório operacional  ·  para o time de marketing  ·  visão geral",
             "KPIs de todas as frentes: o checkout perde vendas e o Meta Ads está fora do limite de CAC",
             FONTE_DADOS + " CTR sobre o alcance, como na planilha. ROI e ROAS sobre faturamento, sem margem. "
                           "Limite: 28% × R$ 450 = R$ 126 por venda.")
texto(s, 0.5, 1.2, 12.33, 0.3,
      "**Objetivo:** detalhar site, Google Ads e Meta Ads nos últimos 30 dias e o plano de otimização. "
      "Verde: dentro do limite. Vermelho: fora do limite ou abaixo da média.", size=11.5, color=MUTED)
gt = {k: sum(c[k] for c in GOOGLE.values()) for k in ("alc", "cliq")}
mt = {k: sum(c[k] for c in META.values()) for k in ("alc", "cliq")}
blocos = [
    ("Negócio", [("Faturamento", rs(FAT)), ("Vendas", num(VENDAS)), ("Ticket médio", rs(TICKET)),
                 ("Investimento em mídia", rs(INV)), ("CAC mídia paga", f"{rs(CAC)} · {pct(CAC / TICKET)}"),
                 ("ROAS mídia paga", num(ROAS, 2)), ("ROI mídia paga", pct(ROI, 0)),
                 ("Mídia ÷ faturamento", pct(INV / FAT))], {5: False, 6: False}),
    ("Site (GA4)", [("Usuários", num(USU)), ("Novos usuários", f"{num(NOVOS)} · {pct(NOVOS / USU, 0)}"),
                    ("Taxa de engajamento", "59%"), ("Leads", f"{num(LEADS)} · {pct(LEADS / USU)}"),
                    ("Conversão em venda", pct(CONV_SITE, 2)),
                    ("Abandono de carrinho", pct(1 - JORNADA[3][1] / JORNADA[2][1], 0)),
                    ("Conclusão do checkout", pct(CHK_CONC)),
                    ("Pagamento → compra", pct(PAG_TAXA))], {6: False, 7: False, 8: False}),
    ("Google Ads", [("Investimento", rs(G_GASTO)), ("Alcance", num(gt["alc"])), ("Cliques", num(gt["cliq"])),
                    ("CTR", pct(gt["cliq"] / gt["alc"])), ("CPC", rs(G_GASTO / gt["cliq"], 2)),
                    ("Vendas", num(G_VENDAS)), ("CAC", f"{rs(g_cac)} · {pct(g_cac / TICKET)}"),
                    ("ROAS", num(G_VENDAS * TICKET / G_GASTO, 2))], {7: True, 8: True}),
    ("Meta Ads", [("Investimento", rs(M_GASTO)), ("Alcance", num(mt["alc"])), ("Cliques", num(mt["cliq"])),
                  ("CTR", pct(mt["cliq"] / mt["alc"], 2)), ("CPC", rs(M_GASTO / mt["cliq"], 2)),
                  ("Vendas", num(M_VENDAS)), ("CAC", f"{rs(m_cac)} · {pct(m_cac / TICKET)}"),
                  ("ROAS", num(M_VENDAS * TICKET / M_GASTO, 2))], {7: False, 8: False}),
]
bw = (12.33 - 3 * 0.18) / 4
for i, (nome, itens, st) in enumerate(blocos):
    x = 0.5 + i * (bw + 0.18)
    lin = [[nome, ""]] + [list(it) for it in itens]
    fills, cores = {}, {}
    for r, ok in st.items():
        fills[(r, 1)], cores[(r, 1)] = (OK_F, OK_T) if ok else (BAD_F, BAD_T)
    tabela(s, x, 1.62, [bw * 0.56, bw * 0.44], lin, size=10.5, row_h=0.29, fills=fills, cores=cores,
           aligns=[PP_ALIGN.LEFT, PP_ALIGN.RIGHT])
texto(s, 0.5, 4.45, 7.6, 0.3, "CAC por campanha e conjunto (R$ por venda) × limite de R$ 126", size=12,
      color=BERRY, bold=True)
itens_cac = sorted([
    ("Google · PMax ✓", CAC_P), ("Meta · C2 Conjunto 1 ✓", CAC_K1), ("Google · Search ✓", CAC_S),
    ("Meta · Campanha 3 ✕", CAC_C3), ("Meta · C2 Conjunto 3 ✕", K3["gasto"] / K3["conv"]),
    ("Meta · C2 Conjunto 2 ✕", K2["gasto"] / K2["conv"]),
    ("Meta · Campanha 1 (leads) ✕", C1["gasto"] / C1["vendas"])], key=lambda t: t[1])
grafico_barras(s, 0.4, 4.75, 7.8, 2.0, [c for c, _ in itens_cac], [("CAC", [v for _, v in itens_cac], C_DENTRO)],
               [[rs(v) for _, v in itens_cac]], cores_pontos=[C_DENTRO if v <= LIMITE else C_FORA
                                                              for _, v in itens_cac], fsize=10, gap=35)
cartao(s, 8.45, 4.45, 4.38, 2.23, "Leitura rápida", [
    dict(t=f"{pct(ORG_DIR, 0)} das vendas vêm de orgânico e direto, sem custo de mídia.", bullet=True),
    dict(t=f"Mídia paga: {num(PAGAS)} vendas a {rs(CAC)} = {pct(CAC / TICKET)} do ticket.", bullet=True),
    dict(t=f"Google dentro do limite ({pct(g_cac / TICKET)}); Meta {num(m_cac / LIMITE, 1)}× acima.",
         bullet=True),
    dict(t=f"{pct(1 - CHK_CONC, 0)} de quem inicia o checkout não compra.", bullet=True)], size=11)

# --- O2: origem do tráfego
s = OP.slide("Site  ·  origem do tráfego (GA4)",
             "Orgânico e direto convertem mais; o Meta traz 39% dos usuários e só 11% das vendas",
             FONTE_DADOS + " Taxa de lead = leads ÷ usuários. Conversão = vendas ÷ usuários.")
lin = [["Origem", "Usuários", "Novos", "Engajamento", "Leads", "Taxa de lead", "Vendas", "Conversão",
        "% das vendas"]]
fills, cores = {}, {}
nomes = {"Referal": "Referral"}
for r, (k, o) in enumerate(ORIGEM.items(), start=1):
    cv = o["vendas"] / o["usu"]
    lin.append([nomes.get(k, k), num(o["usu"]), pct(o["novos"] / o["usu"], 0), pct(o["eng"], 0),
                num(o["leads"]), pct(o["leads"] / o["usu"]), num(o["vendas"]),
                ("▲ " if cv > CONV_SITE else "▼ ") + pct(cv, 2), pct(o["vendas"] / VENDAS)])
    fills[(r, 7)], cores[(r, 7)] = (OK_F, OK_T) if cv > CONV_SITE else (BAD_F, BAD_T)
lin.append(["Total", num(USU), pct(NOVOS / USU, 0), "59%", num(LEADS), pct(LEADS / USU), num(VENDAS),
            pct(CONV_SITE, 2), "100%"])
tabela(s, 0.5, 1.4, [1.6, 1.25, 1.2, 1.4, 1.1, 1.35, 1.1, 1.45, 1.88], lin, size=11.5, row_h=0.33,
       fills=fills, cores=cores, negrito=(6,))
cartao(s, 0.5, 3.92, 6.0, 2.75, "Análise", [
    dict(t=f"**Direto converte {pct(O['Direto']['vendas'] / O['Direto']['usu'], 1)} e orgânico "
           f"{pct(O['Orgânico']['vendas'] / O['Orgânico']['usu'], 1)}**: quem já conhece a marca ou busca o produto "
           f"compra. Juntos, são {pct(ORG_DIR, 0)} das vendas.", bullet=True),
    dict(t=f"**Meta Ads: {pct(O['Meta Ads']['novos'] / O['Meta Ads']['usu'], 0)} de usuários novos e "
           f"{pct(O['Meta Ads']['vendas'] / O['Meta Ads']['usu'], 2)} de conversão.** Tráfego frio e fora do "
           f"perfil de quem compra.", bullet=True),
    dict(t="**Referral tem o pior engajamento (35%)** e converte abaixo da média.", bullet=True),
    dict(t=f"**⚠ Dado a conferir:** o GA4 dá ao Meta {num(O['Meta Ads']['usu'])} usuários e "
           f"{num(O['Meta Ads']['leads'])} leads; a plataforma registra {num(mt['cliq'])} cliques e "
           f"{num(C1['conv'])} leads. Provável UTM errada ou social orgânico somado como pago.", bullet=True),
], size=11)
cartao(s, 6.83, 3.92, 6.0, 2.75, "Otimizações", [
    dict(t="**Padronizar UTMs** em todo link pago (utm_source=meta, utm_medium=paid_social) e separar o "
           f"orgânico do Instagram {REF.format('a')}.", bullet=True),
    dict(t="**SEO por ocasião** (aniversário, Dia das Mães, casamento) com palavras de fundo de funil: o "
           f"orgânico já é a maior fonte de vendas {REF.format('b')}.", bullet=True),
    dict(t="**Rever parceiros de referral:** manter só os que trazem visita engajada.", bullet=True),
    dict(t="**Públicos no GA4** a partir de quem comprou por orgânico e direto, para campanhas de "
           f"semelhantes {REF.format('c')}.", bullet=True),
], size=11)

# --- O3: funil e checkout
s = OP.slide("Site  ·  funil de compra e checkout",
             "Metade abandona o carrinho e 72% desistem depois de informar o pagamento",
             FONTE_DADOS + " Percentual = passagem da etapa anterior para esta.")
texto(s, 0.5, 1.35, 6.2, 0.3, "Jornada de compra (usuários)", size=12, color=BERRY, bold=True)
vj = [v for _, v in JORNADA]
rj = [num(vj[0])] + [f"{num(vj[i])}  ·  {pct(vj[i] / vj[i - 1], 0)}" for i in range(1, 5)]
grafico_barras(s, 0.4, 1.62, 6.3, 2.35, ["Início de sessão", "Viu produto", "Adicionou ao carrinho",
                                         "Iniciou pagamento", "Clicou em comprar*"],
               [("Usuários", vj, C_COMP)], [rj], cores_pontos=[None, None, None, C_FORA, None], fsize=10.5)
texto(s, 0.5, 4.05, 6.2, 0.3, "Finalização da compra (usuários)", size=12, color=BERRY, bold=True)
rc = [num(vals[0])] + [f"{num(vals[i])}  ·  {pct(vals[i] / vals[i - 1], 0)}" for i in range(1, 4)]
grafico_barras(s, 0.4, 4.32, 6.3, 2.0, ["Iniciou o checkout", "Informou o frete", "Informou o pagamento",
                                        "Comprou"],
               [("Usuários", vals, C_COMP)], [rc], cores_pontos=[None, None, None, C_FORA], fsize=10.5)
texto(s, 0.5, 6.36, 6.2, 0.4,
      f"* A planilha chama a etapa de “Comprar” ({num(JORNADA[-1][1])}), mas as vendas são {num(VENDAS)}; e indica "
      f"85% na última etapa do checkout, quando {num(CHK_FIM)} ÷ {num(PAG)} = {pct(PAG_TAXA, 0)}.",
      size=9, color=WARN_T)
cartao(s, 6.95, 1.35, 5.88, 2.62, "Análise", [
    dict(t=f"**{pct(1 - vj[1] / vj[0], 0)} saem sem ver um produto:** a vitrine não leva rápido ao produto.",
         bullet=True),
    dict(t=f"**{pct(1 - vj[3] / vj[2], 0)} abandonam o carrinho** antes de iniciar o pagamento.", bullet=True),
    dict(t=f"**{pct(1 - vals[2] / vals[1], 0)} desistem depois de ver o frete:** custo ou prazo como surpresa.",
         bullet=True),
    dict(t=f"**{pct(1 - PAG_TAXA, 0)} saem depois de informar o pagamento** ({num(PAG - CHK_FIM)} pessoas/mês): "
           f"padrão de recusa ou falha técnica, causa possível de conversão baixa {REF.format('a')}.",
         bullet=True),
    dict(t=f"**Do carrinho à compra, só {pct(VENDAS / vj[2], 0)} concluem** ({num(VENDAS)} de {num(vj[2])}): "
           f"o problema está mais no fim do funil do que na atração.", bullet=True),
], size=11.5)
cartao(s, 6.95, 4.12, 5.88, 2.58, "Otimizações", [
    dict(t="**Auditar o pagamento:** taxa de recusa no gateway, erros por navegador e aparelho, compra de teste.",
         bullet=True),
    dict(t="**Pix e parcelamento visíveis,** compra sem cadastro obrigatório e formulário curto "
           f"{REF.format('b')}.", bullet=True),
    dict(t="**Frete e prazo na página do produto** (teste A/B do slide 7).", bullet=True),
    dict(t="**Eventos no GA4:** begin_checkout, add_shipping_info, add_payment_info, purchase e um evento de "
           f"erro de pagamento {REF.format('c')}.", bullet=True),
], size=11)

# --- O4: perfil
s = OP.slide("Site  ·  perfil de público (GA4)",
             "Quem compra é mulher, tem de 25 a 44 anos e usa o celular; o tráfego não segue esse perfil",
             FONTE_DADOS + " Conversão estimada = (% dos compradores × 655) ÷ (% dos usuários × 38.000). "
                           "Gênero dos compradores soma 90% na planilha.")
ordem = ["Feminino", "Masculino", "18-24 anos", "25-34 anos", "35-44 anos", "45-54 anos", "55+ anos",
         "Moda e Beleza", "Viagens", "Entretenimento", "Tecnologia", "Negócios e Finanças",
         "Mobile", "Desktop", "Tablet"]
rotc = {"18-24 anos": "18–24 anos", "25-34 anos": "25–34 anos", "35-44 anos": "35–44 anos",
        "45-54 anos": "45–54 anos", "Moda e Beleza": "Moda e beleza", "Negócios e Finanças": "Negócios",
        "Mobile": "Celular", "Desktop": "Computador"}
texto(s, 0.5, 1.35, 6.6, 0.3, "Participação nos usuários × nos compradores", size=12, color=BERRY, bold=True)
uu = [PERFIL[a][0] * 100 for a in ordem]
bb = [PERFIL[a][1] * 100 for a in ordem]
grafico_barras(s, 0.4, 1.6, 6.75, 5.15, [rotc.get(a, a) for a in ordem],
               [("Usuários do site", uu, C_USU), ("Compradores", bb, C_COMP)],
               [[f"{v:.0f}%" for v in uu], [f"{v:.0f}%" for v in bb]], legenda=True, fsize=9.5, gap=55,
               vmax=100)
cartao(s, 7.4, 1.35, 5.43, 2.95, "Análise (conversão estimada por grupo)", [
    dict(t=f"**Mulher converte {pct(conv_seg('Feminino'), 2)}; homem, {pct(conv_seg('Masculino'), 2)}** "
           f"(4 vezes menos).", bullet=True),
    dict(t="**25 a 44 anos:** 65% dos usuários e 80% dos compradores. Acima de 55 anos, nenhuma venda.",
         bullet=True),
    dict(t=f"**Entretenimento ({pct(conv_seg('Entretenimento'), 1)}), moda e beleza "
           f"({pct(conv_seg('Moda e Beleza'), 1)}) e viagens ({pct(conv_seg('Viagens'), 1)})** puxam a venda; "
           f"tecnologia é 35% do tráfego e converte {pct(conv_seg('Tecnologia'), 2)}.", bullet=True),
    dict(t=f"**Celular converte {pct(conv_seg('Mobile'), 2)}, computador {pct(conv_seg('Desktop'), 2)}; "
           f"tablet: {num(PERFIL['Tablet'][0] * USU)} usuários e nenhuma venda**, sinal de falha no layout ou "
           f"no checkout.", bullet=True),
], size=11)
cartao(s, 7.4, 4.45, 5.43, 2.25, "Otimizações", [
    dict(t="**Segmentar mídia** para mulheres de 25 a 44 anos com esses interesses (validar no A/B do Meta).",
         bullet=True),
    dict(t=f"**Criativos e páginas pensados primeiro para o celular** {REF.format('b')}.", bullet=True),
    dict(t="**Compra de teste no tablet e no computador** e PageSpeed nas duas versões "
           f"{REF.format('b')}.", bullet=True),
    dict(t=f"**Públicos semelhantes** aos compradores no Google e no Meta {REF.format('c')}.", bullet=True),
], size=11)

# --- O5: Google Ads
s = OP.slide("Google Ads",
             "Google Ads está dentro do limite; a PMax vende mais barato mesmo otimizando para leads",
             FONTE_DADOS + " Conversões = evento configurado em cada campanha (compra na Search, lead na PMax).")
cab = ["Campanha", "Objetivo", "Alcance", "Cliques", "CTR", "CPC", "Conversões", "Custo/conv.", "Investimento",
       "Vendas", "CAC", "% do ticket", "ROAS"]
lin = [cab]
fills, cores = {}, {}
for r, (k, c) in enumerate([("Search", S), ("Pmax", P)], start=1):
    cac = c["gasto"] / c["vendas"]
    lin.append([{"Search": "Search", "Pmax": "Performance Max"}[k], c["obj"], num(c["alc"]), num(c["cliq"]),
                pct(c["cliq"] / c["alc"]), rs(c["gasto"] / c["cliq"], 2),
                num(c["conv"]) + (" leads" if c["obj"] == "Leads" else ""), rs(c["gasto"] / c["conv"]),
                rs(c["gasto"]), num(c["vendas"]), rs(cac), pct(cac / TICKET),
                num(c["vendas"] * TICKET / c["gasto"], 2)])
    fills[(r, 11)], cores[(r, 11)] = OK_F, OK_T
lin.append(["Total", "—", num(gt["alc"]), num(gt["cliq"]), pct(gt["cliq"] / gt["alc"]),
            rs(G_GASTO / gt["cliq"], 2), "—", "—", rs(G_GASTO), num(G_VENDAS), rs(g_cac), pct(g_cac / TICKET),
            num(G_VENDAS * TICKET / G_GASTO, 2)])
fills[(3, 11)], cores[(3, 11)] = OK_F, OK_T
tabela(s, 0.5, 1.4, [1.6, 0.85, 0.95, 0.85, 0.7, 0.8, 1.1, 1.0, 1.05, 0.75, 0.8, 1.0, 0.88], lin, size=11,
       row_h=0.36, fills=fills, cores=cores, negrito=(3,))
cartao(s, 0.5, 3.05, 5.2, 3.62, "Análise", [
    dict(t=f"**Search:** CTR de {pct(S['cliq'] / S['alc'])} mostra anúncio alinhado à busca, mas o CPC de "
           f"{rs(S['gasto'] / S['cliq'], 2)} deixa o CAC ({rs(CAC_S)}) colado no limite de {rs(LIMITE)}.",
         bullet=True, after=6),
    dict(t=f"**Search registra {num(S['conv'])} conversões para {num(S['vendas'])} vendas:** a tag de compra pode "
           f"não disparar em parte dos pedidos.", bullet=True, after=6),
    dict(t=f"**PMax configurada para leads trouxe {num(P['vendas'])} vendas a {rs(CAC_P)}**, o menor CAC da "
           f"conta. Mas a meta configurada é cadastro, não compra; em vendas, os KPIs são CAC e ROAS "
           f"{REF.format('a')}.", bullet=True, after=6),
    dict(t="**Engajamento de 50% no GA4**, o menor entre as origens grandes: parte do tráfego da PMax deve vir "
           "de posicionamentos de baixa intenção.", bullet=True),
], size=11)
caixa(s, 5.95, 3.05, 6.88, 3.62, TINT)
texto(s, 6.15, 3.22, 6.5, 0.4, "Otimizações", size=13, color=BERRY, bold=True)
grupos = [
    ("Search", ["Relatório de termos de pesquisa: negativar termos sem intenção de compra "
                f"{REF.format('d')}.",
                "Priorizar palavras de fundo de funil (presente personalizado + ocasião) e ajustar lance para "
                "celular e mulheres de 25 a 44 anos.",
                "Revisar a tag de compra e anúncios com prazo de produção e entrega."]),
    ("PMax", ["Trocar a meta de conversão para compra, com valor (ROAS desejado ≥ 3,6).",
              f"Subir a verba de {rs(P['gasto'])} para R$ 10.000 em etapas, acompanhando o CAC semanal.",
              f"Usar os detalhes do grupo de recursos para trocar criativos fracos {REF.format('d')}."]),
    ("Remarketing", [f"Públicos do GA4 (carrinho e checkout iniciado) nas campanhas {REF.format('c')}.",
                     "Excluir quem já comprou nos últimos 30 dias."]),
]
for (nome, its), yy in zip(grupos, (3.68, 4.98, 5.98)):
    texto(s, 6.15, yy, 1.25, 0.3, nome, size=11, color=BERRY2, bold=True)
    texto(s, 7.35, yy, 5.3, 1.2, [dict(t=t, bullet=True) for t in its], size=10.5, after=3)

# --- O6: Meta Ads
s = OP.slide("Meta Ads",
             f"Meta Ads vende a {rs(m_cac)} por venda: a campanha de leads e dois conjuntos gastam sem vender",
             FONTE_DADOS + " Conjuntos da Campanha 2 somam 30 conversões; a campanha registra 35.")
lin = [["Campanha", "Objetivo", "Alcance", "Cliques", "CTR", "CPC", "Conversões", "Custo/conv.", "Investimento",
        "Vendas", "CAC", "% do ticket", "ROAS"]]
fills, cores = {}, {}
for r, (k, c) in enumerate(META.items(), start=1):
    cac = c["gasto"] / c["vendas"]
    lin.append([k, c["obj"], num(c["alc"]), num(c["cliq"]), pct(c["cliq"] / c["alc"], 2),
                rs(c["gasto"] / c["cliq"], 2), num(c["conv"]) + (" leads" if c["obj"] == "Leads" else ""),
                rs(c["gasto"] / c["conv"]), rs(c["gasto"]), num(c["vendas"]), rs(cac), pct(cac / TICKET),
                num(c["vendas"] * TICKET / c["gasto"], 2)])
    fills[(r, 11)], cores[(r, 11)] = BAD_F, BAD_T
lin.append(["Total", "—", num(mt["alc"]), num(mt["cliq"]), pct(mt["cliq"] / mt["alc"], 2),
            rs(M_GASTO / mt["cliq"], 2), "—", "—", rs(M_GASTO), num(M_VENDAS), rs(m_cac), pct(m_cac / TICKET),
            num(M_VENDAS * TICKET / M_GASTO, 2)])
fills[(4, 11)], cores[(4, 11)] = BAD_F, BAD_T
tabela(s, 0.5, 1.35, [1.6, 0.85, 0.95, 0.85, 0.7, 0.8, 1.1, 1.0, 1.05, 0.75, 0.8, 1.0, 0.88], lin, size=10.5,
       row_h=0.3, fills=fills, cores=cores, negrito=(4,))
lin = [["Campanha 2", "Alcance", "Cliques", "CTR", "CPC", "Conv.", "Clique → conv.", "CPA", "% ticket"]]
fills, cores = {}, {}
for r, (k, c) in enumerate(CONJ.items(), start=1):
    cpa = c["gasto"] / c["conv"]
    lin.append([k, num(c["alc"]), num(c["cliq"]), pct(c["cliq"] / c["alc"], 2), rs(c["gasto"] / c["cliq"], 2),
                num(c["conv"]), pct(c["conv"] / c["cliq"]), rs(cpa), pct(cpa / TICKET)])
    ok = cpa <= LIMITE
    fills[(r, 8)], cores[(r, 8)] = (OK_F, OK_T) if ok else (BAD_F, BAD_T)
    lin[-1][8] = ("✓ " if ok else "✕ ") + lin[-1][8]
tabela(s, 0.5, 3.0, [1.1, 0.8, 0.65, 0.65, 0.7, 0.55, 1.2, 0.7, 0.8], lin, size=10.5, row_h=0.3,
       fills=fills, cores=cores)
cartao(s, 0.5, 4.38, 7.15, 2.3, "Análise", [
    dict(t=f"**Camp. 1 (leads):** {num(C1['conv'])} leads a {rs(C1['gasto'] / C1['conv'])} (a PMax faz a "
           f"{rs(P['gasto'] / P['conv'])}) e só {num(C1['vendas'])} vendas: {pct(C1['gasto'] / M_GASTO, 0)} da verba "
           f"do Meta para {pct(C1['vendas'] / M_VENDAS, 0)} das vendas.", bullet=True, after=3),
    dict(t="**Conjunto 2:** melhor CTR (1,33%) e pior CPA (R$ 500): o anúncio atrai clique de quem não compra. "
           "**Conjunto 3:** CPC de R$ 10.", bullet=True, after=3),
    dict(t="**Camp. 3:** CTR de 0,32%, mas 5% de quem clica compra: público certo, criativo fraco "
           f"{REF.format('e')}.", bullet=True, after=3),
    dict(t="**Nenhum conjunto chega a 50 conversões** no mês: verba dividida demais não sai do aprendizado "
           f"{REF.format('e')}.", bullet=True),
], size=10.5, after=3)
cartao(s, 7.9, 3.0, 4.93, 3.68, "Otimizações", [
    dict(t="**Pausar a Campanha 1.** Lead que não compra fica para o e-mail e o WhatsApp.", bullet=True),
    dict(t="**Campanha 2:** pausar os Conjuntos 2 e 3 e levar a verba ao Conjunto 1 (R$ 2 mil → R$ 5 mil) "
           f"{REF.format('e')}.", bullet=True),
    dict(t="**Campanha 3:** R$ 4 mil com novos criativos para celular; passar o aprendizado ao time de "
           "criação.", bullet=True),
    dict(t="**Remarketing novo (R$ 6 mil):** catálogo para quem viu produto, pôs no carrinho ou iniciou o "
           f"checkout, e para os leads {REF.format('f')}.", bullet=True),
    dict(t="**Atribuição de 1 dia após o clique** e UTMs padronizadas, para bater com o GA4 "
           f"{REF.format('e')}.", bullet=True),
], size=10.5)

# --- O7: testes A/B
s = OP.slide("Testes A/B",
             "Dois testes para validar as hipóteses antes de mudar o site e a verba",
             "Regra dos dois testes: uma variável por vez, hipótese tirada dos dados e tráfego dividido "
             f"igualmente {REF.format('f')}. Elaborado pelo autor (2026).")
testes = [
    ("Site: frete e prazo na página do produto", [
        ("Dado", f"{pct(1 - vals[2] / vals[1], 0)} desistem depois de ver o frete "
                 f"({num(vals[1])} → {num(vals[2])})."),
        ("Hipótese", "Mostrar frete e prazo antes do checkout reduz a desistência, porque o custo deixa de ser "
                     "surpresa."),
        ("Variável única", "Calculadora de frete e prazo na página do produto."),
        ("Versão A", "Página atual: frete só no checkout."),
        ("Versão B", "Mesma página, com campo de CEP que mostra o valor do frete e a data de entrega."),
        ("Divisão", "50% / 50% dos usuários, todos os aparelhos."),
        ("Métrica", "Principal: passagem do frete para o pagamento (hoje 65%). Secundárias: carrinho e "
                    "conversão do site."),
        ("Duração", f"4 semanas (≈ {num(CHK_INI / 2)} checkouts por versão)."),
        ("Decisão", "B vence se aumentar a passagem com o nível de confiança da ferramenta. Empate: manter A e "
                    "testar frete grátis acima de um valor."),
    ]),
    ("Mídia paga: segmentação no Meta Ads", [
        ("Dado", "Compradores: 75% mulheres e 80% de 25 a 44 anos. Meta converte 0,47%."),
        ("Hipótese", "Público feminino de 25 a 44 anos com interesse em moda e beleza, viagens e entretenimento "
                     "baixa o custo por venda."),
        ("Variável única", "Só o público. Mesmo anúncio, orçamento e otimização para compra."),
        ("Versão A", "Público atual do Conjunto 1 da Campanha 2."),
        ("Versão B", "Mulheres de 25 a 44 anos + esses três interesses."),
        ("Divisão", "Ferramenta de teste A/B do Meta, R$ 2.500 por versão (verba do Conjunto 1)."),
        ("Métrica", f"Principal: CPA de venda (meta ≤ {rs(LIMITE)}). Secundárias: CTR e taxa clique → venda."),
        ("Duração", "14 dias: resposta em um ciclo curto de 1 a 2 semanas."),
        ("Decisão", "Vence o menor CPA com a confiança indicada pelo Meta; a vencedora fica com a verba e a "
                    "outra é pausada."),
    ]),
]
tw2 = (12.33 - 0.3) / 2
for i, (tit, linhas) in enumerate(testes):
    x = 0.5 + i * (tw2 + 0.3)
    bolinha(s, x, 1.38, "AB"[i], d=0.42)
    texto(s, x + 0.55, 1.38, tw2 - 0.6, 0.42, tit, size=14, color=BERRY, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    lin = [["Item", "Teste " + str(i + 1)]] + [list(l) for l in linhas]
    t = tabela(s, x, 1.95, [1.35, tw2 - 1.35], lin, size=10.5, row_h=0.43,
               fills={(r, 0): TINT for r in range(1, len(lin))},
               cores={(r, 0): BERRY for r in range(1, len(lin))}, zebra=False,
               aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT])
    for r in range(1, len(lin)):
        for run in t.cell(r, 0).text_frame.paragraphs[0].runs:
            run.font.bold = True

# --- O8: próximos passos
s = OP.slide("Próximos passos",
             "Plano de 8 semanas: medir certo, destravar o checkout e realocar a verba",
             "Cenário de verba: estimativa conservadora, em que a verba nova rende no máximo o limite de R$ 126 por "
             "venda. Elaborado pelo autor (2026).")
texto(s, 0.5, 1.35, 6.9, 0.3, f"Redistribuição da verba (mesmos {rs(INV)})", size=12, color=BERRY, bold=True)
lin = [["Linha", "Hoje", "Proposto", "Premissa de CAC", "Vendas"]]
for nome, hoje, prop, prem, v in CEN:
    lin.append([nome, rs(hoje), rs(prop), prem, num(v)])
lin.append(["Total", rs(INV), rs(CEN_INV), f"hoje {num(PAGAS)} vendas pagas", num(CEN_VENDAS)])
lin.append(["CAC de mídia paga", f"{rs(CAC)}", f"{rs(CEN_CAC)}", "% do ticket",
            f"{pct(CAC / TICKET)} → {pct(CEN_CAC / TICKET)}"])
n = len(lin)
tabela(s, 0.5, 1.65, [2.45, 0.85, 0.95, 2.35, 1.15], lin, size=10, row_h=0.31,
       fills={(n - 1, 4): OK_F, (n - 1, 2): OK_F}, cores={(n - 1, 4): OK_T, (n - 1, 2): OK_T},
       negrito=(n - 2, n - 1), aligns=[PP_ALIGN.LEFT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT, PP_ALIGN.LEFT,
                                       PP_ALIGN.RIGHT])
texto(s, 0.5, 4.95, 6.9, 0.3, "Metas para 60 dias", size=12, color=BERRY, bold=True)
mw = (7.75 - 3 * 0.15) / 4
for i, (rot, hoje, meta) in enumerate(metas):
    if rot.startswith("Leads"):
        rot, meta = "Leads recuperados", f"{meta} (≈ {num(LEADS_5)})"
    x = 0.5 + i * (mw + 0.15)
    caixa(s, x, 5.27, mw, 0.82, GRAYT)
    texto(s, x + 0.12, 5.31, mw - 0.24, 0.3, rot, size=10, color=MUTED, bold=True)
    texto(s, x + 0.12, 5.6, mw - 0.24, 0.45, f"**{meta}**", size=12.5, color=INK, anchor=MSO_ANCHOR.MIDDLE)
etapas = [
    ("Semana 1", "Medição", "UTMs, tag de compra do Google, eventos do checkout no GA4, atribuição do Meta em 1 dia "
                            "após o clique. Auditoria do pagamento e compra de teste em todos os aparelhos."),
    ("Semanas 1–2", "Verba", "Pausar Camp. 1 e Conjuntos 2 e 3; Conjunto 1 para R$ 5 mil; PMax com meta de compra, "
                             "subindo em etapas; criar remarketing."),
    ("Semanas 2–4", "Site e testes", "Corrigir o pagamento; Pix e parcelamento visíveis; fluxo de carrinho "
                                     "abandonado; iniciar os dois testes A/B."),
    ("Semanas 5–8", "Escala", "Aplicar os vencedores; novos criativos na Camp. 3; SEO por ocasião; rever metas."),
]
x0 = 8.5
texto(s, x0, 1.35, 4.33, 0.3, "Cronograma", size=12, color=BERRY, bold=True)
for i, (quando, oque, desc) in enumerate(etapas):
    y = 1.7 + i * 1.02
    caixa(s, x0, y, 4.33, 0.92, TINT)
    texto(s, x0 + 0.15, y + 0.07, 4.05, 0.26, f"{quando}  ·  {oque}", size=11, color=BERRY, bold=True)
    texto(s, x0 + 0.15, y + 0.33, 4.05, 0.58, desc, size=9.5, color=INK)
caixa(s, x0, 5.8, 4.33, 0.6, GRAYT)
texto(s, x0 + 0.15, 5.82, 4.05, 0.56,
      f"**Rotina:** painel semanal no Looker Studio com CAC por campanha, checkout e conversão {REF.format('g')}.",
      size=9.5, anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.5, 6.18, 7.75, 0.6,
      "**Referências:** PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ (PUCPR). **Web analytics e performance digital.** "
      "Curitiba: PUCPR, [2024]a–g. Material didático: unidades 01 (a) métricas e KPIs; 02 (b) sites e landing pages; "
      "03 (c) Google Analytics 4; 04 (d) Google Ads; 05 (e) Meta Ads; 06 (f) experimentação e growth; "
      "07 (g) relatórios e dashboards.", size=8, color=MUTED)

cp = PRS.core_properties
cp.author = cp.last_modified_by = "Yan Suyama"
cp.title = "Performance digital de uma loja on-line de presentes personalizados"
cp.subject = "Web Analytics e Performance Digital – relatórios estratégico e operacional"
cp.comments = cp.keywords = cp.category = ""
ARQ = os.path.join(SAIDA, "Relatórios de performance - Web Analytics.pptx")
PRS.save(ARQ)
print("ok:", ARQ)

print(f"vendas pagas {PAGAS}, CAC {CAC:.2f}; cenário {CEN_VENDAS:.1f} vendas, CAC {CEN_CAC:.2f} "
      f"({CEN_CAC / TICKET:.1%})")
