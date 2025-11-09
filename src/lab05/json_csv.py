import json
from lab04.io_txt_csv import write_csv

from pathlib import Path

def convert(j: list) -> list:
    """
    Переводит данные, которые считали из json в формат для csv
    """
    result = []
    result1 = []   # заголовок таблицы

    slovar = j[0]
    if type(slovar)!= dict:
        raise ValueError
    
    for key in slovar:
        result1.append(key)
        
    result.append(result1)
    
    # result == [
    #     ["A", "B", "C", "D"],  # заголовок
    # ]

    
    for s in j:
        if type(s)!= dict:
            raise ValueError
        result2 = []
        for key in result1:
            value = s.get(key)
            if value == None:
                value = ""
            result2.append(value)
        result.append(result2)
 
    return result


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).

    json_path: путь до файла на диске, из которого мы читаем данные в формате json
    csv_path: путь до файла на диске, в который мы пишем данные в фомате csv
    """
    
    p = Path(json_path)

    # Загрузка напрямую из файла    
    fp = p.open("r", encoding= "utf-8")

    json_f = None
    try:
        json_f = json.load(fp)
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    
    massive = convert(json_f)
    write_csv(massive, csv_path)


json_to_csv("data/lab05/samples/people_invalid.json","data/lab05/persons2.csv")

