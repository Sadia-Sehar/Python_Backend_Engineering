# =====To-Do List Manager=====
print("\n===To-Do List Manager===\n")

def add_task(tasks,new_task,priority):
    if priority=="y":
        tasks.insert(0,new_task)
    else:
        tasks.append(new_task)
    print("Task added to the list!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for index,task in enumerate(tasks,start=1):
        print(f"{index}. {task}")

def mark_done(tasks,done_task):
    if 1<=done_task<=len(tasks):
        removed=tasks.pop(done_task-1)
        print(f"Completed: {removed}")
        print(f"Remaining tasks: {len(tasks)}")
    else:
        print("Invalid task number!")


def start():
    tasks=[]
    while True:
        print("Menu:\n1. Add Task\n2. View Tasks\n3. Mark Done\n4. Quit")
        choice=input("Enter your choice: ")
        if choice=="1":
            new_task=input("Enter new task: ").strip()
            if not new_task:
                print("Empty task not allowed!")
                continue
            priority=input("High priority? y/n: ").lower()
            while priority not in ("y","n"):
                priority=input("Enter y or n: ").lower()
            add_task(tasks,new_task,priority)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            done=int(input("Enter task number to mark as done: "))
            mark_done(tasks,done)
        elif choice=="4":
            print(f"Goodbye! Stay productive")
            break
        else:
            print("Invalid option!")
    

start()            

