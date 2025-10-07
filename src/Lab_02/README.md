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

![](images/Lab_02/TESTS_1.png "блок A")