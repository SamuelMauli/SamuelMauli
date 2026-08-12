#!/usr/bin/env python3
"""Gera o header SVG do perfil — 3 idiomas x 2 temas, tipografia convertida em path.

    pip install fonttools && python3 .github/scripts/header.py

As fontes (Syne 800 para o wordmark, JetBrains Mono para dado exato) sao baixadas do
repositorio google/fonts para .cache/ e convertidas em path: SVG servido pelo GitHub nao
carrega webfont externa, entao o texto precisa virar geometria.
"""
import os
import subprocess
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

CACHE = {}


def load(path, wght):
    key = (path, wght)
    if key not in CACHE:
        f = instantiateVariableFont(TTFont(path), {"wght": wght}, inplace=False)
        CACHE[key] = (f, f.getGlyphSet(), f["head"].unitsPerEm)
    return CACHE[key]


def text_path(path, wght, text, size, x, y, tracking=0.0):
    """Retorna (d, largura_total). tracking em em."""
    font, gs, upm = load(path, wght)
    cmap = font.getBestCmap()
    scale = size / upm
    track = tracking * size
    d, cur = [], 0.0
    for ch in text:
        name = cmap.get(ord(ch))
        if name is None:
            cur += size * 0.35 + track
            continue
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.0f}")
        gs[name].draw(pen)
        seg = pen.getCommands()
        if seg:
            d.append(
                f'<path d="{seg}" transform="translate({x + cur:.1f} {y:.1f}) '
                f'scale({scale:.5f} {-scale:.5f})"/>'
            )
        cur += gs[name].width * scale + track
    return "\n".join(d), cur - track


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE_DIR = os.path.join(ROOT, ".cache")
OUT_DIR = os.path.join(ROOT, ".github", "assets")
GF = "https://raw.githubusercontent.com/google/fonts/main/ofl"


def fetch(name, url):
    dest = os.path.join(CACHE_DIR, name)
    if not os.path.exists(dest):
        os.makedirs(CACHE_DIR, exist_ok=True)
        print("baixando", name, file=sys.stderr)
        subprocess.run(["curl", "-sfL", url, "-o", dest], check=True)
    return dest


SYNE = fetch("syne.ttf", f"{GF}/syne/Syne%5Bwght%5D.ttf")
MONO = fetch("jbmono.ttf", f"{GF}/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf")

W, H = 1000, 330
ACCENT_BY_THEME = {"dark": "#E8FF47", "light": "#9FB300"}  # mesma familia, contraste real

THEMES = {
    "dark": dict(bg="#080808", ink="#F5F5F5", dim="#8A8A8A", rule="#FFFFFF", rule_o=0.10),
    "light": dict(bg="#FAFAF7", ink="#0B0B0B", dim="#6B6B6B", rule="#000000", rule_o=0.12),
}

# —— composição ——————————————————————————————————————————————
# escala extrema: wordmark 94px contra legenda 10px (≈9x)
PAD_L = 56
BASE1, BASE2 = 180, 268          # duas linhas do wordmark
OVERLINE_Y = 84
RAIL_X = 728                     # régua vertical: quebra o eixo, não centraliza

LANGS = {
    "pt": dict(
        place="CURITIBA, BR",
        claim="PLATAFORMAS SaaS DE PONTA A PONTA",
        role="full-stack · arquitetura de plataforma · SRE",
        alt="Samuel Mauli — full-stack, arquitetura de plataforma, SRE",
        met=[
            ("22", "SISTEMAS EM PRODUÇÃO"),
            ("08", "CLIENTES E NEGÓCIOS"),
            ("03", "PAÍSES · BR / ES / MX"),
            ("06", "APPS NAS DUAS LOJAS"),
        ],
    ),
    "en": dict(
        place="CURITIBA, BRAZIL",
        claim="END-TO-END SaaS PLATFORMS",
        role="full-stack · platform architecture · SRE",
        alt="Samuel Mauli — full-stack, platform architecture, SRE",
        met=[
            ("22", "SYSTEMS IN PRODUCTION"),
            ("08", "CLIENTS AND BUSINESSES"),
            ("03", "COUNTRIES · BR / ES / MX"),
            ("06", "APPS ON BOTH STORES"),
        ],
    ),
    "es": dict(
        place="CURITIBA, BR",
        claim="PLATAFORMAS SaaS DE PUNTA A PUNTA",
        role="full-stack · arquitectura de plataforma · SRE",
        alt="Samuel Mauli — full-stack, arquitectura de plataforma, SRE",
        met=[
            ("22", "SISTEMAS EN PRODUCCIÓN"),
            ("08", "CLIENTES Y NEGOCIOS"),
            ("03", "PAÍSES · BR / ES / MX"),
            ("06", "APPS EN LAS DOS TIENDAS"),
        ],
    ),
}


