import json

def show_options():

    print("- Type what do you want to see:")
    print("1 - Tasks")
    print("2 - Calendary")
    print("3 - Teams")

def list_tasks():

    print("Tasks listed")
    with open("data.json", "r") as file:
        content = file.read()

    content = json.loads(content)

    for task_name in content['task']:
        name = task_name["name"]
        print(f"- {name}")

   

def add_tasks():

    print("Task added")

def remove_tasks():

    print("Task removed")

def done_task():

    print("Task done")

