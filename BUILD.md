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

## Rebuild — newspaper front page (24 Nov 2026)

Rebuild of the 23 Nov "Global Terminal" dashboard after round 2 ranked
it 6,862/9,643 (score 438356). Diagnosis: no pictures at all, only 10
stories vs 35–42 in competing entries, and unreadable at 300px. The new
format is a newspaper front page: masthead + 6-number stat strip, three
illustrated lead panels (flat PIL drawings, not photorealistic, no AI
imagery), a 9-card grid, a 10-item tail list, a DATE CHECK box, a world
map with numbered pins and a UTC timeline. 22 verified stories in total.

### Date corrections found during verification (all against named sources)

- **COP31 is NOT a 23 Nov story.** The collapse happened Sunday 22 Nov
  (CNN: "collapsed Sunday"; Le Monde: "On Sunday, November 22"; AP:
  "fizzled out Sunday"). The 23 Nov coverage is analysis of Sunday's
  collapse. It was the old entry's lead story and is now in the DATE
  CHECK box instead. This deviates from the rebuild brief's "keep 8 of
  10" — the brief predates this verification, and the entry's own footer
  promises every story happened or was first reported on 23 Nov.
- **"31 tanker Hormuz" is a misreading.** UKMTO logged 31 attacks in
  the Strait during OCTOBER (and ~19 in November to 18 Nov), not 31
  tankers on 23 Nov. The old entry correctly stated no count; the new
  entry uses no 23 Nov tanker count either. The stat strip's "31" was
  replaced with "60 banks in EU plan", and the tail says "31 in Oct".
- **Verstappen's Las Vegas GP win was 22 Nov** (AP) — moved to DATE
  CHECK. **Alcaraz's ATP Finals win was Sunday 22 Nov** (ATP Tour) —
  DATE CHECK. **Kerch Bridge** had no verified new attack on 23 Nov
  (major attacks 16–19 Nov) — NOT used. **Gold's plunge (~9%)** was the
  week ending Fri 20 Nov; on 23 Nov gold REBOUNDED >2% (Reuters) — the
  tail says so. **India 720/9** was declared 22 Nov; the 23 Nov event is
  the draw (ESPNcricinfo). **'El Chapo Isidro'** was captured Fri 20 Nov;
  the 23 Nov news is the US extradition order (Reuters).
- **EU sanctions package is a PROPOSAL** (von der Leyen statement 23 Nov
  16:35 CET; Reuters): ~60 banks off SWIFT, 70+ shadow-fleet ships —
  needs unanimous approval by 27 member states. Worded as a proposal,
  never as enacted. **Vanuatu M6.5** (USGS, 23 Nov 02:40:58 UTC):
  depth 598 km (use "~600 km"), no tsunami threat (PTWC), PAGER green,
  no casualties or damage.

### Stories and sources (all 23 Nov unless noted)

Lead: Democrats take House 258 (AP); Ukraine corvette claim (AP);
Dymer 11 killed (Reuters). Grid: EU sanctions proposal (EC/Reuters);
Iran strikes Bahrain (Reuters); AI rout Kospi −3.3% (Reuters); Nvidia
+31% (Reuters); Cikande 24 dead ~30 missing (Reuters); Vanuatu M6.5
(USGS); Gaza strike kills 3 incl. UNRWA staff (Reuters); US sanctions
Iran exchanges, $290B demand (Reuters); FIFA 2031/2035 hosts
(Reuters). Tail: NATO AWACS (Reuters); El Chapo Isidro extradition
(Reuters); Grok lawsuit (Reuters/AP); gold rebound (Reuters); India
720/9 draw (ESPNcricinfo); CrowdStrike–Zscaler ~$43.9B (Reuters);
India $1.6B Nepal package (BBC); UK Myanmar sanctions (BBC); Hormuz
UKMTO October count (UKMTO via ABC); Denmark expels attaché (AP).
DATE CHECK: COP31 (CNN/AP, 22 Nov); Verstappen GP (AP, 22 Nov);
Alcaraz ATP final (ATP Tour, 22 Nov); ICJ Myanmar ruling (19 Nov);
Xi–Trump–Putin summit (19 Nov); Riemann claim (unverified).

### Design notes

- Masthead "THE WORLD IN ONE DAY" at 66pt Serif Bold — 90pt measures
  1303px, wider than the canvas; 66pt is the largest that fits one line
  inside the 984px content width. Date "MONDAY 23 NOVEMBER 2026" at
  38pt. Stat numbers 30pt, main titles 26pt, decks 15pt, tail 14pt.
- Illustrations are hand-drawn flat PIL shapes: Capitol dome, ship +
  drones, rubble + ladder. Grid cards carry region tags, a
  CLAIM/REPORTED/CONFIRMED/PROPOSAL chip and a source line.
- Map: very rough continent shapes with 6 numbered pins (Washington,
  Libya, Kyiv, Bahrain, Cikande, Vanuatu). Timeline: 00:00–24:00 UTC
  axis with the two verified times (02:40 Vanuatu quake, 15:35 EU
  sanctions proposal); no other times were invented.

### Verification (this session)

- `entry.png`: **1024×1024, 176,764 bytes** (limit 1,048,576),
  sha256 `69e08f5592678d694c39e15bbf4be9e5e2005020b748b1924ee459e8977423fc`.
- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/outA and /tmp/outB)
  after each of the two edits (docstring rewrite; PNG magic validation):
  **both outputs byte-identical** to entry.png — same sha256 as above.
  Syntax OK. The program is unchanged in behaviour on a valid PNG.
- Read back at full size and at 300px: masthead, date, all 6 stat
  numbers and all 3 lead titles are clearly readable at 300px; no
  overlap or truncation anywhere (render script prints 0 issues; every
  text block is bounds-checked). Grid titles and the tail list are small
  at 300px — they are density for the full-size view, as in a real
  newspaper; the required 300px elements (masthead, date, lead titles,
  stat numbers) all pass.
- Map at 300px reads as a small tan map with red dots — borderline but
  kept: it is a minor decorative element, the pins are visible as dots,
  and it does not hurt the legibility of the required elements.
- Kit check (`makefun check` from the kit dir) — run after the rebuild;
  see the check output in the parent's submission flow (expected:
  4 passed, 1 failed transcripts_present — parent bundles transcripts).

## Files for commit

render.py (build tool, NOT for commit), entry.png, main.py, LICENSE (MIT,
kit starter), README.md, BUILD.md, GEMINI-DESIGN.md,
gemini-design-prompt.txt, gemini-design-response.txt (parent-supplied).
