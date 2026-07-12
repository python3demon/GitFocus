# GitFocus

<div align="center">

GitFocus — CLI-инструмент для борьбы с хаосом в коммитах и потерей фокуса.

[![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-red.svg)](https://github.com/python3demon/GitFocus)
[![Python 3.12+](https://img.shields.io/badge/Python-3.14-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Platform Linux](https://img.shields.io/badge/Platform-Linux-FCC624.svg?logo=linux&logoColor=black)](https://www.kernel.org/)

</div>


## План разработки (To-Do):
- [x] Добавить базовые флаги для добавления, получения, закрытия, удаления задачи: -s, -g, -c, -r (`v0.0.1-beta`)
- [x] Изменить названия флагов на более корректные (`v0.1.0-alpha`)
- [x] Добавить дополнительную проверку на наличие уже поставленной задачи в флаг -s (`v0.1.1-alpha`)
- [x] Поменять флаги на под команды (`v1.0.0-alpha`)
- [ ] Переписать скрипт с парадигмой ООП (`v1.0.1-alpha`)

## Использование
Программу нужно запускать хотябы с одним из флагов:
```args
-h, --help                  show this help message and exit
-s, --set_task SET_TASK     Назначить задачу
-g, --get_problem           Получить текущую задачу
-c, --close_task            Закрыть задачу
-r, --remove_task           Удалить задачу	
```

```bash
# Переход в рабочу область
cd projects/ToDoListApp

# Получение помощи
gitfocus --help

# Установка задачи, чтобы не забывать зачем открыл файл проекта
gitfocus --set_task "Исправить баг с кнопкой help в шапке приложения и добавления новой кнопки в шапке"

# Поняли что задачу надо разделить
gitfocus --remove_task

# По новой установили задачи...

# Работа...
code .

# Отошли попить чай и вернувшись прописали команду для получения текущей задачи
gitfocus --get_problem

# Закончив работу
gitfocus --close_task
```

## Установка (Linux)
```bash
# Клонируйте репозиторий и перейдите в директорию проекта:
git clone https://github.com/python3demon/GitFocus.git && cd GitFocus/

# Скопируйте скрипт в локальную директорию бинарников и сделайте скрипт исполняемым
cp gitfocus.py ~/.local/bin/gitfocus && chmod +x ~/.local/bin/gitfocus

# Добавьте путь в переменные окружения и обновите конфигурацию:
# Для zshrc:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc

# Для `bash`:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
```
Готово! Теперь вы можете вызывать скрипт из любой папки командой `gitfocus`.

## Стек Технологий
* **Language:** Python 3.14+
* **Library:** argparse
