#!/usr/bin/env python3
import json
import sys
import os
import xml.sax.saxutils


def escape_xml(text):
    return xml.sax.saxutils.escape(text, {"'": "\\'", '"': '\\"'})


def convert_json_to_android_strings(input_path):
    if not os.path.exists(input_path):
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, list):
        print("Error: JSON root must be an array.", file=sys.stderr)
        sys.exit(1)

    output_dir = os.path.dirname(os.path.abspath(input_path))
    base_name = os.path.basename(input_path)
    name, _ = os.path.splitext(base_name)
    output_path = os.path.join(output_dir, f"{name}.xml")

    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append("<resources>")

    for obj in data:
        if "id" not in obj:
            print("Error: Each object must contain an 'id' field.", file=sys.stderr)
            sys.exit(1)

        obj_id = obj["id"]
        for key, value in obj.items():
            if key == "id":
                continue
            content = str(value) if value is not None else ""
            escaped_content = escape_xml(content)
            line = f'    <string name="{key}_{obj_id}">{escaped_content}</string>'
            lines.append(line)

    lines.append("</resources>")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated: {output_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python json_to_android_strings.py <input.json>", file=sys.stderr)
        sys.exit(1)

    convert_json_to_android_strings(sys.argv[1])


if __name__ == "__main__":
    main()
