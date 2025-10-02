import csv


class Task():
    def __init__(self,name,description,priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.name} ({self.priority}) - {self.description}"


class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
        print()
        print(f"{task.name} has been added successfully !")
        print()
    def delete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print()
                print(f"{task.name} has been deleted successfully !")
                print()
                return
        print(f"Task with name '{task_name}' not found !")
        print()

    def show_all_tasks(self):
        if len(self.tasks) == 0:
            print("you have 0 tasks !")
            print()
        else:
            for number , task in enumerate(self.tasks , start= 1):
                print(f"{number} > {task}")
                print()

    def save_tasks(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "description", "priority"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({
                    "name": task.name,
                    "description": task.description,
                    "priority": task.priority
                })
            print(f"{filename} has been saved !")
            print()

    def load_tasks(self, filename):
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["name"], row["description"], row["priority"])
                    self.tasks.append(task)
            print(f"{filename} has been loaded !\n")
            return True 
        except FileNotFoundError:
            print(f"File {filename} not found!\n")
            return False  


todo = ToDoList()
        

def system():
    while True:
        print("+++++++++++++++++++")
        print("1.create a new file")
        print("2.load from a file")
        print("3.EXIT") 
        print("+++++++++++++++++++")
        try :
            print()
            user_file_choice = int(input("enter your choice : "))
            print()
        except ValueError:
            print("please enter a valid number !")
            print()
            user_file_choice = None
        else:
            if user_file_choice == 1:
                file_name = str(input("enter your new file's name : "))
                print()
                while True:
                    print("=====================")
                    print("1.add a task")
                    print("2.delete a task")
                    print("3.show all tasks")
                    print(f"4.save into {file_name}")
                    print("5.EXIT")
                    print("=====================")
                    print()
                    user_task_choice = int(input("enter your choice : "))
                    print()
                    if user_task_choice == 1:
                        temp_task = Task(str(input("enter a name for your task : ")),str(input("enter a description for your task : ")),str(input("enter a priority for your task (LOW,MID,HIGH) : ")))
                        todo.add_task(temp_task)
                    elif user_task_choice == 2:
                        task_name = str(input("enter the task which you want to delete : "))
                        todo.delete_task(task_name)
                    elif user_task_choice == 3:
                        todo.show_all_tasks()
                    elif user_task_choice == 4:
                        todo.save_tasks(file_name)
                    elif user_task_choice == 5:
                        todo.tasks = []
                        break
            elif user_file_choice == 2:
                file_name = str(input("enter your file's path / name : "))
                print()
                file_loaded = todo.load_tasks(file_name)
                if not file_loaded:
                    continue
                while True:
                    print("=====================")
                    print("1.add a task")
                    print("2.delete a task")
                    print("3.show all tasks")
                    print(f"4.save into {file_name}")
                    print("5.EXIT")
                    print("=====================")
                    print()
                    user_task_choice = int(input("enter your choice : "))
                    print()
                    if user_task_choice == 1:
                        temp_task = Task(str(input("enter a name for your task : ")),str(input("enter a description for your task : ")),str(input("enter a priority for your task (LOW,MID,HIGH) : ")))
                        todo.add_task(temp_task)
                    elif user_task_choice == 2:
                        task_name = str(input("enter the task which you want to delete : "))
                        todo.delete_task(task_name)
                    elif user_task_choice == 3:
                        todo.show_all_tasks()
                    elif user_task_choice == 4:
                        todo.save_tasks(file_name)
                    elif user_task_choice == 5:
                        todo.tasks = []
                        break
            elif user_file_choice == 3:
                break
            print("BYE BYE !")
            print()

system()