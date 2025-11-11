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

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for strochka in result:
        ws.append(strochka)
    
    wb.save(xlsx_path)

