#!/usr/bin/env python3
import re, sys, yaml

def write(path, data_obj):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data_obj, f, sort_keys=False)

def try_parse(raw, note):
    try:
        return yaml.safe_load(raw), None
    except Exception as e:
        return None, f"{note}: {e}"

def main():
    if len(sys.argv) != 3:
        print("Usage: extract_yaml.py <issue_body.txt> <out.yaml>", file=sys.stderr)
        sys.exit(2)

    body_path, out_path = sys.argv[1], sys.argv[2]
    text = open(body_path, "r", encoding="utf-8").read()

    # 1) Look for fenced blocks with explicit yaml/yml
    m = re.search(r"```y(?:a)?ml\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if m:
        raw = m.group(1).strip()
        data, err = try_parse(raw, "Invalid fenced yaml")
        if data is not None:
            write(out_path, data)
            print(f"Found fenced yaml block → {out_path}")
            return
        print(err, file=sys.stderr)
        sys.exit(1)

    # 2) Any fenced code block (``` ... ```)
    m = re.search(r"```+\s*([\s\S]*?)```+", text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        data, err = try_parse(raw, "Invalid generic fenced block parsed as YAML")
        if data is not None:
            write(out_path, data)
            print(f"Found generic fenced block → {out_path}")
            return
        # fall through; maybe it wasn't YAML

    # 3) YAML front-matter style: ---\n...\n---
    m = re.search(r"^---\s*\n([\s\S]*?)\n---\s*$", text, re.DOTALL | re.MULTILINE)
    if m:
        raw = m.group(1).strip()
        data, err = try_parse(raw, "Invalid YAML front matter")
        if data is not None:
            write(out_path, data)
            print(f"Found YAML front matter → {out_path}")
            return

    # 4) Last resort: try whole body if it *looks* like YAML (has key: value lines)
    if re.search(r"^[\w\"'].+?:\s+.+", text, re.MULTILINE):
        raw = text.strip()
        data, err = try_parse(raw, "Body is not valid YAML")
        if data is not None:
            write(out_path, data)
            print(f"Parsed whole body as YAML → {out_path}")
            return

    # 5) Couldn’t find valid YAML
    print("ERROR: No YAML found. Please paste YAML inside a fenced block like:\n"
          "```yaml\nname: example\n```\n"
          "or use front matter:\n---\nname: example\n---", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
