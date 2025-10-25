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