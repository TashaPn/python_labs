def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError.
    """
    result = []
    
    if len(mat)==0:
        return []
    
    check_len = len(mat[0])  # длина строки
    height = len(mat)        # всего строк в матрице

    for m in mat:
        if len(m)!=check_len:
            raise ValueError


    for i in range(check_len):
        result.append([])
        for j in range(height):
            result[i].append(0)
    
    for i in range(check_len):
        for j in range(height):
            result[i][j] = mat[j][i]

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждой строке. Требуется прямоугольность.
    """
    result = []

    if len(mat)==0:
        return []
    
    check_len = len(mat[0])  # длина строки
    height = len(mat)        # всего строк в матрице

    for m in mat:
        if len(m)!=check_len:
            raise ValueError
    
    for i in mat:
        summ = 0
        for j in i:
            summ+=j
        result.append(summ)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Сумма по каждому столбцу. Требуется прямоугольность.
    """
    result = row_sums(transpose(mat))

    return result
