#!/usr/bin/env python3
"""Gera a página: python3 site/gerar.py [saida.html]  (padrão: index.html na raiz)."""
import csv, json, sys, datetime
from pathlib import Path
raiz = Path(__file__).resolve().parent.parent
mes = raiz / "outubro-2026"
ler = lambda n: list(csv.DictReader(open(mes / n, encoding="utf8")))
data = {"liga": ler("liga-resumo.csv"), "guerras": ler("ataques.csv"),
        "sorteio": ler("sorteio.csv") if (mes / "sorteio.csv").exists() else [],
        "atualizado": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
tpl = (raiz / "site/landing.html").read_text(encoding="utf8")
tpl = tpl.replace("__CLA__", "https://link.clashofclans.com/pt?action=OpenClanProfile&amp;tag=PJP9CJY9")
tpl = tpl.replace("__BRASAO__", (raiz / "marca/brasao.svg").read_text(encoding="utf8"))
saida = Path(sys.argv[1]) if len(sys.argv) > 1 else raiz / "index.html"
saida.write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf8")
print("Gerado:", saida)
