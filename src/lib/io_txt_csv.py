import csv
from pathlib import Path
from typing import Iterable, Sequence
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку 
    + обработка ошибок + возможность выбора кодировки
    """

    file_data = ""
    with open(file=path, mode="r", encoding=encoding) as fp:
        file_data = fp.read()
        return file_data
    

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создать/перезаписать CSV с разделителем "," + Если передан header, записать его первой строкой 
    + Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError)
    """
     
    p = Path(path)
    rows = list(rows)
    
    if rows:
        expected_length = len(rows[0])
        for r in rows:
            if len(r) != expected_length:
                raise ValueError("Все строки должны иметь одинаковую длину")
            
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f,  delimiter=',')
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)




