from lab04.io_txt_csv import write_csv

csv_file = [
    ["aaa", "bbb"],
    ["ccc", "ddd"],
    ["zzz","xxx"],
    ["vvv","qqq"]
    
]

csv_name = "text.csv"

f_csv = write_csv(csv_file, "data/lab04/text.csv",["AAA","ZZZ"])  