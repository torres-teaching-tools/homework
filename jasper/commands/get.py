import os, requests, json
from jasper.utils import load_config, save_config
from pretty import print_status

def register(subparsers):
    parser = subparsers.add_parser("get", help="Download starter code for a problem")
    parser.add_argument("query", help="Problem name or ID")
    parser.set_defaults(func=run)

def run(args):
    config = load_config()
    server_url = config.get("server_url", "http://localhost:3000")

    try:
        resp = requests.get(f"{server_url}/get-problem", params={"q": args.query})
        if resp.status_code != 200:
            print_status(f"Problem not found: {args.query}", success=False)
            return

        data = resp.json()
        folder_name = data["project_name"]

        # Find project root by locating `.devcontainer`
        root_dir = find_project_root()
        project_path = os.path.join(root_dir, folder_name)
        os.makedirs(project_path, exist_ok=True)

        # Save starter files
        for fname, content in data["files"].items():
            fpath = os.path.join(project_path, fname)
            os.makedirs(os.path.dirname(fpath), exist_ok=True)
            with open(fpath, "w") as f:
                f.write(content)

        # Save meta.json if provided
        if "meta" in data:
            meta_path = os.path.join(project_path, "meta.json")
            with open(meta_path, "w") as f:
                json.dump(data["meta"], f, indent=2)

        print_status(f"Downloaded: {folder_name}", success=True)

    except Exception as e:
        print_status(f"Error: {e}", success=False)


def find_project_root():
    """
    Traverse upward until we find the folder containing `.devcontainer`.
    Defaults to current working directory if not found.
    """
    current = os.getcwd()
    while current != os.path.dirname(current):
        if os.path.isdir(os.path.join(current, ".devcontainer")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()
