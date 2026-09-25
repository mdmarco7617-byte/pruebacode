# -*- coding: utf-8 -*-
"""Genera las paginas de sector en elementor/sectores/.
Uso: python3 tools/sectores/build_all.py"""
import os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sector_build import build
OUT = os.path.join(HERE, "..", "..", "elementor", "sectores")
for mod in sorted(f[:-3] for f in os.listdir(HERE) if f.startswith("data_") and f.endswith(".py")):
    S = importlib.import_module(mod).S
    path = os.path.join(OUT, S["slug"] + ".html")
    open(path, "w", encoding="utf-8").write(build(S))
    print("  %-28s %6d bytes" % (S["slug"], os.path.getsize(path)))
