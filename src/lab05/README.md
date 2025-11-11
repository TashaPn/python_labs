# Лабораторная работа 5
## Задание A
### Тесты для функций json_to_csv и csv_to_json

```python
import json
import csv

from lab04.io_txt_csv import write_csv
from pathlib import Path

from pathlib import Path

def convert_json_to_csv(j: list) -> list:
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

def convert_csv_to_json(csv_input:list)-> list:
    """
    csv_input - массив массивов, например:
    
    csv_input = [
    ["33","22","11"],
    ["3","2","1"],
    ["один", "два", "три"]
    ]
    
    в таком примере, result будет таким:
    
    result = [
    {"33": "3",
     "22": "2",
     "11": "1",
    },
    {"33": "один",
     "22": "два",
     "11": "один"
    },
    ]
    """
    result = [] #конвертированный файл
    stolbiki = csv_input[0]  #  ["33","22","11"]

    slovar = {}                         # пустой
    
    for strochka in csv_input[1:]:      # ["3","2","1"] потом ["один", "два", "три"]
        slovar = {}
        for i in range(len(strochka)):   
            slovar[stolbiki[i]] = strochka[i] 
        
        result.append(slovar)

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
    
    massive = None
    try:
        massive = convert_json_to_csv(json_f)
    except:
        raise ValueError
    
    write_csv(massive, csv_path)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    """
    p = Path(csv_path)
    r = Path(json_path)
    fp = p.open('r')
    rf = r.open('w')
    csv_input = csv.reader(fp)

    result = [] 

    for i in csv_input:
        result.append(i)
    
    if len(result)==0:
        raise ValueError

    try:
        slovar = convert_csv_to_json(result)
    except:
        raise ValueError

    json.dump(slovar, rf, indent=2)

```
### Код 
![](/images/Lab_05/A1.png "json_to_csv")
![](/images/Lab_05/A2.png "json_to_csv")
![](/images/Lab_05/A3.png "csv_to_json")
![](/images/Lab_05/A4.png "csv_to_json")

### Результат/вывод 
![](/images/Lab_05/json_to_csv.png "persons.csv")
![](/images/Lab_05/csv_to_json.png "persons.json")

## Задание B
### Тесты для функции csv_to_xlsx

```python
import csv

from openpyxl import Workbook
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    p = Path(csv_path)
    fp = p.open('r')

    csv_input = csv.reader(fp)

    result = []

    for i in csv_input:
        result.append(i)

    if len(result)==0:
        raise ValueError
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for strochka in result:
        ws.append(strochka)
    
    wb.save(xlsx_path)
```

### Код
![](/images/Lab_05/B1.png "csv_to_xlsx")

### Результат/вывод 
![](/images/Lab_05/csv_to_xlsx.png "cities.xlsx")