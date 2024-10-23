def get_multiplied_digits(number):
    # Преобразуем число в строку для работы с его цифрами
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Берем первую цифру и преобразуем её в целое число
        first = int(str_number[0])
        # Умножаем первую цифру на результат рекурсивного вызова
        return first * get_multiplied_digits(int(str_number[1:]))

    # Если осталась одна цифра, возвращаем её
    return int(str_number[0])


# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
