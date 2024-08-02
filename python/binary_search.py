def binary_search(list, item):
    low = 0     # Минимальная граница, в которой выполняется поиск
    high = len(list) - 1    # максимальная граница, в которой выполняется поиск

    while low <= high:  # Пока эта часть не сократится до одного элемента
        mid = (low + high) // 2  # Проверяем средний элемент
        guess = list[mid]
        if guess == item:   # Если значение найдено
            return mid
        if guess > item:    # Если значение больше нужного
            high = mid - 1
        else:   # Если значение меньше нужного
            low = mid + 1
    return None # Значение не существует

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
