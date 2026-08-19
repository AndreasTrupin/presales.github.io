#!/usr/bin/env python3
"""
Régénère index.html à la racine du repo : une page d'accueil qui liste
tous les dossiers clientN présents, avec un lien vers chacun.
A relancer (python3 generate_index.py) à chaque nouvelle démo ajoutée.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

def find_clients():
    clients = []
    for name in os.listdir(ROOT):
        path = os.path.join(ROOT, name)
        if os.path.isdir(path) and re.fullmatch(r"client\d+", name) and os.path.exists(os.path.join(path, "index.html")):
            clients.append(name)
    clients.sort(key=lambda n: int(re.search(r"\d+", n).group()))
    return clients

def build_html(clients):
    rows = []
    for c in clients:
        num = re.search(r"\d+", c).group()
        rows.append(f'''      <a class="card" href="./{c}/">
        <span class="num">{num}</span>
        <span class="label">Démo {c}</span>
        <span class="arrow">&rarr;</span>
      </a>''')
    cards = "\n".join(rows)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diabolocom - Démos Presales</title>
<style>
  :root{{--bg:#0d1117;--card:#161b22;--line:#2a313c;--txt:#f2f5f8;--muted:#9aa4af;--accent:#29abe2;}}
  *{{box-sizing:border-box}}
  body{{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--txt)}}
  header{{padding:32px 24px 8px;max-width:900px;margin:0 auto}}
  header h1{{margin:0 0 6px;font-size:26px}}
  header p{{margin:0;color:var(--muted);font-size:14px}}
  main{{max-width:900px;margin:0 auto;padding:24px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}}
  .card{{display:flex;align-items:center;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;text-decoration:none;color:var(--txt);transition:transform .1s,border-color .1s}}
  .card:hover{{transform:translateY(-2px);border-color:var(--accent)}}
  .num{{width:36px;height:36px;border-radius:8px;background:var(--accent);color:#0d1117;font-weight:700;display:grid;place-items:center;flex:none}}
  .label{{font-size:15px;font-weight:600;flex:1}}
  .arrow{{color:var(--muted)}}
  .card:hover .arrow{{color:var(--accent)}}
  footer{{max-width:900px;margin:0 auto;padding:24px;color:var(--muted);font-size:12px}}
  .empty{{color:var(--muted);font-size:14px}}
</style>
</head>
<body>
<header>
  <h1>Démos Presales</h1>
  <p>Espaces client de démonstration pour le chatbot Diabolocom.</p>
</header>
<main>
  <div class="grid">
{cards if clients else '    <p class="empty">Aucune démo pour le moment.</p>'}
  </div>
</main>
<footer>&copy; Diabolocom, 2026</footer>
</body>
</html>
"""

if __name__ == "__main__":
    clients = find_clients()
    html = build_html(clients)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html régénéré avec {len(clients)} démo(s) : {', '.join(clients)}")
