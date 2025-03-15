# Список чисел для распределения по четным и нечетным
numbers = [2, 5, 7, 7, 8, 4, 1, 6]

# Инициализируем пустые списки для четных и нечетных чисел (ИСПРАВЛЕНО)
odd = []
even = []

# Проходим по каждому числу в списке numbers
for number in numbers:
    # Проверяем, является ли число четным
    if number % 2 == 0:
        even.append(number)  # Если четное, добавляем в список even
    else:
        odd.append(number)  # Если нечетное, добавляем в список odd

# Выводим списки четных и нечетных чисел
print("Четные числа:", even)
print("Нечетные числа:", odd)
