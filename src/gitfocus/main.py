import argparse
import json

TASK_FILE = ".gitfocus.json"

class TaskManager:
    def __init__(self, name_file):
        self.name_file = name_file
        self.data = self._read_task()
    
    def _read_task(self) -> dict[str, list]:
        try:
            with open(self.name_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {"tasks": []}

    def _save(self):
        with open(self.name_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def clear_task(self):
        try:
            del self.data["tasks"][-1]
            self._save()
        except IndexError:
            return

    def get_tasks(self) -> list[str]:
        return self.data["tasks"]

    def set_task(self, text):
        self.data["tasks"].append(text)
        self._save()

def main():
    parse = argparse.ArgumentParser()
    subparsers = parse.add_subparsers(dest="command")

    add_command = subparsers.add_parser("set", help="Назначить задачу")
    add_command.add_argument("task", type=str, help="Описание задачи")

    subparsers.add_parser("get", help="Получить текущую задачу")
    subparsers.add_parser("close", help="Закрыть задачу")
    subparsers.add_parser("remove", help="Удалить задачу")

    args_user = parse.parse_args()

    manager = TaskManager(TASK_FILE)
    if args_user.command == "set":
        manager.set_task(args_user.task)
    elif args_user.command == "get":
        if manager.get_tasks():
            print(manager.get_tasks()[-1])
        else:
            print("У вас нет ни одной задачи!")
    elif args_user.command == "close" or args_user.command == "remove":
        if not manager.get_tasks():
            print("У вас нет задач")
        elif args_user.command == "close":
            manager.clear_task()
            print("Поздравляю с успешным закрытием задачи!")
        else:
            if input("Вы действительно хотите УДАЛИТЬ задачу? [Y/n]: ").lower() == "y":
                manager.clear_task()
