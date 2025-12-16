from src.lab02.arrays import min_max, unique_sorted, flatten


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
        [[-5, -2, -9], (-9, -2)],
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
            print(
                "Test failed, input=",
                test_input,
                "test_result=",
                test_result,
                "result=",
                result,
            )
        else:
            print(
                "Test passed, input=",
                test_input,
                "test_result=",
                test_result,
                "result=",
                result,
            )


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
        [[1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5]],
    ]

    for t in tests:
        start_unique = t[0]
        result_unique = t[1]
        result = unique_sorted(start_unique)

        if result == result_unique:
            print("Test passed, input=", start_unique, "result=", result_unique)
        else:
            print(
                "Test failed, input=",
                start_unique,
                "result=",
                result,
                "result_unique=",
                result_unique,
            )


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
            print("Test passed, input=", input_flatten, "result=", result_flatten)
        else:
            print(
                "Test failed, input=",
                input_flatten,
                "result=",
                result,
                "result_flatten=",
                result_flatten,
            )


def test_flatten_error():
    try:
        flatten([[1, 2], "ab"])
    except TypeError:
        print("Test passed")
    else:
        print("Test failed")
