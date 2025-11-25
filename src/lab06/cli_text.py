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

