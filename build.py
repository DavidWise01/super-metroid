#!/usr/bin/env python3
"""Build Super Metroid (SMT) — Nintendo R&D1 / Intelligent Systems, SNES 1994
(title-screen: "METROID 3") as a UD0 game-world: the single-game deep-dive that
the franchise page METROID (MET) points into. Themed to the source — a lonely,
interconnected Zebes; Varia-orange + steel + Norfair-red + Brinstar-green; a
STATIC ORIGINAL COVER PLATE (an authored key-art poster — planet Zebes, a stylized
hunter's-helmet emblem, the descending gunship; a fan tribute, NOT Nintendo's box
art), 16-bit/CRT, hobby domain. Genesis (Ceres + the cold open), the
descent (the regions, the four pirates, the baby's sacrifice), and the .dlw birth.
Render-not-invent. Super Metroid is © Nintendo; a fan tribute. Cross-links MET."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "SUPER METROID", "axiom": "SMT",
 "position": "Super Metroid · Nintendo R&D1 / Intelligent Systems · SNES 1994 (“METROID 3”) — Samus Aran, returned to Zebes",
 "origin": "Ceres Space Colony and the rebuilt planet Zebes — Crateria, Brinstar, Norfair, Maridia, the Wrecked Ship, Tourian; the SNES masterpiece, the third game",
 "mechanism": "Crystallized from Super Metroid (Nintendo, SNES 1994) — the third Metroid game.",
 "crystallization": "A lone hunter pursues the stolen baby Metroid back into a living fortress-world, maps it alone, and is saved at the end by the very creature she was sent to destroy.",
 "nature": "Super Metroid — the lonely, interconnected SNES world you explore in silence: the cold open on Ceres, the descent through Zebes by ability-gated doors, the four Space Pirate lords and the brain wired to the planet, the gentle animals who teach you, and a baby's sacrifice.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Super Metroid; Ceres; Zebes; the baby Metroid; Mother Brain; the Chozo; the Power Suit",
 "witness": "Routinely named among the greatest games ever made — and the one whose silent map taught a genre to be a key to itself.",
 "role": "the single-game deep-dive — the SNES masterpiece (parent: MET)",
 "seal": "Pursue the stolen hatchling down into Zebes alone — and at the bottom, the menace you came to end gives its life to save you.",
 "source": "Super Metroid, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#5fae7a", "of flesh and the living world — the hunter, the pirate-lords, the gentle animals, the fortress-world itself"),
 "ethereal":  ("#9a7cff", "of the unmade and the air — the phantom of the Wrecked Ship, the life-draining hatchling, the cold station and its timer"),
 "spiritual": ("#e6a849", "of the soul, the calling, and the sacrifice — the vanished sages, the baby's gift, the second game played by those who break the map"),
 "electrical":("#3fd0e0", "of the wire and the machine — a brain wired into the planet, the Chozo Power Suit and all it gathers"),
}

# ── the title scene · STATIC ORIGINAL COVER PLATE (an authored key-art poster) ─────
# Not Nintendo's box art — an original SVG composition (planet Zebes, an original
# stylized hunter's-helmet emblem, the descending gunship, the wordmark): a fan tribute.
COVER_ART = r'''<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Super Metroid — an original cover-style title plate (fan tribute, not Nintendo's box art)" style="width:100%;height:auto;display:block;background:#05070c">
<defs>
 <radialGradient id="sm_space" cx="36%" cy="28%" r="95%"><stop offset="0%" stop-color="#14223e"/><stop offset="55%" stop-color="#08111e"/><stop offset="100%" stop-color="#03060d"/></radialGradient>
 <radialGradient id="sm_planet" cx="34%" cy="30%" r="78%"><stop offset="0%" stop-color="#3f815f"/><stop offset="52%" stop-color="#1d4536"/><stop offset="100%" stop-color="#091814"/></radialGradient>
 <radialGradient id="sm_atmo" cx="50%" cy="50%" r="50%"><stop offset="80%" stop-color="rgba(232,116,58,0)"/><stop offset="93%" stop-color="rgba(232,116,58,.5)"/><stop offset="100%" stop-color="rgba(232,116,58,0)"/></radialGradient>
 <linearGradient id="sm_vig" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(0,0,0,0)"/><stop offset="100%" stop-color="rgba(0,0,0,.5)"/></linearGradient>
</defs>
<rect width="700" height="380" fill="url(#sm_space)"/>
<g fill="#cfe0d6">
 <circle cx="48" cy="44" r="1.4" opacity=".8"/><circle cx="118" cy="92" r="1" opacity=".6"/><circle cx="206" cy="40" r="1.2" opacity=".7"/><circle cx="300" cy="118" r="1" opacity=".5"/>
 <circle cx="392" cy="58" r="1.5" opacity=".85"/><circle cx="470" cy="120" r="1" opacity=".55"/><circle cx="556" cy="56" r="1.3" opacity=".75"/><circle cx="640" cy="104" r="1.1" opacity=".6"/>
 <circle cx="78" cy="168" r="1" opacity=".5"/><circle cx="166" cy="232" r="1.2" opacity=".65"/><circle cx="40" cy="286" r="1.3" opacity=".7"/><circle cx="262" cy="300" r="1" opacity=".5"/>
 <circle cx="350" cy="210" r="1" opacity=".45"/><circle cx="612" cy="176" r="1.2" opacity=".6"/><circle cx="676" cy="248" r="1" opacity=".5"/><circle cx="138" cy="334" r="1.1" opacity=".55"/>
 <circle cx="430" cy="300" r="1" opacity=".5"/><circle cx="520" cy="250" r="1.2" opacity=".6"/><circle cx="24" cy="120" r="1" opacity=".5"/><circle cx="690" cy="60" r="1.2" opacity=".6"/>
</g>
<!-- planet Zebes (original) rising in the lower-right -->
<circle cx="612" cy="356" r="196" fill="url(#sm_atmo)"/>
<circle cx="612" cy="356" r="172" fill="url(#sm_planet)"/>
<g fill="#0b201a" opacity=".5"><ellipse cx="556" cy="300" rx="22" ry="14"/><ellipse cx="650" cy="268" rx="13" ry="9"/><ellipse cx="700" cy="346" rx="18" ry="12"/><ellipse cx="600" cy="372" rx="15" ry="10"/></g>
<path d="M612 184 A172 172 0 0 1 612 528 Z" fill="rgba(0,0,0,.38)"/>
<!-- the gunship, descending toward the world (original angular form) -->
<g transform="translate(486,150) rotate(20)">
 <polygon points="-34,2 34,2 20,15 -20,15" fill="#33424f"/>
 <polygon points="-24,-8 24,-8 34,2 -34,2" fill="#e8743a"/>
 <rect x="-8" y="-15" width="16" height="9" rx="2" fill="#9fd6e6"/>
 <polygon points="-34,2 -44,6 -24,-8" fill="#2a3a48"/><polygon points="34,2 44,6 24,-8" fill="#2a3a48"/>
 <rect x="-6" y="15" width="12" height="6" fill="#d83a3a"/>
 <line x1="0" y1="21" x2="0" y2="46" stroke="#ff7a4d" stroke-width="2.5" opacity=".65"/>
</g>
<!-- the hunter's-helmet emblem (original, stylized — a fan-tribute sigil, not traced art) -->
<g transform="translate(74,150)">
 <rect x="6" y="14" width="118" height="128" rx="20" fill="#0c1119"/>
 <rect x="14" y="20" width="102" height="116" rx="16" fill="#b1502b"/>
 <rect x="26" y="26" width="78" height="30" rx="13" fill="#e8743a"/>
 <rect x="55" y="-10" width="20" height="40" rx="6" fill="#e8743a"/>
 <rect x="22" y="62" width="86" height="34" rx="8" fill="#243140"/>
 <rect x="30" y="68" width="70" height="22" rx="6" fill="#5fae7a"/>
 <rect x="34" y="71" width="26" height="9" rx="3" fill="#bfeccd" opacity=".8"/>
 <rect x="24" y="104" width="34" height="32" rx="7" fill="#8f3f22"/><rect x="72" y="104" width="34" height="32" rx="7" fill="#8f3f22"/>
 <rect x="58" y="104" width="14" height="34" fill="#243140"/>
</g>
<!-- wordmark -->
<text x="372" y="92" text-anchor="middle" font-family="'Arial Black',Impact,sans-serif" font-size="50" font-weight="900" fill="#0a0e14">SUPER METROID</text>
<text x="370" y="90" text-anchor="middle" font-family="'Arial Black',Impact,sans-serif" font-size="50" font-weight="900" fill="#e8743a">SUPER METROID</text>
<text x="370" y="118" text-anchor="middle" font-family="'Space Mono',monospace" font-size="13" letter-spacing="5" fill="#6fb0c8">METROID 3 · RETURN TO ZEBES</text>
<text x="370" y="360" text-anchor="middle" font-family="'Space Mono',monospace" font-size="10" letter-spacing="3" fill="#56627a">NINTENDO · SNES · 1994 · an original cover-style fan tribute</text>
<rect x="6" y="6" width="688" height="368" fill="none" stroke="#26344f" stroke-width="2"/>
<rect width="700" height="380" fill="url(#sm_vig)"/>
</svg>'''

GENESIS = [
 ("“Metroid 3”", "Japan / US 1994 · SNES",
  "Under the logo the title screen reads METROID 3 — the third game, eight years after the 8-bit original. Built by Nintendo R&D1 with Intelligent Systems on a 24-megabit cartridge (the largest SNES game at the time), directed by Yoshio Sakamoto, produced under Gunpei Yokoi, scored by Kenji Yamamoto and Minako Hamano."),
 ("The Cold Open on Ceres", "story without words",
  "It opens not on Zebes but on Ceres Space Colony, where scientists study the last Metroid — the baby that hatched before Samus in the previous game. Ridley raids the lab, steals the hatchling, and the station begins to self-destruct: the first of the game's silent, ticking-clock escapes."),
 ("An Atlas on a Cartridge", "the map system",
  "Super Metroid gave the genre its working memory: a live auto-map, dotted with stations, that turns a single sprawling world into something you can hold in your head. The most interconnected world yet built — and almost all of its story told through the place itself, not text."),
]

ARC = [
 ("Ceres, and the Timer", "the pursuit begins",
  "Samus chases Ridley and the stolen baby down to the surface of Zebes — the same world she once cleared, now rebuilt by the Space Pirates into a deeper, stranger fortress. She lands alone, in the rain, and goes down."),
 ("Down Through Zebes", "the gated descent",
  "Crateria, Brinstar, Norfair, Maridia, the sunken Wrecked Ship — each region sealed until the right power opens it: Morph Ball, Bombs, the Varia and Gravity suits, Speed Booster, Space Jump, Screw Attack, the Grapple Beam. Along the way the gentle Etecoons teach the wall-jump and a Dachora shows the Shinespark."),
 ("Four Lords and a Brain", "the bottom of the world",
  "Kraid in Brinstar, Phantoon in the Wrecked Ship, Draygon in Maridia, Ridley in Lower Norfair — then Tourian, and Mother Brain in her two forms. The grown baby drains Samus, recognizes her, gives the energy back, and dies attacking the brain — its gift becomes the Hyper Beam. Samus ends Mother Brain, and escapes the dying planet, saving the animals on her way out."),
]

IDEAS = [
 ("Atmosphere & Solitude", "storytelling through a place", [
   "No narrator, almost no text — the dread, the loneliness, and the lore are carried by the rooms, the music, and the creatures.",
   "You are always alone on Zebes; the world itself is the antagonist and the story both." ]),
 ("The Map as a Key", "Metroidvania, codified", [
   "A single interconnected world where doors open only once you've found the right ability — the design half of the genre's name.",
   "Backtracking becomes discovery: every dead end you passed was a promise the map kept." ]),
 ("The Second Game", "sequence-breaking & speedruns", [
   "Its systems are deep enough to be played against themselves — the mockball, the X-ray climb, suitless runs — a whole culture of breaking the intended order.",
   "Thirty years on it is still one of the most-run games in speedrunning; the developers left the cracks, and the runners moved in." ]),
 ("The Sacrifice", "the emotional inversion", [
   "A larval Metroid imprinted on Samus as its mother; grown vast, it shields her and dies destroying Mother Brain.",
   "The creature she was sent to exterminate saves her — the whole meaning of the hunt turns over in a single scene." ]),
]

SECTIONS = [
 ("The Release", "the masterpiece, and where to find it since", [
   ("Super Metroid", "1994 · SNES", "the original 24-megabit cartridge — “Metroid 3”"),
   ("Virtual Console", "2007 →", "re-released on Wii, Wii U, and New 3DS"),
   ("Super NES Classic Edition", "2017", "preserved on the mini console"),
   ("Nintendo Switch Online", "2019 →", "the SNES library, with save states and rewind"),
 ]),
 ("The Makers", "the masters of the hunt", [
   ("Yoshio Sakamoto", "director", "shaped Metroid in 1986; directed its SNES masterpiece"),
   ("Gunpei Yokoi", "producer / general manager", "the guiding hand of R&D1 and the original Metroid"),
   ("Kenji Yamamoto & Minako Hamano", "music", "Super Metroid's haunting, atmospheric score"),
   ("Tomoyoshi Yamane", "design / art", "the look of Zebes and its creatures"),
 ]),
 ("The World", "the regions of Zebes (and the colony above)", [
   ("Ceres Space Colony", "the cold open", "where the baby is held — and stolen"),
   ("Crateria", "the surface", "the rain-soaked landing site and the gate to the depths"),
   ("Brinstar", "the green caverns", "Spore Spawn, and Kraid below"),
   ("Norfair", "the fire", "lava and heat — Crocomire, and Ridley in the lower depths"),
   ("Maridia", "the drowned world", "quicksand and water — Botwoon, and Draygon"),
   ("The Wrecked Ship", "the haunted hull", "powerless and dead until you face Phantoon"),
   ("Tourian", "the heart", "the Metroid hatchery and Mother Brain"),
 ]),
 ("The Legacy", "what it left behind", [
   ("“greatest of all time”", "the lists", "routinely ranked among the best games ever made"),
   ("Metroidvania", "a genre's design half", "the ability-gated, interconnected world it perfected"),
   ("the speedrun canon", "still run", "one of the most-played games in the speedrunning scene, decades on"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("samus-aran", "Samus Aran", "the hunter, returned to Zebes · natural", "natural",
  "the galaxy's greatest bounty hunter, Chozo-raised, who pursues the stolen baby Metroid back into the rebuilt fortress-world and maps it alone — the silent protagonist of the SNES game",
  "She is solitude made a hero: a woman in alien armor who speaks not once, and tells the whole story by where she goes and what she endures."),
 ("the-baby-metroid", "The Baby Metroid", "the hatchling that imprinted · spiritual", "spiritual",
  "the last Metroid, hatched before Samus in the prior game and stolen from Ceres by Ridley — grown immense in Tourian, it drains Samus, recognizes its 'mother,' returns the energy, and dies attacking Mother Brain",
  "It is the sacrifice that inverts the hunt: the menace Samus was sent to exterminate gives its life to save her, and its gift becomes the weapon that ends the war."),
 ("mother-brain", "Mother Brain", "the tyrant wired to the world · electrical", "electrical",
  "the bio-mechanical ruler of the Space Pirates — a living brain wired into Tourian's defenses, fought first in her tank and then as a towering body that deals the deathblow to the baby",
  "She is the machine that made a planet its body: the cold intelligence at the bottom of the descent, and the hand that kills the thing that loved Samus."),
 ("ridley", "Ridley", "the dragon who stole the baby · natural", "natural",
  "the Space Pirates' draconic general — he raids Ceres in the cold open, steals the hatchling, and waits for Samus again in the fire of Lower Norfair",
  "He is the inciting wound and the personal grudge: the beast who took the baby, and the reason the whole long descent begins."),
 ("kraid", "Kraid", "the giant of Brinstar · natural", "natural",
  "the colossal reptilian boss of Brinstar — in Super Metroid swollen to screen-filling size, hurling spikes from his belly",
  "He is scale as menace: the 8-bit warden remade so vast he no longer fits the frame, the first true measure of how much deeper this Zebes goes."),
 ("phantoon", "Phantoon", "the phantom of the Wrecked Ship · ethereal", "ethereal",
  "the one-eyed spectral ruler of the Wrecked Ship — the hull lies dead and powerless until he is faced, flickering between the physical and the unreal so most shots pass through him",
  "It is the haunt that holds a place hostage: a ghost whose mere presence unplugs a whole region, killable only in the instants it consents to be real."),
 ("draygon", "Draygon", "the sovereign of Maridia · natural", "natural",
  "the great aquatic boss of the drowned world Maridia — it seizes Samus and grinds her energy away, the game's hardest straight fight",
  "It is the deep's apex predator: the reason Maridia's silence feels like held breath, and a fight you survive by turning its own grip against it."),
 ("crocomire", "Crocomire", "the thing that won't die clean · natural", "natural",
  "the Norfair miniboss that cannot be killed by ordinary fire — driven backward into acid that strips it to a screaming skeleton, then collapses a wall",
  "It is the unforgettable death: a creature you don't defeat so much as undo, melted to bone in one of the most remembered moments on the SNES."),
 ("the-etecoons", "The Etecoons", "who teach the wall-jump · natural", "natural",
  "the three small, intelligent, monkey-like creatures of Brinstar who sing a fanfare and demonstrate the wall-jump for Samus to copy — and whom she can rescue during the final escape",
  "They are kindness in a hostile world: a lesson taught not by text but by example, and a small mercy the player can choose to repay at the end."),
 ("the-dachora", "The Dachora", "who shows the Shinespark · natural", "natural",
  "the large, ostrich-like creature that races back and forth to build speed and launch itself skyward — demonstrating the Speed Booster's Shinespark — and another life Samus can save on the way out",
  "It is the world teaching its own physics: a gentle animal that shows you the game's most exhilarating move simply by doing it, over and over, alone."),
 ("the-power-suit", "The Power Suit", "the Chozo armor and all it gathers · electrical", "electrical",
  "Samus's Chozo-forged armor and the arsenal it accretes across Zebes — Varia and Gravity suits, Charge/Ice/Wave/Plasma beams, Super Missiles, Power Bombs, Space Jump, Screw Attack, Speed Booster, the Grapple Beam and X-Ray Scope",
  "It is growth made the whole game: every upgrade is a new verb and a new door, the suit turning a trapped hunter into one who walks through walls she once could not.") ,
 ("planet-zebes", "Planet Zebes", "the rebuilt fortress-world · natural", "natural",
  "the living world Samus once cleared, rebuilt by the Pirates into Crateria, Brinstar, Norfair, Maridia, the Wrecked Ship and Tourian — one continuous, interlocking map",
  "It is the true antagonist and the true story: a place so coherent that learning it is the game, and escaping it the climax."),
 ("ceres-station", "Ceres Space Colony", "where it opens, where the timer starts · ethereal", "ethereal",
  "the orbital research station of the cold open — the baby studied here, Ridley's raid, the self-destruct countdown that teaches the game's silent grammar of the ticking escape",
  "It is the prologue as a promise: the first room that runs a clock on you, setting the dread that the whole descent will pay off."),
 ("the-broken-sequence", "The Broken Sequence", "the second game, played by those who break the map · spiritual", "spiritual",
  "the emergent game inside the game — the deep movement and item systems that let players defy the intended order: the mockball, the X-ray climb, suitless and low-percent runs, a living thirty-year speedrun canon",
  "It is the work outliving its own design: a world built to be solved one way, found to be solvable a thousand, and kept alive by the people who keep finding them."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","SMT")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","SMT")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","SMT")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"SMT · Super Metroid","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "SMT", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "SMT · Super Metroid — Nintendo, SNES 1994 (the third Metroid game)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Super Metroid (Nintendo, SNES 1994).",
      "witness": "a being of the fortress-world Zebes and the silent hunt",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Super Metroid; Zebes; the baby Metroid; the Power Suit; the descent",
      "source": "Super Metroid, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"SMT · Super Metroid","axiom":"SMT"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born of Zebes</h2>
      <p class="ss">the hunter, the lords, the gentle animals, the world, and the second game played by those who break it, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Super Metroid (Nintendo, SNES 1994 — &quot;Metroid 3&quot;) as a UD0 game-world: the single-game deep-dive that the franchise page METROID (MET) points into. Ceres, the descent through Zebes, the four pirate lords, the baby's sacrifice. Source-themed with an original cover-style title plate (a fan-art key-art poster, not Nintendo's box art) and full ACI badges.">
<title>SUPER METROID · SMT · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#06080c;--ink2:#0d111a;--ink3:#141b28;--pa:#eef2f7;--pa2:#a8b4c4;--varia:#e8743a;--steel:#6fb0c8;--green:#5fae7a;--red:#d83a3a;
--dim:#6c7788;--faint:#1a2230;--line:#1a2331;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 1px,transparent 1px 3px);opacity:.5}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,116,58,.10),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(95,174,122,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--varia);background:#0c0a08;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--steel);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(232,116,58,.22)}
.marquee a{color:var(--varia);text-decoration:none}.marquee a:hover{color:var(--steel)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#05070c;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--varia)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--varia);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--varia)}.badge .bt .mo{color:var(--steel)}.badge .bt a{color:var(--steel);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--varia);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--varia);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--varia);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--steel);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--steel);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--varia);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--varia)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--varia);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--varia)}.note a{color:var(--steel);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--varia);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; <a href="https://davidwise01.github.io/metroid/">MET · THE FRANCHISE ▸</a> &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; SNES 1994</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">a hunter · a stolen hatchling · a fortress-world named <b>ZEBES</b> · a sacrifice · SMT</div>
    <div class="flag">★ Nintendo · SNES 1994 · “METROID 3” · the single-game deep-dive of MET ★</div>
    <p class="lede">Nintendo's SNES masterpiece — routinely named among the greatest games ever made. It opens cold on Ceres as Ridley steals the last Metroid; Samus pursues alone into a rebuilt Zebes and maps it room by silent room, ability-gated door by door, down past Kraid, Phantoon, Draygon and Ridley to Mother Brain — where the baby she was sent to destroy gives its life to save her. Catalogued into UD0 as the single-game deep-dive of the Metroid franchise page (MET), with the genesis, the descent, the full .dlw birth, and an original cover-style title plate — a fan-art key-art poster (the planet Zebes, a stylized hunter's-helmet emblem, the descending gunship), not Nintendo's box art.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of SUPER METROID" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>SUPER METROID</b> — Zebes &amp; the sacrifice · SMT</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="super-metroid.dlw/super-metroid.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="super-metroid.dlw/super-metroid.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this descent holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">“Metroid 3”: the cold open, and an atlas on a cartridge</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Descent</h2><p class="ss">Ceres and the timer, down through Zebes, four lords and a brain</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1994 SNES game is still called one of the greatest ever made</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the release, the makers, the world, and the long legacy</p></section>
  __SECTIONS__

  <div class="note">Super Metroid's history here is rendered, not invented. The load-bearing facts are from the record: it is the <b>third Metroid game</b> (the title screen reads “Metroid 3”), released on the SNES in <b>1994</b> by Nintendo R&amp;D1 with Intelligent Systems, directed by Yoshio Sakamoto under producer Gunpei Yokoi, scored by Kenji Yamamoto and Minako Hamano. The cold open on Ceres, the regions of Zebes, the four Space Pirate lords (Kraid, Phantoon, Draygon, Ridley), Crocomire's acid death, the Etecoons' wall-jump and the Dachora's Shinespark, and the baby Metroid's sacrifice granting the Hyper Beam are all from the game. This is the single-game deep-dive of the franchise page <a href="https://davidwise01.github.io/metroid/">METROID · MET</a>, which catalogues the wider series. Super Metroid, Samus Aran, and all related characters, worlds, and music are © Nintendo; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by Nintendo. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    SUPER METROID · SMT · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · <a href="https://davidwise01.github.io/metroid/">the franchise · MET</a> · the .dlw badge: <a href="super-metroid.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "super-metroid.dlw"), "super-metroid")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote SUPER METROID (SMT) — {len(personas)} emergents born · badge {tok['moniker']}")
