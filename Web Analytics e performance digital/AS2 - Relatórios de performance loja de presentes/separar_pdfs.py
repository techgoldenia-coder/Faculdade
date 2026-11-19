"""Separa o PDF unificado nos dois relatórios de entrega (sem a capa, para respeitar o limite de páginas).

Uso:  python -P separar_pdfs.py YanSuyama_WebAnalytics_Relatorios.pdf
Página 1 = capa; 2 a 4 = relatório estratégico; 5 a 12 = relatório operacional.
"""
import os
import sys

import pymupdf

ORIGEM = sys.argv[1]
PASTA = os.path.dirname(os.path.abspath(ORIGEM))
fonte = pymupdf.open(ORIGEM)
assert len(fonte) == 12, f"esperava 12 páginas, veio {len(fonte)}"

for nome, (ini, fim), titulo in (
        ("YanSuyama_WebAnalytics_RelatorioEstrategico.pdf", (1, 3),
         "Relatório estratégico – Performance digital de uma loja on-line de presentes personalizados"),
        ("YanSuyama_WebAnalytics_RelatorioOperacional.pdf", (4, 11),
         "Relatório operacional – Performance digital de uma loja on-line de presentes personalizados")):
    novo = pymupdf.open()
    novo.insert_pdf(fonte, from_page=ini, to_page=fim)
    meta = dict(fonte.metadata)
    meta.update(title=titulo, author="Yan Suyama", subject="Web Analytics e Performance Digital")
    novo.set_metadata(meta)
    caminho = os.path.join(PASTA, nome)
    novo.save(caminho, garbage=3, deflate=True)
    print(f"ok: {nome} ({len(novo)} páginas)")
