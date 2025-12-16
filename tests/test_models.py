import pytest

from src.lab08.models import Student


def test_invalid_date():
    with pytest.raises(ValueError):
        Student("Petr", "098765", "SE-01", 4)


def test_invalid_gpa():
    with pytest.raises(ValueError):
        Student("Petr", "2003-05-12", "SE-01", 456)


def test_age():
    inpput = Student("Petr", "1982-11-24", "SE-01", 4)
    assert inpput.age() == 43


def test_str():
    inpput = Student("Petr", "1982-11-24", "SE-01", 4)

    assert f"{inpput}" == "Petr SE-01 4"


def test_to_dict():
    inpput = Student("Petr", "1982-11-24", "SE-01", 4)
    result = {
        "fio": "Petr",
        "birthdate": "1982-11-24",
        "gpa": 4,
        "group": "SE-01",
    }
    assert inpput.to_dict() == result


def test_from_dict():
    student_dt = {
        "fio": "vasya",
        "birthdate": "2013-03-05",
        "group": "se-04",
        "gpa": 3.222,
    }

    b = Student.from_dict(student_dt)
    assert b.fio == "vasya"
    assert b.birthdate == "2013-03-05"
    assert b.group == "se-04"
    assert b.gpa == 3.222
