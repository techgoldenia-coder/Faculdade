"""Gera as imagens das telas a partir da versão de teste do site (site-prototipo-megawr).

Uso:
  1. cd site-prototipo-megawr && npm run build
  2. python Prototipo/gerar_telas_site.py            (todas)
     python Prototipo/gerar_telas_site.py 04-passo2-ok  (só uma)
  3. python Entrega/gerar_pdf.py

Serve o dist/ localmente, abre cada página num iframe de 390 px (largura de celular)
com o Edge em modo headless e recorta a imagem na altura real da página.
"""
import http.server
import pathlib
import socketserver
import subprocess
import sys
import tempfile
import threading
from functools import partial

from PIL import Image

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
AQUI = pathlib.Path(__file__).resolve().parent
DIST = AQUI.parent / "site-prototipo-megawr" / "dist"
OUT = AQUI / "telas-site"
PROF = pathlib.Path(tempfile.gettempdir()) / "edge-telas-site-prof"
PORTA = 4399
BG = (221, 225, 231)  # fundo da página de captura (#DDE1E7)

MOLDURA = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;background:#DDE1E7}iframe{display:block;border:0;width:390px;height:844px;background:#fff}
</style></head><body><iframe id="f"></iframe><script>
var f=document.getElementById('f');
f.src=decodeURIComponent(location.hash.slice(1));
f.onload=function(){setTimeout(function(){
  var d=f.contentDocument.documentElement; f.style.height=d.scrollHeight+'px';
},600)};
</script></body></html>"""

TELAS = {
    # versão revisada (padrão) e versão apresentada nas conversas (?v=1)
    "01-home-v2": "/?shot",
    "01-home-v1": "/?shot&v=1",
    "02-faq": "/?shot&secao=duvidas",
    "03-passo1-produto": "/orcamento/?shot&p=p1",
    "04-passo2-ok": "/orcamento/?shot&p=p2-ok",
    "05-passo2-abaixo-minimo": "/orcamento/?shot&p=p2-baixo",
    "06-passo2-sem-tamanhos-v1": "/orcamento/?shot&p=p2-sem&v=1",
    "06-passo2-sem-tamanhos-v2": "/orcamento/?shot&p=p2-sem",
    "07-passo3-personalizacao-v1": "/orcamento/?shot&p=p3&v=1",
    "07-passo3-personalizacao-v2": "/orcamento/?shot&p=p3",
    "08-passo4-entrega-v1": "/orcamento/?shot&p=p4&v=1",
    "08-passo4-entrega-v2": "/orcamento/?shot&p=p4",
    "08-passo4-erro": "/orcamento/?shot&p=p4-erro",
    "09-resumo-v1": "/orcamento/?shot&p=resumo&v=1",
    "09-resumo-v2": "/orcamento/?shot&p=resumo",
    "10-confirmacao": "/orcamento/?shot&p=confirmacao",
    "10-confirmacao-email": "/orcamento/?shot&p=confirmacao-email",
    "11-pedido-em-grupo": "/orcamento/?shot&p=grupo",
}


def servir():
    class Silencioso(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = partial(Silencioso, directory=str(DIST))
    srv = socketserver.TCPServer(("127.0.0.1", PORTA), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def capturar(nome, caminho):
    png = OUT / f"{nome}.png"
    url = f"http://127.0.0.1:{PORTA}/_moldura.html#{caminho.replace('&', '%26').replace('?', '%3F')}"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=700,4200", f"--user-data-dir={PROF}", "--virtual-time-budget=9000",
                    "--run-all-compositor-stages-before-draw", f"--screenshot={png}", url],
                   capture_output=True, timeout=180)
    im = Image.open(png).convert("RGB")
    px = im.load()
    largura = 780  # 390 px de CSS em escala 2
    # altura útil: última linha, na coluna da esquerda do iframe, que não é o fundo cinza
    base = im.height
    for y in range(im.height - 1, 0, -1):
        if px[3, y] != BG:
            base = y + 1
            break
    im.crop((0, 0, largura, base)).save(png, optimize=True)
    print(nome, (largura, base))


def main():
    OUT.mkdir(exist_ok=True)
    (DIST / "_moldura.html").write_text(MOLDURA, encoding="utf-8")
    srv = servir()
    try:
        so = sys.argv[1:]
        for nome, caminho in TELAS.items():
            if not so or nome in so:
                capturar(nome, caminho)
    finally:
        srv.shutdown()
        (DIST / "_moldura.html").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
