from jasper.utils import save_config



def register(subparsers):
    parser = subparsers.add_parser("init", help="Initialize jasper CLI with your info")
    parser.set_defaults(func=run)

def run(args):
    student_id = input("Enter your Student ID: ")
    server_url = input("Enter grading server URL (default http://localhost:3000): ") or "http://localhost:3000"
    config = {
        "student_id": student_id,
        "server_url": server_url
    }
    save_config(config)
    print("✅ Config saved to jasper/config.json")
