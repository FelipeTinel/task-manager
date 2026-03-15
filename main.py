import argparse
import tasks_functions

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

options = subparsers.add_parser("options")

args = parser.parse_args()

if args.command == "options":
    tasks_functions.show_options()
