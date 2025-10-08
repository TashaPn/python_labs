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