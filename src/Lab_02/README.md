# Лабораторная работа 2
## ЗАДАНИЕ A - ARRAYS.PY

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    min_max: Вернуть кортеж (минимум, максимум). Если список пуст — ValueError
    """
    if len(nums) == 0:
        raise ValueError

    mini = min(nums)
    maxi = max(nums)

    return (mini, maxi)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Вернуть отсортированный список уникальных значений (по возрастанию).
    """
    unique = set(nums)
    unique_result = sorted(unique)
    
    return unique_result

def flatten(nums: list[list | tuple]) -> list:
    """
    «Расплющить» список списков/кортежей в один список по строкам (row-major).
    Если встретилась строка/элемент, который не является списком/кортежем — TypeError.
    """
    result = []
    for i in nums:
        if type(i)==str:
            raise TypeError
        result += i 

    return result
```

```python
from arrays import min_max, unique_sorted, flatten


def test_min_max():

    tests = [
        [
            [3, -1, 5, 5, 0],
            (-1, 5),
        ],
        [
            [42],
            (42, 42),
        ],
        [
            [-5, -2, -9],
            (-9, -2)
        ],
        [
            [1.5, 2, 2.0, -3.1],
            (-3.1, 2),
        ],
    ]

    for t in tests:
        test_input = t[0]
        test_result = t[1]

        result = min_max(test_input)
        if result != test_result:
            print("Test failed, input=", test_input, "test_result=", test_result, "result=", result)
        else:
            print("Test passed, input=", test_input, "test_result=", test_result, "result=", result)


def test_min_max_error():
    try:  # ловушка для исключения (рейза)
        min_max([])
    except ValueError:
        print("Test passed, ValueError")



def test_unique_sorted():
    tests = [
        [
            [3, 1, 2, 1, 3], 
            [1, 2, 3],
        ],
        [
            [],
            [],
        ],
        [
            [-1, -1, 0, 2, 2],
            [-1, 0, 2],
        ],
        [
            [1.0, 1, 2.5, 2.5, 0],
            [0, 1.0, 2.5]
        ],

    ]

    for t in tests:
        start_unique = t[0]
        result_unique = t[1]
        result = unique_sorted(start_unique)

        if result == result_unique:
            print("Test passed, input=", start_unique, "result=", result_unique)
        else:
            print("Test failed, input=", start_unique, "result=", result, "result_unique=", result_unique)

 
def test_flatten():
     
    tests = [
        [
            [[1, 2], [3, 4]],
            [1, 2, 3, 4],
        ],
        [
            [[1, 2], (3, 4, 5)],
            [1, 2, 3, 4, 5],
        ],
        [
            [[1], [], [2, 3]],
            [1, 2, 3],
        ],
        
    ]

    for t in tests:
        input_flatten = t[0]
        result_flatten = t[1]

        result = flatten(input_flatten)
        if result == result_flatten:
            print("Test passed, input=", input_flatten,"result=", result_flatten)
        else:
            print("Test failed, input=", input_flatten, "result=", result, "result_flatten=", result_flatten)


def test_flatten_error():
    try: 
        flatten([[1, 2], "ab"])
    except TypeError:
        print("Test passed")
    else:
        print("Test failed")


print("TEST MIN-MAX")
test_min_max()
test_min_max_error()

print("TEST UNIQUE-SORTED")
test_unique_sorted()

print("TEST FLATTEN")
test_flatten()
test_flatten_error()


