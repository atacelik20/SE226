tasks = {}
execution_order = []
completed_tasks = set()

num_tasks = int(input("Enter number of tasks: "))

for i in range(num_tasks):
    task_name = input("Enter task name: ")
    dep_count = int(input(f"How many dependencies for {task_name}? "))

    dependencies = []
    for j in range(dep_count):
        dep_name = input(f"Enter dependency {j + 1}: ")
        dependencies.append(dep_name)

    tasks[task_name] = dependencies

print("TASK STRUCTURE:")
for task, deps in tasks.items():
    print(f"{task} -> {deps}")

print("INITIAL TASKS (no dependencies):")
initial_tasks = []

for task, deps in tasks.items():
    if len(deps) == 0:
        initial_tasks.append(task)

if len(initial_tasks) == 0:
    print("None")
else:
    for task in initial_tasks:
        print(task)

remaining_tasks = set(tasks.keys())

while len(remaining_tasks) > 0:
    executed_in_this_round = False

    for task in tasks:
        if task not in completed_tasks:
            can_execute = True

            for dep in tasks[task]:
                if dep not in completed_tasks:
                    can_execute = False
                    break

            if can_execute:
                execution_order.append(task)
                completed_tasks.add(task)
                remaining_tasks.remove(task)
                executed_in_this_round = True

    if not executed_in_this_round:
        break


print("EXECUTION ORDER:")

if len(execution_order) == 0:
    print("No task can be started.")
else:
    for i in range(len(execution_order)):
        print(f"Step {i + 1}: {execution_order[i]}")

if len(completed_tasks) == len(tasks):
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed_tasks:
            print(task)