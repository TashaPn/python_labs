import pytest

from src.lab05.json_csv import *
from src.lab05.csv_to_xlsx import *


def test_convert_csv_to_json():  # проверка на работу функций
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/persons.json")


def test_convert_json_to_csv():
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/persons.csv")


def test_convert_csv_to_xlsx():
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")


def test_convert_bad_csv_to_json():  # проверка на ошибку неправильного файла
    with pytest.raises(FileNotFoundError):
        csv_to_json("data/lab05/samples/bad-people.csv", "data/lab05/out/persons.json")


def test_convert_bad_json_to_csv():
    with pytest.raises(FileNotFoundError):
        json_to_csv("data/lab05/samples/bad-people.json", "data/lab05/out/persons.csv")


def test_convert_bad_csv_to_xlsx():
    with pytest.raises(FileNotFoundError):
        csv_to_xlsx("data/lab05/samples/bad-cities.csv", "data/lab05/out/cities.xlsx")


def test_convert_empty_csv_to_json():  # проверка на ошибку пустого файла
    with pytest.raises(ValueError):
        csv_to_json("data/lab05/samples/empty_file.txt", "data/lab05/out/persons.json")


def test_convert_empty_json_to_csv():
    with pytest.raises(ValueError):
        json_to_csv("data/lab05/samples/empty_file.txt", "data/lab05/out/persons.csv")


def test_convert_empty_csv_to_xlsx():
    with pytest.raises(ValueError):
        csv_to_xlsx("data/lab05/samples/empty_file.txt", "data/lab05/out/cities.xlsx")


def test_convert_invalid_csv_to_json():  # проверка на ошибку неверного файла
    with pytest.raises(ValueError):
        csv_to_json("data/lab05/samples/invalid.csv", "data/lab05/out/persons.json")


def test_convert_invalid_json_to_csv():
    with pytest.raises(ValueError):
        json_to_csv("data/lab05/samples/invalid.json", "data/lab05/out/persons.csv")


def test_convert_invalid_csv_to_xlsx():
    with pytest.raises(ValueError):
        csv_to_xlsx("data/lab05/samples/invalid-csv.xlsx", "data/lab05/out/cities.xlsx")
