"""Gera as imagens das telas do protótipo com o Edge em modo headless.

Uso: python Prototipo/gerar_telas.py               (todas)
     python Prototipo/gerar_telas.py 04-passo2-ok  (só uma)
Depois rode python Entrega/gerar_pdf.py para atualizar o PDF.
"""
import pathlib, subprocess, sys, tempfile
from PIL import Image

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "telas"
PROF = pathlib.Path(tempfile.gettempdir()) / "edge-telas-prof"
BG = (221, 225, 231)  # fundo do html (#DDE1E7), usado para recortar

def shot(name, query, h=2600, w=700, url=None, crop=True):
    target = url or (BASE / "index.html").as_uri() + "?" + query
    png = OUT / f"{name}.png"
    cmd = [EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
           f"--window-size={w},{h}", f"--user-data-dir={PROF}", "--virtual-time-budget=6000",
           "--run-all-compositor-stages-before-draw", f"--screenshot={png}", target]
    subprocess.run(cmd, capture_output=True, timeout=120)
    im = Image.open(png).convert("RGB")
    if crop:
        px = im.load()
        W, H = im.size
        # limites laterais: a faixa escura do topo ocupa exatamente a largura do app
        row = 6
        xs = [x for x in range(W) if px[x, row] != BG]
        left, right = min(xs), max(xs) + 1
        cx = (left + right) // 2
        bottom = H
        for y in range(H - 1, 0, -1):
            if px[cx, y] != BG or px[left + 3, y] != BG:
                bottom = y + 1
                break
        im = im.crop((left, 0, right, bottom))
    im.save(png, optimize=True)
    print(name, im.size)

TELAS = {
    "01-home-v2": "p=home&v=2",
    "01-home-v1": "p=home&v=1",
    "02-faq": "p=faq&v=2",
    "03-passo1-produto": "p=p1&v=2",
    "04-passo2-ok": "p=p2-ok&v=2",
    "05-passo2-abaixo-minimo-v1": "p=p2-baixo&v=1",
    "05-passo2-abaixo-minimo-v2": "p=p2-baixo&v=2",
    "06-passo2-sem-tamanhos": "p=p2-sem&v=2",
    "07-passo3-personalizacao": "p=p3&v=2",
    "08-passo4-entrega": "p=p4&v=2",
    "08-passo4-erro": "p=p4-erro&v=2",
    "09-resumo-v2": "p=resumo&v=2",
    "09-resumo-v1": "p=resumo&v=1",
    "10-confirmacao": "p=confirmacao&v=2",
    "11-pedido-em-grupo": "p=grupo&v=2",
}

if __name__ == "__main__":
    only = sys.argv[1:]
    OUT.mkdir(exist_ok=True)
    for n, q in TELAS.items():
        if not only or n in only:
            shot(n, q)
