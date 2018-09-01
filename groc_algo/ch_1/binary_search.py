def binary_search(list, item):
    """
    Функция binary_search получает отсортированный массив и значение.
    Если значение присутствует в массиве, то функция возвращает его позицию.
    """

    low = 0
    high = len(list) - 1

    while high >= low:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
