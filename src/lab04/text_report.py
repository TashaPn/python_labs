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
