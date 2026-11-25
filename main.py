"""Entry for make.fun bounty "One-Line Slogan for a Solana Wallet Agent".

Entry text (draft v1): one slogan for a Solana wallet agent, at most 20 words.
Limit: 1 to 140 characters. No trailing newline is written.
"""

import os

ENTRY = "Your keys stay yours, your trades stay fast — the wallet agent that never sleeps and never fumbles."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
