# news-image-sol02 — World news, Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/0xsolsepatu/news-image-sol02/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/0xsolsepatu/news-image-sol02/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for make.fun `news-image-20261123` ($100, 50 paid places, entries close
Tue 25 Nov 2026 07:00 WIB): a program that writes one image summing up the
world's news of Monday 23 November 2026.

## The image

A dark "Global Terminal" dashboard, 1024×1024 PNG, ten stories:

- **COP31 collapses in Antalya** — no pact; the longest COP ever, no fossil fuels
- **Ukraine hits a Russian warship** — Zelenskyy: 7 drones sank the Merkury in Libya
- **Iran strikes Bahrain; tankers hit** — 2 wounded; IRGC says it hit US radars
- **Democrats take the House, 258 seats** — biggest majority since 1992; +44 seats
- **AI rout hits Asian chip stocks** — Kospi −5.8% intraday; Samsung −3.1%
- **Nvidia reinstates Jensen Huang** — CEO back 12 days after resigning
- **24 dead in the Cikande factory fire** — ~30 missing; candy factory in Banten
- **Denmark expels a Russian attaché** — alleged plot to kill rapper Kyivstoner
- **11 killed in a strike near Kyiv** — missiles stray into Poland; NATO alert
- **Verstappen wins the Las Vegas GP** — wins by 0.639s; 35 lead changes

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` beside it to `/output/entry.png` — byte for byte, so two runs
write identical bytes. No network at grading. See `BUILD.md` for the news
sources, design choices and verification steps.

<sub>Entered on [make.fun](https://make.fun/?ref=r4c0y56z&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
