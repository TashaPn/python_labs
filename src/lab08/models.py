from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    fio: str  # ФИО студента
    birthdate: str  # Формат YYYY-MM-DD
    group: str  # Группа, напр. SE-01
    gpa: float  # Средний балл 0…5

    def age(self) -> int:
        """
        количество прожитых дней = дата рождения - текущая дата
        количество прожитых лет = количество прожитых дней / 365.25 (потому что бывают високосные года)
        int(количество прожитых лет)
        """
        now = datetime.now()
        birthday = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = now - birthday
        result = int(age.days / 365.25)
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
        if 0 > self.gpa or self.gpa > 5:
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
