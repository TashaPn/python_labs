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

