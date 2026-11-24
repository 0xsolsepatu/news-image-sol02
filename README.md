# news-image-sol02 — World news, Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/0xsolsepatu/news-image-sol02/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/0xsolsepatu/news-image-sol02/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for make.fun `news-image-20261123` ($100, 50 paid places, entries close
Tue 25 Nov 2026 07:00 WIB): a program that writes one image summing up the
world's news of Monday 23 November 2026.

## The image

A "THE WORLD IN ONE DAY" newspaper front page, 1024×1024 PNG — cream
paper, serif masthead, a 6-number stat strip, three illustrated lead
stories, a 9-card grid, a 10-item tail list, a DATE CHECK box and a
world map + UTC timeline. 22 verified stories from Monday 23 November
2026 (rebuild of the "Global Terminal" dashboard, round 2 rank
6,862/9,643):

Lead stories: **Democrats take the House, 258 seats** — biggest
majority since 1992; **Ukraine says it sank a Russian corvette** —
Zelenskyy: 7 sea drones sank the Merkury off Libya (Libya: badly
damaged); **11 killed in a strike on Dymer** — drone hits a 5-storey
block near Kyiv. Grid: EU proposes 22nd sanctions package; Iran
strikes Bahrain; AI rout hits Asian chips; Nvidia reinstates Jensen
Huang; Cikande factory fire, 24 dead; Vanuatu quake M6.5; Gaza strike
kills 3, including UNRWA staff; US sanctions Iran exchanges; FIFA
names 2031 World Cup hosts. Tail: NATO AWACS to Poland; US
extradition order for 'El Chapo Isidro'; Virginia & Oregon sue SpaceX
over Grok deepfakes; gold rebounds >2%; India's 720/9 ends in a draw;
CrowdStrike to buy Zscaler; India pledges $1.6B to Nepal; UK sanctions
Myanmar generals; Hormuz attacks at highest level (31 in October);
Denmark expels a Russian attaché. DATE CHECK rejects COP31's collapse
(Sunday 22 Nov), the Verstappen GP win (22 Nov), the Alcaraz ATP final
(22 Nov), the ICJ Myanmar ruling (19 Nov), the Xi–Trump–Putin summit
(19 Nov) and the Riemann Hypothesis 'proof' (unverified).

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` beside it to `/output/entry.png` — byte for byte, so two runs
write identical bytes. No network at grading. See `BUILD.md` for the news
sources, design choices and verification steps.

<sub>Entered on [make.fun](https://make.fun/?ref=r4c0y56z&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
