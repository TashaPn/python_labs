from src.lab05.json_csv import *
from src.lab05.csv_to_xlsx import *


csv_to_json("data/lab05/samples/people.csv","data/lab05/out/persons.json")
json_to_csv("data/lab05/samples/people.json","data/lab05/out/persons.csv")

csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")