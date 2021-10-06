# """
# Домашнее задание №1
# Функции и структуры данных
# """

#
# def power_numbers():
#     """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     >>> power_numbers(1, 2, 5, 7)
#     <<< [1, 4, 25, 49]
#     """
def power_numbers(numbers):
    result = []
    for i in numbers:
        # print(i)
        square = i ** 2
        result.append(square)
    return result


N = ([1, 2, 5, 7])
print(power_numbers(N))
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


# def filter_numbers():
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     # >>> filter_numbers([1, 2, 3], ODD)
#     # <<< [1, 3]
#     # >>> filter_numbers([2, 3, 4, 5], EVEN)
#     # <<< [2, 4]
#     # """
def filter_numbers(list_of_numbers, tip):
    # print(tip)
    elements = []
    for num in list_of_numbers:
        if tip == ODD:
            if num % 2 != 0:
                # print(num, "Это  не четное число")
                elements.append(num)

        elif tip == EVEN:
            if num % 2 == 0:
                # print(num, "Это четное число")
                elements.append(num)

        elif tip == PRIME:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        # print(num, "Это не простое число")
                        break
                else:
                    # print(num, "Это   простое число")
                    elements.append(num)
            # else:
            #     print(num, "Это не простое число")
        else:
             print("Type Error")

    return elements
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filter_numbers(list, PRIME))
print(filter_numbers(list, ODD))
print(filter_numbers(list, EVEN))
