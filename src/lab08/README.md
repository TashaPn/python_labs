# Лабораторная работа 8
## ООП в Python: @dataclass Student, методы и сериализация
### Задание A : Реализовать класс Student (models.py)

```python
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    fio: str                  # ФИО студента
    birthdate: str            # Формат YYYY-MM-DD
    group: str                # Группа, напр. SE-01
    gpa: float                # Средний балл 0…5

    def age(self) -> int:
        '''
        количество прожитых дней = дата рождения - текущая дата
        количество прожитых лет = количество прожитых дней / 365.25 (потому что бывают високосные года)
        int(количество прожитых лет)
        '''
        now = datetime.now()
        birthday = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = now - birthday
        result = int(age.days/365.25)
        return result
    
    def __str__(self) -> str:
        """
        красиво выводит значения, когда класс печатают на print
        """
        return f"{self.fio} {self.group} {self.gpa}" 
    
    def __post_init__(self):
        """
        Этот метод используется для проверки полей класса
        """
        if 0>self.gpa or self.gpa>5:
            raise ValueError("значение gpa должно быть от 0 до 5 включительно")
        
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")

        except ValueError:
            raise ValueError("неверный формат даты рождения, должен быть YYYY-MM-DD")
        
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "gpa": self.gpa,
            "group": self.group,
        }

    @classmethod
    def from_dict(cls, student_data):
        """
        В student_data нам передают словарь такого вида

        {
            "fio": "vasya",
            "birthdate": "2020-10-20",
            "group": "SE-09",
            "gpa": 4.321,
        }

        Наша задача вернуть из классметода экземпляр класса в котором поля класса заполнены так же, как в том словаре,
        который нам передали

        Для этого мы из первой переменной классметода cls делаем экземпляр класса
        Потом накидываем ему в поля то, что лежит в дикте
        Потом возвращаем экземпляр класса из классметода

        Что такое экземпляр класса ?
        Ответ:

        когда мы делаем s = Student()
        в s попадает экземпляр класса
        """

        f = student_data["fio"]
        b = student_data["birthdate"]
        gr = student_data["group"]
        gp = student_data["gpa"]

        result = cls(f, b, gr, gp)
        return result
```

![](/images/Lab_08/models1.png)
![](/images/Lab_08/models2.png)
![](/images/Lab_08/models3.png)


### Задание B : Реализовать модуль serialize.py

```python
import json

from pathlib import Path
from src.lab08.models import Student

def students_to_json(students, path):
    """
    TBD To be done
    """
    data = [s.to_dict() for s in students]

    file_p = Path(path)

    with file_p.open("w") as fp:

        json.dump(data, fp, ensure_ascii=False, indent=2)


student1 = Student("Petr", "1982-11-24", "SE-01", 4)
student2 = Student("Vasya", "1982-12-22", "SE-02", 2.22)

Students = [student1, student2]
students_to_json(Students, "src/lab08/students_output.json")


def students_from_json(path):
    """
    TBD
    """
    file_p = Path(path)

    with file_p.open("r") as fp:

        studen_dicts = json.load(fp)
        result = []

        for one_student_dict in studen_dicts:
            new_student = Student.from_dict(one_student_dict)
            result.append(new_student)
        
    return result
```

![](/images/Lab_08/serialize1.png)
![](/images/Lab_08/serialize2.png)


### Результаты тестов и работы программы

```python
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
```

![](/images/Lab_08/test_lab08.png)
