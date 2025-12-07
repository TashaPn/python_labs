def format_record(rec: tuple[str, str, float]) -> str:
    """
    Работаем с «записями» как с кортежами

    Вызывает ValueError при пустом значении ФИО или группы
    Вызывает TypeError при неверном типе (не float) GPA
    """
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if fio == "" or group == "":
        raise ValueError
    if type(gpa) != float:
        raise TypeError

    fio = fio.split()

    for n in range(len(fio)):
        s = fio[n]
        s = s.capitalize()

        if n > 0:
            s = f"{s[0]}."

        fio[n] = s

    name = fio[0]
    surname = "".join(fio[1:])

    return f"{name} {surname}, гр. {group}, GPA {gpa:.2f}"
