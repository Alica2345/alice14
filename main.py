class Task:
    def init(self, name, description, deadline, status="не выполнено"):
        self.name = "Д/З"
        self.description = "Задание в учебнике"
        self.deadline = "2024-12-3"
        self.status = "не виполнено"

class TaskManager:
    def init(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_as_completed(self, task):
        task.status = "выполнено"

    def print_tasks(self):
        for task in self.tasks:
            print(f"Название: {task.name}, Описание: {task.description}, Дедлайн: {task.deadline}, Статус: {task.status}")

task_manager = TaskManager()

task1 = Task("Сделай дз", "напиши єто в тетради и здай", "2024-12-3")

task_manager.add_task(task1)

task_manager.print_tasks()