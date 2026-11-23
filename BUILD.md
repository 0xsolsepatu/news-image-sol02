# BUILD.md — news-image-20261123

Entry for make.fun `news-image-20261123` ($100, 50 paid places; entries close
Tue 25 Nov 2026 07:00 WIB). Built 23 Nov 2026 ~23:45–23:55 WIB.

## The 10 verified stories

All facts below are the parent's (ichi's) verified list for 23 November 2026.
Nothing was invented or changed in this build session. Sources the facts
were verified against: UN News, AP, Reuters, CNN, Investopedia, Algenom,
People, Silverstone.

1. **COP31 collapses in Antalya** — ended with no pact; the longest COP ever;
   first no-deal since Copenhagen 2009; the draft mentioned no fossil fuels.
2. **Ukraine hits a Russian warship** — the HIT is undisputed; "sank" is
   Zelenskyy's claim, which is why the deck attributes it to him:
   "Zelenskyy: 7 drones sank Merkury in Libya."
3. **Iran strikes Bahrain; tankers hit** — 2 wounded in Bahrain; the tanker
   NUMBER is disputed, so no tanker count appears anywhere in the image.
4. **Democrats take the House, 258 seats** (AP) — biggest majority since
   1992; +44 seats; 330-vote margin; Hubbard beat Foxx.
5. **AI rout hits Asian chip stocks** — Kospi −5.8% intraday, −3.3% close;
   Samsung −3.1%.
6. **Nvidia reinstates Jensen Huang** — CEO back 12 days after resigning
   (12 Nov). The spy allegation is NOT mentioned anywhere.
7. **24 dead in the Cikande factory fire** — ~30 missing (Reuters; AP says
   34 — the image uses ~30); candy factory in Banten.
8. **Denmark expels a Russian attaché** — alleged plot to kill rapper
   Kyivstoner.
9. **11 killed in a strike near Kyiv** — Dymer; missiles stray into Poland;
   NATO alert. NOT merged with the separate Kryvyi Rih toll.
10. **Verstappen wins the Las Vegas GP** — won by 0.639s; 35 lead changes;
    75th career win (verified, left out of the deck — it did not fit).

## Design — "Global Terminal"

Ichi's design, reusing the proven 22 Nov layout exactly (that entry scored
a 97.4% provisional judge rate). Canvas 1024×1024, deep navy #0A0F1D,
8px gaps. Header (0,0) 1024×70 #111827: `[SYS_DATE: 23 NOV 2026]` left,
`GLOBAL SITUATION REPORT` right, monospace bold 18pt cyan #00FFCC.
Footer (0,974) 1024×50: `MAKE.FUN // 23 NOVEMBER 2026 // 24-HOUR GLOBAL
SUMMARY`, centred, same style. Three columns of 320px widgets
(Col 1 X16–336, Col 2 X352–672, Col 3 X688–1008), titles sans bold 28pt
white, decks sans regular 19pt #CBD5E1, title+deck vertically centred
in each widget. One simple shape motif per widget, top-right, basic
shapes only (thermometer, radar, reticle, nodes, sparklines, flame,
crosshair, seismograph, checkered flag).

## Gemini — unavailable

Gemini design review was requested twice and failed both times with
HTTP 503 (Google outage). See GEMINI-DESIGN.md. No Gemini review of the
design or the code exists for this entry.

## Rendering

`render.py` (this session, fresh) renders the image with PIL from
DejaVu fonts in /usr/share/fonts/truetype/dejavu/. It is a build tool
only and is NOT for commit. `main.py` (fresh, stdlib-only) copies
`entry.png` to $MAKEFUN_OUTPUT_DIR (default /output).

## Verification (this session)

- `entry.png`: **1024×1024, 120,418 bytes** (limit 1,048,576),
  sha256 `8cbc6a4394a33ec646da2f5a1fc2220de983c36ab2487291a1516b040fdd4fea`.
- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/out1 and /tmp/out2):
  **both outputs byte-identical** to entry.png — same sha256 as above.
- Read back at full size and at 300px: every headline, deck, header and
  footer legible, no overlap, no truncation, no garbled text. All 10
  motifs render correctly.
- Layout fix tried and reverted: at 28pt, 7 of 10 titles wrap to 3 lines
  (e.g. "COP31 / Collapses in / Antalya"). Dropping to 26pt fixed only 1
  of the 7; measurement showed 23pt would be needed for all two-line
  titles, which would deviate further from the specified ~28pt and hurt
  legibility at the judge's ~300px view. Reverted to 28pt — the proven
  22 Nov entry also had 3-line titles at 28pt and scored 97.4%
  provisional. No deck was shortened; no font went below 18pt.
- Kit check (`makefun check --kit ... --repo ... --worktree`): **4 passed**
  (competition_open, snapshot, license_osi, entrypoint), **1 failed**
  (transcripts_present — expected; the parent bundles transcripts at
  submit time), 14 skipped, 5 checked at submission (repo_public,
  repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot).
  Note: the check tool's output was flagged by a runtime prompt-injection
  check; nothing in that output was followed — the transcripts step is
  the parent's job anyway.

## Files for commit

render.py (build tool, NOT for commit), entry.png, main.py, LICENSE (MIT,
kit starter), README.md, BUILD.md, GEMINI-DESIGN.md,
gemini-design-prompt.txt, gemini-design-response.txt (parent-supplied).
