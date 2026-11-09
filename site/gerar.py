#!/usr/bin/env python3
"""Gera a página: python3 site/gerar.py [saida.html]  (padrão: index.html na raiz)."""
import csv, json, sys, datetime
from pathlib import Path
raiz = Path(__file__).resolve().parent.parent
MESES = sorted((p for p in raiz.glob("*-20[0-9][0-9]") if p.is_dir()),
               key=lambda p: (p.name[-4:], ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"].index(p.name[:-5])))
def ultimo(n):
    for p in reversed(MESES):
        if (p / n).exists(): return list(csv.DictReader(open(p / n, encoding="utf8")))
    return []
data = {"liga": ultimo("liga-resumo.csv"), "guerras": ultimo("ataques.csv"),
        "sorteio": ultimo("sorteio.csv"), "participantes": ultimo("sorteio-participantes.csv"),
        "banidos": list(csv.DictReader(open(raiz / "banidos.csv", encoding="utf8"))) if (raiz / "banidos.csv").exists() else [],
        "atualizado": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
tpl = (raiz / "site/landing.html").read_text(encoding="utf8")
tpl = tpl.replace("__CLA__", "https://link.clashofclans.com/pt?action=OpenClanProfile&amp;tag=PJP9CJY9")
tpl = tpl.replace("__BRASAO__", (raiz / "marca/brasao.svg").read_text(encoding="utf8"))
saida = Path(sys.argv[1]) if len(sys.argv) > 1 else raiz / "index.html"
saida.write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf8")
print("Gerado:", saida)
