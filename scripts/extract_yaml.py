#!/usr/bin/env python3
import re, sys, yaml

issue_body_path = sys.argv[1]
out_path = sys.argv[2]

text = open(issue_body_path, "r", encoding="utf-8").read()

# Match ```yaml ... ``` or ```yml ... ```
m = re.search(r"```y(?:a)?ml\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
if not m:
    print("ERROR: No fenced YAML block found in the issue body.", file=sys.stderr)
    sys.exit(1)

raw = m.group(1).strip()

# Basic parse to verify it’s valid YAML; also normalizes it.
try:
    data = yaml.safe_load(raw)
except yaml.YAMLError as e:
    print(f"ERROR: Invalid YAML: {e}", file=sys.stderr)
    sys.exit(1)

with open(out_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(data, f, sort_keys=False)
print(f"Wrote normalized YAML to {out_path}")
