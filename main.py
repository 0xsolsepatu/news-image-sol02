#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123.

Copies the pre-rendered entry.png (next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), byte for byte,
so two runs write identical bytes. Standard library only; no network.

The image is a 1024x1024 'Global Terminal' dashboard summing up Monday
23 November 2026's world news: COP31 collapsing in Antalya with no pact;
Ukraine's drone hit on the Russian warship Merkury off Libya; Iran's
strikes on Bahrain and tankers; the Democrats taking the US House with
258 seats; the AI rout in Asian chip stocks; Nvidia reinstating Jensen
Huang; the Cikande factory fire; Denmark expelling a Russian attache
over an alleged plot against rapper Kyivstoner; 11 killed in a strike
near Kyiv with missiles straying into Poland; and Verstappen winning
the Las Vegas Grand Prix.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
