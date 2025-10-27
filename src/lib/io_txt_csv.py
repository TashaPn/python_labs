from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    file_data = ""
    with open(file=path, mode="r", encoding=encoding) as fp:
        file_data = fp.read()
        return file_data
    

print(read_text(encoding="koi8-r", path="src/test_data/1-koi8-r.txt"))
print("="*20)
print(read_text("src/test_data/1-cp1251.txt", "cp1251"))
print("="*20)
print(read_text("src/test_data/1.txt"))
