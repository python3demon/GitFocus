<div align="center">
<img src="logo.png" alt="Logo" width="200">

[![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-red.svg)](https://github.com/python3demon/GitFocus)
[![Python 3.12+](https://img.shields.io/badge/Python-3.14-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Platform Linux](https://img.shields.io/badge/Platform-Linux-FCC624.svg?logo=linux&logoColor=black)](https://www.kernel.org/)

<h1>GitFocus — CLI-инструмент для борьбы с хаосом</h1>
</div>

## План разработки (To-Do):
- [x] Добавить базовые флаги для добавления, получения, закрытия, удаления задачи: -s, -g, -c, -r (`v0.0.1-beta`)
- [x] Изменить названия флагов на более корректные (`v0.1.0-alpha`)
- [x] Добавить дополнительную проверку на наличие уже поставленной задачи в флаг -s (`v0.1.1-alpha`)
- [x] Поменять флаги на подкоманды (`v1.0.0-alpha`)
- [ ] Переписать скрипт с парадигмой ООП (`v1.0.1-alpha`)
## Использование
### Под-команды
```text
set                 Назначить задачу
get                 Получить текущую задачу
close               Закрыть задачу
remove              Удалить задачу

-h, --help          Показать эти команды
```
### Пример использования
```bash
# Переход в рабочую область
cd projects/ToDoListApp

# Получение помощи
gitfocus --help

# Установка задачи, чтобы не забывать, зачем открыл файл проекта
gitfocus set "Исправить баг с кнопкой help в шапке приложения и добавить новую кнопку"

# Поняли, что задачу надо разделить
gitfocus remove

# По новой установили задачи...
gitfocus set "..."

# Работа...
code .

# Отошли попить чай и, вернувшись, прописали команду для получения текущей задачи
gitfocus get

# Закончив работу
gitfocus close
```
## Установка (Linux)
```bash
# Клонируйте репозиторий и перейдите в директорию проекта:
git clone https://github.com/python3demon/GitFocus.git && cd GitFocus/

# Скопируйте скрипт в локальную директорию бинарников и сделайте скрипт исполняемым
cp gitfocus.py ~/.local/bin/gitfocus && chmod +x ~/.local/bin/gitfocus

# Добавьте путь в переменные окружения и обновите конфигурацию:
# Для zshrc:
echo 'export PATH="HOME/.local/bin:PATH"' >> ~/.zshrc && source ~/.zshrc

# Для bash:
echo 'export PATH="HOME/.local/bin:PATH"' >> ~/.bashrc && source ~/.bashrc
```
Готово! Теперь вы можете вызывать скрипт из любой папки командой `gitfocus`.
## Стек Технологий
* **Language:** Python 3.12+
* **Library:** argparse
