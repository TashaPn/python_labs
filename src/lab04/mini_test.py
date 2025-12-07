from lab04.io_txt_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt")  # должен вернуть строку
f_csv = write_csv(
    [("word", "count"), ("test", 3)], "data/lab04/check.csv"
)  # создаст CSV

print(txt)
print("=" * 20)
print(f_csv)
