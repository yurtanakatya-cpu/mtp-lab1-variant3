# Лабораторная работа №1 — Git

Юрченко Екатерина Валентиновна, группа 221341, вариант 3.

## Задания варианта

- Среднее №3: добавить файл и сделать коммит.
- Среднее №5: создать ветку `feature` и добавить в ней новый файл.
- Среднее №9: отправить изменения на GitHub.
- Повышенное №3: создать Pull Request.
- Повышенное №7: создать релиз с тегом на GitHub.

## Запуск

Нужен Python 3. Запуск из корня репозитория:

```bash
python main.py
```

Для передачи имени можно указать его аргументом: `python main.py Git`.

## Проверка

```bash
python -m unittest discover -s tests -v
```

## GitHub

- [Pull Request №1: ветка feature в main](https://github.com/yurtanakatya-cpu/mtp-lab1-variant3/pull/1).
- [Релиз v1.0](https://github.com/yurtanakatya-cpu/mtp-lab1-variant3/releases/tag/v1.0).

История изменений: `git log --oneline --graph --decorate --all`.
