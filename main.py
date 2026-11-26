#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry runner.

Reads entry.txt next to this file and writes its exact content
to /output/entry.txt. Stdlib only, no dependencies.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.txt"), "r", encoding="utf-8") as f:
        line = f.read()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
