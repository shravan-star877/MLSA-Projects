# Smart To-Do List Pro
# add, delete, view tasks
# mark tasks as completed
# add priority levels and due dates
# show motivational message when task is completed

tasks = []

def add_task(name, priority, due_date):
    tasks.append({"name": name, "priority": priority, "due_date": due_date, "done": False})

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Great job, keep going!")

def view_tasks():
    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['name']} | Priority: {task['priority']} | Due: {task['due_date']} | {status}")

# Example run
add_task("Finish homework", "High", "2026-04-25")
add_task("Buy groceries", "Medium", "2026-04-24")
view_tasks()
mark_done(0)
view_tasks()