```

![](/images/Lab_02/TESTS_1.png "блок A")

## ЗАДАНИЕ B - MATRIX.PY

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError.
    """
    result = []
    
    if len(mat)==0:
        return []
    
    check_len = len(mat[0])  # длина строки
    height = len(mat)        # всего строк в матрице

    for m in mat:
        if len(m)!=check_len:
            raise ValueError


    for i in range(check_len):
        result.append([])
        for j in range(height):
            result[i].append(0)
    
    for i in range(check_len):
        for j in range(height):
            result[i][j] = mat[j][i]

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждой строке. Требуется прямоугольность.
    """
    result = []

    if len(mat)==0:
        return []
    
    check_len = len(mat[0])  # длина строки
    height = len(mat)        # всего строк в матрице

    for m in mat:
        if len(m)!=check_len:
            raise ValueError
    
    for i in mat:
        summ = 0
        for j in i:
            summ+=j
        result.append(summ)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждому столбцу. Требуется прямоугольность.
    """
    result = row_sums(transpose(mat))

    return result

```
```python
from matrix import transpose, row_sums, col_sums


def test_transpose():
    tests = [
        [
            [[1, 2, 3]],
            [[1], [2], [3]],
        ],
        [
            [[1], [2], [3]],
            [[1, 2, 3]],
        ],
        [
            [[1, 2], [3, 4]],
            [[1, 3], [2, 4]],
        ],
        [
            [],
            [],
        ],
    ]

    for t in tests:
        input_transpose = t[0]
        result_transpose = t[1]
        result = transpose(input_transpose)

        if result == result_transpose :
            print("Test passed, input=", input_transpose, "result=", result_transpose)
        else:
            print("Test failed, input=", input_transpose, "result=", result, "result_transpose=", result_transpose)


def test_transpose_error():
    try:
        transpose([[1, 2], [3]])
    except ValueError:
        print("Test passed, ValueError")
    else:
        print("Test failed")


def test_row_sums():
    tests = [
        [
            [[1, 2, 3], [4, 5, 6]],
            [6, 15],
        ],
        [
            [[-1, 1], [10, -10]],
            [0, 0],
        ],
        [
            [[0, 0], [0, 0]],
            [0, 0],
        ],
    ]

    for t in tests:
        input_row_sums = t[0]
        result_row_sums = t[1]
        result = row_sums(input_row_sums)

        if result == result_row_sums :
            print("Test passed, input=", input_row_sums, "result=", result_row_sums)
        else:
            print("Test failed, input=", input_row_sums, "result=", result, "result_transpose=", result_row_sums)


def test_error_row_sums():
    try:
        row_sums([[1, 2], [3]])
    except ValueError:
        print("Test passed, ValueError")
    else:
        print("Test failed")


def test_col_sums():
    tests = [
        [
            [[1, 2, 3], [4, 5, 6]],
            [5, 7, 9],
        ],
        [
            [[-1, 1], [10, -10]],
            [9, -9],
        ],
        [
            [[0, 0], [0, 0]],
            [0, 0],
        ],
    ]

    for t in tests:
        test_input = t[0]
        test_result = t[1]
        result = col_sums(test_input)

        if result == test_result :
            print("Test passed, input=", test_input, "result=", test_result)
        else:
            print("Test failed, input=", test_input, "result=", result, "result_transpose=", test_result)


def test_error_col_sums():
    try:
        col_sums([[1, 2], [3]])
    except ValueError:
        print("Test passed, ValueError")
    else:
        print("Test failed")


print("TEST TRANSPOSE")
test_transpose()
test_transpose_error()
print("TEST ROW_SUMS")
test_row_sums()
test_error_row_sums()
print("TEST COL_SUMS")
test_col_sums()
test_error_col_sums()
```
![](/images/Lab_02/TESTS_2.png "блок A")

## ЗАДАНИЕ C - TUPLES.PY

```python
def format_record(rec: tuple[str, str, float]) -> str:
    """
    Работаем с «записями» как с кортежами
    
    Вызывает ValueError при пустом значении ФИО или группы
    Вызывает TypeError при неверном типе (не float) GPA
    """
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    if fio=="" or group=="":
        raise ValueError
    if type(gpa)!=float:
        raise TypeError

    fio = fio.split()

    for n in range(len(fio)):
        s = fio[n]
        s = s.capitalize()

        if n > 0:
            s = f"{s[0]}."

        fio[n] = s
    
    name = fio[0]
    surname = "".join(fio[1:])

    return f"{name} {surname}, гр. {group}, GPA {gpa:.2f}"
```

```python
from tuples import format_record


def test_format_record():
    tests = [
        [
            ("Иванов Иван Иванович", "BIVT-25", 4.6),
            "Иванов И.И., гр. BIVT-25, GPA 4.60",
        ],
        [
            ("Петров Пётр", "IKBO-12", 5.0),
            "Петров П., гр. IKBO-12, GPA 5.00",
        ],
        [
            ("Петров Пётр Петрович", "IKBO-12", 5.0),
            "Петров П.П., гр. IKBO-12, GPA 5.00",
        ],
        [
            ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
            "Сидорова А.С., гр. ABB-01, GPA 4.00",
        ],
    ]

    for t in tests:
        input_record = t[0]
        result_record = t[1]
        result = format_record(input_record)

        if result == result_record:
            print("Test passed, input=", input_record, "result=", result_record)
        else:
            print("Test failed, input=", input_record, "result=", result,"result_record=", result_record)


def test_format_record_value_error():
    try:
        format_record(("", 'IKBO-12', 5.0))
    except ValueError:
        print("Test Passed: value error")
    else:
        print("Test Failed: value error")

    try:
        format_record(("Иванов Иван Иванович", '', 5.0))
    except ValueError:
        print("Test Passed: value error")
    else:
        print("Test Failed: value error")


def test_format_record_type_error():
    try:
        format_record(("Иванов Иван Иванович", 'IKBO-12', "5.0"))
    except TypeError:
        print("Test Passed: type error")
    else:
        print("Test Failed: type error")


print("TEST FORMAT-RECORD")
test_format_record()
test_format_record_value_error()
test_format_record_type_error()
```
![](/images/Lab_02/TESTS_3.png "блок A")