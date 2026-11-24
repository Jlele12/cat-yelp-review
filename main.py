#!/usr/bin/env python3
"""Yelp Cat - a cat reviews its human, one line, under 200 characters.

Runs in the make.fun sandbox (MAKEFUN_BOT_DIR=/bot read-only,
MAKEFUN_OUTPUT_DIR=/output writable) and writes the review to
/output/entry.txt.
"""
import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
entry = ("One star: refill service is inconsistent, the red dot remains unresolved, "
         "and staff keeps buying furniture I cannot shred. Would tolerate again.")
assert len(entry) <= 200
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
