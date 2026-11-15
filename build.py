"""Gera quintal-vercel/index.html a partir de ../quintal-de-jogos.html (página completa para a Vercel)."""
import pathlib, re
here = pathlib.Path(__file__).parent
src = (here / "src" / "quintal-de-jogos.html").read_text(encoding="utf-8")
src = re.sub(r'<meta name="claude:[^>]*>\n?', "", src)
cut = src.index("</script>", src.index("</style>")) + len("</script>")
head, body = src[:cut], src[cut:]
title = re.search(r"<title>.*?</title>", head).group(0)
head = head.replace(title, "")
page = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{title}
<meta name="description" content="Três jogos simples para estimular a psicomotricidade de pessoas idosas: Pega a Fruta, Jogo da Memória e Acenda as Luzes.">
<meta name="theme-color" content="#B9DCF4">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Quintal">
<meta name="application-name" content="Quintal de Jogos">
<meta name="format-detection" content="telephone=no">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta property="og:title" content="Quintal de Jogos">
<meta property="og:description" content="Jogos simples de psicomotricidade para pessoas idosas.">
<meta property="og:image" content="/og.png">
<style>img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head.strip()}
</head>
<body>
{body.strip()}
<script>if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("/sw.js").catch(() => {{}}));</script>
</body>
</html>
"""
(here / "index.html").write_text(page, encoding="utf-8")
print("index.html", len(page))
