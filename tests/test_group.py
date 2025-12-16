import pytest

from src.lab08.models import Student
from src.lab09.group import Group


@pytest.fixture
def students():
    """
    Магия pytest - фикстура
    Пишем функцию, которая что-то возвращает
    Сверху пишем декоратор @pytest.fixture
    Потом можем использовать имя этой функции как аргумент в любой другой ТЕСТОВОЙ функции
    РАБОТАЕТ ТОЛЬКО В ТЕСТАХ !!!
    То, что возвращает функция, прилетит в другую ТЕСТОВУЮ функцию в аргументе
    """
    students_result = [
        Student(fio="Иванов Иван", birthdate="2003-10-10", group="БИВТ-21-1", gpa=4.3),
        Student(fio="Петров Петр", birthdate="2005-12-07", group="БИВТ-25-2", gpa=3.5),
        Student(fio="Иванов Иван", birthdate="2004-01-12", group="БИВТ-22-3", gpa=4.5),
    ]
    return students_result


@pytest.fixture
def gr():
    gr = Group("data/lab09/students.csv")
    return gr


def test_group_list(students, gr):
    result = gr.list()
    assert students == result


def test_method_add(students, gr):
    new_student = Student(
        fio="Зинаида Фекловна", birthdate="1904-04-01", group="БИВТ-21-1", gpa=5.0
    )
    gr.add(new_student)
    students.append(new_student)
    assert students == gr.list()


def test_method_find(gr):
    find_fio = "Иван"
    result = gr.find(find_fio)
    assert result == [
        Student(fio="Иванов Иван", birthdate="2003-10-10", group="БИВТ-21-1", gpa=4.3),
        Student(fio="Иванов Иван", birthdate="2004-01-12", group="БИВТ-22-3", gpa=4.5),
    ]


def test_method_remove(gr):
    gr.remove("Петров Петр")
    assert gr.list() == [
        Student(fio="Иванов Иван", birthdate="2003-10-10", group="БИВТ-21-1", gpa=4.3),
        Student(fio="Иванов Иван", birthdate="2004-01-12", group="БИВТ-22-3", gpa=4.5),
    ]


def test_method_update(gr):
    gr.update("Иванов Иван", birthdate="2001-01-01", group="БИВТ-25-5", gpa=2.1)
    assert gr.list() == [
        Student(fio="Иванов Иван", birthdate="2001-01-01", group="БИВТ-25-5", gpa=2.1),
        Student(fio="Петров Петр", birthdate="2005-12-07", group="БИВТ-25-2", gpa=3.5),
        Student(fio="Иванов Иван", birthdate="2004-01-12", group="БИВТ-22-3", gpa=4.5),
    ]


def test_bad_file():
    with pytest.raises(ValueError):
        Group("data/lab09/students-bad.csv")


def test_bad_student():
    with pytest.raises(ValueError):
        Group("data/lab09/students-bad-2.csv")
