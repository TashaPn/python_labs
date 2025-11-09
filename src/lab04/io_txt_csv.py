import csv

from pathlib import Path



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку 
    + обработка ошибок + возможность выбора кодировки (что бы выбрать другую кодировку , нужно ввести
    другой вид кодировки, например: encoding="cp1251")
    """
    p = Path(path)

    file_data = ""
    with p.open("r", encoding=encoding) as fp:
        file_data = fp.read()
        return file_data
    

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Создать/перезаписать CSV с разделителем "," + Если передан header, записать его первой строкой 
    + Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError)

    rows: массив с массивами, в котором лежит данные для таблицы csv
    path: путь до файла, в который надо написать данные

    необязательный параметр
    header: первая строка в csv с названием колонок
    """
     
    p = Path(path)
    
    if rows:
        expected_length = len(rows[0])
        for r in rows:
            if len(r) != expected_length:
                raise ValueError("Все строки должны иметь одинаковую длину")
            
    with p.open("w", newline="", encoding="utf-8") as fp:
        w = csv.writer(fp,  delimiter=',')
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)




