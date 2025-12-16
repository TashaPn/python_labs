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