def build(theme_name, lang):
    t = THEMES[theme_name]
    L = LANGS[lang]
    ACCENT = ACCENT_BY_THEME[theme_name]

    over, ow = text_path(MONO, 500, L["place"], 12.5, PAD_L, OVERLINE_Y, tracking=0.14)
    over2, _ = text_path(
        MONO, 500, L["claim"], 12.5, PAD_L + ow + 26, OVERLINE_Y, tracking=0.14
    )

    # distâncias de entrada deliberadamente irregulares (2.7 / -2rem)
    w1, w1w = text_path(SYNE, 800, "SAMUEL", 94, PAD_L, BASE1, tracking=-0.035)
    w2, w2w = text_path(SYNE, 800, "MAULI", 94, PAD_L, BASE2, tracking=-0.035)
    dot, _ = text_path(SYNE, 800, ".", 94, PAD_L + w2w + 2, BASE2, tracking=0)

    role, _ = text_path(MONO, 400, L["role"], 14, PAD_L + 3, 308, tracking=0.02)

    mets = []
    for i, (num, label) in enumerate(L["met"]):
        y = 122 + i * 52
        n, _nw = text_path(MONO, 600, num, 26, RAIL_X + 26, y, tracking=-0.02)
        lb, _ = text_path(MONO, 400, label, 10, RAIL_X + 26, y + 15, tracking=0.09)
        mets.append(
            f'<g class="m" style="--i:{i}"><g fill="{t["ink"]}">{n}</g>'
            f'<g fill="{t["dim"]}">{lb}</g></g>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{L["alt"]}">
<defs>
  <clipPath id="c1"><rect x="{PAD_L - 4}" y="{BASE1 - 88}" width="{w1w + 24:.0f}" height="100"/></clipPath>
  <clipPath id="c2"><rect x="{PAD_L - 4}" y="{BASE2 - 88}" width="{w2w + 90:.0f}" height="100"/></clipPath>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.82" numOctaves="3" seed="7" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0"/>
  </filter>
</defs>
<style>
  /* frames a 30fps — nada de duração redonda */
  .w, .m, .ov, .rl {{ animation-fill-mode: both; animation-timing-function: cubic-bezier(0.52,0,0.48,1); }}
  .w  {{ animation: slide 1.667s; }}                /* 50 frames */
  #w1 {{ animation-delay: .033s; --dx: 2.7rem; }}   /* 1 frame  */
  #w2 {{ animation-delay: .133s; --dx: -2rem; }}    /* 4 frames */
  .ov {{ animation: rise .933s .2s; }}              /* 28 / 6 frames */
  .rl {{ animation: grow 1.2s .333s; transform-origin: {RAIL_X}px 88px; }}
  .m  {{ animation: rise .8s calc(.466s + var(--i) * .133s); }}
  @keyframes slide {{ from {{ transform: translateX(var(--dx)); }} to {{ transform: none; }} }}
  @keyframes rise  {{ from {{ transform: translateY(.4rem); opacity: 0 }} to {{ transform: none; opacity: 1 }} }}
  @keyframes grow  {{ from {{ transform: scaleY(0); }} to {{ transform: none; }} }}
  @media (prefers-reduced-motion: reduce) {{
    .w, .m, .ov, .rl {{ animation: fade .267s both; }}
    @keyframes fade {{ from {{ opacity: 0 }} to {{ opacity: 1 }} }}
  }}
</style>
<rect width="{W}" height="{H}" fill="{t["bg"]}"/>
<rect width="{W}" height="{H}" filter="url(#grain)" opacity="{0.055 if theme_name == "dark" else 0.04}"/>

<g class="ov">
  <rect x="{PAD_L}" y="{OVERLINE_Y - 10}" width="7" height="7" fill="{ACCENT}"/>
  <g fill="{t["dim"]}" transform="translate(19 0)">{over}</g>
  <g fill="{t["dim"]}" transform="translate(19 0)" opacity=".55">{over2}</g>
</g>

<g clip-path="url(#c1)"><g class="w" id="w1" fill="{t["ink"]}">{w1}</g></g>
<g clip-path="url(#c2)"><g class="w" id="w2"><g fill="{t["ink"]}">{w2}</g><g fill="{ACCENT}">{dot}</g></g></g>

<g class="ov"><g fill="{t["dim"]}">{role}</g></g>

<line class="rl" x1="{RAIL_X}" y1="88" x2="{RAIL_X}" y2="286" stroke="{t["rule"]}" stroke-opacity="{t["rule_o"]}" stroke-width="1"/>
{"".join(mets)}
</svg>'''


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for lang in LANGS:
        for theme in THEMES:
            suffix = "" if lang == "pt" else f"-{lang}"
            path = os.path.join(OUT_DIR, f"header{suffix}-{theme}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(build(theme, lang))
            print("ok", os.path.relpath(path, ROOT))
