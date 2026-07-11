import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-s", "--set", type=str, help="Назначить задачу")
parse.add_argument("-g", "--get_problem", type=str, help="Получить текущую задачу")
parse.add_argument("-c", "--close_task", action="store_true", help="Закрыть задачу")
parse.add_argument("-r", "--remove_task", action="store_true", help="Удалить задачу")

args_user = vars(parse.parse_args())
args_user = {key: val for key, val in args_user.items() if val not in [False, None]}

if len(args_user) > 1:
    print("Нельзя указывать два флага в одной команде")
    exit()
elif len(args_user) < 1:
    print("Укажите один из флагов. Подробнее gitfocus --help")

if args_user.get("p"):
    with open("problem.txt", "w") as file:
        file.write(f"Problem: {args_user.p}")
elif args_user.get("g"):
    with open("problem.txt", "a") as file:
        task = file.readline(f"Problem: {args_user.p}").replace("Problem: ", "")
    print(task)
    exit()
elif args_user.get("c") or args_user.get("r"):
    if args_user.get("c"):
        print("Поздравляю с успешным закрытием задачи!")
    else:
        if input("Вы действительно хотите УДАЛИТЬ задачу? [Y/n]: ").lower() == "n":
            exit()
    with open("problem.txt", "w") as file:
        file.write(f"Problem: ")
    exit()
    
