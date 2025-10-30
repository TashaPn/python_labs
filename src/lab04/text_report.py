import sys

from pathlib import Path

from lab04.io_txt_csv import read_text, write_csv
from lib.text import *


def text_report(path: str | Path = None, encoding: str = "utf-8"):
    """
    Читает один входной файл data/input.txt + Нормализует текст (lib/text.py), токенизирует и считает частоты слов 
    + Сохраняет data/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве)
    + В консоль печатает краткое резюме + если путь пустой -> выводим только заголовок в созданный файл

    Аргументы:
    path - путь к файлу
    enciding - кодировка
    """
    if path == None:
        write_csv([],"data/lab04/report.csv", header=("word", "count"))
        return
    
    p = read_text(path, encoding=encoding)

    norm = normalize(p)
    token = tokenize(norm)
    print("Всего слов:", len(token))

    check = count_freq(token)
    print("Уникальных слов:", len(check))

    top = top_n(check, n=len(check))

    rows = []
    for element in top:
        rows.append((element[0], element[1]))

    rows = sorted(rows, key=lambda n: n[0])
    rows = sorted(rows, key=lambda n: n[1], reverse=True)

    write_csv(rows, "data/lab04/report.csv", header=("word", "count"))

    print("Топ-5:")
    for element in top[:5]:
        print(element[0], ":", element[1])


try:
    #text_report("data/lab04/input-cp1251.txt", encoding="cp1251")
    text_report("data/lab04/input.txt", encoding="utf-8")


except FileNotFoundError as E:
    print("Файл не найден", E)
    sys.exit(1)

sys.exit(0)
