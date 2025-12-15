# Лабораторная работа 8
## «База данных» на CSV: класс Group, CRUD-операции и CLI
### Задание A : Реализовать класс Group

```python
import csv

from pathlib import Path
from src.lab08.models import Student


class Group:

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)

        # Если файла по пути path нет, мы его создаем
        if not self.path.exists():
            self._ensure_storage_exists(self.path)

        self.students = []
        self._read_all()

    def _ensure_storage_exists(self, path):
        """
        Создаём новый csv-файл по пути path и пишем в него нужный заголовок
        """
        with path.open("w", newline="", encoding="utf-8") as fp:
            w = csv.writer(fp, delimiter=",")
            header = ["fio","birthdate","group","gpa"]
            w.writerow(header)

    def _read_all(self):
        """
        Преобразовывает файл csv по пути self.path
        все строчки кроме первой преобразует в обьект Student
        заполняет поле self.students созданнами обьектами Student

        """
        fp = self.path.open("r")
        csv_file_content = csv.reader(fp)

        tmp_students = []

        for stroka in csv_file_content:
            tmp_students.append(stroka)

        # Вот здесь проверяем, что первая строка файла tmp_students содержит заголовок
        # Если нет, raise ValueError

        if tmp_students[0] != ["fio","birthdate","group","gpa"]:
            raise ValueError("неправильный формат файла")

        for student_data in tmp_students[1:]:

            fio = student_data[0]
            birthdate = student_data[1]
            group = student_data[2]
            gpa = float(student_data[3])
            
            student = Student(fio, birthdate, group, gpa)
            self.students.append(student)
  
    def list(self):
        """
        функция возвращает список студентов
        """
        return self.students

    def add(self, student: Student):
        """
        добавляет студента student в поле self.students
        """
        self.students.append(student)

    def find(self, substr: str):
        """
        находит студентов по substr и добавляет их в список
        """
        result = []
        for s in self.students:
            if substr in s.fio:
                result.append(s)

        return result
                   

    def remove(self, fio: str):
        """
        удаляет студента из списка self.student по введённому фио
        """
        for i, r in enumerate(self.students):
            if r.fio == fio:
                self.students.pop(i)
                break

    def update(self, fio: str, **fields):
        """
        заменяет у первого студента найденного по fio все поля значениями из словаря fields
        """
        for student in self.students:
            if student.fio == fio:
                if "birthdate" in fields:
                    student.birthdate = fields["birthdate"]
                if "group" in fields:
                    student.group = fields["group"]
                if "gpa" in fields:
                    student.gpa = fields["gpa"]
                break
```

![](/images/Lab_09/group1.png)
![](/images/Lab_09/group2.png)
![](/images/Lab_09/group3.png)
![](/images/Lab_09/group4.png)

### Результаты тестов и работы программы

```python
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
        Student(fio='Иванов Иван', birthdate='2003-10-10', group='БИВТ-21-1', gpa=4.3),
        Student(fio='Петров Петр', birthdate='2005-12-07', group='БИВТ-25-2', gpa=3.5), 
        Student(fio='Иванов Иван', birthdate='2004-01-12', group='БИВТ-22-3', gpa=4.5),
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
    new_student = Student(fio='Зинаида Фекловна', birthdate='1904-04-01', group='БИВТ-21-1', gpa=5.0)
    gr.add(new_student)
    students.append(new_student)
    assert students == gr.list()

def test_method_find(gr):
    find_fio = "Иван"
    result = gr.find(find_fio)
    assert result == [
        Student(fio='Иванов Иван', birthdate='2003-10-10', group='БИВТ-21-1', gpa=4.3), 
        Student(fio='Иванов Иван', birthdate='2004-01-12', group='БИВТ-22-3', gpa=4.5),
        ]

def test_method_remove(gr):
    gr.remove("Петров Петр")
    assert gr.list() == [
        Student(fio='Иванов Иван', birthdate='2003-10-10', group='БИВТ-21-1', gpa=4.3), 
        Student(fio='Иванов Иван', birthdate='2004-01-12', group='БИВТ-22-3', gpa=4.5),
        ] 

def test_method_update(gr):
    gr.update("Иванов Иван", birthdate='2001-01-01', group='БИВТ-25-5', gpa=2.1)
    assert gr.list() == [
        Student(fio='Иванов Иван', birthdate='2001-01-01', group='БИВТ-25-5', gpa=2.1),
        Student(fio='Петров Петр', birthdate='2005-12-07', group='БИВТ-25-2', gpa=3.5), 
        Student(fio='Иванов Иван', birthdate='2004-01-12', group='БИВТ-22-3', gpa=4.5),
    ]

def test_bad_file():
    with pytest.raises(ValueError):
        Group("data/lab09/students-bad.csv")

def test_bad_student():
    with pytest.raises(ValueError):
        Group("data/lab09/students-bad-2.csv")
```

![](/images/Lab_09/input_tests.png)
![](/images/Lab_09/test_lab09.png)