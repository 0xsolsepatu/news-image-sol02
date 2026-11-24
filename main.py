#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123.

Copies the pre-rendered entry.png (next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), byte for byte,
so two runs write identical bytes. Standard library only; no network.

The image is a 1024x1024 'THE WORLD IN ONE DAY' newspaper front page
summing up Monday 23 November 2026's world news: the Democrats taking
the US House with 258 seats; Ukraine's claim it sank the Russian
corvette Merkury off Libya; 11 killed in a strike on Dymer; the EU
proposing its 22nd sanctions package; Iran's strikes on Bahrain; the
AI rout in Asian chip stocks; Nvidia reinstating Jensen Huang; the
Cikande factory fire; the Vanuatu M6.5 quake; the Gaza strike that
killed 3 including UNRWA staff; US sanctions on Iran-linked exchanges;
FIFA naming the 2031 Women's World Cup hosts; plus a 10-item tail list
and a DATE CHECK box for items rejected as not 23 November (COP31's
collapse was Sunday 22 November). Rebuild of the 'Global Terminal'
dashboard entry (round 2 rank 6,862/9,643).
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        if f.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print(f"error: source is not a PNG file: {SRC}", file=sys.stderr)
            return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if _sha256(dst) != _sha256(SRC):
        print(f"error: copy verification failed: {dst}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {_sha256(dst)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
