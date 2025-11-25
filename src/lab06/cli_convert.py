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