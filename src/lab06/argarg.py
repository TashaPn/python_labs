import sys
import argparse

from pathlib import Path

def c1():
    print(1)

def c2():
    print(2)

def c3():
    print(3)   

# 1 - сделали парсер (всегда одинаково)
parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")


# 2 - сабпарсеры (мелкие парсеры) - всегда пиши так, не думая

sub = parser.add_subparsers(dest="cmd")

# 3 - заполняем сабпарсеры
p1 = sub.add_parser("json2csv")
p1.add_argument("--in", dest="input", required=True)
p1.add_argument("--out", dest="output", required=True)

p2 = sub.add_parser("csv2json")
p2.add_argument("--in", dest="input", required=True)
p2.add_argument("--out", dest="output", required=True)

p3 = sub.add_parser("csv2xlsx")
p3.add_argument("--in", dest="input", required=True)
p3.add_argument("--out", dest="output", required=True, type=int)

p4 = sub.add_parser("jopa")
p4.add_argument("-f","--file", dest="fname", required=True, type=str)



args = parser.parse_args()


if args.cmd == "json2csv":
    c1()

if args.cmd == "csv2json":
    c2()


if args.cmd == "jopa":
    file_path = args.fname
    path = Path(file_path)
    with path.open("r") as fp:
        soderjanka = fp.read()
    print(soderjanka)