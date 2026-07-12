#!/usr/bin/env python3
import argparse
parse = argparse.ArgumentParser()
subparsers = parse.add_subparsers(dest="command")

add_command = subparsers.add_parser("set", help="Назначит задачу")
add_command.add_argument("task", type=str, help="Описание задачи")

subparsers.add_parser("get", help="Получить текущую задачу")
subparsers.add_parser("close", help="Закрыть задачу")
subparsers.add_parser("remove", help="Удалить задачу")

args_user = parse.parse_args()

if args_user.command == "set":
    with open("problem.txt", "r+") as file:
        task = file.readline().replace("Problem:", "").strip()
    if task:
        print("У вас уже есть задача для смены сначало удалите затем добавьте")
    else:
        with open("problem.txt", "w") as file:
            file.write(f"Problem: {args_user.task}\n")

elif args_user.command == "get":
    with open("problem.txt", "r") as file:
        task = file.readline()
        task = task.replace("Problem: ", "").strip()
elif args_user.command == "close" or args_user.command == "remove":
    if args_user.command == "close":
        print("Поздравляю с успешным закрытием задачи!")
    else:
        if input("Вы действительно хотите УДАЛИТЬ задачу? [Y/n]: ").lower() == "n":
            exit()
    with open("problem.txt", "w") as file:
        file.write(f"Problem: \n")
