from src.lib.io_txt_csv import read_text, write_csv

txt = read_text("src/data/input.txt")  # должен вернуть строку
f_csv = write_csv([("word","count"),("test",3)], "src/data/check.csv")  # создаст CSV

print(txt)
print("="*20)
print(f_csv)
