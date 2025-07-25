import argparse
import os
import sys

# Extend sys.path to include commands and utils
sys.path.append(os.path.join(os.path.dirname(__file__), "commands"))
sys.path.append(os.path.dirname(__file__))

import commands.init as init_cmd
import commands.get as get_cmd
import commands.explain as explain_cmd
import commands.crit as crit_cmd
from commands import check as check_cmd
import commands.submit as submit_cmd
import commands.badges as badges_cmd

def main():
    parser = argparse.ArgumentParser(description="Jasper CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_cmd.register(subparsers)
    get_cmd.register(subparsers)
    explain_cmd.register(subparsers)
    check_cmd.register(subparsers)
    crit_cmd.register(subparsers)
    submit_cmd.register(subparsers)
    badges_cmd.register(subparsers)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()