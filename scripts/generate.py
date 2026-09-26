#!/usr/bin/env python3
"""
Generate Hugo content pages from data/clients/*.json

Reads every JSON file in data/clients/ and writes one markdown
file per client into content/listings/<id>.md with proper
YAML-like JSON front matter.
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR  = REPO_ROOT / "data" / "clients"
OUT_DIR   = REPO_ROOT / "content" / "listings"

OUT_DIR.mkdir(parents=True, exist_ok=True)

total = 0
for json_file in sorted(DATA_DIR.glob("*.json")):
    with open(json_file, "r", encoding="utf-8") as f:
        clients = json.load(f)

    for client in clients:
        slug = client["id"]

        # Reserved keys go to the top level of front matter.
        fm = {
            "title":      client.get("name", ""),
            "draft":      False,
            "categories": [client.get("category", "")],
        }

        # Everything else goes under `params`.
        fm["params"] = {
            k: v for k, v in client.items()
            if k not in ("id", "name", "category")
        }

        out_file = OUT_DIR / f"{slug}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(fm, indent=2, ensure_ascii=False))
        total += 1

print(f"✓ Generated {total} content pages in {OUT_DIR}")
