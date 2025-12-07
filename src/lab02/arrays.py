def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    min_max: Вернуть кортеж (минимум, максимум). Если список пуст — ValueError
    """
    if len(nums) == 0:
        raise ValueError

    mini = min(nums)
    maxi = max(nums)

    return (mini, maxi)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Вернуть отсортированный список уникальных значений (по возрастанию).
    """
    unique = set(nums)
    unique_result = sorted(unique)

    return unique_result


def flatten(nums: list[list | tuple]) -> list:
    """
    «Расплющить» список списков/кортежей в один список по строкам (row-major).
    Если встретилась строка/элемент, который не является списком/кортежем — TypeError.
    """
    result = []
    for i in nums:
        if type(i) == str:
            raise TypeError
        result += i

    return result
