import os
import json
import re

def register(subparsers):
    parser = subparsers.add_parser("explain", help="Show problem description")
    parser.set_defaults(func=run)

def run(args):
    cwd = os.getcwd()
    folder_name = os.path.basename(cwd)

    match = re.match(r"^(\d+)", folder_name)
    if not match:
        print("❌ Folder name must start with problem ID (e.g., 132-hello-world)")
        return

    meta_path = os.path.join(cwd, "meta.json")
    if not os.path.isfile(meta_path):
        print("❌ meta.json not found in this folder.")
        return

    try:
        with open(meta_path, "r") as f:
            meta = json.load(f)

        print(f"📘 Problem {match.group(1)}: {meta.get('title', '(No title)')}")
        print()
        print("📝 Description:")
        print(meta.get("description", "(No description)"))
        print()
        if "badges" in meta:
            print(f"🏷️  Badges: {', '.join(meta['badges'])}")
    except Exception as e:
        print(f"❌ Failed to read meta.json: {e}")
