import sys
import csv

def read_text():
    return sys.stdin.read()     # ввод через эхо

def write_csv(data):
    writer = csv.writer(sys.stdout)         # записывает в консоль в формате csv
    writer.writerow(['word', 'count'])      # также записывает но списком (в два столбика)
    for word, count in data:                # создает для каждого слова отдельную строку
        writer.writerow([word, count])