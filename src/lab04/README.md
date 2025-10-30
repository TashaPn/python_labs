# Лабораторная работа 4
## Задание A
### Мини‑тесты (ручные, для README)
```python
from lib.io_txt_csv import read_text, write_csv

txt = read_text("src/data/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "src/data/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)
```
![](/images/Lab_04/mini_test1_A.png "ручной мини-тест")
![](/images/Lab_04/mini_test2_A.png "вывод мини-теста")

## Задание B
### Скрипт src/lab04/text_report.py
```python
from pathlib import Path

from lib.io_txt_csv import read_text
from lib.text import *


def text_report(path: str | Path):
    p = read_text(path)

    norm = normalize(p)
    token = tokenize(norm)
    print("Всего слов:", len(token))

    check = count_freq(token)
    print("Уникальных слов:", len(check))

    top = top_n(check)
    print("Топ-5:")

    for element in top:
        print(element[0], ":", element[1])
    
text_report("src/data/input.txt")
```
![](/images/Lab_04/test_1B.png "скрипт")
![](/images/Lab_04/test_2B.png "тест")
