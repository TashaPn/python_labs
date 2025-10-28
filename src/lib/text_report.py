from src.lib.io_txt_csv import read_text, write_csv
from src.lib.text import *

def text_report(path: str | Path, encoding: str = "utf-8"):
    p = read_text(path, encoding="utf-8")

    norm = normalize(p)
    token = tokenize(norm)
    print("Всего слов:", len(token))

    check = count_freq(token)
    print("Уникальных слов:", len(count))

    top = top_n(count)
    print("Топ-5:")

    for element in top:
        print(element[0], ":", element[1])
    

    