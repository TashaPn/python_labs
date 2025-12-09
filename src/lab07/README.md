# Лабораторная работа 7
## Тестирование: pytest + стиль (black)
### Тесты для src/lib/text.py
### normalize
```python
from src.lib.text import normalize


def test_normalize_1():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"


def test_normalize_2():
    assert normalize("ёжик, Ёлка", yo2e=True) == "ежик, елка"


def test_normalize_3():
    assert normalize("Hello\r\nWorld") == "hello world"


def test_normalize_4():
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
```

![](/images/Lab_07/normalize.PNG "тесты normalize")

### tokenize
```python
from src.lib.text import tokenize


def test_tokenize_1():
    assert tokenize("привет, мир!") == ["привет", "мир"]


def test_tokenize_2():
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]


def test_tokenize_3():
    assert tokenize("2025 год") == ["2025", "год"]


def test_tokenize_4():
    assert tokenize("hello,world!!!") == ["hello", "world"]


def test_tokenize_5():
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]
```

![](/images/Lab_07/tokenize.PNG "тесты tokenize")

### count_freq
```python
from src.lib.text import count_freq


def test_count_freq_1():
    assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def test_count_freq_2():
    assert count_freq(["bb", "aa", "bb", "aa", "cc"]) == {"aa": 2, "bb": 2, "cc": 1}
```

![](/images/Lab_07/count_freq.PNG "тесты count_freq")

### top_n
```python
from src.lib.text import top_n


def test_top_n_1():
    assert top_n({"a": 2, "b": 3, "c": 1}, n=2) == [("b", 3), ("a", 2)]


def test_top_n_2():
    assert top_n({"aa": 2, "bb": 2, "cc": 1}, n=2) == [("aa", 2), ("bb", 2)]
```

![](/images/Lab_07/top_n.PNG "тесты top_n")

### Тесты для src/lab05/json_csv.py
```python
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

```
## Проверка покрытия функций

![](/images/Lab_07/test%20s%20pokr.png "покрытие")

## Проверка кода на стиль black

![](/images/Lab_07/black.png "стиль black")

## Проверка исправности тестов

![](/images/Lab_07/tests.PNG "проверка тестов")