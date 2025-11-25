# Лабораторная работа 6
## Задание 1 (Подкоманды в одном CLI)
### Подкоманды cat и stats
### Код

```python
import argparse

from pathlib import Path
from lib.text import *

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input",dest="fname", required=True)
    cat_parser.add_argument("-n", action="store_true",dest="flag", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", dest="fname", required=True)
    stats_parser.add_argument("--top", type=int, dest="number", default=5)

    args = parser.parse_args()
   
    
    if args.command == "cat":
        """ Реализация команды cat """

        file_path = args.fname
        path = Path(file_path)
        num = 0

        try:
            with path.open("r") as fp:
                strings_in_file = fp.readlines()
        except:
             print("Не могу открыть файл")

        for i in strings_in_file:
            num+=1
            if args.flag==True:
                print(num,")", i, end="")
            else:
                print(i, end="")


    elif args.command == "stats":
        """ Реализация команды stats """

        file_path = args.fname
        path = Path(file_path)

        file_data = ""
        try:
            with path.open("r") as fp:
                file_data = fp.read()

        except:
            print("Не могу открыть файл")
        
        norm_f = normalize(file_data)
        tokens = tokenize(norm_f)
        freqs = count_freq(tokens)
        topn = top_n(freqs, args.number)

        for i in topn:
            print(f"{i[0]}: {i[1]}")
        

main()
```

### Результат/вывод 
![](/images/Lab_06/samples_lab06_stats_or_cat.png "исходный файл")
![](/images/Lab_06/out_lab06_stats.png "результат подкоманды stats")
![](/images/Lab_06/out_lab06_cat.png "результат подкоманды cat")

## Задание 2 (CLI‑конвертер)
### Подкоманды json2csv, csv2json и csv2xlsx
### Код

```python
import argparse

from lab05.json_csv import *
from lab05.csv_to_xlsx import *


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", help="Доступные подкоманды для работы с файлами")

    # ========================================================
    p1 = sub.add_parser("json2csv", help="конвертирует файл json -> csv")
    p1.add_argument("--in", dest="input", required=True, help="путь до файла который мы конвертируем")
    p1.add_argument("--out", dest="output", required=True, help="путь до файла куда мы сохраняем конвертированный файл")
    # ========================================================

    # ========================================================
    p2 = sub.add_parser("csv2json", help="конвертирует файл csv -> json")
    p2.add_argument("--in", dest="input", required=True, help="путь до файла который мы конвертируем")
    p2.add_argument("--out", dest="output", required=True, help="путь до файла куда мы сохраняем конвертированный файл")
    # ========================================================

    # ========================================================
    p3 = sub.add_parser("csv2xlsx", help="конвертирует файл csv -> xlsx")
    p3.add_argument("--in", dest="input", required=True, help="путь до файла который мы конвертируем")
    p3.add_argument("--out", dest="output", required=True, help="путь до файла куда мы сохраняем конвертированный файл")
    # ========================================================

    args = parser.parse_args()
   

    if args.cmd == "json2csv":
        
        json_to_csv(args.input, args.output)
    
    elif args.cmd == "csv2json":
        
        csv_to_json(args.input, args.output)
    
    elif args.cmd == "csv2xlsx":
        
        csv_to_xlsx(args.input, args.output)

main()
```

### Результат/вывод 
![](/images/Lab_06/json2csv_1.png "json2csv")
![](/images/Lab_06/json2csv_2.png "json2csv")
![](/images/Lab_06/json2csv_3.png "json2csv")

![](/images/Lab_06/csv2json_1.png "csv2json")
![](/images/Lab_06/csv2json_2.png "csv2json")
![](/images/Lab_06/csv2json_3.png "csv2json")

![](/images/Lab_06/csv2xlsx_1.png "csv2xlsx")
![](/images/Lab_06/csv2xlsx_2.png "csv2xlsx")
![](/images/Lab_06/csv2xlsx_3.png "csv2xlsx")