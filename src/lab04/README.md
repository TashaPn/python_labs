# Лабораторная работа 4
## Задание A
### Мини‑тесты (ручные, для README)
```python
from src.lib.io_txt_csv import read_text, write_csv

txt = read_text("src/data/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "src/data/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)
```
![](/images/Lab_04/mini_test1_A.png "ручной мини-тест")
![](/images/Lab_04/mini_test2_A.png "вывод мини-теста")
