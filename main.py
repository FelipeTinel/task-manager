import argparse
import tasksfunctions as tk

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

# ================================================== #

tasks_parser = subparsers.add_parser("tasks")
tasks_sub = tasks_parser.add_subparsers(dest="tasks_command")

add = tasks_sub.add_parser("add")
add.add_argument("name")

remove = tasks_sub.add_parser("remove")
remove.add_argument("id")

list = tasks_sub.add_parser("list")

done = tasks_sub.add_parser("done")
done.add_argument("id")

# ================================================== #

options = subparsers.add_parser("options")

calendary = subparsers.add_parser("calendary")

teams = subparsers.add_parser("teams")


args = parser.parse_args()

if args.command == "options":
    tk.show_options()

if args.tasks_command == "add":
    tk.add_tasks()

if args.tasks_command == "remove":
    tk.remove_tasks()

if args.tasks_command == "list":
    tk.list_tasks()

if args.tasks_command == "done":
    tk.list_tasks()