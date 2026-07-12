#!/usr/bin/env python3
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-s", "--set-task", type=str, help="Назначить задачу")
parse.add_argument("-g", "--get-task", action="store_true", help="Получить текущую задачу")
parse.add_argument("-c", "--close-task", action="store_true", help="Закрыть задачу")
parse.add_argument("-r", "--remove-task", action="store_true", help="Удалить задачу")

args_user = vars(parse.parse_args())
args_user = {key: val for key, val in args_user.items() if val not in [False, None]}

if len(args_user) > 1:
    print("Нельзя указывать два флага в одной команде")
    exit()
elif len(args_user) < 1:
    print("Укажите один из флагов. Подробнее gitfocus --help")
    exit()
if args_user.get("set_task"):
    with open("problem.txt", "r+") as file:
        task = file.readline().replace("Problem:", "").strip()
    if task:
        print("У вас уже есть задача для смены сначало удалите затем добавьте")
    else:
        with open("problem.txt", "w") as file:
            file.write(f"Problem: {args_user['set_task']}\n")

elif args_user.get("get_task"):
    with open("problem.txt", "r") as file:
        task = file.readline()
        task = task.replace("Problem: ", "").strip()
    print(task)
elif args_user.get("close_task") or args_user.get("remove_task"):
    if args_user.get("close_task"):
        print("Поздравляю с успешным закрытием задачи!")
    else:
        if input("Вы действительно хотите УДАЛИТЬ задачу? [Y/n]: ").lower() == "n":
            exit()
    with open("problem.txt", "w") as file:
        file.write(f"Problem: \n")
