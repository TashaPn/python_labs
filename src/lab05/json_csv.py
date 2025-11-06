import json
from lab04.io_txt_csv import write_csv

from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    
    p = Path(json_path)

    # Загрузка напрямую из файла    
    fp = p.open("r", encoding= "utf-8")

    json_f = None
    try:
        json_f = json.load(fp)
    except json.decoder.JSONDecodeError:
        raise ValueError("пустой/неверный JSON")
    
    csv_file = []
    
    for i in json_f:
        name = i["name"]
        age = i["age"]
        city = i["city"]
        
        csv_file.append([name, age, city])
    
    write_csv(csv_file, csv_path, ["Name","Age","City"]) 



json_to_csv("data/lab05/samples/people_empty.json","data/lab05/persons2.csv")

